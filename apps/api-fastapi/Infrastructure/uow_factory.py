from Application.unit_of_work import IUnitOfWork
from Infrastructure.unit_of_work import UnitOfWork


def get_uow() -> IUnitOfWork:
    return UnitOfWork()
