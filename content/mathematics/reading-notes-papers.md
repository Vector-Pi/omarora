---
title: "Reading Notes & Papers"
date: 2026-02-06
parent: "Mathematics"
---

This page is a working log. It is not a curated list of the greatest papers in mathematics — that would be a different project, and a longer one. It is a record of what I have actually read, what I found important, what confused me, and what I intend to return to.

The papers are organised by area. Within each area I have tried to distinguish between foundational papers worth reading for background, significant papers from the last decade, and very recent results from the last year or two that I went through recently. Where I have notes or reactions they are included. Where a paper is beyond what I can currently assess technically, I say so.

The arXiv identifiers link directly to the abstracts. For papers with accessible survey articles or blog posts, I have included those too — Terence Tao's blog in particular is an invaluable companion to many recent results.

---

## How to Use arXiv

[arxiv.org](https://arxiv.org/archive/math) is where essentially all new mathematics appears first, before journal publication. The mathematics section is divided into subcategories — math.NT for number theory, math.AG for algebraic geometry, math.AP for analysis and PDEs, and so on. The most useful habit is to check the recent listings in whichever areas you care about once or twice a week.

For navigating a paper you do not yet have the background for, the standard approach is: read the abstract and introduction carefully; read the statement of the main theorem; read the proof sketch if one exists; come back for the details later. Almost no one reads every proof in every paper from start to finish. The introduction is where the author explains what the result means and why it is hard — this is often the most valuable part.

---

## Number Theory

### Foundational Reading

**Riemann, "Über die Anzahl der Primzahlen unter einer gegebenen Grösse" (1859)**
Eight pages. The paper that introduced the Riemann zeta function in its complex form, stated the Riemann Hypothesis, and sketched a proof of the prime number theorem. It contains more ideas per page than almost anything else written in the 19th century. Available freely online. Read the English translation by Wilkins. It is short enough that there is no excuse not to.

**Gauss, *Disquisitiones Arithmeticae* (1801)**
The foundational text of modern number theory. Congruences, quadratic residues, the theorem on quadratic forms. Historically important and still worth reading the early sections directly. The full text is long; the first three sections are the most accessible and contain the key ideas.

**Dirichlet, "Beweis des Satzes, dass jede unbegrenzte arithmetische Progression..." (1837)**
The proof that every arithmetic progression $a, a+d, a+2d, \ldots$ with $\gcd(a,d)=1$ contains infinitely many primes. This is where $L$-functions were invented. The argument is still beautiful and the paper is readable with a modern background in analysis.

### Papers I Have Read

**Taylor and Wiles, "Ring-Theoretic Properties of Certain Hecke Algebras" (1995)** and **Wiles, "Modular Elliptic Curves and Fermat's Last Theorem" (1995)**
The pair of papers that proved Fermat's Last Theorem by establishing the modularity theorem for semistable elliptic curves. The Wiles paper alone is 109 pages. I have not read it in full — that would require considerably more algebraic number theory than I currently have — but I have worked through the structure of the argument and the key ingredients (Galois representations, Hecke algebras, deformation theory). The Taylor–Wiles paper fills the gap in the original argument that Wiles discovered after the initial announcement in 1993.

**Green and Tao, "The Primes Contain Arbitrarily Long Arithmetic Progressions" (2004)** — [math.NT/0404188](https://arxiv.org/abs/math/0404188)
One of the most striking results of the early 21st century: the prime numbers contain arithmetic progressions of any finite length. The proof combines Szemerédi's theorem on arithmetic progressions in dense sets with a transference principle showing that the primes behave, in the relevant sense, like a dense set. I worked through the paper alongside expository notes. The transference principle is the key idea and is not easy to understand on a first pass.

**Zhang, "Bounded Gaps Between Primes" (2013)** — Annals of Mathematics 179 (2014)
The first proof that there exist infinitely many pairs of primes separated by a bounded gap. Zhang's bound was $70{,}000{,}000$; subsequent work (the Polymath8 project) reduced this to $246$, and conditionally to $6$ assuming the Elliott–Halberstam conjecture. The argument uses the Goldston–Pintz–Yıldırım sieve method. Zhang, then a relatively unknown mathematician, had been working on this in near-isolation.

**Deng, Hani, Ma, "Hilbert's Sixth Problem: Derivation of Fluid Equations via Boltzmann's Kinetic Theory" (2025)** — [arXiv:2503.01800](https://arxiv.org/abs/2503.01800)
Technically this is analysis and mathematical physics rather than number theory, but its significance warrants mention early. In March 2025 the authors claimed to have rigorously derived the compressible Euler and incompressible Navier–Stokes–Fourier equations from Newton's laws via Boltzmann's kinetic theory — resolving the fluid mechanics part of Hilbert's sixth problem. The proof requires long-time analysis of Boltzmann's equation on 2D and 3D tori. A critical comment ([arXiv:2504.06297](https://arxiv.org/abs/2504.06297)) by Shan Gao argues the physical interpretation is incomplete. This debate is still unresolved as of early 2026. I went through the introduction and the structure of the argument — the technical details in the main proof are beyond my current analysis background.

---

## Analysis and PDEs

### Foundational Reading

**Fourier, *Théorie analytique de la chaleur* (1822)**
The work that introduced Fourier series. The mathematics is not rigorous by modern standards — Fourier's argument that every function has a Fourier series expansion is simply false in the generality he states it — but the ideas were so productive that they generated a century of subsequent work to make them precise. Worth reading at least the opening chapters.

**Lebesgue, "Intégrale, longueur, aire" (1902)**
The thesis in which Lebesgue introduced his theory of integration. The Lebesgue integral replaced the Riemann integral with something that behaves well under limits and underlies all of modern analysis and probability theory. The original paper is readable with basic analysis preparation.

### Papers I Have Read

**Tao and Vu, *Additive Combinatorics* (2006)**
A book rather than a paper. Additive combinatorics studies the additive structure of sets of integers and has become one of the most active areas in mathematics, connecting to number theory, ergodic theory, and harmonic analysis. I have read the chapters on Fourier analysis on finite groups and the Freiman–Ruzsa theorem.

**Klainerman and Rodnianski (various), work on the stability of Minkowski space**
A series of papers in the 2000s and 2010s developing sharp estimates for the Einstein vacuum equations. Relevant to my interest in mathematical physics. The PDE techniques — bilinear estimates, the $r^p$ method — appear throughout modern mathematical GR.

**Wang and Zahl, "Volume Estimates for Unions of Convex Sets, and the Kakeya Set Conjecture in Three Dimensions" (2025)** — [arXiv:2502.17655](https://arxiv.org/abs/2502.17655)
In February 2025, Hong Wang and Joshua Zahl proved the Kakeya set conjecture in three dimensions — a problem that had been open for fifty years. The conjecture states that a Kakeya set (a compact subset of $\mathbb{R}^3$ containing a unit line segment in every direction) must have Hausdorff and Minkowski dimension 3. Nets Katz described it as "a once-in-a-century kind of result." The key innovation is a reduction to the sticky case (established in an earlier paper [arXiv:2210.09581](https://arxiv.org/abs/2210.09581)) combined with new estimates for unions of convex sets. Tao has written an excellent exposition on his blog. I went through the exposition and the structure of the sticky reduction.

**Guth, "Introduction to the Proof of the Kakeya Conjecture" (2025)** — [arXiv:2505.07695](https://arxiv.org/abs/2505.07695)
A survey article by Larry Guth explaining the Wang–Zahl proof for readers who know the background but want the key ideas before tackling the original. More approachable than the full paper and worth reading alongside Tao's blog post.

---

## Geometry and Topology

### Foundational Reading

**Riemann, "Über die Hypothesen, welche der Geometrie zu Grunde liegen" (1854)**
The habilitation lecture in which Riemann introduced the concept of a Riemannian manifold — a space with a local notion of distance — and speculated about the geometry of physical space. The ideas in this paper eventually became the mathematical foundation of general relativity. The lecture is short, conceptual, and does not assume much technical background.

**Poincaré, *Analysis Situs* (1895) and the five supplements**
The founding papers of algebraic topology. Poincaré introduced homology groups, the fundamental group, and the Poincaré duality theorem. The writing is difficult by modern standards and the proofs sometimes have gaps, but the ideas are entirely original. Reading the introduction to Analysis Situs gives a sense of how Poincaré was thinking about topology.

**Thurston, "Three-Dimensional Manifolds, Kleinian Groups and Hyperbolic Geometry" (1982)**
The bulletin article accompanying Thurston's geometrisation programme for 3-manifolds, which proposed that every closed 3-manifold admits a canonical geometric decomposition. Perelman proved this in 2003. The bulletin article is readable and explains the motivation clearly. Thurston's expository style is unusual — he thinks geometrically and writes that way.

### Papers I Have Read

**Perelman, "The Entropy Formula for the Ricci Flow and Its Geometric Applications" (2002)** — [math.DG/0211159](https://arxiv.org/abs/math/0211159); **"Ricci Flow with Surgery on Three-Manifolds" (2003)** — [math.DG/0303109](https://arxiv.org/abs/math/0303109)
The two papers in which Perelman proved the Poincaré conjecture (and Thurston's geometrisation conjecture) using Ricci flow with surgery. The proofs are dense and require significant background in Riemannian geometry and PDE theory. I have not read them in full — the technical machinery is substantial — but I have read multiple expository accounts and understand the structure of the argument.

**Atiyah and Singer, "The Index of Elliptic Operators: I" (1968)** — Annals of Mathematics
The first paper in the series establishing the Atiyah–Singer index theorem, which relates the analytical index of an elliptic operator to topological invariants of the manifold. One of the deepest results of 20th-century mathematics, connecting analysis, topology, and geometry. The later papers in the series develop the K-theory approach. I have read expository treatments and worked through the statement in specific cases.

**Gaitsgory and Raskin, "Proof of the Geometric Langlands Conjecture I–V" (2024)** — [arXiv:2405.03599](https://arxiv.org/abs/2405.03599) through [arXiv:2409.09856](https://arxiv.org/abs/2409.09856)
In May–September 2024, a team of nine mathematicians including Dennis Gaitsgory and Sam Raskin released five papers totalling over 1,000 pages proving the geometric Langlands conjecture. The conjecture — a central part of the Langlands programme connecting number theory, representation theory, and algebraic geometry — had been open for decades. The proof establishes the existence of a canonical equivalence between two categories associated to a Riemann surface: one encoding automorphic sheaves (related to geometry) and one encoding local systems (related to representation theory). The papers are at the frontier of algebraic geometry and require fluency in $\infty$-categories, D-modules, and the theory of ind-coherent sheaves. I have read the introduction to GLC-I carefully and several expository accounts. The ideas involved are extraordinary in scope.

---

## Algebra and Representation Theory

### Foundational Reading

**Galois, manuscript on the theory of equations (c. 1831, published posthumously)**
The text in which Galois introduced what we now call Galois groups and gave a criterion for a polynomial equation to be solvable by radicals. Written by Galois the night before his fatal duel. The mathematics is correct and deep; the presentation is compressed to the point of being difficult to follow even for experts at the time. Accessible through modern translations.

**Noether, "Idealtheorie in Ringbereichen" (1921)**
The paper in which Emmy Noether introduced the concept of an ideal in a general ring and established the ascending chain condition as the key finiteness property. Modern commutative algebra begins here.

### Papers I Have Read

**Wiles, work on the modularity theorem** — referenced above under Number Theory.

**Lurie, "Higher Topos Theory" (2009)** — [math.CT/0608040](https://arxiv.org/abs/math/0608040)
A foundational text establishing the theory of $(\infty,1)$-categories (specifically quasi-categories) on rigorous footing. 750 pages. I have not read this in full — no one reads it in full — but I have worked through Chapter 1 and referenced specific sections as needed. The theory of $\infty$-categories is now the language in which much of algebraic geometry and algebraic topology is done, including the geometric Langlands proof.

**Bezrukavnikov and Koszul duality** — various papers
Work by Roman Bezrukavnikov on Koszul duality patterns in representation theory, connecting to the geometric Langlands correspondence. Technically very demanding but relevant to understanding the structure of the GLC proof.

---

## Combinatorics and Graph Theory

### Foundational Reading

**Erdős and Szekeres, "A Combinatorial Problem in Geometry" (1935)**
The paper that introduced the Erdős–Szekeres theorem: any sequence of more than $(r-1)(s-1)$ distinct real numbers contains an increasing subsequence of length $r$ or a decreasing subsequence of length $s$. Short, clean, and the beginning of Ramsey theory as a subject. Read it — it takes twenty minutes.

**Ramsey, "On a Problem of Formal Logic" (1930)**
The original Ramsey theory paper, proving the finite and infinite Ramsey theorems as lemmas in a study of formal logic. The mathematical content is now standard but the historical context is interesting.

**Szemerédi, "On Sets of Integers Containing No $k$ Elements in Arithmetic Progression" (1975)**
Szemerédi's theorem: every subset of the integers with positive upper density contains arithmetic progressions of any finite length. The proof is a combinatorial tour de force. The subsequent proofs by Furstenberg (ergodic theory) and Gowers (Fourier analysis) are more influential, but Szemerédi's original proof is worth knowing.

### Papers I Have Read

**Gowers, "A New Proof of Szemerédi's Theorem" (2001)**
The proof using higher-order Fourier analysis (Gowers uniformity norms) that also gave quantitative bounds substantially stronger than previous methods. The paper introduced the Gowers norms, which became fundamental tools in additive combinatorics. I have read this alongside Tao and Vu's treatment.

**Hales and Jewett, "Regularity and Positional Games" (1963)**
The Hales–Jewett theorem is a combinatorial Ramsey-type result underlying Szemerédi's theorem in a certain sense. The density version (Furstenberg–Katznelson, 1991) is harder.

---

## Mathematical Physics (Mathematics Side)

These are papers at the intersection of mathematics and physics where the focus is mathematical rigour rather than physical motivation. I include them here because they connect most directly to my own research interests.

### Papers I Have Read and Am Working Through

**Jaffe and Witten, "Quantum Yang–Mills Theory"** — Clay Millennium Problem description
The official problem statement for the Yang–Mills existence and mass gap problem, one of the seven Millennium Prize Problems. Establishes what a rigorous solution would need to prove. I have read this carefully and repeatedly, as it is directly relevant to my own work on Stueckelberg extensions. The key difficulty is constructing a quantum Yang–Mills theory on $\mathbb{R}^4$ with a positive mass gap rigorously — a problem that remains completely open.

**Faddeev and Popov, "Feynman Diagrams for the Yang–Mills Field" (1967)**
The paper introducing the Faddeev–Popov ghost fields and the path-integral approach to quantising non-abelian gauge theories. Essential background for BRST quantisation. Short and worth reading in its original form.

**Becchi, Rouet, Stora, "Renormalization of Gauge Theories" (1976)**
One of the BRST papers. Introduces the BRST operator as a global symmetry of the gauge-fixed Yang–Mills action, replacing the local gauge symmetry. Directly relevant to the quantisation approach in my own papers.

**Haag, Kastler, "An Algebraic Approach to Quantum Field Theory" (1964)**
The foundational paper of algebraic quantum field theory (AQFT), which treats quantum fields as nets of operator algebras satisfying axioms. Mathematically rigorous where the Lagrangian path-integral approach is not. I am working through this as background for understanding what a rigorous quantum Yang–Mills theory would look like.

**Donaldson, "Self-Dual Connections and the Topology of Smooth 4-Manifolds" (1983)** — Journal of Differential Geometry
Donaldson's use of Yang–Mills instantons (self-dual connections) to prove new results about the topology of smooth 4-manifolds, culminating in his theorem that $\mathbb{R}^4$ has infinitely many distinct smooth structures. One of the most remarkable applications of gauge theory to pure mathematics.

**Witten, "Monopoles and 4-Manifolds" (1994)** and the introduction of Seiberg–Witten theory
Following the Seiberg–Witten paper on electric-magnetic duality, Witten showed that Seiberg–Witten invariants give a simpler and more powerful alternative to Donaldson invariants for studying smooth 4-manifolds. The mathematical theory is cleaner than Donaldson's. I have read the original Witten paper and Kronheimer–Mrowka's mathematical treatment.

---

## Very Recent: Papers I Went Through in Early 2026

These are papers from the last few months that I went through recently, in varying levels of depth.

**Baek, "Optimality of Gerver's Sofa" (2024)** — [arXiv:2411.19826](https://arxiv.org/abs/2411.19826)
Resolves the moving sofa problem, posed by Leo Moser in 1966: what is the largest planar region that can be manoeuvred around a right-angle corner in a unit-width corridor? Baek proves that Gerver's 1992 construction (area $2.2195\ldots$, defined by 18 curve segments) is optimal. The proof is 119 pages and uses variational calculus and geometric analysis. The paper is currently under review at the *Annals of Mathematics*. I went through the introduction and the structure of the variational argument.

**Deng, Hani, Ma, "Hilbert's Sixth Problem" (2025)** — [arXiv:2503.01800](https://arxiv.org/abs/2503.01800)
Referenced above. Fluid dynamics from Newton's laws, long-time derivation of Boltzmann's equation. Still under expert scrutiny. The debate over whether the result resolves the physical question (as opposed to the mathematical one) is genuinely interesting and ongoing.

**Wang, Zahl, "Volume Estimates for Unions of Convex Sets, and the Kakeya Set Conjecture in Three Dimensions" (2025)** — [arXiv:2502.17655](https://arxiv.org/abs/2502.17655)
Also referenced above. The Kakeya conjecture in $\mathbb{R}^3$.

**Recent work on the Langlands programme, January 2026 updates** — [arXiv:2409.09856](https://arxiv.org/abs/2409.09856) (GLC V, updated)
The final paper in the geometric Langlands series was updated in January 2026. The programme continues to develop; the arithmetic (as opposed to geometric) Langlands correspondence remains completely open.

**Ren, Wang, "The Furstenberg Set Conjecture" (2024)**
Proved the Furstenberg set conjecture, which is closely related to the Kakeya conjecture and was a stepping stone to the Wang–Zahl result. The proof uses Fourier analytic methods.

---

## Reading Resources

**arXiv mathematics listings** — [arxiv.org/archive/math](https://arxiv.org/archive/math). The primary source. Sorted by area. The new listings appear every weekday.

**Terence Tao's blog** — [terrytao.wordpress.com](https://terrytao.wordpress.com). Tao writes expository posts on recent results, open problems, and his own research. The post on the Wang–Zahl Kakeya proof is the best non-technical explanation of that result. The posts on the Green–Tao theorem, the Erdős discrepancy problem, and Sendov's conjecture are all worth reading.

**Quanta Magazine mathematics section** — [quantamagazine.org](https://www.quantamagazine.org/mathematics/). High-quality journalism on current mathematical results. The coverage of the Kakeya result and the geometric Langlands proof has been excellent.

**MathOverflow** — [mathoverflow.net](https://mathoverflow.net). Questions and answers from working mathematicians. The "big-list" questions asking for important open problems or historically significant results are particularly valuable for orientation.

**Seminaire Bourbaki** — [bourbaki.fr](http://www.bourbaki.fr). Expository talks on significant recent results, given at the Bourbaki seminar in Paris. Each talk is written by a mathematician explaining another mathematician's result. High quality and thorough.

**Princeton Companion to Mathematics** — Gowers (editor), Princeton University Press. Not a paper, but the survey articles on individual areas of mathematics are among the best available overviews. The articles on the Langlands programme, on Riemannian geometry, and on the relationship between mathematics and physics are particularly good.

---

*This page is updated as I read. Last updated March 2026.*