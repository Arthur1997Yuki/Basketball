# api-fastapi

FastAPI + SQLAlchemy で構成された API です。起動時にテーブルを自動作成します。

## 前提

- Python 3.11+
- PostgreSQL

## セットアップ

```
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy psycopg
```

## データベース設定

接続先は `apps/api-fastapi/Infrastructure/db.py` の `DATABASE_URL` を編集してください。
`alembic.ini` の `sqlalchemy.url` も同じ値に合わせると運用が楽です。

## 起動

```
uvicorn app:app --app-dir apps/api-fastapi --reload
```

`http://127.0.0.1:8000` で起動します。

## 主な API

- `GET /api/teams`
- `GET /api/teams/{team_id}`
- `POST /api/teams`
- `GET /api/divisions`
- `GET /api/divisions/{division_id}`
- `POST /api/divisions`
- `GET /api/conferences`
- `GET /api/conferences/{conference_id}`
- `POST /api/conferences`
- `GET /api/seasons`
- `GET /api/seasons/{season_id}`
- `POST /api/seasons`
- `GET /api/team_affiliations`
- `POST /api/team_affiliations`

## 補足

- 起動時に `Infrastructure/orm` でマッピングし、`metadata.create_all` でテーブルを作成します。
- `migrations/` は Alembic 用ですが、現状 `target_metadata` は未設定です。
