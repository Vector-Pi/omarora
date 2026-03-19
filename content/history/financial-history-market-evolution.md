---
title: "Financial History & Market Evolution"
date: 2026-02-06
parent: "History"
---

There is a standard way to write financial history: a sequence of manias and panics, each illustrating the irrationality of crowds. The tulip bubble, the South Sea Company, 1929, 1987, LTCM, 2008. The lesson is always the same — people get carried away, leverage accumulates, the crash comes — and the reader closes the book knowing that history repeats itself without knowing anything about why it repeats or what the structure of the repetition is.

That is not what this page is. The financial history worth understanding for someone doing quantitative research is not primarily the history of crises — though crises are important and I will cover them — but the history of markets as information-processing mechanisms: how prices are formed, how efficiently they aggregate dispersed information, how the arrival of systematic and algorithmic trading changed the ecology of the system, and what the long-run empirical record of factor premia tells us about the deep question of whether excess returns above the market are real, persistent, and explainable or artefacts of data mining and luck.

These are the questions that matter for the research I am doing. The topological fragmentation research asks whether the structure of the correlation network predicts future returns — which is a question about market efficiency, about the completeness of existing models, and about what kinds of information the market prices slowly rather than instantly. Understanding that question requires understanding how markets evolved.

---

## Part I — What a Financial Market Actually Is

Before the history, a clear statement of what we are tracing the history of.

A financial market is a mechanism for the allocation of capital across competing claims on future cash flows. A stock represents a claim on a fraction of a company's future earnings. A bond represents a claim on a scheduled sequence of payments. A derivative represents a claim contingent on the value of some underlying asset at a future date. The market price of each of these instruments is, in theory, the present value of the expected future cash flows, discounted at a rate that reflects the risk of the claim.

In theory. The extent to which this is true in practice — the extent to which prices efficiently reflect all available information — is the central empirical question of financial economics, and it is not settled.

**Markets as information-processing systems.** The deeper framing — more useful for quantitative research than the standard allocation framing — is that a financial market is a distributed computation. Thousands of participants with different information, different time horizons, different objectives, and different models are simultaneously buying and selling. The price is the output of this computation: a sufficient statistic for the collective beliefs and risk preferences of the participants. The question of market efficiency is the question of how good this computation is — how quickly and accurately it aggregates the dispersed information into prices.

This framing connects to my research because persistent homology applied to the correlation matrix of returns is asking about the structure of this computation: how correlated are the information sets being processed? How redundant are the connections in the network? When the network becomes densely cyclic — high TFI — it may be because the distributed computation has degenerated: everyone is processing the same information, so prices are moving together not because they should but because the diversity of the information-processing has collapsed. This is the microstructure basis for the TFI hypothesis.

---

## Part II — Origins: From Moneylenders to Exchanges

### The Ancient World

Credit — lending at interest — is older than coinage. Babylonian clay tablets from 2000 BCE record loans of grain and silver with interest. The Code of Hammurabi regulated loan terms. The fundamental financial contract — exchange of present value for future claim — is as old as settled agriculture.

The Greeks and Romans developed sophisticated credit markets. Roman *argentarii* (bankers) held deposits, made loans, and facilitated payments across the Mediterranean world. Cicero's letters are full of financial transactions — loans, property purchases, currency exchanges — conducted through a network of business contacts spanning the Roman world. The financial infrastructure of the empire was, in its essentials, recognisably modern.

What was missing was the tradeable security — a claim that could be bought and sold in a secondary market, whose price was determined by supply and demand rather than bilateral negotiation. This required a different institutional infrastructure.

### Amsterdam and the Birth of Modern Finance

The Amsterdam Stock Exchange, established in 1602 for trading shares of the Dutch East India Company (VOC), is the oldest joint-stock exchange in the world. It introduced three things simultaneously that define modern financial markets:

**The joint-stock company.** The VOC was owned by shareholders who could freely buy and sell their shares. Unlike a partnership, which dissolved when partners changed, the joint-stock company persisted independently of its owners. This was a legal innovation as important as the limited liability that came later: it allowed capital to be aggregated across many investors and deployed over time horizons that no individual could manage.

**The secondary market.** Shares traded continuously at prices set by supply and demand. The price reflected not just the current dividend but expectations about future dividends — the present value computation. Market price and book value could diverge, and the divergence was information.

**Derivative instruments.** By the 1630s, Amsterdam traders had developed options, futures, and short selling. The institutional infrastructure of modern derivatives markets was present in Amsterdam within three decades of the first stock exchange. The tulip mania of 1636–1637 — the archetype of all subsequent asset bubbles — involved not just spot tulip transactions but forward contracts and options on tulip bulbs, many of which were never planted.

The Amsterdam market was studied by Joseph de la Vega in his *Confusión de Confusiones* (1688) — the first book ever written about the stock market. De la Vega's description of the market ecology — the bulls, the bears, the arbitrageurs, the manipulators — reads as a sociology of financial markets that still applies. The participants, the incentives, and the strategies were established within a century of the exchange's founding.

### London and the 18th Century

The South Sea Bubble (1720) is the canonical 18th-century financial crisis. The South Sea Company had a near-monopoly on trade with South America and the right to manage the national debt. Its stock price rose from £128 to over £1,000 in eight months of 1720, then collapsed to £124 by year-end. The collapse ruined thousands, including Isaac Newton, who is reported to have said: "I can calculate the motion of heavenly bodies, but not the madness of people."

The structural feature that matters more than the mania: the South Sea Bubble occurred simultaneously with the Mississippi Bubble in France (John Law's scheme) and a broader European speculative episode. Bubbles in correlated assets, driven by credit expansion and optimistic expectations, collapse simultaneously. This is 1720 as a prototype of 2008 — the specific assets differ but the correlation structure of the crisis is the same.

**Lloyds of London** formalised insurance markets from 1688. The coffee houses of Exchange Alley in London became the primary venues for financial trading. By the late 18th century, the London market was the largest and most liquid in the world, trading government bonds (consols), equities, and commodities.

**The London Stock Exchange** formalised its rules in 1801. The NYSE was established in 1792 under the Buttonwood Agreement. By the end of the 18th century, the institutional infrastructure of modern equity markets was in place.

---

## Part III — The 19th Century: Industrialisation, Railroads, and the Bond Market

### Railroad Finance and the Capital Market

The railroad boom of the 1840s in Britain (the "Railway Mania") and of the 1860s–1880s in the United States was the first episode of large-scale industrial capital raising through public equity markets. The amounts involved were extraordinary by the standards of the time — the capital required to build a railroad network was beyond the capacity of any individual, any bank, or any government. Joint-stock equity markets were the mechanism.

The consequences for financial market structure were significant. The scale of railroad financing required the development of investment banking as a distinct activity — firms like J.P. Morgan (in the US) and Baring Brothers (in Britain) that could underwrite large bond issues, distribute them to investors, and provide certification of quality. The investment bank as intermediary between corporations seeking capital and investors seeking returns dates from this period.

The railroad bonds were also the foundation of modern credit analysis. Henry Poor began publishing his annual railroad statistics in 1860 — the precursor to what would become Moody's and Standard & Poor's. The systematic analysis of financial statements to assess creditworthiness is a 19th-century invention, driven by the need to evaluate railroad bond quality.

### Telegraphs and the First Information Revolution

The electric telegraph, deployed commercially from the 1840s, had an immediate and transformative effect on financial markets. Before the telegraph, price differences between geographically separated markets could persist for days or weeks — the time it took for price information to travel. After the telegraph, price differences between London and New York converged to the cost of an arbitrage trade plus the telegraph delay.

This is the first instance of a pattern that recurs throughout financial history: new information technology collapses geographic arbitrage opportunities, forcing market participants to find edge in better analysis or faster execution rather than in information proximity.

The stock ticker (1867, invented by Edward Calahan, improved by Edison) extended real-time price dissemination beyond the exchange floor to brokerage offices across the country. For the first time, investors remote from the exchange could observe current prices and trade on them. Market participation expanded dramatically.

The transatlantic telegraph cable (1866) connected European and American markets in real time. The arbitrage opportunities between the two largest capital markets in the world collapsed from days to minutes. It would take another century before they collapsed further — to microseconds.

---

## Part IV — The 20th Century: Theory Catches Up With Practice

### The Early 20th Century: Graham, Keynes, and the Seeds of Factor Investing

**Benjamin Graham** (1894–1976) developed the framework of value investing in *Security Analysis* (1934, with David Dodd) and *The Intelligent Investor* (1949). The core claim: stocks can be analysed rationally, their intrinsic value estimated from their earnings and assets, and stocks trading significantly below intrinsic value purchased with a "margin of safety."

Graham's framework is the ancestor of every value factor strategy. The statement "you are right not because the crowd agrees with you but because your data and reasoning are right" is both epistemological principle and trading philosophy. It is the first clear statement of the position that market prices can be wrong in systematic, identifiable ways.

**John Maynard Keynes** managed the endowment of King's College Cambridge (1927–1945) and achieved an average annual return of approximately 13.2% against the UK market's -0.1% — one of the most extraordinary long-run track records in the history of active management. He did it through a concentration in equities (unusual at the time), value-oriented stock selection, and global macro positions. He also lost 75% in the 1929 crash and then recovered. His letters to the College's investment committee are among the best documents on the psychology of long-term investing.

Keynes' analysis of speculation — the distinction between fundamental analysis (estimating intrinsic value) and speculation (estimating what the crowd will estimate) — is still the best description of market dynamics: "It is not a case of choosing those faces that, to the best of one's judgment, are really the prettiest, nor even those that average opinion genuinely thinks the prettiest. We have reached the third degree where we devote our intelligences to anticipating what average opinion expects the average opinion to be." The beauty contest metaphor captures something about price formation that no equilibrium model does.

### The 1950s: Markowitz and the Mathematical Turn

**Harry Markowitz** published "Portfolio Selection" in the *Journal of Finance* in 1952. The paper introduced mean-variance optimisation: the insight that the risk of a portfolio depends not on the individual risks of its components but on their covariances. A portfolio of individually risky assets can be much less risky than any of its components if the assets are sufficiently uncorrelated.

This is mathematically obvious once stated. The difficulty was that no one had stated it clearly, and the investment industry of 1952 was still selecting portfolios stock by stock rather than thinking about the covariance structure of the whole. Markowitz made the covariance matrix the central object of portfolio theory, and it has remained so.

The efficient frontier — the set of portfolios that maximise expected return for a given level of risk — gave investors a framework for thinking about the trade-off between return and risk that was quantitative rather than qualitative. The Nobel Prize came in 1990, delayed by decades because the industry was slow to adopt the mathematical framework.

**The Capital Asset Pricing Model** (Sharpe 1964, Lintner 1965, Mossin 1966) extended Markowitz to equilibrium: if all investors hold mean-variance efficient portfolios, the expected return of any asset is linear in its beta — its sensitivity to the market portfolio. $\mathbb{E}[R_i] = r_f + \beta_i(\mathbb{E}[R_m] - r_f)$. The market portfolio is the only source of systematic risk; diversifiable risk is not compensated.

The CAPM is probably wrong as a description of expected returns — the empirical evidence against it is substantial. But it established the framework that all subsequent asset pricing research operates within: what are the systematic risk factors, and what are the risk premia associated with them?

### The Efficient Market Hypothesis and Its Complications

**Eugene Fama** formalised the Efficient Market Hypothesis (EMH) in 1970: prices fully reflect all available information. Three forms:

- *Weak form*: prices reflect all historical price information. Technical analysis cannot generate excess returns.
- *Semi-strong form*: prices reflect all publicly available information. Fundamental analysis cannot generate excess returns.
- *Strong form*: prices reflect all information, including private. Even insiders cannot generate excess returns.

The strong form is false (insider trading generates returns; this is why it is illegal). The semi-strong form is approximately true for large-cap markets with high analyst coverage. The weak form is approximately true for liquid markets.

"Approximately" is doing a lot of work. The anomalies literature — the body of research documenting ways in which prices do not fully and immediately reflect information — began almost as soon as the EMH was formalised. The value premium (Basu 1977), the size premium (Banz 1981), the momentum effect (Jegadeesh and Titman 1993), the low-volatility anomaly — each was published as evidence against the EMH and prompted the debate that still continues: are these genuine excess returns, or are they compensation for unmeasured risk?

**The Grossman-Stiglitz paradox** (1980) put the EMH on more careful logical footing: if prices always fully reflect all available information, there is no incentive to gather information (because it is already in the price), so no one gathers information, so prices do not reflect information. The paradox implies that markets can only be *approximately* efficient — there must be enough mispricing to make information gathering worthwhile. The "right" level of efficiency is the level at which the marginal cost of information gathering equals the marginal return from trading on it.

---

## Part V — The Quantitative Revolution: 1960s–2000s

### Ed Thorp and the Kelly Criterion

**Ed Thorp** published *Beat the Dealer* (1962) — a card-counting system for blackjack — and then applied the same mathematical framework to financial markets. His paper "Beat the Market" (1967, with Sheen Kassouf) described the first systematic options pricing framework, derived independently of Black-Scholes and several years earlier. His hedge fund Princeton/Newport Partners (1969–1988) generated approximately 15.1% annualised net returns — the first great systematic trading fund.

Thorp's application of the **Kelly criterion** — the bet size that maximises the long-run growth rate of capital — to trading is the founding act of quantitative money management. The Kelly fraction $f^* = \mathbb{E}[R] / \sigma^2$ (for approximately normal returns) tells you the optimal position size given an edge and a variance. Full Kelly is theoretically optimal and practically dangerous; fractional Kelly is the standard in serious systematic trading.

The connection to information theory: the Kelly criterion maximises the expected logarithm of wealth, which is equivalent to maximising the rate of entropy reduction — the rate at which you extract information from the market. Thorp understood this explicitly; he had read Shannon and applied information theory to card games before applying it to markets.

### Fischer Black, Myron Scholes, and Robert Merton (1973)

The Black-Scholes-Merton option pricing formula is one of the most consequential mathematical results in the history of finance — not because it is correct (it is not, in a deep sense) but because it established a framework that made options markets possible at scale.

Before 1973, options were traded over-the-counter in illiquid, bilateral markets. The absence of a pricing formula meant no consensus on fair value, which meant wide bid-ask spreads and thin liquidity. The Black-Scholes formula provided a benchmark: a price derived from observable inputs (stock price, strike, time to expiry, risk-free rate, and volatility) under a specific set of assumptions. Once the benchmark existed, traders could quote around it — and the Chicago Board Options Exchange (CBOE) opened on April 26, 1973, the same year the formula was published.

**What the formula gets wrong.** The geometric Brownian motion assumption implies continuous sample paths (no jumps), log-normally distributed returns, and constant volatility. All three are wrong. Equity returns have fat tails; they occasionally jump; and implied volatility varies with strike (the volatility smile) in a way that is inconsistent with constant-vol GBM. Every subsequent development in options pricing theory — local volatility (Dupire 1994), Heston stochastic volatility (1993), rough volatility (Gatheral, Rosenbaum, Jaisson 2018) — is an attempt to fix one of these failures.

The volatility smile — the most important empirical fact in options markets — changed permanently after the 1987 crash. Before October 1987, the implied volatility surface was relatively flat across strikes. After October 1987, out-of-the-money puts consistently traded at higher implied volatility than at-the-money options — the market was permanently pricing in the possibility of a crash that Black-Scholes said should never happen. A single event changed the structure of implied volatility markets and it has not reverted.

### Renaissance Technologies and the Medallion Fund

**Jim Simons** founded Renaissance Technologies in 1982. The Medallion Fund, closed to outside investors since 1993, has generated gross returns of approximately 66% per year since 1988 — after the 5% management fee and 44% performance fee, net returns to investors were approximately 39% per year. This is the greatest investment track record in the history of finance, and it belongs to a fund staffed primarily by mathematicians, physicists, and computer scientists with no prior financial experience.

Simons is, personally, the figure I find most compelling in this entire history — and not primarily because of the returns. Before Renaissance, he was a research mathematician of genuine distinction. He worked on differential geometry and gauge theory in the 1960s and 1970s, and his collaboration with the physicist C.N. Yang produced the Chern-Simons form — a geometric object that appears in the study of topological invariants of three-manifolds and, unexpectedly, in Chern-Simons gauge theory, which became important in condensed matter physics and knot theory. The Chern-Simons term appears in the Lagrangian of topological field theories and plays a role in the description of the fractional quantum Hall effect. It is mathematics done at the frontier, and it was done by the same person who then built the most successful systematic trading operation in history.

The connection is not coincidental. Simons was trained to look for deep mathematical structure in problems, to distrust surface-level pattern recognition, and to demand rigorous validation before acting on an idea. These are the habits of a serious mathematician, and they turn out to be exactly the right habits for systematic trading research. The failure mode he avoided — the one that kills most systematic strategies — is the failure to distinguish genuine statistical signal from data-mining artefact. A mathematician who has spent years working on problems where being approximately right is not acceptable brings a different standard of evidence to strategy validation than someone trained primarily in finance.

This is the version of the physics-to-finance transfer I find most credible: not the naive application of physical models to financial data, but the transfer of intellectual habits — rigour, scepticism, comfort with abstraction, and the insistence on foundations — from one field to another. Simons did not apply gauge theory to markets. He applied the way of thinking that produces gauge theory to a different set of problems.

The Medallion Fund's performance is genuinely anomalous. A Sharpe ratio of approximately 2.0 over thirty-five years is extraordinarily unlikely under the null hypothesis that markets are efficient. The performance cannot be explained by known risk factors — the fund is uncorrelated with every standard factor and generates positive returns in almost every market condition.

What does Simons do? He does not say publicly. The academic literature offers several partial explanations: short-term mean reversion in equity prices (the bid-ask bounce); momentum at intermediate time horizons; complex cross-asset signals that individual markets cannot price correctly; and possibly signals derived from order flow and market microstructure that are visible only to participants with very sophisticated data infrastructure.

The most important lesson from Renaissance is not the specific signals but the methodology: hire the best quantitative talent, build the best data infrastructure, test rigorously, and maintain intellectual honesty about what is working and what is not. The fund runs thousands of signals simultaneously, each contributing a small, diversifiable increment of edge.

### The Birth of Statistical Arbitrage

**Statistical arbitrage** — exploiting statistical relationships between securities — developed at Morgan Stanley in the 1980s. Nunzio Tartaglia's quantitative group discovered that many equity pairs were cointegrated: their prices moved together in the long run even if they diverged in the short run. A long-short position that was long the relatively cheap stock and short the relatively expensive one generated returns as the spread mean-reverted.

The strategy worked well through the late 1980s and early 1990s. Then it became crowded. By the early 2000s, dozens of funds were running variations of the same pairs trading strategies on the same data. The **Quant Quake of August 2007** — a period of extreme, correlated losses across quantitative equity funds over several days in August 2007 — was the consequence of this crowding. When one fund was forced to liquidate, it sold exactly the positions that other funds also held, causing prices to move against every fund simultaneously. The correlation of strategies across the industry, invisible in normal times, became visible in the crisis.

The quant quake is directly relevant to the topological fragmentation research. The correlation between strategies — not just between assets — is a measure of the systemic risk embedded in the quant ecosystem. A market where many participants run similar strategies has a different topology than one where strategies are diverse. The TFI may be sensitive to this crowding effect.

### Long-Term Capital Management: Genius, Leverage, and Failure

**LTCM** (1994–2000) is the most instructive failure in the history of systematic trading. The fund was staffed by the most mathematically sophisticated team ever assembled in finance: Myron Scholes and Robert Merton (Nobel laureates), John Meriwether (the most successful bond arbitrageur of his generation), and a team of PhDs from the best universities. It generated returns of 21%, 43%, and 41% in its first three years.

The strategy was convergence arbitrage: identify pairs of instruments that should trade at the same price (or a stable spread) but currently trade at different prices, go long the cheap instrument and short the expensive one, and wait for convergence. In liquid, normal markets, this works — the statistical relationship is well-established and convergence is virtually certain.

The failure: the strategy required leverage to generate meaningful returns from small spreads. LTCM was running 25:1 balance sheet leverage at the time of its collapse. When the 1998 Russian default and subsequent market stress caused spreads to widen dramatically rather than converge — because every other leveraged fund also faced redemptions and was simultaneously selling the same positions — the strategy that was almost certain to work in the long run required capital that the fund no longer had. The short-run performance of the trade was exactly wrong; the long-run expectation remained correct; the leverage made the short-run move fatal.

The Federal Reserve coordinated a bailout by a consortium of fourteen banks, fearing that LTCM's unwind would cascade through the financial system. The fund was liquidated in 2000, and most of the trades that had been loss-making at the time of the bailout eventually converged — vindicating the fundamental analysis but not saving the fund.

The lesson: the Kelly criterion exists precisely to prevent LTCM-style ruin. The argument for leveraging was sound; the sizing was not. The question "what leverage is consistent with survival through a 3-sigma adverse move?" is the right question, and the answer implied a much smaller position than LTCM held. This is not a lesson about the failure of quantitative methods; it is a lesson about the failure to apply them fully.

---

## Part VI — The Fama-French Revolution and the Factor Zoo

### The Three-Factor Model (1993)

**Fama and French** demonstrated in 1992–1993 that the CAPM beta does not fully explain the cross-section of expected stock returns. Two additional factors — size (small-cap stocks earn more than large-cap stocks after risk adjustment) and value (high book-to-market stocks earn more than low book-to-market stocks) — explain a substantial portion of the variation in average returns that CAPM cannot.

The three-factor model:
$$R_i - R_f = \alpha_i + \beta_i(R_m - R_f) + s_i \cdot SMB + h_i \cdot HML + \varepsilon_i$$

where SMB (Small Minus Big) is the size factor return and HML (High Minus Low) is the value factor return.

The debate this created — and which continues — is about interpretation. Are these factors:
- **Risk factors** that earn a premium because they represent exposure to undiversifiable economic risk? (This is the efficient markets interpretation — the premia are fair compensation for risk.)
- **Behavioural anomalies** that persist because of investor irrationality — the tendency to overprice growth stocks and underprice distressed stocks? (This is the behavioural finance interpretation.)
- **Data mining artefacts** that appeared significant in the historical data but will decay after publication? (This is the sceptical interpretation.)

All three interpretations have empirical support. The value premium was very strong from 1926 to 2007 and has been much weaker since. Whether this represents decay after publication, a regime change driven by structural shifts in the economy (the rise of intangible assets), or random variation within a long-run premium that persists remains actively debated.

### Momentum (1993) and the Continuation of the Debate

**Jegadeesh and Titman** (1993) documented that stocks that have performed well over the past 6–12 months tend to continue performing well over the next 6–12 months — and vice versa. Momentum is the strongest and most pervasive factor in the empirical record, documented in virtually every asset class and every country with available data.

Momentum is deeply uncomfortable for the efficient markets hypothesis because it is explicitly a past-price effect. If prices fully reflect all available information, past price performance should have no predictive power for future returns — but it demonstrably does.

The explanations are multiple: under-reaction to news (investors update their views too slowly, so good news is incorporated gradually), investor herding and trend-following (prices overshoot and then revert), and risk-based explanations (momentum stocks may be riskier in specific ways). None is fully convincing.

The Fama-French **five-factor model** (2015) added profitability (RMW, Robust Minus Weak) and investment (CMA, Conservative Minus Aggressive) to the original three factors. Notably, it does not include momentum — Fama has repeatedly described momentum as a "premier anomaly" that does not fit neatly into a risk-based framework.

### The Factor Zoo and Replication Crisis

By 2018, a review by Harvey, Liu, and Zhu counted over 400 documented equity factors in the academic literature. **McLean and Pontiff** (2016) documented that the average factor premium declines by approximately 26% after academic publication — consistent with investors trading on the published factor and partially arbitraging it away.

This is the **replication crisis in finance**: a substantial fraction of documented anomalies may not survive out-of-sample or may be artefacts of data mining in relatively short historical datasets. The Bailey et al. minimum backtest length results I discussed on the backtesting page apply here too: with 400 tested factors, even random data would produce many apparently significant results.

The honest answer is that some factors are real and some are not, and distinguishing them is difficult. The factors with the most consistent empirical support across long time periods, multiple asset classes, and multiple geographic markets — value, momentum, low volatility, profitability — are most plausibly real. The 350 other factors in the zoo deserve more scepticism.

---

## Part VII — The Algorithmic Age: 1990s–Present

### High-Frequency Trading and the Microstructure Revolution

The Reg NMS rule in the US (2005) mandated that brokers obtain the best available price across all exchanges. One consequence was the fragmentation of equity markets into dozens of competing venues. Another was the creation of the environment that makes high-frequency trading (HFT) profitable: the same stock trades on multiple venues simultaneously, and the fastest participants can exploit the tiny price discrepancies between them.

High-frequency trading is not a single strategy. It encompasses market-making (continuously quoting bid and ask prices, earning the spread), statistical arbitrage at millisecond time horizons, latency arbitrage (being faster than other participants in responding to new information), and other strategies. The defining feature is speed: positions are held for microseconds to milliseconds, and the edge comes from information or execution advantages measured in fractions of a millisecond.

The **Flash Crash** of May 6, 2010 — when the Dow fell approximately 1,000 points in minutes and then recovered — exposed the fragility of a market dominated by algorithmic participants. A large sell order in E-mini S&P futures triggered a cascade of automated responses; market-making algorithms withdrew liquidity; prices fell to absurd levels (some stocks traded at $0.01) before recovering. The incident raised questions about whether a market that is individually rational at each participant level can be collectively unstable.

The microstructure literature since 2010 has focused on: the **adverse selection** problem (market makers are hurt by informed traders who know more about fair value than they do); **order book dynamics** (how the limit order book evolves and what information it contains); and **market impact** (how large orders move prices, and how to minimise this impact — the Almgren-Chriss optimal execution framework).

### The Machine Learning Wave

The systematic trading industry's adoption of machine learning follows a predictable pattern: the tools are powerful, the applications to financial data are non-trivial, and the failure modes are well-documented.

The specific challenges of applying machine learning to financial time series — discussed in detail on the [backtesting page](/omarora/quantitative-finance/resources-backtesting-tutorials/) — are: non-stationarity (the relationships between features and returns change over time), low signal-to-noise ratio (financial returns are mostly noise), look-ahead contamination (easy to introduce inadvertently in feature construction), and multiple testing (the number of features tested far exceeds the effective sample size).

**Two Sigma**, **D.E. Shaw**, and **Man AHL** have led the institutional adoption of machine learning in systematic trading, with the distinction that they apply it with the statistical rigour that the available evidence and the failure modes require. The hedge fund industry's record with machine learning is positive but not transformative — the improvement over well-constructed linear models has been real but modest.

**The crowding problem.** As more capital is allocated to systematic strategies using similar features and similar models, the signals decay. The correlation between systematic funds has increased substantially since 2010. The quant quake of August 2024 — a smaller version of the 2007 episode, driven by similar crowding dynamics in factor strategies — is evidence that the structural problem has not been solved.

### The Current Landscape and Open Questions

The financial markets of 2026 are qualitatively different from those of 1990 in several ways that matter for systematic research:

**Transaction costs have collapsed.** Commissions for retail trading are now zero in most retail platforms; institutional costs have declined from tens of basis points per trade to single digits. This is good for systematic strategies with high turnover and bad for any edge that exists because of frictions — the frictions that once protected systematic alpha from being arbitraged away are smaller.

**Data availability has exploded.** Alternative data — satellite imagery, credit card transaction data, web scraping, sentiment analysis — has expanded the information set available to systematic researchers. The extent to which this represents genuine new alpha or an arms race between well-resourced participants is unclear.

**The factor premium debate is live.** Value has underperformed dramatically since 2007. Momentum has worked in most periods but had catastrophic drawdowns in 2009 and 2020. Low volatility has outperformed but with significant sector concentration risks. Whether these are temporary regime-dependent phenomena or permanent changes in the structure of factor premia is the most important empirical question in asset pricing.

**Passive investing has grown dramatically.** Assets in passive index funds have grown from a small fraction of institutional investment to roughly half of total US equity fund assets. The implications for price discovery — whether passive investors degrade the informational efficiency of markets — are studied actively and unresolved.

---

## Part VIII — What This History Means for My Research

The financial history is not abstract background. It bears directly on the specific questions I am asking.

**The correlation network and crisis structure.** Every major financial crisis in this history — 1929, 1987, 1998 (LTCM), 2008, 2020 — involves the same structural pattern: correlations that are low in normal conditions spike to near-unity during stress. The network that is diverse and tree-like in calm conditions becomes densely cyclic as crisis approaches. The TFI is designed to detect exactly this transition. Understanding *why* it happens — the mechanism of correlation contagion through shared leverage, common factor exposure, and information cascade — is essential for understanding what the topological signal is actually measuring.

**The factor decay problem.** The decay of the value premium after 1992 publication, the crowding of statistical arbitrage strategies leading to the 2007 quant quake, and the broad compression of known factor premia since 2010 all point in the same direction: signals published in the academic literature are partially arbitraged away. The TFI signal, if it has predictive power, will face the same dynamic if it becomes widely known. This is an argument for publishing carefully and understanding the signal deeply before expecting it to persist.

**The information-processing framing.** The history of markets as information-processing systems — from the telegraph arbitrage of the 1860s through the electronic arbitrage of HFT — suggests that the persistent edges are those where the information being processed is not yet fully distributed or not yet fully understood. The topological structure of the correlation network is, by construction, a non-standard piece of information. It requires significant computational infrastructure to compute and interpret. Whether this is sufficient protection against rapid arbitrage is an empirical question.

**LTCM and leverage.** The LTCM failure is the clearest historical illustration of the Kelly criterion's practical importance. The strategies were correct; the leverage was wrong. This is the operative risk management lesson for any systematic strategy: the question "at what leverage does this strategy survive a 3-sigma move?" is more important than the question "what is the expected Sharpe ratio?"

---

*Last updated March 2026.*