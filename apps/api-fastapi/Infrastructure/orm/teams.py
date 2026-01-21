from sqlalchemy import Integer, String, DateTime, Table, Column
from Infrastructure.orm.base import metadata_obj

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
