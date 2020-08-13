---
title: Fonctions et équations du 2^nd^ degré
subtitle: 1^ère^ Spécialité Math
lang: fr-FR
documentclass: scrartcl
geometry: "left=1.5cm,right=1.5cm,top=1.5cm,bottom=2.5cm"
numbersections: true
toc: true
toc-depth: 2
standalone: true
output: pdf_document
header-includes: |
  \usepackage{pgf,tikz,tkz-tab,pgfplots}
  \pgfplotsset{compat=1.15}
  \usepackage{mathrsfs}
  \usetikzlibrary{arrows}
---

---

# Définition et représentation

## Définition : Fonction du 2^nd^ degré
On appelle **fonction polynôme de degré 2** toute fonction $f$ définie sur $\mathbb{R}$ par une expression de la forme 

$$f\left( x \right) = ax^{2} + bx + c$$

où les coefficients **a**, **b** et **c** sont des réels donnés avec $a \neq 0$.

### Remarque : {-}

Une fonction polynôme de degré 2 s'appelle également fonction **trinôme du second degré** ou par abus de langage **"trinôme"**.

### Exemples et contre-exemples : {-}

(1) $f\left( x \right) = 3x^{2} - 7x + 3$

> $f$ est une fonction du 2^nd^ degré avec $a=3$ , $b=-7$ et $c=3$

(2) $g\left( x \right) = \dfrac{1}{2}x^{2} - 5x + \dfrac{3}{5}$

> $g$ est une fonction du 2^nd^ degré avec $a=\dfrac{1}{2}$ , $b=-5$ et $c=\dfrac{3}{5}$

(3) $h\left( x \right) = 4 - 2x^{2}$

> $h$ est une fonction du 2^nd^ degré avec $a=-2$ , $b=0$ et $c=4$

(4) $k\left( x \right) = \left( x - 4 \right)\left( 5 - 2x \right)$

> $k$ est une fonction du 2^nd^ degré car $(x-4)(5-2x)=(5\times x)-(2x\times x)-(4\times 5)+(2\times 4x)$

> Donc $k(x)=-2x^2+13x-20  \Rightarrow a=-2$ , $b=13$ et $c=-20$

(5) $m\left( x \right) = 5x - 3$ 

> $m(x)$ est une fonction polynôme de degré 1 (fonction affine).

(6) $n\left( x \right) = 5x^{4} - 7x^{3} + 3x - 8$

> $n(x)$ est une fonction polynôme de degré 4.

## Variations et représentation graphique

### Exemple {-}

Soit la fonction $f$ définie sur $\mathbb{R}$ par : $f(x) = 2x^2-4x+5$. Pour représenter $f$ dans un repère, nous pouvons calculer quelques valeurs de $f(x)$.

- $f(-2)=2\times (-2)^2-4\times (-2)+5=21$
- $f(-1)=2\times (-1)^2-4\times (-1)+5=11$
- $f(0)=2\times (0)^2-4\times (0)+5=5$
- ...

|   $x$  | -2 | -1 | 0 | 1 | 2 |  3 |  4 |
|:------:|:--:|:--:|:-:|:-:|:-:|:--:|:--:|
| $f(x)$ | 21 | 11 | 5 | 3 | 5 | 11 | 21 |

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=0.2cm]
\begin{axis}[x=1.0cm,y=0.2cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-2.5,xmax=4.5,ymin=-2.0,ymax=25.0,xtick={-2.0,-1.0,...,4.0},ytick={-0.0,5.0,...,25.0},]
\clip(-2.5,-2.) rectangle (4.5,25.);
\draw[line width=1.pt,color=blue,smooth,samples=100,domain=-2.5:4.5] plot(\x,{2.0*(\x)^(2.0)-4.0*(\x)+5.0});
\begin{scriptsize}
\draw [fill=black] (3.,11.) circle (1.5pt);
\draw [fill=black] (2.,5.) circle (1.5pt);
\draw [fill=black] (1.,3.) circle (1.5pt);
\draw [fill=black] (0.,5.) circle (1.5pt);
\draw [fill=black] (-2.,21.) circle (1.5pt);
\draw [fill=black] (-1.,11.) circle (1.5pt);
\draw [fill=black] (4.,21.) circle (1.5pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

### Remarque {-}
- Dans un repère orthogonal $\left( O\ ;\overrightarrow{i},\ \overrightarrow{j} \right)$, la représentation graphique d'une fonction polynôme de degré 2 est une **parabole**.


### Propriété : Minimum et maximum

Soit $f$ une fonction polynôme de degré 2 définie par $f(x) = ax^2+bx+c$, avec $a \neq 0$.

- Si $a > 0$, $f$ admet un **minimum** pour $x=\dfrac{-b}{2a}$. Ce **minimum** est égal à $f\left(\dfrac{-b}{2a}\right)$.
- Si $a < 0$, $f$ admet un **maximum** pour $x=\dfrac{-b}{2a}$. Ce **maximum** est égal à $f\left(\dfrac{-b}{2a}\right)$.

On appelle $\alpha$ la valeur $\dfrac{-b}{2a}$ et $\beta$ la valeur $f\left(\dfrac{-b}{2a}\right)$. $\alpha=\dfrac{-b}{2a}$ et $\beta=f\left(\dfrac{-b}{2a}\right)$.

### Propriété : Variations de $f(x)=ax^2+bx+c$

Nous pouvons résumer la variation d'une fonction du 2^nd^ degré par le tableau ci-dessous :

\begin{center}
\begin{tabular}{c|c}
$a<0$ & $a>0$ \\
\hline \quad  &  \quad \\
\begin{tikzpicture}
   \tkzTabInit[lgt = 1.5, espcl = 1.7]{$x$ / 0.75 , $f(x)$ / 2}{$-\infty$, $-\frac{b}{2a}$, $+\infty$}
   \tkzTabVar{-/ $-\infty$, +/ $f(\frac{-b}{2a})$, -/ $-\infty$}
\end{tikzpicture}
&
\begin{tikzpicture}
   \tkzTabInit[lgt = 1.5, espcl = 1.7]{$x$ / 0.75 , $f(x)$ / 2}{$-\infty$, $-\frac{b}{2a}$, $+\infty$}
   \tkzTabVar{+/ $+\infty$, -/ $f(\frac{-b}{2a})$, +/ $+\infty$}
\end{tikzpicture} \\
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.5cm,y=0.5cm]
\begin{axis}[x=0.5cm,y=0.5cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-3.0,xmax=4.5,ymin=-1.5,ymax=6.0,xtick={0},ytick={0},]
\clip(-3.,-1.5) rectangle (4.5,6.);
\draw[line width=1.2pt,color=blue,smooth,samples=100,domain=-2.0:4.5] plot(\x,{-0.75*((\x)-1.5)^(2.0)+3.7});
\draw [line width=0.5pt,dash pattern=on 1pt off 1pt,color=blue] (1.5,0.)-- (1.5,3.7);
\draw [line width=0.5pt,dash pattern=on 1pt off 1pt,color=blue] (0.,3.7)-- (1.5,3.7);
\draw [color=red](1.2268850945058474,0.07080942721391516) node[anchor=north west] {$\frac{-b}{2a}$};
\draw [color=red](-2.6184962079322918,4.5227752248167786) node[anchor=north west] {$f\left(\frac{-b}{2a}\right) $};
\begin{scriptsize}
\draw [fill=black] (1.5,3.7) circle (1.5pt);
\draw[color=black] (1.45,4.2) node {$M$};
\end{scriptsize}
\end{axis}
\end{tikzpicture}
&
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.5cm,y=0.5cm]
\begin{axis}[x=0.5cm,y=0.5cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-3.0,xmax=4.5,ymin=-1.5,ymax=6.0,xtick={0},ytick={0},]
\clip(-3.,-1.5) rectangle (4.5,6.);
\draw[line width=1.2pt,color=blue,smooth,samples=100,domain=-2.0:4.5] plot(\x,{0.75*((\x)-1.5)^(2.0)+1.7});
\draw [line width=0.5pt,dash pattern=on 3pt off 3pt,color=blue] (1.5,0.)-- (1.5,1.7);
\draw [line width=0.5pt,dash pattern=on 3pt off 3pt,color=blue] (0.,1.7)-- (1.5,1.7);
\draw [color=red](1.2268850945058474,0.07080942721391516) node[anchor=north west] {$\frac{-b}{2a}$};
\draw [color=red](-2.6184962079322918,2.5227752248167786) node[anchor=north west] {$f\left(\frac{-b}{2a}\right) $};
\begin{scriptsize}
\draw [fill=black] (1.5,1.7) circle (1.5pt);
\draw[color=black] (1.45,2.2) node {$M$};
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{tabular}
\end{center}

Il existe un moyen pour se souvenir du résultat précedent :

![](media/img03.png){width="40%"}

### Méthode : Etudier les variations d'une fonction du 2^nd^ degré {-}

> Étudier les variations de la fonction $f$ définie sur $\mathbb{R}$ par $f\left( x \right) = -x^{2} + 4x - 1$.

On a $f(x)=-x^{2}+4x-1$, donc $a=-1$ , $b=4$ et $c=-1$. 

$\alpha=\dfrac{-b}{2a} = \dfrac{-4}{2\times (-1)}= 2$ et $\beta=f(\alpha)=f(2)=-(2)^2+4\times 2 -1 =3$ 

Le sommet de la parabole est le point $S(2;3)$.

$a<0$ donc le tableau de variation de $f$ est :
\begin{center}
\begin{tikzpicture}
   \tkzTabInit{$x$ / 0.75 , $f(x)$ / 1.5}{$+\infty$, $2$, $+\infty$}
   \tkzTabVar{-/ $-\infty$, +/ $3$, -/ $-\infty$}
\end{tikzpicture}
\end{center}

Et sa représentation graphique est :

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[x=1.0cm,y=1.0cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-0.5,xmax=4.5,ymin=-1.5,ymax=4.0,xtick={-0.0,1.0,...,4.0},ytick={-1.0,0.0,...,4.0},]
\clip(-0.5,-1.5) rectangle (4.5,4.);
\draw[line width=2.pt,color=blue,smooth,samples=100,domain=-0.5:4.5] plot(\x,{0-(\x)^(2.0)+4.0*(\x)-1.0});
\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,3.)-- (2.,3.);
\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,3.)-- (2.,0.);
\begin{scriptsize}
\draw [color=black] (2.,3.)-- ++(-2.5pt,-2.5pt) -- ++(5.0pt,5.0pt) ++(-5.0pt,0) -- ++(5.0pt,-5.0pt);
\draw[color=black] (2.0951127605442115,3.252050267803505) node {$S$};
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

---

# Forme factorisée

Il se peut que le polynôme du 2^nd^ degré ne se présente pas sous la forme **developpée** mais sous une forme **factorisée** comme par exemple : $f(x)= (x-1)(x-2)$

En effet :

$\begin{aligned}
f(x) & = (x-1)(x-2) \\
     & = x^2-2x-1x+2 \\
     & = x^2-3x+2 \\
     & \Rightarrow a=1 \text{ , } b=-3 \text{ et } c=2
\end{aligned}$

## Définition

Soit $f$ une fonction définie sur $\mathbb{R}$ tel que : $$f(x)=a(x-x_1)(x-x_2)$$

$f$ est la forme **factorisée** d'une fonction du 2^nd^ degré.

$x_1$ et $x_2$ sont les **racines** de $f$

### Remarque {-}

les **racines** de $f$ sont solutions de l'équation $f(x)=0$.

$f(x_1) = a(x_1 - x_1)(x_1 - x_2)=0$ et $f(x_2) = a(x_2 - x_1)(x_2 - x_2)=0$.

### Exemples {-}

(1) $f(x)=3(x-1)(x+2)$

> $f(x)=3(x-1)\left(x- \left(-2\right)\right)$

> $f$ est une fonction du 2^nd^ degré sous forme factorisée avec $a=3$ , $x_1=1$ et $x_2=-2$

(2) $f(x)=(2x-6)(x-12)$

> Pour faire apparaître la forme factorisée il faut modifier l'écriture de $(2x-6)$

> $(2x-6)=2(x-3)$  donc $f(x)=2(x-3)(x-12)$

> $f$ est une fonction du 2^nd^ degré avec $a=2$ , $x_1=3$ et $x_2=12$

(3) $f(x)=(3-x)(2x+1)$

> On a $(3-x)=-(x-3)$ et $(2x+1)=2\left(x+\dfrac{1}{2}\right)$

> Donc $f(x)=-(x-3)\times 2\left(x+\dfrac{1}{2}\right)=-2(x-3)\left(x+\dfrac{1}{2}\right)$

> $f$ est une fonction du 2^nd^ degré avec $a=-2$ , $x_1=3$ et $x_2=-\dfrac{1}{2}$

## Propriété : Racines de $f(x)$

Soit $f$ une fonction définie sur $\mathbb{R}$ tel que $f(x)=ax^2+bx+c$ et $x_1$ ,$x_2$ les solutions de l'équation $f(x)=0$.

Alors la forme **factorisée** de $f$ est : $f(x)=a(x-x_1)(x-x_2)$

### Exemple {-}

Soit $f(x)=3(x-1)(x+2)$.

> $f$ est une fonction du 2^nd^ degré sous forme factorisée avec $a=3$ , $x_1=1$ et $x_2=-2$.

> D'autre part, $f(x)=3\left(x^2 + 2x - 1x -2\right)=3x^2+3x-6$

> Donc $x_1=1$ et $x_2=-2$ sont solutions de l'équation $3x^2+3x-6=0$

---

# Résolution d'équations du 2^nd^ degré

Résourdre une équation du 2^nd^ degré, c'est résoudre une équation du type $ax^2+bx+c=0$.

## Définition : Discriminant

On appelle **discriminant** du trinôme $ax^{2} + bx + c$, le nombre réel, noté $\Delta$, égal à $b^{2} - 4ac$.

$$\Delta = b^2-4ac$$

## Propriété : Solutions de $ax^2+bx+c=0$

Soit $\Delta$ le discriminant du trinôme $ax^{2} + bx + c$.

- Si $\Delta < 0$ : L'équation $ax^{2} + bx + c = 0$ n'a **pas de solution réelle**.
- Si $\Delta = 0$ : L'équation $ax^{2} + bx + c = 0$ a **une unique solution** : $x_{0}=\dfrac{- b}{2a}$.
- Si $\Delta > 0$ : L'équation $ax^{2} + bx + c = 0$ a **deux solutions distinctes** :

\begin{center}
$x_{1} =$ $\dfrac{- b - \sqrt{\Delta}}{2a}$\quad et\quad $x_{2} =\dfrac{- b + \sqrt{\Delta}}{2a}$.
\end{center}

### Méthode : Résoudre $ax^2+bx+c=0$ {-}

Résoudre les équations suivantes :

(1) $2x^{2} - x - 6 = 0$

> Calculons le discriminant de l'équation $2x^{2} - x - 6 = 0$ :

> *a* $= 2$, *b* $= -1$ et *c* $= -6$ donc $\Delta = b^{2} - 4ac = (-1)^{2} - 4\times 2 \times (-6) = 49$.

> Comme $\Delta > 0$, l'équation possède deux solutions distinctes :

\begin{center}
\begin{tabular}{c|c}
$\begin{aligned}
x_{1} &=\dfrac{-b-\sqrt{\Delta}}{2a}\\
      &=\dfrac{-\left(-1\right)-\sqrt{49}}{2\times 2}\\
      &=-\dfrac{3}{2}
\end{aligned}$
&
$\begin{aligned}
x_{1} &=\dfrac{-b+\sqrt{\Delta}}{2a}\\
      &=\dfrac{-\left(-1\right)+\sqrt{49}}{2\times 2}\\
      &=2
\end{aligned}$
\end{tabular}
\end{center}

> Les solutions de l'équation $2x^{2} - x - 6 = 0$ sont $S=\left\{ -\dfrac{3}{2} ; 2 \right\}$

(2) $2x^{2} - 3x + \dfrac{9}{8} = 0$

> Calculons le discriminant de l'équation $2x^{2} - 3x + \dfrac{9}{8} = 0$ :

> *a* $= 2$, *b* $= -3$ et *c* $= \dfrac{9}{8}$ donc $\Delta = b^{2} - 4ac = (-3)^{2}- 4\times 2 \times \dfrac{9}{8} = 0$.

> Comme $\Delta = 0$, l'équation possède une unique solution : $x_{0}=-\dfrac{b}{2a}=-\dfrac{-3}{2 \times 2}=\dfrac{3}{4}$

(3) $x^{2} + 3x + 10 = 0$

> Calculons le discriminant de l'équation $x^{2} + 3x + 10 = 0$ :

> *a* $= 1$, *b* $= 3$ et *c* $= 10$ donc $\Delta = b^{2} - 4ac = 3^{2} - 4 \times 1 \times 10 = -31$.

> Comme $\Delta < 0$, l'équation ne possède pas de solution réelle.

### Propriété {-}

La somme *S* et le produit *P* des **racines** d’un polynôme du 2^nd^ degré de la forme $ax^{2} + bx + c = 0$ sont donnés par :

\begin{center}
$S=-\dfrac{b}{a}$\quad et\quad $P=\dfrac{c}{a}$
\end{center}

### Démonstration {-}

Soit $x_1$ et $x_2$ les solutions de $x^2+bx+c=0$ alors $x_{1}=\dfrac{-b-\sqrt{\Delta}}{2a}$ et $x_{2}=\dfrac{-b+\sqrt{\Delta}}{2a}$

Donc, la somme des **racines** est $S=x_1 + x_2$ :

$\begin{aligned}
S & = x_1 + x_2\\
  & = \dfrac{-b-\sqrt{\Delta}}{2a}+\dfrac{-b+\sqrt{\Delta}}{2a}\\
  & = \dfrac{(-b-\sqrt{\Delta})+(-b+\sqrt{\Delta})}{2a}\\
  & = \dfrac{-2b}{2a} = \dfrac{-b}{a}
\end{aligned}$

Le produit des **racines** est $P=x_1 \times x_2$ :

$\begin{aligned}
P & = x_1 \times x_2\\
  & = \dfrac{-b-\sqrt{\Delta}}{2a} \times \dfrac{-b+\sqrt{\Delta}}{2a}\\
  & = \dfrac{(-b-\sqrt{\Delta})\times(-b+\sqrt{\Delta})}{2a\times 2a}\\
  & = \dfrac{ (-b)^2 + \left((-b) \times \sqrt{\Delta}\right) + \left(\left(-\sqrt{\Delta}\right) \times (-b)\right) + \left(\left(-\sqrt{\Delta}\right) \times \sqrt{\Delta}\right) }{4a^2}\\
  & = \dfrac{b^2 - \Delta}{4a^2} = \dfrac{b^2 - (b^2-4ac)}{4a^2} = \dfrac{4ac}{4a^2}\\
  & = \dfrac{c}{a}
\end{aligned}$

## Propriété : Forme factorisée de $ax^2+bx+c$

Soit $f$ une fonction polynôme de degré $2$ définie sur par $f\left( x \right) = ax^{2} + bx + c$.

- Si $\Delta = 0$ : Pour tout réel $x$, on a : $f\left( x \right) = a\left( x - x_{0} \right)^{2}$.

- Si $\Delta > 0$ : Pour tout réel $x$, on a : $f\left( x \right) = a\left( x - x_{1} \right)\left( x - x_{2} \right)$.

### Remarque {-}
Si $\Delta < 0$, il n’existe pas de forme factorisée de $f$.

### Méthode : Factoriser un trinôme {-}

Factoriser les trinômes suivants :

(1) ${4x}^{2} + 19x - 5$

> On cherche les racines du trinôme ${4x}^{2} + 19x - 5$

> On a $a=4$ , $b=19$ et $c=-5$ donc $\Delta = 19^2 - 4 \times 4 \times (-5) = 441$

> Les racines du trinôme sont : 

\begin{center}
\begin{tabular}{c|c}
$\begin{aligned}
x_{1} & = \dfrac{-19 - \sqrt{441}}{2 \times 4}\\
      & = -5
\end{aligned}$
&
$\begin{aligned}
x_{2} & = \dfrac{- 19 + \sqrt{441}}{2 \times 4}\\
     & = \dfrac{1}{4}
\end{aligned}$
\end{tabular}
\end{center}

> On a donc :

> $\begin{aligned}
{4x}^{2}+19x-5 & = 4\left(x-\left(-5\right)\right)\left(x-\dfrac{1}{4}\right)\\
               & = 4\left(x+5\right)\left(x-\dfrac{1}{4}\right) \text{  ou  } (x+5)(4x-1)
\end{aligned}$

> Une vérification à l'aide de la calculatrice n'est jamais inutile \! On peut lire une valeur approchée des racines sur l'axe des abscisses.

![](media/img05.png){width="40%"}
![](media/img06.png){width="40%"}

(2) ${9x}^{2} - 6x + 1$

> On cherche les racines du trinôme ${9x}^{2} - 6x + 1$

> On a $a=9$ , $b=-6$ et $c=1$ donc $\Delta = (-6)^2 - 4 \times 9 \times (1) = 0$

> La racine du trinôme est : $x_{0} = \dfrac{-(-6)}{2 \times 9} = \dfrac{1}{3}$

> On a donc : ${9x}^{2}-6x+1=9\left(x-\dfrac{1}{3}\right)^2$

## Propriété : Les différentes représentations possibles de $f$

En fonction du signe de $a$ et de $\Delta$, nous pouvons en déduire les représentations de $f$.

> $a>0$

|             $\Delta>0$            |             $\Delta=0$            |             $\Delta<0$            |
|:---------------------------------:|:---------------------------------:|:---------------------------------:|
| ![](media/img11.png){width="5cm"} | ![](media/img13.png){width="5cm"} | ![](media/img12.png){width="5cm"} |

---

> $a<0$

|             $\Delta>0$            |             $\Delta=0$            |             $\Delta<0$            |
|:---------------------------------:|:---------------------------------:|:---------------------------------:|
| ![](media/img14.png){width="5cm"} | ![](media/img15.png){width="5cm"} | ![](media/img16.png){width="5cm"} |

---

# Forme canonique

## Définition : Forme canonique

Toute fonction polynôme $f$ de degré 2 définie sur $\mathbb{R}$ par $f\left( x \right) = ax^{2} + bx + c$ peut s'écrire sous la forme :

$$f\left( x \right) = a\left( x - \alpha \right)^{2} + \beta$$

où $\alpha$ et $\beta$ sont deux nombres réels.

Cette dernière écriture s'appelle la **forme canonique** de $f$.

### Exemple {-}

$f(x)=2(x-1)^2+3$ est une fonction du 2^nd^ degré sous forme **canonique** avec $a=2$ , $\alpha=1$ et $\beta=3$.

> En effet,

> $\begin{aligned}f(x) & = 2(x-1)^2+3 \\ & = 2(x^2-2x+1)+3 \\ & = 2x^2-4x+2+3 \\ & = 2x^2-4x+5\end{aligned}$

> Donc $a=2$ , $b=-4$ et $c=5$

### Méthode : Déterminer la forme canonique d'une fonction du 2^nd^ degré {-}

Soit la fonction $f$ définie sur $\mathbb{R}$ par : $f\left( x \right) = 2x^{2} - 20x + 10$. On veut exprimer la fonction $f$ sous sa forme canonique.

> $f\left( x \right) =\left(x -\alpha \right)^2 + \beta$ où $\alpha$ et $\beta$ sont des nombres réels.

> $\begin{aligned}
f\left(x\right) & = 2x^{2}-20x+10\\
                & = 2\left\lbrack x^{2}-10x\right\rbrack+10\\
                & = 2\left\lbrack x^{2}-10x+25-25\right\rbrack+10\\
                & = 2\left\lbrack\left(x-5\right)^{2}-25\right\rbrack+10\\
                & = 2\left(x-5\right)^{2}-50+10\\
                & = 2\left(x-5\right)^{2}-40
\end{aligned}$

> On a donc $\alpha=5$ et $\beta=-40$

> $f(x) = 2\left( x - 5 \right)^{2} - 40$ est la forme **canonique** de $f$.

### Démonstration : {-}

Comme $a \neq 0$, on peut écrire pour tout réel $x$ :

$\begin{aligned}
f\left( x \right) & =  ax^{2} + bx + c \\
                  & =  a\left\lbrack x^{2}+\frac{b}{a}x\right\rbrack + c \\
                  & =  a\left\lbrack x^{2}+\frac{b}{a}x+\left(\frac{b}{2a}\right)^{2}-\left(\frac{b}{2a}\right)^{2}\right\rbrack + c \\
                  & =  a\left\lbrack \left( x + \frac{b}{2a} \right)^{2} - \left( \frac{b}{2a} \right)^{2} \right\rbrack + c \\
                  & =  a\left( x + \frac{b}{2a} \right)^{2} - a\frac{b^{2}}{4a^{2}} + c \\
                  & =  a\left( x + \frac{b}{2a} \right)^{2} - \frac{b^{2}}{4a} + c \\
                  & =  a\left( x + \frac{b}{2a} \right)^{2} - \frac{b^{2} - 4ac}{4a} \\
                  & =  a\left( x - \alpha \right)^{2} + \beta
\end{aligned}$

avec $\alpha = -$ $\dfrac{b}{2a}$ et $\beta = f(\alpha) = - \dfrac{b^{2} - 4ac}{4a}$.

### Remarque :{-}
Pour écrire un trinôme sous sa forme canonique, il est possible d’utiliser les deux dernières formules donnant $\alpha$ et $\beta$.

### Méthode : Déterminer la forme canonique d'une fonction du 2^nd^ degré (simple) {-}

Soit la fonction $f$ définie sur $\mathbb{R}$ par : $f\left( x \right) = 2x^{2} - 20x + 10$. On veut exprimer la fonction $f$ sous sa forme canonique.

> On a $a=2$ , $b=-20$ et $c=10$ donc 

> $\begin{aligned}
\alpha & = -\dfrac{b}{2a}\\
       & = -\dfrac{-20}{2\times 2}\\
       & = 5
\end{aligned}$

> Calculons $\beta$ :

> $\begin{aligned}
\beta & = f(\alpha) \\
      & = 2\times 5^{2} - 20\times 5 + 10\\
      & = 50-100+10 = 40
\end{aligned}$

> On a donc $\alpha=5$ et $\beta=-40$  donc $f(x) = 2\left( x - 5 \right)^{2} - 40$

### Exemple : {-}

Soit la fonction $f$ donnée sous sa forme canonique par : $f\left( x \right) = 2\left( x - 1 \right)^{2} + 3$

Alors : $f(x) \geq 3$ car $2\left( x - 1 \right)^{2}$ est positif.

Or $f\left( 1 \right) = 3$ donc pour tout $x$, $f\left( x \right) \geq f(1)$.

$f$ admet donc un minimum en $x=1$. Ce minimum est égal à $3$.

## Propriété : Minimum et maximum

Soit $f$ une fonction polynôme de degré 2 définie par $f(x) = a\left( x - \alpha \right)^{2} + \beta$, avec $a \neq 0$.

- Si $a > 0$, $f$ admet un minimum pour $x = \alpha$. Ce minimum est égal à $\beta$.
- Si $a < 0$, $f$ admet un maximum pour$\ x = \alpha$. Ce maximum est égal à $\beta$.

### Remarque : {-}

Soit la fonction $f$ définie sur $\mathbb{R}$ par : $f\left( x \right) = ax^{2} + bx + c$, avec $a \neq 0$.

On peut retenir que $f$ admet un maximum (ou un minimum) pour $x = -\frac{b}{2a}$.

### Méthode : Déterminer les caractéristiques d’une parabole {-}

Déterminer l’axe de symétrie et le sommet de la parabole d’équation $y = 2x^{2} - 12x + 1$.

La parabole possède un axe de symétrie d'équation $x = -\frac{b}{2a}$, soit $x = -\frac{- 12}{2 \times 2} = 3$.

La droite d’équation $x = 3$ est donc axe de symétrie de la parabole d’équation $y = 2x^{2} - 12x + 1$.

Les coordonnées de son sommet sont : $\left( - \frac{b}{2a}\ ;\ f\left( - \frac{b}{2a} \right) \right)$, soit : $\left( 3\ ;2 \times 3^{2} - 12 \times 3 + 1 \right) = \left( 3\ ;\  - 17 \right)$.

Le point de coordonnées $\left( 3\ ;\  - 17 \right)$ est donc le sommet de la parabole.

$a = 2 > 0$, ce sommet correspond à un minimum.

![](media/img04.png){width="60%"}

\newpage

### Démonstration : Solutions de l'équation $ax^2+bx+c=0$ {-}

La fonction $f$ définie sur $\mathbb{R}$ par $f\left( x \right) = ax^{2} + bx + c$ peut s'écrire sous sa forme canonique :

$f(x) = a\left( x - \alpha \right)^{2} + \beta$ avec $\alpha = -\frac{b}{2a}$ et $\beta =- \frac{b^{2} - 4ac}{4a}$.

Donc :

$ax^{2} + bx + c = 0$ peut s’écrire : 

$\begin{aligned}
a\left( x + \frac{b}{2a} \right)^{2} - \frac{b^{2} - 4ac}{4a}  & = 0 \\
     a\left( x + \frac{b}{2a} \right)^{2} - \frac{\Delta}{4a}  & = 0 \\
                         a\left( x + \frac{b}{2a} \right)^{2}  & = \frac{\Delta}{4a} \\
                          \left( x + \frac{b}{2a} \right)^{2}  & = \frac{\Delta}{4a^{2}} \text{\quad car  } a \neq 0
\end{aligned}$

- Si $\Delta < 0$ : 
Comme un carré ne peut être négatif $\left( \frac{\Delta}{4a^{2}} < 0 \right)$, l'équation $ax^{2} + bx + c = 0$ n'a pas de solution.

- Si $\Delta = 0$ : 
L'équation $ax^{2} + bx + c = 0$ peut s'écrire : $\left( x + \frac{b}{2a} \right)^{2} = 0$

L'équation n'a qu'une seule solution : $x = \frac{-b}{2a}$

- Si $\Delta > 0$ : L'équation $ax^{2} + bx + c = 0$ est équivalente à :

\begin{tabular}{|cc|c}
$\begin{aligned}
x + \frac{b}{2a} & = +\sqrt{\frac{\Delta}{4a^{2}}} \\
               x & = +\sqrt{\frac{\Delta}{4a^{2}}} - \frac{b}{2a} \\
               x & = \frac{+\sqrt{\Delta}}{2a} - \frac{b}{2a} \\
               x & = \frac{+\sqrt{\Delta}-b}{2a} \\
               x & = \frac{-b+\sqrt{\Delta}}{2a}
\end{aligned}$
& et &
$\begin{aligned}
x + \frac{b}{2a}  & = -\sqrt{\frac{\Delta}{4a^{2}}} \\
               x  & = -\sqrt{\frac{\Delta}{4a^{2}}} - \frac{b}{2a} \\
               x  & = \frac{-\sqrt{\Delta}}{2a} - \frac{b}{2a} \\
               x  & = \frac{-\sqrt{\Delta}-b}{2a} \\
               x  & = \frac{-b-\sqrt{\Delta}}{2a}
\end{aligned}$
\end{tabular}

L'équation a deux solutions distinctes :

$x_1 = \frac{-b+\sqrt{\Delta}}{2a}$ et $x_1 = \frac{-b-\sqrt{\Delta}}{2a}$