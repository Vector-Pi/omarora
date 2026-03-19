---
title: "Starting with Theoretical Physics"
date: 2026-02-06
parent: "Theoretical Physics"
---


I started learning theoretical physics in seventh grade. Not the pop-science version — not *A Brief History of Time* and YouTube videos about black holes, though those came first and are not nothing — but the actual subject, with equations. I did not know what I was doing at the time, and I made many of the mistakes that most people make. I read things before I had the mathematics for them. I spent months on topics that were less essential than I thought. I also stumbled onto resources that genuinely changed what I understood.

What follows is the map I wish someone had given me at the start. It is complete — from absolute beginnings through classical mechanics, electrodynamics, quantum mechanics, statistical mechanics, special and general relativity, quantum field theory, and gauge theory — because anything less complete would have been the kind of guide that feels useful but leaves you stranded. I have tried to be specific about what each resource is good for, what its weaknesses are, and what the mathematical prerequisites actually are before you open it.

The path I describe is not the only path. But it is a coherent one, and I can vouch for most of it.

---

## Before Physics: The Mathematical Foundation

Theoretical physics is applied mathematics. Not in the sense that you need all of mathematics before you can start — you do not — but in the sense that every stage of physics corresponds to a stage of mathematics, and trying to do physics without the relevant mathematics is like trying to read a book in a language you do not speak. You can get a rough impression. You cannot actually read it.

The mathematics you need, roughly in order:

**Stage 1 (before classical mechanics):** Calculus — single and multivariable. Limits, derivatives, integrals, partial derivatives, multiple integrals. Vector algebra: dot products, cross products, the geometric intuition. Basic differential equations.

**Stage 2 (alongside classical mechanics and electrodynamics):** Linear algebra — matrices, eigenvalues, linear transformations. Vector calculus — gradient, divergence, curl, the integral theorems (Green's, Stokes', divergence). Ordinary differential equations at a more systematic level.

**Stage 3 (before quantum mechanics):** Linear algebra more deeply — abstract vector spaces, inner products, Hermitian operators. Complex analysis — contour integration, the residue theorem. Partial differential equations — the wave equation, the heat equation, separation of variables.

**Stage 4 (before QFT and GR):** Differential geometry — manifolds, tensors, covariant derivatives, curvature. Group theory and Lie algebras. Fourier analysis. Functional analysis basics.

You do not need to complete each stage before starting the corresponding physics. In practice you learn the mathematics and the physics together. But the sequence matters, and if you find yourself reading about tensors in a GR textbook before you have ever seen a linear transformation, the confusion is not because tensors are mysterious — it is because the prerequisite is missing.

For detailed resource recommendations at each mathematical stage, see the [Mathematics Prerequisites for QFT and GR](/omarora/theoretical-physics/math-prerequisites-for-qft-gr/) page.

---

## Stage 0 — First Contact

Every physicist has a moment where the subject becomes real. For me, at twelve or thirteen, it was finding Feynman. Not the lectures — those came later. The popular books: *Surely You're Joking*, and then *What Do You Care What Other People Think*, and then *The Character of Physical Law*, which is the one that matters at this stage.

**The Character of Physical Law** — Richard Feynman. A series of lectures, not a textbook. Feynman talks about what physical laws are, what they feel like from the inside, why conservation laws are beautiful, what quantum mechanics does to your picture of reality. No equations you cannot follow. More important than any specific fact it conveys is the disposition it models: the combination of rigorous honesty and genuine delight in the subject.

**The Feynman Lectures on Physics, Vol. I** — Feynman, Leighton, Sands. This is the bridge between first contact and real study. Volume I covers classical mechanics, waves, and thermodynamics at a level that assumes some calculus. The exposition is unlike any other physics text — Feynman does not tell you facts, he shows you how a physicist thinks about things. Read it early, read it again later. It will mean different things each time.

**Six Easy Pieces / Six Not-So-Easy Pieces** — distilled excerpts from the Lectures. If you are genuinely at the beginning, Six Easy Pieces gives you access to Feynman's way of thinking before committing to the full volumes.

---

## Stage 1 — Classical Mechanics

Classical mechanics is the first real subject. It is where you learn to think about physics mathematically — where $F = ma$ becomes the Euler-Lagrange equations, where the trajectory of a particle becomes a path that extremises an action. This transition is where theoretical physics begins.

There is a natural progression here: Newtonian mechanics first, then Lagrangian and Hamiltonian mechanics. Do not skip the first to get to the second — the Lagrangian formulation only makes sense as a generalisation of something you already understand concretely.

---

**An Introduction to Classical Mechanics** — David Morin

The best undergraduate classical mechanics textbook for a self-learner. Morin is clear, comprehensive, and the problems are outstanding. He covers Newtonian mechanics thoroughly before moving to Lagrangians and Hamiltonians, and the treatment of constraints and the calculus of variations is cleaner than most alternatives. The examples are chosen well and there are hints for most problems.

This is where I spent serious time early on. If you work through Morin properly — not reading, but actually solving problems — you will have a genuine understanding of classical mechanics, not just familiarity with its equations.

---

**Classical Mechanics** — John Taylor

A gentler alternative to Morin, with more physical motivation and less mathematical density. The treatment of the Lagrangian formalism is excellent for a first encounter. If Morin feels too compressed at the start, Taylor is the right entry point.

---

**Classical Mechanics** — Landau and Lifshitz (Course of Theoretical Physics, Vol. 1)

The first volume of the Landau–Lifshitz Course. It opens with the principle of least action and derives Newtonian mechanics from it — the opposite order from Morin. This is breathtaking the first time you see it. The book is short, terse, and every sentence is load-bearing. It is not a first textbook and it is not easy, but it is one of the most beautiful pieces of mathematical physics writing that exists. Read it after Morin or Taylor, not instead of them.

The Landau–Lifshitz Course (ten volumes) is the systematic treatment of all of theoretical physics at the graduate level. I return to individual volumes repeatedly. The series as a whole — mechanics, classical fields, quantum mechanics, quantum electrodynamics, statistical physics, fluid mechanics, elasticity theory, electrodynamics of continuous media, physical kinetics — is the most coherent curriculum in theoretical physics ever written by a single school.

---

**The Theoretical Minimum: Classical Mechanics** — Leonard Susskind and George Hrabovsky

Susskind's book is aimed at adults who once knew calculus and have forgotten it. If that is not your situation, Morin is better. But Susskind is exceptional at explaining the *structure* of classical mechanics — why we use generalised coordinates, what symplectic structure means, why Hamiltonian mechanics is the right framework for the transition to quantum mechanics. The accompanying video lectures at [theoreticalminimum.com](https://theoreticalminimum.com) are free and excellent.

---

**David Tong's Classical Dynamics lecture notes** — [damtp.cam.ac.uk/user/tong/teaching.html](http://www.damtp.cam.ac.uk/user/tong/teaching.html)

Free, clearly written, used for Part IA of the Cambridge Mathematical Tripos. Covers Newtonian and Lagrangian mechanics concisely. An excellent supplement.

---

## Stage 2 — Special Relativity

Special relativity should be learned early, before electrodynamics and well before general relativity. The sooner you are comfortable thinking in four-vectors and Lorentz transformations, the more natural electrodynamics and QFT will feel.

---

**Spacetime Physics** — Taylor and Wheeler

The most conceptually illuminating introduction to special relativity that exists. Taylor and Wheeler teach you to think in spacetime rather than converting between reference frames — the right approach from the start. The invariant interval as the fundamental object, not the Lorentz transformation, is how relativistic physics is actually done.

---

**Special Relativity** — A. P. French

A thorough undergraduate treatment, more mathematical than Taylor–Wheeler. Covers the kinematic effects, relativistic dynamics, and four-vector formalism systematically. The treatment of four-momentum and energy-momentum invariance is particularly good.

---

**Dynamics and Relativity** — David Tong (lecture notes)

Free Cambridge notes covering special relativity alongside Newtonian mechanics. Clean, precise, and ideal if you want a compact rigorous treatment before moving to electrodynamics.

---

## Stage 3 — Electrodynamics

Electrodynamics is where classical field theory begins. You encounter your first field equations, your first gauge symmetry, your first nontrivial relations between geometry and physics. Understanding Maxwell's equations deeply — not just being able to use them, but understanding what gauge invariance means, why the vector potential is fundamental, what radiation is — is essential preparation for everything that follows.

---

**Introduction to Electrodynamics** — David Griffiths

The standard. Griffiths is exceptionally clear, the problems are carefully chosen, and the treatment covers everything from Coulomb's law through radiation and relativistic electrodynamics. The chapter on electromagnetic waves and the final chapter on electrodynamics and relativity are the best in the book. Every problem is worth attempting.

A mild criticism: Griffiths presents gauge invariance late and somewhat superficially. For the purposes of learning QFT and gauge theory later, you will want to supplement with Tong's electromagnetism notes, which treat gauge invariance as the central structural fact from the beginning.

---

**Electricity and Magnetism** — Purcell and Morin

Purcell derives magnetism from electrostatics and special relativity — the correct physical picture — rather than treating them as separate phenomena unified later. This approach gives a much deeper understanding of what magnetism is. The level is slightly below Griffiths but the conceptual clarity is higher. Use it as a companion, especially for the relativity chapters.

---

**Electrodynamics** — David Tong (lecture notes) — [damtp.cam.ac.uk/user/tong/em.html](http://www.damtp.cam.ac.uk/user/tong/em.html)

The best free treatment of electrodynamics available. Tong's notes cover the same material as Griffiths but with more mathematical precision and a cleaner treatment of gauge invariance, radiation, and the relativistic formulation. Read these alongside or after Griffiths.

---

**Classical Electrodynamics** — Jackson

The graduate reference. Dense, comprehensive, and used in every serious graduate program in physics. Do not begin here. Come to Jackson when you need it — as a reference for specific calculations or for topics (multipole expansion, waveguides, radiation reaction) that go beyond Griffiths. The problems are legendarily difficult.

---

## Stage 4 — Quantum Mechanics

Quantum mechanics is the first genuinely conceptually difficult subject. Not technically difficult — the calculations in an introductory course are often straightforward — but conceptually difficult in the sense that it requires you to abandon the assumptions about how the world works that every prior theory has reinforced. The wavefunction, measurement, uncertainty, spin — these are genuinely strange, and anyone who tells you they are not strange has probably stopped thinking about them.

Learn quantum mechanics in two passes. The first pass (Griffiths) builds the formalism and the intuition. The second pass (Shankar or Sakurai) rebuilds it with more mathematical rigour and deeper structural insight.

---

**Introduction to Quantum Mechanics** — David Griffiths

The standard first textbook. Griffiths starts from the Schrödinger equation, works through the standard model systems (particle in a box, harmonic oscillator, hydrogen atom), and develops the formalism around specific problems. The writing is clear and the examples are well-chosen.

Criticisms worth naming: Griffiths de-emphasises the Dirac formalism and the abstract Hilbert space perspective that you will need later. The treatment of spin is good but the connection to representation theory is absent. These are deliberate pedagogical choices — they make the first encounter gentler. But be aware that the formalism you learn in Griffiths is not quite the formalism you will use in serious quantum mechanics.

---

**Principles of Quantum Mechanics** — R. Shankar

The better second text, or a strong alternative to Griffiths for someone with a solid linear algebra background. Shankar starts from the mathematics — Hilbert spaces, operators, eigenvalue problems — and then builds the physics on top. The treatment is more abstract but ultimately cleaner. The chapters on the harmonic oscillator (using ladder operators systematically), on symmetry and angular momentum, and on path integrals are particularly good.

---

**Modern Quantum Mechanics** — J. J. Sakurai and Napolitano

The standard graduate text. Sakurai assumes you already know quantum mechanics at the Griffiths level and builds from there — the bra-ket formalism from the start, more emphasis on symmetry and angular momentum, a treatment of approximation methods that is more complete than Griffiths. The problems are harder. Essential reading before QFT.

---

**The Theoretical Minimum: Quantum Mechanics** — Susskind and Friedman

Susskind's approach to quantum mechanics is unusual: he starts from spin-1/2 systems and builds the formalism from there, rather than from the Schrödinger equation. This is actually closer to how modern physicists think about quantum mechanics. Less comprehensive than Griffiths but structurally cleaner. Good as a companion, especially for understanding the connection between quantum mechanics and classical mechanics.

---

**Quantum Mechanics** — David Tong (lecture notes) — [damtp.cam.ac.uk/user/tong/quantum.html](http://www.damtp.cam.ac.uk/user/tong/quantum.html)

Tong's undergraduate QM notes, now also a published textbook. Extremely clear and well-structured. A reliable companion to Griffiths or Shankar.

---

**What is the best way to think about quantum mechanics?**

The answer depends on what you mean by "think about." The Copenhagen interpretation — shut up and calculate — will take you far technically. But if you want to understand what the theory is actually saying about the world, the measurement problem and the different interpretations (many-worlds, pilot wave, relational QM, QBism) are worth understanding. Not as a distraction from the physics, but as a sign that you are taking the physics seriously. Tim Maudlin's *Philosophy of Physics: Quantum Theory* is the clearest treatment of the foundational issues from a philosophical perspective.

---

## Stage 5 — Statistical Mechanics and Thermodynamics

Statistical mechanics is the theory that explains how macroscopic properties (temperature, entropy, pressure) emerge from microscopic dynamics. It is where quantum mechanics meets thermodynamics, and it is the framework for condensed matter physics, cosmology, and quantum field theory at finite temperature.

---

**An Introduction to Thermal Physics** — Daniel Schroeder

The most accessible entry point. Schroeder builds thermodynamics and statistical mechanics simultaneously, with excellent physical intuition throughout. The treatment of entropy and the second law is the clearest I have encountered at this level. Good for a first pass before the more demanding texts.

---

**Statistical Mechanics** — Pathria and Beale

The standard graduate reference. Comprehensive and rigorous, covering classical and quantum statistical mechanics, ensemble theory, phase transitions, and the renormalisation group at an introductory level. Dense but reliable.

---

**Statistical Physics** — Landau and Lifshitz (Course of Theoretical Physics, Vol. 5)

Landau's treatment is the most elegant. It derives thermodynamics from statistical mechanics systematically and the treatment of phase transitions is exceptional. Like all L&L volumes: terse, demanding, and worth the effort.

---

**Statistical Field Theory** — David Tong (lecture notes) — [damtp.cam.ac.uk/user/tong/sft.html](http://www.damtp.cam.ac.uk/user/tong/sft.html)

The graduate-level treatment connecting statistical mechanics to quantum field theory via the path integral and the renormalisation group. Essential reading before QFT at a serious level.

---

## Stage 6 — General Relativity

General relativity is the theory of gravity as the geometry of spacetime. It requires differential geometry — the theory of curved manifolds — as its mathematical framework. The conceptual content is among the most beautiful in all of physics: mass curves spacetime, and curved spacetime tells mass how to move.

---

**Gravity: An Introduction to Einstein's General Relativity** — James Hartle

The most accessible introduction. Hartle uses a "physics first" approach — he develops the physical consequences of GR (black holes, gravitational waves, cosmology) before the full mathematical apparatus. This builds intuition before formalism, which is the right order for most people.

---

**Spacetime and Geometry** — Sean Carroll

The standard modern graduate introduction. Carroll develops the differential geometry from scratch and builds GR on top of it carefully. The writing is clear and the treatment is complete. The chapters on black hole spacetimes and cosmology are particularly good. Carroll also has free lecture notes available at his website.

---

**Gravitation** — Misner, Thorne, and Wheeler (MTW)

The encyclopaedia. 1,279 pages. Everything in GR, treated in extraordinary depth. The "track 1" vs "track 2" structure allows you to read the essential content without the full technical depth. A reference that you will return to for years. The treatment of gravitational waves and the post-Newtonian approximation is the most complete outside the research literature.

---

**General Relativity** — Wald

The mathematically rigorous treatment. Wald develops GR from the perspective of differential geometry and global methods. The treatment of singularity theorems, black hole thermodynamics, and the structure of spacetime is the best available. Demanding but essential if you intend to work in mathematical GR.

---

**General Relativity** — Landau and Lifshitz (Course of Theoretical Physics, Vol. 2)

The L&L treatment of classical field theory and GR together. Approaches GR as a classical field theory, which is exactly right for the transition to QFT. The action formulation of GR is derived early. Like all L&L: terse and beautiful.

---

## Stage 7 — Quantum Field Theory

Quantum field theory is the framework that unifies quantum mechanics and special relativity. It is the language of the Standard Model, of condensed matter physics at low temperatures, of cosmological perturbation theory, and of every serious attempt at quantum gravity. Everything before this point has been preparation for it.

The conceptual leap from quantum mechanics to QFT is significant. In quantum mechanics, you quantise particles — you promote positions and momenta to operators. In QFT, you quantise fields — you promote field configurations to operators. This means infinitely many degrees of freedom, and the infinities that result require renormalisation to manage.

---

**Quantum Field Theory** — David Tong (lecture notes) — [damtp.cam.ac.uk/user/tong/qft.html](http://www.damtp.cam.ac.uk/user/tong/qft.html)

Free. Cambridge Part III level (masters). This is the best starting point for QFT. Tong follows the first five chapters of Peskin and Schroeder but with significantly more explanation and motivation at every step. The treatment of canonical quantisation, the Dirac field, and the Feynman rules for QED is exactly right for a first encounter. The accompanying video lectures, recorded at the Perimeter Institute, are available on the same page. Watch them alongside the notes.

---

**An Introduction to Quantum Field Theory** — Peskin and Schroeder

The standard text. Comprehensive, rigorous, and used in virtually every graduate QFT course in the world. After Tong's notes, Peskin and Schroeder fills in the details — the careful treatment of renormalisation, the full derivation of the Ward identities, non-Abelian gauge theories, the renormalisation group. Parts I and II are the core; Part III covers path integrals and more advanced topics.

Criticisms: the first chapter is famously difficult on a first read. The treatment of renormalisation in the middle of the book (Chapters 10–13) requires significant effort. Come to Peskin with Tong already under your belt.

---

**The Quantum Theory of Fields** — Weinberg (three volumes)

Weinberg's QFT is the mathematician's version — derived from first principles with more rigour and less physics intuition than Peskin. Volume I builds QFT from the requirement that quantum mechanics be consistent with special relativity; Volume II covers the Standard Model; Volume III covers supersymmetry. Essential for anyone who wants to understand what QFT actually is, not just how to calculate with it.

---

**Quantum Field Theory in a Nutshell** — Anthony Zee

The physicist's version. Zee covers an extraordinary range of topics — path integrals, renormalisation, gauge theories, gravity as a gauge theory, condensed matter applications, string theory glimpses — with physical intuition and minimal formalism. Not a reference and not a course: a book that makes you want to understand QFT and gives you a sense of its reach.

---

**Sidney Coleman's Quantum Field Theory lectures** — Harvard, 1970s–1980s

Coleman was the greatest QFT pedagogue of his generation. The lecture notes (transcribed by Brian Hill, available freely online) cover the first semester of QFT in extraordinary depth, with Coleman's characteristic combination of precision, humour, and conceptual honesty. The treatment of the harmonic oscillator in QFT and the discussion of why renormalisation is not a trick are particularly good. The notes have recently been extended into a published textbook.

---

**Gauge Theory** — David Tong (lecture notes) — [damtp.cam.ac.uk/user/tong/gaugetheory.html](http://www.damtp.cam.ac.uk/user/tong/gaugetheory.html)

~400 pages. Covers non-Abelian gauge theories in four dimensions — Yang–Mills theory, the beta function, instantons, confinement, Wilson lines, the Higgs mechanism, and 't Hooft lines. This is the mathematical structure of the Standard Model. Essential reading for anyone working on gauge theory. Directly relevant to my own research.

---

## Stage 8 — Advanced Topics

Once you have solid foundations in QFT and GR, the advanced topics branch. The right choice depends on your interests. I note below what I have engaged with most directly.

---

### BRST Quantisation and Gauge Theory

**BRST quantisation** is the modern framework for quantising gauge theories while maintaining manifest covariance. It introduces ghost fields (the Faddeev–Popov ghosts) and the BRST operator, a nilpotent fermionic symmetry that encodes gauge invariance at the quantum level. This is the framework underlying the quantisation of Yang–Mills theory, string theory, and gravity.

The foundational papers are Becchi–Rouet–Stora (1976) and Tyutin (1975). The modern treatment is in:

- **Quantum Field Theory** — Weinberg, Chapter 15 (quantisation of non-Abelian gauge theories)
- **Quantization of Gauge Systems** — Henneaux and Teitelboim. The complete treatment of constrained Hamiltonian systems and BRST quantisation. Demanding but thorough.
- Tong's gauge theory notes, Chapter 2.

This is the framework I used in my paper on the Stueckelberg extension of Yang–Mills theory.

---

### The Mass Gap Problem

The Yang–Mills existence and mass gap problem is one of the Clay Millennium Prize Problems. The problem is to prove that Yang–Mills theory on $\mathbb{R}^4$ exists as a quantum field theory and has a positive mass gap — i.e., the lowest energy state above the vacuum has strictly positive energy.

The problem statement is in the Clay Mathematics Institute volume *The Millennium Prize Problems*. The physics background requires QFT, non-perturbative methods, and lattice gauge theory. My own research has approached a piece of this problem — the mass generation mechanism — through the Stueckelberg extension.

Essential reading:
- Jaffe and Witten, "Quantum Yang–Mills Theory" (the Clay problem statement)
- Tong's gauge theory notes on confinement and the Wilson criterion
- Kogut and Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories" (1975)

---

### Quantum Gravity and String Theory

**General Relativity and Quantum Mechanics are incompatible.** This is the central unsolved problem of theoretical physics. GR is a classical field theory that treats spacetime as a smooth manifold. Quantum mechanics requires that all fields be quantised, including the metric. When you try to quantise gravity perturbatively (treating it as a spin-2 field on flat spacetime), you get a non-renormalisable theory — the ultraviolet divergences cannot be removed by a finite number of counterterms.

The two main approaches to a theory of quantum gravity are string theory and loop quantum gravity. I currently find the mathematical structure of string theory more compelling; LQG has a more direct connection to the geometry of GR.

For string theory:
- **A First Course in String Theory** — Zwiebach. The undergraduate introduction. More accessible than anything else and does not require QFT.
- **String Theory** — Polchinski (two volumes). The graduate reference. D-branes, compactification, and the full framework.
- **String Theory** — David Tong (lecture notes) — [damtp.cam.ac.uk/user/tong/string.html](http://www.damtp.cam.ac.uk/user/tong/string.html). The best free treatment.

---

## Online Lectures and Courses

**Leonard Susskind's Theoretical Minimum** — [theoreticalminimum.com](https://theoreticalminimum.com)

Free video courses covering classical mechanics, quantum mechanics, special relativity, statistical mechanics, cosmology, classical field theory, quantum entanglement, and more. Susskind's courses are explicitly aimed at people who want genuine theoretical understanding rather than pop-science. The clarity of his lectures on the relationship between classical and quantum mechanics is exceptional.

**David Tong's full lecture notes** — [damtp.cam.ac.uk/user/tong/teaching.html](http://www.damtp.cam.ac.uk/user/tong/teaching.html)

Free notes covering the full Cambridge theoretical physics curriculum: vector calculus, classical dynamics, electromagnetism, quantum mechanics, statistical mechanics, quantum field theory, gauge theory, statistical field theory, string theory, solid state physics, and more. This is the closest thing to a free complete theoretical physics curriculum that exists.

**Perimeter Institute Recorded Seminar Archive (PIRSA)** — [pirsa.org](https://pirsa.org)

A permanent, searchable archive of thousands of seminars, courses, and lectures from the Perimeter Institute for Theoretical Physics. Includes full graduate courses on QFT, GR, quantum gravity, string theory, condensed matter, and foundations of quantum mechanics. The PSI (Perimeter Scholars International) courses are the best free graduate-level physics lectures available. Free, citable, and searchable by topic.

**Perimeter Institute PSI Online** — [perimeterinstitute.ca/online-courses](https://perimeterinstitute.ca/online-courses)

Free online learning modules at graduate level, with lecture notes, problem sets, and recorded video. Covers QFT (canonical and path integral), statistical field theory, classical mechanics and symplectic geometry, and more.

**MIT OpenCourseWare Physics** — [ocw.mit.edu/courses/physics/](https://ocw.mit.edu/courses/physics/)

Free course materials — lecture notes, problem sets, exams — from MIT physics courses at all levels. The 8.04 (Quantum Physics I), 8.05 (Quantum Physics II), 8.033 (Relativity), and 8.323 (Relativistic Quantum Field Theory) course pages are particularly useful.

---

## The Landau–Lifshitz Course

The Course of Theoretical Physics by Landau and Lifshitz deserves its own section. It is ten volumes covering the entirety of theoretical physics at a graduate level, written by the Soviet school in the mid-20th century. Every volume is short, terse, and contains almost no wasted words.

| Volume | Topic |
|--------|-------|
| 1 | Mechanics |
| 2 | Classical Theory of Fields |
| 3 | Quantum Mechanics |
| 4 | Quantum Electrodynamics (Berestetskii, Lifshitz, Pitaevskii) |
| 5 | Statistical Physics, Part 1 |
| 6 | Fluid Mechanics |
| 7 | Theory of Elasticity |
| 8 | Electrodynamics of Continuous Media |
| 9 | Statistical Physics, Part 2 |
| 10 | Physical Kinetics |

Volume 2 (*Classical Theory of Fields*) is the one I return to most. It covers special relativity, electrodynamics as a field theory, and general relativity from a unified action-principle perspective. The derivation of the stress-energy tensor from the action, the treatment of the electromagnetic field tensor, and the introduction to GR are the best treatments of these topics at this level of conciseness.

Volume 3 (*Quantum Mechanics*) is the most demanding but contains things no other QM textbook does — the treatment of the quasi-classical approximation, the angular momentum theory, and the systematic use of symmetry throughout are exceptional.

---

## An Honest Account of the Path

I started learning this in grade 7. The truth of that beginning is that I understood almost nothing of what I was reading for the first year. I read about quantum mechanics without having calculus; I read about special relativity without knowing what a four-vector was. I accumulated a vocabulary before I understood what the words meant.

This is not entirely wasted. Some of the vocabulary sticks, and when the mathematics arrives, the words have something to attach to. But it is slower than the alternative, which is to learn the mathematics first and the physics simultaneously. If I were starting again, I would spend the first year doing nothing but calculus and linear algebra, and I would read Morin's classical mechanics alongside.

What I did not regret at any stage was the decision to take the physics seriously enough to learn the mathematics. The pop-science version of any of these subjects — quantum mechanics as spooky action at a distance, general relativity as space being stretchy — is not false exactly, but it does not give you anything to work with. The actual theory, with equations, is harder and more beautiful and more useful.

The path from Feynman's popular books to publishing papers on Yang–Mills theory took roughly five years, done alongside school, olympiad training, and everything else. It is not the fastest path and it is not the path I would design from scratch. But it is a real path, and it leads somewhere.

The work continues.
---

*Last updated March 2026.*