# apps

アプリケーションの実体をまとめたディレクトリです。

## 技術概要（簡易）

本リポジトリのアプリ群は FastAPI（バックエンド）と Next.js（フロントエンド）で構成されています。

## 技術選定の理由（簡易）

- FastAPI: API 開発の生産性が高く、仕様共有が容易。
- Next.js: ルーティングやビルドが統合され、フロント開発が簡潔。

## 用語集（簡易）

- バックエンド: API や DB へのアクセスを担当するサーバー側。
- フロントエンド: 画面表示とユーザー操作を担当するクライアント側。

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
