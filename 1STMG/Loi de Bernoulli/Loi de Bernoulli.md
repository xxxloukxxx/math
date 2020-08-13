---
title: Loi de Bernoulli
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

# Expériences aléatoire à deux épreuves

## Définition : Indépendance de deux expériences

Deux expériences sont dites **indépendantes** si le résultat de l'une n'a aucune influence sur le résultat de l'autre.

## Méthode : Calculer une probabilité associée à une expérience aléatoire à deux épreuves

Léa tente l'expérience suivante avec ses vêtements :

Elle dépose dans un panier 4 chemisiers indiscernables au toucher : 1 blanc, 1 rouge et 2 verts.

Dans un autre panier, elle y dépose 2 jupes également indiscernables au toucher : 1 blanche et 1 noire.

Elle tire successivement et au hasard, un chemisier du premier panier et une jupe du deuxième panier.

Ces deux expériences, "tirer un vêtement dans chaque panier", sont **indépendantes**.

> a) Représenter la situation à l'aide d'un arbre pondéré.
> b) Calculer la probabilité $P_1$ d'obtenir deux vêtements blancs.
> c) Calculer la probabilité $P_2$ de ne pas obtenir un chemisier vert et d'obtenir une jupe noire.

---

(a) La probabilité de tirer un chemisier vert est égale à $0,5$ car le premier panier contient $2$ chemisiers verts sur $4$ en tout, soit $P\left( V \right) =\dfrac{2}{4}= 0,5$.

\begin{center}
\begin{tikzpicture}[xscale=1.0,yscale=1]
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1.5)*\DistanceInterNiveaux}
\def\NiveauC{(2.5)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
\node[noeud] (R) at ({\NiveauA},{(2.5)*\InterFeuilles}) {$$};
\node[noeud,fill=white!20] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$B$};
\node[feuille,fill=white!20] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$B$};
\node[feuille,fill=black!20] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$N$};
\node[noeud,fill=red!20] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$R$};
\node[feuille,fill=white!20] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$B$};
\node[feuille,fill=black!20] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$N$};
\node[noeud,fill=green!20] (Rc) at ({\NiveauB},{(4.5)*\InterFeuilles}) {$V$};
\node[feuille,fill=white!20] (Rca) at ({\NiveauC},{(4)*\InterFeuilles}) {$B$};
\node[feuille,fill=black!20] (Rcb) at ({\NiveauC},{(5)*\InterFeuilles}) {$N$};
\draw[fleche] (R)--(Ra) node[etiquette] {$0.25$};
\draw[fleche] (Ra)--(Raa) node[etiquette] {$0.5$};
\draw[fleche] (Ra)--(Rab) node[etiquette] {$0.5$};
\draw[fleche] (R)--(Rb) node[etiquette] {$0.25$};
\draw[fleche] (Rb)--(Rba) node[etiquette] {$0.5$};
\draw[fleche] (Rb)--(Rbb) node[etiquette] {$0.5$};
\draw[fleche] (R)--(Rc) node[etiquette] {$0.5$};
\draw[fleche] (Rc)--(Rca) node[etiquette] {$0.5$};
\draw[fleche] (Rc)--(Rcb) node[etiquette] {$0.5$};
\end{tikzpicture}
\end{center}

\newpage

(b) La probabilité d'obtenir deux vêtements blancs correspond aux issues $(B;B)$,

**Sur un "chemin de branches", les probabilités se multiplient :**

\begin{center}
% Racine à Gauche, développement vers la droite
\begin{tikzpicture}[xscale=1,yscale=0.6]
% Styles (MODIFIABLES)
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{feuille2}=[fill=white,text=red]
\tikzstyle{etiquette}=[midway,fill=white]
% Dimensions (MODIFIABLES)
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
% Dimensions calculées (NON MODIFIABLES)
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1.6666666666666665)*\DistanceInterNiveaux}
\def\NiveauC{(3)*\DistanceInterNiveaux}
\def\NiveauD{(4)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
% Noeuds (MODIFIABLES : Styles et Coefficients d'InterFeuilles)
\node[noeud] (R) at ({\NiveauA},{(2.5)*\InterFeuilles}) {$$};
\node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$B$};
\node[noeud] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$B$};
\node[feuille2] (Raaa) at ({\NiveauD},{(0)*\InterFeuilles}) {$0.25\times 0.5=0.125$};
\node[feuille,fill=black!20] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$N$};
\node[noeud,fill=red!20] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$R$};
\node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$B$};
\node[feuille,fill=black!20] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$N$};
\node[noeud,fill=green!20] (Rc) at ({\NiveauB},{(4.5)*\InterFeuilles}) {$V$};
\node[feuille] (Rca) at ({\NiveauC},{(4)*\InterFeuilles}) {$B$};
\node[feuille,fill=black!20] (Rcb) at ({\NiveauC},{(5)*\InterFeuilles}) {$N$};
% Arcs (MODIFIABLES : Styles)
\draw[fleche,color=red,line width=2pt] (R)--(Ra) node[etiquette] {$0.25$};
\draw[fleche,color=red,line width=2pt] (Ra)--(Raa) node[etiquette] {$0.5$};
\draw[fleche,color=red,line width=2pt] (Raa)--(Raaa) node {$$};
\draw[fleche] (Ra)--(Rab) node[etiquette] {$0.5$};
\draw[fleche] (R)--(Rb) node[etiquette] {$0.25$};
\draw[fleche] (Rb)--(Rba) node[etiquette] {$0.5$};
\draw[fleche] (Rb)--(Rbb) node[etiquette] {$0.5$};
\draw[fleche] (R)--(Rc) node[etiquette] {$0.5$};
\draw[fleche] (Rc)--(Rca) node[etiquette] {$0.5$};
\draw[fleche] (Rc)--(Rcb) node[etiquette] {$0.5$};
\end{tikzpicture}
\end{center}

Soit : $P_1=P(B ; B)=0,25 \times 0,5=0,125$. La probabilité d'obtenir deux vêtements blancs est égale à $12,5$%.

(c) La probabilité de ne pas obtenir un chemisier vert et d'obtenir une jupe noire correspond aux issues $(B ; N)$ et $(R ; N)$.

**Les probabilités de "plusieurs feuilles" s'additionnent :**

\begin{center}
% Racine à Gauche, développement vers la droite
\begin{tikzpicture}[xscale=1,yscale=1]
% Styles (MODIFIABLES)
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{feuille2}=[fill=white,text=red]
\tikzstyle{etiquette}=[midway,fill=white]
% Dimensions (MODIFIABLES)
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
% Dimensions calculées (NON MODIFIABLES)
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1.6666666666666665)*\DistanceInterNiveaux}
\def\NiveauC{(3)*\DistanceInterNiveaux}
\def\NiveauD{(4)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
% Noeuds (MODIFIABLES : Styles et Coefficients d'InterFeuilles)
\node[noeud] (R) at ({\NiveauA},{(2.5)*\InterFeuilles}) {$$};
\node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$B$};
\node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$B$};
\node[noeud,fill=black!20] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$N$};
\node[feuille2] (Raba) at ({\NiveauD},{(1)*\InterFeuilles}) {$0.25\times 0.5=0.125$};
\node[noeud,fill=red!20] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$R$};
\node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$B$};
\node[noeud,fill=black!20] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$N$};
\node[feuille2] (Rbba) at ({\NiveauD},{(3)*\InterFeuilles}) {$0.25\times 0.5=0.125$};
\node[noeud,fill=green!20] (Rc) at ({\NiveauB},{(4.5)*\InterFeuilles}) {$V$};
\node[feuille] (Rca) at ({\NiveauC},{(4)*\InterFeuilles}) {$B$};
\node[feuille,fill=black!20] (Rcb) at ({\NiveauC},{(5)*\InterFeuilles}) {$N$};
% Arcs (MODIFIABLES : Styles)
\draw[fleche,color=red,line width=2pt] (R)--(Ra) node[etiquette] {$0.25$};
\draw[fleche] (Ra)--(Raa) node[etiquette] {$0.5$};
\draw[fleche,color=red,line width=2pt] (Ra)--(Rab) node[etiquette] {$0.5$};
\draw[fleche,color=red,line width=2pt] (Rab)--(Raba) node {$$};
\draw[fleche,color=red,line width=2pt] (R)--(Rb) node[etiquette] {$0.25$};
\draw[fleche] (Rb)--(Rba) node[etiquette] {$0.5$};
\draw[fleche,color=red,line width=2pt] (Rb)--(Rbb) node[etiquette] {$0.5$};
\draw[fleche,color=red,line width=2pt] (Rbb)--(Rbba) node {$$};
\draw[fleche] (R)--(Rc) node[etiquette] {$0.5$};
\draw[fleche] (Rc)--(Rca) node[etiquette] {$0.5$};
\draw[fleche] (Rc)--(Rcb) node[etiquette] {$0.5$};
\end{tikzpicture}
\end{center}

$P_2=P(B ; N) + P(R ; N)=\left(0,25\times 0,5\right) + \left(0,25\times 0,5\right)=0,125 + 0,125=0,25$.

La probabilité de ne pas obtenir un chemisier vert et d'obtenir une jupe noire est égale à 25 %.

\newpage

# Épreuve de Bernoulli

## Définition : Épreuve de Bernoulli

Une **épreuve de Bernoulli** est une expérience aléatoire à deux issues que l'on peut nommer **"succès"** ou **"échec"**.

\begin{center}
\begin{tikzpicture}[xscale=1,yscale=1]
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
\node[noeud] (R) at ({\NiveauA},{(0.5)*\InterFeuilles}) {};
\node[feuille] (Ra) at ({\NiveauB},{(0)*\InterFeuilles}) {Succès};
\node[feuille] (Rb) at ({\NiveauB},{(1)*\InterFeuilles}) {Échec};
\draw[fleche] (R)--(Ra);
\draw[fleche] (R)--(Rb);
\end{tikzpicture}
\end{center}


### Remarque {-}

Au **succès**, on peut associer le nombre $1$ et à l'**échec**, on peut associer le nombre $0$.

### Exemples {-}

a)  Le jeu du pile ou face : On considère par exemple comme succès **"obtenir pile"** et comme échec **"obtenir face"**.
b)  On lance un dé et on considère par exemple comme succès **"obtenir un 1"** et comme échec **"ne pas obtenir un 1"**.

La loi de Bernoulli associée à cette expérience est :

| $x_i$ | 1 | 0 |
|:-:|:-:|:-:|
| $P\left(X={x}_i\right)$ | $\dfrac{1}{6}$ | $\dfrac{5}{6}$ |

## Définition : loi de Bernoulli

Une **loi de Bernoulli** est une loi de probabilité qui suit le schéma suivant :

- la probabilité d'obtenir $1$ est égale à $p$,
- la probabilité d'obtenir $0$ est égale à $\left(1- p\right)$.

$p$ est appelé le **paramètre** de la loi de Bernoulli.

On peut résumer la loi de Bernoulli de paramètre $p$ dans le tableau :

| $x_i$ | 1 | 0 |
|:-:|:-:|:-:|
| $P\left(X={x}_i\right)$ | $p$ | $1-p$ |

\newpage

### Exemples {-}

Dans les exemples présentés plus haut : 

a) $p=\dfrac{1}{2}$
\begin{center}
\begin{tikzpicture}[xscale=1,yscale=1]
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
\node[noeud] (R) at ({\NiveauA},{(0.5)*\InterFeuilles}) {};
\node[feuille] (Ra) at ({\NiveauB},{(0)*\InterFeuilles}) {P};
\node[feuille] (Rb) at ({\NiveauB},{(1)*\InterFeuilles}) {F};
\draw[fleche] (R)--(Ra) node[etiquette] {$\frac{1}{2}$};
\draw[fleche] (R)--(Rb) node[etiquette] {$\frac{1}{2}$};
\end{tikzpicture}
\end{center}

b) $p=\dfrac{1}{6}$
\begin{center}
\begin{tikzpicture}[xscale=1.5,yscale=1]
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
\node[noeud] (R) at ({\NiveauA},{(0.5)*\InterFeuilles}) {};
\node[feuille] (Ra) at ({\NiveauB},{(0)*\InterFeuilles}) {Obtenir un 1};
\node[feuille] (Rb) at ({\NiveauB},{(1)*\InterFeuilles}) {Ne pas obtenir un 1};
\draw[fleche] (R)--(Ra) node[etiquette] {$\frac{1}{6}$};
\draw[fleche] (R)--(Rb) node[etiquette] {$\frac{5}{6}$};
\end{tikzpicture}
\end{center}

## Propriété : Espérance

Soit $X$ une variable aléatoire qui suit la loi de Bernoulli de paramètre $p$. Alors : $$E(X)=p$$

### Démonstration : 

$E(X)=\left(1 \times p\right) + \left(0  \times (1 - p)\right)=p$

## Méthode : Reconnaître une situation modélisée par une loi de Bernoulli

Après la correction d'un contrôle, le professeur compte que $24$ élèves ont obtenu une note supérieure ou égale à $10$, et $6$ ne l'ont pas obtenue.

Le professeur choisit une copie au hasard. 

> a)Justifier que cette situation peut être modélisée par une loi de Bernoulli.

---

(a) Cette expérience aléatoire possède **deux issues** :

- La copie indique une note supérieure ou égale à 10
- La copie indique une note inférieur à 10

On peut ainsi considérer comme **succès** l'événement "la copie indique une note supérieure ou égale à 10".

La probabilité du succès est égale à $p=\dfrac{24}{30}=\dfrac{4}{5}$.

La situation est donc modélisée par une loi de Bernoulli de paramètre $p=\dfrac{4}{5}$.

\begin{center}
\begin{tikzpicture}[xscale=1,yscale=1]
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
\node[noeud] (R) at ({\NiveauA},{(0.5)*\InterFeuilles}) {};
\node[feuille] (Ra) at ({\NiveauB},{(0)*\InterFeuilles}) {S};
\node[feuille] (Rb) at ({\NiveauB},{(1)*\InterFeuilles}) {E};
\draw[fleche] (R)--(Ra) node[etiquette] {$\frac{4}{5}$};
\draw[fleche] (R)--(Rb) node[etiquette] {$\frac{1}{5}$};
\end{tikzpicture}
\end{center}

# Répétitions d'épreuves de Bernoulli

## Définition : Expériences identiques et indépendantes

Plusieurs expériences sont **identiques et indépendantes** si :

- elles ont les mêmes issues,
- chaque issue possède la même probabilité.

### Exemple 1 :

On lance $5$ fois de suite un dé à six faces et on note à chaque fois le résultat.

À chaque lancer, on considère comme succès **"obtenir un six"** et comme échec **"ne pas obtenir un six"**.

On répète ainsi $5$ fois de suite **la même expérience** de Bernoulli (lancer un dé) et les expériences sont **indépendantes** l'une de l'autre : un lancer n'influence pas le résultat d'un autre lancer.

Pour **chaque expérience**, on a les probabilités suivantes :

\begin{center}
\begin{tikzpicture}[xscale=1,yscale=1]
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
\node[noeud] (R) at ({\NiveauA},{(0.5)*\InterFeuilles}) {};
\node[feuille] (Ra) at ({\NiveauB},{(0)*\InterFeuilles}) {S};
\node[feuille] (Rb) at ({\NiveauB},{(1)*\InterFeuilles}) {E};
\draw[fleche] (R)--(Ra) node[etiquette] {$\frac{1}{6}$};
\draw[fleche] (R)--(Rb) node[etiquette] {$\frac{5}{6}$};
\end{tikzpicture}
\end{center}

On dit ici que $p=\dfrac{1}{6}$ est le paramètre de l'épreuve de Bernoulli répétée $5$ fois.

### Exemple 2 :

On lance $20$ fois de suite une pièce de monnaie. On considère comme succès **"obtenir Pile**"* et comme échec **"obtenir Face**"*.

Ces expériences de Bernoulli sont **identiques et indépendantes**.

Pour chaque expérience, on a les probabilités suivantes :

\begin{center}
\begin{tikzpicture}[xscale=1,yscale=1]
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
\node[noeud] (R) at ({\NiveauA},{(0.5)*\InterFeuilles}) {};
\node[feuille] (Ra) at ({\NiveauB},{(0)*\InterFeuilles}) {S};
\node[feuille] (Rb) at ({\NiveauB},{(1)*\InterFeuilles}) {E};
\draw[fleche] (R)--(Ra) node[etiquette] {$0,5$};
\draw[fleche] (R)--(Rb) node[etiquette] {$0,5$};
\end{tikzpicture}
\end{center}

On dit ici que $p=0,5$ est le paramètre de l'épreuve de Bernoulli répétée $20$ fois.

\newpage

## Méthode : Calculer une probabilité associée à une épreuve de Bernoulli

Une urne contient $3$ boules blanches et $2$ boules rouges. On tire auhasard une boule et **on la remet dans l'urne**. On répète l'expérience **deux fois de suite**.

> 1) Représenter l'ensemble des issues de ces expériences dans un arbre.
> 2) Déterminer les probabilités suivantes :
>    a) On tire deux boules blanches.
>    b) On tire une boule blanche et une boule rouge.
>    c) On tire au moins une boule blanche.

---

(1) On note $A$ l'issue "On tire une boule blanche" et $\overline{A}$ l'issue contraire "On tire une boule rouge".

$P(A)=\dfrac{3}{5}=0,6$ et $P(\overline{A})=\dfrac{2}{5}$=0,4$.

On résume les issues de l'expérience dans un arbre pondéré :

\begin{center}
% Racine à Gauche, développement vers la droite
\begin{tikzpicture}[xscale=1,yscale=1]
% Styles (MODIFIABLES)
\tikzstyle{fleche}=[->,>=latex,thick]
\tikzstyle{noeud}=[fill=white]
\tikzstyle{feuille}=[fill=white]
\tikzstyle{etiquette}=[midway,fill=white]
% Dimensions (MODIFIABLES)
\def\DistanceInterNiveaux{3}
\def\DistanceInterFeuilles{2}
% Dimensions calculées (NON MODIFIABLES)
\def\NiveauA{(0)*\DistanceInterNiveaux}
\def\NiveauB{(1.6666666666666665)*\DistanceInterNiveaux}
\def\NiveauC{(3)*\DistanceInterNiveaux}
\def\NiveauD{(4)*\DistanceInterNiveaux}
\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
% Noeuds (MODIFIABLES : Styles et Coefficients d'InterFeuilles)
\node[noeud] (R) at ({\NiveauA},{(1.5)*\InterFeuilles}) {$$};
\node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$A$};
\node[noeud] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$A$};
\node[feuille] (Raaa) at ({\NiveauD},{(0)*\InterFeuilles}) {$0,6 \times 0,6 = 0,36$};
\node[noeud] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$\overline{A}$};
\node[feuille] (Raba) at ({\NiveauD},{(1)*\InterFeuilles}) {$0,6 \times 0,4 = 0,24$};
\node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$\overline{A}$};
\node[noeud] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$A$};
\node[feuille] (Rbaa) at ({\NiveauD},{(2)*\InterFeuilles}) {$0,4 \times 0,6 = 0,24$};
\node[noeud] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$\overline{A}$};
\node[feuille] (Rbba) at ({\NiveauD},{(3)*\InterFeuilles}) {$0,4 \times 0,4 = 0,16$};
% Arcs (MODIFIABLES : Styles)
\draw[fleche] (R)--(Ra) node[etiquette] {$0,6$};
\draw[fleche] (Ra)--(Raa) node[etiquette] {$0,6$};
\draw[fleche,dashed] (Raa)--(Raaa) node {$$};
\draw[fleche] (Ra)--(Rab) node[etiquette] {$0,4$};
\draw[fleche,dashed] (Rab)--(Raba) node {$$};
\draw[fleche] (R)--(Rb) node[etiquette] {$0,4$};
\draw[fleche] (Rb)--(Rba) node[etiquette] {$0,6$};
\draw[fleche,dashed] (Rba)--(Rbaa) node {$$};
\draw[fleche] (Rb)--(Rbb) node[etiquette] {$0,4$};
\draw[fleche,dashed] (Rbb)--(Rbba) node {$$};
\end{tikzpicture}
\end{center}


(2) En utilisant l'arbre, on peut déterminer les probabilités demandées
  a) Obtenir deux boules blanches correspond à l'issue $(A;A)$ : $P_1=0,36$ (d'après l'arbre).
  b) Obtenir une boule blanche et une boule rouge correspond aux issues :

   - $\left(A; \overline{A}\right)$
   - $\left(\overline{A};A\right)$ 

Donc $P_2 = 0,24 + 0,24 = 0,48$.
    
  c) Obtenir **au moins** une boule blanche correspond aux issues :

   - $\left(A;\overline{A}\right)$
   - $\left(A;A\right)$
   - $\left(\overline{A};A\right)$

Donc : $P_2=0,24 + 0,36 + 0,24=0,84$.
