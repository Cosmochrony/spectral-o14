"""Reproduce O14's conditional endpoint diagnostic and validation figure."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


Q_VALUES = np.array([29, 61, 101, 151, 211], dtype=int)
ETA_BENCHMARK = 0.5
BETA_STAR_LO = 0.09
BETA_STAR_HI = 0.13
EXACT_ASYMPTOTIC_DELTA = 3.0


def load_pipeline_row(q: int) -> dict[str, float]:
    """Load the committed O12/O13 summary for one prime."""
    path = Path("o14_pipeline") / f"q{q}_o12.npz"
    with np.load(path) as data:
        n0 = int(data["n0"])
        n1 = int(data["n1"])
        ell_gamma = data["ell_gam"]
        coherence = float(np.mean(ell_gamma[n0 : n1 + 1]))
        hat_delta = float(data["delta_hat"])

    endpoint_term = ETA_BENCHMARK * np.log(float(q)) / np.log(float(n1))
    delta_endpoint = hat_delta - endpoint_term
    return {
        "q": float(q),
        "hat_delta": hat_delta,
        "n1": float(n1),
        "coherence": coherence,
        "endpoint_term": endpoint_term,
        "delta_endpoint": delta_endpoint,
        "beta_exact_window": 1.0 / (hat_delta + 0.5),
        "beta_endpoint": 1.0 / (delta_endpoint + 0.5),
    }


def compute_results() -> list[dict[str, float]]:
    """Compute the table entries from committed pipeline summaries."""
    return [load_pipeline_row(int(q)) for q in Q_VALUES]


def print_results(results: list[dict[str, float]]) -> None:
    """Print values used in the paper table."""
    print("eta = 0.5 (explicit endpoint benchmark)")
    print("central-phase rank correction = 0 (exact algebraic identity)")
    print("q  delta_hat  n1  endpoint_term  delta_endpoint  beta_endpoint  coherence")
    for row in results:
        print(
            f"{int(row['q']):3d}  {row['hat_delta']:.3f}  {int(row['n1']):2d}  "
            f"{row['endpoint_term']:.4f}  {row['delta_endpoint']:.4f}  "
            f"{row['beta_endpoint']:.4f}  {row['coherence']:.4f}"
        )


def make_figure(results: list[dict[str, float]]) -> None:
    """Generate the four-panel PDF included in the paper."""
    q = np.array([row["q"] for row in results])
    hat_delta = np.array([row["hat_delta"] for row in results])
    delta_endpoint = np.array([row["delta_endpoint"] for row in results])
    beta_window = np.array([row["beta_exact_window"] for row in results])
    beta_endpoint = np.array([row["beta_endpoint"] for row in results])
    coherence = np.array([row["coherence"] for row in results])

    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    fig.suptitle("O14 conditional endpoint bookkeeping", fontsize=13)

    ax = axes[0, 0]
    ax.plot(q, hat_delta, "o-", color="steelblue", label="finite-window slope")
    ax.axhline(EXACT_ASYMPTOTIC_DELTA, color="black", linestyle="--", label="exact asymptotic δ = 3")
    ax.set_title("(A) Non-monotone crossover statistics")
    ax.set_xlabel("prime q")
    ax.set_ylabel("capacity exponent")
    ax.legend(fontsize=8)
    ax.grid(True, linestyle=":")

    ax = axes[0, 1]
    ax.plot(q, hat_delta, "o--", color="steelblue", label="finite-window slope")
    ax.plot(q, delta_endpoint, "s-", color="darkorange", label="endpoint diagnostic")
    ax.axhspan(7.4, 10.6, color="green", alpha=0.12, label="imported target")
    ax.set_title("(B) Benchmark η = 1/2")
    ax.set_xlabel("prime q")
    ax.set_ylabel("exponent")
    ax.legend(fontsize=8)
    ax.grid(True, linestyle=":")

    ax = axes[1, 0]
    ax.plot(q, beta_window, "o--", color="steelblue", label="from finite-window slope")
    ax.plot(q, beta_endpoint, "s-", color="darkorange", label="from endpoint diagnostic")
    ax.axhspan(BETA_STAR_LO, BETA_STAR_HI, color="green", alpha=0.15, label="phenomenological window")
    ax.set_title("(C) Imported reciprocal comparison")
    ax.set_xlabel("prime q")
    ax.set_ylabel("β diagnostic")
    ax.legend(fontsize=8)
    ax.grid(True, linestyle=":")

    ax = axes[1, 1]
    ax.plot(q, coherence, "D-", color="goldenrod")
    ax.set_title("(D) Independent shell-level null control")
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
