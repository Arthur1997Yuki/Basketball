# migrations

Alembicのマイグレーションスクリプトを管理します。

## セットアップ
1. `alembic.ini` の `sqlalchemy.url` を使用するDBに合わせて設定します。
2. `migrations/env.py` の `target_metadata` を必要に応じて設定します。

## 使い方
- 既存のリビジョン適用: `alembic upgrade head`
- 1つ戻す: `alembic downgrade -1`
- 新規リビジョン作成（手動）: `alembic revision -m "..."`  
  自動生成を使う場合は `target_metadata` を設定してください。
