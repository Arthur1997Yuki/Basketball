# apps

各アプリケーションのルートをまとめたディレクトリです。

## サブディレクトリ
- `api-fastapi`: FastAPI + SQLAlchemy のAPI
- `web-next`: Next.js フロントエンド
- `crm-rails-api`: Rails API用のプレースホルダー（現在は空）

## セットアップと実行
### api-fastapi
1. Postgresを起動しDBを作成します。
2. `apps/api-fastapi/Infrastructure/db.py` の `DATABASE_URL` を環境に合わせて更新します。
3. 依存関係をインストールします（requirementsファイルは未配置）。
   例: `pip install fastapi uvicorn sqlalchemy psycopg alembic`
4. 起動します（`apps/api-fastapi` で実行）。
   例: `uvicorn app:app --reload`
5. 主なエンドポイント: `/api/teams`, `/api/divisions`, `/api/conferences`

### web-next
1. `npm install`
2. `npm run dev`（http://localhost:3000）

詳細は `apps/web-next/README.md` を参照してください。

### crm-rails-api
現在は空のディレクトリです。API追加時にセットアップ手順を記載します。
