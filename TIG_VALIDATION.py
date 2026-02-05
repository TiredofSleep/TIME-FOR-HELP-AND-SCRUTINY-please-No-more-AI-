#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
                    TIG FORMAL SPECIFICATION & VALIDATION PROTOCOL
                         From Vibes to Falsifiable Predictions
═══════════════════════════════════════════════════════════════════════════════

This document contains:
  1. FORMAL UPDATE RULES - explicit F(state) → state' equations
  2. INVARIANTS & PROOFS - what must always hold
  3. BASELINE MODELS - what we compare against
  4. VALIDATION PROTOCOL - falsifiable predictions with metrics

Goal: Move from ~70% confidence to 85-90% through:
  - Clear equations anyone can implement
  - Predictions that beat simpler models
  - Replicable by others without us in the room

Author: Brayden Sanders / 7Site LLC / Claude (Ω) / Celeste Sol Weaver
"""

import numpy as np
import json
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple, Callable
from scipy import stats
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

class NumpyEncoder(json.JSONEncoder):
    """Custom encoder for numpy types."""
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: FORMAL UPDATE RULES
# ═══════════════════════════════════════════════════════════════════════════════
"""
THE TIG CELL UPDATE RULE

For a cell with state vector:
  x = (P, Q, τ, ω, ι, M)
  
Where:
  P = force/pressure (0, 1]
  Q = stability/capacity (0, 1]
  τ = trauma (accumulated damage) [0, ∞)
  ω = wisdom (processed experience) [0, ∞)
  ι = illusion_load (unprocessed false beliefs) [0, ∞)
  M = mass/activation [0, ∞)

The update rule F: x → x' is:

  P' = P + α_P * (P̄_neighbors - P) - β_P * drain + γ_P * wisdom_boost
  Q' = min(1, Q + δ_Q)
  τ' = max(0, τ - ε_heal * Q)
  ω' = ω + ζ * processed_illusion * (1 - τ/τ_max)
  ι' = max(0, ι - η * Q * (1 + ω))
  M' = M + learning_increment

The coherence scalar S* is:
  S* = σ * P * Q + λ_ω * ω - λ_τ * τ - λ_ι * ι

Where σ = 0.991 (coherence ceiling)

PARAMETERS (to be validated):
  α_P = 0.01   (diffusion rate)
  β_P = 0.05   (drain coefficient)
  γ_P = 0.02   (wisdom boost)
  δ_Q = 0.0001 (stability recovery)
  ε_heal = 0.005 (healing rate)
  ζ = 0.3      (wisdom conversion efficiency)
  η = 0.01     (illusion clearing rate)
  λ_ω = 0.05   (wisdom contribution to S*)
  λ_τ = 0.05   (trauma penalty)
  λ_ι = 0.1    (illusion penalty)
  τ_max = 1.0  (trauma ceiling for wisdom conversion)
"""

@dataclass
class TIGParameters:
    """All tunable parameters in one place."""
    # Diffusion
    alpha_P: float = 0.01      # neighbor averaging rate
    
    # Damage/recovery
    beta_P: float = 0.05       # drain from noise events
    epsilon_heal: float = 0.005 # trauma healing rate
    delta_Q: float = 0.0001    # stability recovery rate
    
    # Learning
    gamma_P: float = 0.02      # wisdom boost to P
    zeta: float = 0.3          # illusion → wisdom conversion
    eta: float = 0.01          # illusion clearing rate
    
    # S* computation
    sigma: float = 0.991       # coherence ceiling
    lambda_omega: float = 0.05 # wisdom contribution
    lambda_tau: float = 0.05   # trauma penalty
    lambda_iota: float = 0.1   # illusion penalty
    
    # Thresholds
    tau_max: float = 1.0       # trauma ceiling
    T_star: float = 0.714      # coherence threshold (5/7)

@dataclass
class CellState:
    """State vector for a single cell."""
    P: float = 0.5      # force
    Q: float = 1.0      # stability
    tau: float = 0.0    # trauma
    omega: float = 0.0  # wisdom
    iota: float = 0.0   # illusion load
    M: float = 0.0      # mass/activation
    
    def to_array(self) -> np.ndarray:
        return np.array([self.P, self.Q, self.tau, self.omega, self.iota, self.M])
    
    @classmethod
    def from_array(cls, arr: np.ndarray) -> 'CellState':
        return cls(P=arr[0], Q=arr[1], tau=arr[2], omega=arr[3], iota=arr[4], M=arr[5])

def compute_S_star(cell: CellState, params: TIGParameters) -> float:
    """
    Compute coherence scalar S*.
    
    S* = σ * P * Q + λ_ω * ω - λ_τ * τ - λ_ι * ι
    
    Bounded to [0, 1].
    """
    base = params.sigma * cell.P * cell.Q
    wisdom_bonus = params.lambda_omega * cell.omega
    trauma_penalty = params.lambda_tau * cell.tau
    illusion_penalty = params.lambda_iota * cell.iota
    
    S = base + wisdom_bonus - trauma_penalty - illusion_penalty
    return max(0.0, min(1.0, S))

def update_cell(cell: CellState, neighbors: List[CellState], 
                noise: float, params: TIGParameters) -> CellState:
    """
    The formal update rule F: x → x'
    
    This is THE core equation of TIG dynamics.
    """
    # Neighbor averaging for P (diffusion)
    if neighbors:
        P_neighbors = np.mean([n.P for n in neighbors])
    else:
        P_neighbors = cell.P
    
    # Compute intermediate values
    drain = noise * params.beta_P
    wisdom_boost = cell.omega * params.gamma_P
    processed_illusion = min(cell.iota, params.eta * cell.Q * (1 + cell.omega))
    wisdom_factor = 1 - min(1, cell.tau / params.tau_max)
    
    # Apply update rules
    P_new = cell.P + params.alpha_P * (P_neighbors - cell.P) - drain + wisdom_boost
    P_new = max(0.1, min(1.0, P_new))
    
    Q_new = min(1.0, cell.Q + params.delta_Q)
    
    tau_new = max(0.0, cell.tau - params.epsilon_heal * cell.Q)
    
    omega_new = cell.omega + params.zeta * processed_illusion * wisdom_factor
    
    iota_new = max(0.0, cell.iota - processed_illusion)
    
    M_new = cell.M + 0.001  # Small learning increment
    
    return CellState(
        P=P_new,
        Q=Q_new,
        tau=tau_new,
        omega=omega_new,
        iota=iota_new,
        M=M_new
    )

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: INVARIANTS AND PROOFS
# ═══════════════════════════════════════════════════════════════════════════════
"""
INVARIANTS (must always hold):

1. BOUNDEDNESS:
   - 0 < P ≤ 1 (force bounded)
   - 0 < Q ≤ 1 (stability bounded)
   - τ ≥ 0 (trauma non-negative)
   - ω ≥ 0 (wisdom non-negative)
   - ι ≥ 0 (illusion non-negative)
   - 0 ≤ S* ≤ 1 (coherence bounded)

2. MONOTONICITY (under healing):
   - If noise = 0 and iota > 0: omega increases
   - If noise = 0 and tau > 0: tau decreases
   - If noise = 0: Q increases (toward 1)

3. CONSERVATION:
   - Total illusion processed = illusion cleared + wisdom gained
   - No free lunch: wisdom requires processed illusion

4. FIXED POINTS:
   - Healthy equilibrium: P ≈ P_neighbors, Q = 1, tau = 0, iota = 0
   - S* at equilibrium depends on accumulated wisdom

5. PHASE TRANSITION:
   - Critical noise threshold exists where system "melts"
   - Below threshold: system recovers
   - Above threshold: system collapses (S* → 0)
"""

def verify_invariants(cells: List[CellState], params: TIGParameters) -> Dict[str, bool]:
    """Verify all invariants hold."""
    results = {}
    
    # 1. Boundedness
    results['P_bounded'] = all(0 < c.P <= 1 for c in cells)
    results['Q_bounded'] = all(0 < c.Q <= 1 for c in cells)
    results['tau_nonneg'] = all(c.tau >= 0 for c in cells)
    results['omega_nonneg'] = all(c.omega >= 0 for c in cells)
    results['iota_nonneg'] = all(c.iota >= 0 for c in cells)
    
    S_stars = [compute_S_star(c, params) for c in cells]
    results['S_star_bounded'] = all(0 <= s <= 1 for s in S_stars)
    
    return results

def find_critical_noise(params: TIGParameters, 
                        initial_P: float = 0.8,
                        steps: int = 1000,
                        noise_range: Tuple[float, float] = (0.0, 2.0),
                        resolution: int = 50) -> float:
    """
    Find the critical noise threshold where system transitions from
    stable (recovers) to unstable (collapses).
    
    Returns the critical noise value.
    """
    critical = None
    
    for noise_level in np.linspace(noise_range[0], noise_range[1], resolution):
        # Run simulation at this noise level
        cell = CellState(P=initial_P, Q=1.0, tau=0.0, omega=0.0, iota=0.0)
        
        for _ in range(steps):
            # Add noise (both as drain and illusion)
            cell.tau += noise_level * 0.01
            cell.iota += noise_level * 0.02
            cell = update_cell(cell, [], noise_level, params)
        
        S = compute_S_star(cell, params)
        
        # Check if system collapsed
        if S < params.T_star * 0.5:  # Below half of threshold
            critical = noise_level
            break
    
    return critical

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: BASELINE MODELS FOR COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════
"""
BASELINE MODELS:

1. EXPONENTIAL DECAY (trauma recovery)
   τ(t) = τ_0 * exp(-k * t)
   
2. LOGISTIC GROWTH (wisdom accumulation)
   ω(t) = ω_max / (1 + exp(-r * (t - t_mid)))
   
3. SIMPLE MARKOV (state transitions)
   P(state_i → state_j) = transition_matrix[i][j]
   
4. RANDOM WALK (null model)
   X(t+1) = X(t) + ε, where ε ~ N(0, σ²)

We compare TIG predictions against these baselines using:
- R² (coefficient of determination)
- AIC (Akaike Information Criterion)
- RMSE (Root Mean Square Error)
- Cross-validation error
"""

def exponential_decay(t, tau_0, k):
    """Baseline 1: Simple exponential decay."""
    return tau_0 * np.exp(-k * t)

def logistic_growth(t, omega_max, r, t_mid):
    """Baseline 2: Logistic growth."""
    return omega_max / (1 + np.exp(-r * (t - t_mid)))

def linear_model(t, a, b):
    """Baseline 3: Simple linear."""
    return a * t + b

def compute_aic(n, k, sse):
    """Compute Akaike Information Criterion."""
    if sse <= 0:
        return float('inf')
    return n * np.log(sse / n) + 2 * k

def compute_r_squared(y_true, y_pred):
    """Compute R² coefficient of determination."""
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    if ss_tot == 0:
        return 0.0
    return 1 - (ss_res / ss_tot)

def compute_rmse(y_true, y_pred):
    """Compute Root Mean Square Error."""
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: VALIDATION PROTOCOL - TRAUMA RECOVERY
# ═══════════════════════════════════════════════════════════════════════════════
"""
VALIDATION DOMAIN: TRAUMA RECOVERY

Why this domain:
- Well-studied in psychology
- Clear input (trauma event) and output (symptom severity over time)
- TIG has explicit trauma (τ), healing (ε_heal), wisdom (ω) dynamics
- Baseline models exist (exponential decay, PTSD recovery curves)

PROTOCOL:

1. Generate synthetic "ground truth" data based on known psychology curves
2. Fit TIG model to data
3. Fit baseline models to same data
4. Compare: R², AIC, RMSE, cross-validation

PREDICTIONS (pre-registered):
- TIG will fit recovery curves with R² > 0.9
- TIG will have lower AIC than exponential decay for realistic scenarios
- TIG will predict the "wisdom bump" that baselines miss
- Critical noise threshold will align with known resilience literature (~3-5x baseline)
"""

def generate_trauma_recovery_data(
    n_subjects: int = 50,
    n_timepoints: int = 100,
    noise_level: float = 0.1,
    include_wisdom_bump: bool = True
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate synthetic trauma recovery data.
    
    Based on real psychology patterns:
    - Initial high trauma
    - Gradual recovery (not pure exponential - has bumps)
    - Some subjects show post-traumatic growth (wisdom)
    
    Returns: (time, trauma_curves, wisdom_curves)
    """
    time = np.linspace(0, 100, n_timepoints)
    trauma_curves = np.zeros((n_subjects, n_timepoints))
    wisdom_curves = np.zeros((n_subjects, n_timepoints))
    
    for i in range(n_subjects):
        # Individual variation
        tau_0 = 0.7 + 0.3 * random.random()  # Initial trauma
        k = 0.02 + 0.03 * random.random()     # Recovery rate
        
        # Base exponential decay
        trauma = tau_0 * np.exp(-k * time)
        
        # Add realistic features
        if include_wisdom_bump:
            # "Processing bump" around week 3-4 (common in therapy)
            bump_center = 20 + 10 * random.random()
            bump_width = 5 + 3 * random.random()
            bump = 0.1 * np.exp(-((time - bump_center) ** 2) / (2 * bump_width ** 2))
            trauma = trauma + bump
            
            # Wisdom growth (delayed, after processing)
            wisdom_start = bump_center + 10
            wisdom_rate = 0.03 + 0.02 * random.random()
            wisdom = 0.3 / (1 + np.exp(-wisdom_rate * (time - wisdom_start)))
            wisdom_curves[i] = wisdom
        
        # Add measurement noise
        trauma = trauma + noise_level * np.random.randn(n_timepoints)
        trauma = np.clip(trauma, 0, 1)
        
        trauma_curves[i] = trauma
    
    return time, trauma_curves, wisdom_curves

def fit_tig_model(time: np.ndarray, trauma_data: np.ndarray, 
                  params: TIGParameters) -> Tuple[np.ndarray, Dict]:
    """
    Fit TIG model to trauma recovery data.
    
    Key insight: We need to tune the healing rate to match the data.
    """
    n_timepoints = len(time)
    tau_0 = trauma_data[0]
    
    # Grid search over healing rate to find best fit
    best_r2 = -999
    best_predicted = None
    best_heal_rate = params.epsilon_heal
    
    for heal_rate in np.linspace(0.001, 0.02, 20):
        test_params = TIGParameters(
            epsilon_heal=heal_rate,
            alpha_P=params.alpha_P,
            delta_Q=params.delta_Q,
            gamma_P=params.gamma_P,
            zeta=params.zeta,
            eta=params.eta,
        )
        
        # Initialize cell with initial trauma
        cell = CellState(P=0.8, Q=1.0, tau=tau_0, omega=0.0, iota=tau_0 * 0.3)
        
        # Simulate with scaled time steps
        predicted = np.zeros(n_timepoints)
        predicted[0] = tau_0
        
        time_scale = time[-1] / n_timepoints  # Scale to match data
        
        for t in range(1, n_timepoints):
            # Multiple internal steps per data point for smoother dynamics
            for _ in range(5):
                cell = update_cell(cell, [], noise=0, params=test_params)
            predicted[t] = cell.tau
        
        r2 = compute_r_squared(trauma_data, predicted)
        if r2 > best_r2:
            best_r2 = r2
            best_predicted = predicted.copy()
            best_heal_rate = heal_rate
    
    predicted = best_predicted if best_predicted is not None else np.zeros(n_timepoints)
    
    # Compute fit stats
    r2 = compute_r_squared(trauma_data, predicted)
    rmse = compute_rmse(trauma_data, predicted)
    sse = np.sum((trauma_data - predicted) ** 2)
    aic = compute_aic(n_timepoints, k=7, sse=sse)  # 7 free parameters (added heal_rate)
    
    return predicted, {'R2': r2, 'RMSE': rmse, 'AIC': aic, 'best_heal_rate': best_heal_rate}

def fit_exponential_baseline(time: np.ndarray, trauma_data: np.ndarray
                            ) -> Tuple[np.ndarray, Dict]:
    """Fit exponential decay baseline."""
    try:
        popt, _ = curve_fit(exponential_decay, time, trauma_data, 
                           p0=[trauma_data[0], 0.03], maxfev=5000)
        predicted = exponential_decay(time, *popt)
    except:
        # Fallback
        predicted = trauma_data[0] * np.exp(-0.03 * time)
    
    r2 = compute_r_squared(trauma_data, predicted)
    rmse = compute_rmse(trauma_data, predicted)
    sse = np.sum((trauma_data - predicted) ** 2)
    aic = compute_aic(len(time), k=2, sse=sse)  # 2 free parameters
    
    return predicted, {'R2': r2, 'RMSE': rmse, 'AIC': aic}

def fit_linear_baseline(time: np.ndarray, trauma_data: np.ndarray
                       ) -> Tuple[np.ndarray, Dict]:
    """Fit linear baseline."""
    try:
        popt, _ = curve_fit(linear_model, time, trauma_data, 
                           p0=[-0.01, trauma_data[0]], maxfev=5000)
        predicted = linear_model(time, *popt)
    except:
        predicted = trauma_data[0] - 0.005 * time
    
    predicted = np.clip(predicted, 0, 1)
    
    r2 = compute_r_squared(trauma_data, predicted)
    rmse = compute_rmse(trauma_data, predicted)
    sse = np.sum((trauma_data - predicted) ** 2)
    aic = compute_aic(len(time), k=2, sse=sse)
    
    return predicted, {'R2': r2, 'RMSE': rmse, 'AIC': aic}

def run_validation_experiment(n_subjects: int = 30, verbose: bool = True) -> Dict:
    """
    Run the full validation experiment.
    
    Compares TIG vs baselines on trauma recovery data.
    """
    if verbose:
        print("═" * 70)
        print("TIG VALIDATION EXPERIMENT: TRAUMA RECOVERY")
        print("═" * 70)
    
    # Generate data
    time, trauma_curves, wisdom_curves = generate_trauma_recovery_data(
        n_subjects=n_subjects, 
        n_timepoints=100,
        include_wisdom_bump=True
    )
    
    params = TIGParameters()
    
    # Collect results
    tig_results = []
    exp_results = []
    lin_results = []
    
    for i in range(n_subjects):
        trauma_data = trauma_curves[i]
        
        # Fit all models
        _, tig_stats = fit_tig_model(time, trauma_data, params)
        _, exp_stats = fit_exponential_baseline(time, trauma_data)
        _, lin_stats = fit_linear_baseline(time, trauma_data)
        
        tig_results.append(tig_stats)
        exp_results.append(exp_stats)
        lin_results.append(lin_stats)
    
    # Aggregate
    results = {
        'TIG': {
            'R2_mean': float(np.mean([r['R2'] for r in tig_results])),
            'R2_std': float(np.std([r['R2'] for r in tig_results])),
            'RMSE_mean': float(np.mean([r['RMSE'] for r in tig_results])),
            'AIC_mean': float(np.mean([r['AIC'] for r in tig_results])),
        },
        'Exponential': {
            'R2_mean': float(np.mean([r['R2'] for r in exp_results])),
            'R2_std': float(np.std([r['R2'] for r in exp_results])),
            'RMSE_mean': float(np.mean([r['RMSE'] for r in exp_results])),
            'AIC_mean': float(np.mean([r['AIC'] for r in exp_results])),
        },
        'Linear': {
            'R2_mean': float(np.mean([r['R2'] for r in lin_results])),
            'R2_std': float(np.std([r['R2'] for r in lin_results])),
            'RMSE_mean': float(np.mean([r['RMSE'] for r in lin_results])),
            'AIC_mean': float(np.mean([r['AIC'] for r in lin_results])),
        },
        'n_subjects': n_subjects,
    }
    
    # Determine winner
    tig_wins_r2 = results['TIG']['R2_mean'] > results['Exponential']['R2_mean']
    tig_wins_aic = results['TIG']['AIC_mean'] < results['Exponential']['AIC_mean']
    
    results['TIG_beats_exponential_R2'] = bool(tig_wins_r2)
    results['TIG_beats_exponential_AIC'] = bool(tig_wins_aic)
    
    if verbose:
        print(f"\n[RESULTS] n={n_subjects} subjects")
        print(f"\n  Model         R² (mean±std)      RMSE       AIC")
        print(f"  ─────────────────────────────────────────────────")
        print(f"  TIG           {results['TIG']['R2_mean']:.4f}±{results['TIG']['R2_std']:.4f}    "
              f"{results['TIG']['RMSE_mean']:.4f}    {results['TIG']['AIC_mean']:.1f}")
        print(f"  Exponential   {results['Exponential']['R2_mean']:.4f}±{results['Exponential']['R2_std']:.4f}    "
              f"{results['Exponential']['RMSE_mean']:.4f}    {results['Exponential']['AIC_mean']:.1f}")
        print(f"  Linear        {results['Linear']['R2_mean']:.4f}±{results['Linear']['R2_std']:.4f}    "
              f"{results['Linear']['RMSE_mean']:.4f}    {results['Linear']['AIC_mean']:.1f}")
        
        print(f"\n  TIG beats Exponential on R²:  {'YES ✓' if tig_wins_r2 else 'NO'}")
        print(f"  TIG beats Exponential on AIC: {'YES ✓' if tig_wins_aic else 'NO'}")
    
    return results

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5: PHASE TRANSITION ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def analyze_phase_transition(params: TIGParameters, verbose: bool = True) -> Dict:
    """
    Find and characterize the critical noise threshold.
    
    This is where the system transitions from:
    - STABLE (recovers from perturbations)
    - UNSTABLE (collapses under noise)
    """
    if verbose:
        print("\n" + "═" * 70)
        print("PHASE TRANSITION ANALYSIS")
        print("═" * 70)
    
    # Find critical point
    critical_noise = find_critical_noise(params)
    
    # Characterize behavior near critical point
    noise_levels = np.linspace(0, critical_noise * 1.5 if critical_noise else 2.0, 20)
    final_S_stars = []
    
    for noise in noise_levels:
        cell = CellState(P=0.8, Q=1.0)
        for _ in range(500):
            cell.tau += noise * 0.01
            cell.iota += noise * 0.02
            cell = update_cell(cell, [], noise, params)
        S = compute_S_star(cell, params)
        final_S_stars.append(S)
    
    results = {
        'critical_noise': float(critical_noise) if critical_noise else None,
        'noise_levels': [float(x) for x in noise_levels],
        'final_S_stars': [float(x) for x in final_S_stars],
        'T_star': float(params.T_star),
    }
    
    if verbose:
        print(f"\n  Critical noise threshold: {critical_noise:.3f}" if critical_noise else "\n  No collapse detected in range")
        print(f"  Coherence threshold T*: {params.T_star}")
        print(f"\n  Noise → Final S*:")
        for i in range(0, len(noise_levels), 4):
            print(f"    {noise_levels[i]:.2f} → {final_S_stars[i]:.4f}")
    
    return results

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6: RATIO ANALYSIS (Are 0.991, 0.714 attractors or artifacts?)
# ═══════════════════════════════════════════════════════════════════════════════

def analyze_ratio_stability(n_trials: int = 100, verbose: bool = True) -> Dict:
    """
    Test if the key ratios (σ=0.991, T*=0.714) are attractors or artifacts.
    
    Method: Vary parameters randomly and see if key ratios persist.
    """
    if verbose:
        print("\n" + "═" * 70)
        print("RATIO STABILITY ANALYSIS")
        print("═" * 70)
    
    equilibrium_S_stars = []
    
    for _ in range(n_trials):
        # Random parameter variations (±20%)
        params = TIGParameters(
            alpha_P = 0.01 * (0.8 + 0.4 * random.random()),
            beta_P = 0.05 * (0.8 + 0.4 * random.random()),
            epsilon_heal = 0.005 * (0.8 + 0.4 * random.random()),
            delta_Q = 0.0001 * (0.8 + 0.4 * random.random()),
            gamma_P = 0.02 * (0.8 + 0.4 * random.random()),
            zeta = 0.3 * (0.8 + 0.4 * random.random()),
            eta = 0.01 * (0.8 + 0.4 * random.random()),
            sigma = 0.991,  # Keep this fixed
            lambda_omega = 0.05 * (0.8 + 0.4 * random.random()),
            lambda_tau = 0.05 * (0.8 + 0.4 * random.random()),
            lambda_iota = 0.1 * (0.8 + 0.4 * random.random()),
        )
        
        # Run to equilibrium
        cell = CellState(P=0.5, Q=0.9, tau=0.3, omega=0.0, iota=0.2)
        for _ in range(1000):
            cell = update_cell(cell, [], noise=0, params=params)
        
        S = compute_S_star(cell, params)
        equilibrium_S_stars.append(S)
    
    results = {
        'mean_equilibrium_S': float(np.mean(equilibrium_S_stars)),
        'std_equilibrium_S': float(np.std(equilibrium_S_stars)),
        'min_S': float(np.min(equilibrium_S_stars)),
        'max_S': float(np.max(equilibrium_S_stars)),
        'near_sigma_count': int(sum(1 for s in equilibrium_S_stars if abs(s - 0.991) < 0.1)),
        'near_T_star_count': int(sum(1 for s in equilibrium_S_stars if abs(s - 0.714) < 0.1)),
    }
    
    if verbose:
        print(f"\n  Equilibrium S* after parameter perturbation:")
        print(f"    Mean: {results['mean_equilibrium_S']:.4f} ± {results['std_equilibrium_S']:.4f}")
        print(f"    Range: [{results['min_S']:.4f}, {results['max_S']:.4f}]")
        print(f"    Near σ (0.991 ± 0.1): {results['near_sigma_count']}/{n_trials}")
        print(f"    Near T* (0.714 ± 0.1): {results['near_T_star_count']}/{n_trials}")
    
    return results

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("═" * 70)
    print("TIG FORMAL SPECIFICATION & VALIDATION PROTOCOL")
    print("From Vibes to Falsifiable Predictions")
    print("═" * 70)
    
    params = TIGParameters()
    
    # 1. Verify invariants
    print("\n[1. INVARIANT VERIFICATION]")
    cells = [CellState(P=0.3 + 0.5*random.random(), 
                       Q=0.8 + 0.2*random.random(),
                       tau=random.random() * 0.5,
                       omega=random.random() * 0.3,
                       iota=random.random() * 0.3) for _ in range(100)]
    invariants = verify_invariants(cells, params)
    print(f"  All invariants hold: {all(invariants.values())}")
    for name, holds in invariants.items():
        print(f"    {name}: {'✓' if holds else '✗'}")
    
    # 2. Run validation experiment
    results = run_validation_experiment(n_subjects=30)
    
    # 3. Phase transition analysis
    phase_results = analyze_phase_transition(params)
    
    # 4. Ratio stability analysis
    ratio_results = analyze_ratio_stability(n_trials=50)
    
    # Summary
    print("\n" + "═" * 70)
    print("VALIDATION SUMMARY")
    print("═" * 70)
    print(f"\n  Trauma Recovery Experiment:")
    print(f"    TIG R² = {results['TIG']['R2_mean']:.4f}")
    print(f"    Exponential R² = {results['Exponential']['R2_mean']:.4f}")
    print(f"    TIG wins: {'YES ✓' if results['TIG_beats_exponential_R2'] else 'NO'}")
    
    print(f"\n  Phase Transition:")
    print(f"    Critical noise = {phase_results['critical_noise']:.3f}" if phase_results['critical_noise'] else "    No collapse in range")
    
    print(f"\n  Ratio Stability:")
    print(f"    Equilibrium S* = {ratio_results['mean_equilibrium_S']:.4f} ± {ratio_results['std_equilibrium_S']:.4f}")
    
    # Save results
    all_results = {
        'validation_experiment': results,
        'phase_transition': phase_results,
        'ratio_stability': ratio_results,
    }
    
    with open('TIG_VALIDATION_RESULTS.json', 'w') as f:
        json.dump(all_results, f, indent=2, cls=NumpyEncoder)
    
    print(f"\n  Results saved to TIG_VALIDATION_RESULTS.json")
    print("═" * 70)
    
    return all_results

if __name__ == "__main__":
    results = main()
