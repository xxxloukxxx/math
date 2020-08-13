---
title: Fonction polynôme de degré 3
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
  \usepackage{tkz-tab}
---

---

\newpage

# Définition et représentation graphique

## Définition : Fonction polynôme de degré 3

Les fonctions définies sur $\mathbb{R}$ par $x \longmapsto ax^{3}$ ou $x \longmapsto ax^{3} + b$ sont des **fonctions polynômes de degré 3**.

### Exemples et contre-exemples {-}

- $f\left( x \right) = 4x^{3} + 1$ \qquad fonctions polynômes de degré 3
- $g\left( x \right) = x^{3} - 2$ \qquad fonctions polynômes de degré 3
- $h\left( x \right) = 1 + x^{2} - 2x^{3}$ \qquad fonctions polynômes de degré 3
- $m\left( x \right) = - x + 4$  \qquad fonction polynôme de degré 1 (fonction affine).
- $n\left( x \right) = 2x^{5} - x^{3} + 5x - 1$  \qquad fonction polynôme de degré 5.

Les coefficients $a$ et $b$ sont des réels donnés avec $a \neq 0$.

## Propriétés : Variations

Soit $f$ une fonction polynôme de degré 3, telle que $f\left( x \right) = ax^{3} + b$.

- Si $a$ est **positif**, $f$ est **croissante**.
- Si $a$ est **négatif**, $f$ est **décroissante**.

## Représentation grapghique

Voici les représentation grapghique des fonctions polynôme $x \longmapsto ax^{3}$ et $x \longmapsto ax^{3}+b$ en fonction du signe de $a$
\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=10cm,height=8cm,
axis lines=middle,ymajorgrids=true,xmajorgrids=true,
xmin=-3.2,xmax=3.2,ymin=-5.2,ymax=5.2,
xtick={-9.0,-8.0,...,9.0},
ytick={-5.0,-4.0,...,5.0},]
\draw [color=red](-2,3) node[anchor=north west] {$\mathbf{a<0}$};
\draw [color=blue](2,3) node[anchor=north west] {$\mathbf{a>0}$};
\draw[line width=2.pt,color=red,smooth,domain=-3:3] plot(\x,{-0.2*(\x)^(3.0)}); 
\draw[line width=2.pt,color=blue,smooth,domain=-3:3] plot(\x,{0.5*(\x)^(3.0)});
\draw [fill=black] (0.,0.) circle (2.0pt);
\end{axis}
\end{tikzpicture}\qquad
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=10cm,height=8cm,
axis lines=middle,ymajorgrids=true,xmajorgrids=true,
xmin=-3.2,xmax=3.2,ymin=-5.2,ymax=5.2,
xtick={-9.0,-8.0,...,9.0},
ytick={-5.0,-4.0,...,5.0},]
\draw [color=red](-2,4) node[anchor=north west] {$\mathbf{a<0}$};
\draw [color=blue](2,2) node[anchor=north west] {$\mathbf{a>0}$};
\draw[line width=2.pt,color=red,smooth,domain=-3:3] plot(\x,{-0.2*(\x)^(3.0)+1}); 
\draw[line width=2.pt,color=blue,smooth,domain=-3:3] plot(\x,{0.5*(\x)^(3.0)-2});
\draw [fill=black] (0.,0.) circle (2.0pt);
\end{axis}
\end{tikzpicture}
\end{center}
\caption{Répresentation de $ax^{3}$ (à gauche) et $ax^{3}+b$ (à droite) en fonction du signe de $a$}
\end{figure}

\newpage

# Forme factorisée d'une fonction polynôme de degré 3

## Définition : Forme factorisée d'une fonction polynôme de degré 3

Les fonctions définies sur $\mathbb{R}$ par $$f\left( x \right) = a\left( x - x_{1} \right)\left( x - x_{2} \right)\left( x - x_{3} \right)$$ sont des **fonctions polynômes de degré 3**.

Les coefficients $a$, $x_{1}$, $x_{2}$ et $x_{3}$ sont des réels avec $a \neq 0$.

### Exemple {-}

La fonction $f$ définie par $f\left( x \right) = 5\left( x - 4 \right)\left( x - 1 \right)\left( x + 3 \right)$ est une **fonction polynôme de degré 3** sous sa forme factorisée.

Si on développe l'expression de $f$ à l'aide d'un logiciel de calcul formel, on obtient bien l'expression d'une fonction polynôme de degré 3 : $$f\left( x \right) = 5x^{3} - 10x^{2} - 55x + 60$$

![Développement de $f(x)$ à l'aide d'un logiciel de calcul formel](media/expand(1).png){width=30%}

## Propriété : Racines d'une fonction polynôme de degré 3

Soit la fonction $f$ définie sur $\mathbb{R}$ par $f\left( x \right) = a\left( x - x_{1} \right)\left( x - x_{2} \right)\left( x - x_{3} \right)$.

L'équation $f\left( x \right) = 0$ possède trois solutions (éventuellement égales) :$\ x = x_{1}$, $x = x_{2}$ et $x = x_{3}$ appelées les **racines** de la fonction polynôme $f$.

### Exemple {-}

Soit la fonction $f$ définie par $f\left( x \right) = 5\left( x - 4 \right)\left( x - 1 \right)\left( x + 3 \right)$.

On a vu, dans l'exemple précédent que : $f\left( x \right) = 5x^{3} - 10x^{2} - 55x + 60$

En partant de l'expression développée, on peut vérifier que $4$, $1$ et $-3$ sont des racines du polynôme $f$.
\begin{align*}
f\left( 4 \right) &= \left(5\times {4}^{3}\right) - \left(10\times 4^{2}\right) - \left(55 \times 4\right) + 60\\ \quad &= 320 - 160 - 220 + 60\\ \quad &= 0\\
f\left( 1 \right) &= \left(5\times {1}^{3}\right) - \left(10 \times 1^{2}\right) - \left(55 \times 1\right) + 60\\ \quad &= 5 - 10 - 55 + 60\\ \quad &= 0\\
f\left( - 3 \right) &= \left(5\times {\left( -3 \right)}^{3}\right) - \left(10 \times \left( - 3 \right)^{2}\right) - \left(55 \times \left( - 3 \right)\right) + 60\\ \quad &= - 135 - 90 + 165 + 60\\ \quad &= 0
\end{align*}

$4$, $1$ et $-3$, solutions de l'équation $f\left( x \right) = 0$, sont donc des **racines** de $f$.

\newpage

## Méthode : Étudier le signe d'un polynôme de degré 3

Étudier le signe de la fonction polynôme $f$ définie sur $\mathbb{R}$ par : $$f\left( x \right) = 2\left( x + 1 \right)\left( x - 2 \right)\left( x - 5 \right)$$

$2$ étant un nombre positif, le signe de $2\left( x + 1 \right)\left( x - 2 \right)\left( x - 5 \right)$ dépend du signe de chaque facteur : $(x + 1)$, $(x - 2)$ et $(x - 5)$.

On étudie ainsi le signe de chaque facteur et on présente les résultats dans un tableau de signes.
\begin{align*}
x+1>0 & \qquad & x-2>0 & \qquad & x-5>0\\
\Leftrightarrow x>-1 & \qquad & \Leftrightarrow x>2 & \qquad & \Leftrightarrow x>5
\end{align*}

En appliquant la règle des signes dans le tableau, on peut en déduire le signe du produit $f\left( x \right) = 2\left( x + 1 \right)\left( x - 2 \right)\left( x - 5 \right)$.

\begin{center}
\begin{tikzpicture}
   \tkzTabInit{$x$ / 1 , $2$ / 1, $(x+1)$ / 1, $(x-2)$ / 1, $(x-5)$ / 1, $f(x)$ / 1}{$-\infty$, $-1$,$2$, $5$, $+\infty$}
   \tkzTabLine{  ,   ,   ,   , + ,   ,   ,   ,  }
   \tkzTabLine{  , - , z ,   ,   , + ,   ,   ,  }
   \tkzTabLine{  ,   , - ,   , z ,   , + ,   ,  }
   \tkzTabLine{  ,   ,   , - ,   ,   , z , + ,  }
   \tkzTabLine{  , - , z , + , z , - , z , + ,  }
\end{tikzpicture}
\end{center}

On en déduit que :

- $f(x) \geq 0$ pour $x \in \left\lbrack - 1\ ;2 \right\rbrack \cup \left\lbrack 5\ ;\  + \infty \right\lbrack$
- $f(x) \leq 0$ pour $x \in \left\rbrack - \infty\ ;\  - 1 \right\rbrack \cup \left\lbrack 2\ ;5 \right\rbrack$.

La représentation de la fonction $f$ à l'aide d'un logiciel permet de confirmer les résultats établis précédemment.

\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=16cm,height=7cm,
axis lines=middle,ymajorgrids=true,xmajorgrids=true,
xmin=-2,xmax=6,ymin=-30,ymax=30,
xtick={-2,-1,...,10},
ytick={-30,-20,...,30},]
\draw[line width=2.pt,color=red,smooth,domain=-2:-1] plot(\x,{2.0*((\x)+1)*((\x)-2)*((\x)-5)});
\draw [color=red](-1.5,-20) node[anchor=north west] {$f(x)<0$};
\draw[line width=2.pt,color=green,smooth,domain=-1:2] plot(\x,{2.0*((\x)+1)*((\x)-2)*((\x)-5)});
\draw [color=green](0.8,20) node[anchor=south west] {$f(x)>0$};
\draw[line width=2.pt,color=red,smooth,domain=2:5] plot(\x,{2.0*((\x)+1)*((\x)-2)*((\x)-5)});
\draw [color=red](4,-20) node[anchor=north west] {$f(x)<0$};
\draw[line width=2.pt,color=green,smooth,domain=5:7] plot(\x,{2.0*((\x)+1)*((\x)-2)*((\x)-5)});
\draw [color=green](5.3,20) node[anchor=north east] {$f(x)>0$};
\draw [fill=black] (-1,0) circle (2.0pt);
\draw [fill=black] (+2,0) circle (2.0pt);
\draw [fill=black] (+5,0) circle (2.0pt);
\end{axis}
\end{tikzpicture}
\end{center}
\caption{Répresentation graphique de $2\left( x + 1 \right)\left( x - 2 \right)\left( x - 5 \right)$}
\end{figure}

\newpage

# Équation de la forme $x^{3} = c$

## Propriété : Solution de l'équation $x^{3} = c$

L'équation $x^{3} = c$, avec $c$ positif, possède une unique solution $\sqrt[3]{c}$.

Cette solution peut également se noter $c^{\left(\frac{1}{3}\right)}$.

## Méthode : Résoudre une équation du type $x$^3^ = *c*

Résoudre dans $\mathbb{R}$ les équations : 

a) $x^{3} = 27$
b) ${2x}^{3} - 6 = 16$

---

(a) On cherche le nombre qui, élevé au cube, donne $27$.

Ce nombre est égal à la racine cubique de $27$, soit : $x = \sqrt[3]{27} = 3$.

(b) ${2x}^{3} - 6 = 16$
\begin{align*}
2x^{3} - 6 &= 16\\
2x^{3} &= 22\\
x^{3} &=11
\end{align*}

L'équation admet donc une unique solution $x = \sqrt[3]{11}\approx 2,223$.