import { fetchTeamAffiliations } from "@/lib/team_affilistions_api";
import { fetchTeamById } from "@/lib/teams_api";
import { fetchDivisionById } from "@/lib/divisions_api";
import { fetchConferenceById } from "@/lib/conferences_api";
import { fetchSeasonById } from "@/lib/seasons_api";
import Link from "next/link";

export default async function TeamAffiliationsPage() {
  const team_affiliations = await fetchTeamAffiliations();
  const rows = await Promise.all(
    team_affiliations.map(async (team_affiliation) => {
      const [team, division, conference, season] = await Promise.all([
        fetchTeamById(team_affiliation.team_id),
        fetchDivisionById(team_affiliation.division_id),
        fetchConferenceById(team_affiliation.conference_id),
        fetchSeasonById(team_affiliation.season_id),
      ]);
      return { team_affiliation, team, division, conference, season };
    })
  );
  return (
    <main style={{ padding: 24 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <h1>Team Affiliations</h1>
            <Link href="/team_affiliations/new">+ New</Link>
        </div>

        {team_affiliations.length === 0 ? (
            <p style={{ marginTop: 16 }}>まだチームの所属情報が登録されていません。</p>
        )
        : (
            <div style={{ marginTop: 16, display: "grid", gap: 12 }}>
                <h2>チーム所属情報　一覧</h2>
                <table>
                    <thead>
                        <tr>
                            <th>チーム所属情報ID</th>
                            <th>チーム名</th>
                            <th>ディビジョン名</th>
                            <th>カンファレンス名</th>
                            <th>シーズン名</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows.map(({ team_affiliation, team, division, conference, season }) => (
                            <tr key={team_affiliation.id}>
                                <td>{team_affiliation.id}</td>
                                <td>{team.official_name}</td>
                                <td>{division.name}</td>
                                <td>{conference.name}</td>
                                <td>{season.name}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        )}
    </main>
    );
}
