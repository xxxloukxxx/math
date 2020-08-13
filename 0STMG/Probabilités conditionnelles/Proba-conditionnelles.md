---
title: Probabilités conditionnelles
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
  \usepackage{pifont}
  \usepackage{pgf,tikz,tkz-tab,pgfplots}
  \pgfplotsset{compat=1.15}
  \usepackage{tikz-qtree}
  \usepackage{mathrsfs}
  \usetikzlibrary{arrows}
---

---

# Notion de probabilités conditionnelles

## Exemple : Sondage téléphonique dans la classe

Voici les résultats d'un sondage au sein de la classe de TSTMG

|$\quad$ | Fille | Garçon | Total |
|:-:|:-:|:-:|:-:|
|Apple|10|7|17|
|Pas Apple|6|5|11|
|Total|16|12|28|

On choisit au hasard un élève dans la classe.

- Soit $F$ L'événement : "l'élève est une fille"
- Soit $A$ L'événement : "l'élève possède un téléphone Apple"

On a $A\cap F$ : "l'élève est une fille avec un téléphone Apple"

$P(A)=\dfrac{17}{28}$ \quad , \quad $P(F)=\dfrac{16}{28}$ \quad et $P(A \cap F)=\dfrac{10}{28}$

\newpage

A l'aide du tableau :

|$\quad$ | $F$ | $\overline{F}$ | Total |
|:-:|:-:|:-:|:-:|
|$A$|$\left(\dfrac{10}{28}\right)\approx 0.357$|$\left(\dfrac{7}{28}\right)= 0.25$|$\left(\dfrac{17}{28}\right)\approx 0.607$|
|$\overline{A}$|$\left(\dfrac{6}{28}\right)\approx 0.214$|$\left(\dfrac{5}{28}\right)\approx 0.178$|$\left(\dfrac{11}{28}\right)\approx 0.392$|
|Total|$\left(\dfrac{16}{28}\right)\approx 0.571$|$\left(\dfrac{12}{28}\right)\approx 0.428$|$\left(\dfrac{28}{28}\right)=1$|

## Définition : Probabilité conditionnelle

Définition : Soit $A$ et $B$, deux événements avec $P(A)\neq 0$. On appelle **probabilité conditionnelle** de $B$ sachant $A$, la probabilité que l'événement $B$ se réalise **sachant que** l'événement $A$ est réalisé.

Elle est notée $P_{A}(B)$ et est définie par :

\begin{center}
$P_{A}(B)=\dfrac{P(A\cap B)}{P(A)}$

$\text{Proba de "B sachant A"}=\dfrac{\text{Proba de "A et B"}}{\text{Proba de "A"}}$
\end{center}

### Exemple {-}

Dans l'exemple précédent, $P_{F}(A)$, c'est la probabilité que l’élève choisi possède un Apple **sachant que c’est une fille**

Ou "**parmi les filles**, quelle est la probabilité que l’élève possède un **Apple** ?"

\begin{align*}
P_{F}(A)=\dfrac{P(A\cap F)}{P(F)}&=\dfrac{\frac{10}{28}}{\frac{16}{28}} \\
\quad &=\dfrac{10}{16}=\dfrac{5}{8} \\
\quad &=0.625
\end{align*}

On peut retrouver intuitivement ce résultat : sachant que l’élève est une fille, on a $10$ chances sur $16$ qu’elle possède une téléphone Apple.

|$\quad$ | Fille | Garçon | Total |
|:-:|:-:|:-:|:-:|
|Apple|**_10_**|7|17|
|Pas Apple|6|5|11|
|Total|**_16_**|12|28|

\newpage

## Exemple : Gagné ou perdu

Un sac contient $50$ boules, dont $20$ boules rouges et $30$ boules noires, où il est marqué soit "Gagné" ou soit "Perdu".

- Sur $15$ boules rouges, il est marqué "Gagné".
- Sur $9$ boules noires, il est marqué "Gagné".

|$\quad$ | Rouge | Noires | Total |
|:-:|:-:|:-:|:-:|
|Gagné|15|9|24|
|Perdu|5|21|26|
|Total|20|30|50|

On tire au hasard une boule dans le sac.

- Soit R l'événement : "On tire une boule rouge"
- Soit G l'événement : "On tire une boule marquée Gagné"

Donc $R\cap G$ est l'événement : "On tire une boule rouge marquée Gagné"

On a $\quad P(R)=\dfrac{20}{50}=0.4\quad$ et $\quad P(R\cap G)=\dfrac{15}{50}=0.3$

Donc la probabilité qu'on tire une boule marquée "Gagné" **sachant qu'elle est rouge** est :

\begin{align*}
P_{R}(G)&=\dfrac{P(R\cap G)}{P(R)}\\
\quad&=\dfrac{0.3}{0.4}=0.75\\
\end{align*}

On peut retrouver intuitivement ce résultat : **Sachant que le résultat est une boule rouge**, on a $15$ chances sur $20$ qu'il soit marqué Gagné.

|$\quad$ | Rouge | Noires | Total |
|:-:|:-:|:-:|:-:|
|Gagné|**_15_**|9|24|
|Perdu|5|21|26|
|Total|**_20_**|30|50|

## Propriétés

- $0\leq P_{A}(B)\leq 1 \qquad$ (Une probabilité est un nombre entre $0$ et $1$)
- $P_{A}\left(\overline{B}\right)=1-P_{A}\left(B\right) \qquad$ (Probabilité de l'événement contraire)
- $P(A\cap B)=P_{A}(B)\times P(A)$

\newpage

# Arbre pondéré

## Exemple : Gagné ou perdu

50 boules : 20 rouges et 30 noires.

- Sur 15 rouges, il est marqué "Gagné"
- Sur 9 noires, il est marqué "Gagné"

$R$ : On tire une boule rouge$\qquad$ $G$ : On tire un " gagné "

L'expérience aléatoire peut être schématisée par **un arbre pondéré** (ou arbre de _probabilité_).

\begin{center}
\begin{tikzpicture}
\tikzset{grow=right,level distance=4.5cm,sibling distance=3cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base east}}
\Tree   [.{On tire une boule}
            \edge node[auto=right]{$P(\overline{R})=\dfrac{30}{50}$};
            [.$\overline{R}$ 
                \edge node[auto=right]{$P_{\overline{R}}(\overline{G})=\dfrac{21}{30}$};
                [.$\overline{G}$ $P(\overline{R}\cap \overline{G})$ ]
                \edge node[auto=left]{$P_{\overline{R}}(G)=\dfrac{9}{30}$};
                [.$G$ $P(\overline{R}\cap G)$ ]
            ]
            \edge node[auto=left]{$P(R)=\dfrac{20}{50}$};
            [.$R$
                \edge node[auto=right]{$P_{R}(\overline{G})=\dfrac{5}{20}$};
                [.$\overline{G}$  $P(R\cap \overline{G})$ ]
                \edge node[auto=left]{$P_{R}(G)=\dfrac{15}{20}$};
                [.$G$ $P(R\cap G)$ ]
            ]
        ]
\end{tikzpicture}
\end{center}


## Règle 1 : Branches issues d'un même noeud

La somme des probabilités des branches issues d'un même noeud est égale à 1.

\begin{center}
$P(A)+ P(\overline{A}) = 1$\\
\begin{tikzpicture}
\tikzset{grow=right,level distance=4cm,sibling distance=2cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base east}}
\Tree   [.{}
            \edge node[auto=right]{$P(\overline{A})$};
            [.$\overline{A}$ 
            ]
            \edge node[auto=left]{$P(A)$};
            [.$A$
            ]
        ]
\end{tikzpicture}
\end{center}

### Exemples {-}

\begin{center}
\begin{tikzpicture}
\tikzset{grow=right,level distance=4cm,sibling distance=2cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base east}}
\Tree   [.{}
            \edge node[auto=right]{$0.35$}; [.$\overline{A}$ ]
            \edge node[auto=left]{$0.65$}; [.$A$ ]
        ]
\end{tikzpicture}
\qquad
\begin{tikzpicture}
\tikzset{grow=right,level distance=4cm,sibling distance=2cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base east}}
\Tree   [.{}
            \edge node[auto=right]{$0.81$}; [.$\overline{E}$ ]
            \edge node[auto=left]{$0.19$}; [.$E$ ]
        ]
\end{tikzpicture}
\qquad
\begin{tikzpicture}
\tikzset{grow=right,level distance=4cm,sibling distance=2cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base east}}
\Tree   [.{}
            \edge node[auto=right]{$\dfrac{2}{7}$}; [.$\overline{G}$ ]
            \edge node[auto=left]{$\dfrac{5}{7}$}; [.$G$ ]
        ]
\end{tikzpicture}
\end{center}

## Règle 2 : Probabilité d'une "feuille"

La probabilité d'une "feuille" (extrémité d'un chemin) est égale au **produit** des probabilités du chemin aboutissant à cette feuille.

### Exemple {-}

\begin{center}
\begin{tikzpicture}
\tikzset{grow=right,level distance=3.5cm,sibling distance=1cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base west}}
\Tree   [.{}
            \edge node[auto=right]{$0.4$};
            [.$\overline{A}$
                \edge[dashed] node[]{};
                [.{} ]
                \edge[dashed] node[]{};
                [.{} ]
            ]
            \edge node[auto=left]{$0.6$};
            [.$A$
                \edge[dashed] node[]{};
                [.{} ]
                \edge node[auto=left]{$0.9$};
                [.$B\qquad\rightarrow P(A\cap B)=0.6\times 0.9=0.54$ ]
            ]
        ]
\end{tikzpicture}
\end{center}

## Règle 3 : Probabilités totales

La probabilité d'un événement associé à plusieurs "feuilles" est égale à **la somme** des probabilités de chacune de ces "feuilles".

\begin{center}
\begin{tikzpicture}
\tikzset{grow=right,level distance=3.5cm,sibling distance=1cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base west}}
\Tree   [.{}
            \edge node[auto=right]{$0.3$};
            [.$\overline{A}$
                \edge[dashed] node[]{};
                [.{} ]
                \edge node[auto=left]{$0.63$};
                [.$B\quad\rightarrow P(\overline{A}\cap B)=0.3\times0.63$ ]
            ]
            \edge node[auto=left]{$0.7$};
            [.$A$
                \edge[dashed] node[]{};
                [.{} ]
                \edge node[auto=left]{$0.85$};
                [.$B\quad\rightarrow P(A\cap B)=0.7\times0.85$ ]
            ]
        ]
\end{tikzpicture}
\begin{align*}
P(B)&=P(A\cap B)+P(\overline{A}\cap B)\\
\quad&=0.7\times0.85+0.3\times0.63\\
\quad&=0.595+0.169=0.784
\end{align*}
\end{center}

### Exemple : Gagné ou perdu

\begin{center}
\begin{tikzpicture}
\tikzset{grow=right,level distance=4cm,sibling distance=1.5cm}
\tikzset{execute at begin node=\strut}
\tikzset{every tree node/.style={anchor=base west}}
\Tree   [.{}
            \edge node[auto=right]{$\frac{30}{50}=0.6$};
            [.$\overline{R}$ 
                \edge node[auto=right]{$\frac{21}{30}=0.7$};
                [.$\overline{G}$ ]
                \edge node[auto=left]{$\frac{9}{30}=0.3$};
                [.$G\rightarrow P(\overline{R}\cap G)=0.6\times 0.3$ ]
            ]
            \edge node[auto=left]{$\frac{20}{50}=0.4$};
            [.$R$
                \edge node[auto=right]{$\frac{5}{20}=0.25$};
                [.$\overline{G}$ ]
                \edge node[auto=left]{$\frac{15}{20}=0.75$};
                [.$G\rightarrow P(R\cap G)=0.4\times 0.75$ ]
            ]
        ]
\end{tikzpicture}
\end{center}

- $P(R\cap G) = 0.4 \times 0.75$           \quad "Rouge et Gagné"
- $P(\overline{R}\cap G) = 0.6 \times 0.3$ \quad "Noire et Gagné"

\begin{align*}
P(G)  &=P(R\cap G)+P(\overline{R}\cap G)\\
\quad &= 0.4 \times 0.75 + 0.6 \times 0.3\\
\quad &= 0.3 + 0.18 = 0.48
\end{align*}

\newpage

# Probabilités et indépendance

## Définition : Indépendance

On dit que deux évènements $A$ et $B$ de probabilité non nulle sont **indépendants** lorsque :

\begin{center}
$P_{A}(B)=P(B)$/qquad ou/qquad $P_{B}(A)=P(A)$
\end{center}

## Propriété : $P(A\cap B)$
Soient $A$ et $B$ , deux événements **indépendants** alors

\begin{center}
$P(A\cap B)=P(A)\times P(B)$
\end{center}

### Preuve {-}

Par définition, $P_{A}(B)=\dfrac{P(A\cap B)}{P(A)}$\qquad donc\qquad $P(A\cap B)=P(A)\times P_{A}(B)$

Si $A$ et $B$ sont **indépendants** alors $P_{A}(B)=P(B)$

Donc $P(A\cap B)=P(A)\times P(B)$

### Exemple {-}

On tire une carte au hasard dans un jeu de 32 cartes.

- Soit $R$ l'événement "On tire un roi".
- Soit $T$ l'événement "On tire un trèfle".

On a : $P(R)=\dfrac{4}{32}=\dfrac{1}{8}$\qquad et\qquad $P(T)=\dfrac{8}{32}$

Par ailleurs, $P_{T}(R)$ est la probabilité de tirer un roi parmi les trèfles.

On a alors : $P_{T}(R)=\dfrac{1}{8}$\qquad (un roi parmi les 8 trèfles)

Ainsi, $P_{T}(R)=P(R)$

Les événements $R$ et $T$ **sont indépendants**.

### Exemple {-}

On tire une carte au hasard dans un jeu de 32 cartes *+ 2 jokers*.

On a : $P(R)=\dfrac{4}{34}=\dfrac{2}{17}$\qquad et \qquad $P_{T}(R)=\dfrac{1}{8}$

Ainsi, $P_{T}(R)\neq P(R)$

Les événements $R$ et $T$ **ne sont pas indépendants**.

\newpage

## Méthode : Utiliser l'indépendance de deux événements

Dans une population, un individu est atteint par la maladie $a$ avec une probabilité égale à $0,005$ et par la maladie $b$ avec une probabilité égale à $0,001$.

On choisit au hasard un individu de cette population.

- Soit $A$ l'événement "L'individu a la maladie a".
- Soit $B$ l'événement "L'individu a la maladie b".

On suppose que les événements A et B sont **indépendants**.

> \ding{46} Calculer de $P(A\cap B)$ et interpréter le résultat.

Par définition, $P_{A}(B)=\dfrac{P(A\cap B)}{P(A)}$\qquad donc\qquad $P(A\cap B)=P_{A}(B)\times P(A)$

Or, $A$ et $B$ sont indépendants donc $P_{A}(B)=P(B)$

Donc 

\begin{align*}
P(A\cap B)&=P(B) \times P(A)\\
\quad&= 0,001 \times 0,005\\
\quad&= 1\times 10^{-3} \times 5\times 10^{-3}\\
\quad&= 5 \times 10^{-6}= 0,000 005
\end{align*}

La probabilité qu’un individu soit **atteint par les deux maladies** est égale à $0,000 005$

> \ding{46} Calculer de $P(A\cup B)$ et interpréter le résultat.

Par définition, $P(A \cup B) = P(A)+ P(B)- P(A\cap B)$

Donc

\begin{align*}
P(A\cup B)&= P(A)+ P(B)- P(A\cap B)\\
\quad&= 0,001 + 0,005 - 0,000005\\
\quad&= 1\times 10^{-3} + 5\times 10^{-3} - 5\times 10^{-6} \\
\quad&= 0,006 - 0,000005 = 0,005995
\end{align*}

La probabilité qu'un individu choisi au hasard ait **au moins une des deux maladies** est égale à 0,005 995.
