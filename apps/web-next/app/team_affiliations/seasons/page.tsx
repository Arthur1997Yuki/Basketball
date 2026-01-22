import { fetchSeasons } from "@/lib/seasons_api";
import Link from "next/link";

export default async function SeasonsPage() {
  const seasons = await fetchSeasons();
    return (
    <main style={{ padding: 24 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <h1>Seasons</h1>
            <Link href="/team_affiliations/seasons/new">+ New</Link>
        </div>

        {seasons.length === 0 ? (
            <p style={{ marginTop: 16 }}>まだシーズンが登録されていません。</p>
        )
        : (
            <ul style={{ marginTop: 16, display: "grid", gap: 12 }}>
                <h2>シーズン　一覧</h2>
                <table>
                    <thead>
                        <tr>
                            <th>シーズンID</th>
                            <th>シーズン名</th>
                            <th>開始日</th>
                            <th>終了日</th>
                        </tr>
                    </thead>
                    <tbody>
                        {seasons.map((season) => (
                            <tr key={season.id}>
                                <td>{season.id}</td>
                                <td>{season.name}</td>
                                <td>{season.start_date}</td>
                                <td>{season.end_date}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </ul>
        )}
    </main>
    );
}
