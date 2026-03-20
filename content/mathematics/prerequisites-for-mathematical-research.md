---
title: "Prerequisites for Mathematical Research"
date: 2026-02-06
parent: "Mathematics"
---

There are many guides to mathematical research. Most of them are written by people who have seemingly forgotten what it felt like to not know how to do it.

This is not that guide.

What follows is honest. It is about what research actually looks like from the inside — the confusion, the wrong turns, the months where nothing moves. It covers both applied and pure mathematics, because they are genuinely different activities. And it does not pretend that there is a recipe.

There is not a recipe.

---

## What Research Is Not

Before anything else, I want to clear away the most persistent misconception about mathematical research: that it is olympiad problem-solving, but harder.

It is not. They are different activities with different cognitive signatures, and the skills transfer less than you expect.

In olympiad mathematics, a problem exists. Someone has written it. It has a solution. The solution is findable within hours. The entire enterprise is optimised for a clean resolution within a bounded time window.

Research mathematics has none of these properties. The problem may not be precisely stated. It may not have a solution. If it does have a solution, you may not be the right person to find it at this moment, or the tools may not yet exist. The timescale is months or years, not hours. And unlike an olympiad problem, research does not reliably give you the psychological reward of a clean answer.

I wrote about this distinction at more length [here](/omarora/blog/diffinresearchandolympiadmath/). The short version is that olympiad mathematics trains you to be extremely good at closing. Research mathematics requires you to become comfortable with a particular kind of open — the open that might stay open for years.

---

## The Real Prerequisites

### Mathematical Maturity

Every guide says this. Few explain it. Mathematical maturity means three things in practice.

First: you can read a proof and follow every step, including the steps that are left implicit. You can tell the difference between "this step is obvious" and "this step is being smuggled past you." This takes time to develop. You develop it by reading slowly, by writing things down, and by being honest when you have not actually understood something.

Second: you have a working vocabulary across at least two or three areas of mathematics — not deep expertise, but enough that when you encounter a concept from another field, you can place it. Research almost always involves importing ideas from somewhere you did not expect them.

Third: you have some tolerance for confusion. Not comfort with confusion — nobody is comfortable with it — but tolerance. The ability to sit with a problem that is not moving without immediately concluding that you are stupid or that the problem is unsolvable. This is learned, not innate.

### Technical Prerequisites by Area

The prerequisite landscape looks different depending on what kind of research you intend to do. The following is not exhaustive, but it is honest.

**For any serious mathematical research:**
- Proof-writing fluency. Not familiarity. Fluency.
- Linear algebra at the abstract level. Not matrices. Linear maps.
- Real analysis — ε–δ proofs, convergence, continuity — because almost everything eventually touches analysis.
- Some group theory and ring theory. The structures appear everywhere.

**For applied mathematics (analysis, PDE, numerical methods, combinatorics, data):**
- Real and functional analysis, properly.
- Probability and measure theory — mandatory for any work touching randomness, statistics, or stochastic processes.
- Linear algebra at the highest level of fluency you can achieve. It is the substrate.
- Computation. The ability to implement ideas, run experiments, generate examples. This is not optional in modern applied work.
- Domain knowledge. Applied mathematics always has a domain — physics, finance, biology, computer science. You need to understand the domain at a level beyond surface familiarity.

**For pure mathematics (algebra, topology, number theory, geometry):**
- The foundations of whatever area you are entering. These are deep and non-negotiable. You cannot research algebraic number theory without knowing algebraic number theory.
- Category theory — not as a prerequisite to start, but as something you will need before long. It is the language that unifies everything else.
- A significant amount of patience. Pure mathematics is where the gap between "understanding a subject" and "being able to do research in it" is widest.

**For mathematical physics:**
- Everything in the pure list plus differential geometry and topology, done seriously.
- Some exposure to quantum field theory, even at a heuristic level, before you engage with the literature.
- The ability to translate between mathematical precision and physical intuition — and to know which mode you are in at any given moment.

---

## How Research Actually Happens

Professor Pavel Etingof at MIT, in his advice for the PRIMES program, writes: *"Be stubborn and at the same time flexible. In mathematical research, unlike olympiads, solving a problem takes weeks and months rather than hours, and there is no instant gratification."*

That is the cleanest statement of the core difficulty I have seen.

But what he does not describe — what no one describes in the official advice — is what the day-to-day texture of research actually feels like. Lee Lady, a mathematician at the University of Hawaii, wrote something more honest. He described his own process as mostly desperation: no idea where to go, reading other people's mathematics in the hopes that something would connect, and occasionally stumbling on a connection that nobody else had noticed.

That is much closer to the truth.

Research does not usually look like "I had a clear question, I thought hard, I found the answer." It looks like: wandering in several directions simultaneously, accumulating knowledge that does not yet have an obvious use, noticing an unexpected analogy with something you learned six months ago for unrelated reasons, and then spending weeks trying to determine whether the analogy is genuinely structural or merely superficial.

Ideas grow out of other ideas. They almost never arrive from nowhere.

### Finding a Problem

This is the hardest part, and the part that no guide tells you how to do. It cannot be taught directly. It develops from exposure.

The practical mechanisms are:

**Reading recent papers.** Not to understand every detail — you will not, at first — but to develop a sense of what questions are open and which ones seem tractable. The ends of papers are particularly useful. Researchers typically list open problems explicitly.

**Talking to people.** Etingof is right that mathematics is a social activity. The conversation that clarifies what you do not yet understand is often the same conversation that generates the question worth pursuing.

**Computing examples.** Before you can ask a good question, you need to know what the phenomenon looks like. The [OEIS](https://oeis.org/) is invaluable for discrete mathematics — you can compute a sequence and look it up. For open problems more broadly, [erdosproblems.com](https://erdosproblems.com) is an extraordinary resource. Paul Erdős spent his career proposing problems and attaching cash prizes to many of them. The site catalogues hundreds of open problems across combinatorics, number theory, and graph theory, ordered by difficulty and prize amount. Many are genuinely accessible to someone who is not yet a professional mathematician. Browsing it for an hour will do more for your sense of what mathematical research looks like than reading any advice document.

**Reading broadly, not just deeply.** Lee  made this point repeatedly in his account of his own work. His most significant results often came from importing an idea from an area that most people in his specialty had never looked at. This is not unusual — it may be the most common mechanism by which new mathematics gets made.

### Doing the Work

Once you have a problem — or the beginning of one — the process looks roughly like this:

Understand the simplest possible case. Not a simple case. The simplest. Etingof calls this Gelfand's principle: look for the simplest example that captures the phenomenon. If you cannot understand the simplest case, you cannot understand the general case. The general case comes later.

Compute. Run experiments. Generate data. Look for patterns. The pattern is often the theorem, and the theorem is often the pattern with a proof attached.

Make conjectures and try to break them. The most efficient way to make progress is often to conjecture something optimistic and then spend time trying to find a counterexample. If you find one, you have learned something. If you cannot find one after serious effort, you probably have a theorem and you probably have some intuition about why it is true.

Write things down. This is not record-keeping — writing is thinking.

The moment you try to write a proof and find yourself stuck, you have located the exact point where your understanding breaks. That is not failure; that is progress in its most precise form.

Etingof recommends maintaining notes in LaTeX at all times, and this is genuinely valuable advice. Structuring your thoughts formally forces clarity — it exposes what you truly understand and what you are merely assuming.

If you are setting up your workflow, you can refer to [LaTeX FAQs By Evan](https://web.evanchen.cc/faq-latex.html) for a starting point.

Also, a practical note: avoid relying entirely on Overleaf for everything. It is excellent for collaboration, but for serious, long-term work, a local setup is far more effective. There are also alternatives like TeXWolf worth exploring.

The goal is simple — create an environment where writing becomes natural, because that is where real thinking begins.

Expect dead ends. Most of what you try will not work. This is not failure — it is the process. Lee described spending months on an approach that turned out to be completely wrong, and then finding that the wrong approach had taught him something that made the right approach possible. The dead ends are not wasted time. They are part of the work.

---

## Applied Research vs. Pure Research

I want to be honest about this distinction, because it is real and people do not usually say so clearly.

Applied mathematics is, in my experience, more tractable as a starting point. There is usually a phenomenon to study. The phenomenon gives you structure. You can compute. You can run experiments. You can get feedback from data. When you are stuck, the data can tell you that you are stuck and sometimes suggest a direction. The path from "I have an idea" to "I have something publishable" is generally shorter.

I say this from experience. My published work is in applied mathematical physics — an extension of Yang–Mills theory with a confinement mechanism, and a framework for quantum geometric entanglement. These are problems where the physics provides constraints, where computation is possible, and where the gap between a good idea and a written paper is measured in months, not years. That pipeline is something I understand.

Pure mathematics is different. The reward structure is longer. The distance between having an idea and knowing whether the idea is correct is greater. There is no data to check against — only proof, which must be airtight. The problems that are genuinely open tend to be open because they are hard in a particular way: not computationally intensive, but structurally resistant. And the gap between "I understand this subject well" and "I can contribute to this subject" is substantially larger in pure mathematics than in applied mathematics.

I have been working on an idea in pure mathematics for some time now. I am not going to describe it here, partly because I do not know yet whether it leads anywhere, and partly because the ideas are in an early enough state that describing them would misrepresent them. What I can say is that I have not yet reached anything publishable. I have accumulated a great deal of understanding of why certain approaches do not work, which is itself a form of progress — but it is slow, and it does not feel like progress most of the time.

This is the honest experience of pure mathematical research. I find it more elegant than applied work. The questions it asks are more fundamental. The answers, when they come, are cleaner. But the process is harder to sustain, and the feedback loops are longer.

If you are starting out, I would not tell you to avoid pure mathematics. I would tell you to understand what you are signing up for.

---

## Resources

### For Getting Started

**How to Prove It** — Daniel Velleman. Read this before anything else. You need to be able to write a proof before you can write a paper.

**The Art of Problem Solving** community and resources — for building mathematical problem-solving instinct. Useful as a foundation, not as a destination.

**Paul's Mathematical Research Advice** (Lee Lady, University of Hawaii): [math.hawaii.edu/~lee/how-to.html](https://math.hawaii.edu/~lee/how-to.html). One of the most honest accounts of what mathematical research actually feels like that I have encountered. Long, discursive, and essential reading.

**PRIMES: How to Succeed in Mathematical Research** (Pavel Etingof, MIT): [math.mit.edu/research/highschool/primes/succeed.html](https://math.mit.edu/research/highschool/primes/succeed.html). Fifteen concrete, useful pieces of advice. Read it. Follow the parts about examples and note-taking especially.

**r/math discussion on how mathematicians do research**: [the thread](https://www.reddit.com/r/math/comments/ttjl2p/how_do_mathematicians_do_research/). The comments from working mathematicians are more useful than most formal advice. The consensus: it is mostly reading, talking, and being confused for long periods. There is no shortcut.

### For Finding Problems

**Erdős Problems** — [erdosproblems.com](https://erdosproblems.com). Paul Erdős proposed problems throughout his career, often with cash prizes. This site catalogues them cleanly by area, difficulty, and prize amount. An extraordinary resource for anyone looking for an entry point into research-level combinatorics or number theory. Browse it seriously. Some of the problems are genuinely accessible.

**The OEIS** — [oeis.org](https://oeis.org). Compute a sequence, look it up, find the connections. Invaluable for discrete mathematics and number theory.

**MathOverflow** — [mathoverflow.net](https://mathoverflow.net). Questions and answers from professional mathematicians. Useful for understanding the current state of a field and identifying open problems. Do not post a question before you have read the site's standards carefully.

**arXiv** — [arxiv.org/archive/math](https://arxiv.org/archive/math). The preprint server where essentially all new mathematics appears first. Reading preprints in your area regularly is non-optional if you want to do research.

### For Applied Mathematical Research Specifically

**Mathematics of Data Science** — MIT OpenCourseWare covers this. If you intend to work in applied statistics, ML theory, or quantitative finance, this is the mathematical infrastructure.

**Stochastic Calculus for Finance** — Shreve (two volumes). The mathematical foundation for any quantitative finance research.

**Numerical Methods** — Trefethen and Bau, *Numerical Linear Algebra*. The standard reference for computational linear algebra.

### For Pure Mathematical Research

**Evan Chen's Napkin** — [venhance.github.io/napkin](https://venhance.github.io/napkin/Napkin.pdf). The best broad overview of higher mathematics available. Use it as a map before diving into any particular territory.

**The Princeton Companion to Mathematics** — Gowers (editor). An encyclopaedia of modern mathematics, written by the people who do it. The survey articles on individual areas are among the best overviews available anywhere. Read the article on your area before you dive into the primary literature.

**arXiv** and the primary literature. There is no substitute. You must read papers in the area you want to work in, even before you can understand them fully.

---

## A Note on Mentors

Every piece of advice about mathematical research eventually says: find a mentor. This is correct. But it is not always actionable, and most guides do not say what a mentor actually does.

A good mentor does not give you problems and then leave you alone. A good mentor — as Etingof describes and as Lee's account of working with Fred Richman illustrates — asks questions. When you have made no progress, a good mentor asks you what you tried and why it did not work. Those questions force you to articulate your thinking, and articulating your thinking is often how you discover what you missed.

If you do not have access to a formal research mentor (just as me in the pure math work), the substitutes are: MathOverflow (for specific technical questions), the arXiv (for understanding what people are working on), and —  speaking from experience — email. Mathematicians are more willing than most professionals to correspond with students who have read their work carefully and ask specific, well-formed questions. Cold emailing with a vague "I am interested in your research" goes nowhere. Cold emailing with "I read your 2021 paper on X, and I have a question about the proof of Lemma 3.2" often gets a response.

---

## The Honest Summary

Mathematical research is mostly reading, computing examples, being stuck, talking to people, and occasionally noticing something that nobody else has noticed. The noticing happens faster if you have read more and talked to more people. There is no shortcut to the reading and talking.

Applied mathematics is more forgiving as a starting point because the phenomenon tells you where you are. Pure mathematics is more demanding and, in my view, more beautiful — but the process is longer and the feedback is sparser.

I am better, so far, at applied research. The pure work is slower and harder, and I have not yet produced something worth publishing in it. I am comfortable with that. The work continues regardless.

The standard advice — be stubborn, be flexible, take good notes, seek examples, talk to people — is correct. It is just not complete. The part they leave out is that for most of it, you will not know whether you are making progress. You learn to work anyway.

That is the prerequisite that no one lists.

---

*Last updated March 2026.*