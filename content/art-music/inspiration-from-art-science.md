---
title: "Inspiration from Art & Science"
date: 2026-02-06
parent: "Art & Music"
---


There is a passage in Feynman's *The Character of Physical Law* where he describes watching a flower and thinking: I can appreciate the beauty of the flower, and I also know that the pigments that produce the colour are absorbing photons at specific wavelengths determined by their molecular orbital structure, and I also know that the structure of the flower reflects evolutionary pressures that shaped it over millions of years — and all of this knowledge does not diminish the beauty. It adds to it. The flower is more beautiful, not less, for being understood.

I find this right. And I find that the reverse is also true: the beauty of a mathematical structure — of Cartan's exterior algebra, of the classification of simple Lie algebras, of the persistence barcode of a filtered simplicial complex — is not separate from its content. It is part of how the content communicates itself. When a proof is elegant, the elegance is not decoration. It is evidence that you have found the right angle of approach, the level of description at which the structure becomes visible.

This page is about the specific works — in mathematics, in science, in visual art, in writing — that have shaped this sense of what beauty and rigour have to do with each other. It is not a comprehensive survey of art and science. It is a personal account of what specific things did to my thinking, and in some cases, how they changed what I thought was possible.

---

## I — Mathematics as an Aesthetic Experience

### Hardy's Apology

G.H. Hardy wrote *A Mathematician's Apology* in 1940, at the end of his career, as a defence of pure mathematics against the charge that it is useless. The defence is that it is beautiful — that the criterion for mathematical work is aesthetic rather than practical, that a theorem is judged as a work of art is judged, by the coherence and depth and inevitability of its arrangement.

"There is no permanent place in the world for ugly mathematics." Hardy meant this as a methodological claim, not just a preference: ugly proofs are typically wrong, or at best not yet understood. When a proof is ugly — when it proceeds by case analysis or computation rather than by insight — it usually means that the right concept has not yet been found. The beauty is the signal that you have found the right level of abstraction.

The specific examples Hardy uses: Euclid's proof of the infinitude of primes, and Cantor's diagonal argument. Both are one-page arguments. Both settle questions that had been open. Both are what Hardy means by beautiful: they achieve their result by an idea that is surprising, inevitable in retrospect, and could not be shorter without losing something.

Euclid's proof: suppose there are finitely many primes. Multiply them all together and add one. The result is divisible by none of the primes on the list. Therefore either it is prime itself, or it has a prime factor not on the list. Either way, the list was incomplete. Contradiction. The primes are infinite.

The beauty is in the structure: you do not need to find a new prime. You just need to show that any finite list can be extended. The proof is about what follows from the assumption of finitude, and what follows is a contradiction that requires no computation.

Cantor's diagonal argument is the same quality of idea applied to a harder question: are the real numbers more numerous than the natural numbers? Yes — and the proof constructs, from any purported list of all real numbers, a real number guaranteed not to be on the list. The construction is direct and takes one paragraph.

Both proofs have the quality Hardy means. I read them for the first time in school and they changed what I thought mathematics was. Not calculation, not procedure — a practice of finding the right idea.

### Euler's Identity and What It Means

$e^{i\pi} + 1 = 0$ is the equation usually cited as the most beautiful in mathematics, and the citation is so common that it has become a cliché. The cliché does not make it wrong.

What the identity actually says — via Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ — is that the exponential function, the trigonometric functions, and the imaginary unit are not separate objects. They are aspects of a single structure: the unit circle in the complex plane. Multiplication by $e^{i\theta}$ is rotation by angle $\theta$. The exponential function, which in the real line describes growth and decay, describes rotation in the complex plane.

This is not a coincidence that was discovered and named. It is a deep structural fact about the relationship between analysis and geometry, between the discrete structure of the integers and the continuous structure of the circle, between the algebraic and the geometric. The fact that it can be expressed in five symbols is evidence that it is saying something fundamental — that the compression is not loss of information but access to a more fundamental description.

When I use $e^{ipx/\hbar}$ in quantum mechanics — the plane wave, the eigenstate of momentum — I am using exactly this: the fact that the exponential function on the circle is the right way to describe states with definite momentum. The connection between Euler's identity and the structure of quantum mechanics is not metaphorical. It is the reason that Fourier analysis, which decomposes functions into complex exponentials, is the natural language of quantum theory.

### The Classification of Simple Lie Algebras

Killing and Cartan's classification of simple Lie algebras is, for me, the most beautiful result in pure mathematics. The question: what are all the possible simple Lie algebras over the complex numbers? The answer: exactly four infinite families and five exceptional cases. No more, no fewer.

The four infinite families — $\mathfrak{sl}_n$ (traceless matrices), $\mathfrak{so} _n$ (antisymmetric matrices), $\mathfrak{sp} _{2n}$ (symplectic matrices), and the orthogonal algebras in even dimension — are built from classical linear algebra. The five exceptional cases — $G_2$, $F_4$, $E_6$, $E_7$, $E_8$ — have no analogous classical constructions. They were discovered, not invented. They exist because the constraints of the classification force them to exist, and their properties were worked out after their existence was known.

The exceptional Lie algebras appear in physics in ways that are not fully understood. $E_8 \times E_8$ is the gauge group of one of the five superstring theories. $G_2$ appears in the compactification of M-theory on manifolds with $G_2$ holonomy. Whether these appearances are physically significant or mathematical coincidences is an open question. But the fact that the classification — complete and exact — constrains what is possible in physics makes the result feel less like a theorem and more like a discovery about the structure of reality.

---

## II — Visual Art That Works Like Mathematics

### M.C. Escher and the Geometry of Paradox

Escher (1898–1972) made lithographs, woodcuts, and mezzotints that are simultaneously visual art and mathematical demonstrations. His famous impossible structures — *Waterfall*, *Ascending and Descending*, *Belvedere* — are visual realisations of Penrose's impossible figures: three-dimensional objects that cannot exist in Euclidean space but whose projections onto a two-dimensional plane are locally consistent.

What I find most interesting in Escher is not the impossible structures but the tessellations — particularly the series *Metamorphosis I, II, III* and the *Day and Night* series. These works involve the continuous transformation of one regular tiling into another: fish becoming birds, dark shapes becoming light shapes, reptiles becoming lizards. The underlying mathematical structure is the wallpaper groups — the seventeen distinct symmetry groups of the Euclidean plane — and Escher explored all of them without, for most of his career, formal mathematical training.

The mathematician H.S.M. Coxeter encountered Escher's work in 1954 and wrote to him about the hyperbolic geometry behind some of his tessellations. Escher wrote back that he did not understand Coxeter's mathematical notation but that he understood the geometry visually. Coxeter's paper on hyperbolic tessellations had, without Escher knowing it, provided the mathematical framework for what Escher had been doing intuitively. The *Circle Limit* series — four woodcuts made in the late 1950s and 1960s — are direct realisations of the Poincaré disc model of hyperbolic geometry: tilings of the hyperbolic plane that become infinitely dense toward the boundary circle.

This is the art-mathematics relationship at its most direct: Escher working on visual problems, finding solutions that turn out to be mathematically precise, and then corresponding with a professional mathematician who explains why they work. The creative process ran from visual intuition to mathematical understanding, not the other way.

I think about the *Circle Limit* woodcuts when I think about the hyperbolic geometry of financial networks — the Caputi et al. result about financial markets having hyperbolic character in their topological features. The Poincaré disc that Escher used to tile the hyperbolic plane is the same space that appears in the latent geometry of correlation networks. Whether this is just a common mathematical structure appearing in two unrelated contexts or something more is the kind of question I cannot answer with confidence, but cannot stop thinking about.

### Mondrian and the Reduction to Structure

Piet Mondrian (1872–1944) spent thirty years progressively eliminating everything from his paintings that was not pure structure: first the recognisable forms went, then the curves, then the diagonal lines, until what remained was vertical and horizontal black lines on white, with rectangles of primary colour. *Composition with Red, Blue, and Yellow* (1930) is perhaps the most well-known result.

The standard description of Mondrian — that he was trying to express universal harmony through pure abstraction — is not wrong but does not explain why his work is specifically interesting rather than merely minimal. What I find in the late Mondrian is something closer to what I find in a well-constructed proof: the feeling that the constraint is generative rather than restrictive. By accepting that only vertical and horizontal lines are permitted, by accepting that only primary colours are used, the composition has to achieve its effects through exactly those elements. The limitation is what creates the pressure that makes the work interesting.

This is directly analogous to the role of constraints in mathematics and physics. Gauge invariance — the requirement that physical laws are invariant under local symmetry transformations — is a constraint. It severely restricts the possible Lagrangians. The restriction is not impoverishment; it is the pressure that forces the theory toward its correct form. Yang-Mills theory is what you get when you demand non-Abelian gauge invariance. The symmetry requirement does most of the work.

### Kandinsky and Synesthesia

Wassily Kandinsky (1866–1944) was among the first Western painters to make fully abstract works — paintings with no representational content, organised entirely by relationships between colour, form, and line. He was also a synesthete: he experienced colour as sound and sound as colour, and he theorised these correspondences explicitly in *Concerning the Spiritual in Art* (1911).

The theory — that specific colours correspond to specific musical timbres, that the relationships between colours on a canvas are analogous to the relationships between instruments in a score — is not scientifically rigorous, and Kandinsky did not intend it to be. What it is, is a description of how he experienced visual art: as temporal, dynamic, having something like rhythm and melody. His paintings are titled as musical compositions (*Composition VII*, *Improvisation 28*) precisely because he experienced the process of making them as analogous to musical improvisation.

The synesthesia question — whether cross-modal sensory associations are a real perceptual phenomenon or a learned metaphorical habit — is not settled. But what Kandinsky's work demonstrates is independent of the answer: that the principles of organisation in music (rhythm, harmony, counterpoint, development) are not specific to music but are principles of organisation in general, applicable to visual form as well as to sound. And that the same principles might apply to mathematical structure: the "rhythm" of a well-paced proof, the "harmony" of a theorem that sits at the right level of generality, the "counterpoint" of two ideas that illuminate each other by contrast.

This is not a precise claim. But I find that my aesthetic responses to mathematics and to music share more structure than the conventional categorisation of "technical" and "artistic" would suggest. Both involve the perception of structure in time (or in a sequence of steps), both reward attention, and both have the quality of inevitability when they are right.

---

## III — Science That Functions Like Art

### Dirac's Equation and the Prediction of Antimatter

I discussed Dirac at length in the [history of mathematics and physics page](/omarora/history/history-of-mathematics-physics/). I want to say something here about the aesthetic dimension of the derivation, because it is directly relevant to the art-science question.

Dirac derived his equation — the relativistic wave equation for the electron — by demanding that it be first-order in space and time derivatives and that its square equal the Klein-Gordon equation. These are constraints, not assumptions about physical reality. The constraints force the equation into a specific form, and that form turns out to predict: the spin of the electron (as an intrinsic property, not added by hand), the correct magnetic moment, the existence of the positron, and ultimately the entire framework of quantum field theory.

The prediction of the positron is the moment I find most striking aesthetically. The Dirac equation has four components: two for the electron (spin up and spin down) and two for something else — solutions with negative energy that Dirac initially called "holes" in a sea of negative-energy states. This interpretation was eventually replaced by the correct one: the negative-energy solutions represent the antiparticle, the positron, which was discovered experimentally by Anderson in 1932, four years after the equation was published.

Dirac did not observe the positron and then model it. He followed the mathematics and found it was telling him something existed that had not yet been seen. The equation was ahead of the experiment. This is what beauty in physics is for: not decoration, but a signal that you have found a description that is genuinely correct at a level the experiment has not yet reached.

### Noether's Theorems and the Unity of Conservation Laws

Emmy Noether's first theorem — every continuous symmetry of the action corresponds to a conserved quantity — is, for me, the most beautiful result in theoretical physics. I said this on the history page and I want to say it again here, because the reason it belongs on a page about art and science is that it has exactly the quality Hardy describes in pure mathematics: it achieves something vast through a single idea, the idea is surprising in retrospect, and once you have seen it, you cannot imagine having thought about the problem any other way.

Before Noether, conservation of energy was a brute empirical fact: we observe that energy is conserved. We measure it in many situations. We believe it universally. But why? The question was not clearly formulated.

After Noether, the question has a complete answer: energy is conserved because the laws of physics are the same today as they were yesterday — because the action is invariant under time translation. If the laws were different on Tuesdays, energy would not be conserved on Tuesdays. The conservation is not a coincidence; it is a structural consequence of the time-translation symmetry of the laws.

The same argument gives momentum conservation from spatial translation symmetry, angular momentum conservation from rotational symmetry, and charge conservation from gauge symmetry. Every conservation law in physics is the shadow of a symmetry. The theorem does not merely explain conservation laws — it unifies them, showing that they are all instances of the same structural relationship.

This is the same quality as a great mathematical proof: the unification is not forced, it reveals that things that seemed separate were aspects of a single more fundamental thing all along.

---

## IV — The Overlap: What Art and Science Share

There is a conventional account of the relationship between art and science: art is subjective, intuitive, emotional; science is objective, rational, analytical; the two complement each other, each providing what the other lacks. I find this account both common and wrong.

The actual relationship, as I have experienced it, is more uncomfortable: both art and science require the same underlying cognitive habits, and the division between them is largely institutional rather than natural.

**Both require the ability to hold a problem as a felt sense before articulating it.** A physicist working on a new idea often knows it is right before they can prove it — the mathematics follows the intuition, not the other way. Dirac said: "It is more important to have beauty in one's equations than to have them fit experiment." This is not mysticism; it is a methodological observation that a beautiful equation is more likely to be correct than an ugly one, because ugliness usually signals that the right concept has not yet been found. The artist working on a composition knows when something is wrong before they know why — before the explicit analysis of proportion, harmony, or rhythm. The felt sense precedes the articulation in both cases.

**Both require the discipline to discard what is merely pleasing.** Hardy's point about ugly mathematics applies equally to art: work that is smooth and accomplished and says nothing is failing on the most important criterion, regardless of its technical competence. The hardest part of both practices is learning to distinguish genuine rightness from mere pleasingness — to notice when something feels satisfying because it is familiar rather than because it is true.

**Both are forms of discovery rather than invention.** This is contentious, but I believe it in both cases. When Galois worked out the group theory of polynomial equations, when Cantor proved the uncountability of the reals, when Escher found the hyperbolic tiling of the Poincaré disc — in each case, the sense reported is not "I have made something new" but "I have found something that was there." The mathematician or artist who has done genuine work often describes the experience as discovery, not creation. Whether mathematical and aesthetic objects exist independently in some Platonic realm, or whether this is a phenomenological description of a purely cognitive process, is a philosophical question I have not resolved. But the phenomenology is consistent enough to be worth taking seriously.

**Both are transmitted through specific works, not through general principles.** You cannot learn to appreciate Bach by reading about counterpoint. You cannot learn to appreciate the elegance of a proof by reading about what elegance means. The knowledge is embodied and transmitted through specific encounters with specific works. This is why the specific works I have named in this page matter — not as examples of general principles but as the actual content of what I mean when I talk about beauty in mathematics or science.

---

## V — What This Means for How I Work

The connection between the aesthetic and the technical is not merely personal preference. It has methodological implications that I take seriously.

**The preference for structural transparency is a guide.** When two approaches to a problem are available — one that hides the structure in computation and one that makes the structure visible in the argument — the second is almost always more productive in the long run, even when the first reaches the answer faster. Coordinate-based tensor calculus gets you to the right answer in general relativity. Cartan's exterior algebra makes the structure visible. In my own research, I consistently prefer the formulation that makes the underlying geometry explicit over the one that is computationally simpler.

**Aesthetic discomfort with a result is evidence.** When a proof or a model produces a result that feels wrong — not wrong empirically, but aesthetically misshapen — this is weak evidence that something has gone wrong. Not decisive evidence; sometimes correct answers are ugly. But consistently ugly results in a framework are a signal worth taking seriously. The renormalisation procedure in QFT feels ugly because it is — it is a workaround for a problem (ultraviolet divergences) that a better theory should not have. The ugliness is a symptom. I hold this lightly, because the ugliness has not prevented the theory from being the most accurate in history. But I hold it.

**The exposure to different kinds of structured beauty makes the range of available patterns wider.** The patterns I see in financial correlation networks — the way topological features change under stress, the way the network transitions from hierarchical to egalitarian as crisis approaches — have been made more visible to me by having thought about Escher's tessellations, Mondrian's constraint-generated composition, and Cartan's differential geometry. These are not the same patterns. But the habit of seeing structure is transferable, and the richer the set of structures you have encountered, the more likely you are to recognise a new one when it appears.

This is the version of the art-science connection I find defensible and specific, as opposed to vague and inspirational. Not "art makes scientists more creative" (too broad, possibly false) but: the cognitive habits developed in attending carefully to structured works — whether mathematical, musical, visual, or scientific — make the range of patterns available for recognition wider, and that wider range has a direct payoff in research.

---

*Last updated March 2026.*