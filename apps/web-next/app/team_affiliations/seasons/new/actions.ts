"use server";

import { redirect } from "next/navigation";

export async function createSeasonAction(formData: FormData) {
    const name = String(formData.get("name") ?? "").trim();
    const start_date = String(formData.get("start_date") ?? "").trim();
    const end_date = String(formData.get("end_date") ?? "").trim();

    const res = await fetch("http://127.0.0.1:3000/api/seasons", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        cache: "no-store",
        body: JSON.stringify({ name: name, start_date: start_date, end_date: end_date }),
    });

    if(!res.ok) {
        const text = await res.text();
        throw new Error(`API error: ${res.status} ${text}`)
    }

    redirect("/team_affiliations/seasons");
}