from app.Models.Teams import Team, OfficalName, Abbreviation, ManagementCorporation
from app.Models.HomeTowns import Prefecture, City, HomeTown
from app.Infrastructure.unit_of_work import UnitOfWork

class TeamsService:

    uow : UnitOfWork

    def __init__(self, uow: UnitOfWork):
        self.uow = uow


    def create(self, offical_team_name, team_abbreviation, team_prefecuture, team_city, team_management_corporation) -> Team.Team :
        with self.uow as uow:
            offical_name = OfficalName.OfficalName(offical_team_name)
            
            abbreviation = Abbreviation.Abbreviation(team_abbreviation)
            
            prefecture = Prefecture.Prefecture(team_prefecuture)
            city = City.City(prefecture, team_city)
            home_town = HomeTown.HomeTown(prefecture, city)
            
            management_corporation = ManagementCorporation.ManagementCorporation(team_management_corporation)
            
            team = Team.Team(offical_name, abbreviation, home_town, management_corporation)
            
            uow.teams.add(team)
            uow.session.flush
            uow.session.refresh(team)

            return team