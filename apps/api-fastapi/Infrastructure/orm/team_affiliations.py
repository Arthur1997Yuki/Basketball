from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Table, Column
from Infrastructure.orm.base import metadata_obj

team_affiliation_table = Table(
    "team_affiliations",
    metadata_obj,
    Column("team_affiliation_id", Integer, primary_key=True),
    Column("team_id", Integer, ForeignKey("teams.team_id"), nullable=False),
    Column("division_id", Integer, ForeignKey("divisions.division_id"), nullable=False),
    Column("conference_id", Integer, ForeignKey("conferences.conference_id"), nullable=False),
    Column("season_id", Integer, ForeignKey("seasons.season_id"), nullable=False),
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

season_table = Table(
    "seasons",
    metadata_obj,
    Column("season_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("start_date", Date, nullable=False),
    Column("end_date", Date, nullable=False),
    Column("created_at", DateTime, nullable=True),
)
