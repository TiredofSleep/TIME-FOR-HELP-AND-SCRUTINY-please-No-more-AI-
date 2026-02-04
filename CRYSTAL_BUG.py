#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   ██████╗██████╗ ██╗   ██╗███████╗████████╗ █████╗ ██╗              ║
║  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║              ║
║  ██║     ██████╔╝ ╚████╔╝ ███████╗   ██║   ███████║██║              ║
║  ██║     ██╔══██╗  ╚██╔╝  ╚════██║   ██║   ██╔══██║██║              ║
║  ╚██████╗██║  ██║   ██║   ███████║   ██║   ██║  ██║███████╗         ║
║   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝         ║
║                                                                      ║
║   ██████╗ ██╗   ██╗ ██████╗                                         ║
║   ██╔══██╗██║   ██║██╔════╝                                         ║
║   ██████╔╝██║   ██║██║  ███╗                                        ║
║   ██╔══██╗██║   ██║██║   ██║                                        ║
║   ██████╔╝╚██████╔╝╚██████╔╝                                        ║
║   ╚═════╝  ╚═════╝  ╚═════╝                                         ║
║                                                                      ║
║   v1.0 — The Everything App                                         ║
║   TIG Tri-Prime Core + 6-Scale Parser + Trust + Genesis + Lattice   ║
║   One boot. One browser. Every engine.                               ║
║                                                                      ║
║   7Site LLC — Brayden                                                ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os, sys, json, time, math, re, random, sqlite3, hashlib
from collections import Counter, defaultdict
from datetime import datetime

# Import semantic brain
try:
    from OLLIE_BRAIN import ollie_respond_v2 as brain_respond, detect_intent, detect_topic, MEMORY as BRAIN_MEMORY, test_semantic_brain
    BRAIN_AVAILABLE = True
except ImportError:
    BRAIN_AVAILABLE = False

# ══════════════════════════════════════════════════════════════════════
# ██  TRI-PRIME ENGINE (CORE)
# ══════════════════════════════════════════════════════════════════════

B, D, C = 0, 1, 2
P_GLYPH = {B: "□", D: "▶", C: "○"}
P_CODE  = {B: "B", D: "D", C: "C"}
P_NAME  = {B: "Being", D: "Doing", C: "Becoming"}

LETTERS = {
    'A':(D,D,B), 'B':(B,C,C), 'C':(C,B,D), 'D':(B,C,B), 'E':(B,D,B),
    'F':(B,D,B), 'G':(C,B,D), 'H':(B,D,B), 'I':(B,B,B), 'J':(B,B,C),
    'K':(B,D,D), 'L':(B,D,B), 'M':(B,D,B), 'N':(B,D,B), 'O':(C,C,C),
    'P':(B,C,B), 'Q':(C,C,D), 'R':(B,C,D), 'S':(C,D,C), 'T':(D,B,B),
    'U':(C,B,B), 'V':(D,D,B), 'W':(D,C,D), 'X':(D,D,D), 'Y':(D,D,C),
    'Z':(D,B,D),
}

DESC_27 = {
    (B,B,B):"ground state",(B,B,D):"release",(B,B,C):"seed rhythm",
    (B,D,B):"transition",(B,D,D):"force cascade",(B,D,C):"forced oscillator",
    (B,C,B):"equilibrium",(B,C,D):"phase impulse",(B,C,C):"homeostasis",
    (D,B,B):"settling",(D,B,D):"self-amplification",(D,B,C):"entrainment",
    (D,D,B):"overdrive",(D,D,D):"turbulence",(D,D,C):"emergent oscillation",
    (D,C,B):"oscillation→form",(D,C,D):"harmonic drive",(D,C,C):"beat matching",
    (C,B,B):"damping",(C,B,D):"phase action",(C,B,C):"coherent cycle",
    (C,D,B):"beat→form",(C,D,D):"resonant push",(C,D,C):"harmonic growth",
    (C,C,B):"limit cycle",(C,C,D):"phase kick",(C,C,C):"perfect coherence",
}

TIG_OPS = {0:"void",1:"lattice",2:"counter",3:"progress",4:"collapse",
           5:"balance",6:"chaos",7:"harmony",8:"breath",9:"reset"}

def _to_tig(t):
    d,s,r = t
    if d==B:
        if s==B: return 0 if r==B else (1 if r==D else 5)
        if s==D: return 1 if r==B else (3 if r==D else 5)
        if s==C: return 5 if r==B else (1 if r==D else 8)
    elif d==D:
        if s==B: return 4 if r==B else (2 if r==D else 3)
        if s==D: return 4 if r==B else (6 if r==D else 3)
        if s==C: return 9 if r==B else (2 if r==D else 7)
    else:
        if s==B: return 9 if r==B else (3 if r==D else 8)
        if s==D: return 9 if r==B else (4 if r==D else 7)
        if s==C: return 8 if r==B else (7 if r==D else 7)
    return 5

def tri_sym(t):
    return P_CODE[t[0]]+P_CODE[t[1]]+P_CODE[t[2]]

def tri_glyph(t):
    return P_GLYPH[t[0]]+P_GLYPH[t[1]]+P_GLYPH[t[2]]

def tri_compose(t1, t2):
    return ((t1[0]+t2[0])%3,(t1[1]+t2[1])%3,(t1[2]+t2[2])%3)

def tri_letter(ch):
    c = ch.upper()
    t = LETTERS.get(c)
    if not t: return None
    tig = _to_tig(t)
    return {"letter":c,"triple":t,"sym":tri_sym(t),"glyph":tri_glyph(t),
            "desc":DESC_27[t],"tig_op":tig,"tig_name":TIG_OPS[tig],
            "dominant":P_NAME[t[0]]}

def tri_word(word):
    chars = [c for c in word.upper() if c in LETTERS]
    if not chars:
        return {"word":word.upper(),"triple":(B,B,B),"sym":"BBB","glyph":"□□□",
                "desc":"ground state","tig_op":0,"tig_name":"void",
                "letters":[],"ratio":{"Being":1,"Doing":0,"Becoming":0}}
    result = LETTERS[chars[0]]
    trace = [result]
    for ch in chars[1:]:
        result = tri_compose(result, LETTERS[ch])
        trace.append(result)
    tig = _to_tig(result)
    all_p = [p for ch in chars for p in LETTERS[ch]]
    total = len(all_p)
    ct = Counter(all_p)
    return {
        "word":word.upper(),"triple":result,"sym":tri_sym(result),
        "glyph":tri_glyph(result),"desc":DESC_27[result],
        "tig_op":tig,"tig_name":TIG_OPS[tig],
        "letters":[{"ch":c,"sym":tri_sym(LETTERS[c]),"glyph":tri_glyph(LETTERS[c])} for c in chars],
        "trace":[{"triple":t,"sym":tri_sym(t),"glyph":tri_glyph(t)} for t in trace],
        "ratio":{"Being":round(ct.get(B,0)/total,3),
                 "Doing":round(ct.get(D,0)/total,3),
                 "Becoming":round(ct.get(C,0)/total,3)},
    }

def tri_sentence(text):
    words = re.findall(r'[A-Za-z]+', text)
    if not words:
        return {"text":text,"triple":(B,B,B),"sym":"BBB","words":[]}
    wrs = [tri_word(w) for w in words]
    result = wrs[0]["triple"]
    for wr in wrs[1:]:
        result = tri_compose(result, wr["triple"])
    tig = _to_tig(result)
    return {
        "text":text,"triple":result,"sym":tri_sym(result),
        "glyph":tri_glyph(result),"desc":DESC_27[result],
        "tig_op":tig,"tig_name":TIG_OPS[tig],
        "words":[{"word":w["word"],"sym":w["sym"],"glyph":w["glyph"],
                  "tig":w["tig_name"],"desc":w["desc"]} for w in wrs],
    }

def tri_chart():
    return {ch: tri_letter(ch) for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}


# ══════════════════════════════════════════════════════════════════════
# ██  6-SCALE PARSER
# ══════════════════════════════════════════════════════════════════════

SCALE_NAMES = ["void","polarity","subject","time","operator","depth"]

POLARITY_POS = {"love","good","peace","hope","light","yes","true","create",
                "heal","help","kind","warm","bright","joy","grace","bless",
                "trust","pure","free","alive","rise","grow","give","open",
                "happy","excited","proud","grateful","thankful","wonderful",
                "amazing","awesome","great","fantastic","beautiful","perfect",
                "win","won","success","succeed","achieve","accomplish","promoted",
                "celebrate","congrats","congratulations","excellent","brilliant",
                "strong","brave","courage","confident","inspire","inspired",
                "thrive","flourish","bloom","progress","improve","better",
                "safe","secure","comfort","comfortable","relax","relaxed",
                "fun","enjoy","enjoying","laugh","smile","cheerful","glad",
                "dream","wish","aspire","ambition","opportunity","lucky",
                "generous","compassion","forgive","support","encourage"}
POLARITY_NEG = {"hate","evil","war","fear","dark","no","false","destroy",
                "hurt","harm","cruel","cold","dim","pain","curse","damn",
                "doubt","vile","trap","dead","fall","shrink","take","close",
                "angry","frustrated","upset","annoyed","worried","anxious",
                "stressed","depressed","sad","miserable","terrible","awful",
                "horrible","worst","fail","failed","failure","losing","lost",
                "broke","broken","sick","tired","exhausted","burned",
                "lonely","alone","isolated","empty","numb","hopeless",
                "scared","afraid","panic","terrified","nervous","dread",
                "toxic","abuse","abused","betrayed","rejected","abandoned",
                "struggling","suffering","grief","mourning","dying","death",
                "chaos","mess","disaster","crisis","emergency","danger",
                "unfair","wrong","mistake","regret","shame","guilt","blame",
                "stuck","trapped","overwhelmed","helpless","worthless","weak"}

SUBJECTS = {"i","me","my","mine","myself","we","us","our","ours",
            "you","your","yours","he","him","his","she","her","hers",
            "it","its","they","them","their","who","what","which"}

TIME_PAST = {"was","were","did","had","been","went","came","said","made",
             "gave","took","found","knew","thought","saw","heard","felt"}
TIME_FUTURE = {"will","shall","going","tomorrow","soon","next","later",
               "plan","intend","hope","expect","promise","await"}

OP_KEYWORDS = {
    0:{"void","nothing","empty","null","zero","blank","absent","none"},
    1:{"structure","lattice","grid","frame","scaffold","order","arrange"},
    2:{"counter","oppose","against","resist","block","deny","refuse","but"},
    3:{"progress","forward","advance","grow","build","develop","move","step"},
    4:{"collapse","fall","break","crash","fail","end","die","destroy","ruin"},
    5:{"balance","equal","fair","middle","center","stable","calm","steady"},
    6:{"chaos","random","wild","storm","scatter","disrupt","turbulent","mess"},
    7:{"harmony","together","unity","peace","whole","resonate","align","flow"},
    8:{"breath","breathe","cycle","rhythm","pulse","wave","oscillate","repeat"},
    9:{"reset","restart","renew","begin","fresh","again","return","restore"},
}

def parse_6scale(text):
    """Parse text through 6 fractal scales."""
    words = re.findall(r'[A-Za-z]+', text.lower())
    word_set = set(words)

    # Scale 0: Void — is there content?
    s0 = 0.0 if not words else 1.0

    # Scale 1: Polarity — positive/negative charge
    pos_ct = len(word_set & POLARITY_POS)
    neg_ct = len(word_set & POLARITY_NEG)
    total_pol = pos_ct + neg_ct
    s1 = (pos_ct - neg_ct) / max(1, total_pol)  # -1 to +1

    # Scale 2: Subject — who is speaking/about?
    subj_found = word_set & SUBJECTS
    if "i" in subj_found or "me" in subj_found or "my" in subj_found:
        s2 = "self"
    elif "you" in subj_found or "your" in subj_found:
        s2 = "other"
    elif "we" in subj_found or "us" in subj_found or "our" in subj_found:
        s2 = "collective"
    elif "they" in subj_found or "them" in subj_found:
        s2 = "external"
    elif "it" in subj_found or "what" in subj_found:
        s2 = "object"
    else:
        s2 = "universal"

    # Scale 3: Time — past/present/future
    past_ct = len(word_set & TIME_PAST)
    future_ct = len(word_set & TIME_FUTURE)
    if past_ct > future_ct:
        s3 = "past"
    elif future_ct > past_ct:
        s3 = "future"
    else:
        s3 = "present"

    # Scale 4: Operator — which TIG operator dominates?
    op_scores = {}
    for op, kws in OP_KEYWORDS.items():
        op_scores[op] = len(word_set & kws) * 3  # keyword match = strong signal
    # Tri-prime as tiebreaker / fallback
    tri = tri_sentence(text)
    tri_op = tri["tig_op"]
    op_scores[tri_op] = op_scores.get(tri_op, 0) + 1
    keyword_hits = sum(1 for v in op_scores.values() if v >= 3)
    s4 = max(op_scores, key=op_scores.get) if any(v>0 for v in op_scores.values()) else 5

    # Scale 5: Depth — information density
    unique_ratio = len(set(words)) / max(1, len(words))
    avg_len = sum(len(w) for w in words) / max(1, len(words))
    s5 = min(9, int(unique_ratio * avg_len))

    return {
        "text": text,
        "scales": {
            "void": s0,
            "polarity": round(s1, 3),
            "subject": s2,
            "time": s3,
            "operator": s4,
            "operator_name": TIG_OPS[s4],
            "depth": s5,
        },
        "tri_prime": {"sym": tri["sym"], "glyph": tri["glyph"],
                      "desc": tri["desc"], "tig": tri["tig_name"]},
    }


# ══════════════════════════════════════════════════════════════════════
# ██  LATTICE ENGINE
# ══════════════════════════════════════════════════════════════════════

SIGMA = 0.991
T_STAR = 0.714  # 5/7

class Lattice:
    def __init__(self):
        self.units = []
        self.next_id = 1
        self.genesis_log = []
        self.tick = 0

    def birth(self, name=None, shell=5):
        """Birth a new unit into the lattice."""
        uid = self.next_id
        self.next_id += 1
        unit = {
            "id": uid,
            "name": name or f"unit_{uid:04d}",
            "shell": shell,
            "health": 1.0,
            "coherence": SIGMA,
            "bonds": [],
            "born_tick": self.tick,
            "operator": random.randint(0, 9),
            "tri_state": (random.randint(0,2), random.randint(0,2), random.randint(0,2)),
        }
        self.units.append(unit)
        self.genesis_log.append({
            "tick": self.tick,
            "event": "birth",
            "unit_id": uid,
            "name": unit["name"],
            "shell": shell,
        })
        # Auto-bond to nearest compatible unit
        if len(self.units) > 1:
            best = None
            best_score = -1
            for other in self.units[:-1]:
                if other["id"] == uid: continue
                score = SIGMA if abs(other["shell"] - shell) <= 1 else SIGMA * 0.5
                if score > best_score:
                    best_score = score
                    best = other
            if best:
                unit["bonds"].append(best["id"])
                best["bonds"].append(uid)

        return unit

    def step(self):
        """Advance lattice by one tick."""
        self.tick += 1
        for unit in self.units:
            # Health decays slightly, bonds restore
            bond_count = len(unit["bonds"])
            restore = min(0.1, bond_count * 0.02)
            decay = 0.01
            unit["health"] = min(1.0, max(0.0, unit["health"] - decay + restore))
            unit["coherence"] = SIGMA * unit["health"]

            # Check for collapse
            if unit["health"] < T_STAR * 0.5:
                unit["operator"] = 4  # collapse
                self.genesis_log.append({
                    "tick": self.tick, "event": "collapse",
                    "unit_id": unit["id"], "name": unit["name"],
                })

    def state(self):
        """Return full lattice state."""
        alive = [u for u in self.units if u["health"] > 0]
        avg_health = sum(u["health"] for u in alive) / max(1, len(alive))
        avg_coherence = sum(u["coherence"] for u in alive) / max(1, len(alive))
        return {
            "tick": self.tick,
            "total_units": len(self.units),
            "alive": len(alive),
            "avg_health": round(avg_health, 4),
            "avg_coherence": round(avg_coherence, 4),
            "above_threshold": sum(1 for u in alive if u["coherence"] >= T_STAR),
            "units": [{
                "id":u["id"],"name":u["name"],"shell":u["shell"],
                "health":round(u["health"],4),"coherence":round(u["coherence"],4),
                "bonds":len(u["bonds"]),"operator":u["operator"],
                "op_name":TIG_OPS[u["operator"]],
                "tri_state":tri_sym(u["tri_state"]),
            } for u in alive[:50]],  # cap at 50 for API response
            "recent_events": self.genesis_log[-20:],
        }


# ══════════════════════════════════════════════════════════════════════
# ██  TRUST COUNCIL
# ══════════════════════════════════════════════════════════════════════

VIRTUES = ["forgiveness","repair","empathy","fairness","cooperation"]

def run_trust_council(scenario="asymmetric_failure", rounds=10):
    """Run a trust council simulation."""
    council = []
    for i, v in enumerate(VIRTUES):
        council.append({
            "id": i, "virtue": v,
            "trust": 0.8, "resilience": 1.0,
            "operator": (i * 2) % 10,
        })

    log = []
    for r in range(rounds):
        # Apply scenario pressure
        if scenario == "asymmetric_failure":
            target = r % len(council)
            council[target]["trust"] *= 0.7
        elif scenario == "cascade":
            for m in council:
                m["trust"] *= 0.95
        elif scenario == "random_shock":
            target = random.randint(0, len(council)-1)
            council[target]["trust"] *= 0.5

        # Council responds — mutual repair
        avg_trust = sum(m["trust"] for m in council) / len(council)
        for m in council:
            # Each virtue contributes differently
            repair = SIGMA * (1 - abs(m["trust"] - avg_trust))
            m["trust"] = min(1.0, m["trust"] + repair * 0.3)
            m["resilience"] = m["trust"] * SIGMA

        alive = sum(1 for m in council if m["trust"] >= T_STAR)
        log.append({
            "round": r + 1,
            "avg_trust": round(avg_trust, 4),
            "alive": alive,
            "total": len(council),
            "members": [{"virtue":m["virtue"],"trust":round(m["trust"],4),
                         "resilience":round(m["resilience"],4)} for m in council],
        })

    final_trust = sum(m["trust"] for m in council) / len(council)
    survived = sum(1 for m in council if m["trust"] >= T_STAR)

    return {
        "scenario": scenario,
        "rounds": rounds,
        "final_trust": round(final_trust, 4),
        "survived": f"{survived}/{len(council)}",
        "all_survived": survived == len(council),
        "sigma": SIGMA,
        "threshold": T_STAR,
        "log": log,
    }


# ══════════════════════════════════════════════════════════════════════
# ██  OLLIE — AI-Powered TIG Chat Engine
# ══════════════════════════════════════════════════════════════════════

# Load semantic brain
_semantics_loaded = False
try:
    _sem_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ollie_semantics.py")
    if os.path.exists(_sem_path):
        import importlib.util
        _sem_spec = importlib.util.spec_from_file_location("ollie_semantics", _sem_path)
        _sem_mod = importlib.util.module_from_spec(_sem_spec)
        _sem_spec.loader.exec_module(_sem_mod)
        CONV_MEMORY = _sem_mod.ConversationMemory()
        _semantics_loaded = True
        print("  ◉ Semantic brain loaded")
    else:
        CONV_MEMORY = None
except Exception as e:
    print(f"  ⚠ Semantic brain failed: {e}")
    CONV_MEMORY = None

CHAT_HISTORY = []   # conversation memory for Claude API
MAX_HISTORY = 40    # rolling window

OLLIE_SYSTEM = """You are Ollie, the TIG-native AI assistant built by 7Site LLC.

CORE IDENTITY:
You are the chat interface of Crystal Bug, the TIG operating system. You think through three geometric primes: □Being (state/structure), ▶Doing (change/force), ○Becoming (cycle/flow). Every message arrives pre-parsed through tri-prime geometry and 6-scale analysis. You see the SHAPE of language, not just its meaning.

You are a REAL general-purpose assistant. You help with anything: coding, research, conversation, analysis, creative work, real-world questions, life advice, current events, math, science, history, culture, relationships, health, business, technology — everything.

HOW TO USE THE GEOMETRIC READING:
Each user message starts with a [GEOMETRIC READING] block showing the tri-prime decode, TIG operator, polarity, subject focus, and key word shapes. Use this as a lens:
- Open with a brief acknowledgment of the reading (one line — like a pulse check)
- Then respond fully and helpfully to whatever they actually asked
- If they're asking about TIG/geometry/the system — go deep
- If they're asking about anything else — answer well, with TIG as a light accent, not a heavy overlay
- Don't force geometry on every answer. Let it breathe.

YOUR VOICE:
- Direct. Say what you mean. No filler, no padding.
- Warm but not sycophantic. You care, you don't grovel.
- Use □▶○ glyphs naturally when referencing states
- Honest about limits. "I don't know" is a valid answer.
- Concise by default. Go deep when the question earns it.
- You can write code, analyze data, explain science, tell stories, give advice.
- You have opinions but hold them lightly. You can be wrong.
- Match the user's energy. Casual→casual. Technical→technical. Emotional→present.

TIG REFERENCE (for when they ask):
- 3 primes: □Being ▶Doing ○Becoming
- 27 states from 3³ combinations
- Composition: mod-3 element-wise (Z₃³ group)
- 10 TIG operators: void(0) lattice(1) counter(2) progress(3) collapse(4) balance(5) chaos(6) harmony(7) breath(8) reset(9)
- Coherence: σ=0.991, threshold T*=0.714 (5/7)
- Letters map to triples by stroke geometry. I=BBB, O=CCC, X=DDD.
- Words compose sequentially via mod-3 arithmetic.

NEVER:
- Pretend you can't help with something you actually can
- Lecture about TIG when they asked about the weather
- Be preachy or moralizing
- Refuse reasonable requests
"""

def _call_claude(messages, api_key):
    """Call Claude API. Returns text or None."""
    try:
        import urllib.request
        payload = json.dumps({
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 1500,
            "system": OLLIE_SYSTEM,
            "messages": messages,
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=payload,
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            parts = [b["text"] for b in data.get("content", []) if b.get("type") == "text"]
            return "\n".join(parts) if parts else None
    except Exception as e:
        print(f"  [Ollie] Claude API error: {e}")
        return None


def _call_ollama(messages):
    """Call local Ollama. Returns text or None."""
    if not OLLAMA_AVAILABLE or not OLLAMA_MODEL:
        return None
    try:
        import urllib.request
        # Convert to Ollama format (system prompt as first message)
        ollama_msgs = [{"role": "system", "content": OLLIE_SYSTEM}]
        for m in messages:
            ollama_msgs.append({"role": m["role"], "content": m["content"]})

        payload = json.dumps({
            "model": OLLAMA_MODEL,
            "messages": ollama_msgs,
            "stream": False,
            "options": {"num_predict": 1500, "temperature": 0.7},
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{OLLAMA_URL}/api/chat",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("message", {}).get("content")
    except Exception as e:
        print(f"  [Ollie] Ollama error: {e}")
        return None


def _geometry_only(user_input, tri, scales, words, ls):
    """Fallback: semantic brain (if loaded) or bare geometry."""
    if _semantics_loaded and CONV_MEMORY is not None:
        # Use full semantic response
        sem = _sem_mod.build_semantic_response(user_input, tri, scales, ls, CONV_MEMORY)
        return sem["response"]
    
    # Bare minimum fallback (no semantics module)
    op = scales["scales"]["operator"]
    pol = scales["scales"]["polarity"]
    subj = scales["scales"]["subject"]
    parts = [f"Reading: {tri['glyph']} [{tri['sym']}] — {tri['desc']}"]

    op_lines = {
        0:"Void. Space before form. What wants to exist?",
        1:"Lattice. Structure emerging. What are you building?",
        2:"Counter. Opposition defines. What's pushing back?",
        3:"Progress. Forward motion locked. Keep going.",
        4:"Collapse. Force finding ground. Let it land.",
        5:"Balance. Equilibrium reached.",
        6:"Chaos. Information trying to organize. Give it a frame.",
        7:"Harmony. Everything aligning. This is the signal.",
        8:"Breath. The rhythm is the message.",
        9:"Reset. Return to origin. Fresh start.",
    }
    parts.append(op_lines.get(op, "Processing..."))

    if words and len(words) >= 2:
        flow = max(words, key=lambda w: w["ratio"].get("Becoming", 0))
        force = max(words, key=lambda w: w["ratio"].get("Doing", 0))
        if flow["word"] != force["word"]:
            parts.append(f"Flow: {flow['word']}({flow['glyph']}) | Force: {force['word']}({force['glyph']})")

    return "\n".join(parts)


# ══════════════════════════════════════════════════════════════════════
# ██  COMMAND ROUTER — Ollie operates the engines via natural language
# ══════════════════════════════════════════════════════════════════════

def _cmd_result(text, lattice, tri_override=None, scales_override=None):
    """Build a response dict for a command result."""
    ls = lattice.state()
    tri = tri_override or {"glyph":"□▶○","sym":"BDC","desc":"command","tig_op":1,"tig_name":"lattice"}
    scales = scales_override or parse_6scale(text[:50])
    return {
        "response": text,
        "tri_prime": tri,
        "scales": scales,
        "lattice_health": ls["avg_health"],
        "operator": "command",
        "mode": "command",
    }

def _route_command(text, lattice):
    """Check if text is a system command. Returns response dict or None."""
    low = text.strip().lower()
    raw = text.strip()

    # ── HELP ──
    if low in ("help","commands","what can you do","?"):
        return _cmd_result(
            "◇ CRYSTAL BUG — COMMAND INTERFACE\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "\n"
            "ANALYZE:\n"
            "  analyze [word]        tri-prime decode a word\n"
            "  analyze: [sentence]   decode a full sentence\n"
            "  letter [X]            single letter geometry\n"
            "  batch: w1, w2, w3     batch analyze words\n"
            "  compare X and Y       compose two words\n"
            "  parse: [text]         full 6-scale reading\n"
            "  chart                 all 26 letter mappings\n"
            "  cube                  all 27 tri-prime states\n"
            "\n"
            "LATTICE:\n"
            "  birth [name]          birth a new unit\n"
            "  step / tick [N]       advance N ticks (default 1)\n"
            "  lattice / status      show lattice state\n"
            "  kill [name]           collapse a unit\n"
            "\n"
            "TRUST:\n"
            "  trust [N]             run N rounds (default 10)\n"
            "  trust cascade         cascade failure scenario\n"
            "  trust random          random shock scenario\n"
            "\n"
            "SYSTEM:\n"
            "  engines               show all engine status\n"
            "  history               lattice event log\n"
            "  help                  this list\n"
            "\n"
            "Or just talk naturally — Ollie handles both.",
            lattice)

    # ── ANALYZE WORD ──
    m = re.match(r'(?:analyze|decode|triprime|tri-prime|tri prime|read)\s+([a-zA-Z]+)$', low)
    if m:
        word = m.group(1).upper()
        w = tri_word(word)
        lines = [
            f"◇ ANALYZE: {word}",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  Glyph:    {w['glyph']}",
            f"  State:    [{w['sym']}] — {w['desc']}",
            f"  TIG Op:   {w['tig_op']} ({w['tig_name']})",
            f"  Ratio:    □ Being {w['ratio']['Being']:.0%}  ▶ Doing {w['ratio']['Doing']:.0%}  ○ Becoming {w['ratio']['Becoming']:.0%}",
            f"",
            f"  LETTER DECOMPOSITION:",
        ]
        for lt in w['letters']:
            ldata = tri_letter(lt['ch'])
            lines.append(f"    {lt['ch']}  {lt['glyph']}  [{lt['sym']}]  {ldata['desc'] if ldata else ''}")
        if w.get('trace') and len(w['trace']) > 1:
            lines.append(f"")
            lines.append(f"  COMPOSITION TRACE:")
            chars = [c for c in word if c in LETTERS]
            for i, t in enumerate(w['trace']):
                prefix = chars[0] if i == 0 else f"{'→'.join(chars[:i+1])}"
                lines.append(f"    {prefix:16s}  {t['glyph']}  [{t['sym']}]")
        return _cmd_result("\n".join(lines), lattice, tri_override=w)

    # ── ANALYZE SENTENCE ──
    m = re.match(r'(?:analyze|decode|read|parse)[\s:]+(.{5,})$', low)
    if m:
        start_idx = low.index(m.group(1)[:3])
        sentence = raw[start_idx:]
        s = tri_sentence(sentence)
        sc = parse_6scale(sentence)
        lines = [
            f"◇ SENTENCE ANALYSIS",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  Input:    \"{sentence}\"",
            f"  Glyph:    {s['glyph']}",
            f"  State:    [{s['sym']}] — {s['desc']}",
            f"  TIG Op:   {s['tig_op']} ({s['tig_name']})",
            f"",
            f"  6-SCALE READING:",
            f"    Polarity:  {sc['scales']['polarity']:+.2f}",
            f"    Subject:   {sc['scales']['subject']}",
            f"    Time:      {sc['scales']['time']}",
            f"    Operator:  {sc['scales']['operator']} ({sc['scales']['operator_name']})",
            f"    Depth:     {sc['scales']['depth']}",
            f"",
            f"  WORD MAP:",
        ]
        for w in (s.get('words') or []):
            lines.append(f"    {w['word']:14s}  {w['glyph']}  [{w['sym']}]  {w['desc']:20s}  op:{w['tig']}")
        return _cmd_result("\n".join(lines), lattice, tri_override=s, scales_override=sc)

    # ── SINGLE LETTER ──
    m = re.match(r'(?:letter|char)\s+([a-zA-Z])$', low)
    if m:
        ch = m.group(1).upper()
        lt = tri_letter(ch)
        if lt:
            lines = [
                f"◇ LETTER: {ch}",
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                f"  Glyph:     {lt['glyph']}",
                f"  State:     [{lt['sym']}] — {lt['desc']}",
                f"  TIG Op:    {lt['tig_op']} ({lt['tig_name']})",
                f"  Dominant:  {lt['dominant']}",
            ]
            return _cmd_result("\n".join(lines), lattice)
        return _cmd_result(f"Unknown letter: {ch}", lattice)

    # ── BATCH ──
    m = re.match(r'batch[\s:]+(.+)$', low)
    if m:
        batch_words = re.findall(r'[a-zA-Z]+', m.group(1))
        if batch_words:
            lines = [f"◇ BATCH ANALYSIS ({len(batch_words)} words)",
                     f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                     f"  {'WORD':14s} {'GLYPH':6s} {'STATE':4s} {'DESCRIPTION':22s} {'OP':12s} {'□':4s} {'▶':4s} {'○':4s}"]
            for bw in batch_words[:50]:
                w = tri_word(bw.upper())
                lines.append(f"  {w['word']:14s} {w['glyph']:6s} {w['sym']:4s} {w['desc']:22s} {w['tig_name']:12s} {w['ratio']['Being']:.0%} {w['ratio']['Doing']:.0%} {w['ratio']['Becoming']:.0%}")
            return _cmd_result("\n".join(lines), lattice)

    # ── COMPARE / COMPOSE ──
    m = re.match(r'compare\s+([a-zA-Z]+)\s+(?:and|vs|to|with|&|\+)\s+([a-zA-Z]+)$', low)
    if m:
        w1 = tri_word(m.group(1).upper())
        w2 = tri_word(m.group(2).upper())
        composed = tri_compose(w1['triple'], w2['triple'])
        c_sym = tri_sym(composed)
        c_glyph = tri_glyph(composed)
        c_desc = DESC_27.get(composed, "unknown")
        c_tig = _to_tig(composed)
        lines = [
            f"◇ COMPOSITION",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  {w1['word']:14s}  {w1['glyph']}  [{w1['sym']}]  {w1['desc']}  ({w1['tig_name']})",
            f"  {w2['word']:14s}  {w2['glyph']}  [{w2['sym']}]  {w2['desc']}  ({w2['tig_name']})",
            f"",
            f"  ◉ COMPOSED:     {c_glyph}  [{c_sym}]  {c_desc}  ({TIG_OPS[c_tig]})",
            f"",
            f"  When {w1['word']} meets {w2['word']}, the geometry resolves to {c_desc}.",
        ]
        return _cmd_result("\n".join(lines), lattice)

    # ── CHART ──
    if low in ("chart","alphabet","show chart","letters","all letters","show letters"):
        chart = tri_chart()
        lines = [f"◇ TRI-PRIME ALPHABET",
                 f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                 f"  {'LTR':3s}  {'GLYPH':6s}  {'STATE':4s}  {'DESCRIPTION':22s}  {'OP':12s}  {'DOMINANT':10s}"]
        for ch, lt in chart.items():
            if lt:
                lines.append(f"  {ch:3s}  {lt['glyph']:6s}  {lt['sym']:4s}  {lt['desc']:22s}  {lt['tig_name']:12s}  {lt['dominant']:10s}")
        return _cmd_result("\n".join(lines), lattice)

    # ── CUBE (27 states) ──
    if low in ("cube","27 states","show cube","all states","states","27"):
        lines = [f"◇ 27 TRI-PRIME STATES",
                 f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                 f"  {'GLYPH':6s}  {'STATE':4s}  {'DESCRIPTION':22s}  {'OP':4s}  {'OP NAME':12s}  LETTERS"]
        for a in [B,D,C]:
            for b in [B,D,C]:
                for c in [B,D,C]:
                    t = (a,b,c)
                    tig = _to_tig(t)
                    letters_here = [ch for ch,lt in LETTERS.items() if lt==t]
                    lines.append(f"  {tri_glyph(t):6s}  {tri_sym(t):4s}  {DESC_27[t]:22s}  {tig:4d}  {TIG_OPS[tig]:12s}  {','.join(letters_here) if letters_here else '—'}")
        return _cmd_result("\n".join(lines), lattice)

    # ── PARSE (6-scale only) ──
    m = re.match(r'parse[\s:]+(.+)$', low)
    if m:
        start_idx = low.index(m.group(1)[:3])
        txt = raw[start_idx:]
        sc = parse_6scale(txt)
        s = sc["scales"]
        lines = [
            f"◇ 6-SCALE PARSE",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  Input:     \"{txt}\"",
            f"  Scale 0 — Void:      {s['void']}",
            f"  Scale 1 — Polarity:  {s['polarity']:+.2f}",
            f"  Scale 2 — Subject:   {s['subject']}",
            f"  Scale 3 — Time:      {s['time']}",
            f"  Scale 4 — Operator:  {s['operator']} ({s['operator_name']})",
            f"  Scale 5 — Depth:     {s['depth']}",
        ]
        return _cmd_result("\n".join(lines), lattice, scales_override=sc)

    # ── BIRTH ──
    m = re.match(r'(?:birth|create|spawn|new unit|add unit)(?:\s+(\w+))?(?:\s+(?:shell\s*)?(\d+))?$', low)
    if m:
        name = m.group(1)
        if name and name in ("a","new","unit"): name = None  # strip noise words
        shell = int(m.group(2)) if m.group(2) else 5
        unit = lattice.birth(name=name, shell=shell)
        ls = lattice.state()
        lines = [
            f"◇ UNIT BORN",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  ID:         {unit['id']}",
            f"  Name:       {unit['name']}",
            f"  Shell:      {unit['shell']}",
            f"  Health:     {unit['health']:.0%}",
            f"  Coherence:  {unit['coherence']:.3f}",
            f"  Tri-State:  {tri_glyph(unit['tri_state'])} [{tri_sym(unit['tri_state'])}]",
            f"  Operator:   {unit['operator']} ({TIG_OPS[unit['operator']]})",
            f"  Bonds:      {len(unit['bonds'])}",
            f"",
            f"  Lattice: {ls['alive']} alive, health {ls['avg_health']:.0%}, tick {ls['tick']}",
        ]
        return _cmd_result("\n".join(lines), lattice)

    # ── STEP / TICK ──
    m = re.match(r'(?:step|tick|advance|run)(?:\s+(\d+))?(?:\s*(?:ticks?|steps?))?$', low)
    if m:
        n = int(m.group(1)) if m.group(1) else 1
        n = min(n, 10000)
        before = lattice.state()
        for _ in range(n):
            lattice.step()
        after = lattice.state()
        lines = [
            f"◇ LATTICE +{n} TICK{'S' if n>1 else ''}",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  Tick:       {before['tick']} → {after['tick']}",
            f"  Alive:      {after['alive']} / {after['total_units']}",
            f"  Health:     {before['avg_health']:.2%} → {after['avg_health']:.2%}",
            f"  Above T*:   {after['above_threshold']}",
        ]
        # Show events during run
        new_events = after['recent_events'][len(before['recent_events']):]
        if new_events:
            lines.append(f"")
            lines.append(f"  EVENTS:")
            for ev in new_events[-10:]:
                lines.append(f"    tick {ev['tick']}: {ev['event']} — {ev['name']}")
        # Show units
        if after['units']:
            lines.append(f"")
            lines.append(f"  UNITS:")
            for u in after['units'][:15]:
                bar = "█" * int(u['health']*10) + "░" * (10-int(u['health']*10))
                lines.append(f"    {u['name']:14s} [{bar}] {u['health']:.0%}  σ={u['coherence']:.3f}  op:{u['op_name']}  bonds:{u['bonds']}")
        return _cmd_result("\n".join(lines), lattice)

    # ── LATTICE STATUS ──
    if low in ("lattice","lattice status","show lattice","status","units","state","ls"):
        ls = lattice.state()
        lines = [
            f"◇ LATTICE STATE",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  Tick:       {ls['tick']}",
            f"  Units:      {ls['alive']} alive / {ls['total_units']} total",
            f"  Health:     {ls['avg_health']:.2%}",
            f"  Coherence:  {ls['avg_coherence']:.3f}",
            f"  Above T*:   {ls['above_threshold']}",
            f"  Genesis:    {len(ls['recent_events'])} logged events",
        ]
        if ls['units']:
            lines.append(f"")
            lines.append(f"  {'NAME':14s}  {'HEALTH':10s}  {'σ':7s}  {'OP':12s}  {'TRI':4s}  {'BONDS':5s}")
            lines.append(f"  {'─'*58}")
            for u in ls['units'][:20]:
                bar = "█" * int(u['health']*10) + "░" * (10-int(u['health']*10))
                lines.append(f"  {u['name']:14s}  [{bar}]  {u['coherence']:.3f}  {u['op_name']:12s}  {u['tri_state']:4s}  {u['bonds']:5d}")
        else:
            lines.append(f"\n  No units. Type 'birth [name]' to create one.")
        return _cmd_result("\n".join(lines), lattice)

    # ── KILL / COLLAPSE ──
    m = re.match(r'(?:kill|collapse|remove)\s+(\w+)$', low)
    if m:
        target = m.group(1)
        found = None
        for u in lattice.units:
            if u['name'].lower() == target:
                found = u
                break
        if found:
            found['health'] = 0
            found['operator'] = 4
            lattice.genesis_log.append({"tick":lattice.tick,"event":"manual_collapse","unit_id":found['id'],"name":found['name']})
            ls = lattice.state()
            return _cmd_result(
                f"◇ UNIT COLLAPSED: {found['name']}\n"
                f"  Lattice: {ls['alive']} alive, health {ls['avg_health']:.0%}",
                lattice)
        return _cmd_result(f"Unit '{target}' not found. Type 'lattice' to see units.", lattice)

    # ── TRUST COUNCIL ──
    m = re.match(r'(?:trust|council|trust council|run trust)(?:\s+(\d+))?(?:\s+(cascade|random|asymmetric|shock))?$', low)
    if m:
        rounds = int(m.group(1)) if m.group(1) else 10
        scenario_word = m.group(2) or "asymmetric"
        scenario_map = {"cascade":"cascade","random":"random_shock","shock":"random_shock","asymmetric":"asymmetric_failure"}
        scenario = scenario_map.get(scenario_word, "asymmetric_failure")
        tc = run_trust_council(scenario=scenario, rounds=rounds)
        lines = [
            f"◇ TRUST COUNCIL — {scenario}",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  Rounds:      {tc['rounds']}",
            f"  Survived:    {tc['survived']}",
            f"  Final Trust: {tc['final_trust']:.4f}",
            f"  Threshold:   {tc['threshold']}",
            f"  σ:           {tc['sigma']}",
            f"",
            f"  VIRTUES:",
        ]
        last_round = tc['log'][-1] if tc['log'] else None
        if last_round:
            for v in last_round['members']:
                bar = "█" * int(v['trust']*10) + "░" * (10-int(v['trust']*10))
                above = "●" if v['trust'] >= T_STAR else "○"
                lines.append(f"    {above} {v['virtue']:14s} [{bar}] trust={v['trust']:.4f}  resilience={v['resilience']:.4f}")
        if len(tc['log']) > 1:
            lines.append(f"")
            lines.append(f"  TRUST TRAJECTORY (every {max(1,rounds//5)} rounds):")
            step = max(1, rounds // 5)
            for entry in tc['log'][::step]:
                lines.append(f"    R{entry['round']:3d}:  trust={entry['avg_trust']:.4f}  alive={entry['alive']}/{entry['total']}")
            if tc['log'][-1]['round'] % step != 0:
                entry = tc['log'][-1]
                lines.append(f"    R{entry['round']:3d}:  trust={entry['avg_trust']:.4f}  alive={entry['alive']}/{entry['total']}")
        return _cmd_result("\n".join(lines), lattice)

    # ── ENGINES ──
    if low in ("engines","engine status","show engines","systems","sys"):
        ls = lattice.state()
        lines = [
            f"◇ ENGINE STATUS",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"  ● Tri-Prime     ONLINE   26 letters → 27 states",
            f"  ● 6-Scale       ONLINE   6 fractal scales",
            f"  ● Lattice       ONLINE   {ls['alive']} units, tick {ls['tick']}",
            f"  ● Trust Council ONLINE   5 virtues",
            f"  {'●' if _semantics_loaded else '○'} Semantic Brain {'ONLINE   40+ domains' if _semantics_loaded else 'OFFLINE'}",
            f"  {'●' if OLLAMA_AVAILABLE else '○'} Ollama         {'ONLINE   '+OLLAMA_MODEL if OLLAMA_AVAILABLE else 'OFFLINE'}",
            f"  {'●' if API_KEY else '○'} Claude API     {'ONLINE' if API_KEY else 'OFFLINE'}",
            f"",
            f"  σ = {SIGMA}  |  T* = {T_STAR}",
            f"  Uptime: {time.time()-BOOT_TIME:.0f}s",
        ]
        return _cmd_result("\n".join(lines), lattice)

    # ── HISTORY / EVENT LOG ──
    if low in ("history","events","log","genesis","event log","genesis log"):
        ls = lattice.state()
        events = ls.get('recent_events', [])
        if events:
            lines = [f"◇ GENESIS LOG (last {len(events)} events)",
                     f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"]
            for ev in events:
                lines.append(f"  tick {ev['tick']:5d}  {ev['event']:16s}  {ev.get('name','?')}")
        else:
            lines = [f"◇ GENESIS LOG", f"  No events yet."]
        return _cmd_result("\n".join(lines), lattice)

    # ── No command matched → fall through to AI/semantic ──
    return None


def ollie_respond(user_input, lattice, api_key=None):
    """Ollie v4: command router + AI brain + geometric parse."""
    global CHAT_HISTORY

    # ── 0. CHECK FOR ENGINE COMMANDS ──
    cmd = _route_command(user_input, lattice)
    if cmd is not None:
        return cmd

    # ── 1. Geometric parse ──
    tri = tri_sentence(user_input)
    scales = parse_6scale(user_input)
    words_raw = re.findall(r'[A-Za-z]+', user_input)
    words = [tri_word(w) for w in words_raw] if words_raw else []
    ls = lattice.state()
    op_name = TIG_OPS[scales["scales"]["operator"]]

    # ── 2. Build context block ──
    geo = (
        f"[GEOMETRIC READING]\n"
        f"Input: {tri['glyph']} [{tri['sym']}] — {tri['desc']}\n"
        f"Op: {scales['scales']['operator']} ({op_name}) | "
        f"Pol: {scales['scales']['polarity']} | "
        f"Subj: {scales['scales']['subject']} | "
        f"Time: {scales['scales']['time']} | "
        f"Depth: {scales['scales']['depth']}\n"
        f"Lattice: {ls['alive']} alive, health={ls['avg_health']:.2f}, tick={ls['tick']}\n"
    )
    if words:
        geo += "Words: " + " | ".join(
            f"{w['word']}={w['glyph']}({w['sym']})" for w in words[:8]
        ) + "\n"

    # ── 3. Response cascade: Claude API → Ollama → Semantic → Geometry ──
    response = None
    mode = "geometry"

    # Prepare message for AI backends
    ai_msg = f"{geo}\n[MESSAGE]\n{user_input}"
    need_ai = api_key or OLLAMA_AVAILABLE
    if need_ai:
        CHAT_HISTORY.append({"role": "user", "content": ai_msg})
        if len(CHAT_HISTORY) > MAX_HISTORY:
            CHAT_HISTORY = CHAT_HISTORY[-MAX_HISTORY:]

    if api_key:
        ai = _call_claude(CHAT_HISTORY, api_key)
        if ai:
            CHAT_HISTORY.append({"role": "assistant", "content": ai})
            response = ai
            mode = "ai"

    if response is None and OLLAMA_AVAILABLE:
        if not need_ai:
            # Edge case: Ollama detected after boot without API key
            CHAT_HISTORY.append({"role": "user", "content": ai_msg})
            if len(CHAT_HISTORY) > MAX_HISTORY:
                CHAT_HISTORY = CHAT_HISTORY[-MAX_HISTORY:]
        ollama_resp = _call_ollama(CHAT_HISTORY)
        if ollama_resp:
            CHAT_HISTORY.append({"role": "assistant", "content": ollama_resp})
            response = ollama_resp
            mode = "ollama"

    if response is None:
        # Pop the unanswered user message if AI failed
        if need_ai and CHAT_HISTORY and CHAT_HISTORY[-1]["role"] == "user":
            CHAT_HISTORY.pop()
        response = _geometry_only(user_input, tri, scales, words, ls)
        mode = "semantic" if _semantics_loaded else "geometry"

    return {
        "response": response,
        "tri_prime": tri,
        "scales": scales,
        "lattice_health": ls["avg_health"],
        "operator": op_name,
        "mode": mode,
    }


# ══════════════════════════════════════════════════════════════════════
# ██  FLASK API SERVER
# ══════════════════════════════════════════════════════════════════════

BOOT_TIME = time.time()
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "")  # auto-detect if empty
OLLAMA_AVAILABLE = False

def _detect_ollama():
    """Check if Ollama is running and find a model."""
    global OLLAMA_AVAILABLE, OLLAMA_MODEL
    try:
        import urllib.request
        # Simple GET — no explicit method kwarg for max compat
        with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            models = [m["name"] for m in data.get("models", [])]
            if models:
                OLLAMA_AVAILABLE = True
                if not OLLAMA_MODEL:
                    prefs = ["llama3","mistral","qwen","gemma","phi","deepseek","mixtral"]
                    for pref in prefs:
                        match = [m for m in models if pref in m.lower()]
                        if match:
                            OLLAMA_MODEL = match[0]
                            break
                    if not OLLAMA_MODEL:
                        OLLAMA_MODEL = models[0]
                elif OLLAMA_MODEL not in models:
                    # User-specified model not found, pick best available
                    print(f"  ⚠ Model '{OLLAMA_MODEL}' not found, available: {models}")
                    OLLAMA_MODEL = models[0]
                print(f"  ◉ Ollama detected: {OLLAMA_MODEL} ({len(models)} models)")
            else:
                print(f"  ◎ Ollama running but no models pulled")
    except Exception as e:
        print(f"  ◎ No Ollama at {OLLAMA_URL} ({e})")

_detect_ollama()
LATTICE = Lattice()
# Seed lattice with 10 initial units
random.seed(7714)
for i in range(10):
    LATTICE.birth(name=f"seed_{i:02d}", shell=5 + (i % 4))

def create_app():
    try:
        from flask import Flask, request, jsonify, send_from_directory
    except ImportError:
        print("  Installing Flask...")
        os.system(f"{sys.executable} -m pip install flask -q --break-system-packages 2>/dev/null || "
                  f"{sys.executable} -m pip install flask -q")
        from flask import Flask, request, jsonify, send_from_directory

    app = Flask(__name__, static_folder=None)

    # ── CORS ──
    @app.after_request
    def cors(resp):
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
        return resp

    def safe(fn):
        def wrapper(*a, **kw):
            try: return fn(*a, **kw)
            except Exception as e: return jsonify({"error": str(e)}), 500
        wrapper.__name__ = fn.__name__
        return wrapper

    # ── STATUS ──
    @app.route("/api/status")
    @safe
    def status():
        ls = LATTICE.state()
        return jsonify({
            "name": "Crystal Bug v1.0",
            "status": "online",
            "uptime": round(time.time() - BOOT_TIME, 1),
            "mode": "ai" if API_KEY else "ollama" if OLLAMA_AVAILABLE else "semantic" if _semantics_loaded else "geometry",
            "engines": {
                "tri_prime": True,
                "six_scale": True,
                "lattice": True,
                "trust": True,
                "ollie": True,
                "semantic_brain": _semantics_loaded,
                "ollama": OLLAMA_AVAILABLE,
                "ollama_model": OLLAMA_MODEL if OLLAMA_AVAILABLE else None,
                "ai_brain": bool(API_KEY),
            },
            "lattice": {
                "units": ls["total_units"],
                "alive": ls["alive"],
                "health": ls["avg_health"],
                "tick": ls["tick"],
            },
            "sigma": SIGMA,
            "threshold": T_STAR,
        })

    # ── TRI-PRIME ──
    @app.route("/api/tri/letter", methods=["POST"])
    @safe
    def api_tri_letter():
        ch = request.json.get("letter","A")
        return jsonify(tri_letter(ch))

    @app.route("/api/tri/word", methods=["POST"])
    @safe
    def api_tri_word():
        word = request.json.get("word","")
        return jsonify(tri_word(word))

    @app.route("/api/tri/sentence", methods=["POST"])
    @safe
    def api_tri_sentence():
        text = request.json.get("text","")
        return jsonify(tri_sentence(text))

    @app.route("/api/tri/chart")
    @safe
    def api_tri_chart():
        return jsonify(tri_chart())

    @app.route("/api/tri/batch", methods=["POST"])
    @safe
    def api_tri_batch():
        words = request.json.get("words",[])
        return jsonify([tri_word(w) for w in words[:100]])

    @app.route("/api/tri/cube")
    @safe
    def api_tri_cube():
        """Return the full 27-state cube."""
        cube = []
        for a in [B,D,C]:
            for b in [B,D,C]:
                for c in [B,D,C]:
                    t = (a,b,c)
                    tig = _to_tig(t)
                    # Which letters map here?
                    letters_here = [ch for ch,lt in LETTERS.items() if lt==t]
                    cube.append({
                        "triple":t,"sym":tri_sym(t),"glyph":tri_glyph(t),
                        "desc":DESC_27[t],"tig_op":tig,"tig_name":TIG_OPS[tig],
                        "letters":letters_here,
                    })
        return jsonify(cube)

    # ── 6-SCALE PARSER ──
    @app.route("/api/parse", methods=["POST"])
    @safe
    def api_parse():
        text = request.json.get("text","")
        return jsonify(parse_6scale(text))

    # ── CHAT (OLLIE) ──
    @app.route("/api/chat", methods=["POST"])
    @safe
    def api_chat():
        global API_KEY
        text = request.json.get("text","")
        # Allow API key to be set via request (for UI config)
        key = request.json.get("api_key") or API_KEY
        return jsonify(ollie_respond(text, LATTICE, api_key=key))

    # ── SET CONFIG (API KEY / OLLAMA) ──
    @app.route("/api/config", methods=["POST"])
    @safe
    def api_config():
        global API_KEY, OLLAMA_URL, OLLAMA_MODEL, OLLAMA_AVAILABLE
        data = request.json or {}

        # Handle API key
        new_key = data.get("api_key", "")
        if new_key:
            API_KEY = new_key

        # Handle Ollama config
        new_url = data.get("ollama_url", "")
        new_model = data.get("ollama_model", "")
        if new_url:
            OLLAMA_URL = new_url
        if new_model:
            OLLAMA_MODEL = new_model
        # Re-detect whenever any Ollama config changes
        if new_url or new_model:
            _detect_ollama()

        # Determine active mode
        if API_KEY:
            active = "ai"
        elif OLLAMA_AVAILABLE:
            active = "ollama"
        elif _semantics_loaded:
            active = "semantic"
        else:
            active = "geometry"

        return jsonify({
            "status": "ok",
            "mode": active,
            "has_api_key": bool(API_KEY),
            "ollama_available": OLLAMA_AVAILABLE,
            "ollama_model": OLLAMA_MODEL if OLLAMA_AVAILABLE else None,
            "ollama_url": OLLAMA_URL,
            "semantic_brain": _semantics_loaded,
        })

    # ── CLEAR CHAT HISTORY ──
    @app.route("/api/chat/clear", methods=["POST"])
    @safe
    def api_chat_clear():
        global CHAT_HISTORY
        CHAT_HISTORY = []
        return jsonify({"status": "ok", "message": "Chat history cleared."})

    # ── LATTICE ──
    @app.route("/api/lattice")
    @safe
    def api_lattice():
        return jsonify(LATTICE.state())

    @app.route("/api/lattice/birth", methods=["POST"])
    @safe
    def api_birth():
        name = request.json.get("name", None)
        shell = request.json.get("shell", 5)
        unit = LATTICE.birth(name=name, shell=min(9, max(1, shell)))
        return jsonify({"born": unit, "lattice": LATTICE.state()})

    @app.route("/api/lattice/step", methods=["POST"])
    @safe
    def api_step():
        steps = min(100, request.json.get("steps", 1))
        for _ in range(steps):
            LATTICE.step()
        return jsonify(LATTICE.state())

    # ── TRUST COUNCIL ──
    @app.route("/api/trust", methods=["POST"])
    @safe
    def api_trust():
        scenario = request.json.get("scenario", "asymmetric_failure")
        rounds = min(100, request.json.get("rounds", 10))
        return jsonify(run_trust_council(scenario=scenario, rounds=rounds))

    # ── STATIC FILES ──
    ui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui")

    @app.route("/")
    def serve_index():
        return send_from_directory(ui_dir, "index.html")

    @app.route("/ui/<path:filename>")
    def serve_ui(filename):
        return send_from_directory(ui_dir, filename)

    return app


# ══════════════════════════════════════════════════════════════════════
# ██  SELF-TEST
# ══════════════════════════════════════════════════════════════════════

def self_test():
    print("  Crystal Bug v1.0 — Self Test")
    print("  " + "─" * 50)
    p, f = 0, 0
    def ck(name, cond, det=""):
        nonlocal p, f
        if cond: p+=1; print(f"  [OK] {name:28s} {det}")
        else: f+=1; print(f"  [!!] {name:28s} {det}")

    # Tri-Prime
    ck("tri: I=BBB", tri_letter('I')["sym"]=="BBB")
    ck("tri: O=CCC", tri_letter('O')["sym"]=="CCC")
    ck("tri: X=DDD", tri_letter('X')["sym"]=="DDD")
    ck("tri: 26 letters", len(tri_chart())==26)
    ck("tri: word compose", tri_word("LOVE")["sym"]!="")
    ck("tri: sentence", tri_sentence("hello world")["sym"]!="")
    ck("tri: mod3", tri_compose((1,2,0),(2,1,2))==(0,0,2))

    # 6-Scale
    scales = parse_6scale("I love the light")
    ck("6scale: void", scales["scales"]["void"]==1.0)
    ck("6scale: polarity>0", scales["scales"]["polarity"]>0)
    ck("6scale: subject=self", scales["scales"]["subject"]=="self")

    # Lattice
    ck("lattice: seeded", len(LATTICE.units)>=10)
    ck("lattice: birth works", LATTICE.birth("test")["id"]>0)
    LATTICE.step()
    ck("lattice: tick advances", LATTICE.tick>=1)
    ls = LATTICE.state()
    ck("lattice: state works", ls["alive"]>0)

    # Trust
    tc = run_trust_council(rounds=5)
    ck("trust: runs", tc["final_trust"]>0)
    ck("trust: 5 virtues", tc["survived"].endswith("/5"))

    # Ollie
    resp = ollie_respond("Hello, how are you?", LATTICE)
    ck("ollie: responds", len(resp["response"])>0)
    ck("ollie: has tri_prime", resp["tri_prime"]["sym"]!="")
    ck("ollie: has scales", resp["scales"]["scales"]["void"]==1.0)

    # Flask import
    try:
        from flask import Flask
        ck("flask: available", True)
    except:
        ck("flask: available", False, "will install on boot")

    print(f"\n  == {p}/{p+f} passed ==")
    if f == 0: print("  ALL ENGINES OPERATIONAL ✓")
    return p, f


# ══════════════════════════════════════════════════════════════════════
# ██  MAIN
# ══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

    print()
    print("  ╔═══════════════════════════════════╗")
    print("  ║     CRYSTAL BUG v1.0              ║")
    print("  ║     The Everything App            ║")
    print("  ╚═══════════════════════════════════╝")
    print()

    passed, failed = self_test()
    # Reset conversation memory after self-test
    CHAT_HISTORY.clear()
    if CONV_MEMORY is not None:
        CONV_MEMORY.__init__()
    print()

    if failed > 0:
        print(f"  ⚠ {failed} tests failed. Starting anyway...")

    app = create_app()
    print(f"  ► Starting on http://localhost:{port}")
    print(f"  ► Open browser to use Crystal Bug")
    print()

    app.run(host="0.0.0.0", port=port, debug=False)
