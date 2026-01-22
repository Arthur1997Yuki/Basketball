from Models.TeamAffiliations.TeamAffiliation import TeamAffiliation
from Models.TeamAffiliations.ITeamAffiliationRepository import ITeamAffiliationRepository
from sqlalchemy.orm import Session
from sqlalchemy import select

class TeamAffiliationRepository(ITeamAffiliationRepository):

    session : Session

    def __init__(self, session : Session):
        self.session = session

    def add(self, team_affiliation : TeamAffiliation) -> None :
        self.session.add(team_affiliation)

    def list(self) -> list[TeamAffiliation]:
        return list(self.session.scalars(select(TeamAffiliation)).all())