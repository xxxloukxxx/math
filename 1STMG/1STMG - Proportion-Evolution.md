---
marp : true
header : Proportion / Évolution
footer : 1STMG - Lycée Paul Painlevé
size: 4k
---

# Proportion / Évolution

## 1STMG - Lycée Paul Painlevé

![bg fit right:50%](https://kronos-images.schoolmouv.fr/2-fnx-math-c17-img04.png)

---

# Proportion

## Proportion d'une quantité

Soit une population comprenant $N$ éléments et une sous-population comprenant $n$  éléments, la proportion de la sous-population par rapport à la population totale est :
 $$p=\dfrac{n}{N}$$

---

### Méthode : Calculer une proportion d'une sous-population

Sur les $480$ élèves inscrits en classe de 2GT , $108$ d'entre eux sont externes.

* La population totale des élèves de 2GT, notée $N$, est égale à 480.
* La sous-population des élèves externes, notée $n$, est égale à 108.
* La proportion d'élèves externes parmi tous les élèves de seconde, notée $p$, est :

$$p=\dfrac{n}{N}=\dfrac{108}{480}=0,225\qquad\text{soit}\qquad p=22,5\%$$

---

## Proportion d'une proportion

### Méthode : Calculer la proportion d'une quantité

Parmi les $480$ élèves de seconde, $15\%$ ont choisi l'option "sport".

$15\%$ **de** $480$ ont choisi "sport" soit :

$$15\%\times 480=\dfrac{15}{100}\times 480=72\text{ élèves}$$

---

### Méthode : Calculer une proportion de proportion

Dans un car, il y a $40\%$ de scolaires et, **parmi les scolaires**, $60\%$ sont des filles.

Soit :

* $C$ : l'ensemble de toutes les personnes dans le car.
* $S$ : l'ensemble des scolaires dans le car.
* $F$ : l'ensemble des scolaires filles.

---

* L'ensemble $F$ est inclus dans l'ensemble $S$ et on a :
$P_F = 60\%$ de $S$

* L'ensemble $S$ est inclus dans l'ensemble $C$ et on a :
$P_S = 40\%$ de $C$

La proportion de scolaires filles dans le CAR est donc égale à :

$\begin{aligned}
60\% \text{ de } 40\%  &= 60\% \times 40\% \\
                &= 0,6 \times 0,4= 0,24 = 24\%
\end{aligned}$

**Dans le car**, il y a $24\%$ de filles scolaires.

---

### Propriété

Soit "$A$ inclus dans $B$" et "$B$ inclus dans $C$".

* $p_1$ est la proportion de $A$ dans $B$.
* $p_2$ est la proportion de $B$ dans $C$.

Alors $p=p_1\times p_2$ est la proportion de $A$ dans $C$.

**Remarque :** "$A$ inclus dans $B$" se note $A\subset B$

---

# Évolution

## Taux d'évolution

On considère une valeur $V_0$ qui subit une évolution pour arriver à une valeur $V_1$.

Le **taux d'évolution** est égal à :

$$t=\dfrac{V_1-V_0}{V_0}$$

En pourcentage, le taux d'évolution est égal à :

$$t_\%=\dfrac{V_1-V_0}{V_0}\times 100$$

---

### Remarque

* Si $t>0$, l'évolution est une **augmentation**.
* Si $t<0$, l'évolution est une **diminution**.

### Exemple

La population d'un village est passé de $8~500$ à $10~400$ entre 2008 et 2012. Calculons le taux d'évolution de la population en $\%$.

$$t=\dfrac{V_1-V_0}{V_0}=\dfrac{10~400-8~500}{8~500}\approx+0,224\qquad\text{soit}\qquad\quad t_\%=+22,4\%$$

---

## Coefficient multiplicateur

* Faire **évoluer** une valeur de $\pm~t~\%$ revient à la **multiplier** par $CM=1+\dfrac{t_\%}{100}$
* $CM=1+\dfrac{t_\%}{100}$ est appelé **coefficient multiplicateur**

---

### Exemple

* Le prix d'un survêtement est de $49~$€. Il **augmente** de $8\%$. Son nouveau prix est :

$$\left(1 + \dfrac{8}{100}\right)\times 49 = 1,08 \times 49 = 52,25~€$$

* Le prix d'un polo est de $21~$€. Il **diminue** de $12\%$. Son nouveau prix est :

$$\left(1 + \dfrac{-12}{100}\right)\times 21 = 0,88 \times 21 = 18,48~€$$

---

### Propriété : Coefficient multiplicateur et $t_\%$

$$CM=1+\dfrac{t_\%}{100}\qquad\text{et}\qquad t_\% = \left(CM-1\right)\times 100$$

---

## Évolutions successives / taux global

Si une grandeur subit **plusieurs** évolutions successives alors le **coefficient multiplicateur global** est égal **au produit** des coefficients multiplicateurs de chaque évolution.

Le **taux d'évolution global** est le taux d'évolution associé au **coefficient multiplicateur global**.

---

### Exemple

Soit deux évolutions successives de $-20\%$ et $+30%$.

* $CM_1=\left(1+\dfrac{t_1}{100}\right)=\left(1+\dfrac{-20}{100}\right)=0,8$
* $CM_2=\left(1+\dfrac{t_2}{100}\right)=\left(1+\dfrac{+30}{100}\right)=1,3$
* $CM_{global}=CM_1\times CM_2=0,8\times 1,3=1,04$

---

Le **taux d'évolution global** est donc :

$\begin{aligned}
t_{global}  &=(CM_{global}-1)\times 100\\
            &=(1,04-1)\times 100 = +0,04 = +4\%
\end{aligned}$

Deux évolutions successives de $-20\%$ et $+30\%$ équivaut à une évolution de $+4\%$.

---

## Taux d'évolution réciproque

On considère le taux $t$ d'évolution de la valeur $V_0$ à la valeur $V_1$.

On appelle **taux évolution réciproque** le taux $t^\prime$ d'évolution de la valeur $V_1$ à la valeur $V_0$.

L'évolution **réciproque** possède un **coefficient multiplicateur inverse** de l'évolution directe.

---

### Exemple

Soit une évolution de $-20\%$.

* $CM_{direct}=\left(1+\dfrac{-20}{100}\right)=0,8$
* $CM_{réciproque}=\dfrac{1}{0,8}=1,25$

---

Le **taux d'évolution réciproque** est donc de :

$\begin{aligned}
t_{réciproque}  & =(CM_{réciproque}-1)\times 100\\
                & =(1,25-1)\times 100 = +0,25 = +25\%
\end{aligned}$


Si une valeur subit une **baisse** de $20\%$, il faut lui appliquer une **augmentation** de $25\%$ pour revenir à la valeur de départ.
