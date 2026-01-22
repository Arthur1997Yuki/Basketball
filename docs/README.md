# docs

仕様/設計メモ、ユースケース、図などのドキュメントを管理します。

## 技術概要（簡易）

- PlantUML: テキストから図を生成するツール。`*.pu` を図に変換できます。

## 技術選定の理由（簡易）

- PlantUML: 図の差分管理がしやすく、レビューに向く。

## 用語集（簡易）

- `*.pu`: PlantUML のソースファイル拡張子。

## 構成

- `api-fastapi/` FastAPI 関連のドキュメント（ユースケース、ER、用語集など）
- `crm-rails-api/` Rails API のドキュメント（現在はテンプレートのみ）

## 使い方

- `.md` はそのまま閲覧します。
- `.pu` は PlantUML で図を生成できます。
  例: `plantuml docs/api-fastapi/*.pu`
