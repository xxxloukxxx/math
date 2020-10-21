---
title: Généralités sur les fonctions
subtitle: 1^ère^ STMG
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

\newpage

# Définitions, notations et représentation graphique

### Exemple {-}

On considère la fonction $f$ qui exprime l'aire d'un rectangle de dimensions 3 et $x$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\clip(0,0) rectangle (7,5);
\fill[line width=2.pt,color=red,fill=red,fill opacity=0.1] (1.,1.) -- (1.,4.) -- (6.,4.) -- (6.,1.) -- cycle;
\draw [line width=2.pt,color=red] (1.,1.)-- (1.,4.);
\draw [line width=2.pt,color=red] (1.,4.)-- (6.,4.);
\draw [line width=2.pt,color=red] (6.,4.)-- (6.,1.);
\draw [line width=2.pt,color=red] (6.,1.)-- (1.,1.);
\draw (3.45,4.5) node[anchor=north west] {$x$};
\draw (0.5,2.8) node[anchor=north west] {$3$};
\draw (1.5,2.8) node[anchor=north west] {$\text{Aire de ABCD} = 3 \times x$};
\draw [color=black] (1.,1.)-- ++(-2.5pt,-2.5pt) -- ++(5.0pt,5.0pt) ++(-5.0pt,0) -- ++(5.0pt,-5.0pt);
\draw[color=black] (0.8,0.9) node {$A$};
\draw [color=black] (1.,4.)-- ++(-2.5pt,-2.5pt) -- ++(5.0pt,5.0pt) ++(-5.0pt,0) -- ++(5.0pt,-5.0pt);
\draw[color=black] (0.75,4.20) node {$B$};
\draw [color=black] (6.,4.)-- ++(-2.5pt,-2.5pt) -- ++(5.0pt,5.0pt) ++(-5.0pt,0) -- ++(5.0pt,-5.0pt);
\draw[color=black] (6.1,4.25) node {$C$};
\draw [color=black] (6.,1.)-- ++(-2.5pt,-2.5pt) -- ++(5.0pt,5.0pt) ++(-5.0pt,0) -- ++(5.0pt,-5.0pt);
\draw[color=black] (6.2,0.9) node {$D$};
\end{tikzpicture}
\end{center}

Une expression littérale de $f$ est donc : $f\left( x \right) = 3\times x$.

## Définition : Fonction

Une fonction $f$ associe à tout nombre réel $x$ un unique nombre réel, noté $f\left(x\right)$.

On note également : $x \longmapsto f \left(x\right)$ \quad ou \quad $y = f\left(x\right)$.

## Image et antécédent

Pour la fonction $f$ définie plus haut, on a : $f\left(1\right)=3\times 1=3$ et $f\left(4\right)=3\times 4 = 12$

On dit que :

- l'**image** de $1$ par la fonction $f$ est 3.  $1 \longmapsto 3$
- un **antécédent** de $3$ par $f$ est $1$.

\begin{center}
\tikzset{every picture/.style={line width=0.75pt}}
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
\draw    (110,120) .. controls (110.49,91.97) and (120.01,100.77) .. (147.82,81.54) ;
\draw [shift={(150,80)}, rotate = 504.23] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
\draw    (250,120) .. controls (250.49,92.11) and (238.74,98.33) .. (212.48,81.62) ;
\draw [shift={(210,80)}, rotate = 393.81] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
\draw (155,62) node [anchor=north west][inner sep=0.75pt]   [align=left] {$\displaystyle 1\longmapsto 3$};
\draw (110,134.5) node   [align=left] {\begin{minipage}[lt]{81.60000000000001pt}\setlength\topsep{0pt}
\begin{center}
Antécédent de $\displaystyle 3$
\end{center}
\end{minipage}};
\draw (255,134.5) node   [align=left] {\begin{minipage}[lt]{74.80000000000001pt}\setlength\topsep{0pt}
\begin{center}
Image de $\displaystyle 1$
\end{center}
\end{minipage}};
\end{tikzpicture}
\end{center}

### Remarques {-}

- Un nombre possède **une unique image**.
- Cependant, un nombre peut posséder **plusieurs antécédents**.

\newpage

## Méthode : Calculer une image ou un antécédent

Soit la fonction $f$ définie par $f\left(x\right) = \sqrt{x} + 1$

> a) Compléter le tableau de valeurs ci-dessus

| $x$ | $4$ | $10,24$ | $16$ | $20,25$ |
|:-:|:-:|:-:|:-:|:-:|
| $f\left(x\right)$ | \quad | \quad | \quad | \quad |

> b) Compléter alors :
>     - L'image de 4 par $f$ est $\ldots$
>     - Un antécédent de 5 par $f$ est $\ldots$
>     - $f$ : $\ldots \longmapsto 4,2$
>     - $f\left(20,25\right) = \ldots$
> c) Calculer $f\left(4,41\right)$ et $f\left(1310,44\right)$

---

(a) Tableau de valeurs

| $x$ | $4$ | $10,24$ | $16$ | $20,25$ |
|:-:|:-:|:-:|:-:|:-:|
| $f\left(x\right)$ | **3** | **4,2** | **5** | **5,5** |

(b) 
  - L'image de $4$ par $f$ est **3**
  - Un antécédent de $5$ par $f$ est **16**
  - $f$ : **10,24** $\longmapsto 4,2$
  - $f\left(20,25\right) =$ **5,5**

(c) Images de $4,41$ et $1310,44$

$f\left(4,41\right) = \sqrt{4,41} + 1 =$ **3,1**

$f\left(1310,44\right) = \sqrt{1310,44} + 1 =$ **37,2**

\newpage

## Représentation graphique

On considère la fonction $f$ définie par $f\left( x \right) = 5x - x^{2}$.

On réalise le tableau de valeurs suivant :

  $x$                 1    1,5     2    2,5     3    3,5     4    4,5
  ----------------- - -- - ----- - -- - ----- - -- - ----- - -- - ------
  $f\left(x\right)$   4    5,25    6    6,25    6    5,25    4    2,25

On représente les données du tableau de valeurs dans un repère tel qu'on lise $x$ en abscisse et $f\left( x \right)$ en ordonnée. En reliant les points, on obtient la courbe $\mathcal{C}_f$.

\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=14cm,height=10cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-1,
xmax=6,
ymin=-1,
ymax=8,
xtick={-5.0,-4.0,...,14.0},
ytick={-2.0,-1.0,...,8.0},]
\draw[line width=2.5pt,color=red,smooth,domain=1:4.5] plot(\x,{5.0*(\x)-(\x)^(2.0)});
\draw[line width=1.5pt,dashed,color=red!80,smooth,domain=-1:1] plot(\x,{5.0*(\x)-(\x)^(2.0)});
\draw[line width=1.5pt,dashed,color=red!80,smooth,domain=4.5:6] plot(\x,{5.0*(\x)-(\x)^(2.0)});
\draw [fill=black] (1.,4.) circle (2.0pt);
\draw [fill=black] (1.5,5.25) circle (2.0pt);
\draw [fill=black] (2.,6.) circle (2.0pt);
\draw [fill=black] (2.5,6.25) circle (2.0pt);
\draw [fill=black] (3.,6.) circle (2.0pt);
\draw [fill=black] (3.5,5.25) circle (2.0pt);
\draw [fill=black] (4.,4.) circle (2.0pt);
\draw [fill=black] (4.5,2.25) circle (2.0pt);
\draw (3.5,6) node[anchor=north west] {$\mathcal{C}_f$};
\end{axis}
\end{tikzpicture}
\end{center}
\caption{Représentation graphique de $f\left(x\right)=5x-x^{2}$}
\end{figure}

Tous les points de la courbe $\mathcal{C}_f$ possèdent donc des coordonnées de la forme $\left(x ; f\left(x\right)\right)$.

La courbe représentative de la fonction $f$ dépasse les limites du tableau de valeurs : la fonction n'est pas limitée aux valeurs de $x\in[1;4.5]$. C'est pourquoi nous pouvons prolonger la courbe (en pointillé) dans la représentation ci-dessus.

\newpage

# Résolution graphique d'équations et d'inéquations

## Méthode : Résoudre graphiquement une équation ou une inéquation

Répondre **graphiquement** aux questions suivantes :

> a) Résoudre l'équation $5x - x^{2} = 4$
> b) Résoudre graphiquement l'inéquation $5x - x^{2} \geq 4$. Donner une interprétation du résultat.

---

(a) On considère la fonction $f$ définie par $f\left( x \right) = 5x - x^{2}$.

Il s'agit de trouver les antécédents de $4$ par la fonction $f$. Ce qui revient à résoudre l'équation $f(x) = 4$.

On détermine les abscisses des points d'intersection de la courbe $\mathcal{C}_f$ avec la droite $\Delta$ parallèle à l'axe des abscisses passant par le point $\left(0\quad;\quad4\right)$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=10cm,height=6cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-.5,xmax=5.5,ymin=-0.9,ymax=6.9,
xtick={-5.0,-4.0,...,14.0},
ytick={-2.0,-1.0,...,8.0},]
\draw [line width=1.5pt,color=red,smooth,samples=100,domain=-0.5:7] plot(\x,{5.0*(\x)-(\x)^(2.0)});
\draw [line width=1.5pt] (-5,4)-- (15,4);
\draw [->,line width=1.5pt,dash pattern=on 3pt off 3pt] (1,4)-- (1,0);
\draw [->,line width=1.5pt,dash pattern=on 3pt off 3pt] (4,4)-- (4,0);
\draw (5,5) node[anchor=north west] {$\Delta$};
\draw (3.5,6) node[anchor=north west] {$\mathcal{C}_f$};
\begin{scriptsize}
\draw [fill=green] (1,4) circle (2.5pt);
\draw [fill=green] (4,4) circle (2.5pt);
\draw [fill=black] (0,4) circle (2.5pt);
\draw [fill=green] (1,0) circle (2.5pt);
\draw [fill=green] (4,0) circle (2.5pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

On lit graphiquement que l'équation $5x - x^{2} = 4$ admet pour solutions : les nombres $1$ et $4$.

(b) Résoudre l'inéquation $5x - x^{2} \geq 4$ revient à déterminer les abscisses des points de $\mathcal{C}_f$ pour lesquels $\mathcal{C}_f$ est  **au-dessus** la droite $\Delta$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=10cm,height=6cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-.5,xmax=5.5,ymin=-0.9,ymax=6.9,
xtick={-5.0,-4.0,...,14.0},
ytick={-2.0,-1.0,...,8.0},]
\draw [line width=1.5pt] (-5,4)-- (15,4);
\draw [dashed,line width=1pt,color=red,smooth,domain=-0.5:1] plot(\x,{5.0*(\x)-(\x)^(2.0)});
\draw [line width=1.5pt,color=red,smooth,domain=1:4] plot(\x,{5.0*(\x)-(\x)^(2.0)});
\draw [dashed,line width=1pt,color=red,smooth,domain=4:7] plot(\x,{5.0*(\x)-(\x)^(2.0)});
\draw [->,line width=1.5pt,dash pattern=on 3pt off 3pt] (1,4)-- (1,0);
\draw [->,line width=1.5pt,dash pattern=on 3pt off 3pt] (4,4)-- (4,0);
\draw [line width=1.5pt,color=blue] (1,0)-- (4,0);
\draw (5,5) node[anchor=north west] {$\Delta$};
\draw (3.5,6) node[anchor=north west] {$\mathcal{C}_f$};
\begin{scriptsize}
\draw [fill=green] (1,4) circle (2.5pt);
\draw [fill=green] (4,4) circle (2.5pt);
\draw [fill=black] (0,4) circle (2.5pt);
\draw [fill=green] (1,0) circle (2.5pt);
\draw [fill=green] (4,0) circle (2.5pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

On lit graphiquement que l'inéquation $5x - x^{2} \geq 4$ admet pour solutions tous les nombres de l'intervalle $\left\lbrack 1; 4\right\rbrack$.

## Remarques : Validité et unicité des résultats

- Par lecture graphique, les solutions obtenues sont approchées. Il est indispensable de vérifier les résultats par un calcul.
- L'équation $f\left(x\right) = 7$ n'a pas de solution car dans ce cas la droite $\Delta$ ne coupe pas la courbe.
- Graphiquement, on ne peut pas être certain que les solutions qui apparaissent sont les seules. Il pourrait y en avoir d'autres au-delà des limites de la représentation graphique tracée.

# Variations d'une fonction

## Définition : Taux de variation

Le **taux de variation** de la fonction $f$ entre $a$ et $b$ est le nombre : $$t=\dfrac{f\left( b \right) - f\left( a \right)}{b - a}$$

## Propriété : Taux de variation et coefficient directeur

Le taux de variation de $f$ entre $a$ et $b$ est le **coefficient direceteur** _(la pente)_ de la droite passant par les points d'abscisses $a$ et $b$ de la courbe de $f$.

## Méthode : Déterminer un taux de variation d'une fonction

Soit $f$ la fonction définie sur $\mathbb{R}$ par : $f\left( x \right) = 2x^{2} + 1$.

> a) Déterminer le taux de variation entre $1$ et $3$. 
> b) Interpréter géométriquement ce taux de variation. 

---

(a) Taux de variation entre $1$ et $3$
\begin{align*}
\dfrac{f\left( 3 \right) - f\left( 1 \right)}{3 - 1}  &= \dfrac{\left(2 \times 3^{2} + 1\right) - \left( 2 \times 1^{2} + 1 \right)}{2}\\
\quad                                                 &= \frac{19 - 3}{2}\\
\quad                                                 &= 8
\end{align*}

(b) Le taux de variation de $f$ entre $1$ et $3$ est égal à $8$ donc la pente de la droite passant par les points d'abscisses $1$ et $3$ est égale à $8$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=5.0cm]
\begin{axis}[
width=14cm,height=12cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,
xmin=-2.5,xmax=3.5,ymin=-9.0,ymax=25.0,
xtick={1,2,3},ytick={3,11,19},]
\draw[line width=2.pt,color=red,smooth,domain=-2.5:3.5] plot(\x,{2.0*(\x)^(2.0)+1.0});
\draw [color=black!75,line width=2.pt,domain=-2.5:3.5] plot(\x,{(--10.-16.*\x)/-2.});
\draw [line width=1.pt,dashed] (1.,0.)-- (1.,3.);
\draw [line width=1.pt,dashed] (1.,3.)-- (0.,3.);
\draw [line width=1.pt,dashed] (0.,19.)-- (3.,19.);
\draw [line width=1.pt,dashed] (3.,19.)-- (3.,0.);
\draw (-1,3) node[anchor=south west] {$\mathcal{C}_f$};
\draw (0.5,-2) node[anchor=north east] {$d$};
\draw [fill=blue] (1.,3.) circle (2.0pt);
\draw [fill=blue] (2.,11.) circle (2.0pt);
\draw [fill=blue] (3.,19.) circle (2.0pt);
\draw [fill=black] (1.,0.) circle (2.0pt);
\draw [fill=black] (3.,0.) circle (2.0pt);
\draw [fill=black] (0.,3.) circle (2.0pt);
\draw [fill=black] (0.,19.) circle (2.0pt);
\draw [color=blue!30,->, line width=1.pt] (1,3)-- (2,3);
\draw [color=blue!30,->, line width=1.pt] (2,3)-- (2,11);
\draw [color=blue!30] (1.5,3) node[anchor=north] {$1$};
\draw [color=blue!30] (2,7) node[anchor=west] {$8$};
\draw [color=blue!30,->, line width=1.pt] (2,11)-- (3,11);
\draw [color=blue!30,->, line width=1.pt] (3,11)-- (3,19);
\draw [color=blue!30] (2.5,11) node[anchor=north] {$1$};
\draw [color=blue!30] (3,15) node[anchor=west] {$8$};
\end{axis}
\end{tikzpicture}
\end{center}

\newpage

## Définition : Fonctions monotones

On dit qu'une fonction $f$ est **monotone** sur un intervalle $I$, si $f$ est :

- soit **croissante** sur $I$,
- soit **décroissante** sur $I$,
- soit **constante** sur $I$.

## Propriétés : Taux de variation

Si le **taux de variation** d'une fonction $f$ entre deux nombres quelconques d'un intervalle $I$ $\ldots$

- $\ldots$ est **positif**, alors $f$ est **strictement croissante** sur $I$.
- $\ldots$ est **négatif**, $f$ est strictement décroissante sur $I$.
- $\ldots$ est **nul**, $f$ est constante sur $I$.

## Méthode : Étudier les variations d'une fonction à l'aide du taux de variation

Soit $f$ la fonction définie sur $\mathbb{R}$ par : $f\left( x \right) = 5x - 3$.

> a) Démontrer que $f$ est strictement croissante sur $\mathbb{R}$.

---

(a) On considère deux nombres quelconques $a\in\mathbb{R}$ et $b\in\mathbb{R}$.

Le taux de variation de $f$ entre $a$ et $b$ est égal à :

\begin{align*}
\dfrac{f\left( b \right) - f\left(a\right)}{b - a}  &= \dfrac{\left(5b - 3\right) - \left(5a - 3\right)}{b - a}\\
\quad                                               &= \dfrac{5b - 5a}{b - a}\\
\quad                                               &= \dfrac{5\left( b - a \right)}{b - a}\\
\quad                                               &= 5
\end{align*}

Or, $5 > 0$ donc $\dfrac{f\left( b \right) - f\left(a\right)}{b - a}> 0$ et donc $f$ est **strictement croissante** sur $\mathbb{R}$.
