import ITeamRepository
import Team
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update

class TeamRepository(ITeamRepository):

    session : Session

    def __init__(self, session : Session):
        self.session = session

    def add(self, team : Team.Team) -> None :
        self.session.add(team)

    def list(self) -> list[Team.Team]:
        return list(self.session.scalars(select(Team.Team)).all)