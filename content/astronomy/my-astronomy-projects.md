---
title: "My Astronomy Projects"
date: 2026-02-06
parent: "Astronomy"
---

I want to give an honest account of this, including the parts where I did not know what I was doing.

Astronomy was the first thing I pursued seriously and independently. Before the physics, before the mathematics, before any research — there was just the sky and a curiosity about it that felt slightly unreasonable in its intensity. Grade 6, lockdown, Delhi. I have written about how that started in the [beginners guide](/astronomy/astronomy-for-beginners/). This page is about what I actually did with it.

The projects fall into three phases, roughly corresponding to the years since I started. The first phase is observational — learning the sky, tracking down objects, building the visual intuition that makes everything else more meaningful. The second phase is where the astronomy began to connect to the physics — understanding what I was seeing, not just finding it. The third phase, which is where most of my current work is, is computational: analysing data from space telescopes, working with Python and astropy, building pipelines for things that interest me.

I will describe each phase in detail.

---

## Phase 1 — Learning the Sky (2020–2021)

### The First Telescope

Late 2020. A 6-inch (150mm) f/8 Dobsonian reflector. This was a significant step up from binoscope in light-gathering power (the aperture went from 50mm to 150mm, a ninefold increase in light-collecting area) and gave magnifications useful for planets and double stars.

**What I learned from using a Dobsonian.** A Dobsonian has no motor drive. The Earth rotates, objects drift out of the eyepiece, and you push the telescope to follow them by hand. This is frustrating at first. It becomes useful, because it forces you to understand the geometry of the sky — how fast objects move at different declinations, what the relationship is between the direction you push and the direction things move, how to predict where an object will be in thirty seconds. It is the opposite of a GoTo mount, which does all of this for you and teaches you nothing.

### The Messier Catalogue

I spent most of 2021 working through the Messier catalogue — Charles Messier's 1781 list of 110 nebulae, star clusters, and galaxies. The goal was to observe all 110 objects, which I completed in February 2022.

Some observations from this project:

**M42 — Orion Nebula.** The trapezium at the centre — four hot young stars ionising the surrounding gas — is visible at 100× in a 6-inch as a tight quadruple star surrounded by a glowing cloud. The nebulosity extends well beyond the bright central region. This is an active star-forming region 1,344 light-years away; those four stars are less than a million years old.

**M13 — Great Globular Cluster in Hercules.** At 100×, a 6-inch resolves this into individual stars at the edges, with the core remaining a concentrated blur. At 150×, more stars resolve. A globular cluster contains $10^5$–$10^6$ stars in a sphere roughly 150 light-years across, bound together by gravity. The oldest globular clusters are 12–13 billion years old — nearly as old as the universe.

**M57 — Ring Nebula.** A planetary nebula — the expelled outer layers of a dying star, illuminated by the hot white dwarf at the centre. At 150× in the 6-inch it appears as a small, distinct ring, clearly different in structure from any star cluster. The central white dwarf (too faint to see in a 6-inch) is the remnant of a star that died approximately 6,000 years ago.

**The Messier Marathon.** In March 2022, near the spring equinox when all 110 Messier objects are above the horizon in a single night, I attempted to observe all of them between evening twilight and morning twilight. I managed 82 out of 110. The missed objects were either too close to the horizon in heavy atmospheric extinction (M74 and several others near the evening western horizon) or too faint for the light pollution I was observing from (a less-than-ideal site — I was not able to get to a truly dark location that night). The 82 is still the number that matters; the attempt forced me to know every one of those objects well enough to find it quickly without looking anything up.

---

## Phase 2 — Understanding What I Was Seeing (2021–2023)

This phase overlaps with the first. As I was observing, I was also reading — the physics of stars, stellar evolution, the mechanisms that produce the objects I was finding. The Hertzsprung–Russell diagram became a tool rather than a classification scheme when I started being able to locate specific objects on it. M13's stars are old red giants and main sequence stars; the Ring Nebula is a star that has left the main sequence and died; the Trapezium in M42 is so young it has not yet reached the main sequence.

### Variable Star Monitoring

I began making systematic observations of variable stars — stars whose brightness changes over time. I submitted observations to the American Association of Variable Star Observers (AAVSO, [aavso.org](https://www.aavso.org)) beginning in late 2021.

**What variable star observation involves.** You observe a variable star and estimate its magnitude by comparing it to nearby stars of known, constant magnitude. This requires careful attention to the comparison stars (provided on AAVSO finder charts), consistent observing technique, and honest error estimation. The AAVSO database contains observations from thousands of observers worldwide; your individual observation contributes to a long-term light curve.

**Stars I observed regularly:**

*Mira (ο Ceti)* — the prototype long-period variable. A red giant pulsating with a period of approximately 332 days and a range from magnitude 2 (easily naked-eye) to magnitude 10 (requiring a telescope). The mechanism is thermal pulses in the outer layers of the star as it oscillates between helium and hydrogen shell burning. I tracked Mira through one full cycle and part of a second.

*SS Cygni* — a dwarf nova: a binary system in which a white dwarf accretes gas from a companion star. Periodically, the accretion disc becomes unstable and there is a sudden increase in brightness (an outburst) of several magnitudes over a day or two. The AAVSO relies heavily on amateur observers to catch these outbursts as they begin, because the cadence required for early detection is higher than any professional telescope can provide to any single target.

*Eta Aquilae* — a Cepheid variable, pulsating with a well-defined period of 7.177 days. The period-luminosity relation for Cepheids — discovered by Henrietta Swan Leavitt in 1908 — was the tool that allowed Hubble to measure the distance to the Andromeda Galaxy and prove it was a separate galaxy. 
### Solar Observation

With appropriate solar filters (Baader AstroSolar film, which reduces the Sun's light by a factor of $10^5$), sunspot observation is safe and scientifically useful. I made regular sunspot drawings from 2021 through 2023, recording the sunspot number and the positions of sunspot groups.

This period corresponded to the rising phase of Solar Cycle 25 (which began at the December 2019 solar minimum). The increasing activity from 2021 onward was visible directly: the frequency of large sunspot groups increased, and the associated geomagnetic storms became more frequent. Solar Cycle 25 has been more active than predicted — the solar maximum of 2025 was significantly stronger than forecast, with high sunspot numbers exceeding the Cycle 24 maximum by a considerable margin.

**Sundial calibration.** A slightly weird project: I built an accurate sundial and calibrated it using my solar observations and the equation of time — the correction needed to convert apparent solar time (what a sundial reads) to mean solar time (what clocks read). The equation of time arises from two effects: the eccentricity of Earth's orbit (the Sun moves faster near perihelion in January) and the obliquity of the ecliptic (the Sun's path is tilted relative to the equator). Getting the equation of time curve right, including the asymmetric shape of the analemma, was more mathematically interesting than I expected and I ended up making a programme to calculate the correction factor daily and plot the analemma for any given latitude (which was the first in the ones I made specifically for astronomy).

---

## Phase 3 — Computational Work (2023–Present)

This is where most of my current astronomy work lives. The shift happened naturally: I had been learning Python for the mathematical research, and the tools for working with astronomical data — `astropy`, `lightkurve`, `numpy`, `matplotlib`, `scipy` — are the same stack. When I realised I could download actual data from space telescopes and analyse it myself, I found the intersection between the observational astronomy I had been doing and the quantitative work I was doing everywhere else.

What follows is a description of each computational project, with enough technical detail to be useful to someone who wants to do similar work.

---

### Project 1 — TESS Light Curve Analysis Pipeline

**What TESS is.** The Transiting Exoplanet Survey Satellite (TESS, launched April 2018) is a NASA mission that observes sectors of the sky continuously for 27 days at a time, measuring the brightness of millions of stars with two-minute or twenty-minute cadence. A transiting exoplanet causes a periodic dip in the star's light curve — a transit — as it passes in front of the stellar disc. TESS has discovered thousands of planet candidates (TOIs — TESS Objects of Interest).

**What I built.** A Python pipeline for downloading, detrending, and analysing TESS light curves, with a focus on identifying and characterising transit signals.

**The technical stack:**

```python
import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt
from astropy.timeseries import BoxLeastSquares
from astropy.stats import sigma_clipped_stats
import astropy.units as u
from scipy.signal import savgol_filter
```

**Step 1: Data acquisition.** The `lightkurve` package ([lightkurve.github.io](https://lightkurve.github.io/lightkurve/)) provides a clean interface to the MAST (Mikulski Archive for Space Telescopes) database:

```python
# Search data products for a target
search_result = lk.search_lightcurve('TIC 261136679', 
                                      mission='TESS',
                                      author='SPOC')
# Download all sectors
lc_collection = search_result.download_all()
# Stitch sectors
lc = lc_collection.stitch()
```

The `author='SPOC'` flag selects the Science Processing Operations Center pipeline products — the most carefully calibrated light curves. The PDCSAP (Pre-search Data Conditioned Simple Aperture Photometry) flux is the best starting point: it has been corrected for instrumental systematics by the SPOC pipeline but retains astrophysical variability.

**Step 2: Detrending.** Stellar variability — granulation, oscillations, starspots, activity cycles — produces low-frequency variations in the light curve that can obscure or mimic transit signals. Removing this systematically without removing the transit signal itself is a non-trivial problem.

I implemented two detrending approaches:

*Savitzky–Golay filter* — a polynomial smoothing filter applied with a window wider than the expected transit duration. The smoothed curve represents the stellar variability; subtracting it (or dividing the light curve by it) removes the long-term trends while preserving short-duration events:

```python
# Flatten the light curve using SG filter
# window_length should be > the transit duration in cadences
lc_flat = lc.flatten(window_length=401, polyorder=3)
```

*Gaussian Process (GP) regression* — a more principled approach that models the stellar variability as a stochastic process with a specified covariance kernel. The GP simultaneously fits the stellar variability and the transit signal, propagating uncertainties correctly. This is computationally more expensive but more accurate for active stars. I use `celerite2` ([celerite2.readthedocs.io](https://celerite2.readthedocs.io)) for GP detrending:

```python
import celerite2
import celerite2.terms as terms

# Stochastically-driven damped harmonic oscillator kernel
# models stellar granulation and p-mode oscillations
kernel = terms.SHOTerm(sigma=1.0, rho=1.0, tau=10.0)
gp = celerite2.GaussianProcess(kernel, mean=0.0)
gp.compute(time, diag=flux_err**2)
```

**Step 3: Transit search.** The Box Least Squares (BLS) algorithm searches for periodic box-shaped dips characteristic of transit signals:

```python
from astropy.timeseries import BoxLeastSquares

# Define period grid (logarithmic, from 0.5 to 30 days)
period_grid = np.exp(np.linspace(np.log(0.5), np.log(30), 50000))

bls = BoxLeastSquares(lc_flat.time.value, lc_flat.flux.value,
                      dy=lc_flat.flux_err.value)
bls_power = bls.power(period_grid, duration=0.1, oversample=20)

# Find the best period
best_period = bls_power.period[np.argmax(bls_power.power)]
best_t0 = bls_power.transit_time[np.argmax(bls_power.power)]
best_depth = bls_power.depth[np.argmax(bls_power.power)]
```

**Step 4: Phase folding and transit model fitting.** Once a candidate period is identified, fold the light curve at that period to stack all transits:

```python
# Fold the light curve at the best BLS period
folded = lc_flat.fold(period=best_period, epoch_time=best_t0)
folded_binned = folded.bin(time_bin_size=5*u.minute)
```

For transit model fitting, I use the `batman` package ([batman-package](https://github.com/lkreidberg/batman)):

```python
import batman

params = batman.TransitParams()
params.t0 = best_t0          # time of central transit
params.per = best_period      # orbital period (days)
params.rp = 0.05              # planet radius / stellar radius
params.a = 10.0               # semi-major axis / stellar radius
params.inc = 90.0             # orbital inclination (degrees)
params.ecc = 0.0              # eccentricity
params.w = 90.0               # longitude of periastron
params.u = [0.3, 0.2]         # limb darkening coefficients
params.limb_dark = "quadratic"

m = batman.TransitModel(params, time)
transit_model = m.light_curve(params)
```

**Step 5: Parameter estimation with MCMC.** Fit the transit model to the data using MCMC to obtain posterior distributions on the transit parameters — period, depth (which gives $R_p/R_*$), duration (which gives the impact parameter and semi-major axis):

```python
import emcee

def log_probability(theta):
    t0, period, rp, a, inc = theta
    # Prior bounds
    if not (best_t0-0.1 < t0 < best_t0+0.1): return -np.inf
    if not (best_period*0.9 < period < best_period*1.1): return -np.inf
    if not (0 < rp < 0.2): return -np.inf
    if not (2 < a < 50): return -np.inf
    if not (70 < inc < 90): return -np.inf
    
    # Update model
    params.t0, params.per = t0, period
    params.rp, params.a, params.inc = rp, a, inc
    model = m.light_curve(params)
    
    # Log likelihood
    residuals = flux - model
    return -0.5 * np.sum((residuals/flux_err)**2)

sampler = emcee.EnsembleSampler(32, 5, log_probability)
sampler.run_mcmc(initial_state, 2000, progress=True)
```

**What I have found with this pipeline.** I have processed light curves for several known planetary systems to validate the pipeline (WASP-126 b, Pi Mensae c, TOI-270 b/c/d) and recovered the known transit parameters to within the quoted uncertainties. For Pi Mensae c, which has a period of 6.27 days and a depth of approximately 700 ppm, the BLS recovery was clean and the MCMC posteriors were narrow and consistent with the Huang et al. (2018) published values.

The pipeline is available on my GitHub (link coming soon). It handles multi-sector TESS data, GP detrending, BLS search, and MCMC transit fitting.

---

### Project 2 — Exomoon Transit Timing Variation Analysis

**The scientific motivation.** No exomoon has been definitively confirmed. The best candidate remains Kepler-1625b-i (Teachey & Kipping 2018), a Neptune-sized moon candidate around a Jupiter-sized planet, detected in Hubble Space Telescope data. The result remains contested (Kreidberg et al. 2019 argued against it using independent Kepler analysis).

The indirect method I am most interested in is **Transit Timing Variations (TTVs)**. A moon orbiting a transiting planet causes the planet to wobble around the planet-moon barycentre. This wobble shifts the time of each transit — the planet transits slightly early when the moon is in front of it (planet displaced toward us) and slightly late when the moon is behind it. The amplitude of the TTV caused by a moon is:

$$\delta t \approx \frac{M_m}{M_p + M_m} \cdot \frac{a_m}{v_p}$$

where $M_m$ is the moon mass, $M_p$ is the planet mass, $a_m$ is the planet-moon separation, and $v_p$ is the planet's orbital velocity. For an Earth-mass moon around a Jupiter at 1 AU, $\delta t \sim 10$–$100$ seconds — at the edge of TESS's timing precision for bright stars.

**What I am building.** A TTV extraction pipeline that:

1. Fits individual transit times for a known TESS planet across all available sectors
2. Computes the Observed minus Calculated (O-C) diagram — the difference between the observed transit time and the predicted linear ephemeris
3. Searches for periodic signals in the O-C diagram consistent with the TTV signature of a moon
4. Estimates the sensitivity: for a given planet-star system and TESS noise level, what moon masses and separations are detectable?

**The individual transit fitting.** For each transit event, I fit the transit model independently (rather than folding all transits together) to extract the central transit time $t_c$ and its uncertainty $\sigma_{t_c}$:

```python
def fit_single_transit(time_segment, flux_segment, flux_err_segment,
                       period, rp, a, inc, u1, u2):
    """
    Fit a single transit to extract central transit time.
    Returns: t0_fit, t0_err
    """
    from scipy.optimize import minimize
    
    def neg_log_like(t0):
        params.t0 = t0
        model = batman.TransitModel(params, time_segment)
        lc = model.light_curve(params)
        return 0.5 * np.sum(((flux_segment - lc) / flux_err_segment)**2)
    
    result = minimize(neg_log_like, x0=[np.median(time_segment)],
                     method='Nelder-Mead',
                     options={'xatol': 1e-6, 'fatol': 1e-8})
    
    # Estimate uncertainty from curvature of likelihood
    from scipy.optimize import approx_fprime
    hess = approx_fprime([result.x[0]], 
                          lambda t: neg_log_like(t[0]),
                          1e-6)
    t0_err = 1.0 / np.sqrt(hess[0])
    
    return result.x[0], t0_err
```

**The O-C analysis.** With individual transit times $\{t_i\}$ and uncertainties $\{\sigma_i\}$, compute the best-fit linear ephemeris:

$$t_i^\text{calc} = T_0 + n_i \cdot P$$

where $n_i$ is the transit epoch number. The residuals $O_i - C_i = t_i - t_i^\text{calc}$ are the TTVs. Searching for a periodic signal in these residuals using a Lomb-Scargle periodogram:

```python
from astropy.timeseries import LombScargle

# O-C residuals
epochs = np.round((transit_times - T0) / period).astype(int)
t_calc = T0 + epochs * period
O_minus_C = transit_times - t_calc  # in days, convert to minutes
O_minus_C_min = O_minus_C * 24 * 60
sigma_min = sigma_tc * 24 * 60

ls = LombScargle(transit_times, O_minus_C_min, dy=sigma_min)
frequency, power = ls.autopower(minimum_frequency=1/max_period,
                                 maximum_frequency=1/min_period,
                                 samples_per_peak=50)
# Best TTV period
best_ttv_period = 1.0 / frequency[np.argmax(power)]
false_alarm_prob = ls.false_alarm_probability(power.max())
```

**Current status.** I have the pipeline working for simulated data (I inject synthetic TTV signals with known amplitude and period and recover them) and have validated it on WASP-18b (a known null result — WASP-18b has consistent transit times with no significant TTV, as expected for a hot Jupiter with no nearby perturbers).

The next step is to apply the pipeline to a sample of TESS planets with many observed transits and good photometric precision to place upper limits on moon masses as a function of the moon's orbital separation — a population-level constraint rather than a detection in any individual system. This is work in progress.

---

### Project 3 — CMB Power Spectrum Analysis with Planck Public Data

**The motivation.** The connection between the QGET framework (from the [research page](/theoretical-physics/my-research-publications/)) and observational cosmology runs through the CMB. QGET predicts that entanglement structure at the origin of spacetime might leave signatures in the primordial power spectrum — specifically, a modified spectral tilt $n_s$ or non-Gaussianity in the temperature anisotropies.

Developing intuition for what the CMB data actually looks like — not just reading about it in textbooks, but handling the maps and extracting the power spectrum — was a prerequisite for thinking seriously about what predictions QGET could make.

**The Planck data.** The European Space Agency's Planck satellite observed the CMB from 2009 to 2013. All data products are public at [pla.esac.esa.int](https://pla.esac.esa.int), including the HEALPix temperature and polarisation maps at various resolutions and frequency bands.

**Working with HEALPix maps.** The CMB temperature maps are stored in the HEALPix pixelisation scheme ([healpix.sourceforge.net](https://healpix.sourceforge.net)), which divides the sphere into equal-area pixels. The Python package `healpy` provides the interface:

```python
import healpy as hp
import numpy as np
import matplotlib.pyplot as plt

# Load Planck 2018 SMICA map (component-separated temperature map)
# NSIDE=2048 gives ~1.7 arcmin pixel resolution
mapfile = 'COM_CMB_IQU-smica_2048_R3.00_full.fits'
cmb_map, header = hp.read_map(mapfile, h=True, verbose=False)

# View the map in Mollweide projection
hp.mollview(cmb_map, 
            title='Planck 2018 SMICA CMB Temperature Map',
            unit='K',
            cmap='RdBu_r',
            min=-300e-6, max=300e-6)
hp.graticule()
plt.show()
```

**Power spectrum extraction.** The angular power spectrum $C_\ell$ quantifies the variance of CMB temperature fluctuations as a function of angular scale $\ell$ (where $\ell \sim 180°/\theta$):

```python
# Compute angular power spectrum using HEALPix anafast
# Apply the Galactic mask to avoid contamination from the Milky Way
mask_file = 'HFI_Mask_GalPlane-apo0_2048_R2.00.fits'
mask = hp.read_map(mask_file, field=4)  # 80% sky fraction mask
f_sky = mask.mean()  # sky fraction used

# Apply mask
masked_map = cmb_map * mask

# Compute spectrum
cls = hp.anafast(masked_map, lmax=2000)
ells = np.arange(len(cls))

# Correct for mask (approximate)
cls_corrected = cls / f_sky

# Plot the TT power spectrum
D_ell = ells * (ells + 1) * cls_corrected / (2 * np.pi)
plt.figure(figsize=(12, 6))
plt.plot(ells[2:], D_ell[2:] * 1e12, 'b-', linewidth=0.5, alpha=0.7)
plt.xlabel(r'Multipole moment $\ell$')
plt.ylabel(r'$\ell(\ell+1)C_\ell/2\pi$ $[\mu K^2]$')
plt.title('CMB Temperature Angular Power Spectrum (Planck 2018)')
plt.xscale('log')
plt.show()
```

The peaks in $D_\ell$ — at $\ell \approx 220$, $540$, $800$, $1100$ — are the acoustic oscillations in the primordial plasma, frozen into the CMB at recombination. The position and height of each peak constrains the cosmological parameters. The first peak position gives the angular diameter distance to the last scattering surface (constraining the spatial geometry); the ratio of the second to first peak constrains the baryon density; the amplitude of the third and higher peaks constrains the dark matter density.

**What I have done with this.** Reproduced the Planck 2018 power spectrum from the raw data, verified the acoustic peak positions, and compared them to the CAMB ([camb.info](https://camb.info)) theoretical predictions for the best-fit $\Lambda$CDM parameters. The agreement between the theory and data is extraordinary — the $\Lambda$CDM model fits the CMB power spectrum to better than one percent across the full multipole range.

The next step, which I am currently working on, is computing what modifications to the primordial power spectrum the QGET framework would predict, and whether these are within the sensitivity of current or planned CMB experiments (CMB-S4, LiteBIRD).

---

### Project 4 — Variable Star Light Curve Classification

**The motivation.** Variable stars exhibit a wide range of light curve morphologies — the smooth sinusoidal variation of Cepheids and RR Lyrae, the sudden outbursts of dwarf novae, the gradual deepening of long-period Miras, the sharp eclipses of binary stars. Classifying these automatically from light curve data is a machine learning problem with direct scientific application (the AAVSO data, the ASAS-SN survey, and the upcoming Vera Rubin Observatory / LSST will produce millions of variable star light curves that cannot be classified by hand).

**What I built.** A classifier using features extracted from TESS and AAVSO light curves. The feature set includes: period (from Lomb-Scargle periodogram), amplitude, phase-folded light curve shape descriptors (skewness, kurtosis, Fourier coefficients), and the ratio of the fundamental period to the first harmonic.

```python
from astropy.timeseries import LombScargle
from scipy.stats import skew, kurtosis
import numpy as np

def extract_features(time, flux, flux_err=None):
    """Extract features for variable star classification."""
    # Lomb-Scargle period
    ls = LombScargle(time, flux, dy=flux_err)
    freq, power = ls.autopower(minimum_frequency=1/200, 
                               maximum_frequency=2.0,
                               samples_per_peak=10)
    best_freq = freq[np.argmax(power)]
    best_period = 1.0 / best_freq
    
    # Phase-fold at best period
    phase = ((time - time[0]) % best_period) / best_period
    sort_idx = np.argsort(phase)
    folded_flux = flux[sort_idx]
    
    # Shape features of phase-folded light curve
    amplitude = np.percentile(flux, 95) - np.percentile(flux, 5)
    lc_skew = skew(folded_flux)
    lc_kurt = kurtosis(folded_flux)
    
    # Fourier decomposition: fit first 3 harmonics
    phases_rad = 2 * np.pi * phase
    A = np.column_stack([
        np.ones_like(phase),
        np.cos(phases_rad), np.sin(phases_rad),
        np.cos(2*phases_rad), np.sin(2*phases_rad),
        np.cos(3*phases_rad), np.sin(3*phases_rad)
    ])
    coeffs, _, _, _ = np.linalg.lstsq(A, flux, rcond=None)
    R21 = np.sqrt(coeffs[3]**2 + coeffs[4]**2) / np.sqrt(coeffs[1]**2 + coeffs[2]**2)
    
    return {
        'period': best_period,
        'amplitude': amplitude,
        'skewness': lc_skew,
        'kurtosis': lc_kurt,
        'R21': R21,
        'ls_power': power.max()
    }
```

I trained a random forest classifier on a labelled dataset of AAVSO variable stars (Cepheids, RR Lyrae, Miras, SR variables, eclipsing binaries, dwarf novae) with known types, using the features above. The classification accuracy on the test set was approximately 89%, with the main confusion between Cepheids and RR Lyrae (similar period ranges) and between semi-regular (SR) and Mira variables (similar morphology).

This project is ongoing. The classifier is functional; the next steps are adding more feature types (slope of the period-luminosity relation, colour indices if available) and testing it on TESS Full Frame Image (FFI) data where the variable star type is unknown.

---

## Tools, Libraries, and Data Sources

**Python packages I use regularly:**

| Package | Purpose |
|---------|---------|
| `lightkurve` | TESS/Kepler data access and analysis |
| `astropy` | Core astronomy tools: units, coordinates, FITS I/O, BLS |
| `healpy` | HEALPix CMB map manipulation |
| `batman` | Transit light curve modelling |
| `emcee` | MCMC posterior sampling |
| `celerite2` | Gaussian process regression for light curve detrending |
| `scipy` | Optimisation, signal processing, statistics |
| `numpy` / `matplotlib` | Array operations and plotting |
| `astroquery` | Interface to online astronomical databases (SIMBAD, NED, MAST) |

**Data sources I have worked with:**

- **MAST** ([mast.stsci.edu](https://mast.stsci.edu)) — Mikulski Archive for Space Telescopes. All TESS and Kepler data.
- **Planck Legacy Archive** ([pla.esac.esa.int](https://pla.esac.esa.int)) — CMB maps, power spectra, and catalogues.
- **AAVSO International Database** ([aavso.org/data-download](https://www.aavso.org/data-download)) — variable star light curves.
- **SIMBAD** ([simbad.u-strasbg.fr](http://simbad.u-strasbg.fr)) — stellar parameters, coordinates, catalogue cross-matches.
- **ExoFOP-TESS** ([exofop.ipac.caltech.edu/tess](https://exofop.ipac.caltech.edu/tess)) — community follow-up observations of TESS planet candidates.
- **NASA Exoplanet Archive** ([exoplanetarchive.ipac.caltech.edu](https://exoplanetarchive.ipac.caltech.edu)) — confirmed exoplanet parameters.

---

## What Comes Next

The TESS TTV pipeline will be applied to a systematic sample of known TESS planets. The goal is not detection of a specific exomoon but characterisation of the population-level sensitivity: what moon masses, at what orbital separations, can be excluded for what fraction of observed systems? This would be a scientifically useful result independent of any individual detection.

The CMB work depends on the QGET theoretical development. Once the classical limit and the primordial power spectrum prediction are formalised, comparing to Planck data is the natural immediate test.

The variable star classifier is something I would eventually like to run on a large sample of TESS FFI data. The Vera Rubin Observatory begins science operations in 2025 and will produce approximately 10 million variable star light curves in the first data release. Having a working, validated classifier ready before that data arrives is the motivation.

---

*Last updated March 2026. Active projects are updated as they develop.*