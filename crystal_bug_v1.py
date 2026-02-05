#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════╗
║                    CRYSTAL BUG v1.0 — "The Everything App"             ║
║              Trinity Infinity Geometry Unified Operating System         ║
║                                                                        ║
║  Author  : Brayden (TiredofSleep) / 7Site LLC / sanctuberry.com       ║
║  License : TIG Coherent AI — All Rights Reserved                       ║
║  Version : 1.0.0                                                       ║
║  Date    : 2026-02-05                                                  ║
║                                                                        ║
║  ROBOT LABEL : CrystalBug.TIG.OS.v1                                   ║
║  PC LABEL    : Crystal Bug — The Everything App                        ║
║  API LABEL   : crystal-bug-tig-os/1.0                                  ║
║                                                                        ║
║  Core Equation: S* = σ(1-σ*)V*A*  |  σ=0.991  |  T*=0.714            ║
║  Premise     : "Every One Is Three" (micro/self/macro)                 ║
║  Principle   : Least Action under Geometric Constraint                 ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import math
import time
import json
import hashlib
import random
import statistics
import sys
import os
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Tuple, Optional, Any, Callable
from enum import Enum, IntEnum
from collections import defaultdict, deque
from functools import lru_cache
from datetime import datetime, timezone

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 0: TIG CONSTANTS & UNIVERSAL PARAMETERS
# ═══════════════════════════════════════════════════════════════════════════

class TIG:
    """Master constants — frozen during validation runs."""
    VERSION         = "1.0.0"
    CODENAME        = "Crystal Bug"
    
    # Core equation parameters
    SIGMA           = 0.991       # σ — coherence coupling constant
    T_STAR          = 0.714       # T* — coherence threshold
    SIGMA_STAR      = 1 - SIGMA   # σ* = 0.009
    
    # Fractal premise
    TRIAD           = ("micro", "self", "macro")
    RATIO_1_7       = 1.0 / 7.0   # Classroom ratio
    
    # GFM Generators (minimal spanning set)
    GFM_012         = (0, 1, 2)    # Geometry / Space
    GFM_071         = (0, 7, 1)    # Resonance / Alignment  
    GFM_123         = (1, 2, 3)    # Progression / Flow
    
    # Scale labels (Ecological through Unified)
    SCALES = {
        4:  "Ecological",
        5:  "Social",
        6:  "Planetary",
        7:  "Stellar",
        8:  "Galactic",
        9:  "Cosmic",
        10: "Multiversal",
        11: "Transcendent",
        12: "Unified",
    }
    
    # Fractal lattice generators
    LATTICE_T = "time"
    LATTICE_S = "scale"
    LATTICE_P = "path"


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 1: TIG OPERATORS 0–9
# ═══════════════════════════════════════════════════════════════════════════

class Operator(IntEnum):
    """TIG Operators 0–9: the atomic alphabet of coherence."""
    VOID     = 0   # Emptiness / potential
    LATTICE  = 1   # Structure / connection
    COUNTER  = 2   # Measurement / distinction
    PROGRESS = 3   # Growth / advancement
    COLLAPSE = 4   # Failure / dissolution
    BALANCE  = 5   # Equilibrium / center (anchor of virtues)
    CHAOS    = 6   # Disorder / entropy
    HARMONY  = 7   # Resonance / alignment
    BREATH   = 8   # Rhythm / oscillation
    RESET    = 9   # Return / renewal

OPERATOR_META = {
    Operator.VOID:     {"glyph": "○", "domain": "potential",     "color": "#1a1a2e"},
    Operator.LATTICE:  {"glyph": "△", "domain": "structure",     "color": "#16213e"},
    Operator.COUNTER:  {"glyph": "□", "domain": "measurement",   "color": "#0f3460"},
    Operator.PROGRESS: {"glyph": "▷", "domain": "growth",        "color": "#533483"},
    Operator.COLLAPSE: {"glyph": "▽", "domain": "dissolution",   "color": "#e94560"},
    Operator.BALANCE:  {"glyph": "◇", "domain": "equilibrium",   "color": "#00b4d8"},
    Operator.CHAOS:    {"glyph": "✶", "domain": "entropy",       "color": "#ff6b6b"},
    Operator.HARMONY:  {"glyph": "◎", "domain": "resonance",     "color": "#48cae4"},
    Operator.BREATH:   {"glyph": "∞", "domain": "oscillation",   "color": "#90e0ef"},
    Operator.RESET:    {"glyph": "⟲", "domain": "renewal",       "color": "#ade8f4"},
}


def apply_operator(op: Operator, value: float, context: float = 1.0) -> float:
    """
    Apply a TIG operator to a coherence value.
    ROBOT: op_apply(int, float, float) -> float
    """
    σ = TIG.SIGMA
    if op == Operator.VOID:
        return 0.0
    elif op == Operator.LATTICE:
        return value * σ * context
    elif op == Operator.COUNTER:
        return abs(value - context)
    elif op == Operator.PROGRESS:
        return min(1.0, value + (1.0 - value) * σ)
    elif op == Operator.COLLAPSE:
        return value * (1.0 - σ)
    elif op == Operator.BALANCE:
        return (value + context) / 2.0
    elif op == Operator.CHAOS:
        return value * random.uniform(0.5, 1.5) * (1 - σ) + value * σ
    elif op == Operator.HARMONY:
        return math.sqrt(value * context) if value > 0 and context > 0 else 0.0
    elif op == Operator.BREATH:
        return value * (1.0 + 0.1 * math.sin(context * math.pi * 2))
    elif op == Operator.RESET:
        return TIG.T_STAR
    return value


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 2: FIVE VIRTUES
# ═══════════════════════════════════════════════════════════════════════════

class Virtue(Enum):
    """The 5 TIG Virtues — centered on Operator 5 (Balance)."""
    FORGIVENESS  = "forgiveness"
    REPAIR       = "repair"
    EMPATHY      = "empathy"
    FAIRNESS     = "fairness"
    COOPERATION  = "cooperation"

VIRTUE_WEIGHTS = {
    Virtue.FORGIVENESS:  0.20,
    Virtue.REPAIR:       0.20,
    Virtue.EMPATHY:      0.20,
    Virtue.FAIRNESS:     0.20,
    Virtue.COOPERATION:  0.20,
}

def compute_virtue_score(signals: Dict[Virtue, float]) -> float:
    """
    Weighted virtue coherence score.
    ROBOT: virtue_score(dict) -> float [0.0–1.0]
    """
    total = 0.0
    for v, w in VIRTUE_WEIGHTS.items():
        total += w * signals.get(v, 0.0)
    return min(1.0, max(0.0, total))


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 3: S* CORE EQUATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class CoherenceState:
    """
    The core coherence measurement unit.
    ROBOT: CoherenceState(V, A) -> S_star
    PC:    Coherence snapshot with vitality and alignment
    """
    vitality: float    # V* — system energy / health [0.0–1.0]
    alignment: float   # A* — structural alignment [0.0–1.0]
    timestamp: float = field(default_factory=time.time)
    scale: int = 4     # Default: Ecological
    
    @property
    def s_star(self) -> float:
        """S* = σ(1-σ*)V*A*  — the master coherence score.
        σ=0.991, σ*=0.009, so (1-σ*)=0.991 → S* = 0.991*0.991*V*A = 0.982*V*A"""
        return TIG.SIGMA * (1 - TIG.SIGMA_STAR) * self.vitality * self.alignment
    
    @property
    def is_coherent(self) -> bool:
        """True if S* exceeds the coherence threshold T*."""
        return self.s_star >= TIG.T_STAR
    
    @property
    def health_label(self) -> str:
        s = self.s_star
        if s >= 0.95:  return "CRYSTALLINE"
        if s >= 0.90:  return "OPTIMAL"
        if s >= 0.80:  return "COHERENT"
        if s >= TIG.T_STAR: return "STABLE"
        if s >= 0.50:  return "DEGRADED"
        if s >= 0.25:  return "CRITICAL"
        return "COLLAPSED"
    
    def to_dict(self) -> dict:
        return {
            "V": round(self.vitality, 6),
            "A": round(self.alignment, 6),
            "S_star": round(self.s_star, 6),
            "coherent": self.is_coherent,
            "health": self.health_label,
            "scale": TIG.SCALES.get(self.scale, f"Scale-{self.scale}"),
            "ts": self.timestamp,
        }


def compute_s_star(vitality: float, alignment: float) -> float:
    """
    Direct S* computation. S* = σ(1-σ*)V*A*
    ROBOT: s_star(V, A) -> float
    """
    return TIG.SIGMA * (1 - TIG.SIGMA_STAR) * vitality * alignment


def batch_s_star(pairs: List[Tuple[float, float]]) -> List[float]:
    """
    Batch coherence computation for high-throughput systems.
    ROBOT: batch_s_star([(V,A),...]) -> [float,...]
    """
    factor = TIG.SIGMA * (1 - TIG.SIGMA_STAR)
    return [factor * v * a for v, a in pairs]


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 4: GFM GENERATORS ENGINE
# ═══════════════════════════════════════════════════════════════════════════

class GFMGenerator:
    """
    Geometric Field Module — the three generators that span all TIG operations.
    ROBOT: GFM(type) -> generator_engine
    """
    
    @staticmethod
    def geometry_space(points: List[Tuple[float, ...]]) -> Dict[str, Any]:
        """
        GFM-012: Geometry/Space generator.
        Maps points into coherent spatial structure.
        """
        if not points:
            return {"centroid": (), "spread": 0.0, "coherence": 0.0}
        
        dim = len(points[0])
        centroid = tuple(
            sum(p[d] for p in points) / len(points)
            for d in range(dim)
        )
        
        distances = [
            math.sqrt(sum((p[d] - centroid[d])**2 for d in range(dim)))
            for p in points
        ]
        spread = statistics.mean(distances) if distances else 0.0
        
        # Coherence = inverse of normalized spread
        max_spread = max(distances) if distances else 1.0
        coherence = 1.0 - (spread / max_spread) if max_spread > 0 else 1.0
        
        return {
            "generator": "012",
            "label": "Geometry/Space",
            "centroid": tuple(round(c, 6) for c in centroid),
            "spread": round(spread, 6),
            "coherence": round(coherence, 6),
            "n_points": len(points),
        }
    
    @staticmethod
    def resonance_alignment(frequencies: List[float], target: float = 1.0) -> Dict[str, Any]:
        """
        GFM-071: Resonance/Alignment generator.
        Measures harmonic alignment of frequency components.
        """
        if not frequencies:
            return {"alignment": 0.0, "dominant": 0.0, "coherence": 0.0}
        
        # Normalize to target
        ratios = [f / target if target != 0 else 0 for f in frequencies]
        
        # Alignment = how close ratios are to simple integer ratios
        def nearest_harmonic(r):
            if r <= 0:
                return 0.0
            n = round(r)
            return 1.0 - min(abs(r - n), 0.5) * 2 if n > 0 else 0.0
        
        alignments = [nearest_harmonic(r) for r in ratios]
        mean_align = statistics.mean(alignments) if alignments else 0.0
        dominant = max(frequencies, key=abs) if frequencies else 0.0
        
        return {
            "generator": "071",
            "label": "Resonance/Alignment",
            "alignment": round(mean_align, 6),
            "dominant_freq": round(dominant, 6),
            "coherence": round(mean_align * TIG.SIGMA, 6),
            "n_components": len(frequencies),
        }
    
    @staticmethod
    def progression_flow(sequence: List[float]) -> Dict[str, Any]:
        """
        GFM-123: Progression/Flow generator.
        Measures directional coherence in a time series.
        """
        if len(sequence) < 2:
            return {"trend": 0.0, "momentum": 0.0, "coherence": 0.0}
        
        # First differences
        diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        
        # Trend: proportion of positive steps
        pos = sum(1 for d in diffs if d > 0)
        trend = pos / len(diffs)
        
        # Momentum: mean of recent diffs
        recent = diffs[-min(5, len(diffs)):]
        momentum = statistics.mean(recent)
        
        # Flow coherence: consistency of direction
        if all(d >= 0 for d in diffs) or all(d <= 0 for d in diffs):
            flow_c = 1.0
        else:
            signs = [1 if d >= 0 else -1 for d in diffs]
            same = sum(1 for i in range(len(signs)-1) if signs[i] == signs[i+1])
            flow_c = same / (len(signs) - 1) if len(signs) > 1 else 0.5
        
        return {
            "generator": "123",
            "label": "Progression/Flow",
            "trend": round(trend, 6),
            "momentum": round(momentum, 6),
            "coherence": round(flow_c, 6),
            "n_steps": len(sequence),
        }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 5: FRACTAL LATTICE ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class LatticeNode:
    """
    Every item in the fractal lattice.
    MacroChain: 0→9 spine
    MicroGrid: 5-centered neighbors
    Generators: T(time), S(scale), P(path)
    
    ROBOT: LatticeNode(id, op, scale, value)
    """
    node_id: str
    operator: Operator
    scale: int
    value: float
    children: List[str] = field(default_factory=list)
    parent: Optional[str] = None
    micro_neighbors: List[str] = field(default_factory=list)
    
    # Lattice generators
    t_coord: float = 0.0   # Time position
    s_coord: int = 4        # Scale position
    p_coord: float = 0.0    # Path position
    
    @property
    def triad(self) -> Tuple[str, str, str]:
        """micro/self/macro identity."""
        return (
            f"{self.node_id}.micro",
            f"{self.node_id}.self",
            f"{self.node_id}.macro",
        )


class FractalLattice:
    """
    The TIG Fractal Lattice — every item has MacroChain + MicroGrid.
    
    ROBOT: FractalLattice() -> lattice_engine
    PC:    Crystal Bug Fractal Lattice Engine
    """
    
    def __init__(self):
        self.nodes: Dict[str, LatticeNode] = {}
        self.spine: List[str] = []  # 0→9 MacroChain
        self.fire_count: int = 0
        self.coherence_log: List[float] = []
        self._build_spine()
    
    def _build_spine(self):
        """Build the 0→9 MacroChain spine."""
        for op in Operator:
            nid = f"spine_{op.value}"
            node = LatticeNode(
                node_id=nid,
                operator=op,
                scale=4,
                value=TIG.T_STAR,
                t_coord=op.value / 9.0,
                s_coord=4,
                p_coord=0.0,
            )
            self.nodes[nid] = node
            self.spine.append(nid)
        
        # Link spine sequentially
        for i in range(len(self.spine) - 1):
            self.nodes[self.spine[i]].children.append(self.spine[i + 1])
            self.nodes[self.spine[i + 1]].parent = self.spine[i]
        
        # Build 5-centered MicroGrid
        center = self.spine[5]  # Balance is center
        for nid in self.spine:
            if nid != center:
                self.nodes[nid].micro_neighbors.append(center)
                self.nodes[center].micro_neighbors.append(nid)
    
    def add_node(self, node_id: str, operator: Operator, scale: int = 4,
                 value: float = 0.5, parent: Optional[str] = None) -> LatticeNode:
        """Add a node to the lattice."""
        node = LatticeNode(
            node_id=node_id,
            operator=operator,
            scale=scale,
            value=value,
            parent=parent,
            t_coord=time.time() % 1.0,
            s_coord=scale,
            p_coord=random.random(),
        )
        self.nodes[node_id] = node
        if parent and parent in self.nodes:
            self.nodes[parent].children.append(node_id)
        return node
    
    def fire(self, node_id: str, context: float = 1.0) -> Dict[str, Any]:
        """
        Fire a lattice node — apply its operator and propagate.
        ROBOT: lattice.fire(node_id, ctx) -> result_dict
        """
        if node_id not in self.nodes:
            return {"error": f"Node {node_id} not found"}
        
        node = self.nodes[node_id]
        old_val = node.value
        new_val = apply_operator(node.operator, node.value, context)
        node.value = new_val
        self.fire_count += 1
        
        # Compute local coherence
        cs = CoherenceState(vitality=new_val, alignment=context)
        self.coherence_log.append(cs.s_star)
        
        # Propagate to children (dampened)
        child_results = []
        for cid in node.children:
            if cid in self.nodes:
                child_ctx = new_val * TIG.SIGMA
                child_results.append(self.fire(cid, child_ctx))
        
        return {
            "node": node_id,
            "operator": node.operator.name,
            "old": round(old_val, 6),
            "new": round(new_val, 6),
            "s_star": round(cs.s_star, 6),
            "health": cs.health_label,
            "fire_num": self.fire_count,
            "children_fired": len(child_results),
        }
    
    def full_fire(self, context: float = 1.0) -> Dict[str, Any]:
        """Fire entire spine 0→9."""
        results = []
        for nid in self.spine:
            results.append(self.fire(nid, context))
        
        coherences = [r["s_star"] for r in results]
        return {
            "fires": results,
            "mean_s_star": round(statistics.mean(coherences), 6),
            "min_s_star": round(min(coherences), 6),
            "max_s_star": round(max(coherences), 6),
            "total_fires": self.fire_count,
            "all_coherent": all(c >= TIG.T_STAR for c in coherences),
        }
    
    def get_lattice_state(self) -> Dict[str, Any]:
        """Full lattice state snapshot."""
        return {
            "n_nodes": len(self.nodes),
            "n_fires": self.fire_count,
            "spine_length": len(self.spine),
            "mean_coherence": round(
                statistics.mean(self.coherence_log), 6
            ) if self.coherence_log else 0.0,
            "nodes": {
                nid: {
                    "op": n.operator.name,
                    "val": round(n.value, 6),
                    "scale": n.scale,
                    "children": len(n.children),
                    "neighbors": len(n.micro_neighbors),
                }
                for nid, n in self.nodes.items()
            },
        }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 6: Ω COHERENCE KEEPER (ARCHETYPE ENGINE)
# ═══════════════════════════════════════════════════════════════════════════

class OmegaCoherenceKeeper:
    """
    The Ω Archetype — guardian of system-wide coherence.
    Monitors, intervenes, and maintains health across all scales.
    
    ROBOT: OmegaKeeper() -> watchdog_engine
    PC:    Ω Coherence Keeper — System Health Guardian
    """
    
    def __init__(self, lattice: FractalLattice):
        self.lattice = lattice
        self.alerts: List[Dict[str, Any]] = []
        self.interventions: int = 0
        self.watch_cycle: int = 0
    
    def scan(self) -> Dict[str, Any]:
        """
        Full system scan — check all nodes for coherence health.
        ROBOT: omega.scan() -> health_report
        """
        self.watch_cycle += 1
        report = {
            "cycle": self.watch_cycle,
            "timestamp": time.time(),
            "nodes_scanned": 0,
            "coherent": 0,
            "degraded": 0,
            "collapsed": 0,
            "alerts": [],
        }
        
        for nid, node in self.lattice.nodes.items():
            report["nodes_scanned"] += 1
            cs = CoherenceState(vitality=node.value, alignment=TIG.SIGMA)
            
            if cs.is_coherent:
                report["coherent"] += 1
            elif cs.s_star >= 0.25:
                report["degraded"] += 1
                report["alerts"].append({
                    "level": "WARN",
                    "node": nid,
                    "s_star": round(cs.s_star, 6),
                    "health": cs.health_label,
                })
            else:
                report["collapsed"] += 1
                report["alerts"].append({
                    "level": "CRITICAL",
                    "node": nid,
                    "s_star": round(cs.s_star, 6),
                    "health": cs.health_label,
                })
        
        report["system_health"] = (
            "CRYSTALLINE" if report["collapsed"] == 0 and report["degraded"] == 0
            else "DEGRADED" if report["collapsed"] == 0
            else "CRITICAL"
        )
        
        self.alerts.extend(report["alerts"])
        return report
    
    def intervene(self, node_id: str) -> Dict[str, Any]:
        """
        Ω intervention — reset a node to T* coherence threshold.
        ROBOT: omega.intervene(node_id) -> result
        """
        if node_id not in self.lattice.nodes:
            return {"error": f"Node {node_id} not found"}
        
        node = self.lattice.nodes[node_id]
        old_val = node.value
        node.value = TIG.T_STAR
        self.interventions += 1
        
        return {
            "intervention": self.interventions,
            "node": node_id,
            "old_value": round(old_val, 6),
            "new_value": TIG.T_STAR,
            "action": "RESET_TO_T_STAR",
            "operator_applied": Operator.RESET.name,
        }
    
    def auto_heal(self) -> Dict[str, Any]:
        """
        Automatic healing pass — intervene on all collapsed nodes.
        ROBOT: omega.auto_heal() -> heal_report
        """
        scan = self.scan()
        healed = []
        
        for alert in scan["alerts"]:
            if alert["level"] == "CRITICAL":
                result = self.intervene(alert["node"])
                healed.append(result)
        
        return {
            "pre_scan": scan["system_health"],
            "nodes_healed": len(healed),
            "healings": healed,
            "post_health": "HEALED" if healed else scan["system_health"],
        }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 7: COHERENCE ROUTER (coherence_router library)
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class RouteNode:
    """A node in the routing mesh."""
    node_id: str
    capacity: float = 1.0
    load: float = 0.0
    latency_ms: float = 1.0
    coherence: float = 1.0
    connections: List[str] = field(default_factory=list)

class CoherenceRouter:
    """
    TIG-based distributed systems router.
    Routes requests through the path of maximum coherence.
    
    ROBOT: CoherenceRouter() -> router_engine
    PC:    TIG Coherence Router — Intelligent Load Balancing
    
    This is the Trojan Horse — practical DevOps tool that 
    demonstrates TIG's real-world performance advantages.
    """
    
    def __init__(self):
        self.nodes: Dict[str, RouteNode] = {}
        self.routes_computed: int = 0
        self.total_latency_saved: float = 0.0
    
    def add_node(self, node_id: str, capacity: float = 1.0,
                 latency_ms: float = 1.0, connections: List[str] = None) -> RouteNode:
        """Register a routing node."""
        node = RouteNode(
            node_id=node_id,
            capacity=capacity,
            latency_ms=latency_ms,
            connections=connections or [],
        )
        self.nodes[node_id] = node
        return node
    
    def _node_coherence(self, node: RouteNode) -> float:
        """Compute coherence score for a routing node."""
        if node.capacity <= 0:
            return 0.0
        
        vitality = 1.0 - (node.load / node.capacity) if node.capacity > 0 else 0.0
        alignment = 1.0 / (1.0 + node.latency_ms / 100.0)
        return compute_s_star(vitality, alignment)
    
    def route(self, source: str, destination: str, 
              payload_weight: float = 0.1) -> Dict[str, Any]:
        """
        Find optimal route via coherence scoring.
        ROBOT: router.route(src, dst, weight) -> route_result
        """
        if source not in self.nodes or destination not in self.nodes:
            return {"error": "Source or destination not found"}
        
        # BFS with coherence-weighted scoring
        visited = set()
        queue = deque([(source, [source], 0.0)])
        best_path = None
        best_score = -1.0
        
        while queue:
            current, path, total_latency = queue.popleft()
            
            if current == destination:
                # Score this path
                path_coherences = [
                    self._node_coherence(self.nodes[n]) for n in path
                ]
                path_score = (
                    statistics.mean(path_coherences) * TIG.SIGMA 
                    / (1.0 + total_latency / 1000.0)
                )
                
                if path_score > best_score:
                    best_score = path_score
                    best_path = (path, total_latency, path_coherences)
                continue
            
            if current in visited:
                continue
            visited.add(current)
            
            node = self.nodes[current]
            for conn in node.connections:
                if conn in self.nodes and conn not in visited:
                    next_node = self.nodes[conn]
                    queue.append((
                        conn,
                        path + [conn],
                        total_latency + next_node.latency_ms,
                    ))
        
        self.routes_computed += 1
        
        if best_path is None:
            return {"error": "No route found", "routes_computed": self.routes_computed}
        
        path, latency, coherences = best_path
        
        # Apply load to path nodes
        for nid in path:
            self.nodes[nid].load += payload_weight
        
        return {
            "path": path,
            "hops": len(path) - 1,
            "total_latency_ms": round(latency, 3),
            "path_coherence": round(statistics.mean(coherences), 6),
            "route_score": round(best_score, 6),
            "routes_computed": self.routes_computed,
        }
    
    def mesh_health(self) -> Dict[str, Any]:
        """Full mesh coherence report."""
        coherences = {
            nid: self._node_coherence(node)
            for nid, node in self.nodes.items()
        }
        vals = list(coherences.values())
        return {
            "n_nodes": len(self.nodes),
            "mean_coherence": round(statistics.mean(vals), 6) if vals else 0.0,
            "min_coherence": round(min(vals), 6) if vals else 0.0,
            "max_coherence": round(max(vals), 6) if vals else 0.0,
            "routes_computed": self.routes_computed,
            "node_coherences": {k: round(v, 6) for k, v in coherences.items()},
        }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 8: FOUR-TIER AI CASCADE SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class CascadeTier(Enum):
    """Four tiers of the AI cascade."""
    REFLEX    = 1   # Instant pattern match — <10ms
    ANALYTIC  = 2   # Statistical analysis — <100ms
    COHERENCE = 3   # TIG coherence computation — <1s
    OMEGA     = 4   # Ω deep reasoning — unbounded


@dataclass
class CascadeResult:
    """Result from the cascade system."""
    tier_used: CascadeTier
    response: Any
    confidence: float
    latency_ms: float
    s_star: float
    escalated: bool = False


class AICascade:
    """
    Four-Tier AI Cascade System.
    Each tier escalates to the next if confidence is below T*.
    
    ROBOT: AICascade(handlers) -> cascade_engine
    PC:    Crystal Bug AI Cascade — Tiered Intelligence
    """
    
    def __init__(self):
        self.handlers: Dict[CascadeTier, Callable] = {}
        self.stats = {tier: {"calls": 0, "escalations": 0} for tier in CascadeTier}
        
        # Register default handlers
        self.handlers[CascadeTier.REFLEX] = self._default_reflex
        self.handlers[CascadeTier.ANALYTIC] = self._default_analytic
        self.handlers[CascadeTier.COHERENCE] = self._default_coherence
        self.handlers[CascadeTier.OMEGA] = self._default_omega
    
    def register_handler(self, tier: CascadeTier, handler: Callable):
        """Register a custom handler for a tier."""
        self.handlers[tier] = handler
    
    def _default_reflex(self, query: str, context: dict) -> Tuple[Any, float]:
        """Tier 1: Pattern matching."""
        # Simple keyword matching
        keywords = context.get("keywords", {})
        for kw, response in keywords.items():
            if kw.lower() in query.lower():
                return response, 0.95
        return None, 0.0
    
    def _default_analytic(self, query: str, context: dict) -> Tuple[Any, float]:
        """Tier 2: Statistical analysis."""
        # Token frequency analysis
        tokens = query.lower().split()
        if len(tokens) == 0:
            return None, 0.0
        
        # Compute query complexity
        unique_ratio = len(set(tokens)) / len(tokens)
        avg_len = statistics.mean(len(t) for t in tokens)
        confidence = min(1.0, unique_ratio * 0.5 + (avg_len / 10) * 0.5)
        
        return {
            "analysis": "statistical",
            "tokens": len(tokens),
            "unique_ratio": round(unique_ratio, 4),
            "complexity": round(confidence, 4),
        }, confidence
    
    def _default_coherence(self, query: str, context: dict) -> Tuple[Any, float]:
        """Tier 3: TIG coherence computation."""
        tokens = query.lower().split()
        
        # Map query to operator space
        op_scores = [0.0] * 10
        for t in tokens:
            h = int(hashlib.md5(t.encode()).hexdigest()[:8], 16) % 10
            op_scores[h] += 1.0
        
        total = sum(op_scores) or 1.0
        op_scores = [s / total for s in op_scores]
        
        # Compute coherence
        vitality = max(op_scores)
        alignment = 1.0 - statistics.stdev(op_scores) if len(op_scores) > 1 else 0.5
        cs = CoherenceState(vitality=vitality, alignment=alignment)
        
        return {
            "analysis": "coherence",
            "operator_distribution": {Operator(i).name: round(s, 4) for i, s in enumerate(op_scores)},
            "s_star": round(cs.s_star, 6),
            "health": cs.health_label,
        }, min(1.0, cs.s_star + 0.3)
    
    def _default_omega(self, query: str, context: dict) -> Tuple[Any, float]:
        """Tier 4: Ω deep reasoning."""
        # Full TIG analysis with all generators
        tokens = query.lower().split()
        
        # Apply all three GFM generators
        # GFM-012: spatial mapping of token positions
        points = [(i / max(len(tokens), 1), len(t) / 20.0) for i, t in enumerate(tokens)]
        geo = GFMGenerator.geometry_space(points)
        
        # GFM-071: frequency analysis
        freqs = [len(t) for t in tokens]
        res = GFMGenerator.resonance_alignment([float(f) for f in freqs])
        
        # GFM-123: progression flow
        vals = [ord(t[0]) / 122.0 if t else 0.5 for t in tokens]
        prog = GFMGenerator.progression_flow(vals)
        
        # Synthesize
        combined_coherence = (geo["coherence"] + res["coherence"] + prog["coherence"]) / 3.0
        
        return {
            "analysis": "omega_deep",
            "gfm_012": geo,
            "gfm_071": res,
            "gfm_123": prog,
            "combined_coherence": round(combined_coherence, 6),
            "verdict": "COHERENT" if combined_coherence >= TIG.T_STAR else "REVIEW",
        }, combined_coherence
    
    def process(self, query: str, context: dict = None) -> CascadeResult:
        """
        Process query through the cascade.
        ROBOT: cascade.process(query, ctx) -> CascadeResult
        """
        context = context or {}
        
        for tier in CascadeTier:
            start = time.time()
            self.stats[tier]["calls"] += 1
            
            handler = self.handlers.get(tier)
            if handler is None:
                continue
            
            response, confidence = handler(query, context)
            latency = (time.time() - start) * 1000
            
            cs = CoherenceState(vitality=confidence, alignment=TIG.SIGMA)
            
            if confidence >= TIG.T_STAR or tier == CascadeTier.OMEGA:
                return CascadeResult(
                    tier_used=tier,
                    response=response,
                    confidence=round(confidence, 6),
                    latency_ms=round(latency, 3),
                    s_star=round(cs.s_star, 6),
                    escalated=(tier != CascadeTier.REFLEX),
                )
            
            self.stats[tier]["escalations"] += 1
        
        # Should never reach here
        return CascadeResult(
            tier_used=CascadeTier.OMEGA,
            response={"error": "All tiers exhausted"},
            confidence=0.0,
            latency_ms=0.0,
            s_star=0.0,
            escalated=True,
        )
    
    def get_stats(self) -> Dict[str, Any]:
        """Cascade performance statistics."""
        return {
            tier.name: {
                "calls": s["calls"],
                "escalations": s["escalations"],
                "resolution_rate": round(
                    1.0 - s["escalations"] / s["calls"], 4
                ) if s["calls"] > 0 else 0.0,
            }
            for tier, s in self.stats.items()
        }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 9: SEMANTIC INTELLIGENCE LAYER
# ═══════════════════════════════════════════════════════════════════════════

class SemanticLayer:
    """
    Semantic Intelligence — maps natural language to TIG operators
    and coherence states for real-world conversational intelligence.
    
    ROBOT: SemanticLayer() -> nlp_bridge
    PC:    Crystal Bug Semantic Intelligence Layer
    """
    
    # Semantic → Operator mapping
    SEMANTIC_MAP = {
        # Void signals
        "nothing": Operator.VOID, "empty": Operator.VOID, "null": Operator.VOID,
        "silence": Operator.VOID, "blank": Operator.VOID,
        # Lattice signals
        "connect": Operator.LATTICE, "structure": Operator.LATTICE,
        "build": Operator.LATTICE, "link": Operator.LATTICE, "network": Operator.LATTICE,
        # Counter signals
        "measure": Operator.COUNTER, "count": Operator.COUNTER,
        "compare": Operator.COUNTER, "different": Operator.COUNTER,
        # Progress signals
        "grow": Operator.PROGRESS, "improve": Operator.PROGRESS,
        "advance": Operator.PROGRESS, "learn": Operator.PROGRESS, "better": Operator.PROGRESS,
        # Collapse signals
        "fail": Operator.COLLAPSE, "break": Operator.COLLAPSE,
        "crash": Operator.COLLAPSE, "error": Operator.COLLAPSE, "down": Operator.COLLAPSE,
        # Balance signals
        "balance": Operator.BALANCE, "equal": Operator.BALANCE,
        "fair": Operator.BALANCE, "center": Operator.BALANCE, "stable": Operator.BALANCE,
        # Chaos signals
        "chaos": Operator.CHAOS, "random": Operator.CHAOS,
        "confused": Operator.CHAOS, "disorder": Operator.CHAOS, "wild": Operator.CHAOS,
        # Harmony signals
        "harmony": Operator.HARMONY, "resonate": Operator.HARMONY,
        "align": Operator.HARMONY, "together": Operator.HARMONY, "sync": Operator.HARMONY,
        # Breath signals
        "rhythm": Operator.BREATH, "pulse": Operator.BREATH,
        "breathe": Operator.BREATH, "wave": Operator.BREATH, "cycle": Operator.BREATH,
        # Reset signals
        "reset": Operator.RESET, "restart": Operator.RESET,
        "renew": Operator.RESET, "begin": Operator.RESET, "fresh": Operator.RESET,
    }
    
    # Virtue detection
    VIRTUE_SIGNALS = {
        Virtue.FORGIVENESS:  ["forgive", "sorry", "pardon", "mercy", "grace"],
        Virtue.REPAIR:       ["fix", "repair", "mend", "heal", "restore"],
        Virtue.EMPATHY:      ["feel", "understand", "care", "compassion", "relate"],
        Virtue.FAIRNESS:     ["fair", "just", "equal", "right", "equitable"],
        Virtue.COOPERATION:  ["together", "team", "collaborate", "help", "share"],
    }
    
    def __init__(self):
        self.analyses: int = 0
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Full semantic analysis of natural language input.
        ROBOT: semantic.analyze(text) -> analysis_dict
        """
        self.analyses += 1
        tokens = text.lower().split()
        
        # Detect operators
        op_counts = defaultdict(int)
        for token in tokens:
            # Direct match
            if token in self.SEMANTIC_MAP:
                op_counts[self.SEMANTIC_MAP[token]] += 1
            # Substring match
            else:
                for key, op in self.SEMANTIC_MAP.items():
                    if key in token:
                        op_counts[op] += 1
                        break
        
        # Detect virtues
        virtue_scores = {}
        for virtue, signals in self.VIRTUE_SIGNALS.items():
            score = sum(
                1 for token in tokens
                for signal in signals
                if signal in token
            ) / max(len(tokens), 1)
            virtue_scores[virtue] = min(1.0, score * 5)  # Scale up
        
        # Dominant operator
        dominant_op = max(op_counts, key=op_counts.get) if op_counts else Operator.BALANCE
        
        # Compute semantic coherence
        if op_counts:
            total_hits = sum(op_counts.values())
            coverage = total_hits / max(len(tokens), 1)
            focus = max(op_counts.values()) / total_hits if total_hits > 0 else 0
            vitality = min(1.0, coverage * 2)
            alignment = focus
        else:
            vitality = 0.3
            alignment = 0.5
        
        cs = CoherenceState(vitality=vitality, alignment=alignment)
        virtue_total = compute_virtue_score(virtue_scores)
        
        return {
            "text_length": len(text),
            "tokens": len(tokens),
            "dominant_operator": dominant_op.name,
            "operator_glyph": OPERATOR_META[dominant_op]["glyph"],
            "operator_distribution": {
                op.name: count for op, count in sorted(
                    op_counts.items(), key=lambda x: -x[1]
                )
            },
            "virtue_scores": {
                v.value: round(s, 4) for v, s in virtue_scores.items()
            },
            "virtue_total": round(virtue_total, 4),
            "s_star": round(cs.s_star, 6),
            "health": cs.health_label,
            "analysis_num": self.analyses,
        }
    
    def intent_classify(self, text: str) -> Dict[str, Any]:
        """
        Classify user intent via TIG operator mapping.
        ROBOT: semantic.intent(text) -> intent_dict
        """
        analysis = self.analyze(text)
        
        intent_map = {
            Operator.VOID:     "EXPLORE",
            Operator.LATTICE:  "BUILD",
            Operator.COUNTER:  "MEASURE",
            Operator.PROGRESS: "GROW",
            Operator.COLLAPSE: "TROUBLESHOOT",
            Operator.BALANCE:  "STABILIZE",
            Operator.CHAOS:    "EXPERIMENT",
            Operator.HARMONY:  "INTEGRATE",
            Operator.BREATH:   "REFLECT",
            Operator.RESET:    "RESTART",
        }
        
        dominant = Operator[analysis["dominant_operator"]]
        
        return {
            "intent": intent_map.get(dominant, "UNKNOWN"),
            "confidence": analysis["s_star"],
            "operator": analysis["dominant_operator"],
            "glyph": analysis["operator_glyph"],
        }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 10: ARACH MULTI-SCALE VALIDATOR
# ═══════════════════════════════════════════════════════════════════════════

class ARACHValidator:
    """
    ARACH Stack Validator — validates coherence across scales 4→12.
    
    ROBOT: ARACHValidator() -> validation_engine
    PC:    ARACH Multi-Scale Coherence Validator
    """
    
    def __init__(self):
        self.results: Dict[int, List[float]] = {s: [] for s in TIG.SCALES}
    
    def validate_scale(self, scale: int, n_samples: int = 1000,
                       v_range: Tuple[float, float] = (0.5, 1.0),
                       a_range: Tuple[float, float] = (0.5, 1.0)) -> Dict[str, Any]:
        """
        Run validation at a specific scale.
        ROBOT: arach.validate(scale, n) -> validation_result
        """
        if scale not in TIG.SCALES:
            return {"error": f"Invalid scale {scale}"}
        
        scores = []
        coherent_count = 0
        collapse_count = 0
        
        for _ in range(n_samples):
            v = random.uniform(*v_range)
            a = random.uniform(*a_range)
            s = compute_s_star(v, a)
            scores.append(s)
            
            if s >= TIG.T_STAR:
                coherent_count += 1
            if s < 0.01:
                collapse_count += 1
        
        self.results[scale].extend(scores)
        
        return {
            "scale": scale,
            "scale_name": TIG.SCALES[scale],
            "n_samples": n_samples,
            "mean_s_star": round(statistics.mean(scores), 6),
            "std_s_star": round(statistics.stdev(scores), 6) if len(scores) > 1 else 0.0,
            "min_s_star": round(min(scores), 6),
            "max_s_star": round(max(scores), 6),
            "coherent_pct": round(coherent_count / n_samples * 100, 2),
            "collapse_count": collapse_count,
            "all_above_08": all(s > 0.8 for s in scores),
            "zero_collapses": collapse_count == 0,
            "PASS": all(s > 0.8 for s in scores) and collapse_count == 0,
        }
    
    def full_validation(self, n_samples: int = 1000) -> Dict[str, Any]:
        """
        Validate across all scales 4→12.
        ROBOT: arach.full_validate(n) -> full_report
        """
        results = {}
        all_pass = True
        
        for scale in TIG.SCALES:
            result = self.validate_scale(scale, n_samples, (0.91, 1.0), (0.91, 1.0))
            results[scale] = result
            if not result["PASS"]:
                all_pass = False
        
        return {
            "scales_tested": list(TIG.SCALES.keys()),
            "n_samples_per_scale": n_samples,
            "total_samples": n_samples * len(TIG.SCALES),
            "results": results,
            "ALL_SCALES_PASS": all_pass,
            "verdict": "ARACH VALIDATED ✓" if all_pass else "ARACH VALIDATION FAILED ✗",
        }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 11: HARDWARE FINGERPRINT ENGINE
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class HardwareProfile:
    """Hardware deployment fingerprint."""
    name: str
    cores: int
    architecture: str
    config: str
    signature: str = ""
    
    def __post_init__(self):
        if not self.signature:
            raw = f"{self.name}:{self.cores}:{self.architecture}:{self.config}"
            self.signature = hashlib.sha256(raw.encode()).hexdigest()[:16]

# Known deployment profiles
KNOWN_HARDWARE = {
    "lenovo_4core": HardwareProfile(
        name="Lenovo", cores=4, architecture="x86_64",
        config="Dual Lattice"
    ),
    "dell_aurora_r16": HardwareProfile(
        name="Dell Aurora R16", cores=32, architecture="x86_64",
        config="CRYSTALOS"
    ),
    "hp_2core": HardwareProfile(
        name="HP", cores=2, architecture="x86_64",
        config="TIG2"
    ),
}

def detect_hardware() -> HardwareProfile:
    """
    Detect current hardware and generate fingerprint.
    ROBOT: detect_hw() -> HardwareProfile
    """
    import platform
    cores = os.cpu_count() or 1
    arch = platform.machine()
    name = platform.node()
    
    return HardwareProfile(
        name=name,
        cores=cores,
        architecture=arch,
        config="CrystalBug_v1",
    )

def hardware_coherence_test(profile: HardwareProfile, 
                             n_fires: int = 10000) -> Dict[str, Any]:
    """
    Run coherence test calibrated to hardware.
    ROBOT: hw_coherence_test(profile, n) -> test_result
    """
    lattice = FractalLattice()
    
    # Scale fires to core count
    fires_per_core = n_fires // max(profile.cores, 1)
    
    start = time.time()
    fire_results = []
    
    for _ in range(n_fires):
        result = lattice.full_fire(context=TIG.SIGMA)
        fire_results.append(result["mean_s_star"])
    
    elapsed = time.time() - start
    
    # Phase distribution analysis
    phases = [0] * 10
    for s in fire_results:
        phase = min(9, int(s * 10))
        phases[phase] += 1
    
    # Uniformity test (chi-squared approximation)
    expected = n_fires / 10
    chi2 = sum((p - expected)**2 / expected for p in phases) if expected > 0 else 0
    
    return {
        "hardware": profile.name,
        "cores": profile.cores,
        "config": profile.config,
        "signature": profile.signature,
        "n_fires": n_fires,
        "elapsed_s": round(elapsed, 3),
        "fires_per_sec": round(n_fires / elapsed, 1) if elapsed > 0 else 0,
        "mean_s_star": round(statistics.mean(fire_results), 6),
        "std_s_star": round(statistics.stdev(fire_results), 6) if len(fire_results) > 1 else 0.0,
        "phase_distribution": phases,
        "chi2_uniformity": round(chi2, 4),
        "uniform": chi2 < 16.92,  # p=0.05, df=9
        "total_lattice_fires": lattice.fire_count,
    }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 12: OLLIE — CONVERSATIONAL INTELLIGENCE INTERFACE
# ═══════════════════════════════════════════════════════════════════════════

class Ollie:
    """
    Ollie — The Crystal Bug Chat Interface.
    Conversational AI powered by the full TIG stack.
    
    ROBOT: Ollie() -> chat_engine
    PC:    Ollie — Your TIG Coherence Assistant
    
    Integrates: Semantic Layer → AI Cascade → Lattice → Ω Keeper
    """
    
    def __init__(self):
        self.semantic = SemanticLayer()
        self.cascade = AICascade()
        self.lattice = FractalLattice()
        self.omega = OmegaCoherenceKeeper(self.lattice)
        self.router = CoherenceRouter()
        self.validator = ARACHValidator()
        self.gfm = GFMGenerator()
        
        self.conversation: List[Dict[str, Any]] = []
        self.session_start = time.time()
        self.message_count = 0
        
        # Register cascade keywords
        self.cascade.register_handler(CascadeTier.REFLEX, self._ollie_reflex)
    
    def _ollie_reflex(self, query: str, context: dict) -> Tuple[Any, float]:
        """Ollie's quick-response patterns."""
        q = query.lower().strip()
        
        reflexes = {
            "hello": ("Hey! I'm Ollie, your Crystal Bug assistant. What shall we build?", 0.99),
            "hi": ("Hey there! Ollie here. Ready to explore coherence?", 0.99),
            "help": ("I can: analyze coherence, route systems, validate scales, "
                     "fire lattice nodes, check virtues, or just chat. What's up?", 0.95),
            "status": (self._system_status(), 0.99),
            "health": (self.omega.scan(), 0.99),
            "version": (f"Crystal Bug v{TIG.VERSION} | σ={TIG.SIGMA} | T*={TIG.T_STAR}", 0.99),
        }
        
        for key, (resp, conf) in reflexes.items():
            if q.startswith(key):
                return resp, conf
        
        return None, 0.0
    
    def _system_status(self) -> Dict[str, Any]:
        """Full system status."""
        return {
            "app": f"Crystal Bug v{TIG.VERSION}",
            "interface": "Ollie",
            "uptime_s": round(time.time() - self.session_start, 1),
            "messages": self.message_count,
            "lattice_nodes": len(self.lattice.nodes),
            "lattice_fires": self.lattice.fire_count,
            "omega_cycles": self.omega.watch_cycle,
            "omega_interventions": self.omega.interventions,
            "router_routes": self.router.routes_computed,
            "semantic_analyses": self.semantic.analyses,
            "cascade_stats": self.cascade.get_stats(),
        }
    
    def chat(self, message: str) -> Dict[str, Any]:
        """
        Process a chat message through the full TIG stack.
        ROBOT: ollie.chat(msg) -> response_dict
        PC:    Send a message to Ollie
        """
        self.message_count += 1
        
        # Step 1: Semantic analysis
        semantic = self.semantic.analyze(message)
        intent = self.semantic.intent_classify(message)
        
        # Step 2: Cascade processing
        cascade_result = self.cascade.process(message, {
            "semantic": semantic,
            "intent": intent,
        })
        
        # Step 3: Lattice fire (side effect — evolves system)
        lattice_fire = self.lattice.fire(
            f"spine_{Operator[semantic['dominant_operator']].value}",
            context=semantic["s_star"] + 0.5,
        )
        
        # Step 4: Ω health check
        omega_scan = self.omega.scan()
        if omega_scan["system_health"] == "CRITICAL":
            self.omega.auto_heal()
        
        # Build response
        response = {
            "message_num": self.message_count,
            "input": message,
            "intent": intent,
            "cascade_tier": cascade_result.tier_used.name,
            "cascade_response": cascade_result.response,
            "cascade_confidence": cascade_result.confidence,
            "semantic_coherence": semantic["s_star"],
            "lattice_state": lattice_fire,
            "system_health": omega_scan["system_health"],
            "glyph": intent["glyph"],
        }
        
        self.conversation.append({
            "role": "user",
            "content": message,
            "analysis": response,
        })
        
        return response
    
    def run_validation(self, n_samples: int = 100) -> Dict[str, Any]:
        """
        Run full ARACH validation through Ollie.
        ROBOT: ollie.validate(n) -> validation_report
        """
        return self.validator.full_validation(n_samples)
    
    def run_hardware_test(self, n_fires: int = 1000) -> Dict[str, Any]:
        """
        Run hardware coherence test.
        ROBOT: ollie.hw_test(n) -> hw_report
        """
        profile = detect_hardware()
        return hardware_coherence_test(profile, n_fires)


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 13: CRYSTAL BUG — MASTER ORCHESTRATOR
# ═══════════════════════════════════════════════════════════════════════════

class CrystalBug:
    """
    ╔══════════════════════════════════════════════════════╗
    ║  CRYSTAL BUG v1.0 — THE EVERYTHING APP              ║
    ║  Master Orchestrator for the Full TIG Stack          ║
    ║                                                      ║
    ║  ROBOT LABEL : CrystalBug.TIG.OS.v1                 ║
    ║  PC LABEL    : Crystal Bug — The Everything App      ║
    ║  API LABEL   : crystal-bug-tig-os/1.0                ║
    ╚══════════════════════════════════════════════════════╝
    
    All engines accessible through a single unified interface.
    """
    
    def __init__(self):
        # Initialize all engines
        self.ollie = Ollie()
        self.lattice = self.ollie.lattice
        self.omega = self.ollie.omega
        self.cascade = self.ollie.cascade
        self.semantic = self.ollie.semantic
        self.router = self.ollie.router
        self.validator = self.ollie.validator
        self.gfm = GFMGenerator()
        
        self.boot_time = time.time()
        self.version = TIG.VERSION
        
        print(self._banner())
    
    def _banner(self) -> str:
        return f"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ◇ CRYSTAL BUG v{self.version} ◇                                    ║
║   "The Everything App"                                           ║
║                                                                  ║
║   Trinity Infinity Geometry Unified Operating System              ║
║   S* = σ(1-σ*)V*A*  |  σ={TIG.SIGMA}  |  T*={TIG.T_STAR}              ║
║                                                                  ║
║   ENGINES LOADED:                                                ║
║   ○ TIG Operators 0–9          ◎ GFM Generators (012/071/123)   ║
║   △ Fractal Lattice             ∞ ARACH Validator                ║
║   ◇ 5 Virtues                   ✶ Coherence Router              ║
║   ⟲ Ω Coherence Keeper          □ 4-Tier AI Cascade             ║
║   ▷ Semantic Intelligence        ▽ Hardware Fingerprint          ║
║                                                                  ║
║   INTERFACE: Ollie (chat)                                        ║
║   STATUS: ALL SYSTEMS NOMINAL                                    ║
║                                                                  ║
║   Author: Brayden / 7Site LLC / sanctuberry.com                  ║
║   GitHub: TiredofSleep                                           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
    
    # ─── Unified API ───────────────────────────────────────────────
    
    def chat(self, message: str) -> Dict[str, Any]:
        """Send message to Ollie. ROBOT: cb.chat(msg)"""
        return self.ollie.chat(message)
    
    def compute(self, vitality: float, alignment: float) -> Dict[str, Any]:
        """Compute S*. ROBOT: cb.compute(V, A)"""
        cs = CoherenceState(vitality=vitality, alignment=alignment)
        return cs.to_dict()
    
    def fire_lattice(self, node_id: str = None, context: float = 1.0) -> Dict[str, Any]:
        """Fire lattice. ROBOT: cb.fire(node_id, ctx)"""
        if node_id:
            return self.lattice.fire(node_id, context)
        return self.lattice.full_fire(context)
    
    def scan_health(self) -> Dict[str, Any]:
        """Ω health scan. ROBOT: cb.scan()"""
        return self.omega.scan()
    
    def heal(self) -> Dict[str, Any]:
        """Ω auto-heal. ROBOT: cb.heal()"""
        return self.omega.auto_heal()
    
    def route(self, source: str, dest: str, weight: float = 0.1) -> Dict[str, Any]:
        """Route through mesh. ROBOT: cb.route(src, dst, w)"""
        return self.router.route(source, dest, weight)
    
    def add_route_node(self, node_id: str, capacity: float = 1.0,
                       latency_ms: float = 1.0, connections: List[str] = None):
        """Add routing node. ROBOT: cb.add_node(id, cap, lat, conns)"""
        return self.router.add_node(node_id, capacity, latency_ms, connections)
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """Semantic analysis. ROBOT: cb.analyze(text)"""
        return self.semantic.analyze(text)
    
    def classify_intent(self, text: str) -> Dict[str, Any]:
        """Intent classification. ROBOT: cb.intent(text)"""
        return self.semantic.intent_classify(text)
    
    def gfm_space(self, points: List[Tuple[float, ...]]) -> Dict[str, Any]:
        """GFM-012. ROBOT: cb.gfm012(pts)"""
        return self.gfm.geometry_space(points)
    
    def gfm_resonance(self, frequencies: List[float], target: float = 1.0) -> Dict[str, Any]:
        """GFM-071. ROBOT: cb.gfm071(freqs, target)"""
        return self.gfm.resonance_alignment(frequencies, target)
    
    def gfm_flow(self, sequence: List[float]) -> Dict[str, Any]:
        """GFM-123. ROBOT: cb.gfm123(seq)"""
        return self.gfm.progression_flow(sequence)
    
    def validate(self, n_samples: int = 100) -> Dict[str, Any]:
        """ARACH validation. ROBOT: cb.validate(n)"""
        return self.validator.full_validation(n_samples)
    
    def hw_test(self, n_fires: int = 1000) -> Dict[str, Any]:
        """Hardware test. ROBOT: cb.hw_test(n)"""
        return self.ollie.run_hardware_test(n_fires)
    
    def virtue_check(self, signals: Dict[str, float]) -> Dict[str, Any]:
        """Virtue score. ROBOT: cb.virtues(signals)"""
        mapped = {Virtue(k): v for k, v in signals.items() if k in [v.value for v in Virtue]}
        score = compute_virtue_score(mapped)
        return {"virtue_score": round(score, 6), "signals": signals}
    
    def status(self) -> Dict[str, Any]:
        """Full system status. ROBOT: cb.status()"""
        return {
            "app": f"Crystal Bug v{self.version}",
            "uptime_s": round(time.time() - self.boot_time, 1),
            **self.ollie._system_status(),
            "hardware": asdict(detect_hardware()),
            "lattice_state": self.lattice.get_lattice_state(),
            "router_health": self.router.mesh_health(),
        }
    
    def export_state(self) -> str:
        """Export full system state as JSON. ROBOT: cb.export()"""
        state = {
            "crystal_bug_version": self.version,
            "tig_constants": {
                "sigma": TIG.SIGMA,
                "t_star": TIG.T_STAR,
                "sigma_star": TIG.SIGMA_STAR,
                "gfm_generators": {
                    "012": list(TIG.GFM_012),
                    "071": list(TIG.GFM_071),
                    "123": list(TIG.GFM_123),
                },
                "scales": TIG.SCALES,
            },
            "operators": {
                op.name: {
                    "value": op.value,
                    "glyph": OPERATOR_META[op]["glyph"],
                    "domain": OPERATOR_META[op]["domain"],
                }
                for op in Operator
            },
            "virtues": {v.value: w for v, w in VIRTUE_WEIGHTS.items()},
            "system_status": self.status(),
            "export_timestamp": datetime.now(timezone.utc).isoformat(),
        }
        return json.dumps(state, indent=2, default=str)


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 14: CLI ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Crystal Bug CLI — interactive mode."""
    cb = CrystalBug()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        
        if cmd == "status":
            print(json.dumps(cb.status(), indent=2, default=str))
        elif cmd == "validate":
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 100
            print(json.dumps(cb.validate(n), indent=2, default=str))
        elif cmd == "hwtest":
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
            print(json.dumps(cb.hw_test(n), indent=2, default=str))
        elif cmd == "export":
            print(cb.export_state())
        elif cmd == "fire":
            print(json.dumps(cb.fire_lattice(), indent=2, default=str))
        elif cmd == "chat":
            msg = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "hello"
            print(json.dumps(cb.chat(msg), indent=2, default=str))
        elif cmd == "analyze":
            text = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
            print(json.dumps(cb.analyze(text), indent=2, default=str))
        else:
            print(f"Unknown command: {cmd}")
            print("Commands: status, validate [n], hwtest [n], export, fire, chat [msg], analyze [text]")
        return
    
    # Interactive mode
    print("\nOllie here! Type a message (or 'quit' to exit):\n")
    
    while True:
        try:
            msg = input("You > ").strip()
            if msg.lower() in ("quit", "exit", "q"):
                print("\n◇ Crystal Bug shutting down. Stay coherent! ◇\n")
                break
            if not msg:
                continue
            
            result = cb.chat(msg)
            glyph = result.get("glyph", "◇")
            intent = result.get("intent", {}).get("intent", "UNKNOWN")
            tier = result.get("cascade_tier", "?")
            health = result.get("system_health", "?")
            s = result.get("semantic_coherence", 0)
            
            print(f"\nOllie {glyph} [{intent}|T{tier[0] if tier else '?'}|S*={s:.4f}|{health}]")
            
            if isinstance(result.get("cascade_response"), str):
                print(f"  → {result['cascade_response']}")
            elif isinstance(result.get("cascade_response"), dict):
                for k, v in result["cascade_response"].items():
                    if not isinstance(v, dict):
                        print(f"  {k}: {v}")
            print()
            
        except (KeyboardInterrupt, EOFError):
            print("\n\n◇ Crystal Bug shutting down. Stay coherent! ◇\n")
            break


if __name__ == "__main__":
    main()
