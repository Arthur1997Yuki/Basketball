from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from Models.Teams.ITeamRepository import ITeamRepository
from Models.TeamAffiliations.IDivisionRepository import IDivisionRepository
from Models.TeamAffiliations.IConferenceRepository import IConferenceRepository
from Application.HomeTowns.ICityMasterRepository import ICityMasterRepository


class IUnitOfWork(ABC):
    teams: ITeamRepository
    divisions: IDivisionRepository
    conferences: IConferenceRepository
    city_masters: ICityMasterRepository

    def __enter__(self) -> "IUnitOfWork":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass

    @abstractmethod
    def refresh(self, entity: Any) -> None:
        pass
