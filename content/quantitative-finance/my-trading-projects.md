---
title: "My Trading Projects"
date: 2026-02-06
parent: "Quantitative Finance"
---

I want to be direct about the structure of this page before anything else.

Some of what I have built and am building in quantitative trading is proprietary — either because it involves strategies that would lose their edge if described publicly, or because it is connected to commercial work where disclosure is not appropriate. I will not describe those projects in technical detail, and I will not pretend to describe them when I am not.

What I will do is give an honest account of: what the work is, at the level of methods and research questions rather than specific signals; what I have learned from it; and what the current direction is. This is the standard practice — nobody who has built something that works is going to post it on a website. The existence of proprietary constraints is itself information about the seriousness of the work.


---

## What I Have Worked On

My quantitative trading work falls into three broad areas. I will describe each at the level I am able to.

---

### Statistical Signal Research

The foundational question: does a given feature of historical price data contain predictive information about future returns, after accounting for transaction costs, data mining bias, and the multiple testing problem?

The methods I have used:

**Time series feature extraction.** Identifying candidate predictive signals from price, volume, and derived data. The feature engineering is the hardest part — the raw data is not the signal. The relevant methods overlap substantially with what I do in the astronomy projects: Lomb-Scargle periodograms, Fourier decomposition, autocorrelation analysis. The difference is that in astronomy you are looking for a deterministic periodic signal in noise; in finance you are looking for a weak statistical regularity in a process that is adversarially close to a random walk.

**Statistical validation.** The central challenge is distinguishing genuine predictive power from overfitting to historical data. The tools I have applied include walk-forward cross-validation (never in-sample validation), combinatorial purged cross-validation (following López de Prado's methodology), and bootstrap-based significance testing. The multiple testing correction — accounting for the fact that if you test 100 candidate signals, 5 will appear significant at $p < 0.05$ by chance — is something most retail systematic traders get wrong and something I have been careful about.

**Factor decomposition.** Decomposing strategy returns into known factor exposures (market, size, value, momentum, quality) to identify whether apparent alpha is genuine or merely compensation for known risk factors. A strategy that looks like it generates excess returns but is entirely explained by momentum and low-volatility factor exposure is not alpha — it is a complicated way to hold a momentum-tilt portfolio.

The specific signals I have found useful and the strategies built around them are not something I will describe here.

---

### Systematic Strategy Development

**The mechanics of building a systematic strategy** — not the signals, but the infrastructure:

**Position sizing and risk management.** The Kelly criterion in full Kelly form is theoretically optimal but practically dangerous (estimation error in the edge turns full Kelly into a ruin strategy). Fractional Kelly (typically 25–50% Kelly) is the standard in practice. I have implemented volatility-targeting position sizing, where the position in each instrument is scaled so that its volatility contribution is constant rather than its dollar value.

**Portfolio construction.** Building a portfolio of strategies or signals that are jointly optimised for the Sharpe ratio. The covariance matrix of strategy returns (not asset returns) is the central object. In practice, with a small number of strategies, the sample covariance is better than a shrinkage estimator; with a large number, the Ledoit-Wolf shrinkage estimator or a factor model is necessary to avoid the curse of dimensionality.

**Backtesting discipline.** Backtesting is where most retail systematic traders fool themselves. The standard errors are: look-ahead bias (using information not available at the time of the trade), survivorship bias (testing on a universe that includes only assets that still exist), and overfitting (optimising parameters on the historical period and mistaking in-sample fit for out-of-sample prediction). I have been careful about all three, using point-in-time data where available and strict walk-forward validation throughout.

**Transaction costs.** A signal that generates 5 bps of expected daily alpha but requires trading at a cost of 3 bps per round-trip twice a day is not profitable. Incorporating realistic transaction cost models — including market impact (the cost of moving price by trading a large order) — into the backtest is essential and almost universally done incorrectly by beginners.

---

### Topological Fragmentation — Ongoing Research

This is the project I can describe most openly, because it is still at the research stage and does not yet have a deployable strategy associated with it.

The question: does the topological structure of the correlation network of asset returns contain predictive information about future market regimes?

**The setup.** Consider the $N \times N$ correlation matrix $C$ of returns for a universe of assets over a rolling window. This matrix defines a weighted complete graph on $N$ nodes. The topological features of this graph — clustering coefficients, spectral properties of the graph Laplacian, the minimum spanning tree structure, the persistent homology of the Vietoris-Rips complex built from the correlation distances — change over time. The hypothesis is that specific topological signatures precede regime transitions: the transition from a low-volatility, diversified market to a high-volatility, highly correlated crisis state involves a characteristic change in the graph topology.

**Methods I am using:**

*Correlation-based distance:* $d_{ij} = \sqrt{2(1 - C_{ij})}$, which satisfies the triangle inequality and maps correlations to a metric space.

*Minimum spanning tree (MST):* the connected subgraph that spans all nodes with minimum total distance. The MST changes structure as correlations change — during crises, the tree collapses toward a star topology (all assets correlating with a single dominant factor).

*Persistent homology:* computing the Betti numbers $\beta_0$ (connected components), $\beta_1$ (loops), and $\beta_2$ (voids) of the Vietoris-Rips filtration built from the correlation distance matrix, as a function of the filtration parameter. The persistence diagram encodes the multi-scale topological structure of the correlation matrix.

*Spectral graph theory:* eigenvalues of the graph Laplacian $L = D - A$ (where $D$ is the degree matrix and $A$ the adjacency matrix). The Fiedler value (the second-smallest Laplacian eigenvalue, also called the algebraic connectivity) measures how well-connected the graph is. A declining Fiedler value indicates increasing fragmentation — the market is breaking into disconnected components.

**Current status.** This is active research, not a deployed strategy. The empirical finding so far is that the Fiedler value and the MST entropy are useful regime indicators — they change in the weeks before major volatility events in a way that is statistically distinguishable from noise. Whether this translates into a tradeable signal with positive after-cost Sharpe ratio is the question I am currently investigating.

The connection to the mathematical physics work is direct: persistent homology is the same tool used in topological data analysis of physical systems, and the graph Laplacian is the discrete analogue of the continuous Laplace-Beltrami operator from differential geometry. The mathematical infrastructure for this project comes from the same reading that feeds the gauge theory and QGET research.

---

## What I Cannot Discuss

To be specific about the constraints:

- The specific predictive features I use in the statistical signal research are proprietary
- The parameter values, lookback windows, and thresholds of any deployed or near-deployment strategy are proprietary
- Anything connected to commercial work involving other parties

This is not false modesty. The value of a quantitative trading strategy is destroyed by disclosure. Writing it up and posting it would be financially equivalent to deleting it.

---

## Tools and Infrastructure

The technical stack I use for trading research:

**Python** for signal research, backtesting, and data analysis. The standard scientific stack: numpy, pandas, scipy, scikit-learn, statsmodels. For the topological work: `gudhi` (persistent homology), `networkx` (graph algorithms), `scipy.sparse` (sparse Laplacian computations).

**Data sources.** Free and accessible: Yahoo Finance (daily OHLCV), FRED (macroeconomic data), Quandl/Nasdaq Data Link (various). For more serious work: Interactive Brokers historical data API (for backtesting), and for the topological research, the CRSP/Compustat database (accessed through a university).

**Risk monitoring.** A simple but disciplined risk framework: maximum drawdown limits per strategy (strategy is paused if drawdown exceeds threshold), position limits per instrument (no single instrument more than a fixed fraction of NAV), and daily PnL monitoring against an expected range based on volatility.

---

## What I Have Learned

The most important things this work has taught me, which I can state without compromising anything proprietary:

**The multiple testing problem is far more severe than most people appreciate.** If you test enough candidate signals, you will always find some that look good historically. The discipline required to distinguish genuine predictive power from data mining is the hardest part of systematic trading research, and it is almost entirely absent from popular treatments of the subject. López de Prado's *Advances in Financial Machine Learning* is the most honest professional treatment I have found.

**Transaction costs are the graveyard of systematic strategies.** The median high-frequency trader has a Sharpe ratio above 5; the median daily rebalancing strategy has a Sharpe ratio below 0.5. Most of the difference is transaction costs. A signal with a one-day holding period needs to be much stronger than a signal with a one-month holding period to survive costs.

**The connection between physics and systematic trading is real but subtle.** The techniques transfer — time series analysis, signal processing, statistical hypothesis testing, Monte Carlo methods, spectral analysis — but the domain knowledge does not. The social structure of financial markets (reflexivity, the fact that other participants are also running systematic strategies and their actions affect the signals you are trading on) has no analogue in physics. A physics model of a market that ignores this is incomplete in a way that a physics model of a galaxy ignoring the observer's effect is not.

**Patience is a genuine edge.** Most of the value in systematic trading comes from holding positions for longer than feels comfortable. The implication is that the research cycle — identifying a signal, validating it rigorously, sizing the position appropriately, and holding through drawdowns — requires a tolerance for uncertainty that is more character than mathematics.

---

*Last updated March 2026. This page is deliberately less detailed than others on this site.*