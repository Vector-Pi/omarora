---
title: "Math & Coding Prerequisites"
date: 2026-03-14
parent: "Quantitative Finance"
---

This page is the practical companion to the [introduction to quantitative finance](/quantitative-finance/introduction-to-quantitative-finance/). That page describes the landscape of the subject. This page answers the question: what do you actually need to know before you can engage seriously with it?

The answer depends on what part of quantitative finance you are targeting. Derivatives pricing requires a specific subset of mathematics — measure theory, stochastic calculus, PDEs — that overlaps heavily with mathematical physics. Systematic trading requires a different subset — statistics, time series, machine learning, optimisation — that overlaps with data science. Both require programming. I will cover both, and be explicit about which subject belongs where.

The page is structured in three parts: the mathematical prerequisites, the programming prerequisites, and the domain-specific mathematical tools. Within each part, subjects are ordered by dependency — do not skip ahead.

---

## Part I — Mathematical Prerequisites

### 1. Calculus and Analysis

**Why it matters.** Everything in quantitative finance involves continuous functions, rates of change, and integration. The Black-Scholes PDE requires partial derivatives. Option pricing requires integration over probability distributions. Portfolio optimisation requires calculus-based optimisation. These are not optional.

**What you need specifically:**

*Single-variable calculus:* derivatives, the chain rule, integration (Riemann and improper), Taylor series. These should be genuinely fluent — not just the formulas but the understanding of why they work.

*Multivariable calculus:* partial derivatives, the gradient, the Jacobian, multiple integrals, change of variables. In finance, you routinely differentiate option prices with respect to multiple inputs simultaneously (the Greeks: $\Delta = \partial V/\partial S$, $\Gamma = \partial^2 V/\partial S^2$, $\Theta = \partial V/\partial t$, $\mathcal{V} = \partial V/\partial \sigma$, $\rho = \partial V/\partial r$). This requires multivariable calculus.

*Real analysis:* limits, continuity, convergence of sequences and series. This matters less for applied work but becomes essential if you are going to read Shreve rigorously or understand why the Itô integral requires a separate theory from ordinary calculus.

**Resources:**

*Calculus* — Michael Spivak
The rigorous treatment. If you have done this (or an equivalent), you are ready. If not, Stewart's Calculus is adequate for the applied needs of finance, with Spivak's Calculus as the deeper foundation.

*Mathematics for Finance: An Introduction to Financial Engineering* — Marek Capiński and Tomasz Zastawniak
Develops the calculus and probability specifically needed for finance, from scratch, at an accessible level. The most direct path if your calculus is rusty and you want to reach the finance as quickly as possible.

---

### 2. Linear Algebra

**Why it matters.** Portfolio optimisation is a quadratic programme in $\mathbb{R}^n$ where $n$ is the number of assets. The covariance matrix $\Sigma$ of asset returns is the central object — it must be estimated, inverted (or pseudo-inverted), decomposed, and manipulated. Factor models express returns as linear combinations of factor exposures. Principal component analysis (used for dimensionality reduction in systematic strategies) is an eigendecomposition. Numerical methods for PDEs involve large sparse linear systems.

**What you need specifically:**

- Vector spaces, linear maps, and their matrix representations
- Matrix multiplication, the inverse, the determinant, the trace
- Systems of linear equations: Gaussian elimination, the rank-nullity theorem
- Eigenvalues and eigenvectors; diagonalisation; the spectral theorem for symmetric matrices
- The singular value decomposition (SVD)
- Positive definite matrices (covariance matrices are symmetric positive semi-definite)
- The Cholesky decomposition (used for simulating correlated random variables in Monte Carlo)
- Quadratic forms and quadratic optimisation

**Resources:**

*Linear Algebra Done Right* — Sheldon Axler
The right starting point. Axler builds the theory from linear maps, not matrix manipulation, which means the framework transfers cleanly to the abstract settings of functional analysis and numerical methods.

*Introduction to Linear Algebra* — Gilbert Strang
The computational complement to Axler. The MIT OCW lectures are free. Strang is particularly good on applications and numerical methods.

*Matrix Computations* — Golub and Van Loan
The professional reference for numerical linear algebra. Used by practitioners who implement eigendecompositions, Cholesky factorisations, and SVDs from scratch. Heavy; treat as a reference.

---

### 3. Probability Theory

**Why it matters.** All of quantitative finance is built on probability theory. The price of a derivative is an expectation. Risk measurement is a statement about probability distributions. Factor models decompose the distribution of asset returns. The entire machinery of financial mathematics requires a rigorous understanding of probability — not just the formulas but the framework.

The key distinction: *measure-theoretic probability* versus *elementary probability*. Elementary probability (with sample spaces, combinatorics, and naive expectations) is insufficient. You need the framework of:

- **Probability spaces** $(\Omega, \mathcal{F}, \mathbb{P})$: a sample space, a $\sigma$-algebra of events, and a probability measure
- **Random variables** as measurable functions $X: \Omega \to \mathbb{R}$
- **Expectation** as Lebesgue integration: $\mathbb{E}[X] = \int_\Omega X(\omega) d\mathbb{P}(\omega)$
- **Conditional expectation** $\mathbb{E}[X | \mathcal{G}]$ with respect to a sub-$\sigma$-algebra
- **Filtrations** $\{F_t\}_{t \geq 0}$: the formalisation of "information available up to time $t$"
- **Martingales**: processes $M_t$ such that $\mathbb{E}[M_t | \mathcal{F}_s] = M_s$ for $s \leq t$

Martingales are central to financial mathematics because the risk-neutral pricing formula states that the discounted price of any tradeable asset is a martingale under the risk-neutral measure $\mathbb{Q}$.

**Resources:**

*A First Look at Rigorous Probability Theory* — Jeffrey Rosenthal
The gentlest rigorous introduction. Develops measure theory as needed, focuses on what probabilists actually use. The right starting point for someone coming from calculus.

*Probability and Measure* — Patrick Billingsley
The standard rigorous treatment. Demanding but complete. Read after Rosenthal.

*Probability: Theory and Examples* — Rick Durrett
Free online at [math.duke.edu/~rtd/PTE/pte.html](https://www.math.duke.edu/~rtd/PTE/pte.html). The graduate standard. The chapters on martingales are the ones you need most for finance.

*Probability with Martingales* — David Williams
Short, elegant, and specifically focused on the martingale theory needed for finance. The proof of the optional stopping theorem and the martingale convergence theorem are here.

---

### 4. Statistics and Econometrics

**Why it matters.** For systematic trading and risk management, statistics is not background — it is the primary tool. Every strategy requires empirical validation. Every model requires fitting to data. The central challenges of systematic trading are statistical: how do you build a model that is genuinely predictive rather than overfit to historical data?

**What you need specifically:**

*Core statistics:* maximum likelihood estimation, confidence intervals, hypothesis testing, the central limit theorem, the law of large numbers.

*Regression analysis:* ordinary least squares (OLS) in detail — the assumptions, when they fail, and what to do. The Gauss-Markov theorem. Multicollinearity, heteroskedasticity, autocorrelation. The Frisch-Waugh-Lovell theorem (the geometry of projection). Regularisation: Ridge regression ($L_2$ penalty) and Lasso ($L_1$ penalty) for high-dimensional problems.

*Time series analysis:* this is where most systematic trading research lives.
- Stationarity and integration: what it means for a time series to be $I(0)$ (stationary) versus $I(1)$ (random walk)
- Autocorrelation and the ACF/PACF
- AR($p$), MA($q$), ARMA($p,q$), ARIMA($p,d,q$) models
- GARCH models: $\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$ — the standard model for financial volatility, which clusters in real markets
- Cointegration: two $I(1)$ series whose linear combination is $I(0)$. The basis of pairs trading.
- The Kalman filter: state-space model for dynamical systems with noisy observations. Used in adaptive statistical arbitrage.

*Factor models:* the CAPM, Fama-French, APT, and their empirical implementation. Understanding the difference between a factor model for expected returns (used in portfolio construction) and a risk factor model (used in risk management) is important.

**Resources:**

*Statistics* — Freedman, Pisani, Purves
The conceptual foundation. Written for statisticians, not engineers. The chapters on hypothesis testing and the chi-squared test are unusually careful.

*Time Series Analysis* — James Hamilton
The comprehensive treatment. Chapters 3–5 (ARMA models) and Chapter 9 (unit roots and cointegration) are the most relevant for finance.

*Analysis of Financial Time Series* — Ruey Tsay
Finance-specific time series: ARMA, GARCH, high-frequency data, factor models, value at risk. More applied than Hamilton but directly targeted at financial applications.

*Econometrics* — Fumio Hayashi
The rigorous treatment of linear regression and its extensions. The treatment of OLS as a projection in finite-sample and asymptotic settings is the cleanest I have found.

*Advances in Financial Machine Learning* — Marcos López de Prado
The most important practical treatment of statistics as applied to financial time series. López de Prado identifies all the ways standard statistical practice fails in financial data (information leakage, multiple testing, non-stationarity) and proposes solutions. Essential reading for systematic trading.

---

### 5. Stochastic Calculus

**Why it matters for derivatives pricing.** The Black-Scholes model and all its generalisations are formulated as stochastic differential equations. You cannot derive, interpret, or extend these models without stochastic calculus.

**The core content:**

*Brownian motion $W\_t$:* continuous paths, independent increments, $W\_t - W\_s \sim \mathcal{N}(0, t-s)$. The key property that drives the entire theory: **quadratic variation** $[W]\_{t} = t $, meaning $\sum (W_{t\_{i+1}} - W_{t\_i})^2 \to t$ in probability. This is why $dW\_t^2 = dt$ and why Itô calculus is different from ordinary calculus.

*The Itô integral* $\int_0^T f(t, \omega) dW_t$: defined as the $L^2$ limit of a sequence of simple process approximations. Not a Riemann-Stieltjes integral. The Itô isometry: $\mathbb{E}\left[\left(\int_0^T f dW\right)^2\right] = \int_0^T \mathbb{E}[f^2] dt$.

*Itô's lemma:* if $X_t$ satisfies $dX_t = \mu_t dt + \sigma_t dW_t$ and $f$ is twice continuously differentiable, then:
$$df(X_t) = f'(X_t) dX_t + \frac{1}{2} f''(X_t) \sigma_t^2 dt = \left(\mu_t f'(X_t) + \frac{1}{2}\sigma_t^2 f''(X_t)\right)dt + \sigma_t f'(X_t) dW_t$$
The extra $\frac{1}{2}\sigma^2 f''$ term (the Itô correction) arises from $dW_t^2 = dt$ and has no analogue in ordinary calculus. It is responsible for all the distinctive features of stochastic calculus.

*Geometric Brownian Motion:* $dS_t = \mu S_t dt + \sigma S_t dW_t$. The solution is $S_t = S_0 \exp\left((\mu - \frac{1}{2}\sigma^2)t + \sigma W_t\right)$, obtained by applying Itô's lemma to $f(S) = \ln S$.

*Girsanov's theorem:* if $\theta_t$ is an adapted process satisfying the Novikov condition, then the process $\tilde{W}_t = W_t + \int_0^t \theta_s ds$ is a Brownian motion under the new measure $\tilde{\mathbb{P}}$ defined by $\frac{d\tilde{\mathbb{P}}}{d\mathbb{P}} = \exp\left(-\int_0^T \theta_t dW_t - \frac{1}{2}\int_0^T \theta_t^2 dt\right)$. This is the measure change that converts the $\mathbb{P}$-drift to the risk-neutral $\mathbb{Q}$-drift $r$ in the Black-Scholes model.

*The Feynman-Kac formula:* if $V(x,t)$ solves the PDE
$$\frac{\partial V}{\partial t} + \mu(x,t)\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2(x,t)\frac{\partial^2 V}{\partial x^2} - r V = 0, \quad V(x,T) = g(x)$$
then $V(x,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[g(X_T) | X_t = x]$ where $X_t$ satisfies $dX_t = \mu dt + \sigma dW_t^{\mathbb{Q}}$. This directly gives the risk-neutral pricing formula: the Black-Scholes formula is the Feynman-Kac solution of the Black-Scholes PDE.

**Resources:**

*Stochastic Calculus for Finance I: The Binomial Asset Pricing Model* — Shreve
Start here. The discrete-time binomial model introduces risk-neutral pricing, martingales, the change of measure, and the dynamic hedging argument in a setting where all the mathematics is elementary (no measure theory, no Itô calculus). The conceptual structure of continuous-time finance is completely visible in the discrete-time setting.

*Stochastic Calculus for Finance II: Continuous-Time Models* — Shreve
The rigorous continuous-time treatment. The gold standard. Chapters 1–3 (probability background, conditional expectation, Brownian motion) lay the foundations; Chapters 4–5 (Itô integral, risk-neutral pricing) are the core. Do not skip Shreve I before reading Shreve II.

*Financial Calculus: An Introduction to Derivative Pricing* — Baxter and Rennie
The most elegant short introduction (240 pages). Read this alongside Shreve II for a different perspective.

*Introduction to Stochastic Calculus with Applications* — Klebaner
More accessible than Shreve, with more worked examples. Good as a first read before Shreve II.

*Stochastic Differential Equations: An Introduction with Applications* — Øksendal
The standard SDE textbook beyond Shreve. More applied, more examples.

---

### 6. Partial Differential Equations

**Why it matters.** Every derivative pricing problem in the Black-Scholes framework produces a PDE. The Black-Scholes PDE is a parabolic equation:
$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$
with terminal condition $V(S, T) = $ payoff. Solving it for various payoffs and boundary conditions (European options, American options, barrier options, Asian options) requires understanding the theory of parabolic PDEs: the maximum principle, fundamental solutions, Green's functions, and the connection to heat diffusion.

**What you need specifically:**

- Classification of second-order linear PDEs (elliptic, parabolic, hyperbolic)
- The heat equation and its fundamental solution (the Black-Scholes formula *is* the heat equation fundamental solution after a change of variables)
- Boundary value problems and the maximum principle
- Separation of variables and Fourier transforms (used for explicit option pricing formulas)
- Numerical methods: the finite difference method (explicit, implicit, Crank-Nicolson) for solving option pricing PDEs when closed forms are unavailable

**Resources:**

*Introduction to Partial Differential Equations* — Walter Strauss
Clear and accessible. Covers the heat equation, wave equation, and Laplace equation with good physical intuition.

*Paul Wilmott on Quantitative Finance* — Wilmott
The finance-specific PDE treatment. The chapters on the Black-Scholes PDE, boundary conditions for different option types, and numerical methods are directly relevant. Volume 1 is essentially a PDE textbook oriented entirely toward finance.

David Tong's Cambridge PDE notes — free at [damtp.cam.ac.uk/user/tong/teaching.html](http://www.damtp.cam.ac.uk/user/tong/teaching.html). The electrodynamics and applied mathematics notes cover the relevant PDE background.

---

### 7. Optimisation

**Why it matters.** Portfolio construction is an optimisation problem. Model calibration (fitting model parameters to observed market prices) is an optimisation problem. Optimal execution (minimising market impact when buying or selling large positions) is a stochastic optimal control problem.

**What you need specifically:**

*Convex optimisation:* unconstrained optimisation (gradient descent, Newton's method), constrained optimisation (Lagrange multipliers, the KKT conditions), quadratic programming (the Markowitz problem is a QP). The duality theory of convex optimisation is important for understanding factor model construction.

*Dynamic programming and stochastic optimal control:* the Hamilton-Jacobi-Bellman equation. Used for American option pricing (where the optimal exercise boundary is determined dynamically) and for optimal execution (Almgren-Chriss model).

**Resources:**

*Convex Optimization* — Stephen Boyd and Lieven Vandenberghe
Free at [web.stanford.edu/~boyd/cvxbook](https://web.stanford.edu/~boyd/cvxbook). The definitive treatment of convex optimisation, with many finance applications. The chapter on portfolio optimisation is directly applicable.

*Dynamic Programming and Optimal Control* — Dimitri Bertsekas
The comprehensive treatment. Volumes I and II are the standard reference.

---

## Part II — Programming Prerequisites

Programming is not optional in quantitative finance. Every model must be implemented; every strategy must be backtested; every analysis requires code. The question is which languages and which skills.

### Python

**Python is the lingua franca of quantitative finance research and signal development.** The ecosystem — numpy, scipy, pandas, scikit-learn, statsmodels, matplotlib — is comprehensive, well-maintained, and widely used across the industry. If you can do one thing, do Python well.

**What you need to know:**

*Core Python:* data types, control flow, functions, classes, decorators, generators, comprehensions. The specific Python features that matter for finance: vectorised operations (numpy), data manipulation (pandas), and numerical computing (scipy).

*NumPy:* array operations, broadcasting, vectorisation. The cardinal rule: avoid Python loops over arrays; use vectorised numpy operations instead. The difference between $O(n)$ looping and vectorised computation is 100× in speed for typical array sizes.

*Pandas:* DataFrames and Series, indexing (`.loc`, `.iloc`), groupby operations, time series handling (DatetimeIndex, resampling, rolling windows), merging and reshaping. Every financial dataset you will work with lives in a DataFrame.

*SciPy:* optimisation (`scipy.optimize`), statistics (`scipy.stats`), signal processing (`scipy.signal`), linear algebra (`scipy.linalg`). These are the numerical workhorses.

*Matplotlib:* basic plotting. Not the most elegant library but the universal standard.

*Scikit-learn:* for systematic trading research — linear models, random forests, gradient boosting, cross-validation, feature selection.

*Statsmodels:* for time series — ARMA, GARCH, VAR, cointegration tests (Engle-Granger, Johansen), OLS regression with proper standard errors.

**Resources:**

*Python for Data Analysis* — Wes McKinney (creator of pandas)
The definitive guide to pandas. Read the pandas documentation alongside.

*Python for Finance* — Yves Hilpisch
Finance-specific Python: option pricing, portfolio construction, risk management, algorithmic trading, all implemented in Python. The most directly relevant Python book for quants.

*Quantitative Economics with Python* — Thomas Sargent and John Stachurski
Free at [python.quantecon.org](https://python.quantecon.org). Covers linear algebra, dynamic programming, Markov chains, time series, and many topics in mathematical economics, all implemented in Python. Extremely well-written.

*Python for Algorithmic Trading* — Yves Hilpisch
Practical implementation of systematic trading strategies in Python. Backtesting frameworks, API integration, risk management.

---

### C++

**C++ is the language of production quantitative finance.** The performance-critical systems — pricing engines, risk systems, execution infrastructure, market data processing — are written in C++. If you are targeting a derivatives price modelling or quantitative trading, you need C++ at a level sufficient to implement numerical algorithms efficiently.

**What you need to know for finance:**

*Core C++ (modern C++17/20):* classes and objects, templates, the STL (vectors, maps, algorithms), memory management (RAII, smart pointers — avoid raw `new` and `delete`), move semantics. You do not need to be a C++ expert to do finance, but you need to be fluent enough to implement a Monte Carlo pricer or a finite difference solver without making memory errors.

*Numerical performance:* understanding where time goes in numerical code — cache locality, branch prediction, SIMD, compiler optimisation. The difference between well-written and poorly-written C++ for a Monte Carlo simulation is easily 10×.

*Template metaprogramming:* used in financial libraries (QuantLib, for example) to express mathematical operations generically. You need to be able to read and write basic templates.

**Resources:**

*A Tour of C++* — Bjarne Stroustrup
The concise introduction to modern C++ by its creator. 240 pages. Read this first.

*The C++ Programming Language* — Bjarne Stroustrup
The comprehensive reference. Use after the Tour.

*Implementing Quantitative Finance in C++* — Mark Joshi
Directly relevant. Joshi implements option pricing models, Monte Carlo methods, and finite difference schemes in C++. The explanations of why the code is structured the way it is are as valuable as the code itself.

*C++ Design Patterns and Derivatives Pricing* — Mark Joshi
The follow-up. Object-oriented design of financial software. Strategy patterns, polymorphism, and factory methods applied to building a flexible option pricing library.

---

### R (Optional)

**R** is used in quantitative research, particularly in statistical arbitrage and risk research. Its strength is the breadth of statistical packages — the `quantmod`, `PerformanceAnalytics`, `PortfolioAnalytics`, and `rugarch` packages are excellent. If you are primarily targeting derivatives pricing or execution, R is not necessary. If you are targeting statistical research or risk management, it is useful.

---

### SQL

**SQL is unavoidable in practice.** All financial data lives in databases — market data, trade data, position data, reference data. You need to be able to write non-trivial SQL: joins (inner, left, outer), aggregations (`GROUP BY`), window functions (`ROW_NUMBER`, `LAG`, `LEAD`), and CTEs.

---

## Part III — Domain-Specific Mathematical Tools

These are the tools that appear specifically in quantitative finance, not in general mathematics or physics.

### Risk Measures

**Value at Risk (VaR):** the $\alpha$-quantile of the loss distribution over a given horizon. $\text{VaR}_\alpha = -\inf\{l : \mathbb{P}(L > l) \leq 1 - \alpha\}$. The standard risk measure in banking regulation (Basel III), but has the significant deficiency that it is not sub-additive and ignores tail structure beyond the quantile.

**Expected Shortfall (ES / CVaR):** $ES_\alpha = \mathbb{E}[L | L > \text{VaR}_\alpha]$. The expected loss conditional on exceeding VaR. Sub-additive, coherent (in the sense of Artzner-Delbaen-Eber-Heath), and a better measure of tail risk. Mandated by Basel III.5.

**Coherent Risk Measures:** a risk measure $\rho$ is coherent if it satisfies: monotonicity, sub-additivity, positive homogeneity, and translation invariance. The axiomatic framework (Artzner et al. 1999) is the theoretical foundation of risk measurement.

### The Greeks

The Greeks are the partial derivatives of an option price with respect to its inputs. Understanding them is essential for hedging and for understanding the sensitivities of an options portfolio:

| Greek | Symbol | Definition | Interpretation |
|-------|--------|-----------|----------------|
| Delta | $\Delta$ | $\partial V / \partial S$ | sensitivity to underlying price |
| Gamma | $\Gamma$ | $\partial^2 V / \partial S^2$ | rate of change of delta |
| Theta | $\Theta$ | $\partial V / \partial t$ | time decay |
| Vega | $\mathcal{V}$ | $\partial V / \partial \sigma$ | sensitivity to volatility |
| Rho | $\rho$ | $\partial V / \partial r$ | sensitivity to interest rate |

For derivatives pricing roles, you need to be able to derive the Greeks analytically from the Black-Scholes formula and interpret their financial meaning.

### Monte Carlo Methods

Monte Carlo simulation is the universal numerical tool for pricing complex derivatives and for risk management. The basic structure:

1. Simulate $N$ paths of the underlying asset(s) from $t=0$ to $t=T$
2. For each path, compute the payoff of the derivative
3. Average the discounted payoffs: $V \approx e^{-rT} \frac{1}{N}\sum_{i=1}^N \text{payoff}_i$

By the law of large numbers, this converges to the correct price. The convergence rate is $O(1/\sqrt{N})$ — adding 4× more paths halves the error. Variance reduction techniques (antithetic variates, control variates, importance sampling, quasi-Monte Carlo) are important for reducing the computational cost.

**Generating correlated random variables:** if you need $n$ correlated Brownian motions with correlation matrix $C$, generate $n$ independent standard normals and multiply by the Cholesky factor of $C$. This requires the Cholesky decomposition to be numerically stable.

### The Volatility Surface

The **implied volatility** $\sigma_\text{imp}(K, T)$ of an option is the value of $\sigma$ that makes the Black-Scholes formula equal the observed market price. The implied volatility is not constant across strikes and expiries — it varies, forming the **volatility surface**.

The shape of the surface:
- The **volatility smile**: for equity options, implied vol is typically higher for low-strike (out-of-the-money put) options than for high-strike options, reflecting the empirical fat tail of equity returns
- The **term structure**: implied vol varies with expiry, typically increasing for short maturities during stressed periods
- **Skewness**: the asymmetry between puts and calls in the smile

Calibrating a stochastic volatility model (Heston, SABR) or a local volatility model (Dupire) to the observed volatility surface is a core task of derivatives pricing.

### Interest Rate Mathematics

- **Discount factors:** $P(t,T)$ = the price at time $t$ of a zero-coupon bond paying 1 at time $T$. The yield curve is $\{P(0,T)\}_{T \geq 0}$.
- **Forward rates:** $f(t,T) = -\frac{\partial \ln P(t,T)}{\partial T}$, the instantaneous forward rate.
- **Duration and convexity:** the first and second derivatives of a bond's price with respect to yield. The basis of interest rate risk management.
- **The yield curve construction** (bootstrapping from swap rates, Treasury yields, or OIS rates) is a standard task in fixed income.

---

## The Honest Summary

**To read and derive the Black-Scholes formula:** measure-theoretic probability, Brownian motion, the Itô integral, Itô's lemma, Girsanov's theorem, and the Feynman-Kac formula. Shreve I and II cover all of this. Allow 6–12 months of serious study if starting from scratch.

**To build and backtest a systematic trading strategy:** statistics and linear regression, time series analysis (stationarity, ARMA, GARCH), cointegration for pairs trading, and Python (numpy, pandas, statsmodels). López de Prado is the essential practical guide.

**To price exotic derivatives numerically:** PDEs, finite difference methods, Monte Carlo simulation, and C++ for the implementation. Wilmott's three volumes cover the pricing; Joshi covers the C++ implementation.

**To work in quantitative portfolio management:** linear algebra (covariance matrices, PCA, factor decompositions), quadratic optimisation (Markowitz), factor models (CAPM, Fama-French, APT), and both Python and SQL.

Coming from theoretical physics and mathematics, the stochastic calculus and PDE prerequisites are the easiest part — the mathematical structures are familiar. The hardest part is the domain knowledge: the financial vocabulary, the institutional structure of markets, the conventions of derivatives pricing, and the practical challenges of working with real market data. Those take time and cannot be substituted for with mathematical sophistication.

---

*Last updated March 2026.*