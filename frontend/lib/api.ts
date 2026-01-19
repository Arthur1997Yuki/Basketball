export type Team = {
    id: string;
    offical_name: string;
    abbreviation: string;
    home_town: string;
    management_corporation: string;
};

async function apiFetch(path: string) {
    const res = await fetch('/api${path}', { cache: "no-store"});
    if(!res.ok) throw new Error('API error: ${res.status}');
    return res;
}