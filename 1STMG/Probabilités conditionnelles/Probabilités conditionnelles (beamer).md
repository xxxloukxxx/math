---
title: Probabilités conditionnelles
subtitle: 1^ère^ STMG
lang: fr-FR
aspectratio: 1610
numbersections: true
navigation: empty
standalone: true
theme: Singapore
header-includes: |
  \usepackage{pgf,tikz,tkz-tab,pgfplots}
  \pgfplotsset{compat=1.15}
  \usepackage{mathrsfs}
  \usetikzlibrary{arrows}
---

# Calculs à l'aide d'un tableau croisé

---

## Définition : Probabilité conditionelle

. . .

On appelle **probabilité conditionnelle** de **B** sachant **A**, la probabilité que l'événement **B** se réalise **sachant que** l'événement **A** est réalisé. On la note : $$P_{A}\left( B \right)$$.

---

## Méthode : Calculer une probabilité conditionnelle à l'aide d'un tableau croisé

Un laboratoire pharmaceutique a réalisé des tests sur 800 patients atteints d'une maladie. Certains sont traités avec le médicament A, d'autres avec le médicament B.

. . .

Le tableau présente les résultats de l'étude :

              Médicament A   Médicament B   Total
  ----------- -------------- -------------- -------
  Guéri       383            291            674
  Non guéri   72             54             126
  Total       455            345            800

. . .

On choisit au hasard un patient et on considère les évènements suivants :

A : "Le patient a pris le médicament A."

G : "Le patient est guéri."

---

> a) Calculer $P\left( A \right)$ 
> b) Calculer $P\left( G \right)$
> c) Calculer $P\left( G \cap A \right)$
> d) Calculer $P\left( \overline{G} \cap A \right)$
> e) On choisit maintenant au hasard un patient guéri. Calculer la probabilité que le patient ait pris le médicament A **sachant qu**'il est guéri.
> f) On choisit maintenant au hasard un patient traité par le médicament B. Calculer la probabilité que le patient soit guéri **sachant qu**'il a pris le médicament B.

---

(a) La probabilité qu'un patient soit traité avec le médicament A est égale à : $$P\left( A \right) = \dfrac{455}{800} \approx 0,57 = 57\%$$

. . .

(b) La probabilité qu'un patient soit guéri est égale à : $$P\left( G \right) =\dfrac{674}{800}\approx 0,84 = 84\%$$

. . .

(c) La probabilité qu'un patient soit guéri et qu'il soit traité par le médicament A est égale à : $$P\left( G \cap A \right) =\dfrac{383}{800}\approx 0,48 = 48\%$$

. . .

(d) La probabilité qu'un patient ne soit pas guéri et qu'il soit traité par le médicament A est égale à : $$P\left( \overline{G} \cap A \right) =\dfrac{72}{800}\approx 0,09 = 9\%$$

---

(e) La probabilité que le patient ait pris le médicament A **sachant qu'il est guéri** se note $P_{G}\left( A \right)$

. . .

et est égale à $$P_{G}\left( A \right) =\dfrac{383}{674}\approx 0,57 = 57\%$$

. . .

On regarde uniquement **la ligne des patients guéris**.

. . .

f) La probabilité que le patient soit guéri **sachant qu'il a pris le médicament B** se note $P_{B}\left( G \right)$

. . .

et est égale à $P_{B}\left( G \right) =\dfrac{291}{345}\approx 0,84 = 84\%$.

. . .

On regarde uniquement **la colonne du médicament B**.

# Calculs à l'aide de la formule

---

## Propriété : Formule pour déterminer $P_{A}\left( B \right)$

Soit $A$ et $B$ deux événements de l'univers $\Omega$. La **probabilité conditionnelle** de **B** sachant **A** se calcule à l'aide de :

$$P_{A}\left( B \right) =\dfrac{card(A \cap B)}{card(A)}$$ 

. . .

On rappelle que **Cardinal de A**, noté $\text{card}\left(A\right)$, désigne le nombre d'issues de l'événement $A$.

---

## Méthode : Calculer une probabilité conditionnelle à l'aide de la formule

Un sac contient $50$ boules, dont :

- $20$ boules rouges,
- $30$ boules noires,

. . .

où il est marqué soit "_Gagné_" ou soit "_Perdu_".

- Sur $15$ boules rouges, il est marqué _Gagné_.
- Sur $9$ boules noires, il est marqué _Gagné_.

. . .

On tire au hasard une boule dans le sac.

Soit $R$ l'événement "On tire une boule rouge"

Soit $G$ l'événement "On tire une boule marquée Gagné"

Soit $R \cap G$ est l'événement "On tire une boule rouge marquée Gagné".

---

Calculer la probabilité de ...

> a) ... tirer une boule marquée _Gagné_ **sachant qu'elle est rouge**.
> b) ... tirer une boule marquée _Gagné_ **sachant qu'elle est noire**.

---

(a) Sur 15 boules rouges, il est marqué Gagné, donc $\text{card}\left(R \cap G\right)=15$.

. . .

Le sac contient 20 boules rouges, donc $\text{card}\left(R\right)=20$.

. . .

$$P_{R}\left( G \right) = \dfrac{\text{card}\left( R \cap G \right)}{\text{card}\left( R \right)} = \dfrac{15}{20} = 0,75.$$

. . .

b\) Sur 9 boules noires, il est marqué Gagné, donc $\text{card}\left( \overline{R} \cap G \right) = 9$.

. . .

$\overline{R}$ désigne l'événement "On tire une boule qui n'est pas rouge", soit "On tire une boule qui est noire".

Le sac contient 30 boules noires, donc $\text{Card}\left( \overline{R} \right) = 30$.

. . .

$$P_{\overline{R}}\left( G \right) = \dfrac{\text{Card}\left( \overline{R} \cap G \right)}{\text{Card}\left( \overline{R} \right)} = \dfrac{9}{30} = 0,3.$$