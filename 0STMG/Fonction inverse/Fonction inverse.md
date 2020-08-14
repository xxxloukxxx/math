---
title: Fonction inverse
subtitle: T^le^ STMG
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

# Définition et représentation graphique

## Définition : Fonction inverse

Définition : La **fonction inverse** $f$ est définie sur $\mathbb{R}\smallsetminus\left\{ 0 \right\}$ par $$f\left( x \right) =\dfrac{1}{x}$$

## Représentation graphique

| $$x$$ | $-2$ | $-1$ | $-0.25$ | $0.1$ | $0.5$ | $1$ | $1.25$ | $2$ | $2.5$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $$f(x)=\dfrac{1}{x}$$ | $-0.5$ | $-1$ | $-4$ | $10$ | $2$ | $1$ | $0.8$ | $0.5$ | $0.4$ |

Table: Tableau de valeurs de la fonction inverse

\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=10cm,height=10cm,axis lines=middle,
ymajorgrids=true,xmajorgrids=true,
xmin=-4,xmax=4,ymin=-4,ymax=4,
xtick={-4.0,-3.0,...,4.0},
ytick={-4.0,-3.0,...,4.0},]
\draw[line width=2.pt,color=blue,smooth,samples=100,domain=-4:-0.1] plot(\x,{1.0/(\x)});
\draw[line width=2.pt,color=blue,smooth,samples=100,domain=0.1:4] plot(\x,{1.0/(\x)});
\draw [fill=black] (-2.,-0.5) circle (2.0pt);
\draw [fill=black] (-1.,-1.) circle (2.0pt);
\draw [fill=black] (-0.25,-4.) circle (2.0pt);
\draw [fill=black] (0.1,10.) circle (2.0pt);
\draw [fill=black] (0.5,2.) circle (2.0pt);
\draw [fill=black] (1.,1.) circle (2.0pt);
\draw [fill=black] (1.25,0.8) circle (2.0pt);
\draw [fill=black] (2.,0.5) circle (2.0pt);
\draw [fill=black] (2.5,0.4) circle (2.0pt);
\draw [fill=black] (-2.,-0.5) circle (2.0pt);
\draw [fill=black] (-1.,-1.) circle (2.0pt);
\draw [fill=black] (-0.25,-4.) circle (2.0pt);
\draw [fill=black] (0.1,10.) circle (2.0pt);
\draw [fill=black] (0.5,2.) circle (2.0pt);
\draw [fill=black] (1.,1.) circle (2.0pt);
\draw [fill=black] (1.25,0.8) circle (2.0pt);
\draw [fill=black] (2.,0.5) circle (2.0pt);
\draw [fill=black] (2.5,0.4) circle (2.0pt);
\draw[purple!80,dashed,line width=1.5pt] (axis cs:0,-4) -- (axis cs:0,10);
\end{axis}
\end{tikzpicture}
\caption{Représentation graphique de la fonction inverse}
\end{center}
\end{figure}

### Remarque :

La courbe d'équation $y=\dfrac{1}{x}$ de la fonction inverse, appelée **hyperbole** de centre $O$, est symétrique par rapport à l'origine.

\newpage

# Dérivée et sens de variation

## Propriété : Dérivée de la fonction inverse

 La dérivée de la fonction inverse $f$ est définie sur $\mathbb{R}\smallsetminus\left\{ 0 \right\}$ par $$f'\left( x \right) = -\dfrac{1}{x^{2}}$$.

### Démonstration {-}

Soit $f(x)=\dfrac{1}{x}$ définie sur $\mathbb{R}\smallsetminus\left\{ 0 \right\}$. Par définition, la fonction dérivée de $f$ est :

$$f'(a)=\lim_{h\to 0} \dfrac{f(a+h)-f(a)}{h}$$

Dans notre cas :

\begin{align*}
f'(a)  &=\lim_{h\to 0} \left(\dfrac{f(a+h)-f(a)}{h}\right)\\
\quad     &=\lim_{h\to 0} \left(\dfrac{\frac{1}{a+h}-\frac{1}{a}}{h}\right)\\
\quad     &=\lim_{h\to 0} \left(\dfrac{1}{h} \times \left(\dfrac{1}{a+h}-\dfrac{1}{a}\right)\right)\\
\quad     &=\lim_{h\to 0} \left(\dfrac{1}{h} \times \left(\dfrac{a}{a(a+h)}-\dfrac{a+h}{a(a+h)}\right)\right)\\
\quad     &=\lim_{h\to 0} \left(\dfrac{1}{h} \times \left(\dfrac{a-(a+h)}{a(a+h)}\right)\right)\\
\quad     &=\lim_{h\to 0} \left(\dfrac{1}{h} \times \left(\dfrac{-h}{a(a+h)}\right)\right)\\
\quad     &=\lim_{h\to 0} \left(\dfrac{-1}{a(a+h)}\right)\quad=\dfrac{-1}{a^{2}}\\
\end{align*}

Pour tout nombre $a$, on associe le nombre dérivé de la fonction $f$ égal à $\dfrac{-1}{a^{2}}$.

Ainsi, pour tout $x$ de $\mathbb{R}\smallsetminus\left\{ 0 \right\}$, on a : $f'(x) =\dfrac{-1}{x^{2}}$.

\newpage

## Propriété : Variations de la fonction inverse

La fonction inverse est **décroissante** sur $\left\rbrack - \infty\ ;0 \right\lbrack\ $ et sur $\left\rbrack 0\ ;\  + \infty \right\lbrack$.

\begin{center}
\begin{tikzpicture}[scale=0.875]
\tikzstyle{cadre}=[thin]
\tikzstyle{fleche}=[->,>=latex,thin]
\tikzstyle{nondefini}=[lightgray]
\def\Lrg{2.5}
\def\HtX{1}
\def\HtY{0.5}
\def\lignex{-0.5*\HtX}
\def\lignef{-1.5*\HtX}
\def\separateur{-0.5*\Lrg}
\def\gauche{-1.5*\Lrg}
\def\droite{4.5*\Lrg}
\def\haut{0.5*\HtX}
\def\bas{-2.5*\HtX-2*\HtY}
\node at (-1*\Lrg,0) {$x$};
\node at (0*\Lrg,0) {$-\infty$};
\node at (2*\Lrg,0) {$0$};
\node at (4*\Lrg,0) {$+\infty$};
\node at (-1*\Lrg,-1*\HtX) {$f'(x)=\dfrac{-1}{x^{2}}$};
\node at (0*\Lrg,-1*\HtX) {$$};
\node at (1*\Lrg,-1*\HtX) {$-$};
\node at (3*\Lrg,-1*\HtX) {$-$};
\node at (4*\Lrg,-1*\HtX) {$$};
\node  at (-1*\Lrg,{-2*\HtX+(-1)*\HtY}) {$f(x)=\dfrac{1}{x}$};
\node (f1) at (0*\Lrg,{-2*\HtX+(0)*\HtY}) {$0$};
\node[left] (f2) at (2*\Lrg,{-2*\HtX+(-2)*\HtY}) {$-\infty$};
\node[right] (f3) at (2*\Lrg,{-2*\HtX+(0)*\HtY}) {$+\infty$};
\node (f4) at (4*\Lrg,{-2*\HtX+(-2)*\HtY}) {$0$};
\draw[fleche] (f1) -- (f2);
\draw[fleche] (f3) -- (f4);
\draw[double distance=2pt] (2*\Lrg,\lignex-0.1*\HtX) -- (2*\Lrg,\lignef+0.1*\HtX);
\draw[double distance=2pt] (2*\Lrg,\lignef-0.1*\HtX) -- (2*\Lrg,\bas+0.1*\HtX);
\draw[cadre] (\separateur,\haut) -- (\separateur,\bas);
\draw[cadre] (\gauche,\haut) rectangle  (\droite,\bas);
\draw[cadre] (\gauche,\lignex) -- (\droite,\lignex);
\draw[cadre] (\gauche,\lignef) -- (\droite,\lignef);
\end{tikzpicture}
\end{center}

### Démonstration {-}

Pour tout $x$ de $\mathbb{R}\smallsetminus\left\{ 0 \right\}$, $f'\left( x \right) = \dfrac{-1}{x^{2}}<0 \quad$ car $\quad x^{2}>0\quad$ et $\quad -1<0$.

Donc $f$ est **décroissante** sur $\left\rbrack - \infty\ ;0 \right\lbrack$ et sur $\left\rbrack 0\ ;\  + \infty \right\lbrack$.

## Propriété : Comportement de la fonction inverse aux bornes de son ensemble de définition

### En $+\infty$

On s'intéresse aux valeurs de $f\left( x \right)$ lorsque $x$ devient de **plus en plus grand**.

| $$x$$ | $0.1$ | $1$ | $2$ | $4$ | $10$ | $50$ | $100$ | $1000$ | $\ldots$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $$f(x)=\dfrac{1}{x}$$ | $10$ | $1$ | $0.5$ | $0.25$ | $0.1$ | $0.02$ | $0.01$ | $0.001$ | $\ldots$ |

Table: Tableau de valeurs de la fonction inverse lorsque $x\to +\infty$

On constate que $f\left( x \right)$ se rapproche de $0$ lorsque $x$ devient de **plus en plus grand**.

On dit que la **limite** de $f$ lorsque $x$ tend vers $+\infty$ est égale à $0$ et on note :

$$\lim_{x\to +\infty}{f\left( x \right)} = 0$$

Graphiquement, pour des valeurs de plus en plus grandes, la courbe de $f$ se rapproche de plus en plus de l'axe des abscisses.

\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=12cm,height=6cm,axis lines=middle,
ymajorgrids=true,xmajorgrids=true,
xmin=-0.5,xmax=10,ymin=-0.1,ymax=1.5,
xtick={0.0,1.0,...,10.0},
ytick={0.0,.25,...,1.5}]
\draw[line width=2.pt,color=blue,samples=100,smooth,domain=1:10] plot(\x,{1.0/(\x)});
\draw[line width=2.pt,dashed,color=blue,samples=100,smooth,domain=0.1:1] plot(\x,{1.0/(\x)});
\draw[purple,dashed,line width=1.5pt] (axis cs:-10,0) -- (axis cs:10,0);
\end{axis}
\end{tikzpicture}
\caption{Représentation graphique de la fonction inverse sur $\left\rbrack 0\ ;\  + \infty \right\lbrack$}
\end{center}
\end{figure}

### En $-\infty$

On s'intéresse aux valeurs de $f\left( x \right)$ lorsque $x$ devient de **plus en plus grand dans les négatifs**.

| $$x$$ | $\ldots$ | $-1000$ | $-100$ | $-10$ | $-5$ | $-1$ | $-0.5$ | $-0.1$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $$f(x)=\dfrac{1}{x}$$ | $-0.001$ | $-0.01$ | $-0.1$ | $-0.2$ | $-1$ | $-2$ | $-10$ | $\ldots$ |

Table: Tableau de valeurs de la fonction inverse lorsque $x\to -\infty$

On constate que $f\left( x \right)$ se rapproche de $0$ lorsque $x$ devient de **plus en plus grand dans les négatifs**.

On dit que la **limite** de $f$ lorsque $x$ tend vers $-\infty$ est égale à $0$ et on note :

$$\lim_{x\to -\infty}{f\left( x \right)} = 0$$

Graphiquement, pour des valeurs de plus en plus **grandes dans les négatifs**, la courbe de $f$ se rapproche de plus en plus de l'axe des abscisses.

\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=12cm,height=6cm,axis lines=middle,
ymajorgrids=true,xmajorgrids=true,
xmin=-10.0,xmax=0.5,ymin=-1.5,ymax=0.1,
xtick={-10.0,-9.0,...,0.0},
ytick={-1.5,-1.25,...,0.5}]
\draw[line width=2.pt,color=blue,samples=100,smooth,domain=-10:-1] plot(\x,{1.0/(\x)});
\draw[line width=2.pt,dashed,color=blue,samples=100,smooth,domain=-1:-0.1] plot(\x,{1.0/(\x)});
\draw[purple,dashed,line width=1.5pt] (axis cs:-10,0) -- (axis cs:10,0);
\end{axis}
\end{tikzpicture}
\caption{Représentation graphique de la fonction inverse sur $\left\rbrack - \infty\ ;0 \right\lbrack$}
\end{center}
\end{figure}

### Remarque : {-}

On dit que l'axe des abscisses est une **asymptote horizontale** à la courbe de la fonction inverse en $- \infty$ et en $+ \infty$.

\newpage

### Au voisinage de $0$

L'image de $0$ par la fonction $f$ n'existe pas. On s'intéresse cependant aux valeurs de $f\left( x \right)$ lorsque $x$ se rapproche de $0$.

| $$x$$ | $-1$ | $-0.5$ | $-0.1$ | $-0.01$ | $-0.001$ | $\ldots$ | $0.001$ | $0.01$ | 0.1 | 0.5 | 1 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $$f(x)=\dfrac{1}{x}$$ | $-1$ | $-2$ | $-10$ | $-100$ | $-1000$ | $\ldots$ | $1000$ | $100$ | $10$ | $2$ | $1$ |

A l'aide de la calculatrice, on constate que :

- Pour $x > 0$, on a $f\left( x \right)$ devient de **plus en plus grand** lorsque $x$ se rapproche de $0$.

On dit que la limite de $f$ lorsque $x$ tend vers $0$ pour $x > 0$ est égale à $+ \infty$ et on note :

$$\lim_{\begin{matrix}x \to 0 \\x > 0\end{matrix}}{f\left( x \right)} = + \infty$$

- Pour $x < 0$, on a $f\left( x \right)$ devient de **plus en plus grand dans les négatifs** lorsque $x$ se rapproche de $0$.

On dit que la limite de $f$ lorsque $x$ tend vers $0$ pour $x < 0$ est égale à $-\infty$ et on note :

$$\lim_{\begin{matrix}x \to 0 \\x < 0\end{matrix}}{f\left( x \right)} = - \infty$$

\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=8cm,height=8cm,axis lines=middle,
ymajorgrids=true,xmajorgrids=true,
xmin=-1.9,xmax=1.9,ymin=-9.5,ymax=9.5,
xtick={-4.0,-3.0,...,4.0},
ytick={-10.0,-8.0,...,10.0},]
\draw[line width=2.pt,dashed,color=blue,smooth,samples=100,domain=-4:-1] plot(\x,{1.0/(\x)});
\draw[line width=2.pt,color=blue,smooth,samples=100,domain=-1:-0.01] plot(\x,{1.0/(\x)});
\draw[line width=2.pt,color=blue,smooth,samples=100,domain=0.01:1] plot(\x,{1.0/(\x)});
\draw[line width=2.pt,dashed,color=blue,smooth,samples=100,domain=1:4] plot(\x,{1.0/(\x)});
\draw[purple,dashed,line width=1.5pt] (axis cs:0,-10) -- (axis cs:0,10);
\end{axis}
\end{tikzpicture}
\caption{Représentation graphique de la fonction inverse au voisinage de $0$}
\end{center}
\end{figure}

### Remarque {-}

Graphiquement, pour des valeurs de plus en plus en proches de $0$, la courbe de $f$ se rapproche de plus en plus de l'axe des ordonnées.

On dit que l'axe des ordonnées est une **asymptote verticale** à la courbe représentative de la fonction inverse.

\newpage

# Fonction de la forme $f(x)=P(x) + \dfrac{k}{x}$

## Méthode : Étudier une fonction de la forme $f(x)=P(x) + \dfrac{k}{x}$

Soit la fonction $f$ définie sur $\mathbb{R}\smallsetminus\left\{ 0\right\}$ par $f(x) = 1 - 2x -\dfrac{2}{x}$.

> a) Calculer la fonction dérivée de $f$.
> b) Déterminer le signe de $f'$ en fonction de $x$.
> c) Dresser le tableau de variations de $f$.
> d) Représenter la fonction $f$ dans un repère.

---

(a)  On a : $f\left( x \right) = 1 - 2x - 2 \times$ $\frac{1}{x}$

Donc, on a :

\begin{align*}
f'\left( x \right) &=0-2-2\times\left(\dfrac{-1}{x^{2}}\right)\\
\quad                 &=\dfrac{-2\times x^2}{x^2}+\dfrac{2}{x^{2}}\\
\quad                 &=\dfrac{2-2x^2}{x^2}
\end{align*}

On a donc : $f'\left( x \right)=\dfrac{2-2x^2}{x^2}$

(b) On doit résoudre l'inéquation $f'(x) > 0$.

Pour $x\neq 0$, on a :

\begin{align*}
\dfrac{2-2x^2}{x^2} &>0\\
2 - 2x^{2} &> 0\quad\text{car }x^{2}>0\\
2          &> 2x^{2}\\
x^{2}      &< 1
\end{align*}

Et donc si $f'(x) > 0$ alors $-1<x<1$ et $x\neq 0$.

(c)

\begin{center}
\begin{tikzpicture}[scale=0.875]
% Styles 
\tikzstyle{cadre}=[thin]
\tikzstyle{fleche}=[->,>=latex,thin]
\tikzstyle{nondefini}=[lightgray]
% Dimensions Modifiables
\def\Lrg{1.5}
\def\HtX{1}
\def\HtY{0.5}
% Dimensions Calculées
\def\lignex{-0.5*\HtX}
\def\lignef{-1.5*\HtX}
\def\separateur{-0.5*\Lrg}
% Largeur du tableau
\def\gauche{-1.5*\Lrg}
\def\droite{8.5*\Lrg}
% Hauteur du tableau
\def\haut{0.5*\HtX}
\def\bas{-2.5*\HtX-2*\HtY}
% Ligne de l'abscisse : x
\node at (-1*\Lrg,0) {$x$};
\node at (0*\Lrg,0) {$-\infty$};
\node at (2*\Lrg,0) {$-1$};
\node at (4*\Lrg,0) {$0$};
\node at (6*\Lrg,0) {$1$};
\node at (8*\Lrg,0) {$+\infty$};
% Ligne de la dérivée : f'(x)
\node at (-1*\Lrg,-1*\HtX) {$f'(x)$};
\node at (0*\Lrg,-1*\HtX) {$$};
\node at (1*\Lrg,-1*\HtX) {$-$};
\node at (2*\Lrg,-1*\HtX) {$0$};
\node at (3*\Lrg,-1*\HtX) {$+$};
\node at (5*\Lrg,-1*\HtX) {$+$};
\node at (6*\Lrg,-1*\HtX) {$0$};
\node at (7*\Lrg,-1*\HtX) {$-$};
\node at (8*\Lrg,-1*\HtX) {$$};
% Ligne de la fonction : f(x)
\node  at (-1*\Lrg,{-2*\HtX+(-1)*\HtY}) {$f(x)$};
\node (f1) at (0*\Lrg,{-2*\HtX+(0)*\HtY}) {$$};
\node (f2) at (2*\Lrg,{-2*\HtX+(-2)*\HtY}) {$5$};
\node[left] (f3) at (4*\Lrg,{-2*\HtX+(0)*\HtY}) {$$};
\node[right] (f4) at (4*\Lrg,{-2*\HtX+(-2)*\HtY}) {$$};
\node (f5) at (6*\Lrg,{-2*\HtX+(0)*\HtY}) {$-3$};
\node (f6) at (8*\Lrg,{-2*\HtX+(-2)*\HtY}) {$$};
% Flèches
\draw[fleche] (f1) -- (f2);
\draw[fleche] (f2) -- (f3);
\draw[fleche] (f4) -- (f5);
\draw[fleche] (f5) -- (f6);
% Doubles barres
\draw[double distance=2pt] (4*\Lrg,\lignex-0.1*\HtX) -- (4*\Lrg,\lignef+0.1*\HtX);
\draw[double distance=2pt] (4*\Lrg,\lignef-0.1*\HtX) -- (4*\Lrg,\bas+0.1*\HtX);
% Encadrement
\draw[cadre] (\separateur,\haut) -- (\separateur,\bas);
\draw[cadre] (\gauche,\haut) rectangle  (\droite,\bas);
\draw[cadre] (\gauche,\lignex) -- (\droite,\lignex);
\draw[cadre] (\gauche,\lignef) -- (\droite,\lignef);
\end{tikzpicture}
\end{center}

\newpage

(d) Voici la représentation de la fonction $f$

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=14cm,height=10cm,axis lines=middle,
ymajorgrids=true,xmajorgrids=true,
xmin=-5.9,xmax=5.9,ymin=-14,ymax=16,
xtick={-6,-5,...,6},ytick={-15,-10,-5,...,5,10,15}]
\draw[line width=2.pt,color=blue,samples=50,smooth,domain=-10:-0.1] plot(\x,{1-2*\x-(2/(\x))});
\draw[line width=2.pt,color=blue,samples=50,smooth,domain=0.1:10] plot(\x,{1-2*\x-(2/(\x))});
\draw [fill=black] (-1,5) circle (2.0pt);
\draw [fill=black] (1,-3) circle (2.0pt);
\draw [fill=black] (0,-3) circle (2.0pt);
\draw [fill=black] (0,5) circle (2.0pt);
\draw [line width=1.pt,dashed] (-1,0)-- (-1,5);
\draw [line width=1.pt,dashed] (0,5)-- (-1,5);
\draw [line width=1.pt,dashed] (1,0)-- (1,-3);
\draw [line width=1.pt,dashed] (0,-3)-- (1,-3);
\end{axis}
\end{tikzpicture}
\end{center}
