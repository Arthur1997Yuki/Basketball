import Link from "next/link";
import { createTeamAction } from "./actions";

export default function NewTeamPage() {
    return (
        <main style={{ padding: 24, maxWidth: 520}}>
            <h1>チーム　新規登録</h1>

            <form action={createTeamAction} style={{ marginTop: 16, display: "grid", gap: 12}}>
                <label style={{ display: "grid", gap: 6}}>
                    <span>正式名称</span>
                    <input name="official_name" required placeholder="三遠ネオフェニックス" />
                </label>

                <label style={{ display: "grid", gap: 6}}>
                    <span>略称</span>
                    <input name="abbreviation" placeholder="三遠" maxLength={10} />
                </label>

                <label style={{ display: "grid", gap: 6}}>
                    <span>ホームタウン　都道府県</span>
                    <input name="prefecture" placeholder="愛知県" maxLength={10} />
                </label>

                <label style={{ display: "grid", gap: 6}}>
                    <span>ホームタウン　市町村</span>
                    <input name="city" placeholder="豊橋市" maxLength={10} />
                </label>

                <label style={{ display: "grid", gap: 6}}>
                    <span>運営法人</span>
                    <input name="management_corporation" placeholder="株式会社フェニックス" maxLength={10} />
                </label>

                <div style={{ display: "flex", gap: 12, marginTop: 8}}>
                    <button type="submit">新規登録</button>
                    <Link href="teams">キャンセル</Link>
                </div>

            </form>
        </main>
    );
}