# Basketball

FastAPI + PostgreSQL のバックエンドと、Next.js のフロントエンドで構成されたバスケットボール情報管理のサンプルです。

## 構成

- `apps/api-fastapi/` FastAPI + SQLAlchemy API
- `apps/web-next/` Next.js フロントエンド（App Router）
- `migrations/` Alembic マイグレーション
- `docs/` 設計ドキュメント類
- `frontend/` （現在は空）

## 前提

- Python 3.11+（推奨）
- Node.js 20+ / npm
- PostgreSQL

## セットアップ

### 1) データベース

`apps/api-fastapi/Infrastructure/db.py` と `alembic.ini` の接続設定を環境に合わせて更新してください。
デフォルトは以下です。

```
postgresql+psycopg://nwaba:david@127.0.0.1:5432/basketball_db
```

### 2) バックエンド

```
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy psycopg
uvicorn app:app --app-dir apps/api-fastapi --reload
```

起動時にテーブルを自動作成します。API は `http://127.0.0.1:8000` で提供されます。

### 3) フロントエンド

```
cd apps/web-next
npm install
npm run dev
```

`http://127.0.0.1:3000` で起動します。`/api/*` は `apps/web-next/next.config.ts` のリライトでバックエンドに転送されます。

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

## 開発メモ

- DB 接続設定は `apps/api-fastapi/Infrastructure/db.py` と `alembic.ini` を参照してください。
- マイグレーションは `migrations/README.md` を参照してください。
