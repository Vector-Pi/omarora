---
title: "Philosophy for STEM Students"
date: 2026-03-07
parent: "Philosophy"
---


I want to start with something honest: I did not come to philosophy through a course, and I would not have come to it at all through the courses I encountered. The philosophy available to physics and mathematics students at most institutions is a history-of-ideas survey — you learn that Descartes said X and Hume said Y, you write an essay about whether they agreed, and you leave knowing more about the history of philosophy and no more about how to think. That is not what I mean when I say philosophy matters for scientists and mathematicians.

What I mean is more specific and more defensible. There are questions that live inside the technical work — not at the edge of it or in the popular literature about it, but right in the middle — that are philosophical questions. They do not have experimental answers; they require conceptual analysis. A physicist who has never thought about the philosophy of science is not therefore a worse physicist in the way that a physicist who has never learned quantum field theory is a worse physicist. But they are carrying around unexamined assumptions about what science is doing, what mathematical structures are, and what counts as an explanation — assumptions that occasionally matter and are occasionally wrong.

This page is about those questions: what they are, why they are genuinely hard, where they come from in the scientific work, and what the philosophical literature offers. It is also about where to start if you are coming from physics or mathematics and have not read philosophy before.

---

## Why Physics Generates Philosophical Problems Whether You Want It To

The standard scientific attitude is roughly: we do the experiment, we check the theory, the theory that passes the test is the right theory. Philosophy is for people who cannot do experiments. This attitude is understandable but wrong in a specific and important way. It cannot be consistently held, and when it is pushed hard enough it generates exactly the philosophical problems it was supposed to avoid.

**The measurement problem in quantum mechanics** is the clearest example. The Schrödinger equation is deterministic — it evolves quantum states unitarily according to a perfectly well-defined rule. But when we perform a measurement, we observe a definite outcome, and the state appears to "collapse" to that outcome. Nothing in the Schrödinger equation produces this collapse. The "Copenhagen interpretation" — the working assumption of most practising physicists — does not resolve the problem; it instructs you to stop asking questions about what happens before the measurement. That is a philosophical instruction disguised as a methodological one.

The alternatives — Many Worlds (Everett), pilot wave theory (de Broglie-Bohm), GRW spontaneous collapse, relational quantum mechanics, QBism — are genuine philosophical positions about what the formalism means, what exists, and what counts as a satisfactory account of physical reality. Every version of quantum mechanics is a philosophical position. There is no "just shut up and calculate" that is not itself a philosophical position (it is instrumentalism, and instrumentalism has well-developed critics and defenders in the philosophy of science literature).

I encountered this directly when I was working through the foundations of quantum field theory for my Yang-Mills research. The perturbative expansion is formal — the series does not converge in the mathematical sense. The renormalisation procedure involves subtracting divergent quantities in a way that, rigorously, requires justification. What justification? The answer — that it works, that the predictions are confirmed to extraordinary precision — is an empirical answer, not a mathematical one. The philosophical question of whether this constitutes a genuine physical theory in some robust sense, or whether it is a calculational algorithm that happens to produce correct numbers, is open. I do not know the answer, but I think about it.

---

## The Unreasonable Effectiveness Problem

In 1960, Eugene Wigner delivered a lecture at New York University called "The Unreasonable Effectiveness of Mathematics in the Natural Sciences." The central observation: mathematical structures developed for purely aesthetic reasons, with no physical application in mind, repeatedly turn out to be exactly the right language for describing physical phenomena discovered later.

The examples are well-known but the more you think about them the more striking they become. Non-Euclidean geometry was developed by Riemann as an abstract mathematical generalisation in 1854. Fifty years later, Einstein needed exactly that geometry — Riemannian manifolds with curvature — to formulate general relativity. The mathematicians were not thinking about gravity; they were thinking about the abstract structure of smooth manifolds. Yet the structure was the right one.

Group theory was developed as pure mathematics in the 19th century. When quantum mechanics was being formulated in the 1920s, Wigner himself — who won the Nobel Prize partly for this observation — found that the representation theory of the Poincaré group classifies all elementary particles. The spin of an electron is not something you add to the theory; it falls out of the irreducible representations of the symmetry group of spacetime.

This is personal for me in a specific way. The mathematics I use in the Yang-Mills and QGET research — fibre bundles, connections, curvature, characteristic classes — was developed by differential geometers in the 19th and early 20th centuries with no thought of gauge theory. When Yang and Mills introduced non-Abelian gauge fields in 1954, they were writing down the physics of a situation where the correct mathematical structure — the Ehresmann connection on a principal bundle — was already sitting in the mathematics literature, fully worked out, waiting to be applied. I find this genuinely strange. The universe did not have to be describable by mathematics invented on aesthetic grounds by people who were not thinking about physics. That it is — consistently, across centuries — is a fact that deserves a philosophical account.

**The positions on offer:**

*Mathematical Platonism* (Penrose, Hardy, Gödel): mathematical structures exist independently of human minds, in some abstract realm. The universe is described by mathematics because the universe *is* mathematical — physical reality is a mathematical structure. This explains Wigner's observation but at the cost of an ontology that is hard to make sense of.

*Structuralism* (Resnik, Shapiro): mathematics is the study of abstract structures, and science finds that the world has structure. The effectiveness is not mysterious — science is in the business of finding structure, and mathematics is the language of structure.

*Naturalism* (Quine, Maddy): mathematics is continuous with science. Mathematical claims are justified by their indispensable role in scientific theories, just as theoretical posits in science are justified by their role in explaining observations.

*The prosaic account* (Visser, Hamming): the effectiveness is not that unreasonable. We developed the mathematics we found useful, we applied the mathematics we developed, and the mathematics that survived the selection process is the mathematics that happened to work. The abandoned mathematics — the beautiful structures that turned out to be irrelevant to physics — does not make headlines.

Atiyah turned the problem around with "The Unreasonable Effectiveness of Physics in Mathematics" — the claim that physics, specifically quantum field theory and string theory, has generated genuinely new mathematics (Donaldson theory of 4-manifolds, mirror symmetry, quantum cohomology) that mathematicians would not have found without it.

I do not have a settled position on this. I find the Platonist account genuinely tempting — the universe does seem to be made of mathematics in a way that is not merely metaphorical — and I find the naturalist account honest in its refusal to invoke a separate mathematical realm. The question is live and worth thinking about.

---

## The Philosophy of Mathematics: Four Problems You Cannot Avoid

### 1. What are mathematical objects?

When you prove a theorem about the Riemann zeta function, what are you talking about? The zeta function is a mathematical object. Does it exist? In what sense? The question is not merely semantic. Your answer determines what you think mathematical proof *achieves* — whether it is discovery (of something that was already there) or invention (of something that did not previously exist).

**Platonism:** mathematical objects exist in an abstract realm, independent of minds. Proofs are discoveries. This explains why mathematics is objective — the Riemann hypothesis is true or false regardless of whether anyone has proved it — but requires an account of how we come to know about abstract objects.

**Formalism** (Hilbert): mathematics is the manipulation of formal symbols according to explicit rules. Mathematical objects are not real entities but formal constructs. The goal is consistency, not truth about some external realm. Gödel's incompleteness theorems damaged Hilbert's programme by showing that no consistent formal system strong enough to express arithmetic can prove its own consistency.

**Intuitionism** (Brouwer): mathematical objects are mental constructions. A mathematical object exists only when it has been constructed, and a theorem is true only when a proof has been constructed. This requires rejecting the law of excluded middle ($P \lor \lnot P$) for infinite domains — you cannot claim that the Riemann hypothesis is either true or false unless you have a proof or a disproof. Most mathematicians find this too restrictive.

**Structuralism:** mathematics is about structures — not particular objects but patterns of relationships. The natural numbers are not particular objects; they are positions in a structure satisfying the Peano axioms.

### 2. What does it mean to prove something?

A proof, formally, is a finite sequence of statements each of which is either an axiom or follows from previous statements by a rule of inference. In practice, mathematical proofs are not fully formal derivations — they are arguments written in a mixture of mathematical notation and natural language, and their correctness depends on the judgment of mathematicians who read them.

**Gödel's incompleteness theorems** (1931) showed that any consistent formal system strong enough to express arithmetic is incomplete — there are true statements about the natural numbers that cannot be proved within the system. This result has philosophical implications that are still contested. Does it show that mathematical truth outruns formal provability? Does it refute Hilbert's formalism? Does it show something about the nature of mind (Penrose's controversial argument)?

**Computer-assisted proofs:** the four colour theorem (proved by Appel and Haken in 1976 with computer assistance) and Hales' proof of the Kepler conjecture (2005) involved checking cases that no human could verify individually. Are these genuine mathematical proofs? What is the epistemic status of mathematical claims that are "proved" by an algorithm whose correctness is itself only probabilistically verified?

### 3. Why is logic not a foundation for everything?

Frege attempted to derive all of mathematics from pure logic. Russell's paradox (the set of all sets that do not contain themselves: does it contain itself?) showed that Frege's system was inconsistent. Russell and Whitehead's *Principia Mathematica* repaired the damage with a theory of types, but at the cost of complexity that made the project unwieldy. Quine's observation: if set theory is logic, logic is surprisingly powerful; if set theory is mathematics, the reduction to logic is not complete.

### 4. Are mathematical truths contingent?

Could mathematics have been different? Could $2 + 2$ have equalled 5? Most mathematicians intuitively answer no — mathematical truths are necessary, not contingent. But the question of why they are necessary, and what necessity means, is not settled. Modal logic provides a formal framework (possible worlds, accessibility relations) for discussing necessity and possibility, but does not by itself answer the metaphysical question.

---

## The Philosophy of Science: What Scientists Assume Without Knowing It

### What is a scientific explanation?

The standard account (Hempel's covering law model): a scientific explanation is a deductive argument from general laws and initial conditions to the event being explained. This is the view implicit in most scientific practice, and it faces immediate problems: irrelevant information can be deduced from laws (the length of a shadow can be deduced from the sun's position and the height of the flagpole, but the height does not explain the shadow length — it is the other way around). The deduction works symmetrically; explanation is not symmetric.

The causal account: to explain an event is to identify its causes. This is more intuitive but "cause" is precisely the concept that Hume showed cannot be derived from experience. We observe constant conjunction, not causal necessity.

The mechanistic account (prominent in biology and cognitive science): to explain a phenomenon is to describe the mechanism that produces it — the parts, their organisation, and their activities.

For physics, these accounts all run into the same problem: quantum mechanics appears to deny the causal picture at the level of individual events. The decay of a radioactive atom has no cause in the classical sense — it is irreducibly probabilistic. Does this mean quantum mechanics provides no explanation of individual events, only statistical regularities? Or does it require a revision of what "explanation" means?

### Scientific realism versus anti-realism

**Scientific realism:** the entities posited by our best scientific theories — electrons, quarks, black holes, genes — genuinely exist, and our theories are approximately true descriptions of an observer-independent reality.

**Anti-realism (instrumentalism):** theories are tools for predicting observations, not true descriptions of reality. We should not commit to the existence of theoretical entities we cannot directly observe.

The **pessimistic meta-induction** (Laudan 1981): the history of science is full of theories that were empirically successful but whose central posits were later abandoned — caloric fluid, phlogiston, the luminiferous ether. If successful theories in the past were false, why should we trust that successful theories today are true? The realist needs to explain what distinguishes genuine theoretical success from mere predictive success.

The **no-miracles argument** (Putnam): the predictive success of science would be miraculous if our theories were not approximately true. The convergent success of physics — increasingly accurate predictions across wider domains — is best explained by assuming that our theories are getting closer to the truth.

This is a live and important debate. In my own work, I find myself committed to something like structural realism (Worrall): what science preserves across theory change is not the entities (ether replaced by electromagnetic field) but the mathematical structure (Maxwell's equations survived the transition). The structure is what is real; the interpretation in terms of particular entities is secondary.

### The problem of induction

Already discussed in the schools page but worth naming here as a specifically scientific problem. Every experimental result is a finite set of observations. Every scientific law is a claim about an infinite class of cases. The inference from the finite to the infinite is logically unjustified — this is Hume's problem and it has never been resolved.

Popper's response: science does not induct; it hypothesises and attempts to falsify. A scientific theory is not verified by confirming instances but corroborated by surviving falsification attempts. Falsifiability is the criterion of scientific status.

The problem with Popper: every theory can be protected from falsification by auxiliary hypotheses (if the prediction fails, blame the measurement, the equipment, the setup). Lakatos developed the concept of a research programme (a hard core of central commitments protected by a belt of auxiliary hypotheses) to make Popper's picture more realistic.

---

## Five Specific Entry Points for Scientists and Mathematicians

These are the texts where the overlap between scientific/mathematical work and philosophy is most direct and most productive.

### 1. Eugene Wigner — "The Unreasonable Effectiveness of Mathematics in the Natural Sciences" (1960)

Eleven pages. Free online. The founding document of the problem of mathematical applicability. Read it first for the examples — the group theory / quantum mechanics connection, the non-Euclidean geometry / general relativity connection — and then for the philosophical puzzle it poses at the end. Wigner does not resolve the puzzle; he poses it with clarity. Then read Hamming's "The Unreasonable Effectiveness of Mathematics" (1980) and Atiyah's "The Unreasonable Effectiveness of Physics in Mathematics" for the responses.

### 2. Henri Poincaré — *Science and Hypothesis* (1902) and *The Value of Science* (1905)

Poincaré was one of the greatest mathematicians of the 19th century — the creator of topology, the theory of automorphic functions, and the near-discoverer of special relativity. He was also an exceptionally clear philosophical thinker who thought hard about the foundations of his own work.

*Science and Hypothesis* covers: the nature of mathematical reasoning (is it analytic or synthetic? is it about real objects or formal constructions?), the conventionality of geometry (is Euclidean geometry true? or is it a convenient convention we adopt because it simplifies physics?), the principles of mechanics (are Newton's laws empirical truths or disguised definitions?), and the status of scientific hypotheses.

The **conventionalism** Poincaré defends — the claim that some scientific principles are conventions adopted for convenience rather than empirical discoveries — is the predecessor of all 20th-century philosophy of science. Quine's "Two Dogmas of Empiricism" is a direct response to it. You cannot engage seriously with the philosophy of physics without Poincaré.

### 3. W.V.O. Quine — "Two Dogmas of Empiricism" (1951)

One of the most influential philosophical essays of the 20th century. The two dogmas: (1) the analytic-synthetic distinction (there are truths of meaning, like "all bachelors are unmarried," and truths of fact, like "water boils at 100°C"), and (2) the reduction of empirical claims to sense experience (every claim has a unique observational consequence that would verify or falsify it).

Quine argues both are untenable. The analytic-synthetic distinction cannot be drawn sharply: every claim, including apparently analytic ones, is in principle revisable in the light of experience. The reduction is false: claims face experience not individually but as a "corporate body" — the "web of belief." Any claim can be held true in the face of any evidence, provided we make adjustments elsewhere in the web.

The implications for science: there are no experiment-independent "meanings" that make some claims about the physical world true by definition. Every claim is in principle empirical, including the laws of logic and mathematics. This is holism — the view that the unit of empirical significance is not the individual claim but the theory as a whole.

### 4. Tim Maudlin — *Quantum Non-Locality and Relativity* (1994) and *Philosophy of Physics: Quantum Theory* (2019)

Maudlin is the clearest philosophical analyst of the foundations of quantum mechanics. He is a realist who takes the quantum measurement problem seriously and argues that every existing interpretation of quantum mechanics faces genuine unsolved problems. The book is not hostile to physics — it is rigorous, technically careful, and written by someone who has engaged seriously with the physics.

The treatment of Bell's theorem — the proof that no local hidden variable theory can reproduce the predictions of quantum mechanics — is the best I have read. Bell's result is not just an experimental result; it is a fundamental constraint on the metaphysics of physical reality.

For mathematicians who want a more formal treatment: Penrose's *The Emperor's New Mind* and *The Road to Reality* cover the measurement problem, Gödel's theorem, and the philosophy of mathematics with a physicist's perspective.

### 5. Thomas Kuhn — *The Structure of Scientific Revolutions* (1962)

The most widely read philosophy of science text of the 20th century, and also one of the most misread. Kuhn introduced the concept of the **paradigm** — the shared framework of assumptions, methods, and exemplary problems that define normal science — and argued that scientific revolutions are not simply the accumulation of new evidence but shifts in paradigm that are partly non-rational.

The misreading: "paradigm shift" is now used loosely to mean any significant change in thinking. The actual argument is more specific and more interesting: during a scientific revolution, the competing paradigms are **incommensurable** — they cannot be compared on a neutral scale, because the very criteria for what counts as a problem and what counts as a solution differ between paradigms. The decision to adopt a new paradigm involves judgment that cannot be reduced to evidence.

This is controversial and has been criticized by Lakatos, Feyerabend, and others, but it is an essential reference point for anyone thinking about what scientific progress is.

---

## The Questions I Find Myself Thinking About

I want to end with something more personal: the specific philosophical questions that arise directly from my own technical work and that I find genuinely unresolved.

**What is a gauge symmetry?** In the Yang-Mills theory and its Stueckelberg extension, the gauge symmetry is a redundancy in the description — different mathematical configurations correspond to the same physical state. The BRST operator acts on this redundancy; the physical observables are the cohomology classes. But if gauge symmetry is pure redundancy — a mathematical artefact of the description rather than a feature of physical reality — then the geometry of principal bundles, which I find so illuminating, is not describing something real. It is scaffolding we use to construct the theory and then discard. I find this uncomfortable. I think the fibre bundle structure is telling us something about the world, not just providing a convenient formalism. But I do not have a sharp account of what it is telling us.

**Does the Wigner observation apply to topology?** The mathematics I use in the QGET framework — persistent homology, fibre bundles, characteristic classes — was developed without physical applications in mind. If QGET turns out to be on the right track, it will be another instance of Wigner's phenomenon: pure topology describing the structure of physical spacetime. I find this either very encouraging or very suspicious, and I cannot fully decide which.

**What is the relationship between physical and mathematical existence?** The Hilbert space of quantum mechanics is infinite-dimensional. The path integral is over a space of field configurations that is not a well-defined mathematical object in the rigorous sense. The renormalisation group involves taking limits in spaces of theories. These are not approximations or conveniences — they are the fundamental objects of the theory. Whether they are genuinely mathematical objects or useful computational fictions is a philosophical question I cannot resolve by doing more physics.

**What does emergence mean, exactly?** The mass gap problem — why the quantum Yang-Mills theory has a positive mass gap when the classical theory has no mass scale — is a problem about emergence. Massless gluons in the classical theory; massive hadrons in the quantum theory. The mass emerges from the quantum dynamics. But "emergence" here means something specific: a property of the quantum theory that has no counterpart in the classical theory. Making this precise requires thinking carefully about what it means for one level of description to generate properties that cannot be explained by the underlying level — which is the central problem of the philosophy of complex systems and of the philosophy of science more broadly.

These are not questions I am going to resolve on this page or in the near future. But I think they are worth holding as open questions. The instinct of most physicists and mathematicians is to set philosophical questions aside and get on with the technical work. That instinct is often right. But sometimes the philosophical question is the technical question, and not recognising it as such costs you years of working in the wrong direction.

---

## A Curated Reading List

**On the philosophy of physics and quantum foundations:**
- Wigner, "The Unreasonable Effectiveness of Mathematics" (1960) — free online
- Maudlin, *Philosophy of Physics: Quantum Theory* (2019)
- Bell, *Speakable and Unspeakable in Quantum Mechanics* (1987) — the original papers on non-locality
- Penrose, *The Emperor's New Mind* (1989) — consciousness, Gödel, and quantum mechanics
- Albert, *Quantum Mechanics and Experience* (1992) — clear, honest, philosophically rigorous

**On the philosophy of mathematics:**
- Poincaré, *Science and Hypothesis* (1902)
- Hardy, *A Mathematician's Apology* (1940)
- Lakatos, *Proofs and Refutations* (1976) — how mathematical knowledge actually grows
- Shapiro, *Thinking About Mathematics* (2000) — accessible survey of all major positions

**On the philosophy of science:**
- Quine, "Two Dogmas of Empiricism" (1951) — free online
- Kuhn, *The Structure of Scientific Revolutions* (1962)
- Hempel, *Aspects of Scientific Explanation* (1965) — the classic statement of the covering-law model
- Bas van Fraassen, *The Scientific Image* (1980) — the best defence of anti-realism

**On the intersection of all three:**
- Penrose, *The Road to Reality* (2004)
- Putnam, *Mathematics, Matter and Method* (1975) — collected philosophical papers
- Maddy, *Second Philosophy* (2007) — a naturalistic account of mathematics and science
- Atiyah et al., *The Changing Shape of Geometry* (2003) — mathematicians reflecting on the nature of their subject

---

*Last updated March 2026.*