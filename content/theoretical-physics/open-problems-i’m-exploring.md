---
title: "Open Problems I’m Exploring"
date: 2026-03-28
parent: "Theoretical Physics"
---

This page is different from most "open problems" pages. I am not listing problems I find interesting from a distance. These are problems I am in the middle of — problems that are directly connected to my published and ongoing work, that I think about most days, and that I do not currently know how to solve.

The problems are organised into two clusters, corresponding to the two lines of research I described in the [publications page](/theoretical-physics/my-research-publications/): the Yang–Mills mass gap programme and the QGET framework for emergent spacetime. Within each cluster I have listed both the specific technical tasks I am currently working on and the broader open problems in the field that they connect to.

I have also included a third section on problems in the wider field that I am not currently working on but that I find genuinely compelling and that intersect with the mathematics I am building.

---

## A Note on Honesty

Many of these problems are extraordinarily hard. Some of them have been open for fifty years and have resisted the best mathematical physicists of the 20th century. I am a high school student. I am not claiming I will solve them. What I am saying is that my own research — the Stueckelberg extension, the BRST structure, the QGET framework — lives in the neighbourhood of these problems, and working on the smaller questions I can approach is how I am learning to navigate the larger landscape.

The distinction between "problem I am working on" and "problem I am aware of and working toward" is real, and I try to mark it clearly throughout this page.

---

## Cluster I — The Yang–Mills Programme

### Problem 1.1 — The Mass Gap: Non-Perturbative Survival

**Status:** Central open problem in my research programme. Working on it.

**What the problem is.** My 2026 preprint establishes a gauge-invariant mass for Yang–Mills theory at tree level via the Stueckelberg extension, and shows that the one-loop beta function preserves asymptotic freedom. This is perturbative. The Clay Millennium Prize Problem asks for a non-perturbative result: a rigorous proof that the quantum Yang–Mills theory on $\mathbb{R}^4$ exists (satisfies the Wightman axioms or their Osterwalder–Schrader equivalents) and has a strictly positive mass gap $\Delta > 0$ in the full quantum theory.

The gap between my result and the Prize is precisely the non-perturbative gap. A mass term at tree level is necessary but not sufficient. Non-perturbative effects — instantons, confinement, the strong-coupling dynamics — could in principle wash it out.

**What I am working on.** Two approaches in parallel. The first is two-loop renormalisation: computing the two-loop beta function of the Stueckelberg-extended theory and verifying that the mass parameter does not run to zero in the infrared. If the mass is an infrared-stable fixed point of the RG flow, that is strong evidence (not a proof, but evidence) that the mass gap survives.

The second approach is through the Gribov problem, described in Problem 1.2 below.

**Connection to the field.** The activity around the mass gap has intensified recently. In June 2025, Serafini et al. posted [arXiv:2506.00284](https://arxiv.org/abs/2506.00284) claiming a constructive proof of the mass gap for pure $SU(3)$ Yang–Mills on $\mathbb{R}^4$ using a five-dimensional regulator (realising $\mathbb{R}^4$ as the zero-mode sector of a theory on $\mathbb{R}^4 \times S^1/\mathbb{Z}_2$) combined with a convergent polymer expansion for gauge and ghost fields. The paper is currently under expert review; whether it meets the Clay standard is not yet established. Sourav Chatterjee gave a lecture at the Clay Millennium Problems series at Harvard in October 2025 reviewing the state of the problem. Martin Hairer spoke on it at the Clay Mathematics Institute in October 2025. The problem is genuinely active.

Earlier important work: Chatterjee's probabilistic approach ([arXiv:1803.01950](https://arxiv.org/abs/1803.01950)) treats Yang–Mills from the perspective of random matrix theory and has established partial results. The $U(N)$ lattice Yang–Mills mass gap in the 't Hooft regime was proved rigorously by Cao, Chatterjee et al. in 2025 ([arXiv:2510.22788](https://arxiv.org/abs/2510.22788)), establishing a mass gap, unique infinite volume limit, and the large $N$ limit for $U(N)$ lattice Yang–Mills using a random-environment decomposition. This is a partial result — lattice, not continuum — but a genuine one.

---

### Problem 1.2 — The Gribov Problem and the Stueckelberg Extension

**Status:** Active; working on the connection.

**What the problem is.** In 1978, Gribov showed that the Faddeev–Popov gauge-fixing procedure for non-Abelian gauge theories is not globally valid: for any choice of gauge condition, there exist multiple gauge field configurations satisfying that condition (Gribov copies), related by gauge transformations. This means the Faddeev–Popov integral overcounts the physical configurations, and the standard BRST quantisation is incomplete in the non-perturbative regime.

The Gribov–Zwanziger (GZ) framework addresses this by restricting the path integral to the first Gribov region (where the Faddeev–Popov operator is positive definite) by adding a non-local mass term (the Zwanziger horizon function) to the action. The refined Gribov–Zwanziger (RGZ) framework incorporates additional condensates. These modifications affect the infrared gluon propagator: instead of being massless (as in perturbation theory), the gluon propagator saturates in the infrared, consistent with the mass gap.

**The connection to my work.** The Stueckelberg mass term and the Gribov–Zwanziger horizon function both generate an effective gluon mass in the infrared, through different mechanisms. The question I am investigating is: are these two mechanisms related? Specifically, can the Stueckelberg field be understood as encoding the Gribov copy structure — as a field whose non-trivial vacuum expectation value corresponds to the gauge orbit topology?

If this connection can be made precise, it would provide a geometric interpretation of the Stueckelberg extension in terms of the fundamental non-perturbative structure of gauge theory, and potentially a route toward showing that the Stueckelberg mass gap is non-perturbatively stable.

**Key papers in this direction:**
- Gribov, "Quantization of Non-Abelian Gauge Theories" (1978) — the original paper
- Zwanziger, "Non-perturbative modification of the Faddeev–Popov formula and banishment of the naive vacuum" (1989)
- Dudal, Sorella, Vandersickel, Verschelde — the RGZ framework papers (2008–2012)
- Pereira, "Exploring new horizons of the Gribov problem in Yang–Mills theories" ([arXiv:1607.00365](https://arxiv.org/abs/1607.00365)) — a thorough review of extending the GZ framework beyond Landau gauge, directly relevant to the BRST compatibility question

The problem with the standard GZ approach is that it explicitly breaks BRST symmetry, making it difficult to extract gauge-invariant physical predictions. My Stueckelberg extension is BRST-invariant by construction. Whether a BRST-invariant version of the Gribov horizon restriction exists, and whether it coincides with the Stueckelberg extension, is a precise open question.

---

### Problem 1.3 — The Dyson–Schwinger Equations and Mass Generation

**Status:** Studying; not yet writing.

**What the problem is.** The Dyson–Schwinger equations (DSEs) are the quantum equations of motion for the full propagators and vertices of a QFT. For Yang–Mills theory in Landau gauge, the coupled DSEs for the gluon propagator, ghost propagator, and three-gluon vertex have been studied extensively through functional methods (truncated DSE systems, functional renormalisation group).

The result is that the gluon propagator saturates in the infrared rather than diverging as $1/k^2$: it acquires an effective mass. This was studied in detail by Huber, Fischer, and collaborators ([arXiv:2107.05352](https://arxiv.org/abs/2107.05352)), who showed that the mass gap generation is tied to the longitudinal projection of the gluon self-energy, which acts as an effective mass term. The question they could not answer was whether this effective mass term is an artefact of gauge fixing or a genuine gauge-invariant phenomenon.

**The connection.** The Stueckelberg extension provides a gauge-invariant mechanism that generates exactly this kind of longitudinal mass contribution. Understanding whether the Stueckelberg vacuum expectation value reproduces the DSE predictions for the gluon propagator would be a significant consistency check on the framework.

---

### Problem 1.4 — BRST Cohomology and Physical Observables

**Status:** Working on; part of the ongoing paper.

**What the problem is.** In BRST quantisation, physical observables are cohomology classes of the BRST operator $s$: they are $s$-closed operators that are not $s$-exact. The physical Hilbert space is the BRST cohomology $H^*(Q_\text{BRST})$.

In the Stueckelberg-extended theory, the BRST algebra is deformed by the Stueckelberg field. The question is: what is the BRST cohomology of the extended theory? Are the physical observables the same as in pure Yang–Mills, or does the Stueckelberg extension introduce new physical operators?

This matters because if the Stueckelberg field introduces new physical degrees of freedom (beyond the massive gauge boson), then the theory's physical spectrum is different from what the mass gap argument suggests. Getting the BRST cohomology right is a necessary step toward a complete understanding of the physical content of the theory.

---

### Problem 1.5 — Asymptotic Safety and the Stueckelberg Sector at Higher Loops

**Status:** Planned next computation.

**What the problem is.** I established at one loop that the Stueckelberg sector does not contribute to the beta function of $g$, and that asymptotic freedom is preserved. This is a one-loop result. At two loops, additional contributions can appear through:

- Mixed diagrams involving both the gauge field and the Stueckelberg field
- Renormalisation of the Stueckelberg kinetic term (which affects the mass renormalisation)
- Non-trivial mixing between the gauge field and the Stueckelberg field under renormalisation

The specific question is: does the Stueckelberg mass $m$ have a non-trivial fixed point structure under the RG flow? If the theory flows to an infrared fixed point with $m > 0$, that is evidence for an infrared stable mass gap.

---

## Cluster II — QGET: Quantum Geometric Entanglement Theory

### Problem 2.1 — The Classical Limit: Recovering General Relativity

**Status:** The central open problem in QGET. Actively working on.

**What the problem is.** QGET, as formulated in the 2023 paper, proposes that the spacetime metric $g_{\mu\nu}$ evolves according to

$$\frac{dg(t)}{dt} = \mathcal{E}(t) \otimes \mathcal{E}(t)^\dagger$$

where $\mathcal{E}(t)$ is the entanglement operator on the graph. This is a postulate. The central open problem is: in what limit does this equation reduce to the Einstein field equations $G_{\mu\nu} = 8\pi T_{\mu\nu}$?

Making this precise requires:
- Taking the continuum limit of the graph: as the number of nodes $N \to \infty$ with the graph spacing $\ell \to 0$, the discrete entanglement matrix should converge to a continuous distribution on a smooth manifold
- Identifying the entanglement tensor $\mathcal{E} \otimes \mathcal{E}^\dagger$ with the stress-energy tensor $T_{\mu\nu}$ in the appropriate limit
- Showing that the graph Laplacian (encoding the graph geometry) converges to the Ricci scalar in the continuum

Van Raamsdonk's 2010 paper ([arXiv:1005.3035](https://arxiv.org/abs/1005.3035)) argued heuristically that disentangling degrees of freedom causes spacetime to pull apart — that the Einstein equations can be thought of as the equations governing entanglement. QGET is an attempt to make that idea precise and computational. The gap between the heuristic and the rigorous derivation is large and is what this problem is asking.

**Recent context.** Hong Liu's October 2025 lectures ([arXiv:2510.07017](https://arxiv.org/abs/2510.07017)) review the use of von Neumann algebras to analyse entanglement in quantum gravity and the emergence of bulk spacetime structure through subregion–subalgebra duality. This algebraic framework — in which spacetime emerges as a derived structure from operator algebras — is potentially related to the QGET continuum limit, and I am reading this work carefully.

---

### Problem 2.2 — Connection to Loop Quantum Gravity

**Status:** Investigating.

**What the problem is.** Loop quantum gravity (LQG) also uses a graph-theoretic description of spacetime: the Hilbert space of kinematic states is spanned by spin network states, which are functionals of the $SU(2)$ holonomies of the Ashtekar connection along the edges of a graph. The spin foam formalism assigns transition amplitudes between spin network states.

The QGET entanglement graph $G$ with entanglement matrix $M_{ij}$ is structurally similar to a spin network: nodes connected by edges with values encoding correlations. The question is whether the QGET entanglement matrix $M_{ij}$ corresponds, in any precise sense, to the spin labels of a spin network, and whether the QGET evolution equation reduces to the spin foam transition amplitudes in some limit.

If this connection holds, QGET would be interpretable as a specific sector of LQG — one in which the entanglement structure of the kinematic Hilbert space is the primary object, rather than the holonomies of the Ashtekar connection.

This is speculative but not unmotivated. The relationship between entanglement and geometry in LQG has been studied by Livine, Bianchi, and others; the Ryu–Takayanagi formula and its generalisations suggest a precise relationship between entanglement entropy and geometric area in the context of holography; and the QGET framework was designed precisely to make the entanglement-geometry connection explicit.

---

### Problem 2.3 — Black Hole Information and the Page Curve

**Status:** Thinking about; not yet computing.

**What the problem is.** The black hole information paradox asks: when a black hole forms and then evaporates via Hawking radiation, is the process unitary (information preserved) or not (information destroyed)?

The QGET framework has a natural prediction: information is preserved because the entanglement structure of the geometric nodes is not destroyed by the horizon — it is redistributed. As the black hole evaporates, the entanglement edges connecting interior nodes to exterior nodes carry the information back out in the Hawking radiation.

Making this precise requires: defining the QGET evolution for a black hole spacetime (treating the horizon as a boundary of the entanglement graph), showing that the entanglement entropy of the Hawking radiation follows the Page curve (rising to a maximum and then decreasing, as required by unitarity), and connecting the QGET entanglement structure to the island formula of Penington, Almheiri, et al. (2019).

The recent island formula results — which do reproduce the Page curve from a gravitational path integral argument — suggest that the right way to think about black hole information is indeed in terms of the entanglement structure of spacetime regions. QGET, if its classical limit can be established, should make contact with these results naturally.

---

### Problem 2.4 — Testable Predictions: CMB Signatures

**Status:** Speculative; longer-horizon.

**What the problem is.** The QGET paper proposed that if spacetime emergence occurred during inflation, the process of entanglement graph formation could leave signatures in the cosmic microwave background. Specifically: if the primordial power spectrum of quantum fluctuations was generated from an underlying entanglement structure rather than a smooth quantum field, there might be characteristic angular correlations in the CMB that deviate from the predictions of standard slow-roll inflation.

Turning this from a qualitative statement into a quantitative prediction requires:
- A QGET model of inflation (treating the inflaton as a collective mode of the entanglement graph)
- Computing the two-point function of entanglement fluctuations in the inflationary background
- Translating this into a prediction for the primordial power spectrum and comparing to Planck and future CMB-S4 data

This is a long-horizon problem and requires the classical limit (Problem 2.1) to be established first. But it is the most concrete path toward making QGET empirically constrainable.

---

## Cluster III — Wider Open Problems I Am Watching

These are problems in the broader field that I am not currently working on but that intersect closely with my research and that I think about.

---

### Problem 3.1 — The Confinement Problem (Wilson Criterion)

The Wilson criterion for confinement requires that the expectation value of the Wilson loop operator $W(C) = \text{tr}\,\mathcal{P}\exp\left(ig\oint_C A_\mu dx^\mu\right)$ for a large rectangular loop $C$ of dimensions $R \times T$ satisfies the area law:

$$\langle W(C) \rangle \sim \exp(-\sigma R T)$$

for some string tension $\sigma > 0$. This would imply that the energy of a quark-antiquark pair separated by distance $R$ grows linearly with $R$ — precisely the confinement of quarks.

The area law has been verified in lattice simulations for $SU(N)$ gauge theories. Proving it analytically from the continuum Yang–Mills action remains completely open. The Stueckelberg extension generates a Yukawa confinement force at tree level (as shown in my first paper), but demonstrating the area law requires a non-perturbative argument that I do not yet have.

---

### Problem 3.2 — The Instanton Vacuum

Instantons are finite-action, self-dual solutions to the Euclidean Yang–Mills equations. They are topologically non-trivial field configurations (classified by the second Chern class, or instanton number) and contribute non-perturbatively to the Yang–Mills path integral. The instanton vacuum — the vacuum state of Yang–Mills theory dominated by a dilute gas of instantons — is conjectured to be responsible for chiral symmetry breaking and may be related to confinement.

The question of how the Stueckelberg extension modifies the instanton sector is one I intend to investigate. The group-valued Stueckelberg field $U \in G$ transforms non-trivially under the topological $\theta$ term, and the instanton number may be modified.

---

### Problem 3.3 — The ER=EPR Conjecture

Maldacena and Susskind conjectured in 2013 that an Einstein–Rosen bridge (a wormhole connecting two regions) is equivalent to an Einstein–Podolsky–Rosen pair (two maximally entangled particles): ER = EPR. If true, this would mean that any two entangled particles are connected by a Planck-scale wormhole.

The conjecture is supported by the eternal black hole in AdS, whose dual description in AdS/CFT is the thermofield double state — a maximally entangled state of two CFTs. Maldacena showed in 2001 that the dual geometry is a two-sided black hole connected by a wormhole. The ER=EPR conjecture says this correspondence is general.

QGET, if its classical limit can be established, would make a specific prediction: that the entanglement edges of the QGET graph correspond exactly to Planck-scale wormholes, and that the QGET evolution equation governs the geometry of these wormholes. This is a natural extension of the framework but requires the classical limit first.

A recent paper ([arXiv:2512.05022](https://arxiv.org/abs/2512.05022)) derives a concrete realization of ER = EPR within a regularized spacetime by showing that two entangled particles source an Einstein–Rosen geometry. This is the direction QGET should ultimately connect to.

---

### Problem 3.4 — Chiral Symmetry Breaking

In QCD with massless quarks, the theory has a chiral symmetry $SU(N_f)_L \times SU(N_f)_R$ that is spontaneously broken to $SU(N_f)_V$ by the quark condensate $\langle\bar\psi\psi\rangle \neq 0$. This breaking produces the pseudo-Goldstone bosons — the pions. Understanding this spontaneous breaking from first principles of Yang–Mills theory (without phenomenological models) is closely related to the confinement problem.

The Banks–Casher relation connects the quark condensate to the density of near-zero modes of the Dirac operator: $\langle\bar\psi\psi\rangle = -\pi\rho(0)$. This connects chiral symmetry breaking to the spectrum of the Dirac operator in a gauge background — a problem in spectral geometry with connections to the Atiyah–Singer index theorem.

---

### Problem 3.5 — Quantum Gravity in de Sitter Space

Most of the precision results connecting entanglement and geometry (Van Raamsdonk, Ryu–Takayanagi, the island formula) are in the context of AdS/CFT — anti-de Sitter spacetime with a negative cosmological constant. Our universe has a positive cosmological constant and is asymptotically de Sitter, not anti-de Sitter.

Whether AdS/CFT intuitions extend to de Sitter space is a fundamental open question. Recent work has explored the ER=EPR conjecture in de Sitter ([arXiv:2409.13932](https://arxiv.org/abs/2409.13932)), arguing that de Sitter spacetime itself emerges from quantum entanglement between two CFTs. If this picture is correct, the QGET framework should apply to de Sitter as well as AdS, and the QGET graph might have a natural de Sitter-invariant structure.

Holographic entanglement entropy in de Sitter is reviewed in the context of recent developments in [arXiv:2506.06595](https://arxiv.org/abs/2506.06595) (Takayanagi, 2025). The extension of the holographic programme to cosmological spacetimes is a live research front.

---

## The Common Thread

Looking at all of these problems together, a single theme runs through them: the relationship between gauge structure, topology, and the non-perturbative physics of strongly-coupled field theories.

The mass gap, confinement, the Gribov problem, instantons, chiral symmetry breaking — these are all aspects of the same underlying problem, which is understanding what happens to gauge theory when perturbation theory breaks down. The Stueckelberg extension is a specific proposal for how one piece of this — mass generation — works. Whether it connects correctly to the others is the question that will occupy the next several years of work.

The QGET programme is asking a complementary question at a more fundamental level: where does the spacetime in which gauge theories live come from? If the entanglement-geometry connection can be made precise, it might change how we think about the gauge structure itself — gauge symmetry as a consequence of the entanglement geometry rather than a fundamental postulate.

I do not know if either of these programmes will succeed. That is what makes them worth working on.

---

*Last updated March 2026. This page is updated as the research develops.*