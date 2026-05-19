#!/usr/bin/env python3
"""
build-frontier-animation.py

Generate an animated GIF reproducing Lee & Ki (2017) generational technological
frontier figure for a UNC Gillings lecture slide deck.

The animation builds progressively:
  1) Axes + title + source line
  2) Generation 1 S-curve
  3) Generation 2 S-curve on top of Gen 1
  4) Generation 3 S-curve on top of Gen 2
  5) Yellow "Technological Frontier" envelope across all three generations
  6) High-income country growth path (gray, sequential through generations)
  7) Vertical "present day" line at t ~= 91
  8) Developing country Option 1 (catch-up; navy dash-dot) following HIC pattern
  9) Developing country Option 2 (leapfrog; Carolina Blue solid-dot) jumping to frontier
 10) Hold full composed figure, then loop

Output: /Users/sysylvia/Documents/Repos/presentations/research/2026-04-dhep-guest-lecture/images/generational-frontier-animated.gif
"""

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------
OUT_GIF = Path(
    "/Users/sysylvia/Documents/Repos/presentations/research/"
    "2026-04-dhep-guest-lecture/images/generational-frontier-animated.gif"
)

# -----------------------------------------------------------------------------
# Gillings brand palette
# -----------------------------------------------------------------------------
NAVY = "#13294B"          # primary text / axes / Option 1
CAROLINA = "#4B9CD3"      # accent / Option 2 (leapfrog)
GOLD = "#F4C430"          # technological frontier (dashed)
GRAY = "#6B6B6B"          # HIC growth path
GEN_GRAY_1 = "#4D4D4D"    # Gen 1
GEN_GRAY_2 = "#555555"    # Gen 2
GEN_GRAY_3 = "#222222"    # Gen 3 (darkest — envelope of frontier)
PRESENT_LINE = "#13294B"

# -----------------------------------------------------------------------------
# Time axis
# -----------------------------------------------------------------------------
T_MIN, T_MAX = 1, 181
t = np.linspace(T_MIN, T_MAX, 721)   # dense grid; 0.25-unit steps


def sigmoid(x, x0, k, L):
    """Logistic curve that plateaus at level L."""
    return L / (1.0 + np.exp(-k * (x - x0)))


# Generation curves (offsets chosen so each plateaus later and higher)
gen1 = sigmoid(t, x0=20,  k=0.08, L=28.0)
gen2 = sigmoid(t, x0=70,  k=0.07, L=38.0) + 0.0
gen3 = sigmoid(t, x0=120, k=0.07, L=45.0)

# Shift gen2/gen3 so they are only meaningfully non-zero once they "arrive"
gen2 = np.where(t > 40, gen2, gen2 * (t - T_MIN) / 39.0)
gen2 = np.clip(gen2, 0, 40)
gen3 = np.where(t > 90, gen3, gen3 * np.clip((t - 60) / 30.0, 0, 1))
gen3 = np.clip(gen3, 0, 46)

# Frontier = envelope max
frontier = np.maximum.reduce([gen1, gen2, gen3])

# High-income country growth path: smooth S-curve that follows the frontier
# but slightly lagged / below it, crossing each generation sequentially.
def hic_path(tt):
    # Piecewise-smooth: rises in Gen 1 era, climbs Gen 2 plateau, Gen 3 climb.
    base = sigmoid(tt, x0=30, k=0.09, L=26.0)           # first wave
    second = sigmoid(tt, x0=80, k=0.07, L=10.0)         # onto Gen 2
    third = sigmoid(tt, x0=130, k=0.06, L=8.0)          # onto Gen 3
    # Start very low at t=1 so HIC clearly climbs from near zero.
    return base + second + third - 1.5
hic = np.clip(hic_path(t), 0, 45)

# Developing country Option 1 — CATCH-UP (starts ~71, traces HIC trajectory shifted)
# Catch-up = sequential diffusion through the same generations HICs already traversed.
# Starts at productivity 14 at t=71 and rises smoothly, eventually approaching Gen 2.
OPT1_START = 71
opt1 = np.full_like(t, np.nan, dtype=float)
mask1 = t >= OPT1_START
t_catch = t[mask1]
# Two gentle sigmoids: first toward Gen 1 plateau, then continued rise toward Gen 2.
catch_wave1 = sigmoid(t_catch, x0=100, k=0.06, L=14.0)  # rise from 14 toward ~28
catch_wave2 = sigmoid(t_catch, x0=150, k=0.05, L=10.0)  # continue toward ~38
opt1_vals = 14.0 + catch_wave1 + catch_wave2
# Subtract the value at t=OPT1_START so it starts exactly at 14
offset_opt1 = (sigmoid(OPT1_START, x0=100, k=0.06, L=14.0)
               + sigmoid(OPT1_START, x0=150, k=0.05, L=10.0))
opt1_vals = opt1_vals - offset_opt1
opt1_vals = np.maximum.accumulate(opt1_vals)
opt1_vals = np.clip(opt1_vals, 14.0, 38.5)
opt1[mask1] = opt1_vals

# Developing country Option 2 — LEAPFROG (starts ~71, jumps to frontier / Gen 3)
# Jumps over Gen 1 and Gen 2 entirely — sharp climb directly to the frontier.
OPT2_START = 71
opt2 = np.full_like(t, np.nan, dtype=float)
mask2 = t >= OPT2_START
t_leap = t[mask2]
start_val = 14.0
# Sharp sigmoid centered around t=95 (just past present day) that climbs from
# start_val toward the frontier.
leap_sigmoid = sigmoid(t_leap, x0=95, k=0.16, L=1.0)
# Subtract start value at t=OPT2_START so the curve starts exactly at 14
leap_offset = sigmoid(OPT2_START, x0=95, k=0.16, L=1.0)
leap_norm = (leap_sigmoid - leap_offset) / (1.0 - leap_offset)
leap_norm = np.clip(leap_norm, 0, 1)
target = frontier[mask2] - 0.4
opt2_vals = start_val + (target - start_val) * leap_norm
# After catching, hug the frontier from below
opt2_vals = np.minimum(opt2_vals, frontier[mask2] - 0.3)
opt2_vals = np.maximum.accumulate(opt2_vals)
opt2[mask2] = opt2_vals

# -----------------------------------------------------------------------------
# Animation stages (in frames)
# -----------------------------------------------------------------------------
FPS = 24
# Each stage occupies a slice of frames. Total ~ 9.5 s.
STAGES = {
    "axes":        (0,   10),   # 0.4s — axes pop in
    "gen1":        (10,  30),   # 0.8s
    "gen2":        (30,  50),
    "gen3":        (50,  70),
    "frontier":    (70,  95),   # 1.0s
    "hic":         (95, 120),
    "present":     (120, 130),  # 0.4s — vertical line
    "opt1":        (130, 160),
    "opt2":        (160, 195),
    "hold":        (195, 230),  # 1.5s hold
}
TOTAL_FRAMES = 230  # ~9.6s at 24fps


def stage_progress(frame, stage):
    """Return progress in [0,1] through a named stage at given frame."""
    start, end = STAGES[stage]
    if frame < start:
        return 0.0
    if frame >= end:
        return 1.0
    return (frame - start) / (end - start)


# -----------------------------------------------------------------------------
# Figure setup
# -----------------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "axes.edgecolor": NAVY,
    "axes.labelcolor": NAVY,
    "xtick.color": NAVY,
    "ytick.color": NAVY,
    "axes.titlecolor": NAVY,
})

fig, ax = plt.subplots(figsize=(10, 5.6), dpi=130)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

ax.set_xlim(T_MIN, T_MAX)
ax.set_ylim(0, 50)
ax.set_xlabel("Time Periods", fontsize=12, color=NAVY)
ax.set_ylabel("Productivity", fontsize=12, color=NAVY)

# Tick styling
ax.set_xticks(np.arange(1, 182, 10))
ax.set_yticks(np.arange(0, 51, 10))
ax.tick_params(axis="both", length=3, width=0.8)
for spine_name in ("top", "right"):
    ax.spines[spine_name].set_visible(False)
for spine_name in ("left", "bottom"):
    ax.spines[spine_name].set_linewidth(1.0)

# Source line
fig.text(0.08, 0.02, "Source: Lee & Ki (2017)", fontsize=9,
         color=NAVY, style="italic")

# Title
ax.set_title("The Technological Frontier and Developing-Country Choice",
             fontsize=13, color=NAVY, pad=12, loc="left", weight="bold")

# -----------------------------------------------------------------------------
# Artists (created empty, updated per frame)
# -----------------------------------------------------------------------------
(line_gen1,) = ax.plot([], [], linestyle=(0, (5, 2, 1, 2)),
                       color=GEN_GRAY_1, linewidth=2.0, label=None)
(line_gen2,) = ax.plot([], [], linestyle=(0, (4, 2)),
                       color=GEN_GRAY_2, linewidth=2.0, label=None)
(line_gen3,) = ax.plot([], [], linestyle="-",
                       color=GEN_GRAY_3, linewidth=2.2, label=None)

(line_frontier,) = ax.plot([], [], linestyle=(0, (6, 3)),
                           color=GOLD, linewidth=4.2, label=None,
                           solid_capstyle="round")

(line_hic,) = ax.plot([], [], linestyle="-",
                      color=GRAY, linewidth=2.6, label=None)

present_line = ax.axvline(91, color=PRESENT_LINE, linewidth=2.0, alpha=0.0)

(line_opt1,) = ax.plot([], [], linestyle=(0, (3, 2, 1, 2)),
                       color=NAVY, linewidth=2.4, label=None)
(line_opt2,) = ax.plot([], [], linestyle=(0, (1, 1.5)),
                       color=CAROLINA, linewidth=3.0, label=None,
                       solid_capstyle="round")

# Label annotations (created invisible, revealed at the right frame)
def make_label(x, y, text, color, weight="normal", bbox=True, fontsize=10):
    kwargs = dict(color=color, fontsize=fontsize, weight=weight, ha="left",
                  va="center", alpha=0.0)
    if bbox:
        kwargs["bbox"] = dict(boxstyle="round,pad=0.3", fc="white",
                              ec=color, lw=0.8, alpha=0.0)
    return ax.text(x, y, text, **kwargs)

lbl_gen1 = make_label(175, 30.5, "Generation 1", GEN_GRAY_1, bbox=False, fontsize=10)
lbl_gen2 = make_label(175, 39.0, "Generation 2", GEN_GRAY_2, bbox=False, fontsize=10)
lbl_gen3 = make_label(158, 46.2, "Generation 3", GEN_GRAY_3, weight="bold",
                      bbox=False, fontsize=10)
lbl_frontier = make_label(10, 47.0, "Technological\nFrontier",
                          "#A88420", weight="bold", bbox=True, fontsize=10)
lbl_hic = make_label(45, 7, "High-income country\ngrowth path",
                     GRAY, bbox=True, fontsize=9.5)
lbl_present = make_label(92, 2.5, "present day", NAVY, bbox=False, fontsize=9)
lbl_opt1 = make_label(153, 33.5, "Developing country:\nOption 1 (catch-up)",
                      NAVY, bbox=True, fontsize=9.5)
lbl_opt2 = make_label(100, 22, "Developing country:\nOption 2 (leapfrog)",
                      CAROLINA, weight="bold", bbox=True, fontsize=9.5)


def set_alpha(artist, alpha):
    """Set alpha on artist and, if text with bbox, the bbox too."""
    artist.set_alpha(alpha)
    if hasattr(artist, "get_bbox_patch"):
        bp = artist.get_bbox_patch()
        if bp is not None:
            bp.set_alpha(alpha * 0.95)


def partial_line(x_full, y_full, p):
    """Return x,y truncated to fraction p in [0,1] of their length."""
    if p <= 0:
        return [], []
    n = len(x_full)
    k = max(2, int(round(n * p)))
    return x_full[:k], y_full[:k]


def partial_masked(x_full, y_full, mask, p):
    """Draw a partial curve restricted to a boolean mask, parametrized by p."""
    xs = x_full[mask]
    ys = y_full[mask]
    if len(xs) == 0 or p <= 0:
        return [], []
    k = max(2, int(round(len(xs) * p)))
    return xs[:k], ys[:k]


# -----------------------------------------------------------------------------
# Animation update
# -----------------------------------------------------------------------------
def update(frame):
    # Axes appear stage: nothing to draw, already set up. Could fade-in spines.
    # Gen 1
    p = stage_progress(frame, "gen1")
    x, y = partial_line(t, gen1, p)
    line_gen1.set_data(x, y)
    set_alpha(lbl_gen1, min(1.0, max(0.0, (p - 0.7) / 0.3)))

    # Gen 2
    p = stage_progress(frame, "gen2")
    x, y = partial_line(t, gen2, p)
    line_gen2.set_data(x, y)
    set_alpha(lbl_gen2, min(1.0, max(0.0, (p - 0.7) / 0.3)))

    # Gen 3
    p = stage_progress(frame, "gen3")
    x, y = partial_line(t, gen3, p)
    line_gen3.set_data(x, y)
    set_alpha(lbl_gen3, min(1.0, max(0.0, (p - 0.7) / 0.3)))

    # Frontier
    p = stage_progress(frame, "frontier")
    x, y = partial_line(t, frontier, p)
    line_frontier.set_data(x, y)
    set_alpha(lbl_frontier, min(1.0, max(0.0, (p - 0.4) / 0.6)))

    # HIC
    p = stage_progress(frame, "hic")
    x, y = partial_line(t, hic, p)
    line_hic.set_data(x, y)
    set_alpha(lbl_hic, min(1.0, max(0.0, (p - 0.6) / 0.4)))

    # Present day vertical line
    p = stage_progress(frame, "present")
    present_line.set_alpha(p * 0.95)
    set_alpha(lbl_present, p)

    # Option 1 — catch-up
    p = stage_progress(frame, "opt1")
    x, y = partial_masked(t, opt1, mask1, p)
    line_opt1.set_data(x, y)
    set_alpha(lbl_opt1, min(1.0, max(0.0, (p - 0.7) / 0.3)))

    # Option 2 — leapfrog
    p = stage_progress(frame, "opt2")
    x, y = partial_masked(t, opt2, mask2, p)
    line_opt2.set_data(x, y)
    set_alpha(lbl_opt2, min(1.0, max(0.0, (p - 0.7) / 0.3)))

    return (line_gen1, line_gen2, line_gen3, line_frontier, line_hic,
            present_line, line_opt1, line_opt2,
            lbl_gen1, lbl_gen2, lbl_gen3, lbl_frontier, lbl_hic, lbl_present,
            lbl_opt1, lbl_opt2)


anim = FuncAnimation(fig, update, frames=TOTAL_FRAMES,
                     interval=1000 / FPS, blit=False)

OUT_GIF.parent.mkdir(parents=True, exist_ok=True)
writer = PillowWriter(fps=FPS)
anim.save(str(OUT_GIF), writer=writer, dpi=100)
print(f"Saved: {OUT_GIF}")
print(f"Size: {OUT_GIF.stat().st_size / 1024:.1f} KB")
