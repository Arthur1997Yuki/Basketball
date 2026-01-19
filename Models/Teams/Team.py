import OfficalName
import Models.Teams.Abbreviation as Abbreviation
import Models.HomeTowns.HomeTown as HomeTown
import ManagementCorporation

class Teams:
    
    offical_name : OfficalName
    acronym : Abbreviation
    home_town : HomeTown
    management_corporation : ManagementCorporation

    def __init__(self, offical_name, acronym, home_town, management_corporation):
        self.offical_name = offical_name
        self.acronym = acronym
        self.home_town = home_town
        self.management_corporation = management_corporation