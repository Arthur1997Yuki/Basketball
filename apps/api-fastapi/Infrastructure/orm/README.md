# Infrastructure/orm

SQLAlchemy のテーブル定義とマッピング設定を管理します。

## 主なファイル

- `base.py` mapper registry と metadata
- `teams.py` チーム関連のテーブル定義
- `team_affiliations.py` ディビジョン/カンファレンス/シーズン/所属のテーブル定義
- `__init__.py` マッパーの登録と `create_all`
