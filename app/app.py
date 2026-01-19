from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from sqlalchemy import text
from .Infrastructure.db import get_db
from .Infrastructure.unit_of_work import UnitOfWork
from .Services.TeamService import TeamsService

app = FastAPI()

def get_uow():
    return UnitOfWork()

def get_team_service(uow: UnitOfWork = Depends(get_uow)) :
    return TeamsService(uow)

@app.post("/teams")
def create_team(offical_name : str, abbreviation : str, prefecture : str, city : str, management_corporation : str, service : TeamsService = Depends(get_team_service)):
    team = service.create(offical_name, abbreviation, prefecture, city, management_corporation)
    return {"id" : team.team_id,
            "offical_name" : team.offical_name,
            "abbreviation" : team.abbreviation,
            "home_town" : team.home_town.hometown,
            "management_corporation" : team.management_corporation,
            }

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    # 1行だけSQL叩いて疎通確認
    v = db.execute(text("select 1")).scalar_one()
    return {"db": "ok", "select_1": v}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
