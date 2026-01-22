# migrations

Alembic のマイグレーションスクリプトを管理します。

## セットアップ

1. `alembic.ini` の `sqlalchemy.url` を使用する DB に合わせて設定します。
2. 自動生成を使う場合は `migrations/env.py` の `target_metadata` に対象のメタデータを設定します。
   現状は `None` のため、`--autogenerate` は動作しません。

## 使い方

- 既存のリビジョン適用: `alembic upgrade head`
- 1つ戻す: `alembic downgrade -1`
- 新規リビジョン作成（手動）: `alembic revision -m "..."`
