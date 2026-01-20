from sqlalchemy.orm import Session
from backend.Infrastructure.db import SessionLocal
from backend.Models.Teams.TeamRepository import TeamRepository
from backend.Models.TeamAffiliations.DivisionRepository import DivisionRepository
from backend.Models.TeamAffiliations.ConferenceRepository import ConferenceRepository

class UnitOfWork:
    def __enter__(self):
        self.session: Session = SessionLocal()
        self.teams = TeamRepository(self.session)
        self.conferences = ConferenceRepository(self.session)
        self.divisions = DivisionRepository(self.session)
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type:
                self.session.rollback()
            else:
                self.session.commit()
        finally:
            self.session.close()
