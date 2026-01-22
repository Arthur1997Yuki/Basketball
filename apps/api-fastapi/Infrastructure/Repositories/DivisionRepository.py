from Models.TeamAffiliations.Division import Division
from Models.TeamAffiliations.IDivisionRepository import IDivisionRepository
from sqlalchemy.orm import Session
from sqlalchemy import select

class DivisionRepository(IDivisionRepository):

    session : Session

    def __init__(self, session : Session) :
        self.session = session

    def add(self, division : Division) -> None :
        self.session.add(division)

    def list(self) -> list[Division] :
        return self.session.scalars(select(Division)).all()
    
    def get_by_id(self, id: int) -> Division | None:
        return self.session.get(Division, id)
