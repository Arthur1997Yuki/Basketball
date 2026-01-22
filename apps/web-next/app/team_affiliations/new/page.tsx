import Link from "next/link";
import { fetchTeams } from "@/lib/teams_api";
import { fetchDivisions } from "@/lib/divisions_api";
import { fetchConferences } from "@/lib/conferences_api";
import { fetchSeasons } from "@/lib/seasons_api";
import { createTeamAffiliationAction } from "./actions";

export default async function NewTeamAffiliationPage() {
    const [teams, divisions, conferences, seasons] = await Promise.all([
        fetchTeams(),
        fetchDivisions(),
        fetchConferences(),
        fetchSeasons(),
    ]);

    const isReady = teams.length > 0 && divisions.length > 0 && conferences.length > 0 && seasons.length > 0;

    return (
        <main style={{ padding: 24, maxWidth: 640 }}>
            <h1>チーム所属情報　新規登録</h1>

            {!isReady && (
                <p style={{ marginTop: 12 }}>
                    登録前に、チーム・ディビジョン・カンファレンス・シーズンを作成してください。
                </p>
            )}

            <form action={createTeamAffiliationAction} style={{ marginTop: 16, display: "grid", gap: 12 }}>
                <label style={{ display: "grid", gap: 6 }}>
                    <span>チーム</span>
                    <select name="team_id" required defaultValue="">
                        <option value="" disabled>選択してください</option>
                        {teams.map((team) => (
                            <option key={team.id} value={team.id}>{team.official_name}</option>
                        ))}
                    </select>
                </label>

                <label style={{ display: "grid", gap: 6 }}>
                    <span>ディビジョン</span>
                    <select name="division_id" required defaultValue="">
                        <option value="" disabled>選択してください</option>
                        {divisions.map((division) => (
                            <option key={division.id} value={division.id}>{division.name}</option>
                        ))}
                    </select>
                </label>

                <label style={{ display: "grid", gap: 6 }}>
                    <span>カンファレンス</span>
                    <select name="conference_id" required defaultValue="">
                        <option value="" disabled>選択してください</option>
                        {conferences.map((conference) => (
                            <option key={conference.id} value={conference.id}>{conference.name}</option>
                        ))}
                    </select>
                </label>

                <label style={{ display: "grid", gap: 6 }}>
                    <span>シーズン</span>
                    <select name="season_id" required defaultValue="">
                        <option value="" disabled>選択してください</option>
                        {seasons.map((season) => (
                            <option key={season.id} value={season.id}>{season.name}</option>
                        ))}
                    </select>
                </label>

                <div style={{ display: "flex", gap: 12, marginTop: 8 }}>
                    <button type="submit" disabled={!isReady}>新規登録</button>
                    <Link href="/team_affiliations">キャンセル</Link>
                </div>
            </form>
        </main>
    );
}
