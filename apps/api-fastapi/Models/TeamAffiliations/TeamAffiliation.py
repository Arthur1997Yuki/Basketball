from dataclasses import dataclass
from Models.Seasons.Season import Season
from Models.TeamAffiliations.Division import Division
from Models.TeamAffiliations.Conference import Conference
from Models.Teams.Team import Team


class TeamAffiliation:

    team_affiliation_id : int
    team_id : int
    division_id : int
    conference_id : int
    season_id : int

    def __init__(self, team : Team, division: Division, conference: Conference, season: Season, team_affiliation_id=None):

        if not isinstance(team, Team):
            raise TypeError("team must be an instance of Team")
        if not isinstance(division, Division):
            raise TypeError("division must be an instance of Division")
        if not isinstance(conference, Conference):
            raise TypeError("conference must be an instance of Conference")
        if not isinstance(season, Season):
            raise TypeError("season must be an instance of Season")
        
        if team.team_id is None:
            raise ValueError("team must have a valid team_id")
        if division.division_id is None:
            raise ValueError("division must have a valid division_id")
        if conference.conference_id is None:
            raise ValueError("conference must have a valid conference_id")
        if season.season_id is None:
            raise ValueError("season must have a valid season_id")
        
        self.division_id = division.division_id
        self.conference_id = conference.conference_id
        self.season_id = season.season_id
        self.team_id = team.team_id
        self.team_affiliation_id = team_affiliation_id