# O14: Why Exact Heisenberg Capacity Does Not Determine the Phenomenological Cascade Rate

This repository contains the source and reproduction code for O14 in the Cosmochrony spectral-admissibility
programme.

The paper separates exact Heisenberg capacity from the phenomenological cascade-rate variable used in the imported
O7 reciprocal prescription.

## Core result

O12's exact rank formula makes the central coordinate algebraically invisible to the projective-capacity observable:

\[
\Sigma_n^{(c)}=\frac{\Delta r_n^{(c)}}{|S_n|},
\qquad
\delta_{\gamma,\mathrm{corr}}=0.
\]

The central coordinate multiplies a Fourier mode by a non-zero scalar phase.
It changes neither the mode's projective class nor any span rank.
Block heterogeneity instead comes from overlap among the projective frequencies
\((\alpha,\beta)=(B/A,C/A)\bmod q\).

Two genuine transfer gaps remain:

- the exact observable is a mean over heterogeneous Weil blocks, while the proxy argument assumes a scalar capacity;
- the fixed-degree Heisenberg pipeline supplies no changing-degree growth carrier or typed identification with the LPS
  rate variable.

At fixed \(q\), multiplying by \(q^{-\eta}\) changes the intercept of a log-log regression and cannot change its
slope.
The expression \(\eta\log q/\log n^*\) therefore belongs only to an explicitly defined endpoint or inter-\(q\)
statistic.

## Finite-window data and conditional diagnostic

The five O12/O13 fitted slopes are

\[
4.42,\ 4.80,\ 4.51,\ 4.27,\ 3.59
\]

at \(q\in\{29,61,101,151,211\}\).
They rise from \(q=29\) to \(q=61\), then decrease strictly through \(q=211\).
They are finite-window crossover statistics approaching the exact asymptotic exponent \(\delta=3\), not candidate
asymptotic exponents for a capacity-to-rate map.

Conditional on importing the LPS reciprocal prescription and choosing the explicit benchmark \(\eta=1/2\), O14
displays

\[
\delta_{\mathrm{end}}(q)
=\hat\delta_{\mathrm{exact}}(q)-\eta\frac{\log q}{\log n_1(q)},
\qquad
\beta_{\mathrm{diag}}(q)=\frac{1}{\delta_{\mathrm{end}}(q)+\tfrac12}.
\]

The endpoint statistic remains below \(5.0\) at all five primes, and the reciprocal diagnostic remains outside the
phenomenological interval \((0.09,0.13)\).
This selects S2-B inside the conditional comparison, but it does not derive a native Heisenberg cascade rate.

## Reproduction

The committed `code/o14_pipeline/` summaries are the compact inputs consumed by the paper's reproduction script.
The exact command from an independent clone is:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r code/requirements.txt
PYTHON_BIN=.venv/bin/python bash build.sh
```

`build.sh` regenerates `code/fig_SpectralO14_validation.pdf`, verifies it against
`code/ARTIFACT_SHA256SUMS`, and compiles the paper.
The figure PDF and the compiled paper PDF are derived, git-ignored artefacts.

The current citable record is the [Zenodo concept DOI](https://doi.org/10.5281/zenodo.19226272).

## Open directions

1. Define an inter-\(q\) estimator and derive its normalisation without using the target value.
2. Supply a native growth carrier and a typed capacity-to-rate identification.
3. Evaluate any resulting conditional diagnostic for the quark and neutrino sectors only after the carrier and
   normalisation are fixed.

## Version history

- **1.1:** Establishes exact central-phase invariance, removes the phase-bias mechanism, classifies the finite-window
  slopes as non-monotone crossover statistics, and reduces the endpoint diagnostic to its sole benchmark-normalisation
  term.
- **1.0.1:** Separates fixed-\(q\) slope invariance from endpoint and inter-\(q\) bookkeeping.
- **1.0:** Initial release.
