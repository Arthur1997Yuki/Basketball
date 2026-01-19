from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f'postgresql+psycopg://nwaba:david@127.0.0.1:5432/basketball_db'

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # 開発中のスリープ復帰などで壊れた接続を検知
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
