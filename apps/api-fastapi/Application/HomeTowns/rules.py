TOKYO_PREF2 = "13"

def check_granularity(pref2: str, city_name: str) -> None:
    if pref2 != TOKYO_PREF2:
        if "区" in city_name:
            raise ValueError("東京都以外は区までの指定は不可です。市までで入力してください。")
    else:
        # 東京都は区までOK（23区）
        # 将来「東京都は区のみ」にしたいなら以下を有効化
        # if not city_name.endswith("区"):
        #     raise ValueError("東京都は23区（◯◯区）で入力してください。")
        pass
