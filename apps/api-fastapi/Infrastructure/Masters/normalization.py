import unicodedata

def norm_name(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("　", " ").strip()
    s = " ".join(s.split())
    return s
