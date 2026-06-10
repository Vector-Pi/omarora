---
title: "Beginners Guide to Advanced Mathematics"
date: 2026-02-26
parent: "Mathematics"
description: "A practical roadmap for entering advanced mathematics. How to transition from high school math to rigorous proof-based thinking and research-level work."
---


There is a version of this guide that begins with an apology — *"I am not a professional mathematician"*, or *"this is just my personal opinion."* That version is not useful. So I will skip it. 

What follows is a map. It is the map I wish someone had handed me when I started. It will not replace any of the books it points to. It will not make you a mathematician. What it will do is tell you what the landscape looks like before you set foot in it, which is worth something.

One honest note before we begin: you will need pencil and paper. Not metaphorically. Literally. Mathematics is not a reading activity.

---

## Before You Begin: What "Mathematical Maturity" Actually Means

Every advanced mathematics text warns you that it assumes "mathematical maturity." No one explains what this means.

It means two things. First: you are comfortable with proof — you can follow a logical argument from hypothesis to conclusion, and you can identify when a step has been skipped. Second: you have a working vocabulary of sets and functions — you know what a bijection is, what a subset is, what it means for a function to be injective.

If you are not there yet, this is where to start:

**Resources for proof-writing fundamentals:**

- **Book of Proof** — Richard Hammack. Free at [richardhammack.github.io](https://richardhammack.github.io/BookOfProof/). The most gentle introduction to proof-writing that exists. Read Part I and Part II before touching anything else on this page. It is not glamorous. Do it anyway.

- **How to Prove It** — Daniel Velleman. More thorough than Hammack, slightly more demanding. If you are comfortable with high-school mathematics and want something with a bit more substance, start here instead. The chapter on mathematical induction is particularly good.

- **How to Solve It** — George Pólya. Not strictly a proof-writing book — more a philosophy of mathematical problem-solving. Read it once at the start, and again after you have done some real mathematics. It will mean different things each time.

One important thing: *[Brilliant.org](https://brilliant.org)*  gets recommended constantly for this stage, and it is fine for building intuition about individual topics, but do not mistake it for learning mathematics. It is interactive edutainment. The moment the difficulty feels comfortable, leave it behind and open a real book.

---

## Part I — The Starting Points

These are the first areas you should encounter. They are not prerequisites for each other, but they share a common vocabulary, and knowing all three gives you something no individual course does: the ability to see the same structure appear in different guises.

### 1. Groups and Abstract Algebra

**What it is.** Abstract algebra is the study of structure. A group is the simplest structure: a set with an operation that satisfies four axioms (closure, associativity, identity, inverses). That is all. From those four axioms, an enormous theory emerges.

**Why you should care.** Every symmetry in mathematics and physics is, at root, a group. The symmetry of a square, the rotations of a sphere, the gauge symmetry of Yang–Mills theory — all of these are groups. Once you understand groups, you start seeing them everywhere.

**What the subject contains at this stage:**
Groups, subgroups, homomorphisms, cosets, Lagrange's theorem, quotient groups, the first isomorphism theorem. Then rings (groups with two operations), ideals, fields (rings where division is possible), and polynomial rings. Then modules, which generalise vector spaces.

**Resources:**

- **Evan Chen, *An Infinitely Large Napkin***, Chapters 1–5. Free at [venhance.github.io/napkin](https://venhance.github.io/napkin/Napkin.pdf). Start here. Chen's approach is unusual: he explains why a definition should exist before writing it down. The chapters on groups and rings are among the best elementary treatments I have encountered. Do not skip the examples.

- **Algebra** — Michael Artin. The standard undergraduate text for a reason. The examples are excellent. Artin talks to you rather than at you. If the Napkin gives you the overview, Artin gives you the substance.

- **Abstract Algebra** — Dummit and Foote. The encyclopaedia of undergraduate algebra. Thorough to a fault. Useful as a reference once you know what you are looking for; overwhelming as a starting point. People who tell you to begin here are forgetting what it felt like to be a beginner. Start with Artin. Come back to Dummit–Foote when you need it.

- **3Blue1Brown's *Essence of Group Theory*** on YouTube. Not a substitute for any of the above, but the visual intuition for quotient groups and homomorphisms is genuinely useful. Watch it after you have worked through the definitions, not before.

---

### 2. Metric Spaces and Topology

**What it is.** A metric space is a set with a notion of distance. From distance, you get convergence, continuity, open sets, and closed sets. Topology abstracts further: it asks which properties of a space depend only on its "shape" and not on any specific distance function.

**Why you should care.** Analysis without topology is manipulation of symbols without understanding what they mean. Most of the machinery of real analysis — limits, continuity, compactness — is really topology in disguise. If you intend to study any analysis, probability, or geometry seriously, this is the ground it all stands on.

**What the subject contains at this stage:**
Metric spaces, convergence, continuous maps, homeomorphisms, open and closed sets. Then topological spaces (the fully abstract version), compactness, connectedness, the product topology. Later: homotopy, fundamental groups, covering spaces.

**Resources:**

- **Napkin**, Chapter 2 (metric spaces) and Chapters 6–8 (topology). Chen's metric space chapter is excellent as a first contact. Read it before any of the following.

- **Topology Without Tears** — Sidney Morris. Free online. The most genuinely beginner-friendly introduction to point-set topology that exists. If you find the Napkin's topology chapters moving too fast, read this first.

- **Topology** — James Munkres. The canonical reference for point-set topology. Part I is rigorous and complete. Part II (algebraic topology) is where it becomes genuinely exciting — the fundamental group, covering spaces, the beginning of a connection between topology and algebra. Munkres is clearly written and the exercises are well-calibrated.

- **Topology** — Kelley. An older text, more abstract from the outset. Worth knowing about, but not the right place to begin.

A note on *Khan Academy* topology resources: they barely exist. This is one of the few areas where YouTube does not help much at the introductory level. Read a book.

---

### 3. Linear Algebra

**What it is.** The study of vector spaces and linear maps between them. Despite the elementary appearance of the subject at the level of matrices, linear algebra at the right level of abstraction is one of the most powerful tools in all of mathematics.

**Why you should care.** Linear algebra is the language of quantum mechanics, statistics, numerical analysis, machine learning, and much of geometry. Understanding it at the level of abstract vector spaces — not just row operations — is what separates people who can use it from people who are used by it, I myself got this wrong the first time around, and now working in quantative research I can say that this is one of the most important subjects to understand well.

**What the subject contains at this stage:**
Vector spaces over fields, linear maps, bases and dimension, matrices as representations of linear maps, eigenvalues and eigenvectors, inner product spaces, the spectral theorem. Then determinants (done properly, as a multilinear alternating form), dual spaces, tensor products.

**Resources:**

- **Napkin**, Chapters 9–15 (linear algebra) and Chapter 16 onwards (further developments). The treatment is more abstract than most introductions and better for it.

- **Linear Algebra Done Right** — Sheldon Axler. Do not learn linear algebra from a standard computational course and think you have understood it. Axler's book banishes determinants until the final chapter and builds the entire theory from linear maps. This is the correct approach. The title is not modest — it is accurate.

- **Linear Algebra** — Friedberg, Insel, Spence. More comprehensive than Axler, with determinants treated throughout. Useful for a second pass through the material.

- **Gilbert Strang's MIT OpenCourseWare Linear Algebra lectures.** Free on YouTube and MIT OCW. Strang is an exceptional lecturer and the course is outstanding for computational intuition. But be warned: Strang's approach is applied and matrix-centric. After watching his lectures, read Axler to understand what is actually happening.

The most common mistake at this stage is learning linear algebra as matrix manipulation. Reduced row echelon form is a tool. It is not the theory. If after your first linear algebra course you cannot state what a linear map is without mentioning a matrix, you have learned a dialect, not the language.

---

## Part II — Going Deeper

Once the foundations above are solid, the subject branches. What follows is not a complete map of mathematics — that does not exist in finite space — but a tour of the areas that are most important for physics, research mathematics, and quantitative work.

### 4. Real Analysis

**What it is.** The rigorous treatment of everything we are told to accept as calculus in high school. Limits, continuity, differentiation, integration — all made precise. Then: sequences and series of functions, uniform convergence, and the beginnings of functional analysis.

**Why you should care.** Calculus is a tool. Analysis is the understanding of why the tool works. If you want to do anything serious with differential equations, probability, or mathematical physics, you need this.

**What the subject contains:**
ε–δ definitions of limits and continuity, the real number system and its completeness, sequences and series, differentiation and the mean value theorem, Riemann integration, sequences of functions, uniform convergence, the Weierstrass approximation theorem.

**Resources:**

- **Napkin**, Chapters 26–30 (real analysis and calculus foundations).

- **Principles of Mathematical Analysis** — Walter Rudin. Known universally as "Baby Rudin." Terse, elegant, unforgiving. Every proof is tight and every definition is exactly right. Do not begin here if you are starting from scratch — Rudin respects you by not holding your hand, which is admirable, but it means you will spend hours on single paragraphs. This is not a flaw of the book; it is a feature. Work through it slowly. The exercises are essential.

- **Understanding Analysis** — Stephen Abbott. The humane version. Abbott explains the motivation behind every definition and gives you time to digest. Read Abbott first. Then read Rudin for the complete treatment.

- **Real Mathematical Analysis** — Charles Pugh. Somewhere between Abbott and Rudin in style. Excellent for a second reading. The visual intuition is better than either of the above.

A criticism worth making: many university analysis courses (especially the ones I have seen on youtube) spend enormous time on ε–δ proofs of results everyone already believes and then rush through uniform convergence and Fourier analysis, which are actually important. If your course does this, supplement it aggressively.

---

### 5. Complex Analysis

**What it is.** Analysis on the complex plane. Functions of a complex variable behave radically differently from real functions — they are either "nice" everywhere or terrible. This niceness (holomorphicity) has extraordinary consequences.

**Why you should care.** Complex analysis is unreasonably effective. Contour integration solves real integrals that resist every other method. The residue theorem is one of the most useful computational tools in mathematical physics. And the theory itself — conformal maps, Riemann surfaces, the connection to topology — is beautiful in a way that is difficult to describe.

**What the subject contains:**
Holomorphic functions, the Cauchy–Riemann equations, contour integration, Cauchy's integral theorem and formula, power series and Laurent series, poles and residues, the residue theorem, conformal maps.

**Resources:**

- **Napkin**, Chapters 31–34.

- **Complex Analysis** — Elias Stein and Rami Shakarchi. Part of the Princeton Lectures in Analysis. The exposition is superb — rigorous without being arid, and full of connections to other areas. This is the best starting point for complex analysis at a serious level.

- **Visual Complex Analysis** — Tristan Needham. Every other complex analysis book tells you what is true. Needham shows you why. The geometric approach to holomorphic functions, Möbius transformations, and the argument principle is unlike anything else in the literature. Read this alongside a more conventional text. The visual intuition it builds is worth months of calculation.

- **Complex Analysis** — Lars Ahlfors. The classic graduate reference. More demanding than Stein–Shakarchi. Worth reading once you have the foundations — the treatment of Riemann surfaces is particularly good.

---

### 6. Measure Theory and Probability

**What it is.** A rigorous foundation for integration and probability. The Lebesgue integral replaces the Riemann integral with something that behaves better under limits. Measure theory is the language of modern probability.

**Why you should care.** If you want to understand probability at any depth beyond coin flips — stochastic processes, martingales, Brownian motion — you need measure theory. If you want to understand functional analysis, you need measure theory. It is the substrate on which most of modern analysis is built; and after working in quantative research I can easily say that it's importance is beyond what can be expressed in words.

**What the subject contains:**
σ-algebras, measures, the Lebesgue integral, convergence theorems (monotone, dominated), Lp spaces, product measures and Fubini's theorem. Then probability: probability spaces, random variables, expectation, conditional expectation, the law of large numbers, the central limit theorem, martingales.

**Resources:**

- **Napkin**, Chapters 35–39.

- **Real Analysis: Modern Techniques and Their Applications** — Gerald Folland. The standard graduate text. Comprehensive and well-written. Not gentle, but correct in every detail.

- **Probability and Measure** — Patrick Billingsley. The canonical text for measure-theoretic probability. The first half is measure theory; the second half is probability. Dense but rewarding.

- **Probability: Theory and Examples** — Rick Durrett. Available free online. More modern than Billingsley, with better coverage of stochastic processes. The exercises are excellent.

One thing to note is that the resources I mentioned here are considering that you are studying the subject for exploration but if you are studying for quantative finance, it requires a different approach, and alot of focus on the applied side of the subject. 

---

### 7. Differential Geometry

**What it is.** The study of smooth manifolds — spaces that locally look like Euclidean space but can have complicated global geometry. Differential geometry is where calculus meets topology.

**Why you should care.** General relativity is differential geometry. Gauge theory in physics — the framework for electromagnetism, the weak force, the strong force — is differential geometry. If you want to understand the geometry of spacetime or the mathematical structure of field theory, this is unavoidable.

**What the subject contains:**
Smooth manifolds, tangent spaces and tangent bundles, differential forms, the exterior derivative, integration on manifolds, Stokes' theorem. Then Riemannian geometry: metrics, curvature, geodesics. Then connections and fibre bundles (the language of gauge theory).

**Resources:**

- **Napkin**, Chapters 43–52.

- **Introduction to Smooth Manifolds** — John Lee. The best modern textbook on the subject. Clear, thorough, and carefully paced. The treatment of tangent vectors and differential forms is the best I have found.

- **Differential Geometry of Curves and Surfaces** — Carmo. A gentler entry point through the geometry of surfaces in three-dimensional space before the fully abstract theory. Good for building intuition before Lee.

- **Geometry, Topology and Physics** — Nakahara. Written for physicists. The mathematical rigour is lower than Lee's, but the connections to physics — fibre bundles, gauge fields, characteristic classes — are explicit and useful. Essential reading if you intend to use differential geometry for field theory.

---

### 8. Algebraic Topology

**What it is.** The study of topological spaces using algebraic invariants. Given a topological space, algebraic topology assigns to it algebraic objects — groups, rings — that encode information about its shape and do not change under continuous deformation.

**Why you should care.** The fundamental group tells you about loops in a space. Homology tells you about holes. Cohomology rings encode the cup product structure of those holes. These tools appear in theoretical physics (topological field theories, anomalies, instantons) and pure mathematics alike.

**What the subject contains:**
The fundamental group, van Kampen's theorem, covering spaces, singular homology, the long exact sequence, the Mayer–Vietoris sequence, cohomology, the cup product, Poincaré duality.

**Resources:**

- **Napkin**, Chapters 64–76.

- **Algebraic Topology** — Allen Hatcher. Free at [pi.math.cornell.edu/~hatcher](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html). The standard text. The exposition is conversational and the examples are excellent. Some proofs are more intuitive than rigorous — supplement with Munkres Part II for complete precision.

- **A Concise Course in Algebraic Topology** — Peter May. Also free online. More abstract and concise than Hatcher, written from a categorical perspective. Not for beginners, but very efficient once you know the basics.

- **Topology and Geometry** — Glen Bredon. A single volume covering both differential topology and algebraic topology. Useful for seeing how the two areas connect.

---

### 9. Algebraic Number Theory

**What it is.** The study of number fields — extensions of the rational numbers — and the algebraic structures that arise in them. It is where algebra and classical number theory meet.

**Why you should care.** Many of the deepest results in number theory — the proof of Fermat's Last Theorem, the Birch and Swinnerton-Dyer conjecture, the Langlands programme — are fundamentally algebraic. Understanding even the first steps of algebraic number theory reveals how rich the structure of the integers actually is.

**What the subject contains:**
Number fields, rings of integers, unique factorisation in Dedekind domains, ideal class groups, the geometry of numbers (Minkowski's theorem), Dirichlet's unit theorem, ramification and splitting of primes, local fields, and the beginnings of class field theory.

**Resources:**

- **Napkin**, Chapters 53–63.

- **Algebraic Number Theory** — Jürgen Neukirch. The complete reference. Abstract and demanding, but beautifully written. The perspective is geometric throughout — Neukirch treats number fields as analogues of algebraic curves, which is exactly right.

- **A Classical Introduction to Modern Number Theory** — Ireland and Rosen. A more elementary entry point, connecting elementary number theory to its algebraic underpinnings. The chapter on Gauss sums is particularly good.

- **Number Fields** — Daniel Marcus. A concrete introduction with excellent exercises. Good for a first encounter before Neukirch.

---

### 10. Category Theory

**What it is.** The mathematics of mathematical structure itself. Category theory identifies the common patterns that appear across algebra, topology, geometry, and logic, and provides a language for stating results that apply to all of them simultaneously.

**Why you should care.** Once you have seen enough mathematics, you start noticing that the same constructions appear over and over in different guises — quotient objects, products, functors from one category to another. Category theory is the language that makes these observations precise. It is indispensable for algebraic geometry, algebraic topology, and homological algebra.

**What the subject contains:**
Categories, functors, natural transformations, universal properties, limits and colimits, adjoint functors, the Yoneda lemma.

**Resources:**

- **Napkin**, Chapters 67–70.

- **Category Theory** — Steve Awodey. The most accessible introduction. Written for a philosophical/logical audience but clear for mathematicians. Good for a first reading.

- **Categories for the Working Mathematician** — Saunders Mac Lane. The original serious treatment. Dense and abstract. The Yoneda lemma chapter is essential. Do not begin here — it is a reference for people who already know what a category is and want the complete theory.

- **The Napkin itself** is actually one of the better introductions to category theory for someone coming from algebra and topology. Chen's example-driven approach works well for this subject.

---

## Part III — Orientation

### On the Order of Things

No guide can prescribe a single correct path, because the right order depends on what you want. But here is a suggestion for someone who wants a broad foundation:

1. Proof-writing (Hammack or Velleman) — until you are comfortable.
2. Groups and linear algebra simultaneously — they reinforce each other.
3. Metric spaces and topology.
4. Real analysis — properly, not skimmed.
5. Choose a direction: complex analysis, differential geometry, algebraic topology, or number theory. They are all accessible from this point.
6. Category theory — when it starts appearing naturally in what you are reading.

### On Primary Sources

Read the original papers when you can. Gauss's *Disquisitiones Arithmeticae*, Riemann's habilitation lecture on the foundations of geometry, Poincaré's papers on topology — these are not only historically important but often the clearest expositions of the ideas, because the author understood exactly why the definition was needed.

### On the Napkin

Evan Chen's *Infinitely Large Napkin* is unusual. It is not a reference. It is not a course. It is a very good friend who happens to know an extraordinary amount of mathematics explaining things to you over forty hours, without worrying about whether every detail is correct. It sacrifices completeness for understanding, and that trade is the right one for a first encounter with most topics.

Use it as a map. Then go read the actual terrain.

### A Few Resources to Approach Carefully

**Paul's Online Math Notes.** Widely used, clearly written, and a perfectly reasonable supplement for single-variable calculus. The problem is that many people stop there and believe they have done analysis( atleast what I did initially). They have not. Paul's Notes cover computations. Analysis covers why computations are valid. These are different activities.

**Wikipedia mathematics articles.** Useful for definitions and checking facts once you know a subject. Dangerous as a learning tool because the articles assume familiarity with the precise vocabulary, skip motivations, and sometimes have subtly misleading presentations of subtle points. Use it to remind yourself of something you have already understood, not to learn something for the first time.

**Any textbook that never requires you to struggle.** If a mathematics book is going quickly and everything is making sense on the first read, either the book is not teaching you anything you do not already know, or it is lying to you by omission. Real mathematical understanding involves sitting with confusion. A book that never produces confusion is not taking you anywhere new.

---

## A Final Note

Mathematics is not a collection of techniques. It is a way of seeing — the patient extraction of structure from confusion. The resources above will teach you the content. The habit of sitting with a problem until it opens will teach you the rest, and no book can do that for you.

The Napkin quote is worth keeping in mind: *"When introduced to a new idea, always ask why you should care. Do not expect an answer right away, but demand one eventually."*

That is not advice for reading mathematics. That is advice for doing it.

---

*Last updated March 2026. Suggestions and corrections welcome.*