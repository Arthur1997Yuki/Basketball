from Application.unit_of_work import IUnitOfWork
from Models.TeamAffiliations.Conference import Conference
from Models.TeamAffiliations.ConferenceName import ConferenceName

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

    def find_by_id(self, conference_id : int) -> Conference | None :
        with self.uow as uow:
            conference = uow.conferences.get_by_id(conference_id)
            return conference