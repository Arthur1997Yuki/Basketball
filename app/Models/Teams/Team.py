import OfficalName
import Models.Teams.Abbreviation as Abbreviation
import Models.HomeTowns.HomeTown as HomeTown
import ManagementCorporation

class Team:
    
    team_id : int
    offical_name : OfficalName
    acronym : Abbreviation
    home_town : HomeTown
    management_corporation : ManagementCorporation

    def __init__(self, offical_name, acronym, home_town, management_corporation, team_id=None):
        if team_id is not None and not isinstance(team_id, int):
            raise TypeError("チームIDは整数で指定してください。")
        self.team_id = team_id
        self.offical_name = offical_name
        self.acronym = acronym
        self.home_town = home_town
        self.management_corporation = management_corporation
