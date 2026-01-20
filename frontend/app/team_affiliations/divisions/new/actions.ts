"use server";

import { redirect } from "next/navigation";

export async function createDivisionAction(formData: FormData) {
    const name = String(formData.get("name") ?? "").trim();

    const res = await fetch("http://127.0.0.1:3000/api/divisions", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        cache: "no-store",
        body: JSON.stringify({ name: name }),
    });

    if(!res.ok) {
        const text = await res.text();
        throw new Error(`API error: ${res.status} ${text}`)
    }

    redirect("/team_affiliations/divisions");

}