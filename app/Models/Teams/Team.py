import OfficalName
import Models.Teams.Abbreviation as Abbreviation
import Models.HomeTowns.HomeTown as HomeTown
import Models.HomeTowns.Prefecture as Prefecture
import Models.HomeTowns.City as City
import ManagementCorporation

class Team:
    
    team_id : int
    offical_name : OfficalName
    abbreviation : Abbreviation
    home_town_prefecture : str
    home_town_city : str
    management_corporation : ManagementCorporation

    def __init__(
        self,
        offical_name,
        abbreviation,
        home_town : HomeTown.HomeTown,
        management_corporation,
        team_id=None,
    ):
        if team_id is not None and not isinstance(team_id, int):
            raise TypeError("チームIDは整数で指定してください。")
        self.team_id = team_id
        self.offical_name = offical_name
        self.abbreviation = abbreviation
        self.home_town_prefecture = home_town.prefecture.prefecture
        self.home_town_city = home_town.city.city
        self.management_corporation = management_corporation

    @property
    def home_town(self) -> HomeTown.HomeTown:
        prefecture = Prefecture.Prefecture(self.home_town_prefecture)
        city = City.City(prefecture, self.home_town_city)
        return HomeTown.HomeTown(prefecture, city)
