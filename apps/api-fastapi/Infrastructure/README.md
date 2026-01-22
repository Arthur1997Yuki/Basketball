# Infrastructure

DB 接続、ORM マッピング、リポジトリ実装などのインフラ層です。

## 構成

- `db.py` SQLAlchemy エンジン/セッション
- `uow_factory.py` UoW 生成
- `unit_of_work.py` UoW 実装
- `Repositories/` リポジトリ実装
- `Masters/` マスタ参照実装
- `orm/` SQLAlchemy のテーブル定義とマッピング
