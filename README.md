# Basketball

FastAPI + PostgreSQL のバックエンドと、Next.js のフロントエンドで構成されたバスケットボール情報管理のサンプルです。

## 構成

- `apps/api-fastapi/` FastAPI アプリ（旧 backend）
- `apps/web-next/` Next.js アプリ（旧 frontend）
- `apps/crm-rails-api/` Rails API（新規）
- `migrations/` Alembic マイグレーション
- `docs/` 設計ドキュメント類

## 前提

- Python 3.11+（推奨）
- Node.js 20+ / npm
- PostgreSQL

## セットアップ

### 1) データベース

`apps/api-fastapi/Infrastructure/db.py` の `DATABASE_URL` に合わせて DB を用意してください。
デフォルトは以下です。

```
postgresql+psycopg://nwaba:david@127.0.0.1:5432/basketball_db
```

必要に応じてユーザー/パスワード/DB 名を変更してください。

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

`http://127.0.0.1:3000` で起動します。`/api/*` は `next.config.ts` のリライトでバックエンドに転送されます。

## 主な API

- `GET /api/teams`
- `POST /api/teams`
- `GET /api/divisions`
- `POST /api/divisions`
- `GET /api/conferences`
- `POST /api/conferences`

## 開発メモ

- DB 接続設定は `apps/api-fastapi/Infrastructure/db.py` を参照してください。
- 既存データの管理は Alembic を利用できます（`migrations/`, `alembic.ini`）。
