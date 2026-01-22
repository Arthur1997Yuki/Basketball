"use server";

import { redirect } from "next/navigation";

export async function createTeamAffiliationAction(formData: FormData) {
    const team_id = Number(formData.get("team_id"));
    const division_id = Number(formData.get("division_id"));
    const conference_id = Number(formData.get("conference_id"));
    const season_id = Number(formData.get("season_id"));

    if (
        !Number.isFinite(team_id) ||
        !Number.isFinite(division_id) ||
        !Number.isFinite(conference_id) ||
        !Number.isFinite(season_id)
    ) {
        throw new Error("Invalid form values.");
    }

    const res = await fetch("http://127.0.0.1:3000/api/team_affiliations", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        cache: "no-store",
        body: JSON.stringify({
            team_id: team_id,
            division_id: division_id,
            conference_id: conference_id,
            season_id: season_id,
        }),
    });

    if(!res.ok) {
        const text = await res.text();
        throw new Error(`API error: ${res.status} ${text}`)
    }

    redirect("/team_affiliations");
}
