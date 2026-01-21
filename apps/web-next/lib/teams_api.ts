export type Team = {
    id: number;
    official_name: string;
    abbreviation: string;
    home_town: string;
    management_corporation: string;
};

async function apiFetch(path: string) {
    const res = await fetch(`http://127.0.0.1:3000/api${path}`, { cache: "no-store"});
    if(!res.ok) throw new Error(`API error: ${res.status}`);
    return res;
}

export async function fetchTeams(): Promise<Team[]> {
  const res = await apiFetch("/teams");
  return res.json();
}

