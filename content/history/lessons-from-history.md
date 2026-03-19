---
title: "Lessons from History"
date: 2026-02-06
parent: "History"
---


This page depends on the three history pages that precede it. The [history of mathematics and physics](/omarora/history/history-of-mathematics-and-physics/), the [financial history page](/omarora/quantitative-finance/financial-history-and-market-evolution/), and the [schools of philosophy page](/omarora/philosophy/schools-of-thought-in-philosophy/) each traces a specific domain in detail. This page asks: when you look across all three, what patterns are consistent enough, and important enough, to be worth naming?

The standard version of this exercise produces aphorisms. "Those who do not learn from history are doomed to repeat it." "Great minds think alike." "Genius is one percent inspiration, ninety-nine percent perspiration." These are not lessons — they are the verbal gestures that signal the appearance of having thought about something without actually doing so.

The lessons worth extracting from intellectual history are not aphorisms. They are observations about recurring structural patterns — the way new ideas typically arrive, the way communities typically respond, the conditions that enable or prevent progress, and the failure modes that appear in every domain with enough regularity to be predictable. These observations are not certain; they are empirical generalisations over a small and non-random sample of intellectual history. But they are more grounded and more useful than the alternatives, and thinking clearly about them has changed how I approach my own work.

I will give seven. Each is drawn from specific historical episodes documented in the other pages on this site, and each has direct implications for how I think about the research I am doing now.

---

## Lesson I — Mathematics Precedes Its Applications by Decades

The most consistent pattern in the history of mathematical physics is that the mathematics required for a physical theory is developed for purely internal mathematical reasons, with no physical application in view, and then sits waiting — sometimes for decades, sometimes for centuries — until a physicist needs it.

The instances are not occasional curiosities. They form a pattern that is dense enough to be a reliable guide.

Riemann developed the geometry of $n$-dimensional curved manifolds in 1854 as an answer to the internal mathematical question of what geometry is in its most general form. He was not thinking about gravity. The geometry sat essentially unused for fifty years. In 1915, Einstein needed precisely that geometry — the Riemannian metric, the curvature tensor, the geodesic equation — to formulate general relativity. He did not know the mathematics existed; Marcel Grossmann had to introduce him to it.

Lie developed the theory of continuous symmetry groups in the 1870s and 1880s to classify the symmetries of differential equations. Cartan completed the classification of simple Lie algebras in 1894. The list — $A_n, B_n, C_n, D_n$ and the five exceptional cases — was complete and exact. When quantum mechanics was formulated in the 1920s, the symmetry groups of the known physical forces turned out to be drawn from Cartan's finite list. The representation theory of the Poincaré group classifies all elementary particles. The mathematicians did not know they were doing physics.

Ehresmann developed the theory of principal fibre bundles and connections in the 1940s and 1950s — the abstract generalisation of Riemannian geometry to arbitrary structure groups. When Yang and Mills wrote down their non-Abelian gauge theory in 1954, they were, without knowing it, writing down the physics of a connection on a principal $SU(2)$ bundle. The Wu-Yang dictionary of 1975 made the correspondence explicit: gauge potential = connection, field strength = curvature, gauge transformation = bundle automorphism.

Persistent homology — developed as pure algebraic topology in the 1990s and early 2000s — captures the multi-scale topological structure of data. Applied to financial correlation matrices, it appears to contain information about future market regimes. The topologists who developed it were thinking about data analysis and pure topology. They were not thinking about equity returns.

**What this means operationally.** When you encounter a hard problem — a physical phenomenon that resists existing frameworks, a data structure that standard statistics cannot capture — the right first question is not "what new mathematics can I invent?" but "what existing mathematics, developed for internal reasons, describes this structure?" The answer is often already there. The difficulty is knowing where to look, which is an argument for mathematical breadth over mathematical depth as the primary research strategy in early-stage theoretical work.

It is also an argument for taking pure mathematics seriously on its own terms. The value of a mathematical structure is not measurable by its current applications. Riemann's geometry looked useless for fifty years. It was not useless; it was waiting.

---

## Lesson II — New Ideas Are Almost Always Resisted, and Resistance Is Not Evidence of Wrongness

This lesson is easy to misstate. The correct version is not "consensus is always wrong" or "contrarians are always right." It is: when a genuinely new idea enters an established field, the initial response is almost always resistance, and the resistance is usually not driven by careful evaluation of the evidence but by the social and cognitive cost of paradigm change.

The historical record is consistent. When Yang and Mills presented their non-Abelian gauge theory at Princeton in 1954, Pauli interrupted repeatedly to ask about the mass of the gauge bosons. Yang had no answer. Pauli, one of the greatest physicists of the century, was applying the standard of the existing framework (massless Yang-Mills bosons are incompatible with the observed short range of the strong force) to a theory whose full resolution would require the Higgs mechanism, which had not yet been invented. The theory was essentially ignored for a decade.

When Cantor developed set theory and the theory of infinite cardinals in the 1870s and 1880s, he was attacked by Kronecker ("a corrupter of youth") and dismissed by the mathematical establishment. The idea that there are different sizes of infinity — that the real numbers are a strictly larger infinity than the natural numbers — offended deep intuitions about what mathematics was. It is now a foundational result.

When Semmelweis demonstrated in 1847 that handwashing by physicians dramatically reduced childbed fever mortality, the medical establishment rejected the finding. The mechanism was unknown (germ theory had not yet been established) and the implication — that physicians were killing their patients — was too uncomfortable. Semmelweis was committed to a mental institution and died there. The pattern is not unique to medicine.

When Fama documented the equity premium in the early 1970s and Jegadeesh and Titman documented momentum in 1993, both findings were initially dismissed as data mining or artefacts of the sample. Both turned out to be real, robust across geographies and time periods, and subsequently confirmed in hundreds of independent studies.

**What the pattern is not.** Resistance is necessary — not all new ideas are correct, and the burden of proof on a new idea should be high, particularly in fields with short historical records. The problem is not resistance per se but the *form* of resistance: responding to a new idea with social dismissal rather than careful engagement with the evidence. Pauli's interruption of Yang was a legitimate scientific objection (the mass problem was real) poorly delivered (the theory was not given time to develop). Kronecker's attack on Cantor was neither legitimate nor well-delivered.

**The operationally useful version.** A new idea that is resisted is not thereby probably wrong. A new idea should be evaluated on its own evidence and internal consistency, not on whether it fits the existing framework — because fitting the existing framework is precisely what a genuinely new idea cannot do. At the same time, the correct response to resistance is not resentment but better evidence and clearer exposition.

For the TFI research specifically: the claim that the topological structure of correlation networks contains cross-sectional predictive information is a non-standard claim that the existing asset pricing literature has no room for. The appropriate response to scepticism is rigorous out-of-sample testing, not frustration.

---

## Lesson III — The Techniques Always Precede the Foundations, and That Is Fine

In every area of intellectual history, the productive techniques have been developed and used long before their logical foundations were established. This is the normal mode of intellectual progress, not an exception to it.

Newton developed calculus in the 1660s using infinitesimals — quantities that were neither finite nor zero — whose logical status was entirely obscure. Bishop Berkeley attacked the method in 1734, calling infinitesimals "ghosts of departed quantities." He was right that the foundations were unclear. He was wrong to conclude that the technique was invalid. The rigorous foundations — Cauchy's $\epsilon$-$\delta$ definition of limits, Weierstrass's formalisation, Cantor's set theory — came 150 years after the technique was in productive use.

The same pattern appears in every subsequent generation. Dirac introduced the delta function in 1927 — a "function" that is zero everywhere except at a single point and integrates to 1 — without any rigorous mathematical justification. Mathematicians regarded it with suspicion for two decades. Schwartz's theory of distributions, published in 1945, put the delta function on rigorous footing. In the interim, physicists had been using it correctly and productively throughout.

The path integral — Feynman's formulation of quantum mechanics as a sum over all possible paths, weighted by $e^{iS/\hbar}$ — has no rigorous mathematical definition in general. The space of paths is not a well-defined measure space; the integral does not exist as a Lebesgue or Riemann integral. This is a genuine mathematical problem, not a minor technicality. Quantum field theory built on the path integral is the most precisely tested theory in the history of science. The foundations are still being developed.

In finance, Black-Scholes was published in 1973 without a rigorous mathematical foundation for the Itô integral used in its derivation — Itô's lemma was known but the full measure-theoretic framework was not standard in financial economics at the time. The formula was immediately used and consistently produced correct relative prices. The rigorous foundations — Shreve's stochastic calculus textbooks, the martingale theory of arbitrage pricing — came later.

**What this means operationally.** The correct response to the absence of rigorous foundations for a productive technique is not to abandon the technique but to (a) use it carefully, with explicit awareness of its known limitations, and (b) work on the foundations separately, or wait for the foundations to arrive. It is not to pretend the foundational issue does not exist and it is not to refuse to use the technique until it is rigorously established.

In my own work: the renormalisation procedure in quantum field theory is foundationally unclear, and I think about this. The right response is not to stop doing QFT but to understand the limits of the procedure and to be honest about what has and has not been established rigorously.

---

## Lesson IV — Leverage Kills, Every Time, Without Exception

This lesson is specific to finance and is the most consistently demonstrated pattern in the entire history of financial markets. It requires no philosophical qualification. It is simply true.

Every major financial collapse in recorded history involves the same mechanism: an apparently sound strategy, implemented with leverage that is rational given expected conditions, encountering conditions worse than expected. The strategy that was almost certain to work in the long run requires capital that the leverage has consumed before the long run arrives.

The South Sea Company shareholders of 1720 were leveraged. The margin accounts of 1929 were leveraged. Long-Term Capital Management in 1998 was running 25:1 balance sheet leverage on convergence trades whose fundamental soundness was never in question — the trades that had been loss-making at the time of the bailout eventually converged. The leverage made the short-run adverse move fatal. The 2008 financial crisis was, at its core, a leverage crisis: mortgage assets held at high multiples of equity, funded by short-term liabilities, encountering a price decline that turned insolvency from theoretical to actual.

The mechanism is always the same and it is mathematically precise. The Kelly criterion says: the optimal bet size — the size that maximises the long-run growth rate of capital — is $f^* = \mathbb{E}[R] / \sigma^2$ for approximately normal returns. The Kelly fraction decreases as volatility increases and increases as edge increases. Full Kelly is theoretically optimal and practically dangerous, because the estimation error in the edge parameter turns full Kelly into a strategy with significant ruin probability. Fractional Kelly at 25–50% of the full Kelly fraction is the empirically grounded approach.

The LTCM partners were mathematically sophisticated people who understood the Kelly criterion. They leveraged beyond it anyway. The reason was institutional: leverage was available, the expected return on equity was dramatically higher with leverage, and the fund was under pressure to generate returns competitive with other leveraged strategies. The rational individual decision was consistent with catastrophic collective outcome — the classic structure of a financial crisis.

**The deepest version of this lesson.** Leverage does not change the expected value of a strategy; it scales the expected return and the variance by the same multiple. It does not improve a bad strategy. It magnifies whatever the strategy is. A strategy that is right 55% of the time, with full Kelly, will eventually approach certainty of ruin because of the sizing errors in the 45% of cases that go against it. Correct strategies, incorrectly sized, fail. This is not a lesson about risk aversion — it is a lesson about the mathematics of geometric returns.

For my own work: every strategy I build will be sized at fractional Kelly. The question "at what leverage does this strategy survive a 3-sigma adverse move?" is asked before the question "what is the expected Sharpe ratio?"

---

## Lesson V — The Signal Decays After Publication

In systematic finance, this is one of the most empirically well-established phenomena in the literature, and it has direct implications for research strategy.

McLean and Pontiff (2016) studied 97 return predictors from the academic literature and found that the average return associated with the predictor was approximately 26% lower in the five years after publication than in the pre-publication period. The decay is real, consistent, and statistically significant. The mechanism is obvious: once a predictor is published, investors trade on it. The trading eliminates some or all of the mispricing. The premium decays.

The value premium — documented by Basu in 1977, formalised by Fama and French in 1992 — was very strong from 1926 to 2007 and has been substantially weaker since. Whether the decay is entirely due to crowding or partly to structural changes in the economy (the rise of intangible assets and platform businesses, whose value is systematically understated by book value) is contested. Both mechanisms are plausible.

The momentum premium has been more resilient — possibly because its mechanism involves under-reaction to news, and the institutional structure of markets does not quickly eliminate under-reaction. But it has also experienced extreme drawdowns in 2009 and 2020 that were partly crowding-driven.

**The structural reason the decay is not complete.** If factors always decayed to zero after publication, the equilibrium would be an efficient market with no systematic premia. This is not what we observe. The reason is that arbitrage capacity is limited: some strategies require leverage that is costly, some require short positions that are difficult to establish, and some require tolerance for large drawdowns that institutional managers cannot provide without triggering redemptions. These limits to arbitrage are the fundamental reason some premia persist.

**What this means for novel signals.** A signal derived from a non-standard methodology — like persistent homology applied to correlation matrices — has a different exposure to publication decay than a factor based on standard price or accounting variables. It requires significant computational infrastructure to compute. The relevant community of potential arbitrageurs is smaller. The decay, if it occurs, will be slower. This is an argument for pursuing genuinely novel methodology rather than incremental variation on known factors.

It is not an argument for avoiding publication. The evidence on whether factor decay is primarily driven by academic publication or by independent discovery by sophisticated investors is ambiguous — Novy-Marx (2015) argues that most factors were known to practitioners before academic publication. The decay may be primarily an effect of practitioner adoption, not academic dissemination.

---

## Lesson VI — The Hardness of a Problem Is Informative

When a problem resists sustained, talented effort for a long time, that resistance is information about the structure of the problem, not just about the inadequacy of the people working on it.

The Yang-Mills mass gap problem has been open since 1954. It is not open because mathematicians and physicists are insufficiently clever. It is open because it involves a genuinely non-perturbative phenomenon — the generation of mass through quantum effects in a theory that has no mass at the classical level — that requires mathematical tools that do not yet fully exist. The Clay Mathematics Institute designated it one of the seven Millennium Prize Problems, with a $1 million prize for the first correct proof. The difficulty is a signal about where the new mathematics will have to come from.

The Riemann hypothesis — the claim that all non-trivial zeros of the zeta function have real part $1/2$ — has been open since 1859. The best mathematicians of the 19th and 20th centuries worked on it without success: Hardy proved infinitely many zeros lie on the critical line but could not prove all of them do. The difficulty is not accidental. The Riemann hypothesis is connected to deep questions about the distribution of prime numbers, the analytic structure of the zeta function, and — through the Langlands programme — to the entire structure of modern number theory and representation theory. The problem is hard because the answer matters for many things at once.

The measurement problem in quantum mechanics has been open since the 1920s. Bohr's Copenhagen interpretation instructs you to stop asking the question. Everett's many-worlds interpretation answers it by multiplying ontology indefinitely. Bohm's pilot wave theory answers it deterministically but non-locally. None has achieved consensus after a century of work by the greatest physicists and philosophers of science. The difficulty is a signal that the problem is not merely technical but conceptual — it requires not just better mathematics but a different understanding of what physical theory is for.

**What this means operationally.** The correct response to a hard problem is not to assume the existing framework must eventually solve it with enough effort, but to ask whether the difficulty is a signal that the framework itself is inadequate. Kuhn's insight — that normal science within a paradigm tends to protect the paradigm's core commitments by adjusting auxiliary hypotheses — has the corollary that paradigm-breaking insights typically come from people who are willing to question the framework rather than patch it.

For the Yang-Mills mass gap specifically: the perturbative expansion — the standard tool of quantum field theory — breaks down precisely where the mass gap lives, in the strongly coupled regime. The difficulty is not that the perturbative tools are being applied badly but that the strongly coupled regime is genuinely beyond perturbative reach. The problem is telling you that new non-perturbative methods are needed.

---

## Lesson VII — Cross-Domain Transfer Works, But Only One Layer Deep

The final lesson is the subtlest and the one I have had to work out most carefully for myself.

The history of mathematics and physics is full of successful cross-domain transfers: Riemannian geometry to general relativity, Lie groups to particle physics, topology to gauge theory, information theory to statistical mechanics. These transfers are real, productive, and give a strong prior that mathematical structures developed in one domain will find applications in others.

But the nature of the successful transfers is consistently the same: it is the *mathematical structure* that transfers, not the *domain-specific content*. Riemannian geometry — the abstract structure of a smooth manifold with a metric — transferred to general relativity. The specific theorems of Riemannian geometry about surfaces in three-dimensional space did not transfer directly; they had to be generalised and adapted. Lie group theory transferred to quantum mechanics through representation theory — the abstract classification of group representations. The specific applications to differential equations that Lie originally studied did not transfer.

When the transfer goes wrong — when domain-specific content is mistakenly applied to a different domain — the results are at best useless and at worst actively misleading.

The clearest example in finance: several physicists in the 1990s and 2000s applied the formalism of statistical mechanics — partition functions, renormalisation group, critical phenomena — to financial markets. Some of this work was productive (Bouchaud and Potters's analysis of heavy-tailed return distributions as an analogue of critical phenomena). Most of it was not, because the analogy was pushed too far — markets are not in thermal equilibrium, the agents have goals and incentives that particles do not have, and the "interactions" are mediated through prices that are themselves dynamic quantities with no physical analogue.

Simons is the counterexample that clarifies the rule. He did not apply gauge theory to financial markets — he applied the mathematical habits of a physicist (rigour, comfort with abstraction, insistence on foundations) to the problem of finding statistical regularities in market data. The transfer was methodological, not substantive. He took from physics the way of working, not the specific content.

**What transfers and what does not:**

*Transfers well:* mathematical structures (differential geometry, group theory, topology, information theory, stochastic calculus), methodological habits (rigorous hypothesis testing, insistence on foundations, comfort with abstraction), and epistemic standards (the difference between a correlation and a causal claim, the multiple testing problem, the difference between in-sample fit and out-of-sample prediction).

*Does not transfer well:* domain-specific physical intuition (market agents are not particles and do not obey the H-theorem), domain-specific constants and parameters (there is no analogue of Planck's constant in finance), and equilibrium assumptions (physical systems tend toward thermal equilibrium; financial markets tend toward the next non-equilibrium crisis).

**The operationally useful version.** When moving between domains, ask explicitly: am I transferring a mathematical structure, or am I transferring a physical intuition? If the former, the transfer is probably productive. If the latter, be suspicious — the intuition was developed in a specific physical context and its validity in a new context is an empirical question that should be tested rather than assumed.

For the TFI research: I am transferring persistent homology — a mathematical structure — from topological data analysis to financial correlation networks. The structure transfers. The specific interpretations of homology classes in TDA (as voids and tunnels in high-dimensional data clouds) do not transfer directly; the financial interpretation (correlation cycles as redundant network connections) has to be constructed afresh and validated independently.

---

## A Note on How to Read Lessons from History

These seven lessons are not laws. They are empirical generalisations with non-zero error rates. Lesson II (new ideas are resisted) does not imply that all resisted ideas are good — most resisted ideas are bad, and the resistance is appropriate. Lesson III (techniques precede foundations) does not imply that foundations never matter — sometimes they do, and sometimes techniques used without foundational understanding lead to systematic errors. Lesson I (mathematics precedes applications) does not imply that every piece of pure mathematics will eventually find a physical application — most of it will not.

The lessons are useful as priors, not as certainties. When I see a new mathematical structure that seems to describe a physical or financial phenomenon, my prior — informed by Lesson I — is that the connection is worth investigating seriously, not dismissing as coincidence. When I encounter resistance to the TFI research from the asset pricing community, my prior — informed by Lesson II — is that the resistance is probably partly substantive (the evidence needs to be stronger) and partly paradigmatic (the methodology is non-standard), and I should respond to the substantive part while not being deflected by the paradigmatic part.

The value of studying history is not the extraction of rules but the calibration of priors — adjusting your initial estimates about how intellectual progress works in ways that make you more likely to be right and less likely to make the standard mistakes. That calibration is worth the effort. The standard mistakes are expensive.

---

*Last updated March 2026.*