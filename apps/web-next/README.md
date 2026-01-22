# web-next

Next.js（App Router）で構成されたフロントエンドです。

## 前提

- Node.js 20+ / npm

## セットアップ

```
npm install
```

## 開発サーバー

```
npm run dev
```

`http://127.0.0.1:3000` で起動します。

## API プロキシ

`/api/*` は `apps/web-next/next.config.ts` のリライトで `http://127.0.0.1:8000` に転送されます。
バックエンドを先に起動しておくと画面連携が確認できます。

## ディレクトリ構成

- `app/` ルーティングと画面（App Router）
- `lib/` 画面で使うユーティリティ
- `public/` 静的ファイル

## コマンド

- `npm run dev` 開発サーバー起動
- `npm run build` 本番ビルド
- `npm run start` 本番サーバー起動
- `npm run lint` ESLint

## ドメインモデル追加時の改修手順（フロントエンド）

1. API 追加に合わせて `app/` にページやルートを作成します。
2. `lib/` に API クライアントや取得関数を追加/更新します。
3. 画面で必要な UI と入力フォームを実装します。

## 具体例（TeamAffiliation を追加する場合）

- `app/` に一覧/登録ページを追加
- `lib/` に取得/登録用の関数を追加
