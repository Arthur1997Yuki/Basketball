from backend.Models.TeamAffiliations.Conference import Conference
from backend.Models.TeamAffiliations.IConferenceRepository import IConferenceRepository
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
