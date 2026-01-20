from backend.Infrastructure.unit_of_work import UnitOfWork
from backend.Models.TeamAffiliations.Conference import Conference
from backend.Models.TeamAffiliations.ConferenceName import ConferenceName

class ConferenceService:

    uow : UnitOfWork

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def create(self, conference_name) :
        
        with self.uow as uow:
            conference = Conference(ConferenceName(conference_name))

            uow.conferences.add(conference)
            uow.session.flush()
            uow.session.refresh(conference)

            return conference

    def find_all(self) -> list[Conference] :
        with self.uow as uow:
            conferences = uow.conferences.list()
            return conferences