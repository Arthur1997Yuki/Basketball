from backend.Application.unit_of_work import IUnitOfWork
from backend.Infrastructure.unit_of_work import UnitOfWork


def get_uow() -> IUnitOfWork:
    return UnitOfWork()
