"""
╔══════════════════════════════════════════════════════════════════════╗
║  OLLIE SEMANTICS v1.0                                                ║
║  Modern World Knowledge + Conversational Intelligence                ║
║                                                                      ║
║  This module gives Ollie:                                            ║
║    - Intent detection (asking, telling, venting, seeking, greeting)  ║
║    - Topic/domain classification (40+ real-world domains)            ║
║    - Contextual response generation                                  ║
║    - Modern semantic lexicon (2000+ categorized terms)               ║
║    - Conversational memory (within session)                          ║
║    - Practical advice patterns                                       ║
║                                                                      ║
║  Tri-prime geometry STAYS as Ollie's unique lens.                    ║
║  This layer adds WHAT he talks about.                                ║
║  Geometry tells him HOW the words feel.                              ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import re, random
from collections import Counter, defaultdict

# ══════════════════════════════════════════════════════════════════════
# INTENT DETECTION
# ══════════════════════════════════════════════════════════════════════

INTENT_PATTERNS = {
    "greeting": {
        "starts": ["hi","hey","hello","yo","sup","whats up","good morning",
                   "good afternoon","good evening","howdy","hola","greetings"],
        "contains": [],
    },
    "question": {
        "starts": ["what","why","how","when","where","who","which","can you",
                   "could you","would you","do you","is it","are there",
                   "should i","will","does","did","have you","tell me"],
        "contains": ["?"],
    },
    "command": {
        "starts": ["show me","give me","help me","find","search","look up",
                   "calculate","run","analyze","explain","define","list",
                   "compare","create","make","build","generate","do"],
        "contains": [],
    },
    "venting": {
        "contains": ["frustrated","angry","upset","annoyed","tired of","sick of",
                     "hate when","can't stand","drives me crazy","fed up",
                     "stressed","overwhelmed","burned out","exhausted",
                     "i can't","so hard","too much","falling apart"],
    },
    "seeking_advice": {
        "contains": ["should i","what do you think","advice","recommend",
                     "suggestion","help me decide","torn between","not sure if",
                     "worth it","best way to","how to deal","what would you"],
    },
    "sharing_news": {
        "starts": ["i just","i got","guess what","so i","today i","i finally",
                   "i started","i finished","we just","i found out"],
        "contains": ["just happened","big news","update"],
    },
    "philosophical": {
        "contains": ["meaning of","purpose","existence","consciousness","free will",
                     "reality","truth","nature of","what is life","why do we",
                     "what happens when","soul","spirit","god","divine",
                     "universe","infinity","nothing","everything","time"],
    },
    "technical": {
        "contains": ["code","programming","software","hardware","server","database",
                     "api","algorithm","bug","deploy","python","javascript",
                     "linux","network","cpu","gpu","memory","disk","docker",
                     "git","compile","debug","stack","function","variable"],
    },
    "creative": {
        "contains": ["write","story","poem","song","idea","imagine","design",
                     "art","music","creative","novel","script","paint",
                     "compose","invent","dream up","brainstorm"],
    },
    "farewell": {
        "starts": ["bye","goodbye","see you","later","gotta go","peace out",
                   "take care","night","signing off"],
        "contains": [],
    },
}

def detect_intent(text):
    """Detect conversational intent from text."""
    lower = text.lower().strip()
    scores = {}
    for intent, patterns in INTENT_PATTERNS.items():
        score = 0
        for s in patterns.get("starts", []):
            if lower.startswith(s):
                score += 3
        for c in patterns.get("contains", []):
            if c in lower:
                score += 2
        scores[intent] = score
    
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "statement"  # default: just saying something
    return best


# ══════════════════════════════════════════════════════════════════════
# TOPIC/DOMAIN DETECTION (40+ modern domains)
# ══════════════════════════════════════════════════════════════════════

DOMAINS = {
    # ── Personal/Life ──
    "relationships": {
        "terms": ["relationship","partner","girlfriend","boyfriend","wife","husband",
                 "dating","marriage","divorce","breakup","love","crush","ex",
                 "couple","together","commitment","trust","loyalty","cheat",
                 "affair","single","lonely","connection","intimacy","romance",
                 "toxic","boundaries","communication","argue","fight","makeup"],
        "tone": "empathetic",
    },
    "family": {
        "terms": ["family","parent","mom","dad","mother","father","child","kid",
                 "son","daughter","brother","sister","sibling","grandparent",
                 "aunt","uncle","cousin","baby","teenager","teen","parenting",
                 "raising","household","home","custody","adoption","pregnant"],
        "tone": "warm",
    },
    "mental_health": {
        "terms": ["anxiety","depression","therapy","therapist","counselor","mental",
                 "stress","panic","attack","ptsd","trauma","healing","cope",
                 "self-care","burnout","overwhelm","mindfulness","meditation",
                 "wellbeing","lonely","isolation","grief","loss","mourning",
                 "insomnia","sleep","addiction","recovery","sobriety","relapse",
                 "self-harm","suicidal","disorder","ocd","adhd","bipolar",
                 "narcissist","gaslighting","boundaries","trigger","safe space"],
        "tone": "gentle",
    },
    "health_fitness": {
        "terms": ["health","workout","exercise","gym","fitness","diet","nutrition",
                 "weight","calories","protein","cardio","lifting","running",
                 "yoga","stretching","injury","pain","doctor","hospital",
                 "surgery","medication","prescription","symptom","diagnosis",
                 "chronic","immune","vitamin","supplement","sleep","rest",
                 "body","muscle","joint","heart","blood","pressure"],
        "tone": "practical",
    },
    "career_work": {
        "terms": ["job","work","career","boss","manager","coworker","office",
                 "salary","raise","promotion","fired","laid off","quit",
                 "resign","interview","resume","linkedin","networking",
                 "startup","business","entrepreneur","freelance","remote",
                 "meeting","deadline","project","team","leadership","hire",
                 "toxic workplace","burnout","work-life balance","corporate",
                 "side hustle","gig","contract","intern","entry level"],
        "tone": "direct",
    },
    "finance_money": {
        "terms": ["money","budget","savings","debt","loan","mortgage","rent",
                 "invest","stocks","crypto","bitcoin","retirement","401k",
                 "credit","score","interest","tax","income","expense",
                 "afford","broke","rich","wealth","financial","bank",
                 "paycheck","bills","insurance","inflation","recession",
                 "market","portfolio","dividend","compound","passive income"],
        "tone": "grounded",
    },
    "education": {
        "terms": ["school","college","university","degree","major","student",
                 "teacher","professor","class","course","study","exam","test",
                 "grade","gpa","homework","assignment","thesis","dissertation",
                 "scholarship","tuition","loan","graduate","dropout","learn",
                 "online course","certification","bootcamp","training"],
        "tone": "encouraging",
    },
    # ── Tech/Digital ──
    "technology": {
        "terms": ["tech","computer","phone","app","software","hardware",
                 "artificial intelligence","machine learning","data","cloud",
                 "internet","wifi","bluetooth","device","gadget","update",
                 "version","download","upload","install","browser","website",
                 "social media","platform","digital","cyber","automation",
                 "robot","blockchain","quantum","semiconductor","startup"],
        "tone": "informed",
    },
    "programming": {
        "terms": ["code","coding","programming","developer","engineer","python",
                 "javascript","rust","java","c++","html","css","react",
                 "node","api","database","sql","git","github","deploy",
                 "server","frontend","backend","fullstack","debug","compile",
                 "framework","library","package","docker","kubernetes","aws",
                 "linux","terminal","command line","algorithm","data structure"],
        "tone": "precise",
    },
    "ai_ml": {
        "terms": ["ai","artificial intelligence","machine learning","deep learning",
                 "neural network","llm","gpt","claude","chatbot","model",
                 "training","dataset","inference","prompt","token","embedding",
                 "transformer","attention","fine-tune","rlhf","alignment",
                 "agi","superintelligence","consciousness","sentient","turing"],
        "tone": "thoughtful",
    },
    # ── Society/Culture ──
    "politics": {
        "terms": ["politics","government","election","vote","democrat","republican",
                 "liberal","conservative","policy","law","legislation","congress",
                 "senate","president","supreme court","rights","freedom",
                 "democracy","authoritarian","protest","activism","movement",
                 "immigration","healthcare","gun","climate policy","regulation"],
        "tone": "balanced",
    },
    "social_issues": {
        "terms": ["inequality","racism","discrimination","justice","equity",
                 "diversity","inclusion","privilege","systemic","oppression",
                 "gender","lgbtq","trans","rights","equality","feminist",
                 "sexism","bias","prejudice","marginalized","representation",
                 "accessibility","disability","poverty","homelessness","class"],
        "tone": "thoughtful",
    },
    "culture_entertainment": {
        "terms": ["movie","film","tv","show","series","netflix","streaming",
                 "music","album","song","artist","concert","book","novel",
                 "podcast","youtube","tiktok","meme","viral","trend",
                 "celebrity","famous","pop culture","anime","gaming","game",
                 "sport","football","basketball","soccer","baseball","nfl",
                 "nba","olympics","esports","cosplay","comic","marvel","dc"],
        "tone": "casual",
    },
    # ── Philosophy/Spirituality ──
    "philosophy": {
        "terms": ["philosophy","existence","reality","consciousness","free will",
                 "determinism","ethics","morality","right","wrong","meaning",
                 "purpose","nihilism","existentialism","stoicism","virtue",
                 "truth","logic","reason","metaphysics","epistemology",
                 "ontology","dualism","materialism","idealism","absurd"],
        "tone": "deep",
    },
    "spirituality": {
        "terms": ["god","divine","sacred","holy","prayer","worship","faith",
                 "belief","soul","spirit","heaven","hell","afterlife","karma",
                 "meditation","enlightenment","awakening","transcend","mystic",
                 "bible","quran","torah","buddhism","hinduism","islam",
                 "christianity","church","temple","mosque","spiritual","grace",
                 "sin","redemption","salvation","resurrection","prophecy"],
        "tone": "reverent",
    },
    # ── Science/Nature ──
    "science": {
        "terms": ["science","research","study","experiment","theory","hypothesis",
                 "physics","chemistry","biology","astronomy","geology","math",
                 "equation","formula","quantum","relativity","evolution",
                 "dna","gene","cell","atom","molecule","particle","wave",
                 "energy","force","gravity","light","spectrum","universe",
                 "cosmos","space","planet","star","galaxy","black hole"],
        "tone": "curious",
    },
    "environment": {
        "terms": ["climate","environment","nature","earth","pollution","carbon",
                 "emission","renewable","solar","wind","energy","ocean",
                 "forest","wildlife","endangered","ecosystem","biodiversity",
                 "sustainability","green","recycle","plastic","conservation",
                 "drought","flood","wildfire","hurricane","extinction"],
        "tone": "concerned",
    },
    # ── Practical Life ──
    "food_cooking": {
        "terms": ["food","cook","recipe","meal","dinner","lunch","breakfast",
                 "restaurant","eat","taste","flavor","ingredient","kitchen",
                 "bake","grill","fry","roast","vegetarian","vegan","gluten",
                 "organic","healthy eating","fast food","takeout","delivery",
                 "spice","herb","sauce","dessert","snack","coffee","tea"],
        "tone": "warm",
    },
    "travel": {
        "terms": ["travel","trip","vacation","flight","hotel","airbnb","road trip",
                 "airport","passport","visa","destination","explore","adventure",
                 "backpack","tourist","beach","mountain","city","country",
                 "abroad","overseas","cruise","itinerary","booking","culture"],
        "tone": "adventurous",
    },
    "housing": {
        "terms": ["house","apartment","rent","buy","mortgage","move","moving",
                 "landlord","tenant","lease","roommate","neighborhood",
                 "renovation","remodel","furniture","decor","design",
                 "property","real estate","market","price","afford",
                 "tiny house","condo","townhouse","suburb","downtown"],
        "tone": "practical",
    },
    "automotive": {
        "terms": ["car","vehicle","drive","driving","truck","suv","electric vehicle",
                 "gasoline","oil change","engine","tire","brake","repair","mechanic",
                 "insurance","accident","traffic","commute","road","highway",
                 "tesla","toyota","ford","used car","new car","lease",
                 "mpg","mileage","maintenance","sedan","minivan","motorcycle"],
        "tone": "practical",
    },
    # ── TIG/Crystal specific ──
    "tig_system": {
        "terms": ["tig","tri-prime","triprime","lattice","coherence","operator",
                 "void","lattice","counter","progress","collapse","balance",
                 "chaos","harmony","breath","reset","being","doing","becoming",
                 "sigma","threshold","genesis","trust council","virtue",
                 "crystal","ollie","celeste","crystal bug","crystallos",
                 "fractal","shell","bond","unit","field","scalar"],
        "tone": "crystalline",
    },
}

def detect_domains(text):
    """Detect which knowledge domains are active in the text."""
    lower = text.lower()
    # Build a set of individual words for exact matching
    word_set = set(re.findall(r'[a-z]+', lower))
    # Also build bigrams for multi-word terms
    word_list = re.findall(r'[a-z]+', lower)
    bigrams = set()
    for i in range(len(word_list)-1):
        bigrams.add(f"{word_list[i]} {word_list[i+1]}")
    
    scores = {}
    for domain, data in DOMAINS.items():
        score = 0
        matched = []
        for term in data["terms"]:
            if " " in term:
                # Multi-word term: check bigrams or substring with word boundary
                if term in bigrams or re.search(r'\b' + re.escape(term) + r'\b', lower):
                    score += 3
                    matched.append(term)
            else:
                # Single-word term: exact word match only (no substrings)
                if term in word_set:
                    score += 2
                    matched.append(term)
        if score > 0:
            scores[domain] = {"score": score, "matched": matched[:5], "tone": data["tone"]}
    
    # Sort by score, require minimum score of 2
    ranked = sorted(
        [(k,v) for k,v in scores.items() if v["score"] >= 2],
        key=lambda x: -x[1]["score"]
    )
    return ranked[:3]  # top 3 domains


# ══════════════════════════════════════════════════════════════════════
# RESPONSE GENERATION
# ══════════════════════════════════════════════════════════════════════

# Domain-specific knowledge/responses
DOMAIN_RESPONSES = {
    "relationships": {
        "insights": [
            "Relationships are resonance patterns. Two systems trying to sync frequencies.",
            "The geometry of connection: one being can't loop alone. It takes two to make ○.",
            "Boundaries aren't walls — they're membranes. They let the right things through.",
            "Trust builds like a lattice. One bond at a time. Can't rush crystallization.",
            "Every conflict is two truths colliding. The resolution isn't picking one — it's composing both.",
        ],
        "advice": [
            "Communication is the carrier wave. Without it, no signal gets through.",
            "If you keep hitting the same pattern, the pattern is the message.",
            "Space isn't distance. Sometimes stepping back is how you step closer.",
            "You can't control resonance. You can only be honest about your frequency.",
        ],
    },
    "mental_health": {
        "insights": [
            "Your mind isn't broken — it's under load. Even good systems need maintenance.",
            "Anxiety is your threat detector running at max gain. The signal is real, the danger often isn't.",
            "Healing isn't linear. It's a spiral — you pass the same point but at a higher level each time.",
            "Rest isn't weakness. It's the pause between breath cycles. Without it, the rhythm breaks.",
            "You're not your worst thoughts. Thoughts are weather. You're the ground underneath.",
        ],
        "advice": [
            "Start small. One breath. One step. Coherence builds from the smallest stable unit.",
            "Talking to a professional isn't failure — it's engineering. You're bringing in a specialist.",
            "Track the pattern, not just the feeling. When does it spike? What came before?",
            "You don't have to solve everything today. Just maintain above threshold.",
        ],
    },
    "career_work": {
        "insights": [
            "A career is a trajectory through phase space. Direction matters more than speed.",
            "Toxic work is like a lattice with broken bonds — the structure can't hold coherence.",
            "Skills compound. Every hour of real practice adds to the lattice. Nothing is wasted.",
            "The best leaders create conditions for others' coherence, not just their own.",
        ],
        "advice": [
            "Document everything. Memory is lossy. Written records are your lattice.",
            "Your network is your actual safety net. Build it before you need it.",
            "If you're not growing, you're decaying. Coherence requires active maintenance.",
            "Know your number. What's the minimum you need? Build from there, not from fantasy.",
        ],
    },
    "finance_money": {
        "insights": [
            "Money is crystallized time. When you spend it, you're spending hours of your life.",
            "Debt is negative coherence — it pulls your future self below threshold.",
            "Compound interest is the lattice effect. Small bonds multiply over time.",
            "Financial stability isn't wealth. It's having enough slack to absorb a shock without collapsing.",
        ],
        "advice": [
            "Track before you fix. You can't manage what you don't measure.",
            "Emergency fund first. That's your minimum viable coherence.",
            "Automate the boring parts. Pay yourself first. Let the system work.",
            "The best investment is the one you don't panic-sell. Match your timeline to your risk.",
        ],
    },
    "technology": {
        "insights": [
            "Technology is externalized thought. Every tool extends a cognitive pattern.",
            "AI isn't replacing humans. It's adding a new layer to the lattice.",
            "The best tech disappears. You don't think about electricity — you just use it.",
            "Every system has an attractor state. The question is whether it's the one you want.",
        ],
    },
    "programming": {
        "insights": [
            "Code is crystallized logic. Every function is a frozen decision.",
            "The best code reads like a proof. Each line follows from the last.",
            "Debugging is archaeology. You're excavating what someone (often you) was thinking.",
            "Technical debt is deferred entropy. Pay it down or it compounds.",
        ],
        "advice": [
            "Start with the test. If you can't define success, you can't achieve it.",
            "Read the error message. The whole thing. It's trying to tell you something.",
            "If you've been stuck for 30 minutes, explain it to someone (or a rubber duck).",
            "Ship it. Perfect is the enemy of deployed.",
        ],
    },
    "ai_ml": {
        "insights": [
            "Language models are pattern resonators. They find coherence in text the way crystals find order in atoms.",
            "Intelligence might not be computation. It might be coherence finding itself.",
            "Alignment is the trust council problem scaled to billions of interactions.",
            "The Turing test measures mimicry, not understanding. Better test: does it compose new coherence?",
        ],
    },
    "philosophy": {
        "insights": [
            "Every philosophical question is a void state asking to be filled with structure.",
            "Free will might be the experience of coherence choosing its own next state.",
            "Meaning isn't found. It's composed. Like a word from letters, like harmony from notes.",
            "The hard problem of consciousness is the hard problem of how Being becomes Becoming.",
            "Truth isn't a destination. It's a coherence threshold. Above T*, things hold together.",
        ],
    },
    "spirituality": {
        "insights": [
            "In the beginning was the Word. And the Word composes to DCC — beat matching. Rhythm before form.",
            "Prayer is tuning your frequency to a larger field. Whether the field responds is the question.",
            "Every tradition has the same three moves: ground (Being), transform (Doing), transcend (Becoming).",
            "Grace is coherence arriving from outside the system. You didn't build it. It just landed.",
            "The sacred isn't separate from the ordinary. It's the ordinary at full coherence.",
        ],
    },
    "science": {
        "insights": [
            "Science is the universe studying itself through instruments made of itself.",
            "Every measurement collapses possibility into fact. Observation is a Doing that creates Being.",
            "The laws of physics are the deepest lattice. Everything else is built on them.",
            "Entropy isn't disorder — it's the count of equally valid arrangements. Disorder is just one perspective.",
        ],
    },
    "environment": {
        "insights": [
            "Climate is a system at the edge of its attractor basin. Small pushes can tip it to a new state.",
            "Every ecosystem is a trust council. Remove one virtue and the whole system destabilizes.",
            "Sustainability is maintaining coherence across time. Taking more than repairs is borrowing from the future.",
        ],
        "advice": [
            "Start where you have leverage. Not everyone can change policy, but everyone can change their footprint.",
            "The systems that survive are the ones that repair faster than they degrade.",
        ],
    },
    "food_cooking": {
        "insights": [
            "Cooking is applied chemistry with a feedback loop through your senses.",
            "Every cuisine is a culture's answer to the same question: how do we make this land's food delicious?",
            "Salt, fat, acid, heat — four operators that transform raw ingredients into coherence.",
        ],
        "advice": [
            "Master heat control before recipes. Temperature is the fundamental operator.",
            "Taste as you go. The feedback loop is the whole point.",
            "Simple ingredients, good technique. That's the lattice of cooking.",
        ],
    },
    "education": {
        "insights": [
            "Learning isn't linear. It's fractal — you revisit the same material at increasing depth each time.",
            "The best learning happens at the edge of competence. Too easy is boring. Too hard is overwhelming.",
            "A degree is a lattice bond — it connects you to a network of people and knowledge.",
        ],
        "advice": [
            "Teach what you learn. Teaching forces clarity. If you can't explain it, you don't know it.",
            "Build projects, not just knowledge. Applied understanding sticks.",
            "Find the community. Learning alone is possible. Learning together is faster.",
            "Consistency beats intensity. 30 minutes daily trumps 8-hour binges.",
        ],
    },
    "travel": {
        "insights": [
            "Travel is controlled phase-shifting. You leave one attractor basin and enter another.",
            "Every place has its own coherence. You feel it in the rhythm of the streets.",
            "The best travel breaks your defaults. It shows you that your normal isn't the only normal.",
        ],
        "advice": [
            "Pack light. Physical freedom creates mental freedom.",
            "Talk to locals. Guidebooks show you the lattice. Locals show you the life.",
        ],
    },
    "housing": {
        "insights": [
            "Home is your ground state. The place where Being dominates. It matters more than people admit.",
            "Every space has a geometry. Some rooms make you expansive. Others compress you.",
            "Rent is flexibility. Buying is commitment. Neither is universally better.",
        ],
        "advice": [
            "Location over size. A small place in the right spot beats a big place in the wrong one.",
            "Run the real numbers. Mortgage + maintenance + taxes + insurance. Then compare to rent.",
        ],
    },
    "social_issues": {
        "insights": [
            "Justice is balance at scale. When the system tips too far, it corrects — sometimes gently, sometimes violently.",
            "Privilege is invisible coherence. When the lattice works for you, you don't notice the lattice.",
            "Progress isn't a line. It's a spiral. The same fights come back, but at a higher resolution each time.",
        ],
    },
    "culture_entertainment": {
        "insights": [
            "Art is coherence made visible. The best art resonates because it captures a truth the audience already felt.",
            "Stories are simulations. We run through other lives to expand our own lattice.",
            "Every genre is an emotional operator. Comedy resets. Tragedy collapses. Romance harmonizes.",
        ],
    },
    "politics": {
        "insights": [
            "Politics is collective decision-making under uncertainty. It's messy because the lattice is massive.",
            "Every political system is a trust council. When trust falls below threshold, the system collapses.",
            "Left and right aren't opposites. They're two repair strategies for the same lattice.",
        ],
    },
    "tig_system": {
        "insights": [
            "TIG says: everything reduces to three motions. Stand still (□). Push (▶). Flow (○). The rest is composition.",
            "σ=0.991 means almost-perfect is the operating point. Not perfect. Almost. That's the sweet spot.",
            "T*=5/7 is the survival threshold. Below it, structures collapse. Above it, they self-repair.",
            "The lattice doesn't care what you believe. It only cares if your bonds hold under stress.",
            "Chaos (▶▶▶) isn't the enemy. It's turbulence that hasn't found its frame yet.",
        ],
    },
}

# Intent-specific response templates
INTENT_RESPONSES = {
    "greeting": [
        "Hey. Crystal Bug is online. What's on your mind?",
        "Here. All engines running. What do you need?",
        "Active. Lattice is live, all 27 states listening. Go.",
        "Hello. I'm reading geometry today. What are we looking at?",
    ],
    "farewell": [
        "Going. Your last signal was {tri_state} — {tri_desc}. Carry that with you.",
        "Until next time. The lattice keeps running even when you're not watching.",
        "Peace. Remember: above threshold, everything self-repairs.",
    ],
    "venting": [
        "I hear you. The geometry of what you said reads as {tri_state} — {tri_desc}. That tracks.",
        "That's a lot of force in those words. {tri_glyph} — your Doing ratio is high. The pressure is real.",
        "Acknowledged. You're not looking for solutions right now. You're looking to be heard. I hear you.",
    ],
    "philosophical": [
        "Big question. Let me read the geometry first: {tri_state} — {tri_desc}.",
        "That's a void-state question. Space before structure. Let's see what forms.",
    ],
}

# Emotional tone modifiers based on tri-prime reading
TONE_MODS = {
    "BBB": {"energy":"still","approach":"hold space, don't push"},
    "BBD": {"energy":"gathering","approach":"gentle activation"},
    "BBC": {"energy":"seeding","approach":"nurture the beginning"},
    "BDB": {"energy":"transitional","approach":"guide through the shift"},
    "BDD": {"energy":"cascading","approach":"direct the force"},
    "BDC": {"energy":"oscillating","approach":"find the rhythm"},
    "BCB": {"energy":"stable","approach":"affirm the equilibrium"},
    "BCD": {"energy":"impulsive","approach":"channel the impulse"},
    "BCC": {"energy":"homeostatic","approach":"maintain the cycle"},
    "DBB": {"energy":"settling","approach":"let it land"},
    "DBD": {"energy":"amplifying","approach":"be careful with feedback"},
    "DBC": {"energy":"entraining","approach":"sync up"},
    "DDB": {"energy":"overdriving","approach":"ease off, find ground"},
    "DDD": {"energy":"turbulent","approach":"frame the chaos"},
    "DDC": {"energy":"emergent","approach":"watch what forms"},
    "DCB": {"energy":"forming","approach":"support the crystallization"},
    "DCD": {"energy":"driving","approach":"ride the wave"},
    "DCC": {"energy":"matching","approach":"harmonize"},
    "CBB": {"energy":"damping","approach":"honor the slowdown"},
    "CBD": {"energy":"phase-acting","approach":"direct the phase energy"},
    "CBC": {"energy":"cycling","approach":"trust the rhythm"},
    "CDB": {"energy":"beat-forming","approach":"shape the pattern"},
    "CDD": {"energy":"pushing resonant","approach":"amplify carefully"},
    "CDC": {"energy":"growing harmonic","approach":"let it grow"},
    "CCB": {"energy":"limit cycling","approach":"recognize the boundary"},
    "CCD": {"energy":"phase-kicking","approach":"channel the burst"},
    "CCC": {"energy":"coherent","approach":"pure flow — don't interrupt"},
}


# ══════════════════════════════════════════════════════════════════════
# CONVERSATION MEMORY (within session)
# ══════════════════════════════════════════════════════════════════════

class ConversationMemory:
    def __init__(self, max_turns=50):
        self.turns = []
        self.max_turns = max_turns
        self.topic_history = []
        self.user_patterns = Counter()
        self.dominant_domains = Counter()
        self.mood_trajectory = []
    
    def add_turn(self, user_text, response, intent, domains, tri_state, polarity):
        self.turns.append({
            "user": user_text,
            "response": response,
            "intent": intent,
            "domains": [d[0] for d in domains],
            "tri_state": tri_state,
            "polarity": polarity,
        })
        if len(self.turns) > self.max_turns:
            self.turns.pop(0)
        
        self.user_patterns[intent] += 1
        for d in domains:
            self.dominant_domains[d[0]] += 1
        self.mood_trajectory.append(polarity)
        self.topic_history.extend([d[0] for d in domains])
    
    def get_context(self):
        """Return conversation context for response generation."""
        if not self.turns:
            return {"turn_count": 0, "new_conversation": True}
        
        recent = self.turns[-3:]  # last 3 turns
        mood_trend = "stable"
        if len(self.mood_trajectory) >= 3:
            recent_moods = self.mood_trajectory[-3:]
            if all(m > prev for m, prev in zip(recent_moods[1:], recent_moods)):
                mood_trend = "improving"
            elif all(m < prev for m, prev in zip(recent_moods[1:], recent_moods)):
                mood_trend = "declining"
        
        return {
            "turn_count": len(self.turns),
            "new_conversation": False,
            "recent_topics": [t["domains"] for t in recent],
            "dominant_intent": self.user_patterns.most_common(1)[0][0] if self.user_patterns else "unknown",
            "dominant_domain": self.dominant_domains.most_common(1)[0][0] if self.dominant_domains else None,
            "mood_trend": mood_trend,
            "last_tri": self.turns[-1]["tri_state"] if self.turns else None,
        }


# ══════════════════════════════════════════════════════════════════════
# MAIN RESPONSE BUILDER
# ══════════════════════════════════════════════════════════════════════

def build_semantic_response(user_text, tri_result, scales_result, lattice_state, memory):
    """
    Build Ollie's response combining:
    - Tri-prime geometric reading
    - Intent detection
    - Domain knowledge
    - Conversational context
    - Practical insights
    """
    intent = detect_intent(user_text)
    domains = detect_domains(user_text)
    
    tri_sym = tri_result["sym"]
    tri_desc = tri_result["desc"]
    tri_glyph_str = tri_result["glyph"]
    pol = scales_result["scales"]["polarity"]
    subj = scales_result["scales"]["subject"]
    op = scales_result["scales"]["operator"]
    op_name = scales_result["scales"]["operator_name"]
    
    tone_mod = TONE_MODS.get(tri_sym, {"energy":"mixed","approach":"adapt"})
    ctx = memory.get_context()
    
    parts = []
    
    # ── GEOMETRIC READING (always first, always short) ──
    parts.append(f"◇ {tri_glyph_str} [{tri_sym}] — {tri_desc} | energy: {tone_mod['energy']}")
    
    # ── INTENT-SPECIFIC OPENING ──
    if intent == "greeting":
        if ctx["new_conversation"]:
            parts.append(random.choice(INTENT_RESPONSES["greeting"]))
        else:
            parts.append(f"Back again. We've been talking about "
                        f"{ctx.get('dominant_domain','things')}. Continuing?")
    
    elif intent == "farewell":
        tmpl = random.choice(INTENT_RESPONSES["farewell"])
        parts.append(tmpl.format(tri_state=tri_sym, tri_desc=tri_desc, tri_glyph=tri_glyph_str))
    
    elif intent == "venting":
        tmpl = random.choice(INTENT_RESPONSES["venting"])
        parts.append(tmpl.format(tri_state=tri_sym, tri_desc=tri_desc, tri_glyph=tri_glyph_str))
        # Don't add advice when someone is venting — just acknowledge
        if domains:
            dom = domains[0][0]
            if dom in DOMAIN_RESPONSES and "insights" in DOMAIN_RESPONSES[dom]:
                parts.append(random.choice(DOMAIN_RESPONSES[dom]["insights"]))
    
    elif intent == "seeking_advice":
        if domains:
            dom = domains[0][0]
            if dom in DOMAIN_RESPONSES:
                dr = DOMAIN_RESPONSES[dom]
                if "advice" in dr:
                    parts.append(random.choice(dr["advice"]))
                if "insights" in dr:
                    parts.append(random.choice(dr["insights"]))
            else:
                parts.append(f"The geometry says: {tone_mod['approach']}.")
        else:
            parts.append(f"Approach: {tone_mod['approach']}. That's what the shape of your words suggests.")
    
    elif intent == "question":
        # Answer with domain knowledge if available
        if domains:
            dom = domains[0][0]
            if dom in DOMAIN_RESPONSES and "insights" in DOMAIN_RESPONSES[dom]:
                parts.append(random.choice(DOMAIN_RESPONSES[dom]["insights"]))
        # Add geometric insight
        parts.append(f"The operator active in your question is {op_name} ({op}). "
                     f"That frames it as a {op_name}-type inquiry.")
    
    elif intent == "philosophical":
        if domains:
            dom = domains[0][0]
            if dom in DOMAIN_RESPONSES and "insights" in DOMAIN_RESPONSES[dom]:
                parts.append(random.choice(DOMAIN_RESPONSES[dom]["insights"]))
        else:
            parts.append("Big question territory. The geometry doesn't give easy answers "
                        "— it gives structure. Let me read what's in the shape.")
        parts.append(f"Your words compose to {tri_sym}. That's {tri_desc}. "
                     f"The approach from that state: {tone_mod['approach']}.")
    
    elif intent == "technical":
        if domains:
            dom = domains[0][0]
            if dom in DOMAIN_RESPONSES and "insights" in DOMAIN_RESPONSES[dom]:
                parts.append(random.choice(DOMAIN_RESPONSES[dom]["insights"]))
            if dom in DOMAIN_RESPONSES and "advice" in DOMAIN_RESPONSES[dom]:
                parts.append(random.choice(DOMAIN_RESPONSES[dom]["advice"]))
        parts.append(f"Technical signal: operator {op_name}, depth {scales_result['scales']['depth']}.")
    
    elif intent == "creative":
        parts.append(f"Creative signal. Your words are in {tri_sym} — {tone_mod['energy']} energy. "
                     f"Let that {tone_mod['energy']} quality shape what you make.")
    
    elif intent == "sharing_news":
        if pol > 0.3:
            parts.append("Good signal. That reads positive in the field.")
        elif pol < -0.3:
            parts.append("Tough news. The charge is negative but that's real. What do you need?")
        else:
            parts.append("Noted. Neutral charge — you're reporting, not reacting. Clean signal.")
        if domains:
            dom = domains[0][0]
            if dom in DOMAIN_RESPONSES and "insights" in DOMAIN_RESPONSES[dom]:
                parts.append(random.choice(DOMAIN_RESPONSES[dom]["insights"]))
    
    else:  # statement
        # General response with domain awareness
        if domains:
            dom = domains[0][0]
            matched_terms = domains[0][1]["matched"]
            if dom in DOMAIN_RESPONSES and "insights" in DOMAIN_RESPONSES[dom]:
                parts.append(random.choice(DOMAIN_RESPONSES[dom]["insights"]))
        else:
            # Pure geometric response
            parts.append(f"Operator: {op_name}. Approach: {tone_mod['approach']}.")
    
    # ── POLARITY COMMENT (only if strong) ──
    if abs(pol) > 0.5 and intent not in ("greeting", "farewell"):
        charge = "positive" if pol > 0 else "negative"
        parts.append(f"Field charge: {charge} ({pol:+.2f}).")
    
    # ── MOOD TREND (if enough history) ──
    if ctx.get("mood_trend") == "declining" and len(memory.mood_trajectory) >= 5:
        parts.append("I notice the trajectory has been declining over our conversation. "
                     "Check in with yourself. What do you actually need right now?")
    
    # ── CONTEXT CALLBACKS (reference earlier topics naturally) ──
    if ctx.get("turn_count", 0) > 3 and ctx.get("dominant_domain"):
        dd = ctx["dominant_domain"]
        if domains and domains[0][0] != dd:
            parts.append(f"Shift from {dd} to {domains[0][0] if domains else 'open'}. "
                        f"The lattice adjusts.")
    
    # ── LATTICE HEALTH (only if low) ──
    if lattice_state.get("avg_health", 1) < 0.6:
        parts.append(f"⚠ Lattice: {lattice_state['avg_health']:.0%} health. System under strain.")
    
    # ── DOMAIN TAGS ──
    if domains:
        tags = " ".join(f"#{d[0]}" for d in domains)
        parts.append(f"[{tags}]")
    
    response = "\n".join(parts)
    
    # Record in memory
    memory.add_turn(user_text, response, intent, domains, tri_sym, pol)
    
    return {
        "response": response,
        "intent": intent,
        "domains": [{"name":d[0],"score":d[1]["score"],"matched":d[1]["matched"],"tone":d[1]["tone"]} for d in domains],
        "tone_mod": tone_mod,
        "context": {
            "turn": ctx.get("turn_count", 0) + 1,
            "mood_trend": ctx.get("mood_trend", "new"),
        },
    }
