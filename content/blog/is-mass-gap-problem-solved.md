---
title: "Has the Yang-Mills Mass Gap Been Solved? On the Nye Paper and What It Actually Claims"
date: 2026-04-22
tags: ["Research", "Yang-Mills", "Mass Gap", "Millennium Prize", "Physics", "Quantum Information", "Open Problems"]
description: "Every time I mention I am working on the Yang-Mills mass gap problem, someone tells me it has been solved. Here is a careful reading of the paper they are usually referring to — what the approach is, what it does and does not establish, and why I think the problem is harder than any current paper resolves."
---

Every time I tell someone I am working on the Yang-Mills mass gap problem, I get the same response.

"Hasn't that been solved?"

Sometimes it comes with a link. The most common one right now leads to Logan Nye's paper "Existence and Mass Gap in Quantum Yang-Mills Theory," published in the *International Journal of Topology* in February 2025. The paper is titled as if the problem is settled. The abstract says it presents a complete solution. It has been circulating in popular science discussions as evidence that the Clay Millennium Prize is about to be awarded.

I have read the paper carefully. This post is my honest account of what it does, where it is interesting, and why the mass gap problem is not yet solved, at least not in a way that will satisfy the Clay criteria or the mathematical physics community.

But I want to say something first about why I am writing this, and what my position on the mass gap actually is.

---

## My Relationship to This Problem

I have written before about why I work on the Yang-Mills mass gap [here](https://omarora.in/blog/whyyangmills/) and [here](https://omarora.in/blog/whatismassgapproblem/), and in more technical detail on the [open problems page](https://omarora.in/theoretical-physics/open-problems-im-exploring/).

The honest version: I was never trying to solve the mass gap. I am a high school student. The mass gap has resisted the best mathematical physicists of the twentieth century. I took it on as a long-term direction precisely because it is difficult enough that sustained engagement with it teaches you something real, and because the Clay problem sits at the intersection of mathematics and physics in a way I find genuinely compelling.

What I published — the [Stueckelberg extension](https://doi.org/10.5281/zenodo.19057338)  is a perturbative result. It establishes a gauge-invariant mass generation mechanism at tree level and verifies that asymptotic freedom is preserved at one loop. It is not a solution to the mass gap problem. It is a contribution to the programme of approaches.

When I hear that the problem has been solved, my reaction is not defensive. It is careful. I want to understand exactly what the claim is and whether it meets the standard. The standard is precise and demanding, and most things that get labelled "mass gap solved" do not meet it.

The Nye paper is the most mathematically substantive of the recent claims. So lets walk through it properly.

---

## What the Mass Gap Problem Actually Requires

Before reading any claimed solution, you need to know exactly what you are grading it against. The Clay Mathematics Institute's official problem statement, written by Arthur Jaffe and Edward Witten, asks for two things:

**Existence.** Prove that for any compact simple gauge group $G$, a quantum Yang-Mills theory on $\mathbb{R}^4$ exists as a mathematically well-defined object satisfying the Wightman axioms (or their Euclidean equivalents, the Osterwalder-Schrader axioms). This means:

- The theory is not just a formal perturbative expansion but a rigorously defined quantum field theory
- The correlation functions are tempered distributions satisfying specific analyticity, covariance, and positivity conditions
- The Hilbert space of physical states is well-defined

**Mass gap.** Prove that there exists a $\Delta > 0$ such that the energy of every state except the vacuum satisfies $E \geq \Delta$. In other words, the spectrum of the Hamiltonian has a gap between the vacuum (zero energy) and the first excited state.

The difficulty: both of these need to be proved in the full non-perturbative theory on the continuum $\mathbb{R}^4$. A lattice result is not sufficient. A perturbative result is not sufficient. A rigorous result in $2+1$ dimensions is not sufficient. The problem is specifically about the four-dimensional continuum quantum theory.

With that standard in hand, here is what Nye claims to do.

---

## The Nye Paper: The Strategy

The paper's central idea is to reformulate Yang-Mills theory in the language of quantum information. Specifically, it represents the lattice Yang-Mills theory as a quantum circuit and then claims to take the continuum limit.

The approach has three main components, which I will go through in order.

### Component 1: The Quantum Circuit Representation

Nye starts with the lattice Yang-Mills theory — the Wilson action on a hypercubic lattice — and represents it as a quantum circuit. Each link of the lattice carries a group-valued variable $U_{x,\mu} \in G$, and the Hilbert space of the lattice theory is

$$\mathcal{H}_\Lambda = \bigotimes_{(x,\mu)} L^2(G)$$

This is standard lattice gauge theory. The new move is to represent the transfer matrix

$$T = e^{-aH} = e^{-a(H_E + H_B)}$$

using a Trotter decomposition: split the exponential into alternating electric and magnetic parts and approximate the product as a quantum circuit. Nye uses the second-order Trotter formula

$$e^{t(A+B)} = \lim_{n\to\infty} \left(e^{tA/2n} e^{tB/n} e^{tA/2n}\right)^n$$

and establishes an error bound on this approximation. This part is mathematically standard. The Trotter formula is well-understood and the error bound Nye derives — of order $C a^3 n^{-2} V/a^4$ — is a straightforward calculation.

The quantum circuit representation gives a concrete way to think about the lattice theory in terms of quantum computation. It is a useful reformulation but does not by itself establish the continuum limit.

### Component 2: The Continuum Limit

This is where the paper's main claim lives, and where the difficulties are most serious.

Nye defines renormalized correlation functions

$$G^R_a(x_1, \ldots, x_n) = Z(a)^{n/2} G_a(x_1, \ldots, x_n)$$

and claims to prove that these converge as $a \to 0$ to well-defined tempered distributions satisfying the Osterwalder-Schrader axioms.

The strategy follows the standard programme initiated by Balaban and Federbush in the 1980s: control ultraviolet divergences through a multiscale decomposition and renormalization group analysis, establish the thermodynamic limit, and then take the continuum limit.

Here is the problem. Balaban's programme for four-dimensional Yang-Mills was never completed. It is the most technically demanding part of the Clay problem. Balaban published a series of papers in the 1980s and 1990s establishing major parts of this programme, but the complete non-perturbative control of the continuum limit in $d=4$ was not achieved. The mathematical physics community has continued working on this for thirty years since.

Nye's paper treats this as if it is straightforward. The proof of Theorem 10 ("Existence of Continuum Limit") — which is the central result — proceeds as follows:

1. Establish uniform bounds on correlation functions using cluster expansions and reflection positivity
2. Analyze the renormalization group flow and use asymptotic freedom to control the coupling
3. Show the renormalized correlation functions form a Cauchy sequence
4. Verify the Osterwalder-Schrader axioms

Each of these steps is stated with a proof sketch. None of them are complete proofs at the level of rigour the Clay Prize requires. The cluster expansion step, in particular, requires extremely careful technical estimates to work in four dimensions, this is precisely where the Balaban programme becomes most demanding, and Nye's treatment handles it in a few paragraphs.

The asymptotic freedom argument deserves specific comment. It is true that asymptotic freedom (the weakening of the coupling at high energies) gives perturbative control at short distances. But the mass gap is an infrared phenomenon, it lives at long distances and large scales, exactly where asymptotic freedom says coupling becomes strong. The argument that asymptotic freedom helps establish the continuum limit does not directly address the mass gap; it addresses the ultraviolet behaviour, which is the easier part.

### Component 3: The Mass Gap via Entanglement

This is the paper's most novel idea. Nye claims to prove the existence of a mass gap by analyzing the entanglement structure of the vacuum state.

The key result is the claimed bound

$$\Delta \geq \frac{C_G}{g^2 \log(1/g^2)} \Lambda_{QCD}$$

where $C_G$ is a positive constant depending only on the gauge group $G$, and $\Lambda_{QCD}$ is the characteristic scale of the theory.

The argument runs as follows. The Hilbert space of the lattice gauge theory satisfies an area law for entanglement entropy: for the ground state $|\Omega\rangle$ and a spatial region $A$,

$$S(A) = -\text{tr}(\rho_A \log \rho_A) \propto |\partial A|$$

where $|\partial A|$ is the area of the boundary of $A$. This area law, proved for gapped one-dimensional systems and conjectured (with supporting evidence) for higher-dimensional gapped systems, is cited as the basis for the mass gap bound.

The specific claim is: if the vacuum satisfies an area law, then the system has a spectral gap. The entanglement entropy being proportional to boundary area (rather than volume) is the signature of a gapped phase.

This argument has the right physics behind it. In condensed matter, area laws for entanglement entropy and spectral gaps are genuinely related. The work of Hastings (2007) established that gapped one-dimensional systems satisfy an area law. The converse — that area law implies gap — is known in certain settings.

But the argument as Nye presents it is circular. He uses the assumed area law to derive the gap, but the area law for Yang-Mills vacuum was not established independently. It is not a theorem; it is a conjecture (or at best, supported by numerical evidence). The argument runs: "if the system has an area law then it has a gap, and Yang-Mills should have an area law because we expect it to have a gap." This does not constitute a proof.

Furthermore, the specific bound Nye derives — $\Delta \geq C_G g^{-2} (\log g^{-2})^{-1} \Lambda_{QCD}$ — requires careful verification because $g$ depends on scale through the renormalization group. At the scale $\Lambda_{QCD}$, the coupling is of order 1, and the perturbative formula for the coupling breaks down. The bound is derived from a perturbative analysis in a regime where perturbation theory does not apply.

---

## The Wightman Axioms: Were They Actually Verified?

This is where the gap between "claimed" and "established" is clearest.

**W1 (Relativistic invariance).** The lattice breaks full Lorentz invariance to its discrete hypercubic subgroup. Recovering full Lorentz invariance in the continuum limit is a non-trivial step. Nye asserts this follows from the symmetries of the lattice theory, but the argument requires showing that all the Lorentz-violating lattice artefacts vanish in the continuum limit, a detailed calculation that is not provided.

**W3 (Uniqueness of the vacuum).** The paper asserts this follows from "the exponential clustering property." Establishing exponential clustering requires knowing the mass gap, the correlation length is $\xi = 1/\Delta$. This is again circular.

**W5 (Reconstruction: the Hilbert space is generated by field operators acting on the vacuum).** For this to hold in the continuum limit, one needs to show that the continuum field operators, as defined by the limiting process, generate the full Hilbert space. This is not straightforward in four-dimensional Yang-Mills and is not established in the paper.

The Osterwalder-Schrader axioms are treated in Theorem 10 under the heading "Verification." Axiom OS2, reflection positivity, is stated to be "inherited from our quantum circuit construction." Reflection positivity for lattice gauge theories is indeed a known result (it follows from the structure of the lattice path integral with positive weights). But inheriting this in the continuum limit requires careful analysis of how the limiting procedure preserves the positivity properties. The paper does not provide this.

---

## What the Paper Does Well

I want to be clear about what the paper does correctly, because I think the quantum information approach to Yang-Mills is genuinely interesting.

The quantum circuit representation of lattice gauge theory is a clean formulation. The Trotter error bounds are correctly derived. The connection between the entanglement spectrum of the vacuum and the mass gap is a physically motivated and potentially productive idea. The framework the paper sketches reformulating Yang-Mills in terms of quantum circuits, then using quantum information tools like entanglement renormalization to analyse the continuum limit is a research direction worth pursuing.

The paper is also well-organised and clearly written. The motivation is sound. The problem is that the proofs of the central theorems are not rigorous enough to meet the standard the Clay Prize requires. The gap between "this strategy should work" and "here is a complete proof that this strategy works" is precisely the gap that has resisted resolution for forty years.

---

## Where the Problem Actually Stands

The current state of the problem as I understand it from the literature, because this is more useful than just criticising what the Nye paper does not achieve.

**What has been proved:**

The mass gap in lattice Yang-Mills in the 't Hooft limit ($N \to \infty$ with $g^2 N$ fixed) was proved rigorously by Cao, Chatterjee, and collaborators in late 2025 ([arXiv:2510.22788](https://arxiv.org/abs/2510.22788)). This is a genuine result: a mass gap in the lattice theory, unique infinite-volume limit, and control of the large-$N$ limit. But it is a lattice result for $U(N)$, not the continuum result for fixed $N$ that the Clay Problem asks for.

Earlier, Chatterjee's probabilistic approach ([arXiv:1803.01950](https://arxiv.org/abs/1803.01950)) established partial results using random matrix theory methods.

**What is under review:**

In June 2025, Serafini et al. posted a preprint ([arXiv:2506.00284](https://arxiv.org/abs/2506.00284)) claiming a constructive proof of the mass gap for pure $SU(3)$ Yang-Mills on $\mathbb{R}^4$. The approach uses a five-dimensional regulator — realising $\mathbb{R}^4$ as the zero-mode sector of a theory on $\mathbb{R}^4 \times S^1/\mathbb{Z}_2$, combined with a convergent polymer expansion for gauge and ghost fields. This paper is currently under serious expert review. Terrence Tao has commented on the difficulty of assessing such claims. The Clay Institute has not made any announcement. Whether the Serafini et al. approach meets the full Clay standard is an open question among experts.

Separately, Martin Hairer and Sourav Chatterjee gave lectures at the Clay Millennium Problems series at Harvard in October 2025 reviewing the state of the problem. The consensus among the experts I am aware of is: significant progress has been made, particularly from the probabilistic and lattice directions, but the full continuum result remains open.

**Where the Nye paper sits:**

The Nye paper predates the Serafini et al. preprint and is less technically developed. It belongs to the category of papers that sketch a plausible strategy without providing the complete technical machinery to execute it. The quantum information framing is novel. The central theorems are not proved at the required level of rigour. The paper was published in the International Journal of Topology, which is not a specialised mathematical physics or quantum field theory journal; the review process for this class of claim would need to be extremely careful to catch the gaps in the central arguments.

This does not mean the approach is wrong. It means it is incomplete.

---

## My Approach and Where It Differs

My Stueckelberg extension approaches the mass gap from a different direction: instead of trying to prove the existence of the full non-perturbative theory first, it identifies a specific gauge-invariant mechanism (the Stueckelberg field) that generates a mass term at tree level and shows this mechanism is consistent with the renormalization group at one loop.

The connection to the Clay problem is at the level of providing a mechanism, not a proof. The mechanism my paper identifies, that a group-valued Stueckelberg field $U \in G$ introduces a gauge-invariant mass without spontaneous symmetry breaking, is different from the Higgs mechanism and has specific technical properties (BRST cohomology structure, Osterwalder-Schrader compatibility, asymptotic freedom preservation) that I verified within the perturbative framework.

Where my approach and the Nye approach agree: both take seriously the idea that the mass gap is tied to non-perturbative structure that cannot be reached by expanding around the perturbative vacuum. My Stueckelberg field is a non-perturbative field configuration (a group-valued field with non-trivial topology). Nye's entanglement structure is explicitly non-perturbative.

Where they differ: the Nye paper attempts to give a complete proof of the Clay Problem and falls short. My paper makes a more modest claim, a specific mechanism and provides rigorous support for that claim within its scope.

---

## The Bucket List Item

I want to say something honest about what the mass gap problem means to me personally, because I think it is relevant.

I have never believed I would solve this problem. I chose to work on it because it is difficult enough to be worth sustained engagement, because the mathematics it requires BRST cohomology, functional analysis, non-perturbative QFT is mathematics I want to understand deeply regardless of whether it leads to a prize, and because the problem connects to things I care about: the foundations of quantum field theory, the relationship between gauge theory and geometry, the question of what mass actually is at the level of the underlying field.

When I started the Stueckelberg work, one of the things I wrote down in my notes was something like: one of my ambitions is to see this problem solved in my lifetime, not necessarily through my work. The mass gap is the kind of problem where the solution, when it comes, will probably teach everyone something new about the structure of gauge theories not just answer a specific technical question. That is what makes it worth watching.

The Serafini et al. preprint, which I am following carefully  might be closer to a real resolution than anything published before. It uses concrete, constructive methods (polymer expansions, rigorous renormalization group) in the specific setting the Clay problem asks about. Whether it succeeds will be determined by expert review over the coming months.

If it does succeed, I will be one of the first to celebrate not because of any claim to contribution, but because it would mean we understand something genuinely hard that we did not understand before. That is worth celebrating regardless of who did it.

If the Nye paper turns out to have correctly identified an approach that a future paper develops into a complete proof, that is also worth celebrating. Good ideas do not need to be complete to be good.

But right now, the mass gap is not solved. The papers that claim to solve it, including the Nye paper, do not yet meet the standard. Understanding precisely why they fall short which is what this post is about is part of understanding the problem itself.

---

*Technical background: [What the Yang-Mills Mass Gap Problem Actually Asks](https://omarora.in/blog/whatismassgapproblem/) and [Open Problems I'm Exploring](https://omarora.in/theoretical-physics/open-problems-im-exploring/). My own work on mass generation: [A Gauge-Invariant Stueckelberg Extension of Yang-Mills Theory](https://doi.org/10.5281/zenodo.19057338).*