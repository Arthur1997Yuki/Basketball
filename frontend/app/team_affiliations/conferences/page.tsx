import { fetchConferences } from "@/lib/conferences_api";
import Link from "next/link";

export default async function TeamsPage() {
  const conferences = await fetchConferences();
    return (
    <main style={{ padding: 24 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <h1>Conferences</h1>
            <Link href="/team_affiliations/conferences/new">+ New</Link>
        </div>

        {conferences.length === 0 ? (
            <p style={{ marginTop: 16 }}>まだカンファレンスが登録されていません。</p>
        )
        : (
            <ul style={{ marginTop: 16, display: "grid", gap: 12 }}>
                <h2>所属カンファレンス　一覧</h2>
                <table>
                    <thead>
                        <tr>
                            <th>カンファレンスID</th>
                            <th>カンファレンス名</th>
                        </tr>
                    </thead>
                    <tbody>
                        {conferences.map((conference) => (
                            <tr key={conference.id}>
                                <td>{conference.id}</td>
                                <td>{conference.name}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </ul>
        )}
    </main>
    );
}
