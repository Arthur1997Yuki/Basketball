from pydantic import BaseModel


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
