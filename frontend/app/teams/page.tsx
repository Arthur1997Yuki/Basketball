import { fetchTeams } from "@/lib/teams_api";
import Link from "next/link";

export default async function TeamsPage() {
  const teams = await fetchTeams();

    return (
    <main style={{ padding: 24 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <h1>Teams</h1>
            <Link href="/teams/new">+ New</Link>
        </div>

        {teams.length === 0 ? (
            <p style={{ marginTop: 16 }}>まだチームが登録されていません。</p>
        )
        : (
            <ul style={{ marginTop: 16, display: "grid", gap: 12 }}>
                <h2>チーム一覧</h2>
                <table>
                    <thead>
                        <tr>
                            <th>チームID</th>
                            <th>チーム名(正式名称)</th>
                            <th>略称</th>
                            <th>ホームタウン</th>
                            <th>運営法人</th>
                        </tr>
                    </thead>
                    <tbody>
                        {teams.map((team) => (
                            <tr key={team.id}>
                                <td>{team.id}</td>
                                <td>{team.official_name}</td>
                                <td>{team.abbreviation}</td>
                                <td>{team.home_town}</td>
                                <td>{team.management_corporation}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </ul>
        )}
    </main>
    );
}
