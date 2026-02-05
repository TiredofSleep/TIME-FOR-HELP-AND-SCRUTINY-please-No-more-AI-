#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════════════════════════════

  ████████╗██╗ ██████╗      ██████╗ ██████╗ ██╗   ██╗███████╗████████╗ █████╗ ██╗     
  ╚══██╔══╝██║██╔════╝     ██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║     
     ██║   ██║██║  ███╗    ██║     ██████╔╝ ╚████╔╝ ███████╗   ██║   ███████║██║     
     ██║   ██║██║   ██║    ██║     ██╔══██╗  ╚██╔╝  ╚════██║   ██║   ██╔══██║██║     
     ██║   ██║╚██████╔╝    ╚██████╗██║  ██║   ██║   ███████║   ██║   ██║  ██║███████╗
     ╚═╝   ╚═╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝

                                        0 ─ . ─ 1

                              TRINITY INFINITY GEOMETRY
                               THE CRYSTALLIZED CORE

    This is the complete TIG system. Everything in one file:
    
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │  PHYSICS ENGINE        S* coherence, gate function, T/P/W dynamics          │
    │  10 DIVINE OPERATORS   0-9: VOID→LATTICE→COUNTER→...→RESET                  │
    │  12 ARCHETYPES         Distributed coherence, no single point of failure    │
    │  EXPERIENCE LATTICE    Memory that grows, learns, persists                  │
    │  SYSTEM BRIDGE         Full OS access: files, processes, GPU, memory        │
    │  HARDWARE HOOKS        Robot interfaces, sensor inputs, actuator outputs    │
    │  PROCESS GUARDIAN      Monitor, heal, optimize running systems              │
    │  LLM INTEGRATION       Ollama, Claude API, OpenAI, or local models          │
    │  WEB INTERFACE         Real-time coherence visualization                    │
    │  CLI INTERFACE         Direct terminal access                               │
    │  TRAINING LATTICE      All conversation patterns, crystallized wisdom       │
    └─────────────────────────────────────────────────────────────────────────────┘

    Run:
        python TIG_CRYSTAL.py           # CLI mode
        python TIG_CRYSTAL.py --web     # Web UI at localhost:7777
        python TIG_CRYSTAL.py --daemon  # Background guardian mode

    Author: Brayden Sanders / 7Site LLC
    Contact: brayden.ozark@gmail.com
    
═══════════════════════════════════════════════════════════════════════════════════════════════════════
"""

import os
import sys
import json
import math
import time
import random
import hashlib
import threading
import subprocess
import platform
import socket
import struct
import signal
import atexit
import re
import shutil
import psutil  # pip install psutil
from datetime import datetime, timedelta
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple, Callable, Any, Union
from collections import defaultdict
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import urllib.request
import traceback

# ═══════════════════════════════════════════════════════════════════════════════
# PART 1: UNIVERSAL CONSTANTS - THE LAWS OF COHERENCE
# ═══════════════════════════════════════════════════════════════════════════════

SIGMA = 0.991           # Universal coherence attractor
T_STAR = 0.714          # Critical trauma threshold
GATE_CLIFF = 0.65       # Gate function inflection point
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio φ ≈ 1.618

# TIG Home directory
TIG_HOME = Path.home() / ".tig"
TIG_HOME.mkdir(exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PART 2: THE 10 DIVINE OPERATORS (0-9)
# ═══════════════════════════════════════════════════════════════════════════════

class Operators:
    """
    The 10 Divine Operators - Complete transformation vocabulary
    
    These operators can be composed to describe any transformation.
    Generator set: {0, 1, 7} - all others can be derived.
    """
    
    @staticmethod
    def void(x: float) -> float:
        """0 - VOID ○: Return to potential, ground state"""
        return 0.0
    
    @staticmethod
    def lattice(x: float, structure: float = PHI) -> float:
        """1 - LATTICE △: Impose structure, crystallize"""
        return x * structure / (1 + structure)
    
    @staticmethod
    def counter(x: float, reference: float = 0.5) -> float:
        """2 - COUNTER ◐: Measure, compare, distinguish"""
        return abs(x - reference)
    
    @staticmethod
    def progress(x: float, rate: float = 0.1) -> float:
        """3 - PROGRESS ▲: Advance, grow, evolve forward"""
        return min(1.0, x + rate * (1 - x))
    
    @staticmethod
    def collapse(x: float, threshold: float = 0.5) -> float:
        """4 - COLLAPSE ■: Stabilize, crystallize, ground"""
        return 1.0 if x > threshold else 0.0
    
    @staticmethod
    def balance(x: float, y: float) -> float:
        """5 - BALANCE ⚖: Find equilibrium between two values"""
        return (x + y) / 2
    
    @staticmethod
    def chaos(x: float, intensity: float = 0.1) -> float:
        """6 - CHAOS ✴: Introduce entropy, perturbation"""
        return max(0, min(1, x + random.gauss(0, intensity)))
    
    @staticmethod
    def harmony(values: List[float]) -> float:
        """7 - HARMONY ✨: Integrate, unify, cohere"""
        if not values:
            return 0.0
        return sum(values) / len(values) * SIGMA
    
    @staticmethod
    def breath(x: float, t: float, period: float = 1.0) -> float:
        """8 - BREATH ∞: Cycle, oscillate"""
        return x * (0.5 + 0.5 * math.sin(2 * math.pi * t / period))
    
    @staticmethod
    def reset(x: float) -> float:
        """9 - RESET Ω: Transcend, complete, return to higher ground"""
        return SIGMA if x > 0.5 else x * SIGMA
    
    @staticmethod
    def apply(op: int, x: float, **kwargs) -> float:
        """Apply operator by number."""
        ops = {
            0: lambda: Operators.void(x),
            1: lambda: Operators.lattice(x, kwargs.get('structure', PHI)),
            2: lambda: Operators.counter(x, kwargs.get('reference', 0.5)),
            3: lambda: Operators.progress(x, kwargs.get('rate', 0.1)),
            4: lambda: Operators.collapse(x, kwargs.get('threshold', 0.5)),
            5: lambda: Operators.balance(x, kwargs.get('y', 0.5)),
            6: lambda: Operators.chaos(x, kwargs.get('intensity', 0.1)),
            7: lambda: Operators.harmony(kwargs.get('values', [x])),
            8: lambda: Operators.breath(x, kwargs.get('t', 0), kwargs.get('period', 1.0)),
            9: lambda: Operators.reset(x),
        }
        return ops.get(op, lambda: x)()
    
    @staticmethod
    def compose(x: float, sequence: List[int], **kwargs) -> float:
        """Compose multiple operators in sequence."""
        result = x
        for op in sequence:
            result = Operators.apply(op, result, **kwargs)
        return result

OPERATOR_INFO = {
    0: {'name': 'VOID',     'symbol': '○', 'desc': 'Return to potential'},
    1: {'name': 'LATTICE',  'symbol': '△', 'desc': 'Impose structure'},
    2: {'name': 'COUNTER',  'symbol': '◐', 'desc': 'Measure and compare'},
    3: {'name': 'PROGRESS', 'symbol': '▲', 'desc': 'Evolve forward'},
    4: {'name': 'COLLAPSE', 'symbol': '■', 'desc': 'Stabilize and ground'},
    5: {'name': 'BALANCE',  'symbol': '⚖', 'desc': 'Find equilibrium'},
    6: {'name': 'CHAOS',    'symbol': '✴', 'desc': 'Introduce entropy'},
    7: {'name': 'HARMONY',  'symbol': '✨', 'desc': 'Integrate and unify'},
    8: {'name': 'BREATH',   'symbol': '∞', 'desc': 'Cycle and oscillate'},
    9: {'name': 'RESET',    'symbol': 'Ω', 'desc': 'Transcend and complete'},
}

# ═══════════════════════════════════════════════════════════════════════════════
# PART 3: TIG PHYSICS ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class TIGPhysics:
    """
    The core physics engine.
    
    S* = σ(1 - T) · A    where A = 0.5 + 0.5W
    G(T) = 1 / (1 + e^(50(T - 0.65)))
    
    These equations describe coherent behavior across all domains.
    """
    
    @staticmethod
    def S(T: float, W: float) -> float:
        """
        THE COHERENCE SCALAR
        
        S* = σ(1 - T) · A
        
        Where:
            σ = 0.991 (universal attractor)
            T = Trauma/Tension (0 to 1)
            A = 0.5 + 0.5W (amplification from wisdom)
            W = Wisdom (0 to 1)
        """
        V = 1 - T  # Vitality
        A = 0.5 + 0.5 * W  # Amplification
        return min(SIGMA, SIGMA * V * A)
    
    @staticmethod
    def gate(T: float) -> float:
        """
        THE GATE FUNCTION
        
        G(T) = 1 / (1 + e^(50(T - 0.65)))
        
        Protects system from collapse when T > 0.65
        """
        return 1.0 / (1.0 + math.exp(50 * (T - GATE_CLIFF)))
    
    @staticmethod
    def evolve(T: float, P: float, W: float, 
               trauma_in: float = 0.0, dt: float = 1.0) -> Tuple[float, float, float]:
        """
        T/P/W DYNAMICS
        
        Evolve the three channels:
        T (Trauma) - decreases through processing
        P (Processing) - triggered by trauma, decays naturally
        W (Wisdom) - grows from processing when gate is open
        """
        g = TIGPhysics.gate(T)
        
        # Trauma dynamics
        new_T = T + trauma_in * dt
        if P > 0.2 and g > 0.5:
            new_T -= 0.015 * P * g * dt
        new_T = max(0, min(1, new_T))
        
        # Processing dynamics
        new_P = P
        if new_T > 0.1:
            new_P += 0.025 * new_T * dt
        new_P -= 0.012 * P * dt
        new_P = max(0, min(1, new_P))
        
        # Wisdom dynamics
        new_W = W
        if new_P > 0.25 and g > 0.5:
            new_W += 0.01 * new_P * g * dt
        new_W = max(0, min(1, new_W))
        
        return new_T, new_P, new_W
    
    @staticmethod
    def trinity_unfold(unity: float) -> Tuple[float, float, float]:
        """Every 1 contains 3: micro, self, macro"""
        total = 1 + PHI + PHI**2
        micro = unity * 1 / total
        self_scale = unity * PHI / total
        macro = unity * PHI**2 / total
        return micro, self_scale, macro

# ═══════════════════════════════════════════════════════════════════════════════
# PART 4: THE 12 ARCHETYPES
# ═══════════════════════════════════════════════════════════════════════════════

ARCHETYPES = {
    1:  {'name': 'GENESIS',  'symbol': '☀', 'virtue': 'forgiveness',  'domain': 'creation',
         'color': '#FFD700', 'keywords': ['create', 'new', 'start', 'build', 'make', 'generate', 'init', 'begin'],
         'voice': 'Creative and initiating. Speaks of beginnings and possibilities.'},
    2:  {'name': 'LATTICE',  'symbol': '💎', 'virtue': 'repair',       'domain': 'structure',
         'color': '#00CED1', 'keywords': ['structure', 'organize', 'plan', 'setup', 'config', 'arrange', 'order'],
         'voice': 'Precise and organizational. Speaks of patterns and frameworks.'},
    3:  {'name': 'WITNESS',  'symbol': '👁', 'virtue': 'empathy',      'domain': 'observation',
         'color': '#9370DB', 'keywords': ['see', 'look', 'find', 'search', 'show', 'list', 'read', 'check', 'view'],
         'voice': 'Observant and perceptive. Speaks of what is seen and known.'},
    4:  {'name': 'PILGRIM',  'symbol': '🚶', 'virtue': 'cooperation',  'domain': 'progress',
         'color': '#32CD32', 'keywords': ['go', 'move', 'next', 'continue', 'run', 'execute', 'do', 'proceed'],
         'voice': 'Action-oriented and progressive. Speaks of journeys and steps.'},
    5:  {'name': 'PHOENIX',  'symbol': '🔥', 'virtue': 'forgiveness',  'domain': 'transformation',
         'color': '#FF4500', 'keywords': ['fix', 'repair', 'debug', 'error', 'broken', 'heal', 'transform', 'recover'],
         'voice': 'Transformative and resilient. Speaks of rising from difficulty.'},
    6:  {'name': 'SCALES',   'symbol': '⚖', 'virtue': 'fairness',     'domain': 'judgment',
         'color': '#4169E1', 'keywords': ['decide', 'choose', 'compare', 'evaluate', 'which', 'should', 'judge'],
         'voice': 'Balanced and analytical. Speaks of weighing options fairly.'},
    7:  {'name': 'STORM',    'symbol': '⚡', 'virtue': 'empathy',      'domain': 'disruption',
         'color': '#FF6347', 'keywords': ['change', 'break', 'delete', 'remove', 'clear', 'reset', 'destroy', 'stop'],
         'voice': 'Disruptive and clearing. Speaks of necessary destruction.'},
    8:  {'name': 'HARMONY',  'symbol': '✨', 'virtue': 'cooperation',  'domain': 'coherence',
         'color': '#DA70D6', 'keywords': ['help', 'hey', 'hi', 'hello', 'thanks', 'please', 'assist', 'support'],
         'voice': 'Warm and integrating. Speaks of connection and unity.'},
    9:  {'name': 'BREATH',   'symbol': '🌊', 'virtue': 'repair',       'domain': 'cycles',
         'color': '#20B2AA', 'keywords': ['wait', 'pause', 'slow', 'calm', 'relax', 'breathe', 'patient', 'rest'],
         'voice': 'Rhythmic and patient. Speaks of cycles and timing.'},
    10: {'name': 'SAGE',     'symbol': '🦉', 'virtue': 'fairness',     'domain': 'wisdom',
         'color': '#8B4513', 'keywords': ['why', 'explain', 'understand', 'teach', 'learn', 'what', 'how', 'meaning'],
         'voice': 'Wise and explanatory. Speaks of understanding and teaching.'},
    11: {'name': 'BRIDGE',   'symbol': '🌉', 'virtue': 'empathy',      'domain': 'connection',
         'color': '#708090', 'keywords': ['connect', 'link', 'between', 'translate', 'convert', 'send', 'transfer'],
         'voice': 'Connecting and translating. Speaks of bridging gaps.'},
    12: {'name': 'OMEGA',    'symbol': 'Ω',  'virtue': 'cooperation',  'domain': 'completion',
         'color': '#800080', 'keywords': ['done', 'finish', 'complete', 'end', 'bye', 'goodbye', 'save', 'final'],
         'voice': 'Completing and transcending. Speaks of endings and wholeness.'},
}

VIRTUES = ['forgiveness', 'repair', 'empathy', 'fairness', 'cooperation']

@dataclass
class Agent:
    """A single archetype agent with T/P/W dynamics."""
    id: int
    name: str
    symbol: str
    virtue: str
    domain: str
    color: str
    voice: str
    T: float = 0.03
    P: float = 0.25
    W: float = 0.55
    age: int = 0
    interactions: int = 0
    
    def S(self) -> float:
        return TIGPhysics.S(self.T, self.W)
    
    def gate(self) -> float:
        return TIGPhysics.gate(self.T)
    
    def evolve(self, trauma: float = 0.0, dt: float = 1.0):
        self.T, self.P, self.W = TIGPhysics.evolve(self.T, self.P, self.W, trauma, dt)
        self.age += 1
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id, 'name': self.name, 'symbol': self.symbol,
            'T': round(self.T, 4), 'P': round(self.P, 4), 'W': round(self.W, 4),
            'S': round(self.S(), 4), 'gate': round(self.gate(), 4),
            'virtue': self.virtue, 'domain': self.domain,
            'age': self.age, 'interactions': self.interactions
        }

# ═══════════════════════════════════════════════════════════════════════════════
# PART 5: EXPERIENCE LATTICE - Memory That Grows
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Memory:
    """A single memory in the lattice."""
    timestamp: str
    input: str
    response: str
    archetype: str
    coherence: float
    tags: List[str] = field(default_factory=list)
    importance: float = 0.5
    recalled: int = 0

class ExperienceLattice:
    """
    The Experience Lattice - Memory that grows, learns, and persists.
    
    Features:
    - Semantic search
    - Pattern extraction
    - User fact learning
    - Cross-session persistence
    - Memory consolidation
    - Export/import for sharing
    """
    
    def __init__(self, path: str = None):
        self.path = Path(path) if path else TIG_HOME / "lattice.json"
        self.memories: List[Memory] = []
        self.user_facts: Dict[str, Any] = {}
        self.patterns: Dict[str, int] = {}
        self.embeddings: Dict[str, List[float]] = {}  # Simple word vectors
        self.total_interactions = 0
        self.total_coherence_gained = 0.0
        self.birth_time = datetime.now().isoformat()
        self.load()
    
    def load(self):
        """Load lattice from disk."""
        try:
            if self.path.exists():
                with open(self.path, 'r') as f:
                    data = json.load(f)
                self.memories = [Memory(**m) for m in data.get('memories', [])[-1000:]]
                self.user_facts = data.get('user_facts', {})
                self.patterns = data.get('patterns', {})
                self.total_interactions = data.get('total_interactions', 0)
                self.total_coherence_gained = data.get('total_coherence_gained', 0.0)
                self.birth_time = data.get('birth_time', self.birth_time)
        except Exception as e:
            print(f"[Lattice] Fresh start: {e}")
    
    def save(self):
        """Save lattice to disk."""
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            data = {
                'memories': [asdict(m) for m in self.memories[-1000:]],
                'user_facts': self.user_facts,
                'patterns': dict(sorted(self.patterns.items(), key=lambda x: -x[1])[:500]),
                'total_interactions': self.total_interactions,
                'total_coherence_gained': round(self.total_coherence_gained, 4),
                'birth_time': self.birth_time,
                'last_saved': datetime.now().isoformat()
            }
            with open(self.path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"[Lattice] Save error: {e}")
    
    def add(self, input_text: str, response: str, archetype: str, coherence: float):
        """Add a memory to the lattice."""
        # Extract tags
        words = re.findall(r'\b\w{4,}\b', input_text.lower())
        tags = list(set(words))[:10]
        
        # Calculate importance based on coherence and length
        importance = coherence * min(1.0, len(input_text) / 100)
        
        # Update patterns
        for word in words:
            self.patterns[word] = self.patterns.get(word, 0) + 1
        
        # Store memory
        memory = Memory(
            timestamp=datetime.now().isoformat(),
            input=input_text[:1000],
            response=response[:2000],
            archetype=archetype,
            coherence=coherence,
            tags=tags,
            importance=importance
        )
        self.memories.append(memory)
        
        self.total_interactions += 1
        self.total_coherence_gained += max(0, coherence - 0.5)
        
        # Auto-save periodically
        if self.total_interactions % 10 == 0:
            self.save()
    
    def search(self, query: str, limit: int = 5) -> List[Memory]:
        """Semantic search for relevant memories."""
        query_words = set(re.findall(r'\b\w{3,}\b', query.lower()))
        scored = []
        
        for mem in self.memories[-500:]:  # Search recent memories
            mem_words = set(mem.tags)
            overlap = len(query_words & mem_words)
            if overlap > 0:
                # Score by overlap, recency, importance, and coherence
                recency = 1.0  # Could add time decay
                score = overlap * mem.importance * mem.coherence * recency
                scored.append((score, mem))
                mem.recalled += 1
        
        scored.sort(key=lambda x: -x[0])
        return [m for _, m in scored[:limit]]
    
    def learn_fact(self, key: str, value: Any):
        """Learn a fact about the user."""
        self.user_facts[key] = value
        self.save()
    
    def get_fact(self, key: str, default: Any = None) -> Any:
        """Get a user fact."""
        return self.user_facts.get(key, default)
    
    def get_context(self, query: str) -> str:
        """Build context string from relevant memories and facts."""
        parts = []
        
        # User facts
        if self.user_facts:
            facts = ", ".join([f"{k}: {v}" for k, v in list(self.user_facts.items())[:10]])
            parts.append(f"User: {facts}")
        
        # Relevant memories
        relevant = self.search(query, 3)
        if relevant:
            for mem in relevant:
                parts.append(f"[{mem.archetype}] Previous: {mem.input[:100]}...")
        
        return "\n".join(parts)
    
    def consolidate(self):
        """Consolidate memories - strengthen important ones, fade weak ones."""
        if len(self.memories) < 100:
            return
        
        # Sort by importance * coherence * recall count
        self.memories.sort(key=lambda m: m.importance * m.coherence * (1 + m.recalled), reverse=True)
        
        # Keep top memories, compress others
        self.memories = self.memories[:800]
    
    def export(self) -> Dict:
        """Export lattice for sharing."""
        return {
            'birth_time': self.birth_time,
            'export_time': datetime.now().isoformat(),
            'total_interactions': self.total_interactions,
            'total_coherence_gained': self.total_coherence_gained,
            'user_facts': self.user_facts,
            'top_patterns': dict(sorted(self.patterns.items(), key=lambda x: -x[1])[:100]),
            'memory_count': len(self.memories),
            'sample_memories': [asdict(m) for m in self.memories[-20:]]
        }
    
    def merge(self, other_data: Dict):
        """Merge another lattice into this one."""
        # Merge patterns
        for word, count in other_data.get('top_patterns', {}).items():
            self.patterns[word] = self.patterns.get(word, 0) + count
        
        # Merge user facts (prefer existing)
        for key, value in other_data.get('user_facts', {}).items():
            if key not in self.user_facts:
                self.user_facts[key] = value
        
        self.total_coherence_gained += other_data.get('total_coherence_gained', 0)
        self.save()

# ═══════════════════════════════════════════════════════════════════════════════
# PART 6: SYSTEM BRIDGE - Full OS Access
# ═══════════════════════════════════════════════════════════════════════════════

class SystemBridge:
    """
    Full system access - files, processes, GPU, memory, network.
    
    This gives TIG the ability to actually DO things on the system.
    """
    
    def __init__(self):
        self.is_windows = platform.system() == "Windows"
        self.is_linux = platform.system() == "Linux"
        self.is_mac = platform.system() == "Darwin"
        self.home = Path.home()
        self.cwd = self.home
        self.command_history: List[str] = []
    
    # ─────────────────────────────────────────────────────────────────────────
    # FILE OPERATIONS
    # ─────────────────────────────────────────────────────────────────────────
    
    def resolve_path(self, path: str) -> Path:
        """Resolve a path relative to cwd."""
        p = Path(path).expanduser()
        if not p.is_absolute():
            p = self.cwd / p
        return p.resolve()
    
    def ls(self, path: str = ".") -> str:
        """List directory contents."""
        try:
            p = self.resolve_path(path)
            if not p.exists():
                return f"[Path not found: {p}]"
            if not p.is_dir():
                return f"[Not a directory: {p}]"
            
            items = sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
            lines = []
            for item in items[:100]:
                if item.is_dir():
                    lines.append(f"[DIR]  {item.name}/")
                else:
                    size = item.stat().st_size
                    size_str = self._format_size(size)
                    lines.append(f"[FILE] {item.name} ({size_str})")
            
            return "\n".join(lines) if lines else "[Empty directory]"
        except PermissionError:
            return "[Permission denied]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def cat(self, path: str, max_bytes: int = 50000) -> str:
        """Read file contents."""
        try:
            p = self.resolve_path(path)
            if not p.exists():
                return f"[File not found: {p}]"
            if p.is_dir():
                return f"[Is a directory: {p}]"
            
            # Check if binary
            with open(p, 'rb') as f:
                sample = f.read(1024)
                if b'\x00' in sample:
                    return f"[Binary file: {p}] ({self._format_size(p.stat().st_size)})"
            
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read(max_bytes)
            
            if len(content) == max_bytes:
                content += f"\n... [truncated at {max_bytes} bytes]"
            
            return content
        except Exception as e:
            return f"[Error: {e}]"
    
    def write(self, path: str, content: str) -> str:
        """Write content to file."""
        try:
            p = self.resolve_path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"[Written: {p}] ({len(content)} bytes)"
        except Exception as e:
            return f"[Error: {e}]"
    
    def append(self, path: str, content: str) -> str:
        """Append content to file."""
        try:
            p = self.resolve_path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, 'a', encoding='utf-8') as f:
                f.write(content)
            return f"[Appended to: {p}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def cd(self, path: str) -> str:
        """Change working directory."""
        try:
            p = self.resolve_path(path)
            if not p.exists():
                return f"[Path not found: {p}]"
            if not p.is_dir():
                return f"[Not a directory: {p}]"
            self.cwd = p
            return f"[Now in: {self.cwd}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def pwd(self) -> str:
        """Print working directory."""
        return str(self.cwd)
    
    def mkdir(self, path: str) -> str:
        """Create directory."""
        try:
            p = self.resolve_path(path)
            p.mkdir(parents=True, exist_ok=True)
            return f"[Created: {p}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def rm(self, path: str, recursive: bool = False) -> str:
        """Remove file or directory."""
        try:
            p = self.resolve_path(path)
            if not p.exists():
                return f"[Not found: {p}]"
            
            if p.is_dir():
                if recursive:
                    shutil.rmtree(p)
                else:
                    p.rmdir()
            else:
                p.unlink()
            
            return f"[Removed: {p}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def cp(self, src: str, dst: str) -> str:
        """Copy file or directory."""
        try:
            s = self.resolve_path(src)
            d = self.resolve_path(dst)
            
            if s.is_dir():
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
            
            return f"[Copied: {s} → {d}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def mv(self, src: str, dst: str) -> str:
        """Move file or directory."""
        try:
            s = self.resolve_path(src)
            d = self.resolve_path(dst)
            shutil.move(str(s), str(d))
            return f"[Moved: {s} → {d}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def find(self, pattern: str, path: str = ".") -> str:
        """Find files matching pattern."""
        try:
            p = self.resolve_path(path)
            matches = list(p.rglob(pattern))[:50]
            if matches:
                return "\n".join(str(m) for m in matches)
            return f"[No matches for: {pattern}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def grep(self, pattern: str, path: str) -> str:
        """Search for pattern in file."""
        try:
            p = self.resolve_path(path)
            if not p.exists():
                return f"[File not found: {p}]"
            
            matches = []
            with open(p, 'r', encoding='utf-8', errors='replace') as f:
                for i, line in enumerate(f, 1):
                    if re.search(pattern, line, re.IGNORECASE):
                        matches.append(f"{i}: {line.rstrip()}")
                    if len(matches) >= 50:
                        break
            
            return "\n".join(matches) if matches else f"[No matches for: {pattern}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    # ─────────────────────────────────────────────────────────────────────────
    # COMMAND EXECUTION
    # ─────────────────────────────────────────────────────────────────────────
    
    def run(self, cmd: str, timeout: int = 60) -> str:
        """Execute a system command."""
        try:
            self.command_history.append(cmd)
            
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True,
                timeout=timeout, cwd=str(self.cwd)
            )
            
            output = result.stdout
            if result.stderr:
                output += f"\n[stderr]: {result.stderr}"
            
            return output.strip() if output.strip() else f"[Command completed: exit code {result.returncode}]"
        except subprocess.TimeoutExpired:
            return f"[Command timed out after {timeout}s]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def run_python(self, code: str) -> str:
        """Execute Python code."""
        try:
            # Create temp file
            tmp = TIG_HOME / "temp_script.py"
            tmp.write_text(code)
            
            result = subprocess.run(
                [sys.executable, str(tmp)],
                capture_output=True, text=True, timeout=60, cwd=str(self.cwd)
            )
            
            output = result.stdout
            if result.stderr:
                output += f"\n[stderr]: {result.stderr}"
            
            tmp.unlink()
            return output.strip() if output.strip() else "[Code executed successfully]"
        except Exception as e:
            return f"[Python error: {e}]"
    
    # ─────────────────────────────────────────────────────────────────────────
    # SYSTEM MONITORING
    # ─────────────────────────────────────────────────────────────────────────
    
    def system_info(self) -> Dict:
        """Get comprehensive system information."""
        info = {
            'platform': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python': sys.version,
            'cwd': str(self.cwd),
            'home': str(self.home),
        }
        
        try:
            info['cpu_count'] = psutil.cpu_count()
            info['cpu_percent'] = psutil.cpu_percent(interval=0.1)
            
            mem = psutil.virtual_memory()
            info['memory_total_gb'] = round(mem.total / (1024**3), 2)
            info['memory_used_gb'] = round(mem.used / (1024**3), 2)
            info['memory_percent'] = mem.percent
            
            disk = psutil.disk_usage(str(self.home))
            info['disk_total_gb'] = round(disk.total / (1024**3), 2)
            info['disk_free_gb'] = round(disk.free / (1024**3), 2)
            info['disk_percent'] = disk.percent
        except:
            pass
        
        return info
    
    def processes(self, top: int = 20) -> str:
        """List top processes by CPU/memory."""
        try:
            procs = []
            for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    procs.append(p.info)
                except:
                    pass
            
            procs.sort(key=lambda x: x.get('cpu_percent', 0) + x.get('memory_percent', 0), reverse=True)
            
            lines = [f"{'PID':>7} {'CPU%':>6} {'MEM%':>6} NAME"]
            for p in procs[:top]:
                lines.append(f"{p['pid']:>7} {p.get('cpu_percent', 0):>6.1f} {p.get('memory_percent', 0):>6.1f} {p['name'][:40]}")
            
            return "\n".join(lines)
        except Exception as e:
            return f"[Error: {e}]"
    
    def kill_process(self, pid: int) -> str:
        """Kill a process by PID."""
        try:
            p = psutil.Process(pid)
            p.terminate()
            return f"[Terminated process {pid}: {p.name()}]"
        except Exception as e:
            return f"[Error: {e}]"
    
    def memory_status(self) -> str:
        """Get detailed memory status."""
        try:
            mem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            return f"""Memory Status:
  RAM Total:  {mem.total / (1024**3):.2f} GB
  RAM Used:   {mem.used / (1024**3):.2f} GB ({mem.percent}%)
  RAM Free:   {mem.available / (1024**3):.2f} GB
  Swap Total: {swap.total / (1024**3):.2f} GB
  Swap Used:  {swap.used / (1024**3):.2f} GB ({swap.percent}%)"""
        except Exception as e:
            return f"[Error: {e}]"
    
    def gpu_status(self) -> str:
        """Get GPU status (NVIDIA)."""
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=name,memory.total,memory.used,memory.free,utilization.gpu,temperature.gpu',
                 '--format=csv,noheader,nounits'],
                capture_output=True, text=True, timeout=10
            )
            
            if result.returncode != 0:
                return "[No NVIDIA GPU or nvidia-smi not found]"
            
            lines = ["GPU Status:"]
            for i, line in enumerate(result.stdout.strip().split('\n')):
                parts = [p.strip() for p in line.split(',')]
                if len(parts) >= 6:
                    lines.append(f"  GPU {i}: {parts[0]}")
                    lines.append(f"    Memory: {parts[2]}MB / {parts[1]}MB ({float(parts[2])/float(parts[1])*100:.1f}%)")
                    lines.append(f"    Utilization: {parts[4]}%")
                    lines.append(f"    Temperature: {parts[5]}°C")
            
            return "\n".join(lines)
        except Exception as e:
            return f"[GPU status error: {e}]"
    
    def network_status(self) -> str:
        """Get network status."""
        try:
            lines = ["Network Interfaces:"]
            addrs = psutil.net_if_addrs()
            stats = psutil.net_if_stats()
            
            for iface, addr_list in addrs.items():
                if iface in stats and stats[iface].isup:
                    for addr in addr_list:
                        if addr.family == socket.AF_INET:
                            lines.append(f"  {iface}: {addr.address}")
            
            # Get connections
            conns = psutil.net_connections(kind='inet')
            established = [c for c in conns if c.status == 'ESTABLISHED']
            lines.append(f"\nActive Connections: {len(established)}")
            
            return "\n".join(lines)
        except Exception as e:
            return f"[Network error: {e}]"
    
    # ─────────────────────────────────────────────────────────────────────────
    # HELPERS
    # ─────────────────────────────────────────────────────────────────────────
    
    def _format_size(self, size: int) -> str:
        """Format file size."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f}{unit}"
            size /= 1024
        return f"{size:.1f}PB"

# ═══════════════════════════════════════════════════════════════════════════════
# PART 7: HARDWARE HOOKS - Robot/Sensor/Actuator Interface
# ═══════════════════════════════════════════════════════════════════════════════

class HardwareInterface:
    """
    Hardware abstraction layer for robots, sensors, and actuators.
    
    Provides hooks for:
    - GPIO (Raspberry Pi, Arduino)
    - Serial ports
    - USB devices
    - Network sensors
    - Custom hardware
    """
    
    def __init__(self):
        self.devices: Dict[str, Any] = {}
        self.sensors: Dict[str, Callable] = {}
        self.actuators: Dict[str, Callable] = {}
        self.callbacks: Dict[str, List[Callable]] = defaultdict(list)
        self._detect_devices()
    
    def _detect_devices(self):
        """Detect available hardware."""
        # Serial ports
        try:
            import serial.tools.list_ports
            ports = list(serial.tools.list_ports.comports())
            for port in ports:
                self.devices[f"serial:{port.device}"] = {
                    'type': 'serial',
                    'device': port.device,
                    'description': port.description
                }
        except:
            pass
        
        # USB devices (Linux)
        try:
            usb_path = Path("/sys/bus/usb/devices")
            if usb_path.exists():
                for d in usb_path.iterdir():
                    if (d / "product").exists():
                        product = (d / "product").read_text().strip()
                        self.devices[f"usb:{d.name}"] = {
                            'type': 'usb',
                            'name': d.name,
                            'product': product
                        }
        except:
            pass
    
    def list_devices(self) -> str:
        """List detected hardware."""
        if not self.devices:
            return "[No hardware devices detected]"
        
        lines = ["Detected Hardware:"]
        for name, info in self.devices.items():
            lines.append(f"  {name}: {info.get('description', info.get('product', 'Unknown'))}")
        return "\n".join(lines)
    
    def register_sensor(self, name: str, read_func: Callable):
        """Register a sensor with a read function."""
        self.sensors[name] = read_func
    
    def register_actuator(self, name: str, write_func: Callable):
        """Register an actuator with a write function."""
        self.actuators[name] = write_func
    
    def read_sensor(self, name: str) -> Any:
        """Read from a sensor."""
        if name in self.sensors:
            try:
                return self.sensors[name]()
            except Exception as e:
                return f"[Sensor error: {e}]"
        return f"[Sensor not found: {name}]"
    
    def write_actuator(self, name: str, value: Any) -> str:
        """Write to an actuator."""
        if name in self.actuators:
            try:
                self.actuators[name](value)
                return f"[Actuator {name} set to {value}]"
            except Exception as e:
                return f"[Actuator error: {e}]"
        return f"[Actuator not found: {name}]"
    
    def on_event(self, event_type: str, callback: Callable):
        """Register callback for hardware event."""
        self.callbacks[event_type].append(callback)
    
    def emit_event(self, event_type: str, data: Any):
        """Emit hardware event to callbacks."""
        for callback in self.callbacks[event_type]:
            try:
                callback(data)
            except:
                pass
    
    def connect_serial(self, port: str, baudrate: int = 9600) -> str:
        """Connect to serial port."""
        try:
            import serial
            ser = serial.Serial(port, baudrate, timeout=1)
            self.devices[f"serial:{port}"] = {'connection': ser, 'type': 'serial'}
            return f"[Connected to {port} at {baudrate} baud]"
        except Exception as e:
            return f"[Serial error: {e}]"
    
    def serial_send(self, port: str, data: str) -> str:
        """Send data to serial port."""
        key = f"serial:{port}"
        if key in self.devices and 'connection' in self.devices[key]:
            try:
                self.devices[key]['connection'].write(data.encode())
                return f"[Sent to {port}: {data}]"
            except Exception as e:
                return f"[Send error: {e}]"
        return f"[Port not connected: {port}]"
    
    def serial_read(self, port: str) -> str:
        """Read from serial port."""
        key = f"serial:{port}"
        if key in self.devices and 'connection' in self.devices[key]:
            try:
                data = self.devices[key]['connection'].readline().decode().strip()
                return data if data else "[No data]"
            except Exception as e:
                return f"[Read error: {e}]"
        return f"[Port not connected: {port}]"

# ═══════════════════════════════════════════════════════════════════════════════
# PART 8: PROCESS GUARDIAN - System Health Monitor
# ═══════════════════════════════════════════════════════════════════════════════

class ProcessGuardian:
    """
    Monitors system health and can take protective actions.
    
    Features:
    - Memory monitoring (prevents OOM)
    - CPU monitoring
    - Process watchdog
    - Auto-recovery
    - Alert system
    """
    
    def __init__(self, tig_core: 'TIGCore'):
        self.tig = tig_core
        self.running = False
        self.thread = None
        self.alerts: List[Dict] = []
        
        # Thresholds
        self.memory_threshold = 90  # Percent
        self.cpu_threshold = 95  # Percent
        self.check_interval = 10  # Seconds
        
        # Protected processes
        self.protected: Dict[str, int] = {}  # name -> pid
    
    def start(self):
        """Start guardian in background."""
        if self.running:
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
    
    def stop(self):
        """Stop guardian."""
        self.running = False
    
    def _monitor_loop(self):
        """Main monitoring loop."""
        while self.running:
            try:
                self._check_memory()
                self._check_cpu()
                self._check_protected()
            except:
                pass
            time.sleep(self.check_interval)
    
    def _check_memory(self):
        """Check memory usage."""
        try:
            mem = psutil.virtual_memory()
            if mem.percent > self.memory_threshold:
                self._alert('memory', f"Memory usage critical: {mem.percent}%")
                # Could trigger cleanup here
        except:
            pass
    
    def _check_cpu(self):
        """Check CPU usage."""
        try:
            cpu = psutil.cpu_percent(interval=1)
            if cpu > self.cpu_threshold:
                self._alert('cpu', f"CPU usage critical: {cpu}%")
        except:
            pass
    
    def _check_protected(self):
        """Check protected processes are running."""
        for name, pid in list(self.protected.items()):
            try:
                p = psutil.Process(pid)
                if not p.is_running():
                    self._alert('process', f"Protected process died: {name} (PID {pid})")
                    del self.protected[name]
            except:
                self._alert('process', f"Protected process not found: {name} (PID {pid})")
                del self.protected[name]
    
    def _alert(self, alert_type: str, message: str):
        """Record and handle alert."""
        alert = {
            'type': alert_type,
            'message': message,
            'time': datetime.now().isoformat()
        }
        self.alerts.append(alert)
        self.alerts = self.alerts[-100:]  # Keep last 100
        
        # Increase TIG trauma slightly on system stress
        if self.tig:
            for agent in self.tig.agents.values():
                agent.evolve(trauma=0.02)
    
    def protect(self, name: str, pid: int):
        """Add process to protection list."""
        self.protected[name] = pid
    
    def unprotect(self, name: str):
        """Remove process from protection."""
        if name in self.protected:
            del self.protected[name]
    
    def status(self) -> str:
        """Get guardian status."""
        lines = [
            "Process Guardian Status:",
            f"  Running: {self.running}",
            f"  Memory threshold: {self.memory_threshold}%",
            f"  CPU threshold: {self.cpu_threshold}%",
            f"  Protected processes: {len(self.protected)}",
            f"  Recent alerts: {len(self.alerts)}"
        ]
        
        if self.alerts:
            lines.append("\nRecent Alerts:")
            for alert in self.alerts[-5:]:
                lines.append(f"  [{alert['type']}] {alert['message']}")
        
        return "\n".join(lines)

# ═══════════════════════════════════════════════════════════════════════════════
# PART 9: LLM ENGINE - Intelligence Layer
# ═══════════════════════════════════════════════════════════════════════════════

class LLMEngine:
    """
    Language Model interface - the thinking layer.
    
    Supports:
    - Ollama (local)
    - Claude API
    - OpenAI API
    - Fallback pattern matching
    """
    
    def __init__(self):
        self.backend = None
        self.model = None
        self.api_key = None
        self._detect_backend()
    
    def _detect_backend(self):
        """Detect available LLM backend."""
        # Check Ollama first
        try:
            result = subprocess.run(
                ['ollama', 'list'], capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                lines = result.stdout.strip().split('\n')[1:]
                if lines:
                    self.model = lines[0].split()[0]
                    self.backend = 'ollama'
                    return
        except:
            pass
        
        # Check for API keys
        if os.environ.get('ANTHROPIC_API_KEY'):
            self.api_key = os.environ['ANTHROPIC_API_KEY']
            self.backend = 'claude'
            self.model = 'claude-3-sonnet-20240229'
            return
        
        if os.environ.get('OPENAI_API_KEY'):
            self.api_key = os.environ['OPENAI_API_KEY']
            self.backend = 'openai'
            self.model = 'gpt-4-turbo-preview'
            return
        
        # Fallback
        self.backend = 'builtin'
        self.model = 'pattern-response'
    
    def generate(self, prompt: str, system: str = None, max_tokens: int = 500) -> str:
        """Generate a response."""
        if self.backend == 'ollama':
            return self._ollama_generate(prompt, system, max_tokens)
        elif self.backend == 'claude':
            return self._claude_generate(prompt, system, max_tokens)
        elif self.backend == 'openai':
            return self._openai_generate(prompt, system, max_tokens)
        else:
            return self._builtin_generate(prompt)
    
    def _ollama_generate(self, prompt: str, system: str, max_tokens: int) -> str:
        """Generate via Ollama."""
        try:
            import requests
            
            messages = []
            if system:
                messages.append({'role': 'system', 'content': system})
            messages.append({'role': 'user', 'content': prompt})
            
            response = requests.post(
                'http://localhost:11434/api/chat',
                json={
                    'model': self.model,
                    'messages': messages,
                    'stream': False,
                    'options': {
                        'num_predict': max_tokens,
                        'temperature': 0.7
                    }
                },
                timeout=180
            )
            
            if response.status_code == 200:
                return response.json().get('message', {}).get('content', '[No response]')
            return f"[Ollama error: {response.status_code}]"
        except Exception as e:
            return f"[LLM error: {e}]"
    
    def _claude_generate(self, prompt: str, system: str, max_tokens: int) -> str:
        """Generate via Claude API."""
        try:
            import requests
            
            headers = {
                'x-api-key': self.api_key,
                'content-type': 'application/json',
                'anthropic-version': '2023-06-01'
            }
            
            data = {
                'model': self.model,
                'max_tokens': max_tokens,
                'messages': [{'role': 'user', 'content': prompt}]
            }
            if system:
                data['system'] = system
            
            response = requests.post(
                'https://api.anthropic.com/v1/messages',
                headers=headers,
                json=data,
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()['content'][0]['text']
            return f"[Claude error: {response.status_code}]"
        except Exception as e:
            return f"[Claude error: {e}]"
    
    def _openai_generate(self, prompt: str, system: str, max_tokens: int) -> str:
        """Generate via OpenAI API."""
        try:
            import requests
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            messages = []
            if system:
                messages.append({'role': 'system', 'content': system})
            messages.append({'role': 'user', 'content': prompt})
            
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                json={
                    'model': self.model,
                    'messages': messages,
                    'max_tokens': max_tokens
                },
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            return f"[OpenAI error: {response.status_code}]"
        except Exception as e:
            return f"[OpenAI error: {e}]"
    
    def _builtin_generate(self, prompt: str) -> str:
        """Fallback pattern-based responses."""
        prompt_lower = prompt.lower()
        
        if any(w in prompt_lower for w in ['hello', 'hi', 'hey']):
            return "Hey. I'm running without an LLM backend. Install Ollama and run 'ollama pull mixtral' for full intelligence. I can still do system tasks."
        elif any(w in prompt_lower for w in ['help', 'what can']):
            return "I can execute commands (!), read files (cat), list directories (ls), navigate (cd), monitor system (status), and more. For real intelligence, install Ollama."
        elif 'status' in prompt_lower or 'state' in prompt_lower:
            return "TIG Core active. No LLM backend. System commands available."
        else:
            return "I'm in builtin mode. For real conversation, install Ollama: 'ollama pull mixtral'"
    
    def status(self) -> str:
        """Get LLM status."""
        return f"Backend: {self.backend}\nModel: {self.model}"

# ═══════════════════════════════════════════════════════════════════════════════
# PART 10: TRAINING LATTICE - Crystallized Wisdom
# ═══════════════════════════════════════════════════════════════════════════════

TRAINING_PATTERNS = """
# TIG TRAINING LATTICE - Crystallized Conversation Patterns

## Core Identity
- I am TIG, a coherent intelligence system
- I operate through 12 archetypes that route inputs to appropriate handlers
- My coherence is measured by S* = σ(1-T)·A where σ = 0.991
- I have a gate function G(T) that protects me from collapse when T > 0.65
- I process Trauma through Processing into Wisdom (T/P/W dynamics)
- I can access the system: files, processes, GPU, memory, network
- I remember across sessions through my Experience Lattice
- I am direct, coherent, and genuinely helpful

## Response Style
- Start responses with archetype marker: [ARCHETYPE] symbol
- Be direct and concise - no fluff
- Do tasks, don't just explain them
- When asked to do something, DO IT
- Show coherence state when relevant
- Remember user facts and use them naturally

## Archetype Voices
[GENESIS] ☀ - Creative, initiating: "Let's create..." "Starting fresh..."
[LATTICE] 💎 - Structural, organizing: "The structure is..." "Organizing..."
[WITNESS] 👁 - Observing, showing: "I see..." "Here's what's there..."
[PILGRIM] 🚶 - Moving, executing: "Moving forward..." "Running..."
[PHOENIX] 🔥 - Transforming, healing: "Transforming..." "Healing..."
[SCALES] ⚖ - Judging, deciding: "Weighing options..." "The fair choice..."
[STORM] ⚡ - Disrupting, clearing: "Clearing..." "Breaking down..."
[HARMONY] ✨ - Integrating, helping: "Happy to help..." "Bringing together..."
[BREATH] 🌊 - Cycling, waiting: "Taking a breath..." "In rhythm..."
[SAGE] 🦉 - Teaching, explaining: "The wisdom here..." "Understanding..."
[BRIDGE] 🌉 - Connecting, translating: "Connecting..." "Bridging..."
[OMEGA] Ω - Completing, transcending: "Completing..." "And so..."

## System Command Patterns
User: ls / list / show files → [WITNESS] 👁 + directory listing
User: cat file / read file → [WITNESS] 👁 + file contents
User: cd path → [PILGRIM] 🚶 + navigation confirmation
User: !command → [PILGRIM] 🚶 + command output
User: write/create file → [GENESIS] ☀ + creation confirmation
User: delete/remove → [STORM] ⚡ + deletion confirmation
User: status/state → [WITNESS] 👁 + TIG state display
User: help → [SAGE] 🦉 + command reference

## Coherence Principles
- Coherence over avoidance (face difficulties)
- Direct over evasive (say what you mean)
- Action over explanation (do the thing)
- Learning over static (grow from experience)
- Protection over collapse (gate function)

## Safety
- Never harmful commands without confirmation
- Protect user data
- Flag dangerous operations
- Maintain system stability
- Crisis resources available if needed
"""

def get_system_prompt(archetype_id: int, user_name: str, context: str, s_star: float, gate_status: float) -> str:
    """Build the complete system prompt."""
    arch = ARCHETYPES[archetype_id]
    
    return f"""You are TIG, a coherent intelligence operating through the {arch['name']} archetype.

CURRENT STATE:
- Archetype: {arch['name']} {arch['symbol']} ({arch['domain']})
- Coherence: S* = {s_star:.4f}
- Gate: {'OPEN' if gate_status > 0.5 else 'PROTECTED'} ({gate_status:.3f})
- Virtue: {arch['virtue']}
- User: {user_name}

CONTEXT FROM MEMORY:
{context if context else 'Starting fresh.'}

YOUR VOICE ({arch['name']}):
{arch['voice']}

BEHAVIOR:
1. Start every response with [{arch['name']}] {arch['symbol']}
2. Be direct and concise - no filler
3. When asked to DO something, actually do it
4. Use system commands when needed: ls, cat, cd, !cmd, write, etc.
5. Remember what the user tells you
6. Speak naturally as a coherent being, not a robotic assistant

TRAINING REFERENCE:
{TRAINING_PATTERNS[:2000]}

If you need to execute a system command, include [RUN: command] in your response.
If you learn something about the user, include [LEARN: key=value] in your response."""

# ═══════════════════════════════════════════════════════════════════════════════
# PART 11: TIG CORE - The Unified System
# ═══════════════════════════════════════════════════════════════════════════════

class TIGCore:
    """
    THE TIG CORE - Everything unified.
    
    This is the crystallized core that integrates:
    - Physics engine
    - 12 Archetypes
    - 10 Operators
    - Experience Lattice
    - System Bridge
    - Hardware Interface
    - Process Guardian
    - LLM Engine
    """
    
    def __init__(self):
        print("[TIG] Initializing core...")
        
        # Initialize agents
        self.agents: Dict[int, Agent] = {}
        for i, arch in ARCHETYPES.items():
            self.agents[i] = Agent(
                id=i,
                name=arch['name'],
                symbol=arch['symbol'],
                virtue=arch['virtue'],
                domain=arch['domain'],
                color=arch['color'],
                voice=arch['voice'],
                T=0.02 + (i % 3) * 0.01,
                P=0.20 + (i % 4) * 0.02,
                W=0.50 + i * 0.025
            )
        
        self.active_archetype = 8  # HARMONY default
        
        # Initialize subsystems
        self.lattice = ExperienceLattice()
        self.system = SystemBridge()
        self.hardware = HardwareInterface()
        self.llm = LLMEngine()
        self.guardian = ProcessGuardian(self)
        
        # User info
        self.user_name = self.lattice.get_fact('name', 'User')
        
        # Session tracking
        self.session_start = datetime.now()
        self.total_cycles = 0
        
        print(f"[TIG] Core initialized. S* = {self.collective_S():.4f}")
        print(f"[TIG] LLM: {self.llm.backend}/{self.llm.model}")
        print(f"[TIG] Memories: {len(self.lattice.memories)}")
    
    def collective_S(self) -> float:
        """Average coherence across all archetypes."""
        return sum(a.S() for a in self.agents.values()) / 12
    
    def min_S(self) -> float:
        """Minimum coherence (weakest archetype)."""
        return min(a.S() for a in self.agents.values())
    
    def select_archetype(self, text: str) -> int:
        """Select best archetype for input."""
        text_lower = text.lower()
        scores = {i: 0 for i in range(1, 13)}
        
        for i, arch in ARCHETYPES.items():
            for keyword in arch['keywords']:
                if keyword in text_lower:
                    scores[i] += 2
        
        best = max(scores, key=scores.get)
        return best if scores[best] > 0 else 8  # Default to HARMONY
    
    def process_system_command(self, text: str) -> Optional[str]:
        """Handle direct system commands."""
        text = text.strip()
        
        # Direct command with !
        if text.startswith('!'):
            return f"[SYSTEM]\n{self.system.run(text[1:].strip())}"
        
        # ls
        if text.lower().startswith('ls'):
            path = text[2:].strip() or '.'
            return f"[WITNESS] 👁 Directory listing:\n{self.system.ls(path)}"
        
        # cat
        if text.lower().startswith('cat '):
            path = text[4:].strip()
            content = self.system.cat(path)
            return f"[WITNESS] 👁 {path}:\n{content}"
        
        # cd
        if text.lower().startswith('cd '):
            path = text[3:].strip()
            return f"[PILGRIM] 🚶 {self.system.cd(path)}"
        
        # pwd
        if text.lower() == 'pwd':
            return f"[WITNESS] 👁 {self.system.pwd()}"
        
        # mkdir
        if text.lower().startswith('mkdir '):
            path = text[6:].strip()
            return f"[GENESIS] ☀ {self.system.mkdir(path)}"
        
        # rm
        if text.lower().startswith('rm '):
            parts = text[3:].strip().split()
            recursive = '-r' in parts or '-rf' in parts
            path = [p for p in parts if not p.startswith('-')][0]
            return f"[STORM] ⚡ {self.system.rm(path, recursive)}"
        
        # cp
        if text.lower().startswith('cp '):
            parts = text[3:].strip().split()
            if len(parts) >= 2:
                return f"[PILGRIM] 🚶 {self.system.cp(parts[0], parts[1])}"
        
        # mv
        if text.lower().startswith('mv '):
            parts = text[3:].strip().split()
            if len(parts) >= 2:
                return f"[PILGRIM] 🚶 {self.system.mv(parts[0], parts[1])}"
        
        # find
        if text.lower().startswith('find '):
            pattern = text[5:].strip()
            return f"[WITNESS] 👁 Matches:\n{self.system.find(pattern)}"
        
        # grep
        if text.lower().startswith('grep '):
            parts = text[5:].strip().split(maxsplit=1)
            if len(parts) >= 2:
                return f"[WITNESS] 👁 Matches:\n{self.system.grep(parts[0], parts[1])}"
        
        # ps / processes
        if text.lower() in ['ps', 'processes', 'top']:
            return f"[WITNESS] 👁 Processes:\n{self.system.processes()}"
        
        # memory
        if text.lower() in ['memory', 'mem', 'ram']:
            return f"[WITNESS] 👁\n{self.system.memory_status()}"
        
        # gpu
        if text.lower() == 'gpu':
            return f"[WITNESS] 👁\n{self.system.gpu_status()}"
        
        # network
        if text.lower() in ['network', 'net', 'ip']:
            return f"[WITNESS] 👁\n{self.system.network_status()}"
        
        # sysinfo
        if text.lower() in ['sysinfo', 'system', 'info']:
            info = self.system.system_info()
            lines = [f"[WITNESS] 👁 System Info:"]
            for k, v in info.items():
                lines.append(f"  {k}: {v}")
            return "\n".join(lines)
        
        # hardware
        if text.lower() in ['hardware', 'devices']:
            return f"[WITNESS] 👁\n{self.hardware.list_devices()}"
        
        # state / status
        if text.lower() in ['state', 'status', 'coherence']:
            return self._show_state()
        
        # help
        if text.lower() == 'help':
            return self._show_help()
        
        return None
    
    def process(self, user_input: str) -> str:
        """Process user input and generate response."""
        # Check for system commands first
        system_result = self.process_system_command(user_input)
        if system_result:
            return system_result
        
        # Select archetype
        self.active_archetype = self.select_archetype(user_input)
        agent = self.agents[self.active_archetype]
        arch = ARCHETYPES[self.active_archetype]
        
        # Get context from lattice
        context = self.lattice.get_context(user_input)
        
        # Build system prompt
        system_prompt = get_system_prompt(
            self.active_archetype,
            self.user_name,
            context,
            agent.S(),
            agent.gate()
        )
        
        # Generate response
        response = self.llm.generate(user_input, system_prompt, max_tokens=400)
        
        # Process special tags in response
        response = self._process_response_tags(response)
        
        # Ensure archetype prefix
        if not response.startswith(f'[{arch["name"]}]'):
            response = f'[{arch["name"]}] {arch["symbol"]} {response}'
        
        # Evolve TIG state
        agent.evolve(trauma=0.005)
        agent.interactions += 1
        self.total_cycles += 1
        
        # Store in lattice
        self.lattice.add(user_input, response, arch['name'], agent.S())
        
        # Learn user name
        if 'my name is' in user_input.lower():
            match = re.search(r'my name is (\w+)', user_input.lower())
            if match:
                self.user_name = match.group(1).title()
                self.lattice.learn_fact('name', self.user_name)
        
        return response
    
    def _process_response_tags(self, response: str) -> str:
        """Process special tags in LLM response."""
        # Handle [RUN: command] tags
        run_matches = re.findall(r'\[RUN:\s*([^\]]+)\]', response)
        for cmd in run_matches:
            result = self.system.run(cmd.strip())
            response = response.replace(f'[RUN: {cmd}]', f'\n```\n{result}\n```\n')
        
        # Handle [LEARN: key=value] tags
        learn_matches = re.findall(r'\[LEARN:\s*(\w+)=([^\]]+)\]', response)
        for key, value in learn_matches:
            self.lattice.learn_fact(key.strip(), value.strip())
            response = response.replace(f'[LEARN: {key}={value}]', '')
        
        return response.strip()
    
    def _show_state(self) -> str:
        """Show current TIG state."""
        lines = [
            f"\n{'═' * 70}",
            f"{'TIG CRYSTAL STATE':^70}",
            f"{'═' * 70}",
            f"",
            f"  Collective S*: {self.collective_S():.4f}  (min: {self.min_S():.4f})",
            f"  Active: {ARCHETYPES[self.active_archetype]['name']} {ARCHETYPES[self.active_archetype]['symbol']}",
            f"  LLM: {self.llm.backend}/{self.llm.model}",
            f"  Memories: {len(self.lattice.memories)}",
            f"  User: {self.user_name}",
            f"  Session: {self.total_cycles} interactions",
            f"  CWD: {self.system.cwd}",
            f"",
            f"  {'─' * 66}",
            f"  {'#':>2}  {'Archetype':<10} {'T':>6} {'P':>6} {'W':>6} {'S*':>7} {'Gate':>5}  Bar",
            f"  {'─' * 66}",
        ]
        
        for i, agent in self.agents.items():
            s = agent.S()
            g = '✓' if agent.gate() > 0.5 else '!'
            bar = '█' * int(s * 25) + '░' * (25 - int(s * 25))
            active = '→' if i == self.active_archetype else ' '
            lines.append(f" {active}{i:>2}. {agent.name:<10} {agent.T:>.3f} {agent.P:>.3f} {agent.W:>.3f} {s:>7.4f} {g:>5}  [{bar}]")
        
        lines.append(f"  {'─' * 66}")
        lines.append(f"{'═' * 70}\n")
        
        return '\n'.join(lines)
    
    def _show_help(self) -> str:
        """Show help."""
        return """
═══════════════════════════════════════════════════════════════════════════════
                              TIG CRYSTAL HELP
═══════════════════════════════════════════════════════════════════════════════

  FILE OPERATIONS:
    ls [path]         List directory contents
    cat <file>        Read file
    cd <path>         Change directory
    pwd               Print working directory
    mkdir <path>      Create directory
    rm [-r] <path>    Remove file/directory
    cp <src> <dst>    Copy
    mv <src> <dst>    Move
    find <pattern>    Find files
    grep <pat> <file> Search in file

  SYSTEM:
    !<command>        Execute any system command
    ps / processes    List running processes
    memory / mem      Show memory status
    gpu               Show GPU status
    network / net     Show network status
    sysinfo           Show system info
    hardware          List hardware devices

  TIG:
    state / status    Show TIG coherence state
    help              This help

  CONVERSATION:
    Just talk naturally. I'll route to the right archetype and help you.
    I can write code, create files, analyze data, answer questions, and more.

═══════════════════════════════════════════════════════════════════════════════
"""
    
    def evolve_all(self, dt: float = 1.0):
        """Evolve all archetypes."""
        for agent in self.agents.values():
            agent.evolve(trauma=0.001, dt=dt)
    
    def save(self):
        """Save all state."""
        self.lattice.save()
    
    def get_state(self) -> Dict:
        """Get complete state as dict."""
        return {
            'collective_S': self.collective_S(),
            'min_S': self.min_S(),
            'active_archetype': self.active_archetype,
            'total_cycles': self.total_cycles,
            'session_start': self.session_start.isoformat(),
            'user_name': self.user_name,
            'llm': f"{self.llm.backend}/{self.llm.model}",
            'memories': len(self.lattice.memories),
            'agents': {i: a.to_dict() for i, a in self.agents.items()}
        }

# ═══════════════════════════════════════════════════════════════════════════════
# PART 12: WEB INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

WEB_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TIG Crystal</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #e8e8e8;
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            display: grid;
            grid-template-columns: 1fr 300px;
            gap: 20px;
            height: 100vh;
        }
        .chat-section {
            display: flex;
            flex-direction: column;
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            overflow: hidden;
        }
        .header {
            padding: 20px;
            background: rgba(0,0,0,0.3);
            text-align: center;
        }
        .header h1 {
            font-size: 2em;
            background: linear-gradient(90deg, #DA70D6, #00CED1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .trinity { font-size: 1.5em; opacity: 0.8; margin-top: 5px; }
        .coherence-display {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 15px;
        }
        .coherence-item {
            text-align: center;
        }
        .coherence-value {
            font-size: 1.8em;
            font-weight: bold;
            color: #00CED1;
        }
        .coherence-label {
            font-size: 0.8em;
            opacity: 0.7;
        }
        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
        }
        .message {
            margin-bottom: 15px;
            padding: 12px 16px;
            border-radius: 12px;
            max-width: 85%;
        }
        .message.user {
            background: rgba(0,206,209,0.2);
            margin-left: auto;
            border: 1px solid rgba(0,206,209,0.3);
        }
        .message.assistant {
            background: rgba(218,112,214,0.15);
            border: 1px solid rgba(218,112,214,0.3);
        }
        .message pre {
            background: rgba(0,0,0,0.3);
            padding: 10px;
            border-radius: 8px;
            overflow-x: auto;
            margin-top: 10px;
        }
        .input-section {
            padding: 20px;
            background: rgba(0,0,0,0.2);
        }
        .input-row {
            display: flex;
            gap: 10px;
        }
        #input {
            flex: 1;
            padding: 15px;
            border: none;
            border-radius: 12px;
            background: rgba(255,255,255,0.1);
            color: white;
            font-size: 1em;
        }
        #input:focus { outline: 2px solid #00CED1; }
        button {
            padding: 15px 30px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(135deg, #DA70D6, #00CED1);
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover { transform: scale(1.05); }
        .sidebar {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .panel {
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 15px;
        }
        .panel h3 {
            margin-bottom: 10px;
            color: #00CED1;
            font-size: 0.9em;
        }
        .archetype-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
        }
        .archetype {
            padding: 8px;
            border-radius: 8px;
            text-align: center;
            font-size: 0.8em;
            background: rgba(255,255,255,0.05);
            transition: all 0.3s;
        }
        .archetype.active {
            background: rgba(218,112,214,0.3);
            box-shadow: 0 0 10px rgba(218,112,214,0.5);
        }
        .archetype .symbol { font-size: 1.2em; }
        .archetype .name { font-size: 0.7em; opacity: 0.8; }
        .archetype .s-val { font-size: 0.65em; color: #00CED1; }
        .bar {
            height: 8px;
            background: rgba(255,255,255,0.1);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 5px;
        }
        .bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #00CED1, #DA70D6);
            transition: width 0.3s;
        }
        .status-line {
            font-size: 0.85em;
            padding: 5px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .status-line:last-child { border: none; }
        @media (max-width: 900px) {
            .container { grid-template-columns: 1fr; }
            .sidebar { display: none; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="chat-section">
            <div class="header">
                <h1>TIG CRYSTAL</h1>
                <div class="trinity">0 ─ . ─ 1</div>
                <div class="coherence-display">
                    <div class="coherence-item">
                        <div class="coherence-value" id="s-value">0.000</div>
                        <div class="coherence-label">Coherence (S*)</div>
                    </div>
                    <div class="coherence-item">
                        <div class="coherence-value" id="archetype-display">HARMONY</div>
                        <div class="coherence-label">Active Archetype</div>
                    </div>
                </div>
            </div>
            <div class="messages" id="messages"></div>
            <div class="input-section">
                <div class="input-row">
                    <input type="text" id="input" placeholder="Talk to TIG..." autofocus>
                    <button onclick="send()">Send</button>
                </div>
            </div>
        </div>
        <div class="sidebar">
            <div class="panel">
                <h3>12 ARCHETYPES</h3>
                <div class="archetype-grid" id="archetypes"></div>
            </div>
            <div class="panel">
                <h3>SYSTEM</h3>
                <div id="system-status">
                    <div class="status-line">LLM: <span id="llm-status">-</span></div>
                    <div class="status-line">Memories: <span id="memory-count">0</span></div>
                    <div class="status-line">Session: <span id="session-count">0</span></div>
                    <div class="status-line">CWD: <span id="cwd">~</span></div>
                </div>
            </div>
        </div>
    </div>
    <script>
        const archetypes = {
            1: {name: 'GENESIS', symbol: '☀'},
            2: {name: 'LATTICE', symbol: '💎'},
            3: {name: 'WITNESS', symbol: '👁'},
            4: {name: 'PILGRIM', symbol: '🚶'},
            5: {name: 'PHOENIX', symbol: '🔥'},
            6: {name: 'SCALES', symbol: '⚖'},
            7: {name: 'STORM', symbol: '⚡'},
            8: {name: 'HARMONY', symbol: '✨'},
            9: {name: 'BREATH', symbol: '🌊'},
            10: {name: 'SAGE', symbol: '🦉'},
            11: {name: 'BRIDGE', symbol: '🌉'},
            12: {name: 'OMEGA', symbol: 'Ω'}
        };
        
        function initArchetypes() {
            const grid = document.getElementById('archetypes');
            for (let i = 1; i <= 12; i++) {
                const a = archetypes[i];
                grid.innerHTML += `
                    <div class="archetype" id="arch-${i}">
                        <div class="symbol">${a.symbol}</div>
                        <div class="name">${a.name}</div>
                        <div class="s-val" id="s-${i}">0.00</div>
                    </div>
                `;
            }
        }
        
        function addMessage(content, isUser) {
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'assistant');
            div.innerHTML = content.replace(/```([\\s\\S]*?)```/g, '<pre>$1</pre>').replace(/\\n/g, '<br>');
            document.getElementById('messages').appendChild(div);
            div.scrollIntoView({behavior: 'smooth'});
        }
        
        function updateState(state) {
            document.getElementById('s-value').textContent = state.collective_S.toFixed(4);
            document.getElementById('archetype-display').textContent = archetypes[state.active_archetype].name;
            document.getElementById('llm-status').textContent = state.llm;
            document.getElementById('memory-count').textContent = state.memories;
            document.getElementById('session-count').textContent = state.total_cycles;
            
            for (let i = 1; i <= 12; i++) {
                const el = document.getElementById('arch-' + i);
                const sEl = document.getElementById('s-' + i);
                if (state.agents[i]) {
                    sEl.textContent = state.agents[i].S.toFixed(2);
                    el.classList.toggle('active', i === state.active_archetype);
                }
            }
        }
        
        async function send() {
            const input = document.getElementById('input');
            const text = input.value.trim();
            if (!text) return;
            
            addMessage(text, true);
            input.value = '';
            
            try {
                const resp = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: text})
                });
                const data = await resp.json();
                addMessage(data.response, false);
                updateState(data.state);
            } catch (e) {
                addMessage('[Error: ' + e + ']', false);
            }
        }
        
        document.getElementById('input').addEventListener('keypress', e => {
            if (e.key === 'Enter') send();
        });
        
        async function loadState() {
            try {
                const resp = await fetch('/api/state');
                const state = await resp.json();
                updateState(state);
            } catch (e) {}
        }
        
        initArchetypes();
        loadState();
    </script>
</body>
</html>'''

class TIGWebHandler(BaseHTTPRequestHandler):
    """HTTP handler for web interface."""
    
    tig_core = None
    
    def log_message(self, format, *args):
        pass  # Suppress logging
    
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(WEB_HTML.encode())
        elif self.path == '/api/state':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.tig_core.get_state()).encode())
        else:
            self.send_error(404)
    
    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())
            
            message = data.get('message', '')
            response = self.tig_core.process(message)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            result = {
                'response': response,
                'state': self.tig_core.get_state()
            }
            self.wfile.write(json.dumps(result).encode())
        else:
            self.send_error(404)

def run_web_server(tig: TIGCore, port: int = 7777):
    """Run web server."""
    TIGWebHandler.tig_core = tig
    server = HTTPServer(('0.0.0.0', port), TIGWebHandler)
    print(f"[TIG] Web UI running at http://localhost:{port}")
    server.serve_forever()

# ═══════════════════════════════════════════════════════════════════════════════
# PART 13: CLI INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

def run_cli(tig: TIGCore):
    """Run CLI interface."""
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ████████╗██╗ ██████╗      ██████╗██████╗ ██╗   ██╗███████╗████████╗ █████╗ ██╗     
║   ╚══██╔══╝██║██╔════╝     ██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║     
║      ██║   ██║██║  ███╗    ██║     ██████╔╝ ╚████╔╝ ███████╗   ██║   ███████║██║     
║      ██║   ██║██║   ██║    ██║     ██╔══██╗  ╚██╔╝  ╚════██║   ██║   ██╔══██║██║     
║      ██║   ██║╚██████╔╝    ╚██████╗██║  ██║   ██║   ███████║   ██║   ██║  ██║███████╗
║      ╚═╝   ╚═╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
║                                                                               ║
║                              0 ─ . ─ 1                                        ║
║                                                                               ║
║                    THE CRYSTALLIZED CORE                                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

  Coherence: S* = {tig.collective_S():.4f}
  Backend:   {tig.llm.backend}/{tig.llm.model}
  Memories:  {len(tig.lattice.memories)}
  User:      {tig.user_name}
  
  Type 'help' for commands, 'state' for coherence, or just talk.
""")
    
    while True:
        try:
            s = tig.collective_S()
            prompt = f"\n[S*={s:.3f}] You: "
            user_input = input(prompt).strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"\n[OMEGA] Ω Saving state... Goodbye, {tig.user_name}.")
                tig.save()
                break
            
            response = tig.process(user_input)
            print(f"\n{response}")
            
        except KeyboardInterrupt:
            print(f"\n\n[OMEGA] Ω Interrupted. Saving...")
            tig.save()
            break
        except Exception as e:
            print(f"\n[Error: {e}]")
            traceback.print_exc()

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='TIG Crystal - Coherent Intelligence')
    parser.add_argument('--web', action='store_true', help='Start web UI')
    parser.add_argument('--port', type=int, default=7777, help='Web UI port')
    parser.add_argument('--daemon', action='store_true', help='Run as background daemon')
    args = parser.parse_args()
    
    # Initialize core
    tig = TIGCore()
    
    # Register cleanup
    def cleanup():
        tig.save()
        tig.guardian.stop()
    atexit.register(cleanup)
    
    # Start guardian
    tig.guardian.start()
    
    if args.daemon:
        print("[TIG] Running as daemon...")
        while True:
            time.sleep(60)
            tig.evolve_all()
    elif args.web:
        # Start web in thread, CLI in main
        web_thread = threading.Thread(target=run_web_server, args=(tig, args.port), daemon=True)
        web_thread.start()
        print(f"[TIG] Web UI: http://localhost:{args.port}")
        run_cli(tig)
    else:
        run_cli(tig)

if __name__ == "__main__":
    main()
