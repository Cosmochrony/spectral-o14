"""Reproduce O14's finite-window diagnostics and validation figure."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


Q_VALUES = np.array([29, 61, 101, 151, 211], dtype=int)
EXACT_ASYMPTOTIC_DELTA = 3.0


def load_pipeline_row(q: int) -> dict[str, float | bool]:
    """Load the committed O12/O13 summary for one prime."""
    path = Path("o14_pipeline") / f"q{q}_o12.npz"
    with np.load(path) as data:
        n0 = int(data["n0"])
        n1 = int(data["n1"])
        ell_gamma = data["ell_gam"]
        coherence = float(np.mean(ell_gamma[n0 : n1 + 1]))
        hat_delta = float(data["delta_hat"])
        v_max = float(data["v_max_win"])

    return {
        "q": float(q),
        "hat_delta": hat_delta,
        "n0": float(n0),
        "n1": float(n1),
        "v_max": v_max,
        "e2_ok": v_max < 1.0,
        "coherence": coherence,
    }


def compute_results() -> list[dict[str, float | bool]]:
    """Compute the table entries from committed pipeline summaries."""
    return [load_pipeline_row(int(q)) for q in Q_VALUES]


def print_results(results: list[dict[str, float | bool]]) -> None:
    """Print values used in the paper table."""
    print("central-phase rank correction = 0 (exact algebraic identity)")
    print("q  delta_hat  window  V_max  E2  coherence")
    for row in results:
        print(
            f"{int(row['q']):3d}  {row['hat_delta']:.3f}  "
            f"[{int(row['n0'])},{int(row['n1'])}]  {row['v_max']:.3f}  "
            f"{str(row['e2_ok']).lower():5s}  {row['coherence']:.4f}"
        )


def make_figure(results: list[dict[str, float | bool]]) -> None:
    """Generate the three-panel PDF included in the paper."""
    q = np.array([float(row["q"]) for row in results])
    hat_delta = np.array([float(row["hat_delta"]) for row in results])
    v_max = np.array([float(row["v_max"]) for row in results])
    coherence = np.array([float(row["coherence"]) for row in results])

    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    fig.suptitle("O14 finite-window pipeline diagnostics", fontsize=13)

    ax = axes[0]
    ax.plot(q, hat_delta, "o-", color="steelblue", label="finite-window slope")
    ax.axhline(EXACT_ASYMPTOTIC_DELTA, color="black", linestyle="--", label="exact asymptotic δ = 3")
    ax.set_title("(A) Crossover statistics")
    ax.set_xlabel("prime q")
    ax.set_ylabel("capacity exponent")
    ax.legend(fontsize=8)
    ax.grid(True, linestyle=":")

    ax = axes[1]
    ax.plot(q, v_max, "s-", color="darkorange")
    ax.axhline(1.0, color="black", linestyle="--", label="E2 threshold")
    ax.fill_between(q, 0.0, 1.0, color="green", alpha=0.12)
    ax.set_title("(B) Inter-block heterogeneity")
    ax.set_xlabel("prime q")
    ax.set_ylabel("maximum variance ratio")
    ax.set_ylim(bottom=0.0)
    ax.legend(fontsize=8)
    ax.grid(True, linestyle=":")

    ax = axes[2]
    ax.plot(q, coherence, "D-", color="goldenrod")
    ax.set_title("(C) Independent null control")
    ax.set_xlabel("prime q")
    ax.set_ylabel("central-coordinate coherence")
    ax.set_ylim(0.0, 1.05)
    ax.grid(True, linestyle=":")

    fig.tight_layout()
    fig.savefig(
        "fig_SpectralO14_validation.pdf",
        bbox_inches="tight",
        metadata={"Creator": "SpectralO14_simulation.py", "CreationDate": None},
    )
    plt.close(fig)


def main() -> None:
    results = compute_results()
    print_results(results)
    make_figure(results)


if __name__ == "__main__":
    main()
