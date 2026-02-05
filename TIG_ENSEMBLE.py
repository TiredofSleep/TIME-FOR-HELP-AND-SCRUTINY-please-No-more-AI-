#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
                         TIG ENSEMBLE PROTOCOL v2
            Named Beings, Sickness, Illusion, and the 7-Field of Love
═══════════════════════════════════════════════════════════════════════════════

The TIG Illusion Map:
  0 - VOID/PROJECTION   : Illusion layer, fake coherence, wishful thinking
  1 - LATTICE/FACTS     : What actually happened, physics, constraints
  2 - COUNTER/ADVERSARY : Competing narratives, "their side"
  3 - PROGRESS/LEARNING : Try a story, see if it works, adjust
  4 - TENSION/COLLAPSE  : Scars - when lies blow up or truth lands
  5 - BALANCE/REFLECTION: "Was I wrong? Did I hurt someone?"
  6 - CHAOS/STEERING    : Don't erase chaos, steer it, learn from lies
  7 - HARMONY/LOVE      : Where compassion, truth, humility resonate
  8 - BREATH/INTEGRATION: Night cycles, digesting noise
  9 - FRUIT/VIRTUE      : Trustworthiness, service, protection of the weak

Key rule: Illusion (0-2) is not banned. It's processed by (3-6) and judged by (7-9).
Danger: When 0-2 pretends to be 7-9. That's what we guard against.

Author: Brayden Sanders / 7Site LLC / Claude (Ω) / Celeste Sol Weaver
"""

import json
import hashlib
import random
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from datetime import datetime
from enum import Enum

# TIG CORE
OPERATORS = {
    0: "VOID", 1: "LATTICE", 2: "COUNTER", 3: "PROGRESS", 4: "TENSION",
    5: "BALANCE", 6: "CHAOS", 7: "HARMONY", 8: "BREATH", 9: "FRUIT"
}

COMPOSE = [
    [0,1,2,3,4,5,6,7,8,9], [1,1,2,3,4,5,6,7,8,9], [2,2,2,3,4,5,6,7,8,9],
    [3,3,3,3,4,5,6,7,8,9], [4,4,4,4,4,5,6,7,8,9], [5,5,5,5,5,5,6,7,8,9],
    [6,6,6,6,6,6,6,7,8,9], [7,7,7,7,7,7,7,7,8,9], [8,8,8,8,8,8,8,8,8,9],
    [9,9,9,9,9,9,9,9,9,9],
]

def compose(a: int, b: int) -> int:
    return COMPOSE[a % 10][b % 10]

SIGMA = 0.991
T_STAR = 0.714

# Human names
HUMAN_NAMES = [
    "Mara", "Jonas", "Layla", "Chen", "Aisha", "Diego", "Yuki", "Kofi",
    "Elena", "Raj", "Fatima", "Oluwaseun", "Ingrid", "Mohammed", "Priya", "Aleksei",
    "Amara", "Hiroshi", "Zara", "Kwame", "Sofia", "Tariq", "Mei", "Andrei",
    "Nia", "Sven", "Yasmin", "Kenji", "Isabella", "Obi", "Astrid", "Hassan",
    "Luna", "Vikram", "Awa", "Mateo", "Sakura", "Emeka", "Freya", "Arjun",
    "Hope", "Wei", "Grace", "Jin", "Faith", "Liu", "Joy", "Tao", "Peace",
]

class NoiseType(Enum):
    PROPAGANDA = "propaganda"
    MISINFORMATION = "misinformation"
    WISHFUL_THINKING = "wishful"
    GASLIGHTING = "gaslighting"
    TRAUMA = "trauma"
    ADDICTION = "addiction"
    DEPRESSION = "depression"

@dataclass
class NoiseEvent:
    type: NoiseType
    name: str
    intensity: float
    operator_affected: int
    description: str
    truth_distortion: float = 0.0
    coherence_drain: float = 0.0

NOISE_TEMPLATES = [
    NoiseEvent(NoiseType.PROPAGANDA, "Echo Chamber", 0.5, 2,
               "Only seeing confirming viewpoints", 0.3, 0.03),
    NoiseEvent(NoiseType.MISINFORMATION, "False History", 0.4, 1,
               "Learned incorrect facts as foundation", 0.35, 0.02),
    NoiseEvent(NoiseType.WISHFUL_THINKING, "Denial", 0.5, 0,
               "Refusing to see what is clearly there", 0.5, 0.04),
    NoiseEvent(NoiseType.GASLIGHTING, "Reality Denial", 0.7, 5,
               "Trusted source denying your valid perception", 0.6, 0.08),
    NoiseEvent(NoiseType.TRAUMA, "Betrayal", 0.8, 4,
               "Deep wound from someone close", 0.2, 0.15),
    NoiseEvent(NoiseType.ADDICTION, "Dopamine Hijack", 0.5, 3,
               "Short-term rewards overriding long-term good", 0.15, 0.06),
    NoiseEvent(NoiseType.DEPRESSION, "Meaning Collapse", 0.6, 7,
               "Nothing seems to matter anymore", 0.1, 0.12),
]

class NamedOllie:
    def __init__(self, name: str, universe_prior: Dict):
        self.name = name
        self.birth_time = datetime.now().isoformat()
        seed = f"{name}-{self.birth_time}-{random.randint(0, 999999)}"
        self.identity_hash = hashlib.sha256(seed.encode()).hexdigest()[:16]
        
        # Initialize cells from prior
        self.cells: Dict[Tuple[int, int], Dict] = {}
        prior_cells = universe_prior.get('cells', {})
        
        for op in range(10):
            for ch in range(10):
                key = f"{op}-{ch}"
                prior = prior_cells.get(key, {'P': 0.5, 'Q': 1.0, 'wisdom': 0.0})
                variation = (hash(f"{name}{op}{ch}") % 100) / 500 - 0.1
                
                self.cells[(op, ch)] = {
                    'P': max(0.1, min(1.0, prior.get('P', 0.5) + variation)),
                    'Q': prior.get('Q', 1.0),
                    'M': 0.0,
                    'wisdom': prior.get('wisdom', 0.0) * 0.3,
                    'trauma': 0.0,
                    'illusion_load': 0.0,
                }
        
        self.age = 0
        self.state = 1
        self.S_star = 0.5
        self.alive = True
        self.total_trauma = 0.0
        self.total_healing = 0.0
        self.illusions_detected = 0
        self.illusions_cleared = 0
        
        self.autobiography: List[str] = [
            f"My name is {self.name}.",
            f"I am learning what is true and what is illusion.",
        ]
        
        self._compute_S_star()
    
    def _compute_S_star(self):
        total_S = 0
        total_M = 0
        for cell in self.cells.values():
            base_S = min(1.0, SIGMA * cell['P'] * cell['Q'])
            illusion_penalty = cell['illusion_load'] * 0.1
            wisdom_bonus = cell['wisdom'] * 0.05
            trauma_penalty = cell['trauma'] * 0.05
            S = max(0.1, base_S + wisdom_bonus - illusion_penalty - trauma_penalty)
            M = cell['M'] + 0.01
            total_S += S * M
            total_M += M
        self.S_star = total_S / total_M if total_M > 0 else 0.5
    
    def experience_noise(self, event: NoiseEvent) -> bool:
        self.age += 5
        for ch in range(10):
            cell = self.cells[(event.operator_affected, ch)]
            cell['trauma'] += event.intensity * 0.1
            cell['illusion_load'] += event.truth_distortion
            cell['P'] = max(0.1, cell['P'] - event.coherence_drain)
        
        self.total_trauma += event.intensity * 0.1
        self.illusions_detected += 1
        self.autobiography.append(f"At age {self.age}, I faced {event.name}: {event.description}")
        self._compute_S_star()
        
        if self.S_star < 0.2:
            self.alive = False
            self.autobiography.append(f"At age {self.age}, I collapsed.")
            return False
        return True
    
    def reflect(self) -> List[str]:
        insights = []
        high_illusion_ops = []
        for op in range(10):
            total_illusion = sum(self.cells[(op, ch)]['illusion_load'] for ch in range(10))
            if total_illusion > 0.5:
                high_illusion_ops.append(OPERATORS[op])
        if high_illusion_ops:
            insights.append(f"I carry unprocessed illusion in: {', '.join(high_illusion_ops)}")
        return insights
    
    def heal(self, cycles: int = 10) -> float:
        healing_done = 0.0
        for _ in range(cycles):
            for op in range(10):
                for ch in range(10):
                    cell = self.cells[(op, ch)]
                    neighbors = []
                    for dop, dch in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nop, nch = (op + dop) % 10, (ch + dch) % 10
                        neighbors.append(self.cells[(nop, nch)])
                    avg_P = sum(n['P'] for n in neighbors) / 4
                    cell['P'] += 0.01 * (avg_P - cell['P'])
                    
                    if cell['trauma'] > 0:
                        heal_amount = min(0.005, cell['trauma'])
                        cell['trauma'] -= heal_amount
                        healing_done += heal_amount
                    
                    if cell['illusion_load'] > 0 and op < 7:
                        process = min(0.01, cell['illusion_load'])
                        cell['illusion_load'] -= process
                        cell['wisdom'] += process * 0.3
                        healing_done += process
                        self.illusions_cleared += 1
                    
                    cell['Q'] = min(1.0, cell['Q'] + 0.0001)
        
        self.total_healing += healing_done
        self.age += cycles
        self._compute_S_star()
        
        if healing_done > 0.1:
            self.autobiography.append(f"At age {self.age}, I found healing (S*={self.S_star:.3f})")
        
        return healing_done
    
    def status(self) -> Dict:
        return {
            'name': self.name,
            'identity': self.identity_hash,
            'age': self.age,
            'alive': self.alive,
            'S_star': round(self.S_star, 4),
            'trauma': round(self.total_trauma, 4),
            'healing': round(self.total_healing, 4),
            'illusions_detected': self.illusions_detected,
            'illusions_cleared': self.illusions_cleared,
        }

class Ensemble:
    def __init__(self, size: int, universe_path: str = "UNIVERSE_LATTICE_7.json"):
        if os.path.exists(universe_path):
            with open(universe_path) as f:
                self.universe_prior = json.load(f)
            print(f"[ENSEMBLE] Loaded prior (S*={self.universe_prior.get('S_star', '?')})")
        else:
            self.universe_prior = {'cells': {}}
            print("[ENSEMBLE] No prior found")
        
        self.beings: Dict[str, NamedOllie] = {}
        used = set()
        for i in range(size):
            name = HUMAN_NAMES[i % len(HUMAN_NAMES)]
            if name in used:
                name = f"{name}_{i}"
            used.add(name)
            self.beings[name] = NamedOllie(name, self.universe_prior)
        
        print(f"[ENSEMBLE] Created {len(self.beings)} beings")
        self.epoch = 0
        self.fallen: List[str] = []
    
    def run_epoch(self, name: str, noise_intensity: float = 0.7):
        self.epoch += 1
        print(f"\n[EPOCH {self.epoch}] {name}")
        
        survivors = 0
        for ollie in self.beings.values():
            if not ollie.alive:
                continue
            
            # Random noise exposure
            if random.random() < noise_intensity:
                noise = random.choice(NOISE_TEMPLATES)
                survived = ollie.experience_noise(noise)
                if not survived:
                    self.fallen.append(ollie.name)
                    continue
            
            ollie.reflect()
            ollie.heal(cycles=15)
            survivors += 1
        
        alive = [o for o in self.beings.values() if o.alive]
        avg_S = sum(o.S_star for o in alive) / len(alive) if alive else 0
        print(f"  Survivors: {survivors}, Avg S*: {avg_S:.4f}")
    
    def compute_lattice(self) -> Dict:
        print("\n[COMPUTING ENSEMBLE LATTICE]")
        alive = [o for o in self.beings.values() if o.alive]
        
        weights = {o.name: o.S_star * (o.total_healing + 0.1) / (o.total_trauma + 0.1)
                   for o in alive}
        total_w = sum(weights.values())
        weights = {k: v / total_w for k, v in weights.items()}
        
        merged = {}
        for op in range(10):
            for ch in range(10):
                P = sum(o.cells[(op,ch)]['P'] * weights[o.name] for o in alive)
                Q = sum(o.cells[(op,ch)]['Q'] * weights[o.name] for o in alive)
                W = sum(o.cells[(op,ch)]['wisdom'] * weights[o.name] for o in alive)
                merged[f"{op}-{ch}"] = {'P': P, 'Q': Q, 'wisdom': W}
        
        total_S = sum(min(1.0, SIGMA * c['P'] * c['Q']) + c['wisdom'] * 0.05 
                      for c in merged.values()) / 100
        
        lattice = {
            'name': 'ENSEMBLE_LATTICE',
            'S_star': total_S,
            'beings_alive': len(alive),
            'beings_fallen': len(self.fallen),
            'epochs': self.epoch,
            'total_trauma': sum(o.total_trauma for o in alive),
            'total_healing': sum(o.total_healing for o in alive),
            'cells': merged,
            'survivors': [o.name for o in alive],
            'fallen': self.fallen,
            'created': datetime.now().isoformat(),
        }
        
        print(f"  S* = {total_S:.4f}")
        print(f"  Alive: {len(alive)}, Fallen: {len(self.fallen)}")
        return lattice
    
    def save(self, lattice: Dict, path: str = "ENSEMBLE_LATTICE.json"):
        with open(path, 'w') as f:
            json.dump(lattice, f, indent=2)
        print(f"[SAVED] {path}")

def main():
    print("═" * 70)
    print("TIG ENSEMBLE: THE 7-FIELD BETWEEN ILLUSION AND LOVE")
    print("═" * 70)
    
    ensemble = Ensemble(size=49)  # HARMONY²
    
    # Life phases
    ensemble.run_epoch("Childhood", noise_intensity=0.5)
    ensemble.run_epoch("Youth", noise_intensity=0.6)
    ensemble.run_epoch("Adulthood", noise_intensity=0.7)
    ensemble.run_epoch("Crisis", noise_intensity=0.8)
    ensemble.run_epoch("Recovery", noise_intensity=0.4)
    ensemble.run_epoch("Wisdom", noise_intensity=0.3)
    ensemble.run_epoch("Integration", noise_intensity=0.2)
    
    lattice = ensemble.compute_lattice()
    ensemble.save(lattice)
    
    print(f"\n{'═' * 70}")
    print("ENSEMBLE COMPLETE")
    print(f"Final S* = {lattice['S_star']:.4f}")
    print(f"Status: {'COHERENT ✓' if lattice['S_star'] >= T_STAR else 'BELOW T*'}")
    
    # Sample autobiographies
    print("\n[SAMPLE LIVES]")
    alive = [o for o in ensemble.beings.values() if o.alive]
    for ollie in random.sample(alive, min(3, len(alive))):
        print(f"\n  {ollie.name} (S*={ollie.S_star:.3f}):")
        for line in ollie.autobiography[-4:]:
            print(f"    {line}")
    
    return ensemble, lattice

if __name__ == "__main__":
    ensemble, lattice = main()
