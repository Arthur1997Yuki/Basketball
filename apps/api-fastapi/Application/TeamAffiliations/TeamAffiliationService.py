from Application.unit_of_work import IUnitOfWork
from Models.TeamAffiliations.TeamAffiliation import TeamAffiliation
from Models.TeamAffiliations.Conference import Conference
from Models.TeamAffiliations.Division import Division
from Models.Seasons.Season import Season
from Models.Teams.Team import Team

class TeamAffiliationService:
    uow : IUnitOfWork

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def create(self, team_id, division_id, conference_id, season_id) -> TeamAffiliation :
        
        with self.uow as uow:
            team = uow.teams.get_by_id(team_id)
            division = uow.divisions.get_by_id(division_id)
            conference = uow.conferences.get_by_id(conference_id)
            season = uow.seasons.get_by_id(season_id)

            team_affiliation = TeamAffiliation(team, division, conference, season)

            uow.team_affiliations.add(team_affiliation)
            uow.flush()
            uow.refresh(team_affiliation)

            return team_affiliation

    def find_all(self) -> list[TeamAffiliation] :
        with self.uow as uow:
            team_affiliations = uow.team_affiliations.list()
            return team_affiliations
        
    def find_by_id(self, team_affiliation_id : int) -> TeamAffiliation | None :
        with self.uow as uow:
            team_affiliation = uow.team_affiliations.search_by_id(team_affiliation_id)
            return team_affiliation