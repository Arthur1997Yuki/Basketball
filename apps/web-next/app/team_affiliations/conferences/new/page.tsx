import Link from "next/link";
import { createConferenceAction } from "./actions";

export default function NewConferencePage() {
    return (
        <main style={{ padding: 24, maxWidth: 520}}>
            <h1>カンファレンス　新規登録</h1>

            <form action={createConferenceAction} style={{ marginTop: 16, display: "grid", gap: 12}}>
                <label style={{ display: "grid", gap: 6}}>
                    <span>名称</span>
                    <input name="name" required placeholder="B1" />
                </label>

                <div style={{ display: "flex", gap: 12, marginTop: 8}}>
                    <button type="submit">新規登録</button>
                    <Link href="/team_affiliations/conferences">キャンセル</Link>
                </div>

            </form>
        </main>
    );
}