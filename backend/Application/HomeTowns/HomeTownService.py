from pathlib import Path
from backend.Models.HomeTowns.Prefecture import Prefecture
from backend.Models.HomeTowns.City import City
from backend.Models.HomeTowns.HomeTown import HomeTown
from backend.Application.HomeTowns.validators import ensure_city_exists

# このファイル(Application/HomeTowns/services.py)から見て backend/Resources を引く
BASE_DIR = Path(__file__).resolve().parents[2]  # backend/
CSV_PATH = str(BASE_DIR / "Resources"  / "municipalities.csv")

def create_city(prefecture: Prefecture, city: str) -> City:
    # まずDomainで正規化（空チェック含む）
    tmp = City(prefecture=prefecture, city=city)

    # 次にApplicationで粒度+存在確認
    ensure_city_exists(prefecture.code2, tmp.city, CSV_PATH)
    return tmp

def create_hometown(prefecture_name: str, city: str) -> HomeTown:
    pref = Prefecture(prefecture_name)
    c = create_city(pref, city)
    return HomeTown(prefecture=pref, city=c)
