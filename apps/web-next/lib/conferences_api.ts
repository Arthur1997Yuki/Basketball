async function apiFetch(path: string) {
    const res = await fetch(`http://127.0.0.1:3000/api${path}`, { cache: "no-store"});
    if(!res.ok) throw new Error(`API error: ${res.status}`);
    return res;
}

export type Conference = {
    id: number;
    name: string;
};

export async function fetchConferences(): Promise<Conference[]> {
    const res = await apiFetch("/conferences");
    return res.json();
}

export async function fetchConferenceById(id: number): Promise<Conference> {
    const res = await apiFetch(`/conferences/${id}`);
    return res.json();
}