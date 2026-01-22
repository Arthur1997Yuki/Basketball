export type TeamAffiliation = {
    id: number;
    team_id: number;
    division_id: number;
    conference_id: number;
    season_id: number;
};

async function apiFetch(path: string) {
    const res = await fetch(`http://127.0.0.1:3000/api${path}`, { cache: "no-store"});
    if(!res.ok) throw new Error(`API error: ${res.status}`);
    return res;
}

export async function fetchTeamAffiliations(): Promise<TeamAffiliation[]> {
  const res = await apiFetch("/team_affiliations");
  return res.json();
}