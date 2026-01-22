# apps

アプリケーションの実体をまとめたディレクトリです。

## サブディレクトリ

- `api-fastapi/` FastAPI + SQLAlchemy API
- `web-next/` Next.js フロントエンド

## セットアップと実行

### api-fastapi

1. Postgres を起動し DB を作成します。
2. `apps/api-fastapi/Infrastructure/db.py` の `DATABASE_URL` を環境に合わせて更新します。
3. 依存関係をインストールします（requirements ファイルは未配置）。
   例: `pip install fastapi uvicorn sqlalchemy psycopg`
4. 起動します。
   例: `uvicorn app:app --app-dir apps/api-fastapi --reload`
5. 主なエンドポイントは `README.md` を参照してください。

### web-next

1. `npm install`
2. `npm run dev`（http://127.0.0.1:3000）

詳細は `apps/web-next/README.md` を参照してください。
