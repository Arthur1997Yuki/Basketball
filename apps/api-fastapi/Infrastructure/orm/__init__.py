from Infrastructure.orm.base import mapper_registry, metadata_obj
from Infrastructure.orm.teams import team_table
from Infrastructure.orm.team_affiliations import division_table, conference_table, season_table
from Models.Teams.Team import Team
from Models.TeamAffiliations.Division import Division
from Models.TeamAffiliations.Conference import Conference
from Models.Seasons.Season import Season


def start_mappers() -> None:
    mapper_registry.map_imperatively(Team, team_table)
    mapper_registry.map_imperatively(Division, division_table)
    mapper_registry.map_imperatively(Conference, conference_table)
    mapper_registry.map_imperatively(Season, season_table)

def create_tables(engine) -> None:
    metadata_obj.create_all(bind=engine)
