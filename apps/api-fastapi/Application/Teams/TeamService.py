from Models.Teams import OfficialName, Team, Abbreviation, ManagementCorporation
from Models.HomeTowns import Prefecture, City, HomeTown
from Application.unit_of_work import IUnitOfWork
from Application.HomeTowns import HomeTownService

class TeamsService:

    uow : IUnitOfWork

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow


    def create(self, offical_team_name, team_abbreviation, team_prefecuture, team_city, team_management_corporation) -> Team.Team :
        with self.uow as uow:
            official_name = OfficialName.OfficialName(offical_team_name)
            
            abbreviation = Abbreviation.Abbreviation(team_abbreviation)
            
            home_town = HomeTownService.create_hometown(
                team_prefecuture,
                team_city,
                uow.city_masters,
            )
            
            management_corporation = ManagementCorporation.ManagementCorporation(team_management_corporation)
            
            team = Team.Team(official_name, abbreviation, home_town, management_corporation)
            
            uow.teams.add(team)
            uow.flush()
            uow.refresh(team)

            return team
        
    def find_all(self):
        with self.uow as uow:
            return uow.teams.list()
        
    def find_by_id(self, team_id : int) -> Team.Team | None :
        with self.uow as uow:
            team = uow.teams.get_by_id(team_id)
            return team
