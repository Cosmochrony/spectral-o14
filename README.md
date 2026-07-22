This repository contains the source of the **O14** Cosmochrony paper  
*Observable-Class Mismatch in the Proposed δ → β* Relation on Heisenberg Graphs:
Block Normalisation, Central-Phase Diagnostics, and the Transfer Boundary*.

**Version 1.0.1.** The exact capacity measurements and the A1--A3 mismatch taxonomy are
unchanged. This version separates the intra-$q$ slope identity from endpoint/inter-$q$
normalisation and scopes the reciprocal formula as a conditional cross-substrate diagnostic.

This work extends the **spectral admissibility sub-programme** by analysing
the structural mismatch identified in **O13** (Source S2).

While **O13** established that the mismatch is not a finite-size artefact,
it did not explain its origin. The present work provides this explanation
by identifying the observable-class mismatch between:

- the **proxy-level observable** used in O7
- the **exact Weil-block observable** measured in O12–O13

The analysis is both **theoretical** (observable and estimator separation)
and **numerical** (pipeline-based diagnostics using O12/O13 outputs).

---

# Core Result

The paper establishes that the relation
\[
\beta^* = \frac{1}{\delta + \tfrac12}
\]
is **not derived natively in the exact-block setting**. Conditional on importing that
LPS reciprocal prescription, the legacy O14 endpoint diagnostic is:
\[
\beta_{\mathrm{diag}} = \frac{1}{\delta_{\mathrm{end}}(q) + \tfrac12} + \epsilon(q),
\]
where:
\[
\delta_{\mathrm{end}}(q)
= \hat\delta_{\mathrm{exact}}(q)
- \delta_\gamma(q)
- \eta \frac{\log q}{\log n^*(q)}.
  \]

The observable mismatch has three components:

- **block heterogeneity** (A1)
- **block normalisation by $q$** (A2)
- **central-phase contribution** (A3)

The square-root benchmark is:
\[
\eta = \frac{1}{2},
\]
but it is not uniquely derived by the scaling argument.
At fixed $q$, multiplication by $q^{-\eta}$ changes only the regression intercept, so
$\eta\log q/\log n^*$ is an endpoint/inter-$q$ term, not an intra-$q$ slope correction.

---

# Numerical Result (Pipeline Validation)

Using the real BFS pipeline of **O12/O13**, the paper shows that:

- the central-coordinate coherence is high:
  \[
  C(q) \in [0.92, 0.96]
  \]
- the induced phase variance is small:
  \[
  \mathrm{Var}(\theta) \in [0.09, 0.16]
  \]
- the central-phase correction is negligible:
  \[
  \delta_\gamma \ll 1
  \]
- the dominant displacement in the legacy endpoint diagnostic is:
  \[
  \eta \frac{\log q}{\log n_1} \approx 1.03\text{–}1.06
  \]

The legacy endpoint diagnostic satisfies:
\[
\delta_{\mathrm{eff}}(q) < 5.0
\quad \text{for all tested primes}.
\]

Under the imported reciprocal formula, this leads to:
\[
\beta_{\mathrm{diag}} \approx 0.23\text{–}0.33,
\]
which remains outside the phenomenological window $(0.09, 0.13)$.

---

# Structural Role of O14

O14 extends the logical sequence initiated in O12–O13:

- **O11**: proxy-level observable
- **O12**: exact Weil-block observable
- **O13**: asymptotic falsification of finite-size hypothesis (S1)
- **O14**: partial intra-$q$ resolution and transfer boundary for S2

O14 is the first step that:

- identifies the **exact source** of the mismatch
- proves fixed-$q$ slope invariance under $q$-normalisation
- evaluates the historical endpoint diagnostic on the **real computational pipeline**

---

# What O14 Adds

O14 introduces several key advances:

- a **precise classification of observable mismatch** (A1–A3)
- a decomposition:
  \[
  \hat\delta_{\mathrm{exact}} = \delta_{\mathrm{geom}} + \delta_\gamma
  \]
- a square-root benchmark $\eta = 1/2$ for a future inter-$q$ estimator
- identification of:
    - $\delta_\gamma$ as a **finite-window bias**
    - $\epsilon(q)$ as a **modelled variance term** in the conditional diagnostic
- a **pipeline-based numerical section**, using real O12/O13 outputs
- a clarification of:
    - **shell-level vs block-level observables**

---

# Interpretation of the Result

The central conceptual outcome is that:

- the mismatch is **not due to measurement**
- the mismatch is **not due to finite size**
- the mismatch is **not due to the central phase**

The legacy endpoint displacement is dominated by its $q$-normalisation term, but that
term does not alter the intra-$q$ fitted slope. Independently, the native Heisenberg
growth law does not carry the O7 reciprocal prescription.

---

# Outcome: Partial Intra-$q$ Resolution of S2

O14 resolves the intra-$q$ bookkeeping in Source S2 in the following sense:

- the mismatch classes are identified
- fixed-$q$ slope invariance is explicit
- the endpoint and cross-substrate layers are isolated as open assumptions

The result is:

- the historical endpoint diagnostic selects **Scenario S2-B**
- the O7 mapping $\delta \mapsto \beta^*$ has no native Heisenberg derivation

---

# Relation to Previous Steps

O14 preserves all structural results of the programme:

- spectral admissibility
- binary-polyhedral maximality
- ADE stratigraphy
- ordering (O1)
- amplification (O3)
- structural bounds (O4)
- admissible-frontier dynamics (O5)
- no-go (O6)
- capacity formulation (O7)
- geometric resolution (O8–O9)
- algorithmic resolution (O10–O11)
- exact extraction (O12)
- asymptotic validation (O13)

It does not modify these results,
but establishes their **domain of validity**.

---

# Conceptual Structure

O14 continues the extended sequence:

1. Observable defined (O7)
2. Geometry resolved (O9)
3. Representation adapted (O11)
4. Exact observable extracted (O12)
5. Asymptotics tested (O13)
6. Observable and estimator layers separated (O14)

The programme now establishes:

- the observable is well-defined
- the measurement is reliable
- the asymptotic behaviour is controlled
- the intra-$q$ mismatch is classified
- the endpoint/inter-$q$ estimator remains open

---

# What O14 Resolves

O14 provides:

- a proof that constant-in-$n$ block normalisation cannot change an intra-$q$ slope
- a decomposition of all correction terms
- a pipeline-based evaluation of the historical diagnostic
- a precise localisation of the remaining gap

---

# Residual Open Problem

The remaining problem is now clearly identified:

- a native Heisenberg growth carrier for the pair observable is absent
- the inter-$q$ estimator has not been defined and derived

This implies that at least one of the following must be revised:

- the amplification mechanism of O3
- the identification of $\beta^*$ with the lepton hierarchy
- the mapping between spectral capacity and mass ratios

---

# Open Directions

1. **Inter-$q$ estimator and η (O14-O1)**
   Define the estimator before deriving its normalisation from metaplectic phase mixing

2. **Quark and neutrino sectors (O14-O2)**
   Extension of the conditional diagnostic to other representations

3. **Refined central-phase correction (O14-O3)**
   Beyond the Weil-bound estimate

4. **Block-level phase observable (O14-O4)**
   Extract $z_b^{(c)}(n)$ before Gram–Schmidt to test $\delta_\gamma$ directly

5. **Revised amplification mechanism**
   Adapt O3 to the exact-block regime

---

# Status

The programme is now:

- free of algebraic obstruction (**O6**)
- free of geometric obstruction (**O8–O9**)
- free of representation obstruction (**O10–O12**)
- asymptotically validated (**O13**)
- explicit about the estimator and transfer boundary (**O14**)

It does not assume:

- validity of the O7 relation in the exact regime
- equivalence between proxy and exact observables
- convergence toward the phenomenological target

---

# Repository Structure

```text
paper/
├── out/      # Compiled O14 PDF
├── tex/      # LaTeX sources
└── README.md
```
# Citation

If you reference this work, please cite:

J. Beau, Observable-Class Mismatch in the Proposed δ → β* Relation on Heisenberg Graphs:
Block Normalisation, Central-Phase Diagnostics, and the Transfer Boundary,
Zenodo, 2026.

# Acknowledgements

Portions of the derivations, conceptual synthesis, numerical strategy,
and editorial refinement benefited from iterative interactions with
large language models used as analytical assistants.
All theoretical results, computations, and interpretations remain the
sole responsibility of the author.

# Contributions

This repository is intended as a research reference.

Critical feedback, independent verification, alternative implementations
of the O12/O13 pipeline, and block-level phase extraction methods
are welcome.

Please open an issue to discuss conceptual points,
technical details, or possible extensions.
