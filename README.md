# Basketball

FastAPI + PostgreSQL のバックエンドと、Next.js のフロントエンドで構成されたバスケットボール情報管理のサンプルです。

## 技術概要（簡易）

- FastAPI: Python 製の高速な Web API フレームワーク。型ヒントを使って自動ドキュメント（OpenAPI）を生成できます。
- SQLAlchemy: Python の ORM。Python のクラスと DB テーブルを対応づけます。
- Alembic: SQLAlchemy 用のマイグレーションツール。スキーマ変更を履歴管理します。
- Next.js: React ベースのフルスタックフレームワーク。App Router でルーティング/SSR/静的生成を扱えます。
- PostgreSQL: オープンソースの RDB。信頼性が高く、拡張性に優れます。

## 技術選定の理由（簡易）

- FastAPI: 型ヒントと自動ドキュメントにより API の設計/実装/確認がしやすい。
- SQLAlchemy: Python での DB 抽象化ができ、テストや変更に強い。
- Alembic: スキーマ変更の履歴管理がしやすく、ロールバックも可能。
- Next.js: ルーティングやビルドが統合され、フロント実装が簡潔になる。
- PostgreSQL: RDB として機能が豊富で運用実績が多い。

## 用語集（簡易）

- ORM: オブジェクトと DB テーブルを対応づける仕組み。
- マイグレーション: DB スキーマ変更を履歴として管理する仕組み。
- App Router: Next.js のファイルベースルーティング（`app/` ディレクトリ）。
- UoW（Unit of Work）: 複数の DB 操作を 1 つのトランザクションとして扱う設計パターン。

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

## ドメインモデル追加時の改修手順（バックエンド→フロントエンド）

### バックエンド

1. `apps/api-fastapi/Models/` に新しいモデル（エンティティ/値オブジェクト）を追加します。
2. 必要に応じてリポジトリ IF を `apps/api-fastapi/Models/*` に追加します。
3. `apps/api-fastapi/Infrastructure/orm/` にテーブル定義を追加します。
4. `apps/api-fastapi/Infrastructure/orm/__init__.py` のマッピングに追加します。
5. リポジトリ実装を `apps/api-fastapi/Infrastructure/Repositories/` に追加します。
6. ユースケースを `apps/api-fastapi/Application/` に追加し、サービスから利用します。
7. API 入出力スキーマを `apps/api-fastapi/Resources/schemas.py` に追加します。
8. エンドポイントを `apps/api-fastapi/app.py` に追加します。
9. マイグレーション運用を行う場合は `migrations/` を更新します。

### フロントエンド

1. API に合わせて `apps/web-next/app/` にページ/ルートを追加します。
2. データ取得のユーティリティを `apps/web-next/lib/` に追加/拡張します。
3. 画面で必要な表示/入力 UI を実装します。

### 具体例（TeamAffiliation を追加する場合）

バックエンド側:

- `apps/api-fastapi/Models/TeamAffiliations/` にモデルと IF を追加
- `apps/api-fastapi/Infrastructure/orm/team_affiliations.py` にテーブル定義を追加
- `apps/api-fastapi/Infrastructure/orm/__init__.py` にマッピングを追加
- `apps/api-fastapi/Infrastructure/Repositories/TeamAffiliationRepository.py` を追加
- `apps/api-fastapi/Application/TeamAffiliations/TeamAffiliationService.py` を追加
- `apps/api-fastapi/Resources/schemas.py` に入力/出力スキーマを追加
- `apps/api-fastapi/app.py` に `/api/team_affiliations` を追加

フロントエンド側:

- `apps/web-next/app/` に一覧/登録ページを追加
- `apps/web-next/lib/` に取得/登録用関数を追加

### マイグレーション運用の流れ（Alembic）

1. `alembic.ini` の `sqlalchemy.url` を設定します。
2. `migrations/env.py` の `target_metadata` に対象メタデータを設定します。
3. `alembic revision --autogenerate -m "add team affiliations"` を実行します。
4. `alembic upgrade head` を実行します。
5. 必要なら `alembic downgrade -1` で直前の変更を戻します。
