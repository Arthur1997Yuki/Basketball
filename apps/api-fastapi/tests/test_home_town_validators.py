import pytest

from Application.HomeTowns.validators import ensure_city_exists


class FakeCityMasterRepository:
    def __init__(self, city_names_by_pref2: dict[str, set[str]]):
        # CSV I/O を避けるための簡易 in-memory マップ。
        self.city_names_by_pref2 = city_names_by_pref2

    def get_city_names_by_pref2(self, pref2: str) -> set[str] | None:
        # バリデータが要求するI/Fを最小限で模倣。
        return self.city_names_by_pref2.get(pref2)


def test_ensure_city_exists_raises_when_city_missing():
    # 対象の市区町村が含まれないマップを用意。
    repo = FakeCityMasterRepository({"01": {"札幌市"}})

    # マスタにない市区町村はエラーになるはず。
    with pytest.raises(ValueError):
        ensure_city_exists("01", "旭川市", repo)
