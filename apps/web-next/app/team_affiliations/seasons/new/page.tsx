import Link from "next/link";
import { createSeasonAction } from "./actions";

export default function NewSeasonPage() {
    return (
        <main style={{ padding: 24, maxWidth: 520}}>
            <h1>シーズン　新規登録</h1>

            <form action={createSeasonAction} style={{ marginTop: 16, display: "grid", gap: 12}}>
                <label style={{ display: "grid", gap: 6}}>
                    <span>名称</span>
                    <input name="name" required placeholder="B1" />
                </label>

                <label style={{ display: "grid", gap: 6}}>
                    <span>開始日</span>
                    <input name="start_date" required type="date" />
                </label>

                <label style={{ display: "grid", gap: 6}}>
                    <span>終了日</span>
                    <input name="end_date" required type="date" />
                </label>

                <div style={{ display: "flex", gap: 12, marginTop: 8}}>
                    <button type="submit">新規登録</button>
                    <Link href="/team_affiliations/seasons">キャンセル</Link>
                </div>

            </form>
        </main>
    );
}