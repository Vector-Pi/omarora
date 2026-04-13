---
title: "Research in Market Microstructure"
date: 2026-04-13
parent: "Quantitative Finance"
description: "Topological data analysis applied to equity markets. Using persistent homology and network theory to detect market regimes and microstructure patterns."
---


This page describes my active research in quantitative finance. It is more detailed than the [trading projects page](/quantitative-finance/trading-projects/) because this is research rather than deployed strategy — the ideas are at a stage where describing them publicly is appropriate, and where engaging with the literature and with potential collaborators is valuable.

The work sits at the intersection of topological data analysis, network theory, and systematic equity research. The central question is whether the geometric and topological structure of equity correlation networks contains information about future stock returns that is not captured by conventional factors. The short answer, based on what I have found so far, appears to be yes — though the extent to which this translates into an exploitable trading signal after costs is the question still being investigated.

A point to note is that I have not been working in quantitative finance for very long, and most of whatever I have done either as apart of my research or any other project, I have used US equities data only.

The Econophysics Review paper is available [here](https://doi.org/10.5281/zenodo.19552994)  

---

## Part I — Background and Motivation

### The Decay of Conventional Factors

The academic factor zoo has expanded significantly over the past two decades. By some counts, more than 400 distinct equity factors have been published in the finance literature. Many of these factors have experienced substantial decay since their publication — the act of discovery, dissemination, and subsequent trading by systematic investors has eroded the premia they once captured.

The three canonical equity factors — value, momentum, and quality — remain meaningful but are heavily harvested. The Sharpe ratio of a pure momentum strategy in US large-cap equities has declined substantially since the 1990s. Understanding why some factor premia persist while others decay is one of the central empirical questions in asset pricing.

This creates a genuine incentive to look for orthogonal sources of alpha — signals derived from different aspects of market structure than the conventional price-based and fundamental-based factors. Topological data analysis offers one such direction: it extracts information from the *shape* of the correlation network, which is invisible to the standard scalar metrics (average pairwise correlation, market beta, volatility).

### Why Topology?

Standard correlation-based analysis of equity markets captures pairwise relationships between stocks. The correlation matrix $C$ encodes, for each pair $(i,j)$, the linear co-movement of their returns. But a correlation matrix has a complex internal structure that is not fully captured by looking at individual entries or simple aggregates (average correlation, maximum eigenvalue).

Persistent homology is a tool from algebraic topology that characterises the *multi-scale topological structure* of a dataset — the connected components ($H_0$), loops and cycles ($H_1$), voids and cavities ($H_2$) — as a function of a filtration parameter. Applied to a correlation distance matrix, it reveals how the network of equity correlations is connected, how many redundant cycles it contains, and how this structure changes over time.

The physical intuition: in a calm, diversified market, the correlation network is relatively tree-like (low cycle count — stocks are connected but not redundantly so). In a stressed market approaching a crash, the network becomes more densely cyclic — correlations spike uniformly, every pair of assets is connected to every other pair through multiple paths, and the network topology changes in a characteristic way. Persistent homology quantifies this change.

---

## Part II — The Topological Fragmentation Index

### Construction

**Step 1: Rolling correlation matrix.** For each day $t$, compute the Pearson correlation matrix $C_t$ of log returns over a rolling window of $L = 60$ trading days:

$$C_t^{ij} = \frac{\sum_{\tau=t-L+1}^{t} r_i^\tau r_j^\tau}{\sqrt{\sum_\tau (r_i^\tau)^2 \sum_\tau (r_j^\tau)^2}}$$

**Step 2: Correlation distance.** Convert to a metric space using the standard transformation:

$$d_{ij,t} = \sqrt{2(1 - C_t^{ij})} \in [0, 2]$$

This satisfies the triangle inequality (Mantegna 1999) and maps perfectly correlated pairs to distance 0 and perfectly anti-correlated pairs to distance 2.

**Step 3: Vietoris-Rips filtration.** For each threshold $\epsilon \in [0, 2]$, build the Vietoris-Rips complex $\text{VR}_\epsilon(D_t)$: the simplicial complex whose $k$-simplices are sets of $k+1$ assets with pairwise distance $\leq \epsilon$. As $\epsilon$ increases from 0 to 2, the complex grows from a collection of isolated points to a fully connected structure.

**Step 4: Persistent homology.** Compute the persistent homology groups $H_k$ of the filtration for $k = 0, 1, 2$. Each homology class $\alpha$ is born at some $\epsilon_\text{birth}$ and dies at some $\epsilon_\text{death}$. The **persistence** of class $\alpha$ is $\text{pers}(\alpha) = \epsilon_\text{death} - \epsilon_\text{birth}$.

The **Betti curve** $\beta_k(\epsilon) = $ number of $k$-dimensional homology classes alive at threshold $\epsilon$ captures the topological structure at each scale.

**Step 5: Topological Fragmentation Index.** The TFI is defined as the total persistence of 1-dimensional cycles ($H_1$) integrated over the filtration:

$$TFI_t = \int_{\epsilon_{min}}^{\epsilon_{max}} \beta_1(\epsilon) \, d\epsilon = \sum_{\alpha \in H_1} pers(\alpha)$$

High TFI: many persistent 1-cycles, meaning the correlation network has many redundant loops across multiple scales — a characteristic of stressed, highly-correlated markets where every cluster of stocks is densely interconnected. Low TFI: few cycles, tree-like structure, low correlation.

Additional topological features extracted alongside TFI:

**Persistence entropy** for each dimension $k$:
$$E_k = -\sum_\alpha p_\alpha \log p_\alpha, \quad p_\alpha = \frac{\text{pers}(\alpha)}{\sum_\beta \text{pers}(\beta)}$$

**Betti-0 total persistence:** captures the fragmentation of the network into separate components as a function of the distance threshold.

**Spectral Fiedler value:** the second-smallest eigenvalue of the graph Laplacian $L = D - A$ of the correlation network at a fixed threshold. Measures algebraic connectivity — how easy it is to disconnect the graph.

---

## Part III — The Predictive Framework

### Cross-Sectional Stock-Level Sensitivity

The insight that transforms TFI from a market-level indicator to a cross-sectional alpha factor is the observation that individual stocks differ in their sensitivity to TFI changes.

For each stock $i$ at time $t$, compute the rolling correlation between the stock's return and the change in TFI over the past $K = 20$ days:

$$Sens_{i,t} = corr_{K}\left(r_{i,\tau}, \, \Delta TFI_\tau\right)_{\tau = t-K+1}^{t}$$

A stock with high positive sensitivity tends to rise when market fragmentation increases — it benefits from, or is robust to, increasing market stress. A stock with negative sensitivity tends to fall when fragmentation increases.

The hypothesis is that this sensitivity contains information about future returns: stocks that are positively sensitive to fragmentation increases may be priced differently than the market implies, because the market does not fully incorporate the topological signal.

### Portfolio Construction

A long-short portfolio is constructed by ranking stocks within the S&P 500 universe on their sensitivity score at each rebalancing date, going long the top quintile and short the bottom quintile. The portfolio is:

- **Dollar-neutral** (equal dollar value long and short)
- **Factor-neutral** (hedged against market beta, size, value, momentum, and low-volatility factors using a linear regression on contemporaneous factor returns)
- **Sector-neutral** (equal allocation within each GICS sector, long and short)

The factor and sector neutrality are essential for isolating the topological signal from known sources of return variation. A strategy that looks like TFI alpha but is entirely explained by market beta or momentum is not a new factor.

### Statistical Validation Protocol

**Walk-forward validation.** The data is split into a training period (first 60%) and an out-of-sample test period (last 40%). The sensitivity computation uses only past data; no future information enters the signal construction. This is the minimum standard for avoiding look-ahead bias.

**Fama-MacBeth cross-sectional regressions.** At each cross-section date $t$, regress next-period stock returns on lagged TFI sensitivity and control variables:

$$r_{i,t+1} = \alpha_t + \gamma_t \, Sens_{i,t} + \beta_t^M MktBeta_{i,t} + \beta_t^S Size_{i,t} + \beta_t^V Value_{i,t} + \beta_t^M Mom_{i,t} + \varepsilon_{i,t+1}$$

The time-series mean of $\gamma_t$ (with Newey-West standard errors) tests whether TFI sensitivity carries a risk premium after controlling for known factors.

**Combinatorial purged cross-validation** (following López de Prado 2018). Standard $k$-fold cross-validation produces inflated performance estimates in financial time series because train and test folds share overlapping observations. CPCV purges the training set of observations that overlap with the test fold and embargoes adjacent observations. This is the correct procedure for time series with serial dependence.

**Multiple testing correction.** I tested multiple candidate topological features (TFI using $H_1$, Betti-0 total persistence, Fiedler value, persistence entropy $E_0$, $E_1$) before finding the ones with the strongest signal. The Bonferroni correction and the Benjamini-Hochberg procedure are applied to account for multiple testing. Claiming statistical significance on the best of five tested features at $p < 0.05$ requires correcting for the family-wise error rate.

---

## Part IV — Connection to the Hyperbolic Geometry of Financial Networks

The most theoretically interesting result in this area is recent. Caputi, Pidnebesna, and Hlinka (2025) showed that the integral Betti signatures of financial (stock market), brain, and climate networks exhibit a hyperbolic character — their topological features lie between Euclidean and hyperbolic geometry of small curvature, distinctly different from random matrices or spherically-structured matrices.

This is a remarkable finding with direct implications for the TFI framework. Hyperbolic geometry is the geometry of negative curvature — the geometry of the Poincaré disc and the hyperbolic plane. A network with hyperbolic geometry has a characteristic hierarchical structure: a small number of highly-connected hub nodes and a large number of peripheral nodes, with distances growing exponentially from the core. This is exactly the structure of equity correlation networks during normal market conditions.

Earlier work on the hyperbolic geometry of financial networks (Kitsak et al. 2021) demonstrated that networks of European banks could be well-represented by hyperbolic geometry of negative curvature, with the latent dimensions of the Poincaré disc model corresponding to systemic importance and geographic subdivisions.

**The connection to TFI.** If the correlation network has hyperbolic geometry in normal conditions, then a transition away from hyperbolic geometry — toward a more Euclidean or spherical structure, where all nodes become equally central — is a signature of the breakdown of the hierarchical market structure that characterises non-crisis conditions. The TFI, by measuring the total persistence of $H_1$ cycles, is sensitive to exactly this transition: hyperbolic networks have few long-lived cycles (the network is tree-like at most scales), while Euclidean or spherical networks have more.

This gives a geometric interpretation of TFI changes: an increasing TFI signals a transition from hyperbolic to more isotropic geometry, corresponding to the breakdown of sector and industry structure as correlations converge. This is the geometry of contagion.

**Implications for the alpha model.** If market structure is hyperbolic in equilibrium and periodic transitions toward spherical geometry (crises) are predictable from TFI, then stocks that are positioned advantageously in the hyperbolic network — near the periphery, far from the hubs, with low geodesic centrality — should outperform during transitions. Testing whether topological position in the hyperbolic embedding of the correlation network predicts cross-sectional returns is a natural extension of the current work.

---

## Part V — Literature Context

The TDA finance literature divides cleanly into two generations. The first generation focused on crisis detection:

Gidea (2017) developed a TDA-based method to detect early signs of critical transitions in financial data, building time-dependent correlation networks and computing persistent homology to track topological changes as prices approached the 2007-2008 financial crisis.

Gidea and Katz (2018) used persistence homology to detect topological patterns in multidimensional time series during the technology crash of 2000 and the financial crisis of 2007-2009, finding that $L^p$-norms of persistence landscapes exhibit strong growth prior to primary peaks during crashes.

Ruiz-Ortiz et al. (2022) proposed a persistent-homology-based turbulence index tested on the S&P 500, Russell 2000, and other indices across multiple crash events including Black Monday, the dot-com crash, 2007-08, and COVID-19.

The gap the TFI research aims to fill is identified clearly in the document I wrote for this project: existing TDA finance papers demonstrate that persistent homology can flag impending crashes or measure market turbulence, but they stop at detection. None has translated topological signatures into a tradeable cross-sectional factor with rigorous out-of-sample testing and transaction cost analysis. This is the contribution the current work aims to make.

A 2025 paper from MDPI extended the Gidea-Katz methodology with a strictly causal pipeline, applying Vietoris-Rips persistent homology to four major US equity indices over 1999-2021 and achieving detection of two of four canonical crises with a lead time of approximately 34 days. This is a more recent point in the first-generation literature; the second generation — turning topological features into systematic cross-sectional alpha — remains largely unoccupied.

---

## Part VI — Current Status and Open Questions

### What I Have Found

The preliminary empirical findings on the S&P 500 from 2015–2025:

**TFI dynamics are consistent with the prior literature.** TFI spikes during market stress events (March 2020, Q4 2018, Q1 2022) and declines during calm trending markets. The dynamics are intuitive and statistically consistent across different window lengths ($L \in \{30, 60, 90\}$ days).

**The Fiedler value provides complementary information.** The algebraic connectivity of the correlation network declines before major volatility events, with different lead times than TFI. The combination of TFI and the Fiedler value as joint predictors outperforms either alone in preliminary cross-sectional regressions.

**Cross-sectional sensitivity is heterogeneous.** Stocks in defensive sectors (utilities, consumer staples, healthcare) tend to have positive TFI sensitivity — they are relative winners when market fragmentation increases. Stocks in cyclical sectors (energy, materials, financials) tend to have negative sensitivity. This sectoral pattern is partly mechanical (defensive stocks correlate positively with flight-to-quality during crises) but is not fully explained by standard sector dummies.

**The signal is statistically significant in-sample but the out-of-sample picture is more complex.** The Fama-MacBeth $t$-statistic for the TFI sensitivity premium is above 2 in the full sample, but the subsample stability is not as strong as I would like — the signal is stronger in volatile regimes and weaker in low-volatility trending markets. This is a genuine concern about regime-dependence that requires further investigation.

### Open Questions I Am Working On

**Does the signal survive costs?** Preliminary analysis suggests yes at moderate turnover, but the transaction cost model matters significantly. A 10 bps one-way cost assumption gives a positive after-cost Sharpe; a 20 bps assumption makes it marginal. The correct cost assumption depends on implementation quality.

**What is the right topological feature?** TFI (total $H_1$ persistence), Betti-0 total persistence, persistence entropy, Fiedler value, and the integral Betti signature all contain related but distinct information. Finding the combination that maximises out-of-sample predictive power without overfitting the feature selection is a careful statistical problem.

**Is the geometry story testable?** If the hyperbolic geometry interpretation is correct, then a stock's position in the hyperbolic embedding of the correlation network (its hyperbolic centrality) should predict its sensitivity to TFI changes. Testing this requires implementing a hyperbolic embedding algorithm (hydra+ or Mercator) on the rolling correlation network and measuring whether hyperbolic centrality correlates with subsequent TFI sensitivity. This is the most technically demanding part of the research.

**What is the holding period?** The current implementation uses a daily sensitivity score and monthly rebalancing. Shorter rebalancing (weekly) may improve the signal but increase costs; longer rebalancing (quarterly) reduces turnover but may miss regime changes. The optimal holding period is an empirical question.

---

## Part VII — Mathematical Tools

The implementation requires tools from several areas:

**Persistent homology.** Computed using `giotto-tda` (Python) or `GUDHI`. The computational cost of Vietoris-Rips persistence on a 500-node graph is non-trivial — $O(n^3)$ for the persistence algorithm in the worst case. In practice, I use the `ripser` library which implements the Bauer (2021) algorithm and is significantly faster.

**Spectral graph theory.** The graph Laplacian $L = D - A$ is a sparse symmetric matrix. The Fiedler value (second-smallest eigenvalue) is computed using `scipy.sparse.linalg.eigsh` with the shift-invert method, which is efficient for sparse matrices.

**Factor model neutralisation.** The Barra-style factor exposure matrix is estimated by OLS regression of stock returns on factor returns over a rolling window. The residuals (specific returns) provide factor-neutral return series for testing the topological signal.

**Minimum spanning tree.** Computed using `scipy.sparse.csgraph.minimum_spanning_tree` on the distance matrix. The MST topology (degree distribution, diameter, clustering coefficient) provides additional features alongside the persistent homology.

---

## Connections to Physics

The mathematical infrastructure for this work comes directly from the physics background. Persistent homology is the same tool used in topological data analysis of physical systems — it has been applied to materials science (structure of glasses and amorphous solids), biology (protein folding, neural connectivity), and cosmology (large-scale structure of the universe). The Vietoris-Rips complex is formally identical to the Čech complex used in computational geometry.

The graph Laplacian is the discrete analogue of the Laplace-Beltrami operator from Riemannian geometry — the same operator that appears in the diffusion equation, the Schrödinger equation in curved space, and the heat kernel on a manifold. The Fiedler value is the discrete analogue of the spectral gap of the Laplacian, which controls the mixing time of random walks on the graph and the rate of information propagation through the network.

The hyperbolic geometry of financial networks connects directly to the anti-de Sitter space that appears in the AdS/CFT correspondence in string theory: hyperbolic space $\mathbb{H}^n$ with constant negative curvature $-1$ is the Euclidean version of anti-de Sitter space. The Poincaré disc model of hyperbolic geometry, used in the financial network embedding, is the same model that appears in the study of bulk reconstruction in AdS/CFT. This is a connection I find genuinely interesting, though it is currently more mathematical poetry than a working physical analogy.

---

## Plans

The immediate plan is to complete the out-of-sample validation and write up the results as a paper. The timeline is approximately six months for the full empirical analysis and another three months for writing and revision.

The longer-term direction is to develop the hyperbolic geometry connection further — specifically, whether the hyperbolic centrality of an equity in the correlation network is a stable characteristic that predicts its behaviour across multiple market regimes. This is closer to pure financial economics research than to systematic trading, and is the kind of question that could support a more academic-facing paper.

---

*Last updated March 2026. Active research; this page will be updated as the work develops.*
