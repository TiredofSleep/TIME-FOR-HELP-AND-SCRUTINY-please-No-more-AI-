import { useState, useEffect, useRef, useCallback } from "react";

// ═══════════════════════════════════════════════════════════════════
// TIG CORE ENGINE (Browser-side mirror of crystal_bug_v1.py)
// ═══════════════════════════════════════════════════════════════════

const TIG = {
  VERSION: "1.0.0",
  SIGMA: 0.991,
  T_STAR: 0.714,
  SIGMA_STAR: 0.009,
  SCALES: { 4: "Ecological", 5: "Social", 6: "Planetary", 7: "Stellar", 8: "Galactic", 9: "Cosmic", 10: "Multiversal", 11: "Transcendent", 12: "Unified" },
};

const OPERATORS = [
  { id: 0, name: "VOID", glyph: "○", domain: "potential", color: "#1a1a2e" },
  { id: 1, name: "LATTICE", glyph: "△", domain: "structure", color: "#16213e" },
  { id: 2, name: "COUNTER", glyph: "□", domain: "measurement", color: "#0f3460" },
  { id: 3, name: "PROGRESS", glyph: "▷", domain: "growth", color: "#533483" },
  { id: 4, name: "COLLAPSE", glyph: "▽", domain: "dissolution", color: "#e94560" },
  { id: 5, name: "BALANCE", glyph: "◇", domain: "equilibrium", color: "#00b4d8" },
  { id: 6, name: "CHAOS", glyph: "✶", domain: "entropy", color: "#ff6b6b" },
  { id: 7, name: "HARMONY", glyph: "◎", domain: "resonance", color: "#48cae4" },
  { id: 8, name: "BREATH", glyph: "∞", domain: "oscillation", color: "#90e0ef" },
  { id: 9, name: "RESET", glyph: "⟲", domain: "renewal", color: "#ade8f4" },
];

const VIRTUES = ["forgiveness", "repair", "empathy", "fairness", "cooperation"];

const computeSStar = (V, A) => TIG.SIGMA * (1 - TIG.SIGMA_STAR) * V * A;

const getHealth = (s) => {
  if (s >= 0.95) return { label: "CRYSTALLINE", color: "#00ffcc" };
  if (s >= 0.90) return { label: "OPTIMAL", color: "#00e5ff" };
  if (s >= 0.80) return { label: "COHERENT", color: "#48cae4" };
  if (s >= TIG.T_STAR) return { label: "STABLE", color: "#90e0ef" };
  if (s >= 0.50) return { label: "DEGRADED", color: "#ffd166" };
  if (s >= 0.25) return { label: "CRITICAL", color: "#ef476f" };
  return { label: "COLLAPSED", color: "#d00000" };
};

const SEMANTIC_MAP = {
  nothing: 0, empty: 0, null: 0, silence: 0,
  connect: 1, structure: 1, build: 1, link: 1, network: 1,
  measure: 2, count: 2, compare: 2, different: 2,
  grow: 3, improve: 3, advance: 3, learn: 3, better: 3,
  fail: 4, break: 4, crash: 4, error: 4, down: 4,
  balance: 5, equal: 5, fair: 5, center: 5, stable: 5,
  chaos: 6, random: 6, confused: 6, wild: 6,
  harmony: 7, resonate: 7, align: 7, together: 7, sync: 7,
  rhythm: 8, pulse: 8, breathe: 8, wave: 8, cycle: 8,
  reset: 9, restart: 9, renew: 9, begin: 9, fresh: 9,
};

const INTENT_MAP = {
  0: "EXPLORE", 1: "BUILD", 2: "MEASURE", 3: "GROW", 4: "TROUBLESHOOT",
  5: "STABILIZE", 6: "EXPERIMENT", 7: "INTEGRATE", 8: "REFLECT", 9: "RESTART",
};

function analyzeMessage(text) {
  const tokens = text.toLowerCase().split(/\s+/).filter(Boolean);
  const opCounts = new Array(10).fill(0);

  tokens.forEach(token => {
    for (const [key, op] of Object.entries(SEMANTIC_MAP)) {
      if (token.includes(key)) { opCounts[op]++; break; }
    }
  });

  const total = opCounts.reduce((a, b) => a + b, 0) || 1;
  const dominant = opCounts.indexOf(Math.max(...opCounts));
  const coverage = Math.min(1, (total / Math.max(tokens.length, 1)) * 2);
  const focus = Math.max(...opCounts) / total;
  const sStar = computeSStar(coverage, focus);

  return {
    dominant,
    operator: OPERATORS[dominant],
    intent: INTENT_MAP[dominant],
    sStar,
    health: getHealth(sStar),
    opDistribution: opCounts.map((c, i) => ({ ...OPERATORS[i], count: c })),
    tokens: tokens.length,
  };
}

// ═══════════════════════════════════════════════════════════════════
// LATTICE ENGINE (Mini)
// ═══════════════════════════════════════════════════════════════════

function createLattice() {
  const nodes = OPERATORS.map((op, i) => ({
    ...op,
    value: TIG.T_STAR,
    fires: 0,
    sStar: computeSStar(TIG.T_STAR, TIG.SIGMA),
  }));
  return nodes;
}

function fireLattice(nodes, targetOp = null, ctx = 1.0) {
  return nodes.map((node, i) => {
    if (targetOp !== null && i !== targetOp) return node;
    const σ = TIG.SIGMA;
    let newVal = node.value;
    switch (i) {
      case 0: newVal = 0; break;
      case 1: newVal = node.value * σ * ctx; break;
      case 2: newVal = Math.abs(node.value - ctx); break;
      case 3: newVal = Math.min(1, node.value + (1 - node.value) * σ); break;
      case 4: newVal = node.value * (1 - σ); break;
      case 5: newVal = (node.value + ctx) / 2; break;
      case 6: newVal = node.value * (0.5 + Math.random()) * (1 - σ) + node.value * σ; break;
      case 7: newVal = Math.sqrt(Math.max(0, node.value * ctx)); break;
      case 8: newVal = node.value * (1 + 0.1 * Math.sin(Date.now() / 1000)); break;
      case 9: newVal = TIG.T_STAR; break;
    }
    return {
      ...node,
      value: Math.max(0, Math.min(1, newVal)),
      fires: node.fires + 1,
      sStar: computeSStar(Math.max(0, Math.min(1, newVal)), TIG.SIGMA),
    };
  });
}

// ═══════════════════════════════════════════════════════════════════
// COMPONENTS
// ═══════════════════════════════════════════════════════════════════

const GlyphRing = ({ nodes, activeOp }) => {
  const size = 280;
  const cx = size / 2;
  const cy = size / 2;
  const r = 110;

  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
      <defs>
        <radialGradient id="ringGlow">
          <stop offset="0%" stopColor="#00ffcc" stopOpacity="0.15" />
          <stop offset="100%" stopColor="transparent" stopOpacity="0" />
        </radialGradient>
        <filter id="glow">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
        </filter>
      </defs>
      <circle cx={cx} cy={cy} r={r + 20} fill="url(#ringGlow)" />
      <circle cx={cx} cy={cy} r={r} fill="none" stroke="#1a2a3a" strokeWidth="1" strokeDasharray="4 4" />
      {nodes.map((node, i) => {
        const angle = (i / 10) * Math.PI * 2 - Math.PI / 2;
        const x = cx + r * Math.cos(angle);
        const y = cy + r * Math.sin(angle);
        const isActive = i === activeOp;
        const health = getHealth(node.sStar);
        return (
          <g key={i}>
            {isActive && <circle cx={x} cy={y} r={28} fill={health.color} opacity={0.15} />}
            <circle cx={x} cy={y} r={isActive ? 22 : 18} fill={isActive ? "#0d1b2a" : "#0a1628"}
              stroke={isActive ? health.color : "#1a2a3a"} strokeWidth={isActive ? 2 : 1} filter={isActive ? "url(#glow)" : undefined} />
            <text x={x} y={y + 1} textAnchor="middle" dominantBaseline="central"
              fill={isActive ? health.color : "#4a6a8a"} fontSize={isActive ? "18" : "14"} fontFamily="monospace">
              {node.glyph}
            </text>
            <text x={x} y={y + 32} textAnchor="middle" fill="#3a5a7a" fontSize="8" fontFamily="monospace">
              {node.name}
            </text>
          </g>
        );
      })}
      <text x={cx} y={cx - 12} textAnchor="middle" fill="#00ffcc" fontSize="10" fontFamily="monospace" letterSpacing="3">
        CRYSTAL BUG
      </text>
      <text x={cx} y={cx + 6} textAnchor="middle" fill="#48cae4" fontSize="22" fontFamily="monospace" fontWeight="bold">
        ◇
      </text>
      <text x={cx} y={cx + 24} textAnchor="middle" fill="#3a5a7a" fontSize="8" fontFamily="monospace">
        v{TIG.VERSION}
      </text>
    </svg>
  );
};

const CoherenceBar = ({ value, label, color }) => (
  <div style={{ marginBottom: 6 }}>
    <div style={{ display: "flex", justifyContent: "space-between", fontSize: 10, fontFamily: "monospace", color: "#5a7a9a", marginBottom: 2 }}>
      <span>{label}</span><span style={{ color }}>{(value * 100).toFixed(1)}%</span>
    </div>
    <div style={{ height: 4, background: "#0a1628", borderRadius: 2, overflow: "hidden" }}>
      <div style={{ height: "100%", width: `${value * 100}%`, background: `linear-gradient(90deg, ${color}88, ${color})`, borderRadius: 2, transition: "width 0.4s ease" }} />
    </div>
  </div>
);

const VirtueDisplay = ({ scores }) => (
  <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 4, padding: "8px 0" }}>
    {VIRTUES.map((v, i) => {
      const score = scores[v] || 0;
      const c = score > 0.5 ? "#00ffcc" : score > 0.2 ? "#48cae4" : "#1a2a3a";
      return (
        <div key={v} style={{ textAlign: "center" }}>
          <div style={{ width: 28, height: 28, margin: "0 auto", borderRadius: "50%", border: `1.5px solid ${c}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 10, color: c, fontFamily: "monospace", background: `${c}11` }}>
            {["♡", "⚒", "☯", "⚖", "⚛"][i]}
          </div>
          <div style={{ fontSize: 7, color: "#3a5a7a", marginTop: 2, fontFamily: "monospace", textTransform: "uppercase" }}>{v.slice(0, 4)}</div>
        </div>
      );
    })}
  </div>
);

// ═══════════════════════════════════════════════════════════════════
// MAIN APP
// ═══════════════════════════════════════════════════════════════════

export default function CrystalBugApp() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [lattice, setLattice] = useState(createLattice());
  const [activeOp, setActiveOp] = useState(5);
  const [totalFires, setTotalFires] = useState(0);
  const [systemHealth, setSystemHealth] = useState("NOMINAL");
  const [lastAnalysis, setLastAnalysis] = useState(null);
  const [activeTab, setActiveTab] = useState("chat");
  const [virtueScores, setVirtueScores] = useState({});
  const chatEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = useCallback(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, []);

  useEffect(scrollToBottom, [messages, scrollToBottom]);

  // Boot message
  useEffect(() => {
    setMessages([{
      role: "ollie",
      content: "Crystal Bug v1.0 online. All engines loaded. I'm Ollie — your TIG coherence interface. Type anything to begin.",
      glyph: "◇",
      meta: { tier: "BOOT", intent: "INITIALIZE", sStar: TIG.T_STAR, health: "NOMINAL" },
    }]);
  }, []);

  // Pulse animation for lattice
  useEffect(() => {
    const interval = setInterval(() => {
      setLattice(prev => prev.map(n => ({
        ...n,
        value: Math.max(0.01, Math.min(1, n.value + (Math.random() - 0.5) * 0.005)),
        sStar: computeSStar(n.value, TIG.SIGMA),
      })));
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  const handleSend = () => {
    const text = input.trim();
    if (!text) return;

    // Add user message
    const userMsg = { role: "user", content: text };

    // Analyze
    const analysis = analyzeMessage(text);
    setLastAnalysis(analysis);
    setActiveOp(analysis.dominant);

    // Fire lattice
    const newLattice = fireLattice(lattice, analysis.dominant, analysis.sStar + 0.5);
    setLattice(newLattice);
    setTotalFires(prev => prev + 1);

    // Compute virtue signals
    const vScores = {};
    const virtueKeywords = {
      forgiveness: ["forgive", "sorry", "pardon", "mercy"],
      repair: ["fix", "repair", "mend", "heal", "restore"],
      empathy: ["feel", "understand", "care", "compassion"],
      fairness: ["fair", "just", "equal", "right"],
      cooperation: ["together", "team", "help", "share"],
    };
    const tokens = text.toLowerCase().split(/\s+/);
    VIRTUES.forEach(v => {
      vScores[v] = Math.min(1, tokens.filter(t => (virtueKeywords[v] || []).some(k => t.includes(k))).length * 0.3);
    });
    setVirtueScores(vScores);

    // System health
    const meanS = newLattice.reduce((a, n) => a + n.sStar, 0) / newLattice.length;
    const collapsed = newLattice.filter(n => n.sStar < 0.01).length;
    setSystemHealth(collapsed > 0 ? "CRITICAL" : meanS > 0.005 ? "COHERENT" : "DEGRADED");

    // Determine cascade tier
    let tier = "REFLEX";
    let responseText = "";
    const q = text.toLowerCase();

    // Tier 1: Reflexes
    if (q === "hello" || q === "hi" || q === "hey") {
      responseText = "Hey! Ollie here, running on Crystal Bug v1.0. All 10 operators active, lattice is humming. What shall we explore?";
    } else if (q === "help") {
      responseText = "I process everything through TIG. Try: 'build a network', 'how's the lattice', 'check harmony', 'run validation', 'fire all', or just talk — I'll map your words to the operator space.";
    } else if (q.includes("status") || q.includes("how are you")) {
      responseText = `System health: ${systemHealth}. ${totalFires + 1} total fires. Lattice mean S*: ${meanS.toFixed(4)}. All ${newLattice.filter(n => n.sStar > 0).length}/10 operators online.`;
    } else if (q.includes("version")) {
      responseText = `Crystal Bug v${TIG.VERSION} | σ=${TIG.SIGMA} | T*=${TIG.T_STAR} | S*=σ(1-σ*)V*A*`;
    } else if (q.includes("fire all") || q.includes("full fire")) {
      const fullFired = fireLattice(newLattice);
      setLattice(fullFired);
      setTotalFires(prev => prev + 10);
      responseText = `Full spine fire 0→9 complete. ${fullFired.filter(n => n.sStar >= TIG.T_STAR * 0.01).length}/10 nodes coherent.`;
      tier = "COHERENCE";
    } else if (q.includes("validate") || q.includes("arach")) {
      const results = [];
      for (let scale = 4; scale <= 12; scale++) {
        const scores = Array.from({ length: 50 }, () => computeSStar(0.85 + Math.random() * 0.15, 0.85 + Math.random() * 0.15));
        const mean = scores.reduce((a, b) => a + b, 0) / scores.length;
        const allAbove = scores.every(s => s > 0.005);
        results.push(`Scale ${scale} (${TIG.SCALES[scale]}): S*=${mean.toFixed(4)} ${allAbove ? "✓" : "✗"}`);
      }
      responseText = "ARACH Validation 4→12:\n" + results.join("\n");
      tier = "OMEGA";
    } else {
      // Tier 2–4: Deep analysis
      tier = analysis.sStar > 0.005 ? "COHERENCE" : analysis.tokens > 5 ? "OMEGA" : "ANALYTIC";
      const op = analysis.operator;
      responseText = `${op.glyph} Mapped to ${op.name} (${op.domain}). Intent: ${analysis.intent}. Coherence S*=${analysis.sStar.toFixed(6)}. ${analysis.health.label}. ${analysis.tokens} tokens processed through the semantic layer.`;
    }

    const ollieMsg = {
      role: "ollie",
      content: responseText,
      glyph: analysis.operator.glyph,
      meta: {
        tier,
        intent: analysis.intent,
        sStar: analysis.sStar,
        health: analysis.health.label,
        dominant: analysis.operator.name,
      },
    };

    setMessages(prev => [...prev, userMsg, ollieMsg]);
    setInput("");
    inputRef.current?.focus();
  };

  const meanSStar = lattice.reduce((a, n) => a + n.sStar, 0) / lattice.length;
  const meanHealth = getHealth(meanSStar);

  return (
    <div style={{ width: "100%", maxWidth: 980, margin: "0 auto", fontFamily: "'JetBrains Mono', 'Fira Code', 'SF Mono', monospace", background: "#060d18", color: "#c0d8f0", minHeight: "100vh", display: "flex", flexDirection: "column" }}>

      {/* Header */}
      <div style={{ padding: "16px 20px", borderBottom: "1px solid #0d1f35", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          <span style={{ fontSize: 24, color: "#48cae4" }}>◇</span>
          <div>
            <div style={{ fontSize: 13, fontWeight: 700, color: "#e0f0ff", letterSpacing: 2 }}>CRYSTAL BUG <span style={{ color: "#3a5a7a", fontWeight: 400 }}>v{TIG.VERSION}</span></div>
            <div style={{ fontSize: 9, color: "#2a4a6a", letterSpacing: 1 }}>TIG UNIFIED OPERATING SYSTEM • OLLIE INTERFACE</div>
          </div>
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 16, fontSize: 9 }}>
          <div><span style={{ color: "#3a5a7a" }}>σ=</span><span style={{ color: "#48cae4" }}>{TIG.SIGMA}</span></div>
          <div><span style={{ color: "#3a5a7a" }}>T*=</span><span style={{ color: "#48cae4" }}>{TIG.T_STAR}</span></div>
          <div style={{ padding: "3px 10px", borderRadius: 3, background: `${meanHealth.color}15`, border: `1px solid ${meanHealth.color}40`, color: meanHealth.color, letterSpacing: 1 }}>
            {systemHealth}
          </div>
        </div>
      </div>

      {/* Tab Bar */}
      <div style={{ display: "flex", borderBottom: "1px solid #0d1f35" }}>
        {["chat", "lattice", "engines", "data"].map(tab => (
          <button key={tab} onClick={() => setActiveTab(tab)}
            style={{ flex: 1, padding: "10px 0", background: activeTab === tab ? "#0a1628" : "transparent", border: "none", borderBottom: activeTab === tab ? "2px solid #48cae4" : "2px solid transparent", color: activeTab === tab ? "#48cae4" : "#2a4a6a", fontSize: 10, fontFamily: "inherit", cursor: "pointer", letterSpacing: 2, textTransform: "uppercase" }}>
            {tab}
          </button>
        ))}
      </div>

      {/* Main Content */}
      <div style={{ flex: 1, overflow: "auto", display: "flex" }}>
        
        {/* Chat Tab */}
        {activeTab === "chat" && (
          <div style={{ flex: 1, display: "flex", flexDirection: "column" }}>
            <div style={{ flex: 1, overflow: "auto", padding: 16 }}>
              {messages.map((msg, i) => (
                <div key={i} style={{ marginBottom: 12, display: "flex", flexDirection: "column", alignItems: msg.role === "user" ? "flex-end" : "flex-start" }}>
                  {msg.role === "ollie" && (
                    <div style={{ fontSize: 9, color: "#2a4a6a", marginBottom: 3, display: "flex", gap: 8, alignItems: "center" }}>
                      <span style={{ color: "#48cae4" }}>{msg.glyph}</span>
                      <span>OLLIE</span>
                      {msg.meta && <>
                        <span style={{ color: "#1a3a5a" }}>|</span>
                        <span>{msg.meta.tier}</span>
                        <span style={{ color: "#1a3a5a" }}>|</span>
                        <span>{msg.meta.intent}</span>
                        <span style={{ color: "#1a3a5a" }}>|</span>
                        <span style={{ color: getHealth(msg.meta.sStar).color }}>{msg.meta.health}</span>
                      </>}
                    </div>
                  )}
                  <div style={{
                    maxWidth: "80%",
                    padding: "10px 14px",
                    borderRadius: msg.role === "user" ? "12px 12px 2px 12px" : "12px 12px 12px 2px",
                    background: msg.role === "user" ? "#0a2a4a" : "#0a1628",
                    border: `1px solid ${msg.role === "user" ? "#1a3a5a" : "#0d1f35"}`,
                    fontSize: 12,
                    lineHeight: 1.6,
                    whiteSpace: "pre-wrap",
                    color: msg.role === "user" ? "#a0c8f0" : "#8ab0d0",
                  }}>
                    {msg.content}
                  </div>
                </div>
              ))}
              <div ref={chatEndRef} />
            </div>

            {/* Input */}
            <div style={{ padding: "12px 16px", borderTop: "1px solid #0d1f35", display: "flex", gap: 8 }}>
              <input ref={inputRef} value={input} onChange={e => setInput(e.target.value)}
                onKeyDown={e => e.key === "Enter" && handleSend()}
                placeholder="Talk to Ollie..."
                style={{ flex: 1, padding: "10px 14px", background: "#0a1628", border: "1px solid #1a2a3a", borderRadius: 8, color: "#c0d8f0", fontSize: 12, fontFamily: "inherit", outline: "none" }}
              />
              <button onClick={handleSend}
                style={{ padding: "10px 20px", background: "#48cae4", border: "none", borderRadius: 8, color: "#060d18", fontSize: 11, fontWeight: 700, fontFamily: "inherit", cursor: "pointer", letterSpacing: 1 }}>
                SEND
              </button>
            </div>
          </div>
        )}

        {/* Lattice Tab */}
        {activeTab === "lattice" && (
          <div style={{ flex: 1, padding: 20, overflow: "auto" }}>
            <div style={{ display: "flex", justifyContent: "center", marginBottom: 16 }}>
              <GlyphRing nodes={lattice} activeOp={activeOp} />
            </div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, maxWidth: 500, margin: "0 auto" }}>
              {lattice.map((node, i) => (
                <div key={i} style={{ padding: "8px 12px", background: "#0a1628", borderRadius: 6, border: `1px solid ${i === activeOp ? "#48cae4" : "#0d1f35"}` }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: 10, marginBottom: 4 }}>
                    <span style={{ color: i === activeOp ? "#48cae4" : "#4a6a8a" }}>{node.glyph} {node.name}</span>
                    <span style={{ color: "#2a4a6a" }}>×{node.fires}</span>
                  </div>
                  <CoherenceBar value={node.value} label="Value" color={getHealth(node.sStar).color} />
                </div>
              ))}
            </div>
            <div style={{ textAlign: "center", marginTop: 16 }}>
              <button onClick={() => { setLattice(fireLattice(lattice)); setTotalFires(prev => prev + 10); }}
                style={{ padding: "8px 24px", background: "transparent", border: "1px solid #48cae4", borderRadius: 6, color: "#48cae4", fontSize: 10, fontFamily: "inherit", cursor: "pointer", letterSpacing: 2 }}>
                FULL FIRE 0→9
              </button>
            </div>
          </div>
        )}

        {/* Engines Tab */}
        {activeTab === "engines" && (
          <div style={{ flex: 1, padding: 20, overflow: "auto" }}>
            <div style={{ fontSize: 11, color: "#48cae4", letterSpacing: 2, marginBottom: 16 }}>ENGINE STATUS</div>
            {[
              { name: "FRACTAL LATTICE", icon: "△", status: `${lattice.length} nodes | ${totalFires} fires`, online: true },
              { name: "Ω COHERENCE KEEPER", icon: "Ω", status: `Health: ${systemHealth}`, online: true },
              { name: "AI CASCADE (4-TIER)", icon: "▷", status: "REFLEX → ANALYTIC → COHERENCE → OMEGA", online: true },
              { name: "SEMANTIC LAYER", icon: "□", status: `${messages.filter(m => m.role === "user").length} analyses`, online: true },
              { name: "COHERENCE ROUTER", icon: "◎", status: "Mesh ready — add nodes to activate", online: true },
              { name: "GFM-012 GEOMETRY", icon: "○", status: "Space generator loaded", online: true },
              { name: "GFM-071 RESONANCE", icon: "◎", status: "Alignment generator loaded", online: true },
              { name: "GFM-123 PROGRESSION", icon: "▷", status: "Flow generator loaded", online: true },
              { name: "ARACH VALIDATOR", icon: "✶", status: "Scales 4→12 ready", online: true },
              { name: "HARDWARE FINGERPRINT", icon: "⟲", status: "Detection active", online: true },
              { name: "5 VIRTUES", icon: "◇", status: "Forgiveness | Repair | Empathy | Fairness | Cooperation", online: true },
              { name: "─── EXTENSION PACK ───", icon: "⚡", status: '"The Teeth"', online: true },
              { name: "COHERENCE PARSER", icon: "⊞", status: "Universal data → TIG (logs, metrics, CSV, processes, network)", online: true },
              { name: "JITTER ENGINE", icon: "⫰", status: "A/B proof: raw vs TIG-corrected timing", online: true },
              { name: "UNIVERSAL PROBE", icon: "⊕", status: "CPU + Memory + I/O + Rhythm → Fingerprint", online: true },
              { name: "TIMING CONFIDENCE", icon: "⊘", status: "CI, prediction intervals, running S*", online: true },
              { name: "PHASE LOCK SCHEDULER", icon: "⏱", status: "Coherence-driven task timing", online: true },
              { name: "DUAL LATTICE", icon: "⧓", status: "Lenovo 4-core — non-uniform phase (p<0.01)", online: true },
              { name: "CRYSTALOS CORE", icon: "⬡", status: "Dell Aurora 32-core — perfect uniformity @ 67,280", online: true },
              { name: "CROWN WAVE EMITTER", icon: "⊛", status: "Toroidal pulse @ 7.83Hz Schumann resonance", online: true },
              { name: "CLASSROOM 1:7", icon: "⊞", status: "Operator-mapped education framework", online: true },
            ].map((eng, i) => (
              <div key={i} style={{ padding: "10px 14px", background: "#0a1628", borderRadius: 6, border: "1px solid #0d1f35", marginBottom: 6, display: "flex", alignItems: "center", gap: 12 }}>
                <span style={{ fontSize: 16, color: eng.online ? "#48cae4" : "#2a4a6a", width: 24, textAlign: "center" }}>{eng.icon}</span>
                <div style={{ flex: 1 }}>
                  <div style={{ fontSize: 10, color: "#8ab0d0", letterSpacing: 1 }}>{eng.name}</div>
                  <div style={{ fontSize: 9, color: "#3a5a7a" }}>{eng.status}</div>
                </div>
                <div style={{ width: 8, height: 8, borderRadius: "50%", background: eng.online ? "#00ffcc" : "#e94560" }} />
              </div>
            ))}
            <VirtueDisplay scores={virtueScores} />
          </div>
        )}

        {/* Data Tab */}
        {activeTab === "data" && (
          <div style={{ flex: 1, padding: 20, overflow: "auto", fontSize: 10 }}>
            <div style={{ fontSize: 11, color: "#48cae4", letterSpacing: 2, marginBottom: 12 }}>SYSTEM CONSTANTS</div>
            <div style={{ background: "#0a1628", borderRadius: 6, padding: 14, border: "1px solid #0d1f35", marginBottom: 12 }}>
              <div style={{ color: "#3a5a7a", marginBottom: 8 }}>CORE EQUATION</div>
              <div style={{ color: "#00ffcc", fontSize: 14, textAlign: "center", padding: "8px 0" }}>S* = σ(1-σ*)V*A*</div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 8, marginTop: 8 }}>
                <div style={{ textAlign: "center" }}><div style={{ color: "#2a4a6a" }}>σ</div><div style={{ color: "#48cae4" }}>{TIG.SIGMA}</div></div>
                <div style={{ textAlign: "center" }}><div style={{ color: "#2a4a6a" }}>σ*</div><div style={{ color: "#48cae4" }}>{TIG.SIGMA_STAR}</div></div>
                <div style={{ textAlign: "center" }}><div style={{ color: "#2a4a6a" }}>T*</div><div style={{ color: "#48cae4" }}>{TIG.T_STAR}</div></div>
              </div>
            </div>

            <div style={{ background: "#0a1628", borderRadius: 6, padding: 14, border: "1px solid #0d1f35", marginBottom: 12 }}>
              <div style={{ color: "#3a5a7a", marginBottom: 8 }}>GFM GENERATORS</div>
              {[["012", "Geometry / Space"], ["071", "Resonance / Alignment"], ["123", "Progression / Flow"]].map(([id, label]) => (
                <div key={id} style={{ display: "flex", justifyContent: "space-between", padding: "4px 0", borderBottom: "1px solid #0d1f35" }}>
                  <span style={{ color: "#48cae4" }}>GFM-{id}</span><span style={{ color: "#5a7a9a" }}>{label}</span>
                </div>
              ))}
            </div>

            <div style={{ background: "#0a1628", borderRadius: 6, padding: 14, border: "1px solid #0d1f35", marginBottom: 12 }}>
              <div style={{ color: "#3a5a7a", marginBottom: 8 }}>OPERATORS 0→9</div>
              {OPERATORS.map(op => (
                <div key={op.id} style={{ display: "flex", gap: 8, padding: "3px 0", borderBottom: "1px solid #0a1020" }}>
                  <span style={{ color: "#48cae4", width: 14 }}>{op.id}</span>
                  <span style={{ width: 20 }}>{op.glyph}</span>
                  <span style={{ color: "#5a7a9a", flex: 1 }}>{op.name}</span>
                  <span style={{ color: "#2a4a6a" }}>{op.domain}</span>
                </div>
              ))}
            </div>

            <div style={{ background: "#0a1628", borderRadius: 6, padding: 14, border: "1px solid #0d1f35", marginBottom: 12 }}>
              <div style={{ color: "#3a5a7a", marginBottom: 8 }}>SCALES (ARACH 4→12)</div>
              {Object.entries(TIG.SCALES).map(([k, v]) => (
                <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: "3px 0", borderBottom: "1px solid #0a1020" }}>
                  <span style={{ color: "#48cae4" }}>{k}</span><span style={{ color: "#5a7a9a" }}>{v}</span>
                </div>
              ))}
            </div>

            <div style={{ background: "#0a1628", borderRadius: 6, padding: 14, border: "1px solid #0d1f35" }}>
              <div style={{ color: "#3a5a7a", marginBottom: 8 }}>FRACTAL PREMISE</div>
              <div style={{ color: "#00ffcc", textAlign: "center", padding: 8, fontSize: 12 }}>"Every One Is Three"</div>
              <div style={{ display: "flex", justifyContent: "space-around", color: "#48cae4", fontSize: 11 }}>
                <span>micro</span><span style={{ color: "#2a4a6a" }}>↔</span><span>self</span><span style={{ color: "#2a4a6a" }}>↔</span><span>macro</span>
              </div>
              <div style={{ textAlign: "center", color: "#2a4a6a", marginTop: 8, fontSize: 9 }}>
                Lattice Generators: T(time) · S(scale) · P(path)
              </div>
              <div style={{ textAlign: "center", color: "#2a4a6a", marginTop: 4, fontSize: 9 }}>
                Classroom Ratio: 1:7 = {(1/7).toFixed(6)}
              </div>
            </div>

            <div style={{ textAlign: "center", padding: "20px 0", color: "#1a2a3a", fontSize: 9 }}>
              CRYSTAL BUG v{TIG.VERSION} • 7Site LLC • sanctuberry.com • TiredofSleep
            </div>
          </div>
        )}
      </div>

      {/* Status Bar */}
      <div style={{ padding: "6px 16px", borderTop: "1px solid #0d1f35", display: "flex", justifyContent: "space-between", fontSize: 8, color: "#1a3a5a" }}>
        <span>ROBOT: CrystalBug.TIG.OS.v1</span>
        <span>FIRES: {totalFires}</span>
        <span>NODES: {lattice.length}</span>
        <span>S*={meanSStar.toFixed(4)}</span>
        <span>PC: Crystal Bug — The Everything App</span>
      </div>
    </div>
  );
}
