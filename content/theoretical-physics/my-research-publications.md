---
title: "My Research & Publications"
date: 2026-03-26
parent: "Theoretical Physics"
description: "Yang-Mills theory research, mass gap problem, BRST quantisation, and Stueckelberg extensions. Published papers on gauge theory and quantum gravity."
---


I want to write about this honestly, which means starting from the beginning rather than presenting a cleaned-up retrospective in which everything was planned and every step was deliberate.

It was not. The research grew out of a genuine obsession with a problem that I found too important to ignore, pursued with the tools I had at the time, which were not the tools I would have chosen if I were designing the project from scratch. They grew as the project grew. That is how it actually happened.

What follows is an account of each paper — what I was trying to do, what I actually did, how the work connects across the three publications, and where it is going. The mathematics is included where it is needed to understand the argument.

---

## The Problem That Started Everything: The Mass Gap

The Yang–Mills mass gap problem is one of the seven Millennium Prize Problems set by the Clay Mathematics Institute in 2000. A correct solution carries a prize of one million dollars, but more importantly, it would resolve a fundamental question in theoretical physics that has remained open since the formulation of quantum chromodynamics in the 1970s.

The problem is this. The Standard Model describes the strong nuclear force — the force that binds quarks into protons and neutrons — using Yang–Mills theory with gauge group $SU(3)$. Classically, Yang–Mills theory is a theory of massless gauge bosons. The gluons, which mediate the strong force, are massless in the classical theory. But experimentally, the strong force is short-range — it does not reach beyond the size of a hadron — which implies that the force-carrying particles effectively behave as if they are massive. More precisely, the quantum theory should exhibit a *mass gap*: a positive lower bound $\Delta > 0$ on the energy of any state above the vacuum.

The question is: why? What mechanism generates this mass gap, given that it does not exist in the classical theory?

The standard answer from lattice QCD is that confinement and the mass gap arise from non-perturbative effects — effects that are invisible in perturbation theory and emerge from the strongly-coupled dynamics of the gauge field. This is consistent with experiment and with numerical simulations. But a rigorous mathematical proof, from the axioms of quantum field theory, does not exist.

I became obsessed with this problem in grade 8. The Higgs mechanism — which explains how the $W$ and $Z$ bosons of the electroweak force acquire mass — was my initial inspiration. The Higgs field gives mass to gauge bosons by spontaneous symmetry breaking. Could something analogous work for Yang–Mills theory? Could there be a mechanism that generates a mass gap gauge-invariantly, without breaking the gauge symmetry?

That question led to the first paper.

---

## Paper 1 — Yang-Mills Theory with a Scalar Field: A Unified Model for Confinement and Mass Gap

**Journal:** International Journal of Research in Engineering and Science (IJRES), Vol. 11, Issue 6, June 2023, pp. 45–51
**DOI:** [10.6084/m9.figshare.23301395](https://doi.org/10.6084/m9.figshare.23301395)
**PDF:** [ijres.org](https://www.ijres.org/papers/Volume-11/Issue-6/11064551.pdf)

---

### The Problem and the Approach

This paper was written when I was in grade 9, a month before I turned 15. I want to be clear about that not to frame the work as a prodigy story — it is not that — but because it affects how to read the paper honestly. The ideas are genuine, the approach has merit, and the motivation for the mechanism turned out to point in a direction that subsequent work has confirmed is worth pursuing. But the mathematical treatment is less complete than the problem demands, and there are places where I was working at the edge of what I fully understood at the time.

The central idea was this: instead of the Higgs mechanism's complex scalar field, introduce a new particle — which I called the *confinement particle* — that mediates the confinement force between quarks. This particle was assumed to be massive, to carry colour charge, and to couple to quarks through an interaction term in the Lagrangian.

### The Lagrangian

The confinement sector Lagrangian I proposed was:

$$ L_c = -\frac{1}{4} F^c_{\mu\nu} F^{c\,\mu\nu} + m_c^2 A^c_\mu A^{c\,\mu} + g_c \bar{\psi} \gamma^\mu A^c_\mu T^c \psi$$

where $F^c_{\mu\nu} = \partial_\mu A^c_\nu - \partial_\nu A^c_\mu + g_c f^{abc} A^a_\mu A^b_\nu$ is the field strength tensor for the confinement field, $A^c_\mu$ is its gauge potential, $m_c$ is its mass, and $g_c$ is its coupling constant. The last term describes the interaction with quarks.

The confinement force between two quarks was derived as a Yukawa-type potential:

$$F_c(r) = \frac{g_c^2}{4\pi} \frac{e^{-m_c r}}{r}$$

This is attractive and increases with distance at intermediate scales — consistent with the intuitive picture of confinement. The mass of a hadron was expressed as:

$$M_H = \sum_{i=1}^n m_i + E_c$$

where $m_i$ are the constituent quark masses and $E_c$ is the energy stored in the confinement force.

### What the Paper Did and Did Not Do

The paper introduced a confinement mechanism and showed that it naturally generates a mass gap: the lightest hadronic states have a minimum energy contribution $E_c$ from the confinement sector, which is nonzero precisely because $m_c > 0$.

Crucially, I also introduced the **Stueckelberg mechanism** — discovered during the process of trying to make the mass term gauge-invariant. The standard mass term $m^2 A_\mu A^\mu$ for a gauge boson breaks gauge invariance. The Stueckelberg mechanism introduces an additional scalar field $\phi$ (the Stueckelberg field) that shifts under gauge transformations to compensate, restoring gauge invariance while preserving the mass. This observation became the foundation of the second paper.

What the paper did not do: it did not carry out full BRST quantisation. It did not compute one-loop corrections or verify that the theory was renormalisable. The Stueckelberg mechanism was introduced but not systematically developed. These gaps were the motivation for the work that followed.

### Personal Reflection

Looking at this paper now, I see both the genuine insight and the places where the mathematics was running ahead of my full command of it. The Yukawa confinement force is physically reasonable. The connection between the mass term and the Stueckelberg field is correct and important. The treatment of the non-perturbative aspects is too qualitative.

But the inspiration for the approach — drawing on the Higgs mechanism as an analogy, asking what gauge-invariant mass generation could look like in a non-Abelian gauge theory — turned out to point in the right direction. The second paper is a much more rigorous development of the same core idea.

---

## Paper 2 — Quantum Geometric Entanglement: A Unified Model for the Emergence of Spacetime in Quantum Gravity

**Journal:** International Journal of Research in Engineering and Science (IJRES), Vol. 11, Issue 9, September 2023, pp. 11–16
**Co-author:** Vihaan Gupta
**DOI:** [10.6084/m9.figshare.24560755](https://doi.org/10.6084/m9.figshare.24560755)

---

### A Different Direction

This paper came from a different line of thinking, running in parallel with the Yang–Mills work. The question it addresses is the other great unsolved problem in theoretical physics: the unification of quantum mechanics and general relativity.

Quantum mechanics and general relativity are incompatible. Quantum mechanics is a theory of the microscopic world — particles, wavefunctions, Hilbert spaces. General relativity is a theory of the macroscopic world — spacetime curvature, geodesics, the stress-energy tensor. Both are extraordinarily accurate in their respective domains. When you try to combine them, the mathematics breaks down.

The question I had been thinking about was: what if spacetime is not fundamental? What if the geometry of spacetime — the metric, the curvature — *emerges* from something more primitive? And what if that primitive thing is quantum entanglement?

This idea has a serious pedigree. Van Raamsdonk's 2010 paper "Building up spacetime with quantum entanglement," the ER=EPR conjecture of Maldacena and Susskind, and the work on holography and AdS/CFT all suggest deep connections between entanglement and geometry. QGET was our attempt to build a theoretical framework around this connection.

### The QGET Framework

The framework uses a graph-theoretic representation. Spacetime is modelled as a graph $G$ with nodes $V = \{v_1, v_2, \ldots, v_N\}$ representing geometric entities (with positions, curvatures, and other local properties) and edges $E = \{e_1, e_2, \ldots, e_m\}$ representing entanglement connections between them.

The entanglement structure is encoded in an $N \times N$ **entanglement matrix** $M$, where $M_{ij}$ is the entanglement correlation between nodes $v_i$ and $v_j$.

The dynamics of entanglement are governed by an **entanglement operator** $\mathcal{E}(t)$ — an $N \times N$ matrix whose components $\mathcal{E}_{ij}(t)$ give the entanglement correlation between nodes $v_i$ and $v_j$ at time $t$. Its evolution equation is:

$$\frac{d E_{ij}(t)}{dt} = -i[H_{ij}, E_{ij}(t)] + \sum_k \left(E_{ik}(t)\,\Gamma_{kj} - \Gamma_{ik}\,E_{kj}(t)\right)$$

where $H_{ij}$ is the Hamiltonian governing entanglement dynamics between nodes $v_i$ and $v_j$, and $\Gamma_{ij}$ is the coupling strength.

The connection between entanglement and spacetime geometry is made through the spacetime metric tensor $g(t)$, expressed as:

$$g(t) = \sum_{ij} g_{ij}(t)\, e_i(t) \otimes e_j(t)$$

The fundamental coupling between entanglement and emergent geometry is:

$$\frac{dg(t)}{dt} = \mathcal{E}(t) \otimes \mathcal{E}(t)^\dagger$$

This equation says that the rate of change of the spacetime metric is determined by the tensor square of the entanglement operator — spacetime geometry is driven by entanglement dynamics.

### What QGET Predicts

The theory makes several empirically testable predictions:

- Non-local entanglement correlations between spatially separated geometric nodes, detectable in principle through precision measurements
- Characteristic signatures in the cosmic microwave background if spacetime emergence occurred during inflation
- Modification of gravitational wave dispersion if entanglement correlations contribute to spacetime structure at short distances
- Information preservation in black hole formation and evaporation, with the entanglement structure preventing genuine information loss

### Honest Assessment

QGET as formulated in this paper is a framework — a proposal for how entanglement and geometry are coupled — rather than a complete theory. The evolution equations are written down and are mathematically well-defined, but deriving them from first principles of quantum gravity (rather than postulating them) remains work to be done. The connection to the Einstein field equations — showing that the emergent metric satisfies something like $G_{\mu\nu} = 8\pi T_{\mu\nu}$ in some appropriate limit — is stated as a goal but not derived.

I am still working on QGET. The current work focuses on two things: first, showing that the framework reduces to general relativity in the classical limit; second, investigating whether the entanglement matrix approach has a natural formulation in the language of spin networks and loop quantum gravity, where similar graph-theoretic structures appear. There is a genuine connection here that I have not yet fully understood.

The paper was written at 15, in the same period as the Yang–Mills work. Looking at it now, I think the core idea — that entanglement is the substrate from which spacetime geometry emerges, formalised through a graph-theoretic coupling — is worth developing seriously. The mathematical treatment needs to be made substantially more rigorous.

---

## Paper 3 — A Gauge-Invariant Stueckelberg Extension of Yang–Mills Theory

**Preprint:** figshare, 2025
**DOI:** [10.6084/m9.figshare.31768417](https://doi.org/10.6084/m9.figshare.31768417)

---

### The Continuation

This paper is the direct continuation of the first. Two years of additional study — in particular, working through BRST quantisation, the Faddeev–Popov procedure, the theory of renormalisation, and the structure of non-Abelian gauge theories at the level of Peskin–Schroeder and Tong's gauge theory notes — made it possible to develop the Stueckelberg extension properly.

The central result is a Yang–Mills theory extended by a group-valued Stueckelberg field $U \in G$ (where $G = SU(N)$ is the gauge group) that generates a gauge-invariant mass for the gauge bosons while preserving BRST symmetry and asymptotic freedom.

### The Stueckelberg Extension

The standard Stueckelberg mechanism for an Abelian ($U(1)$) gauge field $A_\mu$ introduces a scalar field $\phi$ and modifies the mass term to:

$$m^2\left(A_\mu - \frac{1}{m}\partial_\mu\phi\right)^2$$

which is invariant under $A_\mu \to A_\mu + \partial_\mu\alpha$, $\phi \to \phi + m\alpha$. For a non-Abelian gauge theory, the direct generalisation replaces the scalar $\phi$ with a group-valued field $U \in G$, and the mass term becomes:

$$m^2 \,\text{tr}\left[(A_\mu - \frac{i}{g}U^{-1}\partial_\mu U)^2\right]$$

This is invariant under the combined gauge transformation $A_\mu \to V A_\mu V^{-1} + \frac{i}{g}V\partial_\mu V^{-1}$ and $U \to VU$, where $V \in G$ is the gauge transformation.

### BRST Quantisation

The gauge-fixed action includes the BRST-invariant ghost sector. The BRST operator $s$ acts as:

$$sA^a_\mu = D^{ab}_\mu c^b, \qquad sc^a = -\frac{1}{2}f^{abc}c^b c^c, \qquad s\bar{c}^a = b^a, \qquad sb^a = 0$$

where $c^a$ and $\bar{c}^a$ are the ghost and anti-ghost fields, $b^a$ is the Nakanishi–Lautrup auxiliary field, and $D^{ab}_\mu$ is the covariant derivative in the adjoint representation. The Stueckelberg field transforms as $sU = gc^a T^a U$, which is the statement that $U$ transforms in the fundamental representation under BRST.

The full gauge-fixed and BRST-invariant action is:

$$S = S_\text{YM} + S_\text{Stueck} + S_\text{gf} + S_\text{ghost}$$

where $S_\text{YM} = -\frac{1}{4}\int F^a_{\mu\nu}F^{a\,\mu\nu}$, $S_\text{Stueck}$ contains the mass term and the Stueckelberg kinetic term, and $S_\text{gf} + S_\text{ghost}$ is the standard Faddeev–Popov gauge-fixing sector.

The nilpotency of $s$ — $s^2 = 0$ — guarantees the consistency of the gauge-fixing procedure and the decoupling of unphysical degrees of freedom.

### One-Loop Renormalisation and Asymptotic Freedom

The one-loop beta function for the coupling $g$ in the Stueckelberg-extended theory was computed in the $\overline{\text{MS}}$ scheme. The result is:

$$\beta(g) = -\frac{g^3}{16\pi^2}\left(\frac{11}{3}C_2(G) - \frac{2}{3}n_f T(R)\right) + \mathcal{O}(g^5)$$

where $C_2(G)$ is the quadratic Casimir of the adjoint representation, $n_f$ is the number of fermion flavours, and $T(R)$ is the index of the fermion representation. This is identical to the one-loop beta function of pure Yang–Mills theory — the Stueckelberg sector does not contribute at one loop to the running of $g$. Asymptotic freedom is therefore preserved: $\beta(g) < 0$ for $n_f < \frac{11}{2}C_2(G)/T(R)$, which is satisfied for $SU(3)$ with the physical number of quark flavours.

The mass parameter $m$ renormalises multiplicatively:

$$m(\mu) = m(\mu_0)\left(\frac{\alpha_s(\mu)}{\alpha_s(\mu_0)}\right)^\gamma$$

with the anomalous dimension $\gamma$ computable in perturbation theory.

### What the Paper Shows

The Stueckelberg extension generates a mass gap at tree level through the mass parameter $m > 0$. The gauge symmetry is not broken — it is instead extended, with the Stueckelberg field carrying the gauge degrees of freedom. The theory is BRST-consistent, which guarantees that the physical S-matrix is unitary and that unphysical states decouple. And asymptotic freedom is preserved, which means the theory is weakly coupled at high energies and strongly coupled at low energies — consistent with the physical picture of confinement.

The remaining open question, which the paper does not resolve and which is the central challenge of the Millennium Prize problem, is a rigorous non-perturbative proof that the mass gap persists beyond perturbation theory — that the quantum theory on $\mathbb{R}^4$ is well-defined and has a strictly positive mass gap in the Hilbert space. The Stueckelberg extension provides a mechanism; the rigorous construction is a harder and separate problem.

---

## What I Am Working On Now

### Continuing the Yang–Mills Programme

The preprint is the second paper in what I intend as a multi-paper programme on the Yang–Mills mass gap. The next step is the non-perturbative analysis. The Stueckelberg extension gives a tree-level mass gap; demonstrating that this survives quantum corrections requires either lattice methods or analytic non-perturbative techniques.

I am currently working on the two-loop renormalisation and on the connection between the Stueckelberg mass generation and the Gribov problem — the observation that the Faddeev–Popov gauge-fixing procedure is not globally well-defined for non-Abelian gauge theories, due to the existence of Gribov copies. The Gribov–Zwanziger modification of the gauge-fixed action is related to confinement and may connect naturally to the Stueckelberg sector.

### QGET — Active Development

QGET is a live project. The current focus is:

**Reduction to GR.** Showing that in the classical limit — where entanglement correlations become semiclassical and the graph becomes a smooth manifold — the QGET evolution equations reduce to the Einstein field equations. This requires taking the continuum limit of the graph Laplacian and interpreting the entanglement tensor as the stress-energy source.

**Connection to loop quantum gravity.** The graph-theoretic structure of QGET is similar to the spin network states of LQG. Whether the QGET entanglement matrix corresponds to something like the spin foam amplitudes of LQG is a question I am actively investigating. If the connection holds, QGET may be interpretable as a specific regime of LQG.

**Black hole information.** QGET predicts that information is preserved in black hole formation and evaporation because the entanglement structure is not destroyed by the horizon — it is merely redistributed. Making this precise requires a careful treatment of the horizon as a boundary of the entanglement graph and connecting to the recent work on island formulae and the Page curve.

These are long-horizon projects. I am working on them steadily.

---

## Overview

| Paper | Year | Topic | Status |
|-------|------|-------|--------|
| Yang-Mills Theory with a Scalar Field | 2023 | Mass gap, confinement particle, Stueckelberg introduction | Published, IJRES |
| Quantum Geometric Entanglement (QGET) | 2023 | Emergent spacetime from entanglement correlations | Published, IJRES |
| A Gauge-Invariant Stueckelberg Extension of Yang–Mills Theory | 2025 | BRST quantisation, one-loop renormalisation, asymptotic freedom | Preprint |
| QGET — Continuation | In progress | Classical limit, LQG connection, black hole information | Active |
| Yang–Mills — Non-perturbative analysis | In progress | Gribov problem, two-loop structure, mass gap beyond perturbation theory | Active |

---

*The work continues.*

*Last updated March 2026.*