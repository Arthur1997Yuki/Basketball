from sqlalchemy.orm import registry
from sqlalchemy import MetaData

mapper_registry = registry()
metadata_obj: MetaData = mapper_registry.metadata
