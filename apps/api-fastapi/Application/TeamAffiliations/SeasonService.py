from Application.unit_of_work import IUnitOfWork
from Models.Seasons.Season import Season
from Models.Seasons.Season import SeasonName

class SeasonService:

    uow : IUnitOfWork

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def create(self, season_name, start_date, end_date) -> Season :
        
        with self.uow as uow:
            season = Season(SeasonName(season_name), start_date, end_date)

            uow.seasons.add(season)
            uow.flush()
            uow.refresh(season)

            return season

    def find_all(self) -> list[Season] :
        with self.uow as uow:
            seasons = uow.seasons.list()
            return seasons
