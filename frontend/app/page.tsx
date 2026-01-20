import Link from "next/link";

export default function Home() {
  return (
    <main style={{ padding: 24}}>
      <h1>BasketBall</h1>
      <p style={{ marginTop: 12}}>
        <Link href="/teams">チーム</Link>
      </p>
    </main>
  );
}
