from backend.Models.Teams.OfficialName import OfficialName
from backend.Models.Teams.Abbreviation import Abbreviation
from backend.Models.HomeTowns.HomeTown import HomeTown
from backend.Models.HomeTowns.Prefecture import Prefecture
from backend.Models.HomeTowns.City import City
from backend.Models.Teams.ManagementCorporation import ManagementCorporation

class Team:
    
    team_id : int
    official_name : str
    abbreviation : str
    home_town_prefecture : str
    home_town_city : str
    management_corporation : str

    def __init__(
        self,
        official_name : OfficialName,
        abbreviation : Abbreviation,
        home_town : HomeTown,
        management_corporation : ManagementCorporation,
        team_id=None,
    ):
        if team_id is not None and not isinstance(team_id, int):
            raise TypeError("チームIDは整数で指定してください。")
        self.team_id = team_id
        self.official_name = official_name.offical_name if isinstance(official_name, OfficialName) else official_name
        self.abbreviation = abbreviation.abbreviation if isinstance(abbreviation, Abbreviation) else abbreviation
        self.home_town_prefecture = home_town.prefecture.prefecture
        self.home_town_city = home_town.city.city
        self.management_corporation = (
            management_corporation.management_corporation
            if isinstance(management_corporation, ManagementCorporation)
            else management_corporation
        )

    @property
    def home_town(self) -> HomeTown:
        prefecture = Prefecture(self.home_town_prefecture)
        city = City(prefecture, self.home_town_city)
        return HomeTown(prefecture, city)
