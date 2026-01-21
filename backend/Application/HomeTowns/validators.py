from backend.Application.HomeTowns.rules import check_granularity
from backend.Application.HomeTowns.ICityMasterRepository import ICityMasterRepository

def ensure_city_exists(
    pref2: str,
    city_name: str,
    repo: ICityMasterRepository,
) -> None:
    check_granularity(pref2, city_name)

    names = repo.get_city_names_by_pref2(pref2)
    if not names:
        raise RuntimeError(f"市区町村マスタに都道府県コードが存在しません: {pref2}")

    if city_name not in names:
        raise ValueError(f"市区町村が存在しません。pref2={pref2}, city={city_name}")
