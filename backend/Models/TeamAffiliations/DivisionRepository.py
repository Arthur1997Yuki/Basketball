from backend.Models.TeamAffiliations.Division import Division
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete

class DivisionRepository:

    session : Session

    def __init__(self, session) :
        self.session = session

    def add(self, division : Division) :
        self.session.add(division)

    def list(self) -> list[Division] :
        return self.session.scalars(select(Division)).all()
