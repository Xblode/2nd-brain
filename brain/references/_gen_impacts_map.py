# -*- coding: utf-8 -*-
"""Génère second-brain-impacts-map.excalidraw — cycle circulaire des 3 piliers + améliorations."""
import json
import math
from pathlib import Path

OUT = Path(__file__).with_name("second-brain-impacts-map.excalidraw")


def base(eid, typ, x, y, w, h, **kw):
    return {
        "id": eid,
        "type": typ,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": kw.get("stroke", "#1e1e1e"),
        "backgroundColor": kw.get("bg", "transparent"),
        "fillStyle": kw.get("fill", "solid"),
        "strokeWidth": kw.get("sw", 2),
        "strokeStyle": kw.get("ss", "solid"),
        "roughness": 0,
        "opacity": kw.get("opacity", 100),
        "groupIds": kw.get("groupIds", []),
        "frameId": None,
        "roundness": {"type": 3} if typ == "rectangle" else None,
        "seed": abs(hash(eid)) % 100000,
        "versionNonce": abs(hash(eid + "v")) % 100000,
        "isDeleted": False,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
    }


def rect(eid, x, y, w, h, **kw):
    return base(eid, "rectangle", x, y, w, h, **kw)


def ellipse(eid, x, y, w, h, **kw):
    e = base(eid, "ellipse", x, y, w, h, **kw)
    e["roundness"] = None
    return e


def text(eid, x, y, w, h, txt, size=15, align="left", valign="top", color="#1e1e1e", container=None, **kw):
    e = base(eid, "text", x, y, w, h, stroke=color, bg="transparent", sw=1, **kw)
    e["roundness"] = None
    e["text"] = txt
    e["fontSize"] = size
    e["fontFamily"] = 3
    e["textAlign"] = align
    e["verticalAlign"] = valign
    e["containerId"] = container
    e["originalText"] = txt
    e["lineHeight"] = 1.25
    e["width"] = w
    if container:
        e["height"] = h
        e["autoResize"] = False
    else:
        lines = txt.count("\n") + 1
        e["height"] = max(h, int(lines * size * 1.25))
        e["autoResize"] = True
    return e


def _orthogonalize(points):
    if len(points) < 2:
        return points
    if len(points) == 2:
        x0, y0 = points[0]
        x1, y1 = points[1]
        if x0 != x1 and y0 != y1:
            return [[x0, y0], [x1, y0], [x1, y1]]
        return points
    out = [list(points[0])]
    for px, py in points[1:]:
        lx, ly = out[-1]
        if px != lx and py != ly:
            out.append([px, ly])
        out.append([px, py])
    return out


def arrow(eid, x, y, points, color="#1e1e1e", ss="solid", sw=2):
    points = _orthogonalize(points)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    w = max(xs) - min(xs)
    h = max(ys) - min(ys)
    e = base(eid, "arrow", x, y, w if w else 1, h if h else 1, stroke=color, bg="transparent", sw=sw, ss=ss)
    e["roundness"] = None
    e["roughness"] = 0
    e["elbowed"] = True
    e["points"] = points
    e["lastCommittedPoint"] = None
    e["startBinding"] = None
    e["endBinding"] = None
    e["startArrowhead"] = None
    e["endArrowhead"] = "triangle"
    return e


def mid_top(x, y, w, h):
    return (x + w / 2, y)


def mid_bot(x, y, w, h):
    return (x + w / 2, y + h)


def mid_left(x, y, w, h):
    return (x, y + h / 2)


def mid_right(x, y, w, h):
    return (x + w, y + h / 2)


def edge(x, y, w, h, side, t=0.5):
    """Point sur un bord ; t∈[0,1] pour espacer plusieurs flèches sur le même côté."""
    t = max(0.08, min(0.92, t))
    if side == "top":
        return (x + w * t, y)
    if side == "bot":
        return (x + w * t, y + h)
    if side == "left":
        return (x, y + h * t)
    return (x + w, y + h * t)


def arrow_abs(eid, abs_points, color="#1e1e1e", ss="solid", sw=2):
    x0, y0 = abs_points[0]
    rel = [[p[0] - x0, p[1] - y0] for p in abs_points]
    return arrow(eid, x0, y0, rel, color=color, ss=ss, sw=sw)


def status_badge(G, eid, x, y, kind, group=None):
    styles = {
        "ok": ("✅", "#2f9e44", "#b2f2bb"),
        "warn": ("⚠️", "#e67700", "#ffec99"),
        "pending": ("🟡", "#e67700", "#fff3bf"),
    }
    glyph, stroke, bg = styles[kind]
    gids = [group] if group else []
    rid, tid = f"badge-{kind}-{eid}", f"t-badge-{kind}-{eid}"
    G.append(rect(rid, x - 6, y - 10, 30, 30, stroke=stroke, bg=bg, sw=2, groupIds=gids))
    te = text(tid, x - 6, y - 10, 30, 30, glyph, size=14, align="center", valign="top", groupIds=gids)
    te["y"] = y - 10 + (30 - 18) / 2
    te["height"] = 18
    te["autoResize"] = False
    G.append(te)


def warn_badge(G, eid, x, y, group=None):
    status_badge(G, eid, x, y, "warn", group=group)


def chip(G, eid, x, y, w, h, label, *, stroke, bg, sw=1, ss="solid", size=13, color="#1e1e1e", group=None, status=None):
    gids = [group] if group else []
    rid, tid = f"c-{eid}", f"t-{eid}"
    G.append(rect(rid, x, y, w, h, stroke=stroke, bg=bg, sw=sw, ss=ss, groupIds=gids))
    lines = label.count("\n") + 1
    text_h = int(lines * size * 1.25)
    ty = y + max(0, (h - text_h) / 2)
    te = text(tid, x, ty, w, text_h, label, size=size, align="center", valign="top", color=color, groupIds=gids)
    te["autoResize"] = False
    G.append(te)
    if status:
        status_badge(G, eid, x, y, status, group=group)
    return (x, y, w, h)


def header_box(G, eid, x, y, w, h, title, blurb, *, stroke, bg, sw=2, title_color=None, group=None):
    gids = [group] if group else []
    G.append(rect(eid, x, y, w, h, stroke=stroke, bg=bg, sw=sw, groupIds=gids))
    G.append(text(f"lbl-{eid}", x + 16, y + 12, w - 32, 28, title, size=20, color=title_color or stroke, groupIds=gids))
    if blurb:
        G.append(text(f"blurb-{eid}", x + 16, y + 42, w - 32, 28, blurb, size=14, color="#495057", groupIds=gids))


G = []

GREEN, GREEN_BG, GREEN_SOFT = "#2f9e44", "#b2f2bb", "#d3f9d8"
BLUE, BLUE_BG, BLUE_SOFT = "#1971c2", "#a5d8ff", "#e7f5ff"
VIOLET, VIOLET_BG, VIOLET_SOFT = "#9c36b5", "#eebefa", "#f8f0fc"
YELLOW, YELLOW_BG = "#e67700", "#ffec99"
RED, RED_BG, RED_SOFT = "#e03131", "#ffc9c9", "#fff5f5"
RED_DARK = "#c92a2a"

MARGIN, GAP_X, GAP_Y, PAD, CGAP = 48, 80, 100, 18, 14

G.append(text("title", MARGIN, 16, 1700, 40, "Second Brain — Carte d'impacts V1 (DEC-011)", size=30))
G.append(
    text(
        "subtitle",
        MARGIN,
        56,
        1900,
        48,
        "Cycle horaire : Chatbot (message) → brain-main (skills) → brain/ (écriture) → Chatbot (contexte)\n"
        "Vert=mémoire · Bleu=système · Violet=chatbot · Jaune=hubs · Rouge=humain / hors V1 · Flèches elbow △",
        size=13,
        color="#495057",
    )
)
chip(G, "leg-ok", 1020, 18, 120, 28, "✅ validé", stroke="#2f9e44", bg="#b2f2bb", size=11, group="g-leg")
chip(G, "leg-pend", 1155, 18, 140, 28, "🟡 en attente", stroke="#e67700", bg="#fff3bf", size=11, group="g-leg")
chip(G, "leg-warn", 1310, 18, 170, 28, "⚠️ pas développé", stroke="#e67700", bg="#ffec99", size=11, group="g-leg")

# ============================================================================
# TOP — Notion | ClickUp | GitHub (inchangé structurellement)
# ============================================================================
TOP_Y, TOP_H = 118, 260
NW, CW_SEC, GW = 380, 700, 400
NX = MARGIN
CX_SEC = NX + NW + GAP_X
GX = CX_SEC + CW_SEC + GAP_X

header_box(G, "sec-notion", NX, TOP_Y, NW, TOP_H, "NOTION", "Vue humaine — notes / docs · ≠ SoT", stroke=RED, bg=RED_SOFT, sw=2, group="g-notion")
chip(G, "no-main", NX + PAD, TOP_Y + 72, NW - 2 * PAD, 38, "Notion", stroke=RED, bg=RED_BG, sw=3, size=14, group="g-notion", status="pending")
hw = (NW - 2 * PAD - CGAP) // 2
chip(G, "no-pages", NX + PAD, TOP_Y + 120, hw, 36, "pages", stroke=RED, bg=RED_BG, size=12, group="g-notion", status="pending")
chip(G, "no-db", NX + PAD + hw + CGAP, TOP_Y + 120, hw, 36, "bases de données", stroke=RED, bg=RED_BG, size=11, group="g-notion", status="pending")
chip(G, "no-mcp", NX + PAD, TOP_Y + 166, NW - 2 * PAD, 36, "intégration MCP", stroke=RED, bg=RED_BG, size=12, group="g-notion", status="pending")
chip(G, "no-conv", NX + PAD, TOP_Y + 212, NW - 2 * PAD, 30, "contrat → conventions", stroke=YELLOW, bg=YELLOW_BG, size=11, group="g-notion", status="ok")

header_box(G, "sec-clickup", CX_SEC, TOP_Y, CW_SEC, TOP_H, "CLICKUP", "Vue humaine — projection ops · ≠ SoT", stroke=RED, bg=RED_SOFT, sw=2, group="g-cu")
cw4 = (CW_SEC - 2 * PAD - 3 * CGAP) // 4
chip(G, "cu-main", CX_SEC + PAD, TOP_Y + 72, cw4, 38, "ClickUp", stroke=RED, bg=RED_BG, sw=3, size=14, group="g-cu", status="ok")
chip(G, "cu-list", CX_SEC + PAD + cw4 + CGAP, TOP_Y + 72, cw4, 38, "LIST.TASKS", stroke=RED, bg=RED_BG, size=12, group="g-cu", status="pending")
chip(G, "cu-map", CX_SEC + PAD + 2 * (cw4 + CGAP), TOP_Y + 72, cw4, 38, "mapping.yaml", stroke=YELLOW, bg=YELLOW_BG, sw=3, size=12, group="g-cu", status="ok")
chip(G, "cu-sync", CX_SEC + PAD + 3 * (cw4 + CGAP), TOP_Y + 72, cw4, 38, "/clickup · sync", stroke=RED, bg=RED_BG, size=12, group="g-cu", status="pending")
hw2 = (CW_SEC - 2 * PAD - CGAP) // 2
chip(G, "cu-tags", CX_SEC + PAD, TOP_Y + 124, hw2, 48, "étiquettes = tags locaux 1:1\n(IDEA-002)", stroke=YELLOW, bg=YELLOW_BG, sw=2, size=11, group="g-cu", status="ok")
chip(G, "cu-proj", CX_SEC + PAD + hw2 + CGAP, TOP_Y + 124, hw2, 48, "projection brain → ClickUp\n≠ SoT", stroke=YELLOW, bg=YELLOW_BG, sw=2, size=11, group="g-cu", status="ok")
chip(G, "cu-conv", CX_SEC + PAD, TOP_Y + 186, CW_SEC - 2 * PAD, 40, "contrat → conventions ClickUp", stroke=YELLOW, bg=YELLOW_BG, size=12, group="g-cu", status="ok")

header_box(G, "sec-github", GX, TOP_Y, GW, TOP_H, "GITHUB", "Vue humaine — code & revue · ≠ SoT", stroke=RED, bg=RED_SOFT, sw=2, group="g-gh")
chip(G, "gh-main", GX + PAD, TOP_Y + 72, GW - 2 * PAD, 38, "GitHub", stroke=RED, bg=RED_BG, sw=3, size=14, group="g-gh", status="pending")
ghw = (GW - 2 * PAD - CGAP) // 2
chip(G, "gh-repos", GX + PAD, TOP_Y + 120, ghw, 36, "repos", stroke=RED, bg=RED_BG, size=12, group="g-gh", status="pending")
chip(G, "gh-issues", GX + PAD + ghw + CGAP, TOP_Y + 120, ghw, 36, "issues", stroke=RED, bg=RED_BG, size=12, group="g-gh", status="pending")
chip(G, "gh-pr", GX + PAD, TOP_Y + 166, ghw, 36, "PR", stroke=RED, bg=RED_BG, size=12, group="g-gh", status="pending")
chip(G, "gh-web", GX + PAD + ghw + CGAP, TOP_Y + 166, ghw, 36, "via web-starter", stroke=VIOLET, bg=VIOLET_BG, size=11, group="g-gh", status="ok")
chip(G, "gh-conv", GX + PAD, TOP_Y + 214, GW - 2 * PAD, 28, "contrat → conventions", stroke=YELLOW, bg=YELLOW_BG, size=11, group="g-gh", status="ok")

# ============================================================================
# CYCLE — triangle horaire : Chatbot (haut) → brain-main (bas-droite) → brain/ (bas-gauche)
# ============================================================================
AW, AH = 420, 620
BW, BH = 440, 640
MW, MH = 400, 620

# Centre du cycle sous les hubs (assez bas pour ne pas chevaucher Notion/CU/GH)
OCC_X = (NX + GX + GW) / 2
OCC_Y = TOP_Y + TOP_H + 900
RADIUS = 500

def panel_xy(angle_deg, pw, ph):
    rad = math.radians(angle_deg)
    pcx = OCC_X + RADIUS * math.cos(rad)
    pcy = OCC_Y + RADIUS * math.sin(rad)
    return pcx - pw / 2, pcy - ph / 2

# Angles écran : 0=est, 90=sud — Chatbot à -90° (nord), brain-main à 30°, brain à 150°
AX, AY = panel_xy(-90, AW, AH)
BX, BY = panel_xy(30, BW, BH)
MX, MY = panel_xy(150, MW, MH)

# --- Chatbot (haut du cycle) ---
header_box(G, "sec-agents", AX, AY, AW, AH, "CHATBOTS / AGENTS", "① Reçoit le message · nourrit le tour suivant", stroke=VIOLET, bg=VIOLET_SOFT, sw=2, group="g-agents")
ay = AY + 72
chip(G, "a-cursor", AX + PAD, ay, AW - 2 * PAD, 36, "Cursor", stroke=VIOLET, bg=VIOLET_BG, sw=2, size=13, group="g-agents", status="ok")
G.append(text("lbl-a-flow", AX + PAD, ay + 44, AW - 2 * PAD, 18, "Flux chatbot", size=13, color=VIOLET, groupIds=["g-agents"]))
cw3 = (AW - 2 * PAD - 2 * CGAP) // 3
chip(G, "a-contexte", AX + PAD, ay + 66, cw3, 40, "Contexte", stroke=VIOLET, bg=VIOLET_BG, sw=2, size=13, group="g-agents", status="ok")
chip(G, "a-prompt", AX + PAD + cw3 + CGAP, ay + 66, cw3, 40, "Prompt", stroke=VIOLET, bg=VIOLET_BG, sw=2, size=13, group="g-agents", status="ok")
chip(G, "a-resultat", AX + PAD + 2 * (cw3 + CGAP), ay + 66, cw3, 40, "Résultat", stroke=VIOLET, bg=VIOLET_BG, sw=2, size=13, group="g-agents", status="ok")
ahw = (AW - 2 * PAD - CGAP) // 2
chip(G, "a-chats", AX + PAD, ay + 120, ahw, 34, "chats", stroke=VIOLET, bg=VIOLET_BG, size=12, group="g-agents", status="ok")
chip(G, "a-runtime", AX + PAD + ahw + CGAP, ay + 120, ahw, 34, "runtime agent", stroke=VIOLET, bg=VIOLET_BG, size=12, group="g-agents", status="ok")
chip(G, "a-agents", AX + PAD, ay + 166, AW - 2 * PAD, 34, "agents", stroke=VIOLET, bg=VIOLET_BG, size=13, group="g-agents", status="ok")
chip(G, "a-md-depot", AX + PAD, ay + 212, ahw, 34, "AGENTS.md dépôt", stroke=BLUE, bg=BLUE_BG, size=11, group="g-agents", status="ok")
chip(G, "a-md-tpl", AX + PAD + ahw + CGAP, ay + 212, ahw, 34, "AGENTS.md tpl", stroke=BLUE, bg=BLUE_BG, size=11, group="g-agents", status="ok")
G.append(text("lbl-a-skills", AX + PAD, ay + 256, AW - 2 * PAD, 18, "Skills (procédures)", size=13, color=VIOLET, groupIds=["g-agents"]))
agent_skills = [("second-brain", "ok"), ("clickup", "ok"), ("COMMANDS", "ok"), ("MCP", "pending"), ("Tri", "pending"), ("Agent", "pending"), ("Rules", "pending"), ("Skills Perso", "pending")]
asw = (AW - 2 * PAD - 3 * CGAP) // 4
for i, (name, st_status) in enumerate(agent_skills):
    col, row = i % 4, i // 4
    chip(G, f"a-sk-{i}-{name.replace(' ', '')}", AX + PAD + col * (asw + CGAP), ay + 278 + row * 42, asw, 34, name, stroke=VIOLET, bg=VIOLET_BG, size=11, group="g-agents", status=st_status)
G.append(text("lbl-a-slash", AX + PAD, ay + 372, AW - 2 * PAD, 18, "Commandes slash", size=13, color=VIOLET, groupIds=["g-agents"]))
for i, name in enumerate(["cadrer", "build", "go", "note", "sync", "faire", "clickup"]):
    col, row = i % 4, i // 4
    chip(G, f"as-{name}", AX + PAD + col * (asw + CGAP), ay + 394 + row * 42, asw, 34, f"/{name}", stroke=VIOLET, bg=VIOLET_BG, size=12, group="g-agents", status="ok")
chip(G, "a-write", AX + PAD, ay + 488, AW - 2 * PAD, 34, "écrit brain/ après oui", stroke=BLUE, bg=BLUE_BG, size=12, group="g-agents", status="ok")
chip(G, "a-lit-conv", AX + PAD, ay + 532, AW - 2 * PAD, 34, "lit conventions", stroke=YELLOW, bg=YELLOW_BG, size=12, group="g-agents", status="ok")
chip(G, "a-yes", AX + PAD, ay + 576, AW - 2 * PAD, 30, "après confirmation", stroke=BLUE, bg=BLUE_BG, size=12, group="g-agents", status="ok")

# --- brain-main (bas-droite) ---
G.append(rect("hub-brain-main", BX, BY, BW, BH, stroke=BLUE, bg=BLUE_SOFT, sw=3, groupIds=["g-sys"]))
G.append(text("t-sys-title", BX + 14, BY + 10, BW - 28, 26, "brain-main — SYSTÈME", size=18, align="left", color=BLUE, groupIds=["g-sys"]))
G.append(text("t-sys-blurb", BX + 14, BY + 36, BW - 28, 24, "② Analyse via skills · règles", size=13, align="left", color="#495057", groupIds=["g-sys"]))
sx0, sy0 = BX + PAD, BY + 68
sw2 = (BW - 2 * PAD - CGAP) // 2
chip(G, "s-yaml", sx0, sy0, sw2, 32, ".second-brain.yaml", stroke=YELLOW, bg=YELLOW_BG, sw=3, size=10, group="g-sys", status="ok")
chip(G, "s-manifest", sx0 + sw2 + CGAP, sy0, sw2, 32, "manifeste", stroke=YELLOW, bg=YELLOW_BG, sw=2, size=11, group="g-sys", status="ok")
chip(G, "s-agents-d", sx0, sy0 + 42, sw2, 32, "AGENTS.md dépôt", stroke=BLUE, bg=BLUE_BG, size=10, group="g-sys", status="ok")
chip(G, "s-agents-t", sx0 + sw2 + CGAP, sy0 + 42, sw2, 32, "AGENTS.md tpl", stroke=BLUE, bg=BLUE_BG, size=10, group="g-sys", status="ok")
for i, name in enumerate(["taxonomy", "schema", "memory-policy", "naming"]):
    col, row = i % 2, i // 2
    chip(G, f"s-conv-{name}", sx0 + col * (sw2 + CGAP), sy0 + 90 + row * 40, sw2, 32, name, stroke=YELLOW, bg=YELLOW_BG, size=10, group="g-sys", status="ok")
cw3s = (BW - 2 * PAD - 2 * CGAP) // 3
chip(G, "s-c-gh", sx0, sy0 + 180, cw3s, 30, "→ GitHub", stroke=RED, bg=RED_BG, size=10, group="g-sys", status="ok")
chip(G, "s-c-cu", sx0 + cw3s + CGAP, sy0 + 180, cw3s, 30, "→ ClickUp", stroke=RED, bg=RED_BG, size=10, group="g-sys", status="ok")
chip(G, "s-c-no", sx0 + 2 * (cw3s + CGAP), sy0 + 180, cw3s, 30, "→ Notion", stroke=RED, bg=RED_BG, size=10, group="g-sys", status="ok")
for i, name in enumerate(["second-brain", "clickup", "COMMANDS"]):
    chip(G, f"sk-canon-{name}", sx0 + i * ((BW - 2 * PAD - 2 * CGAP) // 3 + CGAP), sy0 + 222, (BW - 2 * PAD - 2 * CGAP) // 3, 30, name, stroke=VIOLET, bg=VIOLET_BG, size=10, group="g-sys", status="ok")
sw4 = (BW - 2 * PAD - 3 * CGAP) // 4
for i, name in enumerate(["cadrer", "build", "go", "note", "sync", "clickup", "faire"]):
    col, row = i % 4, i // 4
    chip(G, f"sk-{name}", sx0 + col * (sw4 + CGAP), sy0 + 264 + row * 38, sw4, 30, f"/{name}", stroke=VIOLET, bg=VIOLET_BG, size=11, group="g-sys", status="ok")
chip(G, "s-docs", sx0, sy0 + 350, sw2, 30, "docs/00–05", stroke=BLUE, bg=BLUE_BG, size=11, group="g-sys", status="ok")
chip(G, "s-dec", sx0 + sw2 + CGAP, sy0 + 350, sw2, 30, "DEC-001…012", stroke=BLUE, bg=BLUE_BG, size=11, group="g-sys", status="ok")
chip(G, "s-integ", sx0, sy0 + 392, sw2, 30, "integrations/", stroke=BLUE, bg=BLUE_BG, size=11, group="g-sys", status="ok")
chip(G, "s-imap", sx0 + sw2 + CGAP, sy0 + 392, sw2, 30, "INFORMATION_MAP", stroke=BLUE, bg=BLUE_BG, size=10, group="g-sys", status="ok")
chip(G, "s-integrate", sx0, sy0 + 434, BW - 2 * PAD, 30, "travaille avec Chatbot", stroke=VIOLET, bg=VIOLET_BG, sw=2, size=11, group="g-sys", status="pending")
chip(G, "sec-systeme-note", BX + PAD, BY + BH - 42, BW - 2 * PAD, 28, "SYSTÈME (= brain-main)", stroke=BLUE, bg=BLUE_BG, size=10, group="g-sys", status="ok")

# --- brain/ SoT (bas-gauche) ---
header_box(G, "sec-memoire", MX, MY, MW, MH, "brain/ — SoT", "③ Écriture durable · source de vérité", stroke=GREEN, bg=GREEN_SOFT, sw=3, group="g-brain")
G.append(ellipse("hub-brain", MX + MW - 66, MY + 8, 48, 48, stroke=GREEN, bg=GREEN_BG, sw=3, groupIds=["g-brain"]))
G.append(text("t-brain-title", MX + PAD, MY + 70, MW - 2 * PAD, 24, "🧠 mémoire du dépôt", size=15, align="center", color=GREEN, groupIds=["g-brain"]))
G.append(text("t-brain-blurb", MX + PAD, MY + 98, MW - 2 * PAD, 36, "SoT pour Chatbot & projet\nNotion/CU/GH = vues humaines", size=12, align="center", color="#495057", groupIds=["g-brain"]))
mem_chips = [
    ("m-state", "STATE.md", YELLOW, YELLOW_BG, 3, "ok"),
    ("m-overview", "OVERVIEW", GREEN, GREEN_BG, 2, "ok"),
    ("m-arch", "ARCHITECTURE", GREEN, GREEN_BG, 2, "ok"),
    ("m-dec", "DECISIONS", GREEN, GREEN_BG, 2, "ok"),
    ("m-tasks", "TASKS (JSONL)", GREEN, GREEN_BG, 2, "ok"),
    ("m-ideas", "registre idées", GREEN, GREEN_BG, 2, "ok"),
    ("m-refs", "références/ · lots", GREEN, GREEN_BG, 2, "ok"),
    ("m-inbox", "✖ Inbox humaine", RED_DARK, "#ffe3e3", 2, "ok"),
]
cw, ch = (MW - 2 * PAD - CGAP) // 2, 42
mx0, my0 = MX + PAD, MY + 148
for i, (eid, label, st, bg, sw, st_status) in enumerate(mem_chips):
    col, row = i % 2, i // 2
    chip(G, eid, mx0 + col * (cw + CGAP), my0 + row * (ch + CGAP), cw, ch, label, stroke=st, bg=bg, sw=sw, ss=("dashed" if eid == "m-inbox" else "solid"), size=12, color=(RED_DARK if eid == "m-inbox" else "#1e1e1e"), group="g-brain", status=st_status)
flow_y = my0 + 4 * (ch + CGAP) + 12
chip(G, "m-flow", MX + PAD, flow_y, MW - 2 * PAD, 44, "alimenté par Chatbot + brain-main", stroke=GREEN, bg=GREEN_BG, size=12, group="g-brain", status="ok")
chip(G, "m-human", MX + PAD, flow_y + 56, MW - 2 * PAD, 44, "projeté vers Notion / ClickUp / GitHub", stroke=YELLOW, bg=YELLOW_BG, size=11, group="g-brain", status="ok")
chip(G, "m-readback", MX + PAD, flow_y + 112, MW - 2 * PAD, 44, "lu par Chatbot pour bosser", stroke=VIOLET, bg=VIOLET_BG, size=12, group="g-brain", status="ok")

# ============================================================================
# AMÉLIORATIONS — 3 petites cartes au centre du cycle
# ============================================================================
IMP_W, IMP_H = 200, 78
# a) feedback brain → chatbot (près du côté haut-gauche du cycle)
FB_X, FB_Y = OCC_X - 220, OCC_Y - 160
chip(G, "improve-feedback", FB_X, FB_Y, IMP_W, IMP_H, "↩ Feedback\nbrain → chatbot\naprès écriture", stroke=VIOLET, bg=VIOLET_BG, sw=3, size=12, group="g-improve", status="pending")
# b) conflit brain-main ↔ brain (bas du cycle)
CF_X, CF_Y = OCC_X - IMP_W / 2, OCC_Y + 40
chip(G, "improve-conflict", CF_X, CF_Y, IMP_W, IMP_H, "⚡ Conflit\nbrain-main ↔ brain/\nrègles vs SoT", stroke=YELLOW, bg=YELLOW_BG, sw=3, size=12, group="g-improve", status="pending")
# c) journal de cycle (centre)
LG_X, LG_Y = OCC_X + 30, OCC_Y - 160
chip(G, "improve-cycle-log", LG_X, LG_Y, IMP_W, IMP_H, "📓 Journal cycle\ntrace chaque\nitération", stroke=BLUE, bg=BLUE_BG, sw=3, size=12, group="g-improve", status="pending")
G.append(text("lbl-cycle", OCC_X - 90, OCC_Y - 20, 180, 36, "CYCLE\nhoraire →", size=16, align="center", color="#495057", groupIds=["g-improve"]))

# ============================================================================
# BOTTOM — templates + hors V1
# ============================================================================
CYCLE_BOTTOM = max(BY + BH, MY + MH, AY + AH)
BY_BOTTOM = CYCLE_BOTTOM + GAP_Y
TW = 420
header_box(G, "sec-tpl", MARGIN, BY_BOTTOM, TW, 220, "TEMPLATES", "Amorces de projets futurs", stroke=VIOLET, bg=VIOLET_SOFT, sw=2, group="g-tpl")
chip(G, "tpl-proj", MARGIN + PAD, BY_BOTTOM + 72, TW - 2 * PAD, 48, "project/ + AGENTS généraliste", stroke=VIOLET, bg=VIOLET_BG, size=13, group="g-tpl", status="ok")
thw = (TW - 2 * PAD - CGAP) // 2
chip(G, "tpl-web", MARGIN + PAD, BY_BOTTOM + 134, thw, 48, "web-starter", stroke=VIOLET, bg=VIOLET_BG, ss="dashed", size=12, group="g-tpl", status="ok")
chip(G, "tpl-mob", MARGIN + PAD + thw + CGAP, BY_BOTTOM + 134, thw, 48, "mobile-starter", stroke=VIOLET, bg=VIOLET_BG, ss="dashed", size=12, group="g-tpl", status="ok")

RT_X = MARGIN + TW + GAP_X
RT_W = (GX + GW) - RT_X
header_box(G, "sec-runtime", RT_X, BY_BOTTOM, RT_W, 220, "HORS V1 — runtime scaffolding", "Gardé, pas développé — aucune flèche active depuis skills V1", stroke=RED_DARK, bg="#ffe3e3", sw=2, title_color=RED_DARK, group="g-rt")
for e in G:
    if e["id"] == "sec-runtime":
        e["strokeStyle"] = "dashed"
        e["fillStyle"] = "hachure"
        break
rtw = (RT_W - 2 * PAD - 5 * CGAP) // 6
for i, name in enumerate(["core", "MCP", "CLI", "scripts", "tests", "adapters"]):
    rx, ry = RT_X + PAD + i * (rtw + CGAP), BY_BOTTOM + 78
    chip(G, f"rt-{name}", rx, ry, rtw, 48, name, stroke=RED_DARK, bg=RED_BG, ss="dashed", size=13, color=RED_DARK, group="g-rt")
    warn_badge(G, f"rt-{name}", rx, ry, group="g-rt")
chip(G, "rt-sqlite", RT_X + PAD, BY_BOTTOM + 144, RT_W - 2 * PAD, 42, "SQLite brain/runtime/ · skills research|planning|implementation|review|memory", stroke=RED_DARK, bg=RED_BG, ss="dashed", size=12, color=RED_DARK, group="g-rt")
warn_badge(G, "rt-sqlite", RT_X + PAD, BY_BOTTOM + 144, group="g-rt")
warn_badge(G, "sec-runtime", RT_X, BY_BOTTOM, group="g-rt")

# ============================================================================
# FLÈCHES — boucle horaire + hubs + améliorations + internes
# ============================================================================
agents_b = (AX, AY, AW, AH)
sys_b = (BX, BY, BW, BH)
brain_b = (MX, MY, MW, MH)
notion = (NX, TOP_Y, NW, TOP_H)
clickup = (CX_SEC, TOP_Y, CW_SEC, TOP_H)
github = (GX, TOP_Y, GW, TOP_H)
tpl = (MARGIN, BY_BOTTOM, TW, 220)
fb_b = (FB_X, FB_Y, IMP_W, IMP_H)
cf_b = (CF_X, CF_Y, IMP_W, IMP_H)
lg_b = (LG_X, LG_Y, IMP_W, IMP_H)

LEFT_X = min(MX, NX) - 36
RIGHT_X = max(BX + BW, GX + GW) + 36
# Couloirs dédiés (X/Y uniques) — aucune superpositions
LANE_R_CYCLE = BX + BW + 55          # ① Chatbot → sys (extérieur droite proche)
LANE_R_OUTER = RIGHT_X + 10          # retour secondaire sys → chatbot
LANE_L_CYCLE = MX - 55               # ③ brain → chatbot
LANE_L_OUTER = MX - 100              # secondaire / hubs
LANE_BOT_CYCLE = max(BY + BH, MY + MH) + 50   # ② sys → brain
LANE_BOT_SEC = LANE_BOT_CYCLE + 55            # secondaire bas
LANE_UNDER_CHAT = AY + AH + 45       # sous chatbot (écriture directe / log)
LANE_ABOVE_SYS = BY - 45             # au-dessus de brain-main
LANE_ABOVE_BRAIN = MY - 45           # au-dessus de brain/

# --- Boucle horaire principale (3 couloirs séparés) ---
# ① Chatbot (bord droit haut) → brain-main (bord haut droite) via LANE_R_CYCLE
p1 = edge(*agents_b, "right", 0.35)
p1b = edge(*sys_b, "top", 0.65)
G.append(
    arrow_abs(
        "a-sys-agents-1",
        [p1, (LANE_R_CYCLE, p1[1]), (LANE_R_CYCLE, LANE_ABOVE_SYS), (p1b[0], LANE_ABOVE_SYS), p1b],
        color=VIOLET,
        sw=3,
    )
)
G.append(text("lbl-ag", LANE_R_CYCLE + 8, (p1[1] + LANE_ABOVE_SYS) / 2 - 10, 120, 40, "① message\n→ analyse", size=12, color=VIOLET))

# ② brain-main (bord bas) → brain/ (bord bas) via LANE_BOT_CYCLE — pas le côté gauche
p2 = edge(*sys_b, "bot", 0.35)
p2b = edge(*brain_b, "bot", 0.65)
G.append(
    arrow_abs(
        "a-sys-brain",
        [p2, (p2[0], LANE_BOT_CYCLE), (p2b[0], LANE_BOT_CYCLE), p2b],
        color=BLUE,
        sw=3,
    )
)
G.append(text("lbl-sys-brain", (p2[0] + p2b[0]) / 2 - 40, LANE_BOT_CYCLE - 24, 100, 22, "② écrit SoT", size=12, color=BLUE))

# ③ brain/ (bord gauche haut) → Chatbot (bord gauche bas) via LANE_L_CYCLE
p3 = edge(*brain_b, "left", 0.25)
p3b = edge(*agents_b, "left", 0.70)
G.append(
    arrow_abs(
        "a-brain-agents-read",
        [p3, (LANE_L_CYCLE, p3[1]), (LANE_L_CYCLE, p3b[1]), p3b],
        color=VIOLET,
        ss="dashed",
        sw=3,
    )
)
G.append(text("lbl-read", LANE_L_CYCLE - 95, (p3[1] + p3b[1]) / 2 - 10, 90, 22, "③ contexte", size=12, color=VIOLET))

# --- Secondaires (couloirs encore plus extérieurs) ---
# écriture directe Chatbot → brain (sous chatbot, puis gauche)
p4 = edge(*agents_b, "bot", 0.30)
p4b = edge(*brain_b, "top", 0.40)
G.append(
    arrow_abs(
        "a-agents-brain",
        [p4, (p4[0], LANE_UNDER_CHAT), (LANE_L_OUTER, LANE_UNDER_CHAT), (LANE_L_OUTER, LANE_ABOVE_BRAIN), (p4b[0], LANE_ABOVE_BRAIN), p4b],
        color=BLUE,
        ss="dashed",
        sw=2,
    )
)
# retour sys → chatbot (extérieur droite lointain)
p5 = edge(*sys_b, "right", 0.40)
p5b = edge(*agents_b, "bot", 0.75)
G.append(
    arrow_abs(
        "a-sys-agents-2",
        [p5, (LANE_R_OUTER, p5[1]), (LANE_R_OUTER, LANE_UNDER_CHAT + 35), (p5b[0], LANE_UNDER_CHAT + 35), p5b],
        color=VIOLET,
        ss="dashed",
        sw=2,
    )
)
# alternatif chatbot → sys (dessus sys, couloir haut)
p6 = edge(*agents_b, "right", 0.15)
p6b = edge(*sys_b, "top", 0.30)
G.append(
    arrow_abs(
        "a-agents-sys-3",
        [p6, (LANE_R_CYCLE + 45, p6[1]), (LANE_R_CYCLE + 45, LANE_ABOVE_SYS - 40), (p6b[0], LANE_ABOVE_SYS - 40), p6b],
        color=VIOLET,
        ss="dashed",
        sw=2,
    )
)
G.append(text("lbl-integ", OCC_X - 60, LANE_BOT_CYCLE - 70, 140, 36, "ensemble\nChatbot↔système", size=12, color=VIOLET, align="center"))

# --- Améliorations : stubs courts, bords dédiés, sans croiser la boucle ---
# Feedback (haut-gauche) : brain top → fb → chatbot left (t distincts)
fb_in = edge(*fb_b, "bot", 0.5)
fb_out = edge(*fb_b, "top", 0.5)
br_fb = edge(*brain_b, "top", 0.20)
ag_fb = edge(*agents_b, "left", 0.45)
G.append(
    arrow_abs(
        "a-improve-feedback-src",
        [br_fb, (br_fb[0], LANE_ABOVE_BRAIN + 20), (fb_in[0], LANE_ABOVE_BRAIN + 20), fb_in],
        color=VIOLET,
        ss="dashed",
        sw=2,
    )
)
G.append(
    arrow_abs(
        "a-improve-feedback",
        [fb_out, (fb_out[0], ag_fb[1]), ag_fb],
        color=VIOLET,
        sw=2,
    )
)

# Conflit (bas centre) : sys left & brain right → conflit (couloir LANE_CF_Y, au-dessus de ②)
cf_r = edge(*cf_b, "right", 0.5)
cf_l = edge(*cf_b, "left", 0.5)
sys_cf = edge(*sys_b, "left", 0.55)
br_cf = edge(*brain_b, "right", 0.55)
G.append(
    arrow_abs(
        "a-improve-conflict-sys",
        [sys_cf, (sys_cf[0] - 40, sys_cf[1]), (sys_cf[0] - 40, cf_r[1]), cf_r],
        color=YELLOW,
        sw=2,
    )
)
G.append(
    arrow_abs(
        "a-improve-conflict-brain",
        [br_cf, (br_cf[0] + 40, br_cf[1]), (br_cf[0] + 40, cf_l[1]), cf_l],
        color=YELLOW,
        sw=2,
    )
)

# Journal (centre-droit) : 3 stubs depuis bords intérieurs, Y/X distincts
lg_t = edge(*lg_b, "top", 0.5)
lg_r = edge(*lg_b, "right", 0.5)
lg_l = edge(*lg_b, "left", 0.5)
ag_lg = edge(*agents_b, "bot", 0.55)
sys_lg = edge(*sys_b, "left", 0.25)
br_lg = edge(*brain_b, "right", 0.25)
G.append(
    arrow_abs(
        "a-improve-log-agents",
        [ag_lg, (ag_lg[0], LANE_UNDER_CHAT - 15), (lg_t[0], LANE_UNDER_CHAT - 15), lg_t],
        color=BLUE,
        ss="dashed",
        sw=2,
    )
)
G.append(
    arrow_abs(
        "a-improve-log-sys",
        [sys_lg, (OCC_X + 120, sys_lg[1]), (OCC_X + 120, lg_r[1]), lg_r],
        color=BLUE,
        ss="dashed",
        sw=2,
    )
)
G.append(
    arrow_abs(
        "a-improve-log-brain",
        [br_lg, (OCC_X - 40, br_lg[1]), (OCC_X - 40, lg_l[1]), lg_l],
        color=BLUE,
        ss="dashed",
        sw=2,
    )
)

# --- Hubs humains → brain/ ---
n0, b_left = mid_bot(*notion), mid_left(*brain_b)
G.append(arrow_abs("a-notion-brain", [n0, (LEFT_X, n0[1]), (LEFT_X, b_left[1]), b_left], color=YELLOW, ss="dashed", sw=2))
c0, b_top = mid_bot(*clickup), mid_top(*brain_b)
# ClickUp vers brain : passe par la gauche du chatbot pour rester extérieur
band = TOP_Y + TOP_H + 40
G.append(arrow_abs("a-brain-cu", [c0, (c0[0], band), (LEFT_X + 20, band), (LEFT_X + 20, b_top[1]), b_top], color=YELLOW, ss="solid", sw=3))
G.append(text("lbl-proj", c0[0] - 20, band - 20, 100, 20, "vue humaine", size=11, color=YELLOW))
g0, b_right = mid_bot(*github), mid_right(*brain_b)
G.append(arrow_abs("a-github-brain", [g0, (RIGHT_X, g0[1]), (RIGHT_X, BY + BH + 20), (b_right[0], BY + BH + 20), b_right], color=YELLOW, ss="dashed", sw=2))

# --- Flux interne chatbot ---
ctx = (AX + PAD, ay + 66, cw3, 40)
prm = (AX + PAD + cw3 + CGAP, ay + 66, cw3, 40)
res = (AX + PAD + 2 * (cw3 + CGAP), ay + 66, cw3, 40)
cur = (AX + PAD, ay, AW - 2 * PAD, 36)
agt = (AX + PAD, ay + 166, AW - 2 * PAD, 34)
c_bot, ctx_top = mid_bot(*cur), mid_top(*ctx)
G.append(arrow_abs("a-cur-ctx", [c_bot, (c_bot[0], (c_bot[1] + ctx_top[1]) / 2), (ctx_top[0], (c_bot[1] + ctx_top[1]) / 2), ctx_top], color=VIOLET, sw=2))
G.append(arrow_abs("a-ctx-prompt", [mid_right(*ctx), mid_left(*prm)], color=VIOLET, sw=2))
G.append(arrow_abs("a-prompt-res", [mid_right(*prm), mid_left(*res)], color=VIOLET, sw=2))
r_bot, a_top2 = mid_bot(*res), mid_top(*agt)
G.append(arrow_abs("a-res-agents", [r_bot, (r_bot[0], (r_bot[1] + a_top2[1]) / 2), (a_top2[0], (r_bot[1] + a_top2[1]) / 2), a_top2], color=VIOLET, sw=2))

# yaml → AGENTS.md
yaml_box = (sx0, sy0, sw2, 32)
md_box = (AX + PAD, ay + 212, ahw, 34)
y0, md_left = mid_top(*yaml_box), mid_left(*md_box)
G.append(arrow_abs("a-yaml-agents", [y0, (y0[0], band + 20), (RIGHT_X - 20, band + 20), (RIGHT_X - 20, md_left[1]), md_left], color=YELLOW, ss="dashed", sw=2))

# conventions → ClickUp
conv_box = (sx0, sy0 + 90, sw2, 32)
cv0, cu_bot = mid_left(*conv_box), mid_bot(*clickup)
G.append(arrow_abs("a-conv-cu", [cv0, (LEFT_X - 20, cv0[1]), (LEFT_X - 20, cu_bot[1]), cu_bot], color=YELLOW, ss="dashed", sw=2))

# manifeste → templates
man_box = (sx0 + sw2 + CGAP, sy0, sw2, 32)
t_top = mid_top(*tpl)
m0 = mid_bot(*man_box)
G.append(arrow_abs("a-man-tpl", [m0, (LEFT_X - 40, m0[1]), (LEFT_X - 40, t_top[1]), t_top], color=GREEN, sw=2))

header_box(G, "sec-systeme", BX - 10000, BY - 10000, 10, 10, "SYSTÈME — brain-main", "voir panneau brain-main", stroke=BLUE, bg=BLUE_SOFT, sw=1, group="g-sys")

doc = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": G,
    "appState": {
        "gridSize": None,
        "viewBackgroundColor": "#ffffff",
        "scrollX": 0,
        "scrollY": 0,
        "zoom": {"value": 0.22},
    },
    "files": {},
}
OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"OK {len(G)} elements → {OUT}")
ids = {e["id"] for e in G}
required = [
    "hub-brain", "hub-brain-main", "sec-notion", "sec-clickup", "sec-github", "sec-agents",
    "sec-systeme", "sec-tpl", "sec-runtime", "sec-memoire",
    "c-a-contexte", "c-a-prompt", "c-a-resultat", "c-m-state", "c-s-yaml", "c-rt-core",
    "c-improve-feedback", "c-improve-conflict", "c-improve-cycle-log",
    "a-sys-brain", "a-brain-agents-read", "a-sys-agents-1", "a-notion-brain",
]
missing = [r for r in required if r not in ids]
print("missing", missing)
print(f"panels: chatbot=({AX:.0f},{AY:.0f}) sys=({BX:.0f},{BY:.0f}) brain=({MX:.0f},{MY:.0f}) occ=({OCC_X:.0f},{OCC_Y:.0f})")
print(f"arrows={sum(1 for e in G if e['type']=='arrow')}")
