---
title: "Introduction to Quantitative Finance"
date: 2026-03-12
parent: "Quantitative Finance"
description: "Quantitative finance from a mathematical physics perspective. Stochastic calculus, Black-Scholes equations, risk-neutral pricing, and financial mathematics."
---


I came to quantitative finance the way a physicist might: through the mathematics. The connection became obvious once I understood what the subject actually is. Quantitative finance is, at its core, the application of probability theory, stochastic calculus, and partial differential equations to the problem of pricing financial instruments and managing the risks they generate. The Black-Scholes equation is a parabolic PDE. The risk-neutral pricing measure is a Girsanov transformation. The Feynman-Kac theorem connects stochastic differential equations to PDEs in exactly the way the path integral connects quantum mechanics to classical mechanics.

The mathematics I had been studying for theoretical physics — measure theory, PDEs, stochastic processes, functional analysis — turned out to be exactly the mathematics of quantitative finance, applied to a different set of questions. That was the entry point.

This page is an account of how I have approached the subject: the structure of the field, the mathematical prerequisites, the resources I have found useful, and where my current interest lies. It is written from the perspective of someone coming from physics and mathematics, not from economics or trading.

---

## What Quantitative Finance Actually Is

The term is used loosely in the industry to cover several related but distinct activities. It is worth being precise about the distinctions, because the mathematics and the skills required are quite different.

**Derivatives pricing and financial engineering.** Building mathematical models for the fair value of financial derivatives — options, futures, swaps, and more exotic instruments. The fundamental problem is: given the current state of the market, what is the correct price for a contract that pays off in some state-contingent way in the future? The tools are risk-neutral pricing, stochastic calculus, and PDEs. Black-Scholes is the prototype; volatility surface modelling, interest rate models, and credit models are the main areas of active work.

**Statistical arbitrage and systematic trading.** Identifying and exploiting predictable patterns in financial time series using statistical and machine learning methods. The fundamental problem is: given historical data on asset prices and other signals, can you identify a strategy that generates risk-adjusted returns above the market? The tools are time series analysis, linear algebra, signal processing, machine learning, and execution algorithms.

**Risk management.** Measuring and controlling the risk exposures of a portfolio or an institution. The fundamental problem is: given a complex portfolio of financial instruments, what is its exposure to various risk factors, and how do you hedge or limit that exposure? The tools are scenario analysis, Value at Risk (VaR) and Expected Shortfall, copulas, and Monte Carlo simulation.

**Portfolio management and asset allocation.** Determining the optimal allocation of capital across assets to achieve a given objective (maximise return for a given level of risk, or minimise tracking error against a benchmark). The tools are mean-variance optimisation (Markowitz), the Capital Asset Pricing Model (CAPM), factor models, and more modern approaches including machine learning.

My interest is primarily in derivatives pricing and in systematic trading — the former because the mathematics is beautiful and connects directly to the physics I already know, the latter because the empirical structure of financial markets is a genuinely interesting complex system.

---

## The Mathematical Prerequisites

Coming from theoretical physics, I had most of the mathematics already. But the specific tools needed for quantitative finance are worth naming precisely, because they are a specific subset of the broader mathematical infrastructure.

### Probability Theory

Not just elementary probability — measure-theoretic probability. You need to understand what a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ is, what a random variable is as a measurable function, what expectation is as a Lebesgue integral, and what conditional expectation $\mathbb{E}[X | \mathcal{F}_t]$ means. Conditional expectation with respect to a $\sigma$-algebra is the central operation of mathematical finance — the price of a derivative at time $t$ is the conditional expectation of its discounted payoff, under the risk-neutral measure, given the information available at $t$.

**Resources:**
- *Probability and Measure* — Patrick Billingsley. The standard rigorous treatment. Demanding but complete.
- *A First Look at Rigorous Probability Theory* — Jeffrey Rosenthal. Gentler than Billingsley; good starting point.
- *Probability: Theory and Examples* — Rick Durrett. Free online. The graduate standard in the US.

### Stochastic Calculus

The mathematics of integration with respect to Brownian motion. The key objects are:
- Brownian motion $W_t$ and its properties (continuous paths, independent increments, Gaussian distributions)
- The Itô integral $\int_0^T f(t) dW_t$ and why ordinary Riemann integration does not work (quadratic variation is non-zero)
- Itô's lemma: the stochastic chain rule $df(W_t) = f'(W_t)dW_t + \frac{1}{2}f''(W_t)dt$
- Stochastic differential equations: $dX_t = \mu(X_t, t)dt + \sigma(X_t, t)dW_t$
- Girsanov's theorem: change of measure, risk-neutral pricing
- The Feynman-Kac formula: connecting SDEs to PDEs

**Why this matters for finance.** The price of a stock (in the simplest model) follows the SDE $dS_t = \mu S_t dt + \sigma S_t dW_t$ — geometric Brownian motion. The Black-Scholes equation for the price $V(S, t)$ of an option follows from applying Itô's lemma to $V(S_t, t)$ and eliminating the stochastic term by hedging. The resulting PDE is:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

This is a parabolic PDE — structurally identical to the heat equation, which is one of the basic equations of mathematical physics. The connection is not a coincidence: by the Feynman-Kac theorem, the solution to any parabolic PDE of this form can be written as an expectation of the terminal condition under a related stochastic process.

**Resources:**

*Stochastic Calculus for Finance I: The Binomial Asset Pricing Model* — Steven Shreve
The discrete-time treatment. The binomial model for option pricing introduces risk-neutral pricing, the no-arbitrage condition, and the martingale approach in a setting where the mathematics is elementary. Do this first.

*Stochastic Calculus for Finance II: Continuous-Time Models* — Steven Shreve
The continuous-time treatment. The standard rigorous introduction to Itô calculus for finance. Chapters 1–2 develop the necessary measure theory; Chapters 3–5 develop Brownian motion, the Itô integral, and Itô's lemma. The second half covers the Black-Scholes model, American options, and interest rate models. This is the book that develops the subject properly.

*Introduction to Stochastic Calculus with Applications* — Fima Klebaner
More accessible than Shreve, with more worked examples. A good first read before Shreve II.

*Brownian Motion and Stochastic Calculus* — Karatzas and Shreve
The rigorous graduate-level treatment. Demanding; for those who want the full mathematical foundations.

*Stochastic Differential Equations: An Introduction with Applications* — Bernt Øksendal
The standard SDE textbook. Well-written and more applied than Karatzas-Shreve.

### Partial Differential Equations

The Black-Scholes equation is a PDE. More generally, derivative pricing problems often reduce to solving boundary value problems for parabolic or elliptic PDEs. The methods needed include:

- Separation of variables and Fourier transform methods (for explicit solutions in simple cases)
- Green's functions and the fundamental solution (the Black-Scholes formula is the Green's function of the Black-Scholes PDE)
- Finite difference methods (for numerical solution when closed forms are unavailable)
- The connection between PDEs and stochastic processes (Feynman-Kac)

**Resources:**
- Tong's PDE notes (Cambridge Part II) — free, covers what is needed for the physics-to-finance transition
- Evans, *Partial Differential Equations* — the rigorous graduate treatment
- Wilmott, *Paul Wilmott on Quantitative Finance* — PDE methods in finance, specifically

### Linear Algebra and Numerical Methods

Portfolio optimisation is a quadratic programming problem in the space of asset weights. The covariance matrix of asset returns is the central object. Numerical linear algebra — eigendecomposition, the Cholesky factorisation, numerical stability — becomes important when the dimension is large (hundreds or thousands of assets).

Numerical methods for PDEs (finite differences, finite elements) and for stochastic processes (Monte Carlo simulation) are the main computational tools of quantitative finance.

### Statistics and Time Series Analysis

For systematic trading, the relevant mathematics is:
- Linear regression and its properties (OLS, GLS, the Gauss-Markov theorem)
- Time series models: AR, MA, ARMA, ARIMA, GARCH
- Cointegration and pairs trading
- Factor models for asset returns
- Machine learning methods: regularisation (Lasso, Ridge), random forests, neural networks

---

## The Subject Itself

### Derivatives and Option Pricing

A **derivative** is a financial instrument whose value depends on (is derived from) the value of some underlying asset — a stock price, an interest rate, a commodity price, a credit spread. Options are the most important class of derivatives.

A **European call option** gives the holder the right (but not the obligation) to buy the underlying asset at price $K$ (the strike) at time $T$ (the expiry). The payoff is $\max(S_T - K, 0)$. What is this worth today?

The Black-Scholes answer assumes that the stock price follows geometric Brownian motion:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
Under this assumption, the price of the European call is:
$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$
where
$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$
and $N(\cdot)$ is the standard normal CDF. This is the Black-Scholes formula.

The derivation — through the delta-hedging argument, the Itô calculus, and the PDE — is one of the most elegant applications of mathematics to a practical problem I have encountered. The key insight is that the $\mu$ (the drift of the stock) does not appear in the formula: the option price depends only on the volatility $\sigma$, the current stock price, the strike, the time to expiry, and the risk-free rate. This is risk-neutral pricing.

**What Black-Scholes gets wrong.** The model assumes constant volatility. In practice, implied volatility varies with strike and expiry — the **volatility surface** or **volatility smile**. Understanding and modelling this smile is the central problem of modern options pricing. The main approaches are:

- **Local volatility models** (Dupire, 1994): $\sigma = \sigma(S, t)$, a deterministic function of price and time
- **Stochastic volatility models** (Heston, 1993; SABR): $\sigma$ itself follows an SDE
- **Jump-diffusion models** (Merton, 1976): add Poisson jump processes to the stock price dynamics
- **Rough volatility models** (Gatheral, Rosenbaum, Jaisson, 2018): fractional Brownian motion with Hurst exponent $H < 1/2$, motivated by empirical evidence that volatility is rougher than standard Brownian motion predicts

### Interest Rate Models

Interest rates are not constant — they vary over time and across maturities (the yield curve). Modelling the yield curve is essential for pricing bonds, interest rate swaps, caps, floors, and swaptions.

The main frameworks:
- **Short rate models**: model the instantaneous risk-free rate $r_t$ as an SDE. Vasicek (1977): $dr_t = \kappa(\theta - r_t)dt + \sigma dW_t$ (mean-reverting, Gaussian). Cox-Ingersoll-Ross (1985): $dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t}dW_t$ (mean-reverting, non-negative).
- **HJM framework** (Heath-Jarrow-Morton, 1992): model the entire forward rate curve $f(t, T)$ directly. No-arbitrage imposes a drift condition (the HJM drift restriction) on the SDE for $f$.
- **LIBOR Market Model** (Brace-Gatarek-Musiela, 1997): model the discrete forward rates (LIBOR rates) directly; better suited to calibration to cap/floor prices.

### Portfolio Theory

**Markowitz mean-variance optimisation.** Given $N$ assets with expected returns $\mu$ and covariance matrix $\Sigma$, find the portfolio weights $w$ that minimise variance for a given expected return:
$$\min_w \; w^T \Sigma w \quad \text{s.t.} \quad w^T \mu = \bar{\mu}, \quad \mathbf{1}^T w = 1$$
The solution traces out the **efficient frontier** in (risk, return) space. In practice, the covariance matrix is estimated from historical data and the optimisation is sensitive to estimation error — a serious practical problem.

**Factor models.** The **Capital Asset Pricing Model** (CAPM) asserts that the expected return of an asset is linear in its beta (sensitivity to the market):
$$\mathbb{E}[R_i] = r_f + \beta_i(\mathbb{E}[R_m] - r_f)$$
The Fama-French three-factor model adds size and value factors. Modern factor models have hundreds of factors.

**The Arbitrage Pricing Theory** (Ross, 1976) and its modern implementations as linear factor models are the theoretical foundation of systematic equity strategies.

### Systematic Trading and Market Microstructure

The most mathematically active area of quantitative finance for someone with a physics background. Systematic trading means constructing trading strategies that are fully specified by mathematical rules — no discretionary decisions. The main approaches:

**Statistical arbitrage** — exploiting statistical relationships between securities that should hold in equilibrium but deviate temporarily. Pairs trading (two cointegrated stocks) is the simplest example; modern stat arb strategies involve hundreds or thousands of assets and sophisticated machine learning models.

**Trend following (momentum)** — buying assets that have been rising, selling assets that have been falling. The empirical finding that momentum is persistent across a wide range of asset classes (equities, bonds, commodities, currencies) is one of the most robustly documented anomalies in finance.

**Mean reversion** — the opposite: betting that recent moves will reverse. Works at short horizons (minutes to hours, due to market microstructure effects like the bid-ask bounce) and at long horizons (value strategies).

**Market microstructure** — the study of the mechanics of how prices are formed: order books, bid-ask spreads, price impact, adverse selection, optimal execution. The mathematics involves queuing theory, stochastic optimal control, and point processes. The Almgren-Chriss model for optimal execution is a classic application of optimal control to finance.

---

## Resources, Organised by Topic

### Entry Points

**Options, Futures, and Other Derivatives** — John Hull
The standard first book. Covers derivatives, pricing models, and risk management at an accessible level without heavy mathematics. No stochastic calculus — Hull's treatment is largely intuitive and algebraic. Read this first to get the vocabulary and the financial context. Every quant has read this.

**Paul Wilmott Introduces Quantitative Finance** — Paul Wilmott
A gentler version of Wilmott's three-volume treatise. More mathematical than Hull, but more intuitive than Shreve. Covers Black-Scholes, volatility, numerical methods, and a wide range of derivative products. Good as a bridge between Hull and the serious mathematical treatments.

**The Concepts and Practice of Mathematical Finance** — Mark Joshi
The book I found most useful as a transition from physics/mathematics into finance. Joshi is a former mathematical physicist turned quant, and the book is written from that perspective — it takes the mathematics seriously and connects the theory to how models are actually used and calibrated in practice. The chapter on model risk is particularly good.

**Financial Calculus: An Introduction to Derivative Pricing** — Martin Baxter and Andrew Rennie
Short (240 pages), rigorous, and beautifully written. The most elegant introduction to the mathematics of derivative pricing that I have found. Develops the martingale approach to pricing from first principles, treats the continuous-time limit carefully, and covers Black-Scholes, interest rates, and the change-of-numeraire technique. Read this alongside or after Shreve I.

### Stochastic Calculus

*Already covered in the prerequisites section.* The progression is: Shreve I (discrete) → Baxter-Rennie or Klebaner (continuous, accessible) → Shreve II (continuous, rigorous) → Karatzas-Shreve or Øksendal (advanced).

### Derivatives Pricing and Volatility

**Paul Wilmott on Quantitative Finance** (3 volumes) — Paul Wilmott
The encyclopaedia of quantitative finance. Covers every significant derivative product, pricing model, and numerical method. Very broad and reasonably deep. The treatment of exotic options and the chapters on volatility modelling are the best single-volume treatments of those topics.

**The Volatility Surface** — Jim Gatheral
The definitive treatment of stochastic volatility modelling and the volatility surface. Covers local volatility, Heston, SABR, and the connection between these models and the empirical behaviour of implied volatility. Assumes knowledge of stochastic calculus.

**Interest Rate Models — Theory and Practice** — Brigo and Mercurio
The comprehensive treatment of interest rate derivatives and term structure modelling. Covers short rate models, HJM, the LIBOR market model, and credit risk. Dense but authoritative.

### Systematic Trading and Quantitative Strategies

**Quantitative Trading** — Ernest Chan
An accessible introduction to systematic trading strategies. Chan explains backtesting, the dangers of overfitting, Sharpe ratio, and the construction of simple mean-reversion and momentum strategies. Practical and honest. The sections on the Kelly criterion and position sizing are particularly useful.

**Algorithmic Trading** — Ernest Chan
The sequel. More advanced strategies, more detailed treatment of market microstructure and execution, and case studies of specific systems. The treatment of cointegration and pairs trading is clear and practical.

**Active Portfolio Management** — Grinold and Kahn
The foundational text on quantitative equity portfolio management. Introduces the information ratio, the fundamental law of active management (IR ≈ IC × √BR, where IC is information coefficient and BR is breadth), and the alpha model framework. More technical than Chan but more directly relevant to institutional quantitative equity investing.

**Inside the Black Box** — Rishi Narang
Not a technical text — a clear-eyed overview of how quantitative hedge funds actually work, what the different strategies are, how risk management operates, and what distinguishes successful from unsuccessful firms. Essential context.

**Advances in Financial Machine Learning** — Marcos López de Prado
A sophisticated treatment of machine learning methods specifically designed for financial time series. López de Prado identifies the standard pitfalls of applying ML to finance (data snooping, leakage, non-stationarity) and proposes methods to avoid them. The chapter on feature engineering for financial signals is the best treatment of that problem I have found.

### Interview Preparation

**A Practical Guide to Quantitative Finance Interviews** — Xinfeng Zhou
The standard interview preparation book. Covers probability, statistics, linear algebra, stochastic processes, and derivatives pricing at the level required for quantitative trading and research interviews at hedge funds, investment banks, and prop trading firms.

**Heard on the Street** — Timothy Crack
A classic collection of quantitative interview questions. Less systematic than Zhou but covers a wider range of puzzles and probability problems. The questions on market microstructure and options are useful.

**Quant Job Interview Questions and Answers** — Mark Joshi
More technically demanding than Zhou. Covers the mathematics of derivatives pricing in detail and includes real interview questions from firms. Good for those targeting derivatives pricing roles.

---

## Online Resources

**QuantLib** — [quantlib.org](https://www.quantlib.org)
Open-source library for quantitative finance. Implements most standard pricing models, yield curve construction, Monte Carlo simulation, and much else. Available in C++, Python, and other languages. Working through QuantLib's implementation of specific models is one of the best ways to understand how the mathematics is actually computed.

**QuantStart** — [quantstart.com](https://www.quantstart.com)
Articles and self-study guides on quantitative finance, algorithmic trading, and the associated mathematics and programming. The self-study plan for becoming a quantitative analyst is well-structured.

**Wilmott Forums** — [wilmott.com](https://wilmott.com)
The professional forum for quantitative finance. Active discussion of technical problems in derivatives pricing, volatility modelling, and risk management. The level is high.

**QuantLib Python Cookbook** — 
Practical guide to using QuantLib from Python, with worked examples in bond pricing, yield curve construction, and option pricing.

**Lectures in Quantitative Finance** — various authors on arXiv (q-fin section: [arxiv.org/archive/q-fin](https://arxiv.org/archive/q-fin))
Research papers in quantitative finance. The q-fin.MF (mathematical finance) and q-fin.PR (pricing) sections are most relevant for derivatives; q-fin.ST (statistical finance) and q-fin.PM (portfolio management) for systematic trading.

---

## How This Connects to My Other Work

The connection to theoretical physics is not superficial. Several specific areas of overlap are worth naming.

**Stochastic processes and field theory.** The path integral formulation of quantum mechanics is the continuous-time limit of a random walk. The Black-Scholes PDE is the heat equation. The pricing measure change (Girsanov's theorem) is formally analogous to the Faddeev-Popov procedure in gauge theory: both involve a change of measure that introduces a Jacobian. The functional methods of quantum field theory — the generating functional, perturbation theory, Feynman diagrams — have been applied directly to financial problems (the statistical mechanics of markets approach, developed by Bouchaud, Potters, and collaborators).

**Renormalisation group and complex systems.** Financial markets are complex systems exhibiting scale-free behaviour, power-law tails in return distributions, and non-trivial correlations across time scales. The empirical observation that price fluctuations are heavy-tailed (not Gaussian) is inconsistent with the Black-Scholes assumption and has been studied using the same tools as critical phenomena in statistical mechanics: scaling laws, universality, the renormalisation group.

**The connection to my research.** My active interest in quantitative finance is specifically in the systematic trading direction — building data-driven strategies that exploit predictable structure in financial time series. The mathematical connection to the time series analysis I do in the astronomy projects (Lomb-Scargle periodograms, feature extraction from variable star light curves) is direct: in both cases you are looking for predictable signal in noisy data, and the question is whether the signal is statistically significant or an artefact of multiple testing.

The physics perspective on financial markets — treating them as complex systems governed by emergent statistical regularities rather than as mechanisms for aggregating rational expectations — is the perspective I find most compelling and most scientifically honest.

---

## Where I Am

I am actively reading in this area. The current focus is on the systematic trading direction — understanding the mathematical foundations of factor models and the statistical methods for building and validating quantitative strategies. The Shreve volumes are the active technical reading; Joshi's book has been the most useful practical bridge; López de Prado's treatment of ML in finance is the most relevant to the data analysis skills I already have from the astronomy projects.

The honest summary is that I am at an intermediate level: the mathematics is familiar from the physics background, the financial applications are being learned. The subject is large and the learning curve is genuinely steep, not because the mathematics is harder than what I already know but because the vocabulary, the conventions, and the specific institutional structure of financial markets require dedicated study.

The goal is to build the depth needed for quantitative research in systematic trading — not just to understand the existing methods but to contribute to them.

---

*Last updated March 2026.*