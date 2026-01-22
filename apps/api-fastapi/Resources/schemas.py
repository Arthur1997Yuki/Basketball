from pydantic import BaseModel
from datetime import date


class TeamCreateIn(BaseModel):
    official_name: str
    abbreviation: str
    prefecture: str
    city: str
    management_corporation: str


class DivisionCreateIn(BaseModel):
    name: str


class ConferenceCreateIn(BaseModel):
    name: str

class SeasonCreateIn(BaseModel):
    name: str
    start_date: date
    end_date: date
