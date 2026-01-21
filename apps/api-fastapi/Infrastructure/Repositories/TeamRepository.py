from Models.Teams.ITeamRepository import ITeamRepository
from Models.Teams.Team import Team
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

class TeamRepository(ITeamRepository):

    session : Session

    def __init__(self, session : Session):
        self.session = session

    def add(self, team : Team) -> None :
        self.session.add(team)

    def list(self) -> list[Team]:
        return list(self.session.scalars(select(Team)).all())
    
    def update(self, team_id : int, new_team : Team) -> None :
        stmt = (
            update(Team).
            where(Team.id == team_id).
            values(
                name = new_team.name,
                home_town = new_team.home_town,
                abbreviation = new_team.abbreviation
            )
        )
        self.session.execute(stmt)

    def delete(self, team_id : int) -> None :
        stmt = delete(Team).where(Team.id == team_id)
        self.session.execute(stmt)
