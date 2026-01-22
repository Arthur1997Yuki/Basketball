from Application.unit_of_work import IUnitOfWork
from Models.TeamAffiliations.Division import Division
from Models.TeamAffiliations.DivisionName import DivisionName

class DivisionService:

    uow : IUnitOfWork

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def create(self, division_name) :
        
        with self.uow as uow:
            division = Division(DivisionName(division_name))

            uow.divisions.add(division)
            uow.flush()
            uow.refresh(division)

            return division
    
    def find_all(self) -> list[Division] :
        with self.uow as uow:
            divisions = uow.divisions.list()
            return divisions

    def find_by_id(self, division_id : int) -> Division | None :
        with self.uow as uow:
            division = uow.divisions.get_by_id(division_id)
            return division