from backend.Models.TeamAffiliations.Conference import Conference
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete

class ConferenceRepository:

    session : Session

    def __init__(self, session) :
        self.session = session

    def add(self, conference : Conference) :
        self.session.add(conference)

    def list(self) -> list[Conference] :
        return self.session.scalars(select(Conference)).all()