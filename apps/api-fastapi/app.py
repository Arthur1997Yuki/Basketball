from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy import text
from Infrastructure.db import get_db, engine
from Infrastructure.uow_factory import get_uow
from Application.Teams.TeamService import TeamsService
from Application.unit_of_work import IUnitOfWork
from Resources.schemas import (
    TeamCreateIn,
    DivisionCreateIn,
    ConferenceCreateIn,
    SeasonCreateIn,
    TeamAffiliationCreateIn,
)
from Infrastructure.orm import start_mappers, create_tables
from Application.TeamAffiliations.DivisionService import DivisionService
from Application.TeamAffiliations.ConferenceService import ConferenceService
from Application.TeamAffiliations.SeasonService import SeasonService
from Application.TeamAffiliations.TeamAffiliationService import TeamAffiliationService

app = FastAPI()

@app.on_event("startup")
def on_startup():
    start_mappers()
    create_tables(engine)

def get_team_service(uow: IUnitOfWork = Depends(get_uow)) :
    return TeamsService(uow)

@app.get("/api/teams")
def list_teams(service : TeamsService = Depends(get_team_service)):
    teams = service.find_all()
    return [
        {
            "id": team.team_id,
            "official_name": team.official_name,
            "abbreviation": team.abbreviation,
            "home_town": team.home_town.hometown,
            "management_corporation": team.management_corporation,
        }
        for team in teams
    ]

@app.get("/api/teams/{team_id}")
def get_team(
    team_id: int,
    service: TeamsService = Depends(get_team_service),
):
    team = service.find_by_id(team_id)
    if not team:
        return {"error": "Team not found"}
    return {
        "id": team.team_id,
        "official_name": team.official_name,
        "abbreviation": team.abbreviation,
        "home_town": team.home_town.hometown,
        "management_corporation": team.management_corporation,
    }

@app.post("/api/teams", status_code=201)
def create_team(
    payload: TeamCreateIn,
    service: TeamsService = Depends(get_team_service),
    ):
    team = service.create(
        payload.official_name,
        payload.abbreviation,
        payload.prefecture,
        payload.city,
        payload.management_corporation,
    )
    return {"id" : team.team_id,
            "official_name" : team.official_name,
            "abbreviation" : team.abbreviation,
            "home_town" : team.home_town.hometown,
            "management_corporation" : team.management_corporation,
            }

def get_division_service(uow: IUnitOfWork = Depends(get_uow)) :
    return DivisionService(uow)

@app.get("/api/divisions")
def list_divisions(service : DivisionService = Depends(get_division_service)):
    divisions = service.find_all()
    return [
        {
            "id": division.division_id,
            "name": division.name,
        }
        for division in divisions
    ]

@app.get("/api/divisions/{division_id}")
def get_division(
    division_id: int,
    service: DivisionService = Depends(get_division_service),
):
    division = service.find_by_id(division_id)
    if not division:
        return {"error": "Division not found"}
    return {
        "id": division.division_id,
        "name": division.name,
    }

@app.post("/api/divisions", status_code=201)
def create_division(
    payload: DivisionCreateIn,
    service: DivisionService = Depends(get_division_service),
    ):
    division = service.create(
        payload.name,
    )
    return {"id" : division.division_id,
            "name" : division.name,
            }

def get_conference_service(uow: IUnitOfWork = Depends(get_uow)) :
    return ConferenceService(uow)
    
@app.get("/api/conferences")
def list_conferences(service : ConferenceService = Depends(get_conference_service)):
    conferences = service.find_all()
    return [
        {
            "id": conference.conference_id,
            "name": conference.name,
        }
        for conference in conferences
    ]

@app.get("/api/conferences/{conference_id}")
def get_conference(
    conference_id: int,
    service: ConferenceService = Depends(get_conference_service),
):
    conference = service.find_by_id(conference_id)
    if not conference:
        return {"error": "Conference not found"}
    return {
        "id": conference.conference_id,
        "name": conference.name,
    }

@app.post("/api/conferences", status_code=201)
def create_conference(
    payload: ConferenceCreateIn,
    service: ConferenceService = Depends(get_conference_service),
    ):
    conference = service.create(
        payload.name,
    )
    return {"id" : conference.conference_id,
            "name" : conference.name,
            }

def get_season_service(uow: IUnitOfWork = Depends(get_uow)) :
    return SeasonService(uow)

@app.get("/api/seasons")
def list_seasons(service : SeasonService = Depends(get_season_service)):
    seasons = service.find_all()
    return [
        {
            "id": season.season_id,
            "name": season.name,
            "start_date": season.start_date,
            "end_date": season.end_date,
        }
        for season in seasons
    ]

@app.get("/api/seasons/{season_id}")
def get_season(
    season_id: int,
    service: SeasonService = Depends(get_season_service),
):
    season = service.find_by_id(season_id)
    if not season:
        return {"error": "Season not found"}
    return {
        "id": season.season_id,
        "name": season.name,
        "start_date": season.start_date,
        "end_date": season.end_date,
    }

@app.post("/api/seasons", status_code=201)
def create_season(
    payload: SeasonCreateIn,
    service: SeasonService = Depends(get_season_service),
    ):
    season = service.create(
        payload.name,
        payload.start_date,
        payload.end_date,
    )
    return {"id" : season.season_id,
            "name" : season.name,
            "start_date": season.start_date,
            "end_date": season.end_date,
            }

def get_team_affiliation_service(uow: IUnitOfWork = Depends(get_uow)) :
    return TeamAffiliationService(uow)

@app.post("/api/team_affiliations", status_code=201)
def create_team_affiliation(
    payload: TeamAffiliationCreateIn,
    service: TeamAffiliationService = Depends(get_team_affiliation_service),
    ):
    team_affiliation = service.create(
        payload.team_id,
        payload.division_id,
        payload.conference_id,
        payload.season_id,
    )
    return {
        "id": team_affiliation.team_affiliation_id,
        "team_id": team_affiliation.team_id,
        "division_id": team_affiliation.division_id,
        "conference_id": team_affiliation.conference_id,
        "season_id": team_affiliation.season_id,
    }

@app.get("/api/team_affiliations")
def list_team_affiliations(service : TeamAffiliationService = Depends(get_team_affiliation_service)):
    team_affiliations = service.find_all()
    return [
        {
            "id": team_affiliation.team_affiliation_id,
            "team_id": team_affiliation.team_id,
            "division_id": team_affiliation.division_id,
            "conference_id": team_affiliation.conference_id,
            "season_id": team_affiliation.season_id,
        }
        for team_affiliation in team_affiliations
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
