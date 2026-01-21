from backend.Application.unit_of_work import IUnitOfWork
from backend.Models.TeamAffiliations.Conference import Conference
from backend.Models.TeamAffiliations.ConferenceName import ConferenceName

class ConferenceService:

    uow : IUnitOfWork

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def create(self, conference_name) :
        
        with self.uow as uow:
            conference = Conference(ConferenceName(conference_name))

            uow.conferences.add(conference)
            uow.flush()
            uow.refresh(conference)

            return conference

    def find_all(self) -> list[Conference] :
        with self.uow as uow:
            conferences = uow.conferences.list()
            return conferences
