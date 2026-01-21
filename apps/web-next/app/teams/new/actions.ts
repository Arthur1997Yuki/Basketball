"use server";

import { redirect } from "next/navigation";

export async function createTeamAction(formData: FormData) {
    const official_name = String(formData.get("official_name") ?? "").trim();
    const abbreviation = String(formData.get("abbreviation") ?? "").trim();
    const prefecture = String(formData.get("prefecture") ?? "").trim();
    const city = String(formData.get("city") ?? "").trim();
    const management_corporation = String(formData.get("management_corporation") ?? "").trim();

    const res = await fetch("http://127.0.0.1:3000/api/teams", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        cache: "no-store",
        body: JSON.stringify({ official_name: official_name, abbreviation: abbreviation, prefecture: prefecture, city: city, management_corporation: management_corporation || null}),
    });

    if(!res.ok) {
        const text = await res.text();
        throw new Error(`API error: ${res.status} ${text}`)
    }

    redirect("/teams");
}