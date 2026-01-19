from dataclasses import dataclass
import json
import os
import urllib.error
import urllib.parse
import urllib.request
import Prefecture

PREF_CODE_BY_NAME = {
    "北海道": "01",
    "青森県": "02", "岩手県": "03", "宮城県": "04", "秋田県": "05", "山形県": "06", "福島県": "07",
    "茨城県": "08", "栃木県": "09", "群馬県": "10", "埼玉県": "11", "千葉県": "12", "東京都": "13", "神奈川県": "14",
    "新潟県": "15", "富山県": "16", "石川県": "17", "福井県": "18", "山梨県": "19", "長野県": "20",
    "岐阜県": "21", "静岡県": "22", "愛知県": "23", "三重県": "24",
    "滋賀県": "25", "京都府": "26", "大阪府": "27", "兵庫県": "28", "奈良県": "29", "和歌山県": "30",
    "鳥取県": "31", "島根県": "32", "岡山県": "33", "広島県": "34", "山口県": "35",
    "徳島県": "36", "香川県": "37", "愛媛県": "38", "高知県": "39",
    "福岡県": "40", "佐賀県": "41", "長崎県": "42", "熊本県": "43", "大分県": "44", "宮崎県": "45", "鹿児島県": "46",
    "沖縄県": "47",
}

@dataclass(frozen=True)
class City:

    prefecture : Prefecture
    city : str

    def __init__(self, prefecture, city):
        
        if type(prefecture) is not Prefecture:
            raise TypeError("引数の型が都道府県でありません")
        
        if not city:
            raise ValueError("市区町村名は必須です。")
        
        self._ensure_city_exists(prefecture, city)

        self.city = city

    @property
    def city(self) -> str :
        return self.city

    def _ensure_city_exists(self, prefecture, city):
        api_key = os.getenv("ESTAT_API_KEY")
        if not api_key:
            raise RuntimeError("ESTAT_API_KEYが未設定です。")

        pref_code = PREF_CODE_BY_NAME.get(prefecture.prefecture)
        if not pref_code:
            raise ValueError("都道府県コードが取得できません。")

        base_url = os.getenv(
            "ESTAT_API_URL",
            "https://api.e-stat.go.jp/rest/3.0/app/json/getCityList",
        )
        params = {
            "appId": api_key,
            "prefCode": pref_code,
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"

        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Basketball/1.0"})
            with urllib.request.urlopen(request, timeout=10) as response:
                if response.status != 200:
                    raise RuntimeError(f"e-Stat APIが失敗しました。status={response.status}")
                payload = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError("市町村の存在確認に失敗しました。") from exc

        city_names = _extract_city_names(payload)
        if city not in city_names:
            raise ValueError("市町村が存在しません。")


def _extract_city_names(payload):
    names = set()

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key in ("@name", "cityName", "city_name", "name") and isinstance(value, str):
                    names.add(value)
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(payload)
    return names
