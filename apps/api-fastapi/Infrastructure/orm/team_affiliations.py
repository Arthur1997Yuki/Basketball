from sqlalchemy import Integer, String, DateTime, Table, Column, Date
from Infrastructure.orm.base import metadata_obj

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
