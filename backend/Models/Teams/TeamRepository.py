from backend.Models.Teams.ITeamRepository import ITeamRepository
from backend.Models.Teams.Team import Team
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update

class TeamRepository(ITeamRepository):

    session : Session

    def __init__(self, session : Session):
        self.session = session

    def add(self, team : Team) -> None :
        self.session.add(team)

    def list(self) -> list[Team]:
        return list(self.session.scalars(select(Team)).all())
