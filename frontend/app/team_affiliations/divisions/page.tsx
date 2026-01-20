import { fetchDivisions } from "@/lib/api";
import Link from "next/link";

export default async function TeamsPage() {
  const divisions = await fetchDivisions();
    return (
    <main style={{ padding: 24 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <h1>Divisions</h1>
            <Link href="/team_affiliations/divisions/new">+ New</Link>
        </div>

        {divisions.length === 0 ? (
            <p style={{ marginTop: 16 }}>まだディビジョンが登録されていません。</p>
        )
        : (
            <ul style={{ marginTop: 16, display: "grid", gap: 12 }}>
                <h2>ディビジョン　一覧</h2>
                <table>
                    <thead>
                        <tr>
                            <th>ディビジョンID</th>
                            <th>ディビジョン名</th>
                        </tr>
                    </thead>
                    <tbody>
                        {divisions.map((division) => (
                            <tr key={division.id}>
                                <td>{division.id}</td>
                                <td>{division.name}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </ul>
        )}
    </main>
    );
}
