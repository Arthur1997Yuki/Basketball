import { fetchTeams } from "@/lib/api";
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
      ) : (
        <ul style={{ marginTop: 16, display: "grid", gap: 12 }}>
          {teams.map((team) => (
            <li key={team.id} style={{ border: "1px solid #ddd", padding: 12, borderRadius: 8 }}>
              <div style={{ fontWeight: 700 }}>{team.official_name}</div>
              <div>{team.abbreviation}</div>
              <div>{team.home_town}</div>
              <div>{team.management_corporation}</div>
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}
