---
title: "Research Log — March 2026"
date: 2026-03-26
tags: ["Research", "Yang-Mills", "QGET", "Defence", "Topological Finance", "Research Log"]
description: "What happened in March 2026 — the Stueckelberg preprint released and submitted for publication, and where things stand with QGET, the defence middleware project, and the topological finance work."
---

March was a month where something that had been building for a long time finally crossed the line from work-in-progress to something that exists in the world.

---

## The Stueckelberg Paper

The main event of this month was releasing the preprint for *A Gauge-Invariant Stueckelberg Extension of Yang–Mills Theory* and submitting it for publication.

The paper has been in some form of progress for longer than I would like to admit. The core idea — that you can generate mass in a non-Abelian gauge theory through a Stueckelberg mechanism without touching the Higgs — was clear relatively early. What took time was making the argument complete enough to put it in front of other people.

The final paper does three things. It constructs the full BRST cohomology of the extended action. It derives the Feynman rules, including the non-polynomial interaction vertices that the Stueckelberg scalar introduces. And it computes the one-loop beta function to verify that asymptotic freedom is not destroyed by the mass term — which was the result I was most uncertain about before working through the calculation.

The preprint is on Zenodo ([here](https://doi.org/10.5281/zenodo.19057338)).

Releasing it felt like a particular kind of moment — not triumphant, exactly, but clarifying. The work stops being internal when you release it. Someone else can now read it, disagree with it, find an error, or build on it. That transition matters.

I wrote two posts earlier this month about the Yang–Mills mass gap specifically — [what the problem actually asks](https://omarora.in/blog/whatismassgapproblem/) and [why I am interested in it](https://omarora.in/blog/whyyangmills/) — if the background is useful.

---

## QGET

The Quantum Geometric Entanglement Theory work is in a different and more frustrating phase.

The framework is coherent — the claim that spacetime geometry emerges from the entanglement structure of fundamental quantum degrees of freedom has internal logic to it, and the connection to the Ryu-Takayanagi formula gives it a foothold in established results. But a framework being coherent is not the same as it being useful. The question I keep returning to is: what does this model actually predict, concretely, that current approaches do not?

That is what I am working on now. Deriving the specific observational and theoretical consequences of the model — the places where QGET either makes a different prediction than standard approaches or provides a mechanism where other approaches only assert an outcome.

The honest answer is that this is taking longer than I expected, and I am not going to pretend otherwise. The direction looks promising — there are a few consequences that, if I can make them precise enough, would be interesting. But "interesting" and "publishable" are different standards, and I am not at the second one yet. A few more months, at minimum, before there is anything tangible enough to put in a paper.

---

## Defence Protocol Translation Middleware

The defence project is in a more satisfying state than the QGET work, in the sense that there is always something concrete to do.

The architecture is fixed — the five-component structure with the Common Internal Representation at the centre, the MIL-STD-1553B and STANAG 4586 adapters, the Translation Engine, and the Audit Logger. The gap analysis is done: 49 field-level incompatibilities across six dimensions, classified by the six-category taxonomy.

What remains is completing the software implementation and writing the manuscript around it, which should not take much time. The implementation is in Python using asyncio for bus emulation and real UDP sockets for the STANAG transport layer. The Translation Engine latency is already sub-millisecond in simulation. The plan for next week is finishing the implementation to the point where it is clean enough to be described in a paper, and then writing that paper.

The manuscript is taking shape in parallel. The three-contribution structure is clear — gap analysis, architecture, simulation validation — and the writing is going reasonably well. This one feels like it is moving toward a definite endpoint, even if the exact timeline depends on how the implementation goes.

---

## Topological Finance

The topological finance project — the Topological Fragmentation Index — is in a good place relative to where it was two months ago.

The signal construction is solid. The Vietoris-Rips filtration on rolling correlation distance matrices, extracting total H₁ persistence as the TFI, and computing individual stock sensitivities to TFI changes — that pipeline is working. The Fama-MacBeth validation framework is in place. The combinatorial purged cross-validation is running correctly.

What I am doing now is stress-testing the results — checking that the signal holds across different rolling window lengths, different filtration parameters, different rebalancing frequencies. You can always find a signal if you try enough combinations. The question is whether the signal is robust to parameter choices that were not chosen post-hoc to maximise it. That robustness testing is the current focus.

If it holds up — and the early indications are that it does — the paper is probably a few months away. Not an enormous amount of work remains on the research side. The writing will take time.

---

## A Note on Pacing

One thing March clarified for me is how differently the four active projects feel to work on.

The Stueckelberg work felt like it had a natural resolution — there was a point where the argument was complete, and crossing that point was identifiable. You could tell when you were done.

The QGET work does not have that quality yet. The argument is not yet complete enough that I know what completion looks like. That is uncomfortable in a specific way.

The defence middleware has a clear remaining task list. Implementation, manuscript. That has its own satisfactions.

The finance work is somewhere in between — the research has direction but the robustness testing is inherently open-ended in the sense that you can always test more things.

Four projects at different stages of resolution, demanding different things from attention and patience. That is the actual texture of this month, honestly described.

The Stueckelberg paper going out was the moment. Everything else is still moving.

---

*Research logs are posted approximately monthly. The next one will cover April.*