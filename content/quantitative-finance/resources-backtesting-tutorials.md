---
title: "Resources & Backtesting Tutorials"
date: 2026-02-06
parent: "Quantitative Finance"
---

Backtesting is the scientific method of systematic trading. You have a hypothesis — that some feature of historical market data predicts future returns. Backtesting is the experiment that tests the hypothesis. Like any scientific experiment, it can be done well or poorly. Most retail backtests are done poorly, and the errors are systematic and predictable. This page is about doing it properly.

The page is organised as follows: the methodology (what a rigorous backtest actually requires), the errors (what almost everyone gets wrong), the frameworks (what tools exist and what each is good for), the data sources, and a set of additional resources. There is a final section on a unified backtesting framework I am currently developing — a project aimed at closing the gap between the state of available open-source tools and the requirements of serious institutional-grade research.

---

## Part I — Backtesting Methodology

### What a Backtest Is and Is Not

A backtest is a simulation of how a trading strategy would have performed on historical data. It is not evidence that the strategy will perform in the future. The distinction matters more than it might seem.

The primary purpose of a backtest is **falsification**, not validation. A strategy that fails its backtest should be rejected. A strategy that passes its backtest has not been proven — it has survived the test. Whether it survives out-of-sample testing, whether it survives transaction costs, and whether the historical performance is a genuine signal or an artefact of data mining are separate questions that the backtest itself cannot answer.

### The Correct Workflow

**Step 1: Form the hypothesis before looking at the data.** The moment you start constructing a strategy by looking at charts and finding patterns, you have already contaminated the experiment. Every strategy should begin with an economic or statistical prior — a reason to believe the signal should work that is independent of the historical data you are about to test on. This reason should be written down before the backtest begins.

**Step 2: Define the strategy completely before running it.** Every parameter, every threshold, every rule should be specified in advance. The backtest should not be iteratively modified based on its results. If you find yourself adjusting parameters to improve the backtest, you are overfitting.

**Step 3: Use point-in-time data.** The data available at each historical date should be what was actually available on that date, not what is available now. Accounting restatements, index rebalancings, and corporate actions change historical data retroactively. Using restated data when the original data was different is a form of look-ahead bias.

**Step 4: Include transaction costs.** Every backtest that does not include realistic transaction costs is meaningless for practical purposes. The cost model should include the bid-ask spread, the exchange fee, and an estimate of market impact (the price movement caused by your own trading). Market impact scales approximately with the square root of the order size relative to average daily volume.

**Step 5: Walk-forward validation.** Split the data into an in-sample period for model development and an out-of-sample period for validation. Never adjust the strategy based on the out-of-sample results — once you look at the out-of-sample results and make a change, that period is no longer out-of-sample.

**Step 6: Report honestly.** The full distribution of outcomes matters, not just the headline Sharpe ratio. Include the maximum drawdown, the Calmar ratio, the Sortino ratio, and the performance in each subperiod. A strategy that has a Sharpe ratio of 1.5 over 10 years but had a 40% drawdown in 2022 is a different strategy from one with the same Sharpe ratio and a 10% maximum drawdown.

---

## Part II — The Seven Deadly Errors

These are the mistakes that appear in almost every retail backtest, in roughly decreasing order of severity.

### 1. Look-Ahead Bias

Using information in the backtest that would not have been available at the time of the trade. The most common forms:

- Using the closing price to generate a signal and also filling the trade at the closing price of the *same* bar (the signal was generated after the close, but the trade happened at the close)
- Using end-of-day fundamental data that was reported after market close as if it were available before open
- Using a moving average that includes the current bar's data as a signal for the current bar

**The fix:** every signal must be generated using data available before the trade is executed, and there must be an explicit delay between signal generation and execution.

### 2. Survivorship Bias

Testing on a universe of stocks that contains only the survivors — companies that still exist at the end of the backtest period. The S&P 500 constituents today are not the same as the S&P 500 constituents in 2010. Testing on the current constituents going back to 2010 overstates returns because you are only trading stocks that survived the period.

**The fix:** use a point-in-time constituent database that records which stocks were in the index on each historical date. Free workarounds include using broad market ETFs or the Russell 3000 universe with delisting returns.

### 3. Overfitting and Data Mining Bias

Optimising strategy parameters on the historical data and reporting the in-sample performance as if it were a genuine prediction. If you test 100 parameter combinations and report the best one, the best combination will look better than the true predictive power of the strategy — even if the strategy has no predictive power at all.

**The fix:** strict walk-forward validation with a fixed out-of-sample period. Correct for multiple testing using the Bonferroni correction or the Benjamini-Hochberg procedure. Report all parameter combinations tested, not just the best one.

**The number to care about.** Bailey et al. (2014) introduced the concept of the minimum backtest length needed to distinguish a genuine Sharpe ratio from data mining, as a function of the number of trials tested. For 100 parameter combinations, you need approximately 8 years of daily data before the best result's t-statistic is meaningful. For 1,000 combinations, you need 20+ years.

### 4. Ignoring Transaction Costs

A strategy that generates 3 bps of expected daily alpha but turns over the entire portfolio every day at a cost of 5 bps per round-trip is not profitable. This calculation is straightforward, but many backtests either ignore costs entirely or use unrealistically low cost assumptions.

**Typical cost structure for institutional equity trading:**

- Bid-ask spread: 1–5 bps for large-cap US equities, 5–20 bps for small-cap
- Exchange fee: 0.1–0.3 bps
- Market impact: approximately $0.1\% \times \sqrt{\text{order size} / \text{ADV}}$ (Kyle's square-root law)
- Total round-trip for large-cap: 5–15 bps at low impact, 20–50 bps at moderate impact

**The fix:** include explicit cost assumptions. Run the backtest across a range of cost assumptions (5, 10, 20 bps) and check at what cost level the strategy becomes unprofitable. If the answer is "10 bps," the strategy is marginal.

### 5. Not Accounting for Liquidity

A strategy that trades micro-cap stocks generating extraordinary backtested returns often cannot be implemented at any meaningful scale — the stocks do not have enough volume to absorb the position sizes required. A backtest that does not include a liquidity filter (minimum average daily volume, minimum market cap) will overstate capacity.

**The fix:** restrict the universe to stocks with sufficient liquidity at the intended strategy scale. A common rule: size the position so that the daily trading is less than 5% of average daily volume.

### 6. Regime Non-Stationarity

A strategy that worked well from 2010 to 2020 in a low-rate, low-volatility regime may not work in a high-rate, high-volatility regime. Many systematic strategies have implicit factor exposures that look like alpha in some regimes and are exposed in others.

**The fix:** test the strategy in subperiods with distinct market regimes: the 2011-2015 low-volatility period, the 2018 correction, the 2020 COVID crash, the 2022 rate-hiking cycle. A strategy that fails in one or more distinct subperiods is a regime-dependent strategy, not a robust one.

### 7. Conflating Gross and Net Returns

Reporting strategy gross returns (before fees, before costs) as if they were net returns. A fund with 20% gross returns and 2-and-20 fee structure returns 12-14% net to investors — still good, but not the 20% that might be cited.

---

## Part III — The Performance Metrics That Matter

### The Sharpe Ratio

$$SR = \frac{\mathbb{E}[R_p - R_f]}{\sigma_p}$$

The standard measure of risk-adjusted return. Annualised by multiplying by $\sqrt{252}$ (for daily returns). Interpretation: a Sharpe ratio above 1.0 is considered acceptable; above 1.5, good; above 2.0, exceptional and suspicious (worth checking for errors).

**The Sharpe ratio is insufficient on its own.** Two strategies with the same Sharpe ratio can have very different profiles: one might have a maximum drawdown of 5%, another 40%. The Sharpe ratio does not distinguish between them.

### The Sortino Ratio

Like the Sharpe ratio but uses only downside volatility in the denominator. Appropriate when the return distribution is asymmetric (more relevant for trend-following strategies that cut losses).

### The Calmar Ratio

$$\text{Calmar} = \frac{\text{Annualised Return}}{\text{Maximum Drawdown}}$$

Arguably more relevant than the Sharpe ratio for practitioners, because maximum drawdown is the real experience of holding the strategy through its worst period.

### Information Coefficient (IC)

For cross-sectional strategies (factor models), the IC is the rank correlation between the predicted signal and the subsequent return. An IC of 0.05 is considered good for daily predictions; 0.03 is typical for established factors.

### The Fundamental Law of Active Management

Grinold and Kahn (1994): $IR \approx IC \times \sqrt{BR}$

where $IR$ is the information ratio (Sharpe ratio of active returns), $IC$ is the information coefficient, and $BR$ is the breadth (number of independent bets per year). A low IC can be offset by high breadth — which is why diversified systematic strategies can achieve meaningful IRs with weak individual signals.

### Maximum Drawdown and Time to Recovery

The maximum drawdown is the maximum peak-to-trough decline in portfolio value. The time to recovery is how long it takes to reach a new high after the trough. A strategy with a 30% maximum drawdown and a 3-year recovery time is practically unmanageable for most investors.

---

## Part IV — The Backtesting Framework Landscape

The Python ecosystem for backtesting has bifurcated into two clear paradigms: **vectorised** (ultra-fast, batch processing, ideal for signal research) and **event-driven** (realistic, sequential, closer to production). The choice between them is a genuine trade-off, not a matter of one being universally better.

### The Vectorised Paradigm

Vectorised backtesting processes the entire historical dataset as matrix operations rather than simulating time step by step. The speed advantage is significant: a vectorised backtest that takes 10 seconds would take 10 minutes in event-driven mode.

The trade-off is realism. Vectorised engines typically assume:
- You can fill at the bar's close price regardless of order size
- All positions are rebalanced simultaneously
- There is no order book, no partial fills, no latency

For signal research and parameter sweeps — where you want to test thousands of parameter combinations quickly — vectorised is the right choice. For final validation and production deployment, you want event-driven.

**VectorBT / VectorBT PRO** ([vectorbt.pro](https://vectorbt.pro))
The best vectorised backtesting library available as of 2026. Built on NumPy, pandas, and Numba JIT compilation. Designed for parameter grid searches: you can test 10,000 combinations of lookback windows and thresholds in minutes rather than hours. The PRO version adds portfolio simulation, more realistic execution semantics, and a full research infrastructure. For signal research on large universes, this is the current state of the art. The open-source version is free; PRO requires a licence.

**backtesting.py** ([kernc.github.io/backtesting.py](https://kernc.github.io/backtesting.py))
Lightweight, well-documented, beginner-friendly. For quick prototyping. Automatically calculates performance metrics and generates interactive plots. Not suitable for large-scale research or production-grade work, but the fastest path from idea to initial result.

### The Event-Driven Paradigm

Event-driven backtesting processes data sequentially, bar by bar or tick by tick, simulating how the strategy would have behaved in real time. Each event (new bar, filled order, stop triggered) generates a response from the strategy. This is more computationally expensive but more realistic.

**Backtrader** ([backtrader.com](https://www.backtrader.com))
The most widely used event-driven framework. Mature, well-documented, supports multiple data feeds and live trading through Interactive Brokers, OANDA, and Alpaca. The learning curve is steeper than backtesting.py but the flexibility is much greater. Actively maintained by the community (the original developer stepped back, but the project continues). Good choice for strategies that need realistic order management — stops, limits, brackets, OCO.

**NautilusTrader** ([nautilustrader.io](https://nautilustrader.io))
The current best option for production-first workflows. Written in Rust with Python bindings, so performance approaches compiled code while keeping the Python research interface. Specifically designed to bridge the research-to-production gap: the same strategy code that runs in the backtest runs in live trading with minimal modification. Supports full limit order book simulation, realistic latency, and multiple asset classes. Steep learning curve but the right choice if you are building something intended for deployment.

**QuantConnect / LEAN** ([quantconnect.com](https://www.quantconnect.com))
A cloud-based platform built on the open-source LEAN engine. The most complete end-to-end solution: data, backtesting, optimisation, paper trading, and live deployment in one environment. The research environment is Jupyter-based. The disadvantage is ecosystem dependency — you are building inside QuantConnect's infrastructure, which limits portability. The managed data (equities, futures, options, crypto, forex) is genuinely good and includes survivorship-bias-free equity data going back decades.

**Zipline-Reloaded** ([github.com/stefan-jansen/zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded))
The maintained fork of Quantopian's Zipline library. The Pipeline API is uniquely expressive for cross-sectional equity factor research — it allows you to define universe selection, factor computation, and portfolio construction in a clean, composable way. Best choice for factor model research that needs the Pipeline architecture. Not ideal for anything other than daily equity strategies.

**pysystemtrade** ([github.com/robcarver17/pysystemtrade](https://github.com/robcarver17/pysystemtrade))
Rob Carver's framework, developed alongside his book *Systematic Trading*. Specifically designed for systematic futures trading with a clear, principled approach to position sizing (instrument weights, forecast scaling, volatility targeting). The most complete open-source framework for systematic futures. The documentation is excellent.

### Comparison Summary

| Framework | Paradigm | Speed | Realism | Best For |
|-----------|----------|-------|---------|----------|
| VectorBT PRO | Vectorised | ★★★★★ | ★★★ | Parameter sweeps, signal research |
| backtesting.py | Vectorised | ★★★★ | ★★ | Quick prototyping |
| Backtrader | Event-driven | ★★★ | ★★★★ | Multi-asset, live trading |
| NautilusTrader | Event-driven | ★★★★ | ★★★★★ | Production deployment |
| QuantConnect | Event-driven | ★★★ | ★★★★ | End-to-end platform |
| Zipline-Reloaded | Event-driven | ★★ | ★★★ | Equity factor research |
| pysystemtrade | Event-driven | ★★★ | ★★★★ | Systematic futures |

---

## Part V — Data Sources

**Free and accessible:**

*Yahoo Finance* (via `yfinance`) — daily OHLCV for global equities, ETFs, indices, and FX. Survivorship-biased; does not include delisted stocks. Adequate for initial research on strategies with multi-week holding periods. Do not use for strategies that depend on the composition of specific indices.

*FRED* (Federal Reserve Economic Data, [fred.stlouisfed.org](https://fred.stlouisfed.org)) — macroeconomic time series including interest rates, inflation, employment, and economic activity. Essential for macroeconomic systematic strategies.

*Nasdaq Data Link* (formerly Quandl, [data.nasdaq.com](https://data.nasdaq.com)) — various free and premium datasets. The free Sharadar Core US Equities dataset is particularly useful — it includes point-in-time fundamental data (earnings, book value, cash flows) without survivorship bias.

*SEC EDGAR* ([sec.gov/edgar](https://www.sec.gov/edgar)) — all public company filings. The EDGAR full-text search API allows programmatic access. Source for 10-K and 10-Q data for fundamental strategies.

**Institutional quality (paid or academic access):**

*CRSP* (Center for Research in Security Prices) — the gold standard for US equity data. Includes all historical returns with delisting adjustments, survivorship-bias-free constituent histories, and dividend/split adjustments. Accessible through most universities.

*Compustat* — fundamental accounting data. Used alongside CRSP for academic factor research.

*Bloomberg Terminal* — the industry standard for market professionals. Comprehensive data across all asset classes. Very expensive; available at most financial institutions.

*Refinitiv (LSEG Data & Analytics)* — comparable to Bloomberg; used in many institutional research environments.

*Interactive Brokers Historical Data API* — if you have an IB account, the API provides historical data for equities, futures, options, and FX at moderate resolution. The best free institutional-quality data source for those with an account.

---

## Part VI — A Unified Framework: Work in Progress

The current state of the open-source backtesting ecosystem has a gap that becomes visible once you have worked with several of the available tools. The vectorised frameworks (VectorBT, backtesting.py) are fast but not realistic enough for final strategy validation. The event-driven frameworks (Backtrader, NautilusTrader) are realistic but either difficult to use or require significant infrastructure to set up. The end-to-end platforms (QuantConnect) are convenient but create ecosystem dependency. None of them has a clean, integrated solution for the full research pipeline: signal research → rigorous statistical validation → realistic backtesting → live deployment.

I am currently developing a unified backtesting framework — **QuantCore** — that attempts to address this gap with a dual-engine architecture. The framework is designed from the ground up around the principle that research integrity and computational efficiency are not in conflict; they require different components of the same system.

**The dual-engine architecture.** A vectorised engine for signal research and parameter optimisation — the stage where you need to run tens of thousands of parameter combinations quickly without caring about tick-level realism. And an event-driven engine for final validation and production staging — where every order is simulated with realistic fills, market impact, and latency.

**The key design principles:**

*Zero look-ahead bias by construction.* The data pipeline enforces strict temporal ordering. Signal generation has no access to data after the signal time. This is not a feature to be carefully configured — it is the default, with explicit opt-in required for any relaxation.

*Realistic transaction cost modelling.* Not a flat bps assumption but a proper market impact model: exchange fees, bid-ask spread simulation, and the square-root impact model calibrated to typical daily volume profiles.

*Statistical validation as a first-class component.* Walk-forward validation, combinatorial purged cross-validation (López de Prado), and multiple testing correction are built into the framework — not bolted on as external scripts.

*Research-to-production continuity.* The same strategy object that runs in the backtest runs in paper trading and live trading. Switching from historical data to a live data feed changes one line of configuration, not the strategy code.

The framework is in active development. When it is ready for public release, it will be published as open-source under the MIT licence. If you are interested in contributing or following the development, it will be available at [github.com/Vector-Pi/quantcore](https://github.com/Vector-Pi/quantcore) (not yet public — will be updated when the first stable version is ready).

The detailed technical specification of the architecture — the order management system, the market microstructure simulation, the risk framework, and the statistical validation pipeline — is documented internally and will be released alongside the code.

---

## Part VII — Learning Resources

### Books

*Quantitative Trading* — Ernest Chan
The most practical introduction to systematic trading research. Honest about the pitfalls of backtesting, clear on the Kelly criterion and position sizing, and specific enough to implement. The second edition (2021) updates the examples for current data sources.

*Advances in Financial Machine Learning* — Marcos López de Prado
The essential reference for anyone doing systematic research seriously. The chapters on combinatorial purged cross-validation, feature engineering for financial signals, and the deflated Sharpe ratio are the most important treatments of statistical methodology in systematic trading I have found.

*Systematic Trading* — Robert Carver
Principled, honest, and practical. Carver's framework for systematic futures trading — combining forecasts, scaling positions by volatility, and weighting instruments — is the most coherent presentation of a complete systematic methodology I have read. The companion pysystemtrade library implements it.

*Evidence-Based Technical Analysis* — David Aronson
A thorough treatment of statistical methodology for testing technical analysis claims. The chapters on hypothesis testing, the bootstrap, and the test of data-snooping are directly applicable to systematic strategy research.

*The Man from the Future: The Visionary Life of John von Neumann* — Ananyo Bhattacharya
Not a quantitative finance book. But understanding the history of Monte Carlo methods — invented at Los Alamos by von Neumann, Ulam, and Fermi to simulate neutron diffusion — gives the technique a different kind of clarity. Monte Carlo simulation in finance is the direct descendant of that work.

### Online Resources

**QuantStart** — [quantstart.com](https://www.quantstart.com)
Michael Halls-Moore's articles on systematic trading and backtesting methodology. The series on building an event-driven backtester from scratch in Python is the best tutorial on the subject I have found.

**Quantopian Lectures** (archived)
The Quantopian educational materials, now archived but still accessible. The lectures on factor analysis, risk management, and the correct interpretation of backtesting results are high quality.

**Quant Stackexchange** — [quant.stackexchange.com](https://quant.stackexchange.com)
The professional Q&A forum for quantitative finance. High signal-to-noise ratio. Useful for specific technical questions on model implementation and data handling.

**Lopez de Prado's papers on arXiv** — [arxiv.org/search/?query=lopez+de+prado](https://arxiv.org/search/?query=lopez+de+prado&searchtype=author)
His papers on the deflated Sharpe ratio, combinatorial purged cross-validation, and the false strategy theorem are essential reading. The false strategy theorem alone should be assigned to every person who has ever reported a backtested Sharpe ratio.

**Ernie Chan's blog** — [epchan.blogspot.com](http://epchan.blogspot.com)
Practical, honest, and frequently updated. The posts on mean reversion, cointegration, and the practicalities of live systematic trading are worth reading.

---

## A Note on Intellectual Honesty in Backtesting

The temptation in systematic research is to iterate on the backtest until it looks good and then report the result. This is the wrong way to do it, and the errors it produces are not small. A 10-year backtest optimised over 1,000 parameter combinations has an expected best Sharpe ratio of around 2.5 even if every tested strategy has zero true predictive power, purely from data mining.

The correct question to ask of any backtest is not "does this look good?" but "what is the minimum true Sharpe ratio consistent with this result, after accounting for all the tests I ran to get here?" If the answer is below 0.5, the strategy should probably not be traded.

This is not pessimism about systematic trading. Genuine predictive signals exist, and genuine systematic strategies have been built and sustained over decades. The point is that finding them requires the same rigour as finding any other genuine empirical result — which means being as hard on your own work as you would be on anyone else's.

---

*Last updated March 2026. The QuantCore framework section will be updated when the first stable version is publicly available.*