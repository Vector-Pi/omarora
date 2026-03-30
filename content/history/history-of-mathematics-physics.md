---
title: "History of Mathematics & Physics"
date: 2026-02-22
parent: "History"
---


History of science, done badly, is a list of names and dates. Newton invented calculus in 1666; Einstein published special relativity in 1905; the Standard Model was completed in 1973. These statements are all true and almost entirely uninformative. They tell you what happened without telling you *why it happened* — what problem the invention was solving, why existing tools were insufficient, why the solution took the form it did.

Done well, history of science is something different: it is the recovery of the intellectual situation that made the breakthrough necessary and possible. When you understand what problem Riemann was solving in 1854 — what it would have meant to take geometry seriously as an intrinsic science, independent of the surrounding space — then the fact that his work sat essentially unused for fifty years, and then became exactly the mathematics Einstein needed for general relativity, stops being a coincidence and starts being explicable. The mathematics was the right answer to a question that physics had not yet learned to ask.

This page traces the history of the mathematical and physical ideas I find most compelling, from the perspective of someone who works with them. It is not comprehensive. It is the history of the ideas I can see running through my own work — from Euclid to Gauss to Riemann to Cartan to Weyl to Yang and Mills to the present. It is history told from the inside.

---

## Part I — The Ancient Foundations

### Greek Mathematics and the Invention of Proof

The decisive contribution of Greek mathematics was not any specific theorem but the invention of *proof* — the demand that mathematical claims be established by chains of deductive reasoning from explicit assumptions, rather than by measurement, example, or authority.

The shift is visible between Babylonian mathematics (which solved quadratic equations by procedure, without justification) and Euclid's *Elements* (which derived an enormous body of geometry from five postulates by logic alone). The fifth postulate — the parallel postulate — stated that through a point not on a given line, exactly one line can be drawn parallel to the given line. It was more complex than the others, and Greek mathematicians spent centuries trying to prove it from the other four. The attempt failed. It would take two thousand years to understand why.

Archimedes developed what was, in everything but name, integral calculus — computing areas and volumes of curved figures by exhaustion, approximating them with sequences of polygons. He knew the method was productive; he could not justify why the limiting process was valid. The justification would have to wait for the 17th century.

---

### The Conflict Over Infinity

Greek mathematics was systematically uncomfortable with the infinite. Zeno's paradoxes — Achilles and the tortoise, the arrow — showed that naive thinking about continuous motion generates contradictions. Aristotle's resolution was to distinguish *potential* infinity (a process can go on indefinitely) from *actual* infinity (an infinite set exists as a completed totality). He accepted the former and rejected the latter.

This was a compromise that delayed confrontation with the real problem for two millennia. The limit concept — the foundation of calculus — requires taking actual infinite processes seriously. When Newton and Leibniz developed calculus in the 17th century, they did not resolve the foundational issue; they built an enormously productive set of techniques whose logical foundations remained murky until Cauchy, Weierstrass, and Riemann in the 19th century.

The pattern — techniques developed in advance of foundations, with the foundations eventually catching up — recurs constantly in this history.

---

## Part II — The 17th Century: Mechanics, Calculus, and the Mathematisation of Nature

### Galileo and the Language of Mathematics

"The book of nature is written in the language of mathematics." Galileo did not merely assert this; he demonstrated it by finding the mathematical laws governing falling bodies and projectile motion. The parabolic trajectory of a projectile — the combination of uniform horizontal motion and uniformly accelerated vertical motion — is not obvious from observation. It required idealisation (no air resistance, perfectly smooth inclines) and mathematical analysis.

The idealisation is philosophically significant. Real trajectories are not parabolas; they are messy curves modified by air resistance, the Coriolis effect, and the finite size of the projectile. The mathematical law describes an idealised situation. Whether the law is *about* the real world or about the idealisation is a question the philosophy of science is still working through.

### Newton and the Synthesis

Newton's *Principia Mathematica* (1687) is the most important work in the history of physics. It did three things simultaneously: developed calculus as a mathematical tool, formulated the laws of motion, and applied them to derive Kepler's laws of planetary motion from the law of universal gravitation.

The inverse square law of gravity — $F = GMm/r^2$ — was already suspected by several people (Hooke, Halley) when Newton published. What Newton did that no one else could was prove that an inverse square law implies elliptical orbits, and derive the entire observed phenomenology of the solar system from it. This was a demonstration of the power of mathematical physics that changed what scientists thought they were doing.

Two technical contributions that shaped everything subsequent:

**The calculus.** Newton called it the "method of fluxions" — rates of change and accumulated change. The fundamental theorem (integration and differentiation are inverses) is among the most important in mathematics. The logical foundations were obscure — the infinitesimals Newton used were neither finite nor zero — but the technique worked with extraordinary power.

**The law of gravitation as action at a distance.** The sun acts on the earth across 150 million kilometres of empty space, instantaneously. Newton found this deeply unsatisfying — "I feign no hypotheses" — and the conceptual problem it raised would not be resolved until Einstein replaced action at a distance with field theory.

### Leibniz and the Calculus War

Leibniz developed calculus independently and published first (1684), with notation that was superior to Newton's and that we still use ($dy/dx$, $\int$). The priority dispute between Newton and Leibniz poisoned the relationship between British and Continental mathematics for a century — British mathematicians, loyal to Newton's fluxion notation, fell significantly behind.

This is a useful lesson in how sociology affects intellectual progress. The best ideas do not automatically win; they win or lose partly through the social structures in which they are embedded.

---

## Part III — The 18th Century: Euler, Lagrange, and the Mathematisation of Mechanics

### Euler: The Most Productive Mathematician in History

Leonhard Euler (1707–1783) produced 866 books and papers — more than any mathematician before or since. He worked on virtually every area of mathematics and physics then known: number theory, analysis, geometry, mechanics, fluid dynamics, optics, and astronomy.

The contributions that matter most for what follows:

**$e^{i\pi} + 1 = 0$** — Euler's identity, relating the five most fundamental constants in mathematics. More important is the formula it comes from: $e^{i\theta} = \cos\theta + i\sin\theta$. This connects complex analysis to trigonometry and is the key to Fourier analysis, quantum mechanics (the wavefunction $\psi = e^{ipx/\hbar}$), and the representation theory of compact groups.

**The Königsberg bridge problem (1736).** Euler proved that it is impossible to walk through Königsberg crossing each of its seven bridges exactly once. The proof introduced the concept of a *graph* — a collection of vertices connected by edges — and the notion that what mattered was the structure of connections, not the geometric form. This is the founding act of both graph theory and topology.

### Lagrange and the Action Principle

Lagrange's *Mécanique Analytique* (1788) reformulated all of Newtonian mechanics without a single diagram. The approach: instead of specifying forces, specify the kinetic and potential energy of the system as functions of generalised coordinates. The equations of motion follow from the principle of stationary action — the actual trajectory of a system is the one that makes the action $S = \int (T - V) dt$ stationary.

This reformulation is mathematically beautiful but has a deeper significance: it makes the symmetries of the system manifest. If the Lagrangian does not depend on a particular coordinate, the corresponding momentum is conserved. This is the seed of Noether's theorem, planted a century before Noether.

The Lagrangian approach also generalises vastly more easily than Newton's laws. Quantum mechanics, quantum field theory, general relativity, and string theory are all formulated in terms of action principles. Newton's second law is a special case.

---

## Part IV — The 19th Century: The Most Consequential Period in Mathematical History

The 19th century produced the mathematical structures that underlie virtually all of contemporary theoretical physics. It is the period I find most historically extraordinary — not just because of the results but because of how many of them were developed for purely internal mathematical reasons, with no physical application in view, and then turned out to be exactly what physics needed.

### Gauss and Non-Euclidean Geometry

Carl Friedrich Gauss (1777–1855) secretly explored non-Euclidean geometry — geometry in which the parallel postulate fails — but did not publish, fearing ridicule. Lobachevsky and Bolyai published independently in the 1820s. In non-Euclidean (hyperbolic) geometry, the angle sum of a triangle is less than 180°; through a point not on a line, infinitely many parallel lines can be drawn.

Gauss had a more fundamental insight: curvature is an *intrinsic* property of a surface, measurable from within the surface itself without reference to an embedding in higher-dimensional space. The Gaussian curvature $K = 1/(r_1 r_2)$ (the product of the principal curvatures) can be computed from measurements made on the surface. This is the **Theorema Egregium** — the remarkable theorem.

Why it matters: it opens the possibility of studying spaces whose geometry is not Euclidean, not because they are bent in some higher-dimensional space but intrinsically. Riemann would generalise this to arbitrary dimensions. Einstein would use the result to describe spacetime.

### Riemann's Habilitation Lecture (1854)

On June 10, 1854, Bernhard Riemann delivered his habilitation lecture "On the Hypotheses Which Lie at the Foundation of Geometry" to the faculty of Göttingen, with Gauss in the audience. It is one of the most important lectures in the history of mathematics.

In less than thirty pages — with no equations in the lecture itself, at Gauss's insistence — Riemann generalised the concept of geometry to $n$-dimensional spaces with arbitrary curvature at every point. He introduced what we now call the *Riemannian metric* $g_{ij}$: a smoothly varying symmetric positive-definite tensor that defines the notion of distance at each point of the manifold. The geometry is determined by the metric; the curvature of the space is encoded in the Riemann curvature tensor, a quantity built from the metric and its first and second derivatives.

Riemann also asked, remarkably, whether physical space might not be Euclidean — whether the geometry of the actual world was a matter for empirical investigation rather than a priori assumption. This was philosophically radical. Kant had argued that Euclidean geometry was a synthetic a priori truth — necessarily true, knowable without experience. Riemann suggested it might be an empirical question.

He was right. Sixty-one years later, Einstein would use Riemannian geometry to formulate general relativity. The curvature of the Riemannian manifold is exactly the gravitational field. The geodesics of the metric are the paths of freely falling objects. The Einstein field equations relate the Ricci curvature tensor — built from the Riemann tensor — to the stress-energy tensor of matter.

Riemann died of tuberculosis in 1866, aged 39, having also proved the Riemann mapping theorem, developed the theory of Riemann surfaces, and stated the Riemann hypothesis — still unproved — about the distribution of prime numbers. He may be the single most influential mathematician in the history of physics.

### The Development of Group Theory

Group theory — the study of symmetry — was developed in the first half of the 19th century from two independent directions.

**Galois (1811–1832)** asked whether polynomial equations are solvable by radicals. He introduced the concept of a group of permutations of the roots and showed that an equation is solvable if and only if its Galois group has a specific structure (is "solvable" in a technical sense). The fifth-degree polynomial equation has a non-solvable Galois group, which is why there is no formula for its roots analogous to the quadratic formula.

Galois died in a duel at age 20, having transmitted his mathematical discoveries to a friend in a letter the night before. The letter was largely ignored for a decade.

**Lie (1842–1899)** developed continuous groups — what we now call Lie groups — as the groups of symmetries of differential equations. The symmetries of the laws of physics are Lie groups: the rotation group $SO(3)$, the Lorentz group $SO(3,1)$, the gauge groups $U(1)$, $SU(2)$, $SU(3)$.

By the end of the 19th century, Killing and Cartan had classified all simple Lie algebras: the four infinite families $A_n, B_n, C_n, D_n$ and the five exceptional cases $G_2, F_4, E_6, E_7, E_8$. This classification is complete and exact. The symmetry groups of nature are drawn from this finite list — a fact that is remarkable from whatever perspective you approach it.

### Maxwell and the Unification of Electricity and Magnetism

James Clerk Maxwell's equations (1865) unified electricity and magnetism and predicted the existence of electromagnetic waves travelling at the speed of light — thereby identifying light as an electromagnetic phenomenon.

The equations in modern notation:
$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}, \quad \nabla \cdot \mathbf{B} = 0$$
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}$$

The displacement current (the $\partial\mathbf{E}/\partial t$ term) was Maxwell's original contribution — added to make the equations consistent with conservation of charge. It is the term that implies electromagnetic waves.

The philosophical significance: Maxwell's equations are the prototype of all subsequent gauge theories. The electric and magnetic fields are not the fundamental objects — the electromagnetic potential $A_\mu$ is. The transformation $A_\mu \to A_\mu + \partial_\mu\alpha$ (gauge transformation) leaves all observable quantities unchanged. This gauge freedom — this redundancy in the description — is the mathematical structure that Yang and Mills would generalise ninety years later.

### Noether and the Connection Between Symmetry and Conservation

Emmy Noether (1882–1935) proved two theorems in 1915 that are among the most important in all of theoretical physics.

**First Noether theorem:** every continuous symmetry of the action of a physical system corresponds to a conserved quantity.

- Time translation symmetry $\rightarrow$ conservation of energy
- Spatial translation symmetry $\rightarrow$ conservation of momentum
- Rotational symmetry $\rightarrow$ conservation of angular momentum
- $U(1)$ gauge symmetry of electromagnetism $\rightarrow$ conservation of electric charge

This theorem transforms the question "why is energy conserved?" from a mysterious empirical fact into a mathematical theorem about the symmetry of the laws of physics. Conservation laws are not brute facts about nature — they are consequences of symmetry. This is possibly the deepest structural insight in the history of physics.

**Second Noether theorem:** if the action has an infinite-dimensional (local) symmetry group — as in general relativity and gauge theories — then the Euler-Lagrange equations are not independent; there are identities among them. These identities are the Bianchi identities of general relativity and the gauge identity $D_\mu J^\mu = 0$ in Yang-Mills theory.

Noether proved these theorems while working at Göttingen without a salary, barred from academic positions because she was a woman. The theorems were prompted by questions about conservation of energy in general relativity that Einstein and Klein were struggling with. She resolved the issue completely and in far greater generality than was needed.

---

## Part V — The 20th Century: The Geometric Turn

### Einstein and General Relativity (1915)

Einstein published special relativity in 1905 and spent the following ten years searching for a relativistic theory of gravity. The key constraint: the equivalence principle — inertial mass and gravitational mass are equal, so a freely falling observer cannot distinguish gravity from the absence of gravity. Gravity is not a force; it is the curvature of spacetime.

The mathematical framework was Riemannian geometry. Einstein did not know enough differential geometry in 1912 when he began; his friend Marcel Grossmann (a mathematician) supplied the tools — and specifically brought Riemann's 1854 work to Einstein's attention. The connection between Riemann's abstract geometry and Einstein's physical problem was not obvious to Einstein when he began. It took three years of struggle, including a near-miss in 1913 with the "Entwurf" equations that were not generally covariant.

The Einstein field equations (1915):
$$R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}$$

Left side: geometry (Ricci curvature, Ricci scalar, metric). Right side: matter and energy (stress-energy tensor). "Matter tells spacetime how to curve; spacetime tells matter how to move."

The confirmation: the 1919 solar eclipse expedition, led by Eddington, measured the bending of starlight around the sun. Newton's theory predicted half the deflection that general relativity predicted. The measured deflection agreed with Einstein.

### Cartan and the Moving Frame

Élie Cartan (1869–1951) reformulated differential geometry in a way that made the structure of connections and curvature fully explicit and independent of coordinates. His method of moving frames and the calculus of differential forms gave the geometric infrastructure that gauge theory would eventually be built on.

Cartan's exterior derivative $d$ — satisfying $d^2 = 0$ — is the unified framework for gradient, curl, and divergence, and the foundation of de Rham cohomology. The generalised Stokes theorem $\int_M d\omega = \int_{\partial M} \omega$ unifies the classical integral theorems of vector calculus into a single statement.

More importantly for what follows: Cartan introduced the notion of a *connection* on a bundle — a rule for parallel transport, for comparing vectors at different points. The curvature of a connection is the failure of parallel transport around a closed loop to return to the starting vector. This is exactly the mathematical structure of gauge theory: the gauge field is a connection, and the field strength is the curvature of that connection.

Cartan developed all of this before gauge theory existed as a physical concept. When physicists needed it, it was waiting.

### Weyl and the First Gauge Theory (1918)

Hermann Weyl attempted in 1918 to unify general relativity and electromagnetism by introducing a *scale gauge* — allowing the metric to change not just under coordinate transformations but under local rescaling. He proposed that the electromagnetic potential $A_\mu$ was the compensating connection for this local scale invariance.

Einstein rejected the theory on physical grounds: if lengths could change under parallel transport, atomic spectra would depend on the history of the atom, which is not observed. Weyl's specific programme failed.

But the mathematical structure survived. When quantum mechanics was developed in the 1920s, Weyl reinterpreted his gauge principle: the phase of the wavefunction (not the scale of lengths) is the quantity that can be freely chosen at each point. The electromagnetic potential is the compensating connection for local $U(1)$ phase invariance. This works: it produces exactly Maxwell's equations from the invariance requirement.

The conceptual shift from scale gauge to phase gauge — and the realisation that electromagnetism *is* a gauge theory in this sense — is one of the great conceptual achievements in the history of physics.

### Dirac and the Path Between Mathematics and Physics

Paul Dirac had an unusual philosophical principle: the laws of physics should be expressible in beautiful mathematics. His derivation of the relativistic equation for the electron (1928) is the purest expression of this principle.

The equation needed to be first-order in both space and time derivatives (to transform properly under Lorentz transformations) and to reduce to the Schrödinger equation in the non-relativistic limit. The square of the equation had to equal the Klein-Gordon equation. The only way to achieve this is with matrices — the Dirac matrices $\gamma^\mu$ satisfying $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$.

The equation automatically predicted the electron's spin as an intrinsic property, not added by hand. It predicted the electron's magnetic moment with the correct $g$-factor of 2. And it predicted the existence of antimatter — the positron, discovered four years later.

Dirac also introduced bra-ket notation, the delta function (before it had a rigorous mathematical foundation), and the concept of the magnetic monopole (predicted on topological grounds — the quantisation of magnetic charge follows from the consistency of the quantum theory of a charged particle in the field of a monopole). The monopole has not been observed, but the topological argument connecting its charge quantisation to the first Chern class of a fibre bundle is one of the first instances of deep topology entering physics.

### Yang and Mills: The Non-Abelian Revolution (1954)

The story of the Yang-Mills paper matters to me personally because it is where my own research begins.

Chen-Ning Yang and Robert Mills asked in 1954: what if the gauge symmetry of electromagnetism — the $U(1)$ phase invariance — were generalised to a non-Abelian group, specifically $SU(2)$ (the group of isospin rotations of the proton and neutron)? Could the same principle — demand local gauge invariance, derive the forces — explain the strong interactions?

The answer was: yes and no. The local $SU(2)$ invariance requires the introduction of three gauge bosons (the generalisation of the photon), self-interacting because the group is non-Abelian. But the theory requires these bosons to be massless, which contradicts observations — the strong force is short-range, implying massive force carriers.

At the seminar where Yang presented the paper, Pauli (who had worked on the same idea independently) interrupted repeatedly to ask: "What is the mass of this field?" Yang had no answer. The mass problem — how to give mass to the gauge bosons while preserving gauge invariance — is what the Higgs mechanism, the Stueckelberg mechanism, and my own research are all attempts to address.

The Yang-Mills paper was published and largely ignored for a decade. Then two things happened: the Higgs mechanism (1964) showed how gauge boson mass could be generated through spontaneous symmetry breaking, and 't Hooft and Veltman (1971) proved that non-Abelian gauge theories are renormalisable. Gross, Wilczek, and Politzer (1973) proved asymptotic freedom. Suddenly Yang-Mills theory became the framework for the entire Standard Model.

The story of Yang-Mills is the story of a mathematical structure that was more powerful than anyone realised when it was first written down, whose full implications took twenty years to understand.

### Fibre Bundles and the Geometric Synthesis (1950s–1970s)

The full mathematical picture of gauge theory was developed in parallel with the physics, but the two communities did not realise they were working on the same thing until much later.

Charles Ehresmann (1905–1979) introduced the concept of a fibre bundle and the notion of a connection on a principal bundle in the 1940s and 1950s. The precise definition: a principal $G$-bundle $P \to M$ is a space $P$ with a group action of $G$ such that the orbits are the fibres over the base space $M$. A connection is a $G$-equivariant splitting of the tangent bundle of $P$ into horizontal and vertical parts.

Shiing-Shen Chern (1911–2004) developed characteristic classes — topological invariants of fibre bundles. The Chern classes $c_k(E)$ of a complex vector bundle $E$ are cohomology classes of the base manifold that measure the global topological twist of the bundle. The first Chern class of a $U(1)$ bundle is the magnetic monopole charge. The second Chern class of an $SU(2)$ bundle is the instanton number — the topological charge of Yang-Mills instantons.

The connection between the physics and the mathematics was made explicit when Wu and Yang wrote a "dictionary" in 1975 translating between the physics language (gauge potentials, field strengths, gauge transformations) and the mathematics language (connections, curvature, bundle automorphisms). They found that the Dirac monopole — a singular classical solution that had puzzled physicists since 1931 — was exactly a non-trivial $U(1)$ bundle with first Chern class equal to the monopole charge.

The singularity in the Dirac string was not physical; it was the artifact of using a single coordinate chart on a topologically non-trivial bundle. Different charts — different gauges — are needed to cover the bundle, and the Dirac string is the overlap region. The topology resolves the apparent singularity.

When I work through the BRST quantisation of the Stueckelberg-extended Yang-Mills theory, I am working within this geometric framework — built by Riemann, Cartan, Ehresmann, and Chern over a century — that the physicists of the Standard Model inherited.

---

## Part VI — The Late 20th Century: When Physics Started Teaching Mathematics

### Donaldson and Four-Manifolds (1983)

Simon Donaldson, then a graduate student at Oxford, used the moduli space of instantons (self-dual Yang-Mills connections on a four-manifold) to prove a theorem that stunned the mathematical community: the smooth classification of compact simply connected four-manifolds is radically different from their topological classification. In particular, he proved that the definite quadratic forms that can be realised as intersection forms of smooth four-manifolds are very restricted.

The proof used physics — the Yang-Mills equations and the moduli space of their solutions — to answer a pure mathematics question about four-manifolds. Atiyah called it "one of the most dramatic events in the recent history of mathematics." The Fields Medal was awarded to Donaldson in 1986.

The physics had crossed the boundary. Not just "physics uses mathematics" but "physics generates new mathematics."

### The Atiyah-Singer Index Theorem and Anomalies

The Atiyah-Singer index theorem (1963, proved 1968) relates the analytical index of an elliptic differential operator — the number of its zero modes — to topological invariants of the underlying manifold. In physics, the index of the Dirac operator in a gauge background gives the number of fermionic zero modes — and this number is exactly the instanton number (second Chern class) of the gauge field.

The physical consequence: the axial anomaly. The classical theory has a $U(1)$ axial symmetry, but the quantum theory does not — the symmetry is anomalous. The anomaly is computed by the index of the Dirac operator. This non-perturbative result connects the deepest topology with the physics of quarks and hadrons.

BRST cohomology — the framework I use for the Stueckelberg extension — is related to this. The BRST operator $s$ is nilpotent ($s^2 = 0$), making it formally analogous to the exterior derivative $d$ of de Rham cohomology. The physical observables are the cohomology of $s$, just as differential forms modulo exact forms are the de Rham cohomology. The physical operators are the $s$-closed operators modulo the $s$-exact ones.

### String Theory and the Fertilisation of Mathematics

String theory has not yet produced a single confirmed experimental prediction. It has produced an extraordinary amount of mathematics.

Mirror symmetry — the duality between two topologically distinct Calabi-Yau manifolds that give rise to the same string theory — was observed by physicists in the 1990s and used to compute the number of rational curves on the quintic threefold. The result (genus-0 curves: 2875, 609250, 317206375, ...) was verified by mathematicians who had not been able to compute these numbers by traditional methods. Kontsevich's proof using the physics-motivated machinery of Gromov-Witten theory earned him the Fields Medal.

The Seiberg-Witten invariants (1994) — topological invariants of four-manifolds derived from a supersymmetric gauge theory — replaced the technically more difficult Donaldson invariants in smooth topology. Physicists, by analysing the infrared behaviour of an $\mathcal{N}=2$ supersymmetric gauge theory, produced new tools for four-dimensional topology.

Monstrous moonshine — the unexpected connection between the Monster group (the largest sporadic simple group, with approximately $8 \times 10^{53}$ elements) and the $j$-function of modular forms — was proved by Borcherds using vertex operator algebras that had been developed in string theory. Borcherds received the Fields Medal in 1998.

The pattern is clear: when physics and mathematics work in close contact, each disciplines the other and produces results that neither could reach alone.

---

## A Personal Note on What This History Means

I did not learn this history before learning the physics and mathematics. I learned it alongside and after — reading Dyson's 1951 Cornell lectures as historical documents, finding Weyl in the history of gauge theory, tracing the fibre bundle formalism back through Ehresmann to Cartan to Riemann. The history changed how I understand the technical work.

Knowing that Riemann's 1854 geometry sat waiting for fifty years before Einstein needed it makes me less surprised that the mathematics of persistent homology — developed in pure topology — might turn out to be the right language for financial correlation networks. The pattern is too consistent to be coincidental. The universe is structured in a way that mathematics captures, and pure mathematicians working on abstract structures keep finding that physicists later need exactly those structures.

Understanding why Yang and Mills could not solve the mass problem in 1954 — and that it took twenty years of work by Higgs, 't Hooft, Veltman, Gross, Wilczek, and Politzer to make the theory viable — makes my own work on the Stueckelberg extension feel like a continuation of something real, not an isolated exercise.

History of science done from the inside is the recovery of why the problems were hard — not just what the solutions were. The hardness is informative. It tells you something about the structure of the questions.

---

*Last updated March 2026.*