from sqlalchemy.orm import registry, mapped_column
from sqlalchemy import Integer, String, DateTime, Table, MetaData
from app.Models.Teams import Team

mapper_registry = registry()
metadata_obj: MetaData = mapper_registry.metadata

team_table = Table(
    "teams",
    metadata_obj,
    mapped_column("team_id", Integer, primary_key=True),
    mapped_column("offical_name", String, nullable=False),
    mapped_column("abbreviation", String, nullable=False),
    mapped_column("home_town_prefecture", String, nullable=False),
    mapped_column("home_town_city", String, nullable=False),
    mapped_column("management_corporation", String, nullable=False),
    mapped_column("signup_at", DateTime, nullable=True),
)

def start_mappers() -> None:
    mapper_registry.map_imperatively(Team, team_table)
