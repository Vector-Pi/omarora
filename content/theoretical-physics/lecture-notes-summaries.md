---
title: "Lecture Notes & Summaries"
date: 2026-02-06
parent: "Theoretical Physics"
---

This page is a log of the lecture notes I have worked through, organised by subject. Every set of notes here is something I have actually read, not a list of things I intend to read. I have included personal notes on what each course does well, where it requires supplementing, and how it connects to my own research.

The emphasis is on freely available material. With very few exceptions, everything below is free online. The theoretical physics community has been extraordinarily generous in this regard: the Cambridge Mathematical Tripos notes, the Harvard recordings, the Perimeter Institute lectures — collectively they constitute a complete graduate curriculum available to anyone with an internet connection.

---

## How to Read Lecture Notes

Lecture notes are not textbooks. A textbook is written to be complete; a set of lecture notes is written to be taught from. The difference matters when you are self-studying. Lecture notes often omit calculations that would be worked on problem sets. They sometimes skip steps that a lecturer would fill in verbally. They are usually fast.

The right approach is: read a section, close the notes, and try to reconstruct the argument from memory. Then open the notes and compare. The gaps between your reconstruction and the actual argument are precisely the things you have not understood. Do this for every major theorem, every derivation, every calculation you care about. It is slow. There is no faster way.

For every course below I have listed the associated problem sets where they exist. The notes without the problem sets are half the course.

---

## The David Tong Cambridge Curriculum

David Tong has written lecture notes covering the complete theoretical physics curriculum taught in Part I, Part II, and Part III of the Cambridge Mathematical Tripos, and several graduate courses beyond that. The full collection is at [damtp.cam.ac.uk/user/tong/teaching.html](http://www.damtp.cam.ac.uk/user/tong/teaching.html). I have worked through most of these at various depths, and they are collectively the most coherent free curriculum in theoretical physics that exists.

What distinguishes Tong's notes from most alternatives is that they are written by someone who cares about both physical intuition and mathematical precision. He does not sacrifice one for the other. He also writes well — an underrated quality in a genre where prose is often an afterthought.

---

### Classical Dynamics

[damtp.cam.ac.uk/user/tong/dynamics.html](http://www.damtp.cam.ac.uk/user/tong/dynamics.html)

A compact course on Newtonian mechanics, the Lagrangian formalism, the Hamiltonian formalism, and an introduction to chaos. Part IA level — first-year undergraduate. The derivation of the Euler–Lagrange equations from the action principle is the clearest I have seen at this level. The section on Noether's theorem is brief but correct. The treatment of the Hamilton–Jacobi equation sets up the connection to quantum mechanics.

**What I used it for.** First encounter with the action principle as the unifying structure of mechanics. Returning to this after studying QFT makes the structural parallels obvious in a way they were not the first time through.

**Problem sets.** Available on the course page. Do them. The problems on constrained systems are excellent.

---

### Dynamics and Relativity

[damtp.cam.ac.uk/user/tong/relativity.html](http://www.damtp.cam.ac.uk/user/tong/relativity.html)

Special relativity alongside Newtonian mechanics, at Part IA level. Covers Lorentz transformations, four-vectors, relativistic kinematics and dynamics, and an introduction to the stress-energy tensor. The section on the geometry of spacetime — the invariant interval, the light cone, the spacetime diagrams — is beautifully done. Published as a textbook in 2023 (*Dynamics and Relativity*, Cambridge University Press), but the notes are still freely available.

**What I used it for.** Foundation for understanding the four-vector notation that appears throughout QFT. The section on the stress-energy tensor prepared me for how it appears in the Einstein equations.

---

### Electromagnetism

[damtp.cam.ac.uk/user/tong/em.html](http://www.damtp.cam.ac.uk/user/tong/em.html)

The most conceptually thorough undergraduate electromagnetism notes I have used. The key difference from Griffiths: Tong treats gauge invariance as the central structural fact of the theory from the start, rather than introducing it as a technical convenience. The section on the electromagnetic field tensor $F_{\mu\nu}$ and Maxwell's equations as a single equation $\partial_\mu F^{\mu\nu} = J^\nu$ is done early and clearly. The treatment of radiation is good.

**What I used it for.** Understanding gauge symmetry at a level that transfers directly to QFT. Returning to the gauge transformation $A_\mu \to A_\mu + \partial_\mu \alpha$ after studying BRST quantisation makes the structure much clearer — and reading these notes first made the BRST structure much more natural when I encountered it.

**A note on Griffiths.** Griffiths is a better first book for building physical intuition. Tong is a better second read for understanding the structure. Use both.

---

### Quantum Mechanics

[damtp.cam.ac.uk/user/tong/quantum.html](http://www.damtp.cam.ac.uk/user/tong/quantum.html)

The undergraduate QM course, now a published textbook (*Quantum Mechanics*, Cambridge University Press, 2023). The notes cover the Schrödinger equation, wavefunctions, the harmonic oscillator, the hydrogen atom, spin, and perturbation theory. The exposition is clear and honest about the conceptual difficulties — the measurement problem and the interpretational issues are not swept under the rug.

**What I found most useful.** The chapter on spin and the connection to the group theory of $SU(2)$ and $SO(3)$. This is the entry point to representation theory in quantum mechanics.


---

### Statistical Physics

[damtp.cam.ac.uk/user/tong/statphys.html](http://www.damtp.cam.ac.uk/user/tong/statphys.html)

Undergraduate statistical mechanics and thermodynamics. The treatment is more careful about the foundations than most physics courses — entropy is derived from the microcanonical ensemble rather than postulated, which is the right approach. The chapters on quantum gases (Bose–Einstein and Fermi–Dirac statistics) are excellent. The final chapter on phase transitions prepares the conceptual ground for the renormalisation group.

---

### Kinetic Theory

[damtp.cam.ac.uk/user/tong/kinetic.html](http://www.damtp.cam.ac.uk/user/tong/kinetic.html)

The Boltzmann equation, the H-theorem, transport coefficients. Relevant to the recent Hilbert sixth problem work (Deng–Hani–Ma, 2025) on deriving fluid equations from the Boltzmann equation. I read these notes alongside the Deng–Hani–Ma introduction to understand what the mathematical problem actually was.

---

### General Relativity

[damtp.cam.ac.uk/user/tong/gr.html](http://www.damtp.cam.ac.uk/user/tong/gr.html)

A graduate-level GR course, aimed at Part III students. Covers differential geometry (briefly), the Einstein equations, geodesics, the Schwarzschild solution and black holes, gravitational waves, and cosmology. The treatment of the equivalence principle and the geometric derivation of the geodesic equation are excellent. The section on the Penrose process (energy extraction from a Kerr black hole) is one of the better treatments at this level.

**What I used it for.** Foundation for understanding the geometry of spacetime that underlies the QGET framework. The derivation of the Riemann tensor from the Levi-Civita connection, and the connection between curvature and tidal forces, is the section I have returned to most.

**Limitation.** The differential geometry is developed quickly. Read John Lee's *Introduction to Smooth Manifolds* alongside for mathematical rigour.

---

### Quantum Field Theory

[damtp.cam.ac.uk/user/tong/qft.html](http://www.damtp.cam.ac.uk/user/tong/qft.html)

The Part III QFT course. This is the most important set of notes on this page for my own research. The course covers canonical quantisation of scalar, Dirac, and vector fields; Feynman diagrams and the LSZ reduction formula; one-loop renormalisation; the renormalisation group; and an introduction to non-Abelian gauge theories. The companion video lectures, recorded at the Perimeter Institute, are available on the course page.

Tong's QFT notes follow roughly the first six chapters of Peskin and Schroeder but with significantly more explanation at each step — roughly half the density with twice the motivation. For a first encounter with QFT, these notes are the right starting point.

**What I used most.** Chapter 6 (Quantum Electrodynamics) for the Feynman rules and the Ward identities; Chapter 4 (Interacting Fields) for Wick's theorem and the systematic development of perturbation theory; and particularly the discussion of regularisation and renormalisation, which I read alongside Chapter 10 of Peskin–Schroeder.

**The video lectures.** The video lectures at the Perimeter Institute are worth watching alongside the notes. Tong lectures well and the PIRSA recording quality is good. The lectures on canonical quantisation and the lectures on renormalisation are the most valuable.

---

### Gauge Theory

[damtp.cam.ac.uk/user/tong/gaugetheory.html](http://www.damtp.cam.ac.uk/user/tong/gaugetheory.html)

Approximately 400 pages. This is the most directly relevant set of notes to my own research. The course covers: magnetic monopoles and the Dirac quantisation condition; the Yang–Mills action and its classical solutions; the theta term and instantons; the one-loop beta function and asymptotic freedom; confinement and the Wilson criterion; 't Hooft lines; large-$N$ Yang–Mills; chiral symmetry breaking and the chiral Lagrangian; anomalies (chiral anomaly, gauge anomalies, the Atiyah–Singer index theorem); lattice gauge theory; QFT in 2+1 dimensions (Chern–Simons theory); and an introduction to Seiberg–Witten theory.

This is the deepest freely available treatment of non-Abelian gauge theory that I know of. The section on instantons (Chapter 2) is where I first understood the connection between the instanton number, the second Chern class, and the topological $\theta$ term — a connection that is central to the non-perturbative structure of Yang–Mills theory. The anomalies chapter (Chapter 3) is the best pedagogical treatment of the Atiyah–Singer index theorem and its physical consequences that I have found outside Nakahara's book.

**What I have spent most time on.** The sections on confinement, the beta function, and instantons are the parts most directly connected to my research. The treatment of the Gribov problem is brief (Tong acknowledges it in a footnote and refers to the Gribov–Zwanziger literature), which is a gap I have filled from other sources.

**What I have not yet worked through.** The Seiberg–Witten chapter requires significant background in supersymmetry. I have read it once but not worked through the details.

---

### Statistical Field Theory

[damtp.cam.ac.uk/user/tong/sft.html](http://www.damtp.cam.ac.uk/user/tong/sft.html)

The connection between statistical mechanics and QFT via the path integral and the renormalisation group. The course covers the Ising model and mean field theory; the renormalisation group as a flow on the space of theories; universality and critical exponents; the $\phi^4$ theory in $d = 4 - \epsilon$ dimensions. The treatment of the Wilsonian RG — in which the RG transformation is a literal integration over short-distance degrees of freedom — is the clearest I have found.

**Why this matters for QFT.** The Wilsonian perspective on renormalisation changed how I think about the structure of QFT. Renormalisation is not a way of removing infinities — it is a statement that physical theories are descriptions of physics at a given scale, with the short-distance structure integrated out. This is the perspective from which the mass gap problem should be approached.

---

### String Theory

[damtp.cam.ac.uk/user/tong/string.html](http://www.damtp.cam.ac.uk/user/tong/string.html)

Also on arXiv as [0908.0333](https://arxiv.org/abs/0908.0333). A one-semester course on bosonic string theory. Covers the classical and quantum bosonic string; the open string and D-branes; conformal field theory; the Polyakov path integral and ghosts; string interactions; the low-energy effective action; and compactification and T-duality.

**My status with these notes.** I have read Chapters 1–4 carefully. The treatment of conformal field theory in Chapter 4 is excellent — the stress-energy tensor in CFT, the Virasoro algebra, and the OPE are all developed carefully. The ghost system (Chapter 5) is directly relevant to my BRST work, since the bc ghost system of string theory is the same structure as the Faddeev–Popov ghosts of gauge theory, generalised to the worldsheet.

---

### Cosmology

[damtp.cam.ac.uk/user/tong/cosmo.html](http://www.damtp.cam.ac.uk/user/tong/cosmo.html)

Introductory cosmology: the FRW metric and the expanding universe, thermal history of the universe, big bang nucleosynthesis, recombination, inflation. The treatment of inflation is the section I have spent most time on — particularly the generation of primordial perturbations during inflation, which is relevant to the QGET prediction about CMB signatures.

---

### Solid State Physics

[damtp.cam.ac.uk/user/tong/solidstate.html](http://www.damtp.cam.ac.uk/user/tong/solidstate.html)

Band theory, Fermi surfaces, phonons, electrons in magnetic fields, and an introduction to the quantum Hall effect. The quantum Hall effect treatment in particular is excellent and connects naturally to the Chern–Simons theory in the gauge theory notes — the integer quantum Hall effect is a topological phenomenon characterised by a Chern–Simons term in the effective action.

---

## Sidney Coleman — Harvard QFT Lectures

The late Sidney Coleman taught the QFT course at Harvard for decades, and is widely considered the greatest QFT teacher of the 20th century. His lectures from the mid-1970s were transcribed by Brian Hill and are available at [damtp.cam.ac.uk/user/tong/qft.html](http://www.damtp.cam.ac.uk/user/tong/qft.html) (linked from Tong's page). The transcribed notes were subsequently extended into a textbook: *Quantum Field Theory: Lectures of Sidney Coleman*, edited by Bryan Gin-ge Chen et al. (World Scientific, 2019).

**What Coleman does differently.** Coleman's approach is unusual in that he spends more time than any other QFT course on the harmonic oscillator — not because it is simple, but because every level of QFT is the harmonic oscillator in more abstract language ("The career of a young theoretical physicist consists of treating the harmonic oscillator in ever-increasing levels of abstraction"). This insistence on building from the simplest nontrivial case is characteristic of his pedagogy.

The treatment of renormalisation in Coleman's notes is the most conceptually honest I have encountered. He does not present renormalisation as a procedure for removing infinities (the usual first presentation, which is technically correct but physically misleading). He presents it as a statement about the physical parameters of the theory — mass and coupling constant — are defined at a renormalisation scale, and the relationship between parameters at different scales is the RG.

**What I have read.** The first half (through Chapter 9 in the textbook version, covering canonical quantisation, the LSZ formula, and the beginning of renormalisation) I have worked through carefully. The second half (renormalisation at higher loops, the renormalisation group) I have read once. The course on *Aspects of Symmetry* (Coleman's lectures on spontaneous symmetry breaking, instantons, and the $1/N$ expansion) is separate and also available — I have read the instanton and $1/N$ sections.

---

## Freeman Dyson — Cornell Lectures on Advanced Quantum Mechanics (1951)

Available online through various archives. These are Dyson's transcribed 1951 lectures, in which he presented the techniques of QED — Feynman diagrams, the $S$-matrix, the Dyson series — to Cornell graduate students shortly after Feynman, Schwinger, and Tomonaga's work on renormalised QED. The lectures are historically remarkable: Dyson understood Feynman's methods better than Feynman could explain them, and these notes are the clearest early account of what the Feynman rules actually mean.

I read these partly for historical interest and partly because Dyson's formulation of the $S$-matrix expansion is cleaner than most modern treatments. The derivation of the Feynman rules from the Dyson series — without path integrals — is in some ways more transparent than the path integral derivation.

---

## Frederic Schuller — Lectures on the Geometrical Anatomy of Theoretical Physics

Available on YouTube at [Schuller's Lectures](https://www.youtube.com/watch?v=V49i_LM8B0E&list=PLPH7f_7ZlzxTi6kS4vCmv4ZKm9u8g5yic). A full-semester course (28 lectures, approximately 90 minutes each) on the Geometrical Anatomy of Theoretical Physics.

**Why this course is exceptional.** Schuller is a mathematical physicist at Utrecht, and his approach is to start from the absolute mathematical foundations and build upward. The result is the most rigorous treatment of differential geometry and fibre bundles for physicists that I have found outside formal mathematics textbooks. The section on principal fibre bundles (lectures 20–24) builds the gauge theory framework from scratch: a gauge field is a connection on a principal $G$-bundle, a gauge transformation is a vertical automorphism of the bundle, the field strength is the curvature of the connection. This is the genuine geometric picture, not an approximation.

**What I used it for.** After working through Tong's notes on gauge theory, Schuller's lectures provided the geometric foundation that Tong's notes treat briefly. The concept of the Ehresmann connection on a principal bundle — which is what a gauge field actually is — is derived carefully in Schuller's lectures. This changed how I understand the BRST structure: the ghost field is a Lie algebra valued 1-form on the bundle, and the BRST operator is the exterior derivative on the bundle restricted to the fibre.

**The companion notes.** Simon Rea's typed notes from the course are available online and are an excellent complement to the videos.

---

## Perimeter Institute — PSI Courses

The Perimeter Scholars International program at the Perimeter Institute in Waterloo, Canada is a one-year masters program for exceptional physics students. All PSI lectures are recorded and available through the Perimeter Institute Recorded Seminar Archive (PIRSA) at [pirsa.org](https://pirsa.org).

### Quantum Field Theory (PSI)

Multiple years available. The courses I have worked through most are the QFT courses taught by Frederic Dupuis (path integral approach) and Pedro Liendo (renormalisation). The PSI QFT courses tend to emphasise the path integral formalism from the start, which is a different pedagogical choice from Tong's canonical quantisation approach. Having worked through both, I think the canonical approach is better for the first encounter (you understand what you are quantising) and the path integral approach is better for the second (the connection to classical mechanics is clearer and gauge fixing is more natural).

### General Relativity (PSI)

The PSI GR courses I have watched are taught by Frederic Schuller (whose pedagogy matches his YouTube lectures) and Neil Turok. Turok's lectures are unusual in their emphasis on cosmology and the initial singularity; the treatment of the Big Bang and its relationship to black hole singularities is the best I have found at this level.

### Quantum Gravity (PSI)

[pirsa.org/quantum-gravity](https://pirsa.org/quantum-gravity)

The most advanced course I have worked through. The PSI quantum gravity courses cover loop quantum gravity, spin foams, causal dynamical triangulations, and the holographic principle in detail. The lectures by Lee Smolin (on the conceptual foundations of quantum gravity), by Bianca Dittrich (on spin foams and coarse graining), and by Laurent Freidel (on the relational interpretation of quantum gravity) are the most relevant to the QGET framework.

### Foundations of Quantum Mechanics (PSI)

The courses by Rob Spekkens on the foundations and by Lucien Hardy on the axiomatic reconstruction of quantum mechanics from information-theoretic principles are exceptional. Hardy's reconstruction — deriving the Hilbert space formalism from five information-theoretic axioms — is directly relevant to understanding whether the QGET entanglement structure can be derived from axioms rather than postulated.

---

## 't Hooft's How to Become a Good Theoretical Physicist

[goodtheorist.science](https://www.goodtheorist.science/)

Gerard 't Hooft, Nobel laureate and one of the architects of modern gauge theory (he proved renormalisability of non-Abelian gauge theories with his student Veltman in 1971), maintains a personal website with a structured curriculum for self-studying theoretical physics. The list covers mathematics, classical mechanics, statistical mechanics, quantum mechanics, electromagnetism, GR, QFT, and string theory, with specific book recommendations at each stage.

I have used this page as a checklist and a sanity check on my own curriculum. The recommendations align broadly with what I have described here, with the addition of 't Hooft's emphasis on knowing classical physics to the same depth as quantum physics — a corrective against the tendency to rush toward QFT without solid foundations in classical mechanics and electrodynamics.

---

## Kevin Zhou's Physics Olympiad and Graduate Notes

[knzhou.github.io](https://knzhou.github.io)

Kevin Zhou (Stanford) has published detailed notes on physics ranging from olympiad level through graduate QFT and GR. His graduate QFT notes ([knzhou.github.io/notes/qft.pdf](https://knzhou.github.io/notes/qft.pdf)) are an excellent annotated bibliography — he assesses every major QFT reference with specific comments on what each does well and where it is weak. His notes on the Standard Model, electroweak theory, and QCD are well-organised and cover topics that Tong's introductory QFT notes do not reach.

**What I have used.** The QFT resource guide as a map when deciding what to read. The Standard Model notes for understanding the electroweak sector, which I needed when situating the Yang–Mills mass generation mechanism in the context of the full Standard Model.

---

## Surya Ganguli — Lecture Notes on Statistical Mechanics of Learning

Available through the Stanford course page. This is not strictly theoretical physics — it is at the intersection of statistical mechanics and machine learning theory. I include it because the renormalisation group and statistical field theory techniques that appear in Tong's statistical field theory notes are the same mathematical framework used to analyse neural network training dynamics and phase transitions in learning systems. The connection is not merely formal: understanding the physics of phase transitions helps understand the phenomenology of neural network learning.

---

## My Own Notes: What I Keep

I keep notes in LaTeX at all times. Below is what I maintain.

**Yang–Mills theory.** A running document that summarises the Stueckelberg extension, the BRST algebra, the one-loop calculation, and the connection to the Gribov problem. Currently about 140 pages. This is not a paper draft — it is a working document that includes failed approaches, questions I have not answered, and calculations I am not sure are correct.

**QGET.** A separate document on the entanglement framework, the classical limit problem, and the connection to the LQG literature. About 90 pages.

**Differential geometry.** A reference document summarising the definitions and theorems I need most: connections, curvature, fibre bundles, the relationship between the Ehresmann connection and the gauge field. Built from Lee, Nakahara, and Schuller's lectures.

**The physics I do not understand.** A list, maintained honestly, of things I have encountered and not yet understood. Currently includes: the full proof that lattice Yang–Mills has a mass gap in the large-$N$ limit and what it implies for finite-$N$; the mathematical content of the AdS/CFT correspondence beyond the basic dictionary; the precise sense in which the BRST cohomology of the Stueckelberg-extended theory is trivial in the ghost sector.

---

## A Note on Taking Notes

The activity that I have found most useful is not reading lecture notes — it is rewriting them. Taking a proof or a derivation that I have understood in Tong's notes or Coleman's lectures and writing it out from memory in my own LaTeX file, using my own notation, is the test that distinguishes actual understanding from the feeling of understanding. The feeling is common; the thing itself is rarer and more valuable.

The mathematics in my papers came from this process. The BRST algebra in my Stueckelberg paper is written in my own notation because I derived it myself — following Tong's gauge theory notes, Coleman's lectures, and Becchi–Rouet–Stora's original 1976 paper — and then wrote it from scratch. The calculation has the minor errors and the idiosyncrasies of something actually done, rather than the smoothness of something copied. That is how it should be.

---

*Last updated March 2026. This page is updated as I work through new material.*