from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from Infrastructure.orm import create_tables, start_mappers
from Infrastructure.orm.base import mapper_registry
from Infrastructure.Repositories.TeamRepository import TeamRepository
from Models.HomeTowns.Prefecture import Prefecture
from Models.HomeTowns.City import City
from Models.HomeTowns.HomeTown import HomeTown
from Models.Teams.OfficialName import OfficialName
from Models.Teams.Abbreviation import Abbreviation
from Models.Teams.ManagementCorporation import ManagementCorporation
from Models.Teams.Team import Team


def _build_team() -> Team:
    # テスト用のTeamを組み立てる（値オブジェクト経由）。
    pref = Prefecture("東京都")
    city = City(pref, "新宿区")
    home_town = HomeTown(pref, city)
    return Team(
        OfficialName("Tokyo Hoopers"),
        Abbreviation("TH"),
        home_town,
        ManagementCorporation("Hoopers Inc."),
    )


def test_team_repository_add_and_get_by_id():
    # SQLite in-memory を共有接続で使い、複数セッションでも同一DBを参照できるようにする。
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
    session = SessionLocal()

    repo = TeamRepository(session)
    team = _build_team()

    repo.add(team)
    session.commit()

    loaded = repo.get_by_id(team.team_id)

    assert loaded is not None
    assert loaded.official_name == "Tokyo Hoopers"
    assert loaded.abbreviation == "TH"
    assert loaded.home_town.hometown == "東京都新宿区"
    assert loaded.management_corporation == "Hoopers Inc."
