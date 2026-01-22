from Models.TeamAffiliations.Conference import Conference
from Models.TeamAffiliations.IConferenceRepository import IConferenceRepository
from sqlalchemy.orm import Session
from sqlalchemy import select

class ConferenceRepository(IConferenceRepository):

    session : Session

    def __init__(self, session : Session) :
        self.session = session

    def add(self, conference : Conference) -> None :
        self.session.add(conference)

    def list(self) -> list[Conference] :
        return self.session.scalars(select(Conference)).all()
    
    def get_by_id(self, id: int) -> Conference | None:
        return self.session.get(Conference, id)
