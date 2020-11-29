---
title: Généralités sur les fonctions
subtitle: 2^nde^
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

# Définition et vocabulaire

## Définition

Soit $\mathscr{D}_f$ une partie de l'ensemble $\mathbb{R}$.

Une fonction $f$ définie sur $\mathscr{D}_f$, associe à tout nombre $x$ de $\mathscr{D}_f$, un unique nombre, noté $f(x)$.

$\mathscr{D}_f$ est l'ensemble de définition de $f$.

### Notation

\begin{eqnarray*}
f: & \mathscr{D}_f & \mapsto \mathbb{R}\\
   & x & \mapsto f(x)
\end{eqnarray*}

ou

> Soit $f$ une fonction définie sur $\mathscr{D}_f$ tel que $f(x) = ...$.

### Exemple

\begin{eqnarray*}
f: & \left[0;5\right] & \mapsto \mathbb{R}\\
   & x & \mapsto x\left(5-x\right)
\end{eqnarray*}

ou

> Soit $f$ une fonction définie sur $\left[0;5 \right]$ tel que $f(x) = x\left(5-x\right)$.

### Méthode : Établir un tableau de valeurs de $f$

Soit $f$ une fonction définie sur $\left[0;5 \right]$ tel que $f(x) = x\left(5-x\right)$.

Établir un tableau de valeurs de $f$, c'est calculer quelques valeurs de $f(x)$ pour des valeurs de $x\in \mathscr{D}_f$.

| $x$ | $f(x)$ |
|---:|:------|
| $0$ | $0\times (5-0)=0$ |
| $1$ | $1\times (5-1)=4$ |
| $1,5$ | $1,5\times (5-1,5)=5,25$ |
| $2$ | $6$ |
| $2,5$ | $6,25$ |
| $3$ | $6$ |
| $4$ | $4$ |
| $...$ | $...$ |

\newpage

## Vocabulaire : Image, antécédent

Pour la fonction $f(x)=x(5-x)$, on a :

* $f(2,5)=2,5\times (5-2,5)=6,25$
* $f(1)=1\times (5-1)=4$
  
On dit que :

* L'image de $2,5$ par la fonction $f$ est $6,25$
* L'image de $1$ par la fonction $f$ est $4$
* $2,5$ est **un** antécédent de $6,25$ par la fonction $f$
* $1$ est **un** antécédent de $4$ par la fonction $f$

### Remarque

* Un nombre possède une unique image.
* Cependant, un nombre peut posséder plusieurs antécédents.

Dans l'exemple précédent :

* L'image de $1$ est $4$
* $2$ et $3$ sont des antécédents de $6$

\newpage

# Représentation graphique

## Représentation graphique d'une fonction

On peut représenter une fonction $f$ à l'aide du tableau de valeurs. Pour cela, il faut placer dans un repère quelques points de coordonnées $\left(x;f\left(x\right)\right)$

### Exemple

Soit $f$ une fonction définie sur $\left[0;5 \right]$ tel que $f(x) = x\left(5-x\right)$.

| $x$ | $0$ | $1$ | $1,5$ | $2$ | $2,5$ | $3$ | $4$ | $4,25$ | $5$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $f(x)$ | $0$ | $4$ | $5,25$ | $6$ | $6,25$ | $6$ | $4$ | $2,25$ | $0$ |

En plaçant les points dans un repère et en "reliant" ces points, on obtient :

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=8cm,height=8cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-1,
xmax=6,
ymin=-1,
ymax=7,
xtick={0,1,...,5},
ytick={0,1,...,6},]
\draw [line width=2.pt,dash pattern=on 3pt off 3pt] (2.,0.)-- (2.,6.);
\draw [line width=2.pt,dash pattern=on 3pt off 3pt] (2.,6.)-- (0.,6.);
\begin{scriptsize}
\draw [fill=blue] (0.,0.) circle (2.0pt);
\draw [fill=blue] (1.,4.) circle (2.0pt);
\draw [fill=blue] (1.5,5.25) circle (2.0pt);
\draw [fill=blue] (2.,6.) circle (2.0pt);
\draw [fill=blue] (2.5,6.25) circle (2.0pt);
\draw [fill=blue] (3.,6.) circle (2.0pt);
\draw [fill=blue] (4.,4.) circle (2.0pt);
\draw [fill=blue] (4.5,2.25) circle (2.0pt);
\draw [fill=blue] (5.,0.) circle (2.0pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\quad
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=8cm,height=8cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-1,
xmax=6,
ymin=-1,
ymax=7,
xtick={0,1,...,5},
ytick={0,1,...,6},]
\draw[line width=2.pt,color=red,smooth,samples=100,domain=0:5] plot(\x,{(\x)*(5.0-(\x))});
\begin{scriptsize}
\draw [fill=blue] (0.,0.) circle (2.0pt);
\draw [fill=blue] (1.,4.) circle (2.0pt);
\draw [fill=blue] (1.5,5.25) circle (2.0pt);
\draw [fill=blue] (2.,6.) circle (2.0pt);
\draw [fill=blue] (2.5,6.25) circle (2.0pt);
\draw [fill=blue] (3.,6.) circle (2.0pt);
\draw [fill=blue] (4.,4.) circle (2.0pt);
\draw [fill=blue] (4.5,2.25) circle (2.0pt);
\draw [fill=blue] (5.,0.) circle (2.0pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

### Remarque

L'ensemble des points de coordonnées $\left(x ; y\right)$ avec $y=f(x)$ définissent la courbe représentative de la fonction $f$.

On dira que $y=f(x)$ est **l'équation de la courbe**.

\newpage

# Résolution graphique d'équations

## Résoudre graphiquement une équation du type $f(x)=k$

Pour résoudre une équation du type $f(x)=k$, il s'agit de trouver le (ou les) antécédent(s) de $k$ par la fonction $f$.

### Exemple

Soit $f$ une fonction définie sur $\left[0;5 \right]$ tel que $f(x) = x\left(5-x\right)$.

Pour résoudre $f(x)=2$, il s'agit de lire graphiquement les antécédents de $2$ par la fonction $f$.

On détermine les abscisses des points d'intersection de la courbe $\mathscr{C}_f$ avec la droite parallèle à l'axe des abscisses passant par le point $(0 ; 2)$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=8cm,height=8cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-1,
xmax=6,
ymin=-1,
ymax=7,
xtick={0,1,...,5},
ytick={0,1,...,6},]
\draw[line width=2.pt,color=red,smooth,samples=100,domain=0:5] plot(\x,{(\x)*(5.0-(\x))});
\draw [line width=2.pt,domain=-7.699581853126063:14.263867703012684] plot(\x,{(--2.-0.*\x)/1.});
\draw [->,line width=1.pt] (0.4384471871911697,2.) -- (0.4384471871911697,0.);
\draw [->,line width=1.pt] (4.561552812808831,2.) -- (4.561552812808831,0.);
\begin{scriptsize}
\draw [fill=blue] (0.4384471871911697,2.) circle (2.0pt);
\draw [fill=blue] (4.561552812808831,2.) circle (2.0pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

Deux solutions "approchées" : $x\approx 0,5$ et $x\approx 4,5$

### Remarques

* Par lecture graphique, les solutions obtenues sont approchées.
* L'équation $f(x)=7$ n'a pas de solution car dans ce cas la droite ne coupe pas la courbe.
* Graphiquement, on ne peut pas être certain que les solutions qui apparaissent sont les seules. Il pourrait y en avoir d'autres au-delà des limites de la représentation graphique tracée.

\newpage

## Résoudre graphiquement une équation du type $f(x)=g(x)$

Pour déterminer les solutions de l'équation $f(x)=g(x)$, il suffit de lire l'abscisse des points d'intersection des deux courbes $\mathscr{C}_f$ et $\mathscr{C}_g$.

### Exemple

On considère les fonctions $f$ et $g$ définie sur $\mathbb{R}$ par :

* $f(x)=x^2+2$
* $g(x)=-x^2+3x+2$

Leurs représentations graphiques sont les suivantes :

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[width=8cm,height=7cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-2,xmax=4,ymin=-1,ymax=6,xtick={-2,-1,0,1,...,5},ytick={-1,0,1,...,6},]
\draw[line width=1.pt,color=red,smooth,samples=100,domain=-2:5] plot(\x,{(\x)*(\x)+2)});
\draw[line width=1.pt,color=blue,smooth,samples=100,domain=-2:5] plot(\x,{-1.0*(\x)*(\x)+3*(\x)+2)});
\draw (2,6) node[anchor=north west] {$\mathscr{C}_f$};
\draw (3,3) node[anchor=north west] {$\mathscr{C}_g$};
\draw [line width=2.pt,color=green,dashed] (0,2) -- (0,0);
\draw [line width=2.pt,color=green,dashed] (1.5,4.25) -- (1.5,0);
\begin{scriptsize}
\draw [fill=black] (0,2) circle (2.0pt);
\draw [fill=black] (1.5,4.25) circle (2.0pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

Les points d'intersections des deux courbes $\mathscr{C}_f$ et $\mathscr{C}_g$ ont pour abscisses $0$ et $1,5$.

Graphiquement, on lit que l'équation $f(x)=g(x)$ admet pour solutions : $x=0$ et $x=1,5$.

---

Pour déterminer l'ensemble des solutions de l'inéquation $f(x)<g(x)$, il faut lire l'ensemble des valeurs de $x$ pour lesquelles $\mathscr{C}_f$ est **au-dessous** de $\mathscr{C}_g$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[width=8cm,height=7cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-2,xmax=4,ymin=-1,ymax=6,xtick={-2,-1,0,1,...,5},ytick={-1,0,1,...,6},]
\draw[line width=1.pt,color=red,smooth,samples=100,domain=-2:5] plot(\x,{(\x)*(\x)+2)});
\draw[line width=1.pt,color=blue,smooth,samples=100,domain=-2:5] plot(\x,{-1.0*(\x)*(\x)+3*(\x)+2)});
\draw (2,6) node[anchor=north west] {$\mathscr{C}_f$};
\draw (3,3) node[anchor=north west] {$\mathscr{C}_g$};
\draw [->,line width=1.pt,color=green] (0,2) -- (0,0);
\draw [->,line width=1.pt,color=green] (1.5,4.25) -- (1.5,0);
\draw [line width=2.pt,color=green] (0,0) -- (1.5,0);
\begin{scriptsize}
\draw [fill=black] (0,2) circle (2.0pt);
\draw [fill=black] (1.5,4.25) circle (2.0pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}
\end{center}

Graphiquement, $f(x)<g(x) \Leftrightarrow x\in \left]0;1.5\right[$
