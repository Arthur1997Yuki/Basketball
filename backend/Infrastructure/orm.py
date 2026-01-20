from sqlalchemy.orm import registry
from sqlalchemy import Integer, String, DateTime, Table, MetaData, Column
from backend.Models.Teams.Team import Team
from backend.Models.TeamAffiliations.Division import Division
from backend.Models.TeamAffiliations.Conference import Conference

mapper_registry = registry()
metadata_obj: MetaData = mapper_registry.metadata

team_table = Table(
    "teams",
    metadata_obj,
    Column("team_id", Integer, primary_key=True),
    Column("official_name", String, nullable=False),
    Column("abbreviation", String, nullable=False),
    Column("home_town_prefecture", String, nullable=False),
    Column("home_town_city", String, nullable=False),
    Column("management_corporation", String, nullable=False),
    Column("created_at", DateTime, nullable=True),
)

division_table = Table(
    "divisions",
    metadata_obj,
    Column("division_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("created_at", DateTime, nullable=True),
)

conference_table = Table(
    "conferences",
    metadata_obj,
    Column("conference_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("created_at", DateTime, nullable=True),
)

def start_mappers() -> None:
    mapper_registry.map_imperatively(Team, team_table)
    mapper_registry.map_imperatively(Division, division_table)
    mapper_registry.map_imperatively(Conference, conference_table)
    
def create_tables(engine) -> None:
    metadata_obj.create_all(bind=engine)
