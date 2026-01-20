from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from sqlalchemy import text
from .Infrastructure.db import get_db, engine
from .Infrastructure.unit_of_work import UnitOfWork
from backend.Application.Teams.TeamService import TeamsService
from pydantic import BaseModel
from backend.Infrastructure.orm import start_mappers, create_tables
from backend.Application.TeamAffiliations.DivisionService import DivisionService

class TeamCreateIn(BaseModel):
    official_name: str
    abbreviation: str
    prefecture: str
    city: str
    management_corporation: str

class DivisionCreateIn(BaseModel):
    name: str

app = FastAPI()

@app.on_event("startup")
def on_startup():
    start_mappers()
    create_tables(engine)

def get_uow():
    return UnitOfWork()

def get_team_service(uow: UnitOfWork = Depends(get_uow)) :
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

def get_division_service(uow: UnitOfWork = Depends(get_uow)) :
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
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
