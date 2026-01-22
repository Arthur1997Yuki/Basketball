# Glossary

共通の用語集です。各 README から参照します。

## 一般

- バックエンド: API や DB へのアクセスを担当するサーバー側（例: `apps/api-fastapi/`）。
- フロントエンド: 画面表示とユーザー操作を担当するクライアント側（例: `apps/web-next/`）。

## API / バックエンド

- FastAPI: Python 製の Web API フレームワーク（例: `apps/api-fastapi/app.py`）。
- OpenAPI: REST API の仕様を記述する標準フォーマット（例: `/docs` で自動生成）。
- エンドポイント: API の URL と HTTP メソッドの組み合わせ（例: `GET /api/teams`）。
- ORM: オブジェクトと DB テーブルを対応づける仕組み（例: `Infrastructure/orm`）。
- Repository: 永続化層のアクセスを抽象化するパターン（例: `TeamRepository`）。
- DTO: データ転送用のオブジェクト。API の入出力を表現する（例: `TeamCreateIn`）。
- UoW（Unit of Work）: 複数の DB 操作を 1 つのトランザクションとして扱う設計パターン（例: `unit_of_work.py`）。

## フロントエンド

- Next.js: React ベースのフルスタックフレームワーク（例: `apps/web-next/`）。
- App Router: `app/` ディレクトリでルーティングを定義する仕組み（例: `apps/web-next/app/`）。
- CSR/SSR: クライアント/サーバーでレンダリングする方式（例: `npm run dev` で SSR 可能）。

## DB / マイグレーション

- マイグレーション: DB スキーマ変更を履歴として管理する仕組み（例: `migrations/`）。
- リビジョン: マイグレーションの単位（1 回の変更）（例: `alembic revision -m \"...\"`）。

## ドキュメント

- PlantUML: テキストから図を生成するツール（例: `docs/api-fastapi/er.pu`）。
- `*.pu`: PlantUML のソースファイル拡張子（例: `class.pu`）。
