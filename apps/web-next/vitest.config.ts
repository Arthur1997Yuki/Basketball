import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    // DOM不要なため Node 環境で実行する。
    environment: "node",
    // テスト探索を tests 配下に限定して実行を安定化する。
    include: ["tests/**/*.test.ts"],
  },
});
