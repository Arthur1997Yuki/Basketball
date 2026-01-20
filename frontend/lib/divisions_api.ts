async function apiFetch(path: string) {
    const res = await fetch(`http://127.0.0.1:3000/api${path}`, { cache: "no-store"});
    if(!res.ok) throw new Error(`API error: ${res.status}`);
    return res;
}

export type Division = {
    id: number;
    name: string;
};

export async function fetchDivisions(): Promise<Division[]> {
    const res = await apiFetch("/divisions");
    return res.json();
}