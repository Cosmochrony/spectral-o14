This repository contains the source of the **O14** Cosmochrony paper  
*Observable-Class Mismatch and the Corrected δ → β* Relation on Heisenberg Graphs:
Block Normalisation, Central-Phase Contribution, and Structural Correspondence*.

This work extends the **spectral admissibility sub-programme** by resolving
the structural mismatch identified in **O13** (Source S2), which remained the
only explanation of the discrepancy between the exact exponent and the
phenomenological target for $\beta^*$.

While **O13** established that the mismatch is not a finite-size artefact,
it did not explain its origin. The present work provides this explanation
by identifying and correcting the observable-class mismatch between:

- the **proxy-level observable** used in O7
- the **exact Weil-block observable** measured in O12–O13

The analysis is both **theoretical** (derivation of the corrected relation)
and **numerical** (pipeline-based validation using O12/O13 outputs).

---

# Core Result

The paper establishes that the relation
\[
\beta^* = \frac{1}{\delta + \tfrac12}
\]
is **not valid in the exact-block setting**, and must be replaced by:
\[
\beta^* = \frac{1}{\delta_{\mathrm{eff}}(q) + \tfrac12} + \epsilon(q),
\]
where:
\[
\delta_{\mathrm{eff}}(q)
= \hat\delta_{\mathrm{exact}}(q)
- \delta_\gamma(q)
- \eta \frac{\log q}{\log n^*(q)}.
  \]

The correction has three structural components:

- **block heterogeneity** (A1)
- **block normalisation by $q$** (A2)
- **central-phase contribution** (A3)

The normalisation exponent is identified as:
\[
\eta = \frac{1}{2},
\]
as the unique value compatible with Weil scaling and block aggregation.

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
- the dominant correction is the normalisation term:
  \[
  \eta \frac{\log q}{\log n_1} \approx 1.03\text{–}1.06
  \]

The corrected exponent satisfies:
\[
\delta_{\mathrm{eff}}(q) < 5.0
\quad \text{for all tested primes}.
\]

This leads to:
\[
\beta^* \approx 0.23\text{–}0.33,
\]
which remains outside the phenomenological window $(0.09, 0.13)$.

---

# Structural Role of O14

O14 completes the logical chain initiated in O12–O13:

- **O11**: proxy-level observable
- **O12**: exact Weil-block observable
- **O13**: asymptotic falsification of finite-size hypothesis (S1)
- **O14**: theoretical resolution of observable mismatch (S2)

O14 is the first step that:

- identifies the **exact source** of the mismatch
- derives the **corrected structural relation**
- tests it on the **real computational pipeline**

---

# What O14 Adds

O14 introduces several key advances:

- a **precise classification of observable mismatch** (A1–A3)
- a decomposition:
  \[
  \hat\delta_{\mathrm{exact}} = \delta_{\mathrm{geom}} + \delta_\gamma
  \]
- a derivation of the **normalisation exponent** $\eta = 1/2$
- identification of:
    - $\delta_\gamma$ as a **finite-window bias**
    - $\epsilon(q)$ as the **observable trace of projection residuals**
- a **pipeline-based numerical section**, using real O12/O13 outputs
- a clarification of:
    - **shell-level vs block-level observables**

---

# Interpretation of the Result

The central conceptual outcome is that:

- the mismatch is **not due to measurement**
- the mismatch is **not due to finite size**
- the mismatch is **not due to the central phase**

but instead:

👉 it is dominated by **block normalisation**

This implies that:

- the corrected observable remains incompatible with the O7 relation
- the discrepancy is therefore **structural at the level of the theory**

---

# Outcome: Resolution of S2

O14 resolves Source S2 in the following sense:

- the mismatch is fully explained at the observable level
- all correction terms are identified and quantified
- the corrected relation is derived and tested

The result is:

- **Scenario S2-B is realised**
- the O7 mapping $\delta \mapsto \beta^*$ does not extend to the exact regime

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

O14 completes the extended chain:

1. Observable defined (O7)
2. Geometry resolved (O9)
3. Representation adapted (O11)
4. Exact observable extracted (O12)
5. Asymptotics tested (O13)
6. Observable-class corrected (O14)

The programme now establishes:

- the observable is well-defined
- the measurement is reliable
- the asymptotic behaviour is controlled
- the structural mismatch is explained

---

# What O14 Resolves

O14 provides:

- a full derivation of the corrected δ → β* relation
- a decomposition of all correction terms
- a pipeline-based validation
- a precise localisation of the remaining gap

---

# Residual Open Problem

The remaining problem is now clearly identified:

- the corrected relation does **not recover** the phenomenological range

This implies that at least one of the following must be revised:

- the amplification mechanism of O3
- the identification of $\beta^*$ with the lepton hierarchy
- the mapping between spectral capacity and mass ratios

---

# Open Directions

1. **Analytical derivation of η (O14-O1)**  
   Rigorous derivation from metaplectic phase mixing

2. **Quark and neutrino sectors (O14-O2)**  
   Extension of the corrected relation to other representations

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
- structurally corrected (**O14**)

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

J. Beau, Observable-Class Mismatch and the Corrected δ → β* Relation on Heisenberg Graphs:
Block Normalisation, Central-Phase Contribution, and Structural Correspondence,
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
