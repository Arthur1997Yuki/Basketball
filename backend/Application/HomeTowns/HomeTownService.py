from backend.Models.HomeTowns.Prefecture import Prefecture
from backend.Models.HomeTowns.City import City
from backend.Models.HomeTowns.HomeTown import HomeTown
from backend.Application.HomeTowns.validators import ensure_city_exists
from backend.Application.HomeTowns.ICityMasterRepository import ICityMasterRepository

def create_city(
    prefecture: Prefecture,
    city: str,
    repo: ICityMasterRepository,
) -> City:
    # まずDomainで正規化（空チェック含む）
    tmp = City(prefecture=prefecture, city=city)

    # 次にApplicationで粒度+存在確認
    ensure_city_exists(prefecture.code2, tmp.city, repo)
    return tmp

def create_hometown(
    prefecture_name: str,
    city: str,
    repo: ICityMasterRepository,
) -> HomeTown:
    pref = Prefecture(prefecture_name)
    c = create_city(pref, city, repo)
    return HomeTown(prefecture=pref, city=c)
