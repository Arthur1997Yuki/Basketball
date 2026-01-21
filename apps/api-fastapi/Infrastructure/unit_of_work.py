from sqlalchemy.orm import Session
from Application.unit_of_work import IUnitOfWork
from Infrastructure.db import SessionLocal
from Infrastructure.Repositories.TeamRepository import TeamRepository
from Infrastructure.Repositories.DivisionRepository import DivisionRepository
from Infrastructure.Repositories.ConferenceRepository import ConferenceRepository
from Infrastructure.Masters.city_master_repository import CityMasterRepository

class UnitOfWork(IUnitOfWork):
    def __enter__(self):
        self.session: Session = SessionLocal()
        self.teams = TeamRepository(self.session)
        self.conferences = ConferenceRepository(self.session)
        self.divisions = DivisionRepository(self.session)
        self.city_masters = CityMasterRepository()
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type:
                self.rollback()
            else:
                self.commit()
        finally:
            self.session.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def flush(self) -> None:
        self.session.flush()

    def refresh(self, entity) -> None:
        self.session.refresh(entity)
