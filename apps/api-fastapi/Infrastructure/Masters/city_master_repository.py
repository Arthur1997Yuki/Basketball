import csv
from functools import lru_cache
from pathlib import Path
from Infrastructure.Masters.normalization import norm_name
from Application.HomeTowns.ICityMasterRepository import ICityMasterRepository

@lru_cache(maxsize=1)
def load_city_names_by_pref2(csv_path: str) -> dict[str, set[str]]:
    path = Path(csv_path)
    if not path.exists():
        raise RuntimeError(f"市区町村マスタCSVが見つかりません: {csv_path}")

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise RuntimeError("CSVヘッダが読めません。")

        code_candidates = [
            "標準地域コード", 
            "市区町村コード", "市町村コード", "団体コード", "code"
        ]
        name_candidates = [
            "市区町村", 
            "市区町村名", "市町村名", "団体名", "name"
        ]

        def pick(cands):
            for c in cands:
                if c in reader.fieldnames:
                    return c
            return None

        code_col = pick(code_candidates)
        name_col = pick(name_candidates)
        if not code_col or not name_col:
            raise RuntimeError(f"CSV列名が想定外です: {reader.fieldnames}")

        m: dict[str, set[str]] = {}
        for row in reader:
            code = (row.get(code_col) or "").strip()
            name = (row.get(name_col) or "").strip()
            if not code or not name:
                continue
            pref2 = code[:2]
            m.setdefault(pref2, set()).add(norm_name(name))

        return m


DEFAULT_CSV_PATH = Path(__file__).resolve().parents[2] / "Resources" / "municipalities.csv"


class CityMasterRepository(ICityMasterRepository):
    def __init__(self, csv_path: str | Path = DEFAULT_CSV_PATH) -> None:
        self.csv_path = str(csv_path)

    def get_city_names_by_pref2(self, pref2: str) -> set[str] | None:
        city_map = load_city_names_by_pref2(self.csv_path)
        return city_map.get(pref2)
