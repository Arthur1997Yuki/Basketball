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
