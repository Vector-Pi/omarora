---
title: "Cosmology & Astrophysics Notes"
date: 2026-02-14
parent: "Astronomy"
---


These are notes in the genuine sense — a working document, not a polished account. They are organised by topic and represent a synthesis of what I have read, worked through, and thought about across several years of studying cosmology alongside the theoretical physics. Where I have personal views or where there is genuine scientific controversy, I say so.

The connection between this page and my research is not accidental. The QGET framework — the approach to emergent spacetime from entanglement correlations described in my [research page](/theoretical-physics/my-research-publications/) — makes predictions about the early universe that should, eventually, be testable against CMB data. Understanding the observational cosmology side of that is part of the work.

The notes are organised as follows: the foundational framework (FRW cosmology, the Friedmann equations, the thermal history), the content of the universe (dark matter, dark energy, the cosmological constant problem), the physics of the early universe (inflation, baryogenesis, nucleosynthesis), structure formation, the observational landscape (CMB, BAO, gravitational waves), stellar and galactic astrophysics, and finally the current state of the field — what DESI is telling us, what the tensions in cosmology mean, and where the field is going.

---

## Part I — The Cosmological Framework

### The Cosmological Principle

Modern cosmology rests on the *cosmological principle*: on sufficiently large scales, the universe is homogeneous (the same everywhere) and isotropic (the same in all directions). This is not a logical necessity but an empirical observation — the CMB is uniform to one part in $10^5$, and galaxy surveys show homogeneity above scales of about 200 Mpc.

The cosmological principle constrains the geometry of spacetime to be described by the **Friedmann–Lemaître–Robertson–Walker (FRW) metric**:

$$ds^2 = -c^2 dt^2 + a(t)^2 \left[\frac{dr^2}{1-kr^2} + r^2 d\Omega^2\right]$$

where $a(t)$ is the **scale factor** (normalised to $a(t_0) = 1$ today), $k \in \{-1, 0, +1\}$ is the spatial curvature (open, flat, closed), and $d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2$ is the solid angle element.

The redshift $z$ of a photon emitted at time $t_e$ and observed today is:
$$1 + z = \frac{a(t_0)}{a(t_e)} = \frac{1}{a(t_e)}$$

This is the fundamental observable: the redshift tells you the scale factor at the time of emission.

---

### The Friedmann Equations

Inserting the FRW metric into the Einstein field equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ (with cosmological constant $\Lambda$) gives the two Friedmann equations:

$$\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}$$

$$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}\left(\rho + \frac{3p}{c^2}\right) + \frac{\Lambda c^2}{3}$$

The **Hubble parameter** $H(t) = \dot{a}/a$ measures the expansion rate. Today, $H_0 = H(t_0)$. The **density parameter** $\Omega\_i = \rho\_i / \rho\_{\text{crit}}$ for each component $i$, where the critical density $\rho\_{\text{crit}} = 3H^2/8\pi G$ is the density that gives flat spatial geometry.

**The equation of state** $w = p/\rho c^2$ determines how each component dilutes as the universe expands:
- Radiation: $w = 1/3$, so $\rho_r \propto a^{-4}$
- Matter (dust): $w = 0$, so $\rho_m \propto a^{-3}$
- Cosmological constant: $w = -1$, so $\rho\_\Lambda = \text{const}$
- Dark energy (general): $-1 \leq w \leq 1$ (observationally constrained by DESI and CMB)

The deceleration parameter $q = -\ddot{a}a/\dot{a}^2 = -1 - \dot{H}/H^2$ is positive (decelerating) in a matter-dominated universe and negative (accelerating) when $\Lambda$ dominates. The observed transition from deceleration to acceleration occurred at $z \approx 0.6$.

---

### The Thermal History of the Universe

The universe emerged from a hot, dense initial state and has been expanding and cooling ever since. The thermal history is a sequence of phase transitions as the temperature falls.

**$t \sim 10^{-43}$ s, $T \sim 10^{32}$ K — the Planck epoch.** Quantum gravitational effects are important. The energy density is Planck-scale. We have no reliable theory of what happened here.

**$t \sim 10^{-36}$ s — Inflation.** A brief period of exponential expansion driven by the potential energy of the inflaton field. Inflation explains: (1) the flatness of the observed universe ($\Omega\_\text{total} \approx 1$), (2) the horizon problem (why the CMB is uniform to $10^{-5}$ even in regions that were not causally connected in the standard picture), (3) the absence of magnetic monopoles, and (4) the generation of the primordial density perturbations that seeded structure formation.

**$t \sim 10^{-10}$ s, $T \sim 10^{15}$ K — Electroweak phase transition.** The Higgs field acquires a non-zero vacuum expectation value, spontaneously breaking the $SU(2)\_L \times U(1)\_Y$ gauge symmetry to $U(1)\_{\text{EM}}$. The $W$ and $Z$ bosons acquire mass. Baryogenesis may have occurred here.

**$t \sim 10^{-5}$ s, $T \sim 10^{12}$ K — QCD phase transition.** The quark-gluon plasma condenses into hadrons (protons, neutrons, pions). The strong force confines quarks into colour-neutral bound states. This is the transition that my Yang–Mills research is concerned with, at the level of the underlying mechanism.

**$t \sim 1$–$200$ s, $T \sim 10^9$ K — Big Bang Nucleosynthesis (BBN).** Protons and neutrons combine to form light nuclei: deuterium, helium-3, helium-4, and a small amount of lithium-7. The predicted abundance of $^4$He ($\approx 25\%$ by mass) and the deuterium-to-hydrogen ratio are among the most precise predictions of the Big Bang model, confirmed observationally to good precision.

**$t \sim 380{,}000$ years, $T \sim 3{,}000$ K — Recombination.** Electrons combine with nuclei to form neutral atoms. The universe becomes transparent: photons decouple from matter and free-stream to become the **Cosmic Microwave Background** (CMB). The surface of last scattering at $z \approx 1100$.

**$t \sim 100$–$500$ Myr — Cosmic dawn and Epoch of Reionisation.** The first stars and galaxies form (the precise epoch is an active area of research, now being probed by JWST). UV radiation from these first objects reionises the intergalactic medium.

**$t \sim 9$ Gyr, $z \approx 0.6$ — Dark energy domination.** The energy density of the cosmological constant begins to dominate over matter. The expansion transitions from decelerating to accelerating.

**$t = 13.8$ Gyr, $z = 0$ — Today.**

---

## Part II — The Content of the Universe

### The Standard Cosmological Model: $\Lambda$CDM

The standard model of cosmology — $\Lambda$CDM — describes the universe with six parameters: the Hubble constant $H_0$, the baryon density $\Omega\_b h^2$, the cold dark matter density $\Omega\_c h^2$, the optical depth to reionisation $\tau$, the amplitude $A_s$ and spectral index $n_s$ of the primordial power spectrum.

The current best-fit values from Planck 2018:
- $H_0 = 67.4 \pm 0.5$ km/s/Mpc
- $\Omega\_b h^2 = 0.02237 \pm 0.00015$
- $\Omega\_c h^2 = 0.1200 \pm 0.0012$
- $n_s = 0.965 \pm 0.004$

The energy budget of the universe today: $\sim 68\%$ dark energy, $\sim 27\%$ dark matter, $\sim 5\%$ baryonic matter, $\sim 0.01\%$ radiation.

---

### Dark Matter

**What it is (observationally).** Dark matter is a non-luminous, non-baryonic component of matter that interacts gravitationally and (by hypothesis) through the weak force, but not through electromagnetism or the strong force. The evidence for its existence is overwhelming:

- **Galaxy rotation curves.** Stars in the outer regions of spiral galaxies orbit at approximately constant velocity rather than falling off as $v \propto r^{-1/2}$ as Newtonian gravity would predict from the visible mass. The mass profile implied is $M(r) \propto r$, extending well beyond the visible disc — a dark matter halo.

- **Galaxy cluster dynamics.** Zwicky (1933) first noted that the velocity dispersion of galaxies in the Coma cluster was far too high to be explained by the visible mass. The mass inferred from dynamics exceeds the visible mass by a factor of several hundred.

- **Gravitational lensing.** The bending of light from background galaxies by galaxy clusters allows a direct mass measurement independent of dynamics. The mass maps from lensing consistently show extended dark matter halos.

- **The Bullet Cluster.** Two galaxy clusters passing through each other. The gas (which interacts and slows down) and the dark matter (which passes through) have separated. The mass concentration, measured by lensing, coincides with the dark matter, not the gas. This is the most direct evidence that dark matter is a separate component, not a modification of gravity.

- **CMB power spectrum.** The characteristic peaks in the CMB power spectrum depend on the ratio of baryonic to dark matter. The observed peak positions and heights are inconsistent with a universe containing only baryonic matter.

**What it might be.** The leading candidates are:

*WIMPs (Weakly Interacting Massive Particles)* — particles with mass $\sim 10$–$10^4$ GeV that interact through the weak force. The "WIMP miracle": a particle with weak-scale mass and coupling naturally gives the right relic density ($\Omega\_\text{DM} \approx 0.27$) if it was in thermal equilibrium in the early universe. WIMPs are strongly motivated by supersymmetry. However, direct detection experiments (XENON1T, PandaX, LZ) have now excluded large regions of parameter space.

*Axions* — very light pseudoscalar particles originally proposed to solve the strong CP problem. The QCD axion has a mass $\sim 10^{-5}$–$10^{-3}$ eV. Axion dark matter would behave as a coherent oscillating field rather than a gas of particles. Experiments including ADMX and HAYSTAC are searching for axion conversion to photons in a magnetic field.

*Primordial Black Holes (PBHs)* — black holes formed in the early universe before BBN. Their abundance is constrained by microlensing surveys (MACHO, EROS, HSC), CMB spectral distortions, and gravitational wave observations. They remain viable as a fraction of dark matter in specific mass windows.

*Sterile neutrinos* — right-handed neutrinos that mix with active neutrinos. They could be produced in the early universe through oscillations and contribute to the dark matter density.

---

### Dark Energy

**What it is (observationally).** Dark energy is the component driving the accelerated expansion of the universe, inferred from:

- Type Ia supernovae (Perlmutter, Schmidt, Riess 1998/1999, Nobel Prize 2011)
- CMB + BAO joint constraints
- The age of the universe (a flat matter-only universe would be younger than the oldest stars)

In $\Lambda$CDM, dark energy is the cosmological constant $\Lambda$ — a constant energy density of the vacuum. Its equation of state is exactly $w = -1$.

**The cosmological constant problem.** When you compute the vacuum energy expected from quantum field theory — the zero-point energies of all quantum fields — you get a number that is $10^{120}$ times larger than the observed value of $\Lambda$. This is the worst fine-tuning problem in physics: why is the cosmological constant so small?

This problem is genuinely unsolved. The most discussed approaches are:

*Anthropic selection* (Weinberg 1987, before the discovery of $\Lambda$): in a theory with a large landscape of vacua (string theory landscape), only vacua with sufficiently small $\Lambda$ allow structure formation and hence observers.

*Quintessence*: replace $\Lambda$ with a dynamical scalar field $\phi$ with potential $V(\phi)$ that rolls slowly to its minimum. The equation of state $w(z)$ evolves with redshift. This is the class of models now being tested by DESI.

*Modified gravity*: perhaps dark energy is not a matter component but a modification of gravity at cosmological scales. $f(R)$ gravity, scalar-tensor theories, and Horndeski theories are the main candidates.

---

### The DESI Results and the Fate of $\Lambda$CDM

This is the most active observational front in cosmology right now, and the results are genuinely surprising.

**DESI (Dark Energy Spectroscopic Instrument)** is a spectroscopic survey on the Mayall telescope at Kitt Peak, measuring the positions and redshifts of approximately 40 million galaxies and quasars. By measuring the **Baryon Acoustic Oscillation** (BAO) scale — a characteristic separation of $\sim 150$ Mpc imprinted by sound waves in the early universe — as a function of redshift, DESI maps the expansion history of the universe.

**DESI Data Release 1 (2024)** measured BAO across six galaxy and quasar samples spanning $0.1 < z < 4.2$. Combined with CMB and supernova data, the results suggested the dark energy equation of state $w$ is *not* equal to $-1$ — i.e., that dark energy might be dynamical. The tension with $\Lambda$CDM was at the $\sim 2.5\sigma$ level in the $w_0 w_a$ parameterisation (where $w(z) = w_0 + w_a z/(1+z)$).

**DESI Data Release 2 (March 2026)** extended the dataset to approximately 50 million tracers spanning $0.1 < z < 3.5$, achieving approximately twice the statistical precision of DR1. The evidence for evolving dark energy strengthened: using DESI DR2 BAO combined with CMB (ACT, SPT, Planck) and the Union3 supernova compilation, the preference for $w_0 > -1$ and $w_a < 0$ is now at approximately $3.5\sigma$, with best-fit values $w_0 \approx -0.7$ and $w_a \approx -1.1$.

This is not yet a 5$\sigma$ detection — the threshold for a "discovery" in physics — but it is the strongest evidence yet that the cosmological constant is not the correct description of dark energy. Whether this represents genuine new physics or a systematic effect in the data is a subject of active debate ([arXiv:2504.15222](https://arxiv.org/abs/2504.15222), Wang 2025).

**What this means if it holds.** If $w(z)$ is genuinely evolving with redshift, then:
- $\Lambda$CDM is not the final cosmological model
- Dark energy is not the vacuum energy but a dynamical field
- The fate of the universe is different: instead of exponential de Sitter expansion, the future depends on how $w(z)$ evolves
- The coincidence problem (why does $\Omega\_\Lambda \approx \Omega\_m$ today?) may have a dynamical explanation

**What to watch.** The next DESI data release, the Euclid mission (launched July 2023), the Vera C. Rubin Observatory (first light 2025), and the Nancy Grace Roman Space Telescope. All will provide independent and complementary constraints on $w(z)$.

---

## Part III — The Hubble Tension

The **Hubble tension** is the most significant observational anomaly in cosmology. It refers to the disagreement between:

- **Early-universe measurements** (CMB + $\Lambda$CDM): $H_0 = 67.4 \pm 0.5$ km/s/Mpc (Planck 2018)
- **Late-universe measurements** (distance ladder): $H_0 = 73.0 \pm 1.0$ km/s/Mpc (Riess et al., SH0ES team, Cepheids + Type Ia SNe)

The discrepancy is approximately $5\sigma$ when the latest calibrations are used. This is too large to be attributed to statistical fluctuation and has been confirmed by independent methods:

- TRGB (tip of the red giant branch): $H_0 = 69.8 \pm 2.1$ km/s/Mpc (Carnegie-Chicago Hubble Program) — between the two
- Gravitational lensing time delays (H0LiCOW): $H_0 = 73.3^{+1.7}_{-1.8}$ km/s/Mpc — consistent with SH0ES
- Gravitational wave standard sirens (LIGO GW170817): $H_0 = 70^{+12}_{-8}$ km/s/Mpc — consistent with both but too uncertain to discriminate
- Megamaser Cosmology Project: $H_0 = 73.9 \pm 3.0$ km/s/Mpc

The pattern is clear: direct local measurements consistently give $H_0 \approx 73$, while inferences based on the CMB and the early universe consistently give $H_0 \approx 67$.

**Proposed explanations** fall into three categories:

*Systematic errors in the distance ladder.* The Cepheid calibration might be wrong due to metallicity effects, crowding in dense stellar regions, or period-luminosity relation systematics. The JWST has been used to recalibrate the Cepheid distances (Riess et al. 2023), and the tension persisted after this recalibration.

*New physics before recombination* that reduces the sound horizon: early dark energy (a scalar field that contributes to the energy budget near matter-radiation equality, reducing the comoving sound horizon and thus shifting $H_0$ upward); extra relativistic species ($N\_{\text{eff}} > 3$); and modified neutrino physics.

*New physics after recombination* that modifies the late-time expansion history: interacting dark matter-dark energy, decaying dark matter, modified gravity. These generally make the $S_8$ tension worse.

No satisfying explanation has been found. The Hubble tension is the most important unsolved problem in observational cosmology.

**The $S\_8$ tension.** A related (and possibly connected) tension: the amplitude of matter fluctuations $S\_8 = \sigma\_8 \sqrt{\Omega\_m/0.3}$, where $\sigma\_8$ is the rms matter fluctuation in spheres of radius 8 Mpc/h, is measured to be lower in weak lensing surveys (KiDS, DES) than predicted by Planck + $\Lambda$CDM. The significance is $2$–$3\sigma$.

---

## Part IV — Inflation

Inflation was proposed by Alan Guth (1981) and developed by Linde, Starobinsky, and Albrecht–Steinhardt to solve the flatness, horizon, and monopole problems of standard Big Bang cosmology.

### The Mechanism

Inflation is a period of quasi-exponential expansion driven by the potential energy $V(\phi)$ of a slowly rolling scalar field (the inflaton) $\phi$. The **slow-roll conditions** require:
$$\epsilon = \frac{M\_\text{Pl}^2}{2}\left(\frac{V'}{V}\right)^2 \ll 1, \qquad \eta = M\_\text{Pl}^2 \frac{V''}{V} \ll 1$$

Inflation ends when $\epsilon \to 1$. During inflation, quantum fluctuations of the inflaton field are stretched to superhorizon scales and become classical density perturbations — the seeds of all structure in the universe.

### Primordial Power Spectra

The scalar perturbations generated during inflation have a nearly scale-invariant power spectrum:
$$P_s(k) = A_s \left(\frac{k}{k_*}\right)^{n_s - 1}$$

where $n_s < 1$ (red tilt) for most inflationary models. The Planck 2018 measurement gives $n_s = 0.965 \pm 0.004$, consistent with single-field slow-roll inflation.

Inflation also generates a background of primordial gravitational waves (tensor perturbations) with amplitude parameterised by the tensor-to-scalar ratio $r$. The current upper limit from Planck + BICEP/Keck is $r < 0.036$. CMB-S4 and LiteBIRD aim to reach $\sigma(r) \sim 10^{-3}$.

### Recent Developments

The combination of CMB data from Planck, ACT, and SPT with DESI DR2 BAO data has placed new constraints on inflation models. The Starobinsky $R^2$ inflation model — which predicts $n_s \approx 0.965$ and $r \approx 10^{-3}$ — remains the best-fitting model by most metrics, though it is now in mild tension with the DESI-shifted value of $n_s$ ([arXiv:2512.10613](https://arxiv.org/abs/2512.10613)). The results from the South Pole Telescope (SPT-3G) and the Atacama Cosmology Telescope (ACT DR6) have provided independent CMB measurements with their own $n_s$ constraints, and combining all CMB data gives $n_s = 0.9682 \pm 0.0032$.

---

## Part V — The Cosmic Microwave Background

The CMB is the thermal radiation left over from recombination, observed today at $T = 2.725$ K, redshifted by a factor of $(1+z_*) \approx 1100$. It is the most precisely measured cosmological observable.

### Temperature Anisotropies

The small temperature fluctuations $\delta T/T \sim 10^{-5}$ are decomposed in spherical harmonics:
$$\frac{\delta T}{T}(\hat{n}) = \sum_{\ell m} a_{\ell m} Y_{\ell m}(\hat{n})$$

The angular power spectrum $C\_\ell = \langle |a\_{\ell m}|^2 \rangle$ encodes all the cosmological information. The characteristic peaks in $C\_\ell$:

- **First acoustic peak** ($\ell \approx 220$, angular scale $\approx 1°$): the mode that completed exactly half an oscillation by recombination. The position encodes the angular diameter distance to the last scattering surface, and with BAO data, constrains $H_0$.
- **Second peak** ($\ell \approx 540$): the mode that completed a full oscillation. The ratio of the second to first peak constrains the baryon density $\Omega_b h^2$.
- **Third and higher peaks**: constrains the dark matter density $\Omega_c h^2$.

### CMB Polarisation

The CMB is partially polarised due to Thomson scattering near the last scattering surface. The polarisation is decomposed into E-modes and B-modes. E-modes are generated by scalar (density) perturbations and have been detected. B-modes are generated by tensor perturbations (primordial gravitational waves from inflation) and have not yet been detected at a significant level — their detection would confirm inflation and measure $r$.

### Resources on the CMB

- **Planck Collaboration papers** — [cosmos.esa.int/web/planck](https://www.cosmos.esa.int/web/planck/publications). The 2018 data release papers are the definitive reference.
- **Wayne Hu's CMB tutorial** — [background.uchicago.edu](http://background.uchicago.edu). The best online introduction to the physics of the CMB power spectrum.
- **Dodelson, *Modern Cosmology*** — the most complete textbook treatment of the CMB.

---

## Part VI — Structure Formation

How do the small primordial perturbations ($\delta\rho/\rho \sim 10^{-5}$) grow into the galaxies and large-scale structure we observe today?

### Linear Perturbation Theory

In the linear regime ($\delta\rho/\rho \ll 1$), density perturbations grow according to:
$$\ddot{\delta} + 2H\dot{\delta} = 4\pi G \bar{\rho}\delta$$

The solutions depend on the expansion history. In a matter-dominated universe: $\delta \propto a \propto t^{2/3}$ (growing mode) and $\delta \propto t^{-1}$ (decaying mode). The Hubble friction term $2H\dot{\delta}$ suppresses growth in a $\Lambda$-dominated universe — this is why structure formation has been slowing down since dark energy domination.

### The Matter Power Spectrum

The **matter power spectrum** $P(k) = |\delta_k|^2$ describes the amplitude of density fluctuations as a function of scale $k$. It is related to the primordial power spectrum through the **transfer function** $T(k)$, which encodes the effects of radiation pressure, Silk damping, and matter-radiation equality.

The shape of $P(k)$ encodes:
- The primordial spectral index $n_s$
- The horizon scale at matter-radiation equality (suppression of small-scale modes during radiation domination)
- The baryon-to-dark matter ratio (BAO wiggles)
- The neutrino mass (damping of small-scale structure due to free-streaming)

Large-scale structure surveys (DESI, Euclid, SDSS) measure $P(k)$ and compare to theoretical predictions to constrain cosmological parameters.

### The Cosmic Web

Dark matter halos form through gravitational collapse of overdense regions. The large-scale structure of the universe — the **cosmic web** — consists of filaments, sheets (walls), voids, and nodes (clusters). This structure was predicted by N-body simulations (Millennium Simulation, IllustrisTNG) and observed in galaxy redshift surveys.

**Baryon Acoustic Oscillations.** The same acoustic oscillations that produce the CMB peaks leave an imprint in the matter distribution: a preferred clustering scale of $\sim 150$ Mpc comoving. This scale — the **BAO scale** — serves as a standard ruler, allowing measurement of the angular diameter distance and Hubble parameter as a function of redshift. This is what DESI is measuring.

---

## Part VII — Stellar Astrophysics

### Stellar Structure

A star in hydrostatic equilibrium balances gravity against pressure. The equations of stellar structure:

$$\frac{dP}{dr} = -\frac{G M(r) \rho}{r^2} \qquad \text{(hydrostatic equilibrium)}$$

$$\frac{dM}{dr} = 4\pi r^2 \rho \qquad \text{(mass continuity)}$$

$$\frac{dL}{dr} = 4\pi r^2 \rho \epsilon \qquad \text{(energy generation)}$$

$$\frac{dT}{dr} = -\frac{3\kappa \rho L}{64\pi \sigma r^2 T^3} \qquad \text{(radiative transport)}$$

where $\epsilon$ is the energy generation rate per unit mass, $\kappa$ is the opacity, and $\sigma$ is the Stefan–Boltzmann constant.

### Nuclear Burning Stages

The energy source of a main-sequence star is hydrogen burning:

**pp chain** (dominant in low-mass stars like the Sun):
$$4p \to {^4\text{He}} + 2e^+ + 2\nu_e + 26.7 \text{ MeV}$$

**CNO cycle** (dominant in high-mass stars, $M > 1.5 M\_\odot$): carbon, nitrogen, and oxygen act as catalysts for the same net reaction. The CNO cycle has a steeper temperature dependence ($\propto T^{20}$ versus $\propto T^4$ for the pp chain), making massive stars far more luminous.

After hydrogen exhaustion on the main sequence, the helium core contracts and hydrogen burning continues in a shell — the star becomes a red giant. Helium burning (triple-alpha process: $3{^4\text{He}} \to {^{12}\text{C}} + 7.4 \text{ MeV}$) begins when the core temperature reaches $\sim 10^8$ K.

### Stellar Evolution and Endpoints

**Low-mass stars** ($M < 8 M_\odot$): After helium burning, the core becomes a **white dwarf** (supported by electron degeneracy pressure). The outer layers are expelled as a planetary nebula.

**High-mass stars** ($M > 8 M_\odot$): Burning continues through carbon, neon, oxygen, and silicon burning until an iron core forms. Iron is the most tightly bound nucleus — no further energy can be extracted by fusion. The iron core collapses in $\sim 0.1$ seconds to form a **neutron star** (supported by neutron degeneracy pressure and nuclear forces) and the outer layers are expelled in a **core-collapse supernova** (Type II/Ib/Ic).

**White dwarf $\to$ Type Ia supernova**: if a white dwarf in a binary system accretes enough mass to exceed the Chandrasekhar limit ($M\_{\text{Ch}} \approx 1.44 M\_\odot$), it undergoes thermonuclear runaway. Type Ia supernovae are standard candles (they have nearly uniform peak luminosity after correction) — they were used to discover the accelerating expansion of the universe.

**Neutron stars and pulsars**: neutron stars can be observed as pulsars — rotating neutron stars emitting beams of radio waves that sweep across the Earth. The Hulse–Taylor binary pulsar provided the first indirect evidence for gravitational wave emission (Nobel Prize 1993).

**Black holes**: if the collapsing core mass exceeds $\sim 3 M\_\odot$, no force can halt the collapse and a black hole forms.

---

## Part VIII — Gravitational Wave Astronomy

The detection of gravitational waves by LIGO on 14 September 2015 (GW150914 — the merger of two black holes of $\sim 36$ and $\sim 29 M_\odot$) opened a new observational window on the universe.

### Sources

**Binary black hole mergers (BBH)**: the most commonly detected source. LIGO-Virgo-KAGRA has detected $\sim 90$ confirmed events as of O3 (the third observing run). The masses range from stellar ($\sim 5$–$60 M\_\odot$) through intermediate mass.

**Binary neutron star mergers (BNS)**: GW170817 was the first detected BNS merger and was also observed electromagnetically in all wavelength bands (the first multi-messenger gravitational wave event). The simultaneous observation of the gravitational wave and gamma-ray burst showed that gravitational waves travel at the speed of light to within $\sim 10^{-15}$.

**Continuous gravitational waves**: not yet detected. Sources include rapidly rotating neutron stars with asymmetric mass distributions.

**Stochastic gravitational wave background**: a recent discovery. The pulsar timing array (PTA) experiments — NANOGrav, PPTA, EPTA — announced in 2023 the detection of a stochastic gravitational wave background with $f \sim 1$–$100$ nHz using millisecond pulsars as a galactic-scale gravitational wave detector. The source is likely supermassive black hole binaries.

### Gravitational Wave Cosmology

GW standard sirens offer an independent measurement of $H_0$ without using the distance ladder. The gravitational wave signal encodes the luminosity distance; if the host galaxy is identified and its redshift measured, $H_0$ can be inferred. GW170817 gave $H_0 = 70^{+12}_{-8}$ km/s/Mpc. With many future events (LIGO O5, Einstein Telescope, LISA), gravitational wave cosmology will become competitive with CMB and BAO measurements.

---

## Part IX — The James Webb Space Telescope

JWST, launched 25 December 2021 and operating from the Sun-Earth L2 point, is transforming observational cosmology and astrophysics. Some key results relevant to these notes:

**Early galaxy formation.** JWST has detected galaxies at $z > 10$ (less than 500 Myr after the Big Bang) that are far more massive and structured than standard $\Lambda$CDM simulations predicted. Several galaxies at $z \sim 12$–$16$ have been confirmed spectroscopically. Whether this represents a problem for $\Lambda$CDM or a failure of the baryonic physics models used in simulations is actively debated.

**First quasars.** JWST has discovered quasars at $z > 10$, hosting supermassive black holes of $\sim 10^7$–$10^8 M_\odot$. How black holes this massive formed within the first 500 Myr after the Big Bang is a significant theoretical challenge.

**Exoplanet atmospheres.** The transmission spectroscopy of exoplanet atmospheres by JWST — detecting molecular absorption features in the starlight filtered through the atmosphere — is producing the most detailed characterisations of exoplanet compositions to date.

---

## Resources

### Textbooks: A Calibrated Guide

**For first contact:**
- **Introduction to Cosmology** — Barbara Ryden. The most accessible quantitative introduction. Requires calculus but not GR. The equations are developed carefully from first principles. Perfect for a first serious encounter with the subject.
- **The First Three Minutes** — Steven Weinberg. The thermal history, explained by the man who helped write it. Short, readable, and still accurate in its broad picture.

**Undergraduate level:**
- **Cosmological Physics** — John Peacock. All of physics relevant to cosmology — which, as Peacock notes, is all of physics. Demanding but genuinely comprehensive. The treatment of large-scale structure and CMB physics is particularly good.
- **Introduction to Modern Astrophysics** — Carroll and Ostlie. The encyclopaedia of astrophysics. Stars, galaxies, cosmology, and everything in between, at undergraduate level. A reference that every astrophysicist has on their shelf.

**Graduate level:**
- **Modern Cosmology** — Scott Dodelson. The standard graduate cosmology text. Particularly strong on perturbation theory, the CMB, and the connections between observations and theory.
- **Cosmology** — Steven Weinberg. Weinberg's systematic treatment at graduate level. More mathematical than Dodelson, with more emphasis on the field theory foundations.
- **Physical Foundations of Cosmology** — Viatcheslav Mukhanov. Mukhanov developed inflationary perturbation theory; his book reflects this. The treatment of inflation and quantum fluctuations is the best available.
- **The Early Universe** — Kolb and Turner. The classic treatment of early-universe cosmology — baryogenesis, dark matter production, phase transitions. Somewhat dated in places but still the most complete treatment of thermal relics and freeze-out.
- **Principles of Physical Cosmology** — P.J.E. Peebles. A comprehensive treatment by one of the founding figures of modern cosmology. The writing is dense; the content is authoritative.

### Online Resources

**Wayne Hu's CMB pages** — [background.uchicago.edu](http://background.uchicago.edu). The best online introduction to CMB physics. The animations showing acoustic oscillations are conceptually invaluable.

**Sean Carroll's Cosmology lecture notes** — free at his website. Companion to *Spacetime and Geometry*, with more explicit cosmological applications.

**David Tong's Cosmology notes** — [damtp.cam.ac.uk/user/tong/cosmo.html](http://www.damtp.cam.ac.uk/user/tong/cosmo.html). The Cambridge Part III treatment. Covers the FRW metric, inflation, and CMB power spectrum carefully.

**Planck public data** — [pla.esac.esa.int](https://pla.esac.esa.int). All Planck data products, including maps and power spectra, are public.

**DESI public data** — [data.desi.lbl.gov](https://data.desi.lbl.gov). The DR1 and DR2 catalogues are public and available for analysis.

**NASA/IPAC Infrared Science Archive (IRSA)** — [irsa.ipac.caltech.edu](https://irsa.ipac.caltech.edu). Public data from NASA infrared and submillimeter missions including Spitzer, WISE, and Planck.

**Astrobites** — [astrobites.org](https://astrobites.org). Graduate students summarising recent astronomy papers for a broader audience. The best way to follow the field without reading every paper.

---

## A Personal Note

The subjects in these notes — the FRW metric, the thermal history, inflation — look, written down, like a list of established facts. They are not. Almost every paragraph contains an active research problem: the nature of dark matter, the equation of state of dark energy, the mechanism of inflation, the origin of the baryon asymmetry, the Hubble tension. The universe described by $\Lambda$CDM fits the data with extraordinary precision, and the $\Lambda$CDM parameters are known to percent-level precision. And yet the underlying physics of almost every component — what dark matter is, what dark energy is, why the cosmological constant has its observed value — is not understood.

The DESI DR2 results, released last year, are the clearest sign yet that $\Lambda$CDM may not be the final answer. Whether the evolving dark energy signal survives further scrutiny, and what it means if it does, is the most interesting question in observational cosmology right now.

The universe started it all, for me. A YouTube video about black holes in grade 6 during a lockdown. The fact that it is still surprising — that data is still coming in that challenges the models — is one of the things that keeps it compelling.

---

*Last updated March 2026.*