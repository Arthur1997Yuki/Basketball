import Link from "next/link";

export default function Home() {
  return (
    <main style={{ padding: 24}}>
      <h1>BasketBall</h1>
      <p style={{ marginTop: 12}}>
        <Link href="/teams">チーム</Link><br />
        <Link href="/team_affiliations">チーム所属情報</Link><br />
        <Link href="/team_affiliations/conferences">カンファレンス</Link><br />
        <Link href="/team_affiliations/divisions">ディビジョン</Link><br />
        <Link href="/team_affiliations/seasons">シーズン</Link><br />
      </p>
    </main>
  );
}
