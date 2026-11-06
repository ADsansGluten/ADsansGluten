"""Génère contributions-creatures.svg à partir des vraies contributions GitHub.

Variables d'environnement : GITHUB_TOKEN, GITHUB_USER.
Option --mock pour tester sans réseau.
"""
import json, os, random, sys, urllib.request

QUERY = """
query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
weeks{contributionDays{weekday contributionLevel}}}}}}
"""
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}


def fetch(user, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": user}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "profile-creatures"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    grid = []
    for w in weeks:
        col = [None] * 7
        for d in w["contributionDays"]:
            col[d["weekday"]] = LEVELS.get(d["contributionLevel"], 0)
        grid.append(col)
    return grid


def mock():
    random.seed(3)
    return [[random.choices(range(5), [30, 25, 20, 15, 10])[0] for _ in range(7)] for _ in range(53)]


def build(grid):
    W, H = 1200, 300
    cell, gap = 18, 4
    pitch = cell + gap
    cols = len(grid)
    x0 = (W - (cols * pitch - gap)) // 2
    y0 = 96
    DUR = 14.0
    greens = ['#1b1633', '#0e4429', '#006d32', '#26a641', '#39d353']
    lanes = [('l', [0, 1], 118, 0.0), ('o', [2, 3, 4], 104, 0.6), ('d', [5, 6], 132, 0.3)]
    total = cols * pitch
    cells = []
    for c, col in enumerate(grid):
        for r in range(7):
            lvl = col[r]
            if lvl is None:
                continue
            lane = [ln for ln in lanes if r in ln[1]][0]
            spd, off = lane[2], lane[3]
            x, y = x0 + c * pitch, y0 + r * pitch
            t = off + (c * pitch + cell / 2 + 30) / spd
            k = min(t / DUR, 0.84)
            k2 = min(k + 0.012, 0.85)
            cells.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="{greens[lvl]}">'
                f'<animate attributeName="opacity" values="1;1;0;0;1;1" keyTimes="0;{k:.4f};{k2:.4f};0.90;0.96;1" dur="{DUR}s" repeatCount="indefinite"/></rect>')
    eyes = ('<g id="eyes"><ellipse cx="-30" cy="0" rx="16" ry="20" fill="#0f172a"/><ellipse cx="30" cy="0" rx="16" ry="20" fill="#0f172a"/>'
            '<circle cx="-25" cy="-7" r="6" fill="#fff"/><circle cx="35" cy="-7" r="6" fill="#fff"/></g>')
    minis = {
        'l': '<g transform="scale(.155) translate(0,-232)"><path d="M0 110 C 55 180 100 235 100 295 C 100 350 60 378 0 378 C -60 378 -100 350 -100 295 C -100 235 -55 180 0 110 Z" fill="url(#teal)" stroke="#99f6e4" stroke-width="5"/><path d="M-22 130 L-40 82 L-6 112 Z" fill="#c4b5fd"/><path d="M22 130 L40 82 L6 112 Z" fill="#c4b5fd"/><use href="#eyes" x="0" y="290"/></g>',
        'o': '<g transform="scale(.17) translate(0,-250)"><path d="M-95 170 L95 170 L125 370 L-125 370 Z" fill="url(#gold)" stroke="#fef3c7" stroke-width="5"/><path d="M-95 170 L-70 130 L70 130 L95 170 Z" fill="#fef3c7"/><use href="#eyes" x="0" y="275"/><circle cx="-120" cy="260" r="20" fill="#fbbf24"/><circle cx="120" cy="260" r="20" fill="#fbbf24"/></g>',
        'd': '<g transform="scale(.165) translate(0,-232)"><path d="M-90 170 V330 C-90 372 90 372 90 330 V170 Z" fill="url(#viol)" stroke="#ddd6fe" stroke-width="5"/><ellipse cx="0" cy="170" rx="90" ry="28" fill="#ddd6fe"/><use href="#eyes" x="0" y="290"/><rect x="-5" y="110" width="10" height="38" rx="5" fill="#ddd6fe"/><circle cx="0" cy="104" r="12" fill="#22d3ee"/></g>',
    }
    creat = []
    for name, rws, spd, off in lanes:
        cy = y0 + (rws[0] + rws[-1] + 1) / 2 * pitch - gap / 2
        xs, xe = x0 - 30, x0 + total
        k1 = max(off / DUR, 0.001)
        k2 = min((off + (xe - xs) / spd + 0.2) / DUR, 0.86)
        creat.append(
            f'<g opacity="0"><animateTransform attributeName="transform" type="translate" values="{xs} {cy};{xs} {cy};{xe} {cy};{xe} {cy}" keyTimes="0;{k1:.4f};{k2:.4f};1" dur="{DUR}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;{k1:.4f};{k2-0.005:.4f};{k2:.4f};1" dur="{DUR}s" repeatCount="indefinite"/>'
            f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -3;0 0" dur=".5s" repeatCount="indefinite" additive="sum"/>{minis[name]}</g></g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Inter,'Segoe UI',Arial,sans-serif">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a1458"/><stop offset=".6" stop-color="#120a26"/><stop offset="1" stop-color="#08060f"/></linearGradient>
<linearGradient id="teal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5eead4"/><stop offset="1" stop-color="#0d9488"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fde68a"/><stop offset="1" stop-color="#d97706"/></linearGradient>
<linearGradient id="viol" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4b5fd"/><stop offset="1" stop-color="#6d28d9"/></linearGradient>
{eyes}
<clipPath id="r"><rect width="{W}" height="{H}" rx="24"/></clipPath></defs>
<g clip-path="url(#r)"><rect width="{W}" height="{H}" fill="url(#bg)"/>
<text x="{x0}" y="52" font-size="21" font-weight="700" fill="#a78bfa" letter-spacing="4">LES CRÉATURES CROQUENT MES CONTRIBUTIONS</text>
<text x="{x0}" y="78" font-size="16" fill="#a8a29e">Mes vraies contributions GitHub des 12 derniers mois, mises à jour chaque nuit</text>
{''.join(cells)}
{''.join(creat)}
</g></svg>'''


if __name__ == "__main__":
    if "--mock" in sys.argv:
        grid = mock()
    else:
        grid = fetch(os.environ["GITHUB_USER"], os.environ["GITHUB_TOKEN"])
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "contributions-creatures.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write(build(grid))
    print("écrit", out)
