---
title: "Physics of Market Regimes and Microstructure"
date: 2026-04-13
tags: ["Research", "Quantitative Finance", "Econophysics", "Physics", "Statistical Mechanics", "Topological Data Analysis", "Research Log"]
description: "The origin and motivation behind my comprehensive review of physics applied to financial markets — what drew me to econophysics, what the paper covers, and what writing it taught me about the relationship between theoretical physics and quantitative finance."
---

I have been working at the intersection of physics and quantitative finance for long enough now that the connection feels obvious to me. Physics provides the language — phase transitions, scaling laws, entropy, topology, geodesics — and financial markets provide the data. The question of whether these two things have anything real to say to each other is, to me, already settled. The more interesting question is how deep the connection goes.

The review paper — *Physics of Market Regimes and Microstructure: Formalisms, Empirics, and Quantitative Applications* — is my attempt to map that connection in one place. It is out now, and this post is about why I wrote it and what I found.

---

## How This Started

The honest version is that I wrote this paper because I needed it.

When I started the topological finance project — applying persistent homology to equity correlation networks to build the TFI — I was reading across a very large literature simultaneously. Random matrix theory for cleaning the correlation matrix. Hidden Markov models for regime detection. Hawkes processes for understanding order flow. Log-periodic power laws for crisis prediction. Each of these came from a different corner of the econophysics literature and each assumed background that the others did not provide.

There was no single paper I could point to that gave the full picture. The closest things were Mantegna and Stanley's *Introduction to Econophysics* from 1999 — foundational but obviously predating twenty years of subsequent work — and Bouchaud and Potters' *Theory of Financial Risk* — rigorous and excellent but focused primarily on the statistical physics of returns rather than the full breadth of microstructure and regime detection.

So I started taking notes. Over several months, as I was reading for the TFI project, the notes grew into something that was worth organising. The review is what those notes became.

---

## What the Paper Actually Covers

The paper spans thirteen sections and approximately one hundred references. Rather than summarising it section by section — the abstract does that — I want to talk about the threads that connect it.

**The stylized facts are the empirical foundation.** Fat tails, volatility clustering, the leverage effect, correlation breakdown in crises. These are the things any model of financial markets has to reproduce. The power-law tail exponent of approximately 3 showing up across asset classes and time periods — first documented by Mantegna and Stanley in the S&P 500 in 1995 and confirmed in dozens of markets since — is the kind of universality that immediately signals to a physicist that something interesting is going on. When the same exponent appears in systems with completely different microscopic details, there is usually a deeper structure at work.

**Random matrix theory is the most immediately practical result.** The Marchenko-Pastur distribution tells you which eigenvalues of your correlation matrix are genuine signal and which are noise. In a universe where you are estimating the covariance of 500 stocks from daily returns over two years, the signal-to-noise problem is severe — Laloux et al. showed in 1999 that the vast majority of eigenvalues in a typical empirical correlation matrix are consistent with the random bulk, carrying no useful information. Denoising the matrix before plugging it into a portfolio optimiser is not optional if you want the optimisation to mean anything. This is a result from nuclear physics — Wigner's work on random matrices in the 1950s — applied to finance, and it works.

**The Hawkes process section taught me the most.** I knew Hawkes processes in broad terms before writing this — self-exciting point processes, used for high-frequency order flow modelling — but working through the branching ratio result carefully was the part of the review where I felt I genuinely understood something I had not before. Jaisson and Rosenbaum proved that a Hawkes process near the critical branching ratio — where the endogenous fraction of activity approaches 1 — converges to a Heston-type stochastic volatility model at the macro scale. This is a microscopic derivation of rough volatility from order-flow endogeneity. The fact that Filimonov and Sornette measured this branching ratio in S&P 500 E-mini futures and found it increased from roughly 30% before 2000 to roughly 70% after 2008 is the most striking empirical finding in the paper, I think. Markets became more endogenous — more self-exciting, less driven by external information — as electronic trading scaled up. The implication for systemic risk is obvious and unsettling.

**The TDA section is where my own research sits.** The treatment of persistent homology in this paper is the formal mathematical background for the TFI project. Gidea and Katz's finding that first Betti numbers — the count of independent 1-cycles in the correlation network — increase dramatically in the months preceding major crashes is exactly the mechanism the TFI is trying to quantify at the cross-sectional level. Writing this section made the theoretical basis for TFI significantly clearer to me than it was when I started the project.

**The ABE framework was new to me entirely.** Briet's Acceleration Balance Equation — a third-order nonlinear ODE for economic dynamics, interpreted as geodesic motion on a Riemannian manifold defined by a T-metric — is the most unusual result in the paper. It takes the Lagrangian/Hamiltonian formalism seriously as a model of macroeconomic dynamics, not just as a mathematical analogy. The T-metric endows the space of economic trajectories with a genuine Riemannian structure, and the natural dynamics of the system are geodesics in that structure. I find this genuinely interesting — the same geometric machinery that appears in general relativity, applied to economic forecasting. Whether it works as well as Briet claims empirically is a separate question, but the framework is coherent and the physics is sound.

---

## What Writing This Taught Me

Three things, which I want to record honestly.

**The transfer from physics to finance is one layer deep.** I wrote about this in the [inspiration from art and science](/art-music/inspiration-from-art-science/) page on this site. The mathematical structures — random matrices, point processes, persistent homology, Riemannian geometry — transfer correctly from physics to finance. The physical intuitions — specific parameter values, equilibrium assumptions, thermodynamic limits — often do not. The Hawkes process near the critical regime is a real financial phenomenon. The analogy between market crashes and second-order phase transitions is illuminating. But markets are not gases and economic agents are not particles, and pushing the analogy past the mathematical structure tends to produce either trivial restatements or false predictions. The review is careful about this distinction. The paper I most wanted to write was one that was honest about where the transfer works and where it becomes metaphor.

**The most useful tools for practitioners are the least glamorous.** The ABE framework and the quantum finance section are intellectually interesting. RMT denoising, HMM regime detection, and Hawkes process endogeneity monitoring are what actually changes portfolio construction. The hierarchy in Section 12.3 of the paper — start with RMT, add HMMs, use Hawkes branching ratio for risk monitoring, apply TDA as a complementary crash signal — is the honest answer to a practitioner asking where to spend their time. Glamour and utility are not correlated in this literature.

**Writing a review paper forces you to find the holes.** I went into this project with a reasonably confident mental picture of the field. By the end I had a clearer picture with more explicit gaps. The open problems in Section 12.2 are not decorative — they are the places where I genuinely do not know the answer and found that the literature does not either. The consistent multi-scale modelling problem — how to derive macroscopic regime dynamics from microscopic Hawkes order flow — is the one I keep thinking about in the context of the TFI work. If the TFI measures topological complexity in the correlation network, and the correlation network emerges from the aggregate behaviour of order flows that can themselves be modelled as Hawkes processes, then there is a chain connecting microstructure to topology that nobody has traced cleanly. That is a research direction.

---

## Where This Sits Relative to the Other Work

The review paper is not a research paper in the usual sense. It does not prove a new theorem or establish a new empirical finding. What it does is assemble the current state of a field that is spread across physics, mathematics, and finance journals in a way that nobody who approaches from any one of those disciplines would naturally encounter in full.

For me specifically, writing it was the right thing to do at this stage of the TFI project — I needed to understand the landscape before I could be confident about where the topological finance work sits within it. Now I have that picture.

The paper is available on my [quantitative finance research page](/quantitative-finance/research-in-market-microstructure/) alongside the TFI project notes.

The TFI itself is still a few months from a publishable state. The robustness testing is ongoing. But the theoretical foundation is now documented in a form that others can read and engage with, which was the point.

---

*The full paper is linked from the [quantitative finance section](/quantitative-finance/research-in-market-microstructure/) of this site.*
