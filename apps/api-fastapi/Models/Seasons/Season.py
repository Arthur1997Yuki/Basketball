from dataclasses import dataclass
from datetime import date
from Models.Seasons.SeasonName import SeasonName

class Season:

    season_id : int
    name : str
    start_date : date
    end_date : date

    def __init__(self, season_name : SeasonName, start_date : date, end_date : date, season_id=None):
        if season_id is not None and not isinstance(season_id, int):
            raise TypeError("シーズンIDは整数で指定してください。")
        
        if not isinstance(season_name, SeasonName):
            raise TypeError("シーズン名称の型が不正です。")

        if not isinstance(start_date, date):
            raise TypeError("開始日の型が不正です。")

        if not isinstance(end_date, date):
            raise TypeError("終了日の型が不正です。")

        if start_date >= end_date:
            raise ValueError("開始日は終了日より前の日付を指定してください。")

        self.season_id = season_id
        self.name = season_name.season_name
        self.start_date = start_date
        self.end_date = end_date
