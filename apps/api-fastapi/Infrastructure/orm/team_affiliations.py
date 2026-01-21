from sqlalchemy import Integer, String, DateTime, Table, Column
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
