# api-fastapi

FastAPI + SQLAlchemy で構成された API です。起動時にテーブルを自動作成します。

## 技術概要（簡易）

- FastAPI: Python 製の高速 Web API フレームワーク。型ヒントに基づくバリデーションと OpenAPI 生成が特長です。
- SQLAlchemy: ORM。モデルとテーブルの対応づけやクエリ生成を担当します。
- Alembic: マイグレーションツール。DB スキーマ変更の履歴管理をします。

## 技術選定の理由（簡易）

- FastAPI: API 開発の生産性が高く、OpenAPI による仕様共有が容易。
- SQLAlchemy: DB 変更に強く、Python でドメインモデルを扱いやすい。
- Alembic: スキーマ変更の追跡/ロールバックができ、運用しやすい。

## 用語集（簡易）

- OpenAPI: REST API の仕様を記述する標準フォーマット。
- ORM: オブジェクトと DB テーブルを対応づける仕組み。
- マイグレーション: DB スキーマ変更を履歴として管理する仕組み。

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

## ドメインモデル追加時の改修手順（バックエンド）

1. `Models/` にモデル（エンティティ/値オブジェクト）を追加します。
2. 必要に応じてリポジトリ IF を `Models/` 配下に追加します。
3. `Infrastructure/orm/` にテーブル定義を追加します。
4. `Infrastructure/orm/__init__.py` のマッピングに追加します。
5. `Infrastructure/Repositories/` にリポジトリ実装を追加します。
6. `Application/` にユースケースとサービスを追加します。
7. `Resources/schemas.py` に API 入出力スキーマを追加します。
8. `app.py` にエンドポイントを追加します。
9. 必要に応じて `migrations/` を更新します。

## 具体例（TeamAffiliation を追加する場合）

- `Models/TeamAffiliations/` にモデルと IF を追加
- `Infrastructure/orm/team_affiliations.py` にテーブル定義を追加
- `Infrastructure/orm/__init__.py` にマッピングを追加
- `Infrastructure/Repositories/TeamAffiliationRepository.py` を追加
- `Application/TeamAffiliations/TeamAffiliationService.py` を追加
- `Resources/schemas.py` に入力/出力スキーマを追加
- `app.py` に `/api/team_affiliations` を追加

## マイグレーション運用の流れ（Alembic）

1. `alembic.ini` の `sqlalchemy.url` を設定します。
2. `migrations/env.py` の `target_metadata` に対象メタデータを設定します。
3. `alembic revision --autogenerate -m "add team affiliations"` を実行します。
4. `alembic upgrade head` を実行します。
5. 必要なら `alembic downgrade -1` で直前の変更を戻します。

### `target_metadata` の設定例

`apps/api-fastapi/Infrastructure/orm/base.py` の `metadata_obj` を使います。

```
from Infrastructure.orm.base import metadata_obj
from Infrastructure.orm import start_mappers

start_mappers()
target_metadata = metadata_obj
```

`start_mappers()` を呼ぶことでテーブル定義が読み込まれます。
