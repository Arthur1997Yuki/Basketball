from Models.Seasons.Season import Season
from Models.Seasons.ISeasonRepository import ISeasonRepository
from sqlalchemy.orm import Session
from sqlalchemy import select

class SeasonRepository(ISeasonRepository):

    session : Session

    def __init__(self, session : Session) :
        self.session = session

    def add(self, season : Season) -> None :
        self.session.add(season)

    def list(self) -> list[Season] :
        return self.session.scalars(select(Season)).all()
    
    def get_by_id(self, id: int) -> Season | None:
        return self.session.get(Season, id)