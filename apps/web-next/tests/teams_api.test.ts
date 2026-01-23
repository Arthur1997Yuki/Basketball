import { afterEach, describe, expect, it, vi } from "vitest";

import { fetchTeams } from "../lib/teams_api";

afterEach(() => {
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

describe("fetchTeams", () => {
  it("returns parsed team list from the API", async () => {
    // Arrange: APIの返却データを用意する。
    const payload = [
      {
        id: 1,
        official_name: "Tokyo Hoopers",
        abbreviation: "TH",
        home_town: "東京都新宿区",
        management_corporation: "Hoopers Inc.",
      },
    ];

    // Arrange: 実HTTPを避けるため fetch をスタブする。
    const fetchMock = vi.fn(async () =>
      new Response(JSON.stringify(payload), { status: 200 })
    );
    vi.stubGlobal("fetch", fetchMock);

    // Act: APIクライアントを呼び出す。
    const result = await fetchTeams();

    // Assert: 返却値とリクエスト内容を検証する。
    expect(result).toEqual(payload);
    expect(fetchMock).toHaveBeenCalledWith(
      "http://127.0.0.1:3000/api/teams",
      { cache: "no-store" }
    );
  });
});
