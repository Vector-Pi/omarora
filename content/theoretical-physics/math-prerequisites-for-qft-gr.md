---
title: "Math Prerequisites for QFT & GR"
date: 2026-03-24
parent: "Theoretical Physics"
---


There is a version of this guide that lists twenty subjects, provides no ordering, and leaves you with no idea where to start. This is not that version.

What follows is the complete mathematical infrastructure for serious work in quantum field theory and general relativity — every subject, in the order you should encounter it, with honest assessments of why each one is needed and which resources are actually worth your time. The guide is structured in tiers: foundations that everyone needs before anything else; intermediate mathematics that comes alongside the physics; and advanced mathematics that becomes necessary as you approach gauge theory, BRST quantisation, and differential geometric GR.

I have worked through most of this material. Where I have not, I say so. The resources I recommend are ones I have either used directly or have examined carefully.

---

## How to Use This Guide

The mathematics and physics develop together. You do not need to complete all of calculus before beginning mechanics, or all of differential geometry before beginning GR. What you do need is to never be more than a little ahead of the mathematics when you open a physics text.

The guide is divided into six tiers:

- **Tier 0** — Before everything: proof-writing and basic set theory
- **Tier 1** — Calculus and linear algebra
- **Tier 2** — Intermediate analysis, ODEs, PDEs
- **Tier 3** — Complex analysis, Fourier analysis, group theory
- **Tier 4** — Differential geometry, topology, Lie groups and Lie algebras
- **Tier 5** — Advanced: functional analysis, fibre bundles, algebraic topology, index theory

Each tier is a prerequisite for the next. The physics you can do expands substantially at each tier.

---

## Tier 0 — Proof-Writing and Logic

### Why it matters

Everything in this guide involves reading and writing proofs. Doing physics at this level without being able to follow a mathematical argument is like trying to read a text in a language you do not know. You will get an impression. You will not understand it.

This tier is not glamorous and most people skip it. Skipping it is a mistake that costs months later.

### What you need

- Propositional and predicate logic: what a valid argument is
- Set theory: sets, functions, relations, cardinality
- Proof techniques: direct proof, proof by contradiction, proof by induction, contrapositive
- The language of mathematics: quantifiers, definitions, theorems, lemmas, corollaries

### Resources

**Book of Proof** — Richard Hammack
Free at [bookofproof.com](https://richardhammack.github.io/BookOfProof/Main.pdf). The most accessible introduction to proof-writing. Read Parts I and II before anything else on this page.

**How to Prove It** — Daniel Velleman
More thorough than Hammack, structured around logic and set theory from the ground up. The chapter on mathematical induction is excellent. If you have time, do this alongside Hammack rather than instead of it.

**How to Solve It** — George Pólya
Not a proof-writing book in the technical sense — more a philosophy of mathematical problem-solving. Read it once at the start. It changes how you approach every problem you encounter subsequently.

---

## Tier 1 — Calculus and Linear Algebra

These two subjects are the substrate of everything else. Weak calculus or weak linear algebra creates problems at every subsequent stage. Do not move past this tier until you are genuinely fluent.

### 1A. Calculus

#### What you need

**Single-variable calculus:** limits, derivatives, the fundamental theorem of calculus, integration techniques, Taylor series, sequences and series. Convergence matters — a physicist who does not understand what it means for a series to converge will make errors throughout their career.

**Multivariable calculus:** partial derivatives, the gradient, directional derivatives, multiple integrals, change of variables (Jacobians). The chain rule in higher dimensions. Lagrange multipliers.

**Vector calculus:** the gradient, divergence, and curl as objects with geometric meaning — not just formulas. The integral theorems — Green's theorem, Stokes' theorem, the divergence theorem. These theorems appear in electrodynamics, in the action principle, and in differential geometry.

#### Resources

**Calculus** — Michael Spivak
The rigorous treatment. Spivak proves everything carefully and forces you to understand why calculus works, not just how to use it. Slow and demanding; worth it. This is the calculus that mathematicians actually use.

**Calculus** — James Stewart
The standard university calculus textbook. Less demanding than Spivak, more comprehensive in its coverage of techniques. Use it for computational fluency if Spivak is too slow. The multivariable chapters are reliable.

**Calculus on Manifolds** — Michael Spivak
The short, rigorous treatment of multivariable calculus that leads directly into differential geometry. 140 pages. Dense but essential. Read this after basic multivariable calculus and before differential geometry.

**Vector Calculus, Linear Algebra, and Differential Forms** — Hubbard and Hubbard
A unified treatment that does all three subjects together, emphasising the geometric meaning of each operation. The treatment of differential forms as the natural objects for integration is excellent and unusual at this level.

**David Tong's Vector Calculus lecture notes** — [damtp.cam.ac.uk/user/tong/teaching.html](http://www.damtp.cam.ac.uk/user/tong/teaching.html)
Free. Cambridge Part IA level. Covers gradient, divergence, curl, and the integral theorems with physical applications throughout. An ideal supplement to any calculus textbook.

---

### 1B. Linear Algebra

#### What you need

The critical distinction: do not learn linear algebra as matrix manipulation. Learning linear algebra as matrix manipulation is learning a dialect of the subject, not the subject itself. You need the abstract framework — vector spaces, linear maps, eigenvalues — because this is what quantum mechanics and QFT are built on. Matrices are representations of linear maps, not the primary objects.

**Core topics:**
- Abstract vector spaces and subspaces
- Linear maps and their matrices
- Bases, dimension, change of basis
- Eigenvalues and eigenvectors, diagonalisation
- Inner product spaces, orthonormal bases, the Gram–Schmidt process
- Self-adjoint (Hermitian) and unitary operators
- The spectral theorem
- Tensor products of vector spaces
- Dual spaces and covectors

#### Resources

**Linear Algebra Done Right** — Sheldon Axler
The right book. Axler banishes determinants until the final chapter and builds the entire theory from linear maps. This is the approach that transfers to quantum mechanics and QFT. The treatment of self-adjoint operators and the spectral theorem is exactly what you need for quantum mechanics.

**Linear Algebra** — Friedberg, Insel, Spence
More comprehensive than Axler, with determinants treated throughout. Reliable as a second read or reference. The problems are well-chosen.

**Linear Algebra and Its Applications** — Gilbert Strang
Strang's MIT OpenCourseWare lectures are free and outstanding for building computational intuition. Watch them if the abstract approach in Axler is moving too slowly. But after Strang, read Axler — the abstract framework is what you actually need.

**Introduction to Linear Algebra** — Strang (companion textbook to the OCW course)
The most used linear algebra textbook in the world. Reliable for computational fluency. Not the final word on the subject.

**A note on tensor products:** most linear algebra courses do not cover tensor products seriously. They are central to QFT and to differential geometry. The treatment in Axler's later chapters is a starting point; a more thorough treatment is in the Hubbard–Hubbard book above and in Nakahara (Tier 4).

---

## Tier 2 — Intermediate Analysis, ODEs, PDEs

### 2A. Real Analysis

#### Why it matters

Real analysis is why calculus works. The formal theory of limits, the precise definitions of continuity and differentiability, the theory of integration — these underlie everything. In physics, you use results from real analysis constantly without necessarily formalising them. But when things go wrong (divergent integrals, distributions, the rigorous path integral), you need the theory underneath.

#### What you need

- The real number system: completeness, supremum, infimum
- Sequences and their convergence: the Cauchy criterion, subsequences, the Bolzano–Weierstrass theorem
- Continuous functions: uniform continuity, intermediate value theorem, extreme value theorem
- Differentiation: mean value theorem, Taylor's theorem with remainder
- Integration: Riemann integral, improper integrals, the fundamental theorem
- Sequences and series of functions: pointwise and uniform convergence
- The Lebesgue integral (at least the definitions and the key theorems: monotone convergence, dominated convergence)

#### Resources

**Understanding Analysis** — Stephen Abbott
The humane entry point. Abbott explains motivation before formalism and gives you time to assimilate each idea. The chapter on uniform convergence and the chapter on the Cantor set are particularly good. Read this first.

**Principles of Mathematical Analysis** — Walter Rudin (Baby Rudin)
Terse, elegant, demanding, correct. Every proof is exactly right. Work through it slowly — this is the standard that physicists doing serious mathematics are held to. Use Abbott to understand what Rudin is doing and why.

**Real Mathematical Analysis** — Charles Pugh
Between Abbott and Rudin in style, with better visual intuition. An excellent second read.

---

### 2B. Ordinary Differential Equations

#### Why it matters

Every equation of motion in classical mechanics is an ODE. The Schrödinger equation for time-independent problems reduces to ODEs. The geodesic equation in GR is an ODE system. Knowing ODEs is knowing the basic language of dynamics.

#### What you need

- First-order ODEs: separation of variables, integrating factors, exact equations
- Second-order linear ODEs with constant coefficients
- The method of Frobenius (power series solutions): essential for special functions
- Systems of ODEs and phase plane analysis
- Existence and uniqueness (Picard's theorem)
- Special functions: Legendre polynomials, Bessel functions, spherical harmonics — these arise constantly in physics

#### Resources

**Ordinary Differential Equations** — V.I. Arnold
The geometric approach to ODEs, emphasising phase flows and the qualitative behaviour of solutions. More abstract than most physics ODE courses but more illuminating. Arnold's writing is exceptional. Read this alongside a more computational treatment.

**Ordinary Differential Equations** — Tenenbaum and Pollard
Comprehensive, systematic, and practical. Good for building technique before Arnold.

**Mathematical Methods for Physics and Engineering** — Riley, Hobson, Bence
The encyclopaedic reference for mathematical methods in physics. Covers ODEs, PDEs, complex analysis, linear algebra, group theory, Fourier analysis, and more. Not the deepest treatment of any individual subject but reliable and comprehensive. Use it as a reference alongside more focused texts.

---

### 2C. Partial Differential Equations

#### Why it matters

The fundamental equations of physics are PDEs: Maxwell's equations, the Schrödinger equation, the Klein–Gordon equation, the Dirac equation, the Einstein field equations. Understanding PDEs at a meaningful level — not just knowing techniques but understanding what the solutions mean and why they behave as they do — is essential.

#### What you need

- Classification: elliptic, parabolic, hyperbolic
- The wave equation: d'Alembert's solution, solutions on bounded domains
- The heat equation: separation of variables, the diffusion kernel
- Laplace's equation: separation of variables, harmonic functions, boundary value problems
- The method of characteristics
- Green's functions: the fundamental solution, the free-space Green's function, physical interpretation
- Sturm–Liouville theory: eigenfunction expansions, completeness
- The Fourier transform as a PDE tool

#### Resources

**Introduction to Partial Differential Equations** — Walter Strauss
Clear, concise, and focused on the main examples. Good for a first systematic treatment.

**Partial Differential Equations** — Lawrence Evans
The rigorous graduate treatment. Demanding but the standard reference. The treatment of Sobolev spaces and weak solutions is the foundation for mathematical QFT.

**Partial Differential Equations in Physics** — Arnold Sommerfeld (Lectures on Theoretical Physics, Vol. 6)
An older text but still excellent for physical intuition. Sommerfeld connects PDEs directly to physics throughout.

**David Tong's lecture notes on various topics** cover PDEs implicitly throughout the electrodynamics and field theory notes.

---

## Tier 3 — Complex Analysis, Fourier Analysis, Group Theory

### 3A. Complex Analysis

#### Why it matters

Complex analysis is indispensable for QFT. Propagators in quantum field theory are distributions with poles in the complex plane; evaluating them requires contour integration. The $i\varepsilon$ prescription for the Feynman propagator is a statement about which side of the poles in the complex energy plane the contour passes. The analytic structure of scattering amplitudes is encoded in branch cuts and Riemann sheets. Dispersion relations use the Cauchy integral theorem. None of this makes sense without complex analysis.

#### What you need

- Holomorphic functions and the Cauchy–Riemann equations
- Contour integration: the Cauchy integral theorem and Cauchy integral formula
- Laurent series and poles
- The residue theorem and its applications
- Analytic continuation
- Branch cuts and multi-valued functions (logarithm, square root)
- The argument principle and Rouché's theorem
- Conformal mappings

#### Resources

**Visual Complex Analysis** — Tristan Needham
The geometric approach. Needham shows you what complex analysis looks like before writing down any formulas. The treatment of Möbius transformations, conformal maps, and the argument principle through visual intuition is unique. Read this first — it builds the geometric picture that makes the formalism natural.

**Complex Analysis** — Elias Stein and Rami Shakarchi
The best conventional treatment. Part of the Princeton Lectures in Analysis. Rigorous, clear, and full of connections to other areas. The chapters on the Fourier transform and the Gamma function are particularly relevant to physics.

**Complex Variables and Applications** — Churchill and Brown
The standard physics-oriented complex analysis textbook. Less demanding than Stein–Shakarchi but covers the contour integration and residue theorem material that physics needs. Use it for computational practice.

**Complex Analysis** — Lars Ahlfors
The classic graduate reference. More demanding than either of the above. Worth knowing; not the first book.

---

### 3B. Fourier Analysis

#### Why it matters

Fourier analysis is the mathematical foundation of the momentum representation in quantum mechanics, of field theory in momentum space, of the Feynman propagator, of signal processing and the Green's function method for PDEs. The relationship between position and momentum in quantum mechanics is the Fourier transform. You cannot understand QFT without understanding Fourier analysis.

#### What you need

- Fourier series: convergence, Parseval's theorem, completeness
- The Fourier transform and inverse transform
- Properties: linearity, shift, convolution theorem, Plancherel's theorem
- Distributions (generalised functions): the Dirac delta, principal value, step function
- The Schwartz space and tempered distributions
- The Fourier transform of distributions
- Applications to PDEs and to quantum mechanics

#### Resources

**Fourier Analysis: An Introduction** — Stein and Shakarchi (Princeton Lectures in Analysis, Vol. 1)
The rigorous treatment of Fourier series and the Fourier transform, with applications throughout. The chapters on distributions are the best starting point for the generalised function theory you need for QFT.

**The Fourier Transform and Its Applications** — Bracewell
The engineer's approach, but with excellent physical intuition. Good for building the operational understanding before the rigorous theory.

**Distributions and Their Applications in Physics** — Friedlander
The precise mathematical treatment of distributions. Essential reading before you encounter the Feynman propagator.

**Mathematical Methods for Physicists** — Arfken and Weber
Covers Fourier analysis alongside every other mathematical method used in physics. Less rigorous than dedicated treatments but comprehensive and physically motivated. A reliable reference throughout the physics curriculum.

---

### 3C. Group Theory and Representation Theory

#### Why it matters

Symmetry is the central organising principle of theoretical physics. Every conservation law is a symmetry by Noether's theorem. The elementary particles of the Standard Model are classified by representations of the Poincaré group and the gauge group $SU(3) \times SU(2) \times U(1)$. The structure of QFT is largely determined by what representations of the symmetry group the fields transform under. You cannot understand the Standard Model, gauge theory, or general relativity without group theory.

#### What you need

**Finite group theory:**
- Groups, subgroups, normal subgroups, quotient groups
- Homomorphisms, isomorphisms, the isomorphism theorems
- Group actions, orbits, stabilisers
- Permutation groups, Cayley's theorem

**Representation theory:**
- Linear representations of finite groups
- Characters and character tables
- Irreducible representations and their classification
- Schur's lemma
- Tensor products of representations

**Lie groups and Lie algebras** (see Tier 4 for more depth):
- The definition of a Lie group
- The Lie algebra as the tangent space at the identity
- The exponential map
- $SU(2)$, $SO(3)$, and their relationship (the covering map)
- $SU(N)$, $U(1)$, the groups of the Standard Model

#### Resources

**Algebra** — Michael Artin
The undergraduate algebra text that treats group theory, linear algebra, and their interaction. The chapters on group representations and Lie groups are excellent and unusually accessible. This is the starting point.

**Group Theory in Physics** — Wu-Ki Tung
The standard reference for group theory as used in physics. Covers finite groups, continuous groups, Lie algebras, and the representations relevant to particle physics and quantum mechanics.

**Lie Algebras in Particle Physics** — Howard Georgi
The physicist's treatment of Lie algebras and their representations, written explicitly for particle physics applications. Clear, direct, and focused on what matters for the Standard Model.

**Groups, Representations and Physics** — H.F. Jones
More accessible than Georgi, with worked examples throughout. A good first exposure before Tung or Georgi.

**Symmetries, Lie Algebras and Representations** — Jürgen Fuchs and Christoph Schweigert
The more mathematical treatment. Complete and rigorous.

**Symmetries and Group Theory in Particle Physics** — Giovanni Costa and Gianluigi Fogli
Modern treatment with applications to the Standard Model throughout. Good for understanding how group theory connects to actual particle physics.

---

## Tier 4 — Differential Geometry, Topology, Lie Groups

This is where GR and gauge theory live. Everything before this tier is preparation; everything in this tier is the language in which the most important physics is written.

---

### 4A. Topology

#### Why it matters

Topology is the study of properties that are preserved under continuous deformation. For physics, it matters because: the configuration space of a physical system is a topological space; global properties of gauge field configurations (instantons, monopoles, the Aharonov–Bohm effect) are topological; the classification of particles by statistics involves the topology of the configuration space; and differential geometry is built on a topological foundation.

#### What you need

**Point-set topology:**
- Topological spaces, open and closed sets
- Continuity, homeomorphisms
- Compactness and connectedness
- Product and quotient topologies
- Metric spaces

**Algebraic topology:**
- The fundamental group and homotopy
- Higher homotopy groups $\pi_n$
- Homology groups
- De Rham cohomology (treated in the differential geometry section)
- Fibre bundles (classified by homotopy)

#### Resources

**Topology** — James Munkres
The standard undergraduate topology text. Part I (point-set topology) is thorough and clear. Part II (algebraic topology: the fundamental group and covering spaces) is excellent. The most reliable starting point.

**Topology Without Tears** — Sidney Morris
Free online. More accessible than Munkres for a complete beginner.

**Algebraic Topology** — Allen Hatcher
Free at [pi.math.cornell.edu/~hatcher](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html). The standard graduate reference for algebraic topology: the fundamental group, van Kampen's theorem, covering spaces, singular homology, cohomology, the cup product. Essential for understanding the topological aspects of gauge theory.

---

### 4B. Differential Geometry

#### Why it matters

Differential geometry is the mathematics of GR. The spacetime manifold is a pseudo-Riemannian manifold. The Einstein field equations are a statement about the Ricci curvature of this manifold. The geodesic equation is a statement about the Levi-Civita connection. None of these can be formulated, let alone solved, without differential geometry.

For gauge theory: gauge fields are connections on principal fibre bundles. The field strength tensor is the curvature of the connection. The structure group is the gauge group. Gauge transformations are changes of local trivialisation of the bundle. This is the full mathematical picture, and it requires differential geometry.

#### What you need

**Smooth manifolds:**
- Manifolds, charts, atlases, smooth maps
- Tangent spaces and tangent vectors
- Tangent and cotangent bundles
- Vector fields, 1-forms, tensor fields
- The Lie bracket of vector fields
- Flows and the Lie derivative

**Differential forms:**
- $p$-forms and the exterior algebra
- The exterior derivative $d$
- Closed and exact forms
- Integration of differential forms on manifolds
- Stokes' theorem in the language of forms (which unifies Green's, Gauss', and Stokes' classical theorems)
- De Rham cohomology

**Riemannian geometry:**
- Riemannian metrics and pseudo-Riemannian metrics (Lorentzian signature for GR)
- Connections and covariant derivatives
- The Levi-Civita connection
- Geodesics and the geodesic equation
- Curvature: the Riemann curvature tensor, Ricci tensor, Ricci scalar
- The Bianchi identities
- Parallel transport and holonomy

**Fibre bundles:**
- Principal $G$-bundles
- Associated vector bundles
- Connections on principal bundles
- Curvature of a connection
- Gauge transformations as bundle automorphisms
- The Yang–Mills field as the curvature of a connection

#### Resources

**Introduction to Smooth Manifolds** — John Lee
The best modern textbook on smooth manifolds. Clear, thorough, and mathematically rigorous. The treatment of differential forms, the exterior derivative, and Stokes' theorem is the best available. The transition from manifolds to Riemannian geometry is handled carefully. This is the primary reference for the manifold and differential form material.

**Riemannian Manifolds: An Introduction to Curvature** — John Lee
The sequel to the above. Covers the Levi-Civita connection, geodesics, and curvature in detail. More rigorous than any physics GR textbook.

**Differential Geometry of Curves and Surfaces** — Carmo
A gentler entry through surfaces in $\mathbb{R}^3$ before the full abstract theory. Good for building geometric intuition before Lee. The intrinsic geometry of surfaces (the first and second fundamental forms, Gaussian curvature) sets up the right mental pictures.

**Geometry, Topology and Physics** — Nakahara
The bridge between mathematics and physics. Covers homology, homotopy, manifolds, differential forms, Riemannian geometry, complex manifolds, fibre bundles, connections, characteristic classes, and index theorems — all with physical applications. Each chapter ends with applications to physics. Wald's GR makes more sense after Nakahara; so does Peskin and Schroeder on gauge theory.

It is not the most rigorous treatment — Lee is more rigorous — and it is not always the most readable. But it is the most complete bridge from mathematical physics to differential geometry and topology. Essential.

**The Geometry of Physics** — Theodore Frankel
Covers similar material to Nakahara but with more emphasis on the geometric picture and more physical motivation. Wordier than Nakahara; some find it more readable. The treatment of fibre bundles and their applications to electromagnetism and Yang–Mills theory is particularly good.

**Gauge Fields, Knots and Gravity** — John Baez and Javier Muniain
The most readable treatment of the connection between gauge theory and geometry. Covers differential forms, Hodge theory, electromagnetism as a $U(1)$ gauge theory, Yang–Mills theory, and an introduction to gravity. The exposition is excellent and the conceptual clarity is high. A good companion to Nakahara.

**Differential Forms and Connections** — R.W.R. Darling
A focused treatment of differential forms and connections, written for physicists and applied mathematicians. More concise than Lee and more rigorous than Nakahara.

---

### 4C. Lie Groups and Lie Algebras (Advanced)

The finite group theory in Tier 3 gets you to the definitions of the gauge groups. The Lie group theory in this tier gets you to their geometry — the exponential map, the adjoint representation, root systems, the classification of simple Lie algebras.

#### Resources

**Lie Groups, Lie Algebras, and Representations** — Brian Hall
The best starting point for the full theory. Clear, rigorous, and accessible to someone with linear algebra and real analysis. The treatment of the relationship between Lie groups and Lie algebras via the exponential map is excellent.

**Representation Theory: A First Course** — Fulton and Harris
The comprehensive treatment of Lie group representations, including the classification of complex semisimple Lie algebras, root systems, and Dynkin diagrams. The standard graduate reference.

**Geometry of Lie Groups** — Rosenfeld
More geometric in flavour. For the differential-geometric perspective on Lie groups.

---

## Tier 5 — Advanced: Functional Analysis, Characteristic Classes, Index Theory

This tier is necessary for rigorous QFT, for advanced gauge theory, and for understanding the relationship between physics and modern mathematics (the Atiyah–Singer index theorem, anomalies in gauge theories, topological field theory).

---

### 5A. Functional Analysis

#### Why it matters

The rigorous foundation of quantum mechanics is functional analysis: the Hilbert space of states, the operators representing observables (which are unbounded and require careful treatment), the spectral theorem for self-adjoint operators, and the theory of distributions. In QFT, functional analysis underlies the path integral (as an integral over a function space), the renormalisation group (as a flow on a space of theories), and axiomatic QFT.

#### What you need

- Banach spaces and Hilbert spaces
- Bounded and unbounded operators
- The spectral theorem for self-adjoint operators
- Compact operators
- The Riesz representation theorem
- Sobolev spaces (function spaces that carry derivative information)
- Tempered distributions and their Fourier transforms

#### Resources

**Functional Analysis** — Walter Rudin (Real and Complex Analysis or Functional Analysis)
The standard rigorous treatment. Demanding. Covers the spectral theorem and the theory of distributions.

**Quantum Theory for Mathematicians** — Brian Hall
The treatment of quantum mechanics from the perspective of functional analysis. Hall proves the spectral theorem carefully and connects it to the physics throughout. Essential if you want a rigorous foundation for quantum mechanics.

**Methods of Modern Mathematical Physics** — Reed and Simon (four volumes)
The encyclopaedic reference for functional analysis as applied to quantum mechanics and QFT. Volumes I (Functional Analysis) and II (Fourier Analysis, Self-Adjointness) are the core. Essential for anyone working on rigorous QFT.

---

### 5B. Characteristic Classes

#### Why it matters

Characteristic classes are topological invariants of fibre bundles. They classify bundles and encode information about the global topology of gauge field configurations. The Chern classes are the characteristic classes of complex vector bundles; the Pontryagin classes of real bundles. The first Chern class of a $U(1)$ bundle encodes the magnetic monopole charge. The second Chern class of a $SU(2)$ bundle is the instanton number. Anomalies in gauge theories are detected by characteristic classes (the descent formalism and the Atiyah–Singer index theorem).

#### Resources

**Characteristic Classes** — Milnor and Stasheff
The mathematical reference. Rigorous and complete.

**Geometry, Topology and Physics** — Nakahara
Covers characteristic classes with physical applications in Chapters 11–12. A more accessible starting point than Milnor–Stasheff.

**Anomalies in Quantum Field Theory** — Bertlmann
A complete treatment of anomalies in gauge theories from the perspective of differential geometry and characteristic classes.

---

### 5C. Index Theory

#### Why it matters

The Atiyah–Singer index theorem relates the analytical index of an elliptic differential operator to topological invariants of the underlying manifold. This connects functional analysis, differential geometry, and topology in one of the deepest results of 20th-century mathematics. In physics, it underlies: the chiral anomaly (the index of the Dirac operator gives the number of zero modes); the Witten index in supersymmetric quantum mechanics; and the mathematical theory of topological field theories.

#### Resources

**The Index of Elliptic Operators I–V** — Atiyah and Singer
The original papers. Available in Atiyah's collected works.

**The Atiyah–Singer Index Theorem** — Patrick Shanahan
An accessible introduction to the theorem and its proof, aimed at mathematicians.

**Heat Kernels and Dirac Operators** — Berline, Getzler, Vergne
The modern approach to the index theorem via the heat kernel and supersymmetric quantum mechanics.

---

## Special Topic: Spinors and Clifford Algebras

Spinors appear throughout theoretical physics — in the Dirac equation, in supersymmetry, in string theory. They are not vector fields or tensor fields; they are sections of the spinor bundle, which requires the frame bundle and the spin structure of the manifold.

#### Resources

**Spinors and Spacetime** — Penrose and Rindler (two volumes)
The complete mathematical treatment of spinors in the context of general relativity and conformal geometry. Dense but definitive.

**Geometry, Spinors and Applications** — Donal Husemoller
A more accessible treatment of the relationship between Clifford algebras, spinors, and geometry.

**Quantum Theory, Groups and Representations** — Peter Woit
Covers the representation theory relevant to quantum mechanics and QFT, including the Dirac equation and spinors, from a rigorous mathematical perspective. Free online at [math.columbia.edu/~woit/QM/quantum.pdf](https://www.math.columbia.edu/~woit/QM/quantum.pdf).

---

## The Physicist's Mathematics References

### Books that cover multiple topics

**Mathematical Methods for Physicists** — Arfken, Weber, Harris
The standard omnibus reference. Covers linear algebra, complex analysis, special functions, PDEs, group theory, and more in a single volume. Less rigorous than any dedicated text on each subject, but comprehensive and reliable. Every working physicist has a copy.

**Mathematics for Physics** — Stone and Goldbart
A more mathematically careful version of Arfken. Covers differential geometry and topology as well as the standard analytical tools. Free online. A better book than Arfken for someone who wants to understand rather than just use.

**Mathematical Physics** — Robert Geroch
A rigorous treatment of the mathematical structures that appear in theoretical physics — topology, groups, Hilbert spaces, distributions — from a mathematical physicist's perspective. Written with extraordinary clarity.

**A Course in Modern Mathematical Physics** — Peter Szekeres
Groups, Hilbert spaces, differential geometry, Lie groups, and fibre bundles — all in one volume, at graduate level. A very good book that does not get enough attention.

**Mathematical Methods of Classical Mechanics** — V.I. Arnold
The geometric approach to classical mechanics: symplectic geometry, Hamiltonian flows, Arnold–Liouville integrability. Essential for understanding the mathematical structure of classical mechanics and its quantisation.

---

## The Honest Summary

For QFT at Peskin–Schroeder level, you need through Tier 3: calculus, linear algebra, ODEs, PDEs, complex analysis, Fourier analysis, and basic group theory.

For gauge theory at Tong's level, you need Tier 4: differential geometry, fibre bundles, connections, Lie groups.

For GR at Wald's level, you need Tiers 3 and 4 done properly: all the analysis, and all the differential geometry.

For BRST quantisation and the mass gap problem (my own area), you need Tiers 3, 4, and parts of 5: Lie algebras, differential geometry, fibre bundles, and some functional analysis.

For the rigorous mathematical foundations of QFT — constructive QFT, axiomatic approaches, the mathematical theory of the path integral — you need everything through Tier 5, and then some.

The good news is that you do not need to complete each tier before starting the physics. In practice you learn mathematics and physics in parallel, returning to the mathematics when the physics demands it. The sequencing matters — you cannot understand the geodesic equation without connections, and you cannot understand connections without fibre bundles, and you cannot understand fibre bundles without manifolds — but the overall enterprise is a spiral, not a ladder.

One thing I have found consistently: the mathematics makes the physics more beautiful, not more complicated. Once you understand that a gauge field is a connection on a principal bundle, and that the field strength is the curvature of that connection, the entire structure of gauge theory becomes transparent. The mathematical language is not obscuring the physics — it is revealing what the physics actually is.

---

*Last updated March 2026.*