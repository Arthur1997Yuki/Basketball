from Models.HomeTowns.Prefecture import Prefecture
from Models.HomeTowns.City import City
from Models.HomeTowns.HomeTown import HomeTown
from Application.HomeTowns.validators import ensure_city_exists
from Application.HomeTowns.ICityMasterRepository import ICityMasterRepository

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
