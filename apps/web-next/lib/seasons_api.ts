async function apiFetch(path: string) {
    const res = await fetch(`http://127.0.0.1:3000/api${path}`, { cache: "no-store"});
    if(!res.ok) throw new Error(`API error: ${res.status}`);
    return res;
}

export type Season = {
    id: number;
    name: string;
    start_date: Date;
    end_date: Date;
};

export async function fetchSeasons(): Promise<Season[]> {
    const res = await apiFetch("/seasons");
    return res.json();
}