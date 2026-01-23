from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import app as api_app
from Infrastructure.orm import create_tables, start_mappers
from Infrastructure.orm.base import mapper_registry
from Infrastructure.uow_factory import get_uow
from Infrastructure.Repositories.TeamRepository import TeamRepository
from Application.HomeTowns.ICityMasterRepository import ICityMasterRepository
from Application.unit_of_work import IUnitOfWork


class FakeCityMasterRepository(ICityMasterRepository):
    def __init__(self, city_names_by_pref2: dict[str, set[str]]):
        self.city_names_by_pref2 = city_names_by_pref2

    def get_city_names_by_pref2(self, pref2: str) -> set[str] | None:
        return self.city_names_by_pref2.get(pref2)


class TestUnitOfWork(IUnitOfWork):
    def __init__(self, session_factory):
        self._session_factory = session_factory

    def __enter__(self):
        # 各リクエストで新しいセッションを作る。
        self.session = self._session_factory()
        self.teams = TeamRepository(self.session)
        # 今回のAPIでは未使用なのでダミーを置く。
        self.team_affiliations = None  # type: ignore[assignment]
        self.divisions = None  # type: ignore[assignment]
        self.conferences = None  # type: ignore[assignment]
        self.seasons = None  # type: ignore[assignment]
        self.city_masters = FakeCityMasterRepository({"13": {"新宿区"}})
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.session.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def flush(self) -> None:
        self.session.flush()

    def refresh(self, entity) -> None:
        self.session.refresh(entity)


def test_create_and_list_teams_via_api():
    # SQLite in-memory を共有接続で使い、テスト内で状態を保持する。
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    # マッピングは一度だけ実行する。
    if not mapper_registry.mappers:
        start_mappers()

    create_tables(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    # 起動イベントで本番DBに触れないようにする。
    api_app.start_mappers = lambda: None
    api_app.create_tables = lambda _engine: None
    api_app.engine = engine

    api_app.app.dependency_overrides[get_uow] = lambda: TestUnitOfWork(SessionLocal)

    client = TestClient(api_app.app)

    payload = {
        "official_name": "Tokyo Hoopers",
        "abbreviation": "TH",
        "prefecture": "東京都",
        "city": "新宿区",
        "management_corporation": "Hoopers Inc.",
    }

    try:
        res = client.post("/api/teams", json=payload)
        assert res.status_code == 201

        list_res = client.get("/api/teams")
        assert list_res.status_code == 200
        teams = list_res.json()

        assert len(teams) == 1
        assert teams[0]["official_name"] == "Tokyo Hoopers"
        assert teams[0]["home_town"] == "東京都新宿区"
    finally:
        # 依存オーバーライドは後片付けする。
        api_app.app.dependency_overrides.clear()
