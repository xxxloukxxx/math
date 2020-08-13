---
title: Nombre dérivé
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

# Limite en zéro d'une fonction

## Exemple

Soit la fonction $f$ définie sur $\left\rbrack - \infty\ ;0 \right\lbrack \cup \left\rbrack 0\ ;\  + \infty \right\lbrack$ par $f\left( x \right) =\dfrac{\left( x + 1 \right)^{2} - 1}{x}$.

L'image de $0$ par la fonction $f$ n'existe pas. On s'intéresse cependant aux valeurs de $f\left( x \right)$ lorsque $x$ se rapproche de $0$.

  $x$                     -0,5   -0,1   -0,01   -0,001   ...   0,001   0,01   0,1   0,5
  ----------------------- ------ ------ ------- -------- ----- ------- ------ ----- -----
  $f\left( x \right)$     1,5    1,9    1,99    1,999    ?     2,001   2,01   2,1   2,5

On constate que $f\left( x \right)$ se rapproche de $2$ lorsque $x$ se rapproche de $0$.

On dit que la limite de $f$ lorsque $x$ tend vers $0$ est égale à $2$ et on note : $$\lim_{x \to 0}{f\left( x \right)} = 2$$

# Nombre dérivé

## Rappel : Coefficient directeur d'une droite

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=10cm,height=8cm,axis lines=middle,
ymajorgrids=true,xmajorgrids=true,
xmin=-3,xmax=7,ymin=-2,ymax=6,
xtick={-2.0,-1.0,...,6.0},ytick={-1.0,0.0,...,5.0},]
\draw [color=black!50,line width=2.pt,domain=-3:7] plot(\x,{(--7.--2.*\x)/3.});
\draw [color=black!50,line width=2.pt,domain=-3:7] plot(\x,{(--8.-2.*\x)/4.});
\draw [->,line width=1.pt,dash pattern=on 3pt off 3pt,color=blue] (1.,3.) -- (4.,3.);
\draw [->,line width=1.pt,dash pattern=on 3pt off 3pt,color=red] (4.,3.) -- (4.,5.);
\draw [->,line width=1.pt,dash pattern=on 3pt off 3pt,color=blue] (2.,1.) -- (6.,1.);
\draw [->,line width=1.pt,dash pattern=on 3pt off 3pt,color=red] (6.,1.) -- (6.,-1.);
\draw [color=blue](2.5,3) node[anchor=north] {3};
\draw [color=red](4.0,4.0) node[anchor=west] {2};
\draw [color=blue](4.0,1) node[anchor=south] {4};
\draw [color=red](6.0,0.0) node[anchor=south west] {-2};
\draw [fill=black] (1.,3.) circle (2.5pt);
\draw[color=black] (1.0,3.0) node[anchor=south east] {$A$};
\draw [fill=black] (4.,5.) circle (2.5pt);
\draw[color=black] (4.0,5.0) node[anchor=south east] {$B$};
\draw [fill=black] (2.,1.) circle (2.5pt);
\draw[color=black] (2.0,1.0) node[anchor=north east] {$C$};
\draw [fill=black] (6.,-1.) circle (2.5pt);
\draw[color=black] (6.0,-1.0) node[anchor=north east] {$D$};
\end{axis}
\end{tikzpicture}
\end{center}

Le coefficient directeur de la droite (AB) est égal à : $$\dfrac{5 - 3}{4 - 1} = \frac{2}{3}$$

Le coefficient directeur de la droite (CD) est égal à : $$\frac{- 1 - 1}{6 - 2} = \frac{- 2}{4} = - \frac{1}{2}$$

\newpage

## Définition : Nombre dérivé

Soit une fonction $f$ et $\mathcal{C}_f$ sa représentation graphique dans le repère ci-dessous.

Soit $A$ et $M$ deux points de la courbe représentative de $f$ d'abscisses respectives $(a)$ et $(a+h)$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=14cm,height=10cm,axis lines=middle,xmin=-2.0,xmax=6.0,ymin=-1.0,ymax=6.0,
xtick={0,2,...,10},ytick={0,2,...,10},]
\clip(-2.,-1.) rectangle (6.,6.);
\draw[line width=2.pt,color=green,smooth,domain=-2.0:6.0] plot(\x,{0-0.25*((\x)-8.0)*((\x)+1.0)});
\draw [line width=1.pt,color=black!50,domain=-2.:6.] plot(\x,{(--5.5--1.5*\x)/2.});
\draw [dashed,line width=0.5pt,color=red!40,domain=-2.:6.] plot(\x,{(1.25*\x+2.25});
\draw [line width=1.pt,dash pattern=on 4pt off 4pt] (1.,0.)-- (1.,3.5);
\draw [line width=1.pt,dash pattern=on 4pt off 4pt] (1.,3.5)-- (0.,3.5);
\draw [line width=1.pt,dash pattern=on 4pt off 4pt] (3.,5.)-- (0.,5.);
\draw [line width=1.pt,dash pattern=on 4pt off 4pt] (3.,0.)-- (3.,3.5);
\draw [color=blue,->,line width=1.5pt] (1.,3.5) -- (3.,3.5);
\draw [color=red,->,line width=1.5pt] (3.,3.5) -- (3.,5.);
\draw (3.0,0.0) node[anchor=north] {$a+h$};
\draw (1.0,0.0) node[anchor=north] {$a$};
\draw (0.0,3.5) node[anchor=east] {$f(a)$};
\draw (0,5.0) node[anchor=east] {$f(a+h)$};
\draw (2.0,3.5) node[anchor=north] {$h$};
\draw (3.00,4.25) node[anchor=west] {$f(a+h)-f(a)$};
\draw [fill=black] (1.,3.5) circle (2.0pt);
\draw[color=black] (1.,3.5) node[anchor=south east] {$A$};
\draw [fill=black] (3.,5.) circle (2.0pt);
\draw[color=black] (3.,5.) node[anchor=south east] {$M$};
\draw [fill=black] (3.,3.5) circle (2.0pt);
\end{axis}
\end{tikzpicture}
\end{center}

Le coefficient directeur de la droite (AM) est égal à : $$\frac{f\left( a + h \right) - f\left( a \right)}{a + h - a} = \frac{f\left( a + h \right) - f\left( a \right)}{h}$$.

Lorsque le point M se rapproche du point A, le coefficient directeur de la droite (AM) est égal à la limite de $\left(\dfrac{f\left( a + h \right) - f\left( a \right)}{h}\right)$ lorsque $h$ tend vers $0$.

Ce coefficient directeur s'appelle le **nombre dérivé** de $f$ en $a$ et on le note $f'(a)$.

$$f'(a)=\lim_{h\to 0}\left(\dfrac{f\left( a + h \right) - f\left( a \right)}{h}\right)$$

\newpage

## Méthode : Calculer le nombre dérivé

Soit la fonction $f$ définie sur $\mathbb{R}$ par $f\left( x \right) = x^{2} + 2x - 3$.

> a) Calculer le nombre dérivé de la fonction $f$ en $x = 2$.

---

(a) On commence par calculer $\dfrac{f\left( 2 + h \right) - f\left( 2 \right)}{h}$ 

On a :
\begin{align*}
f\left(2+h\right)   &= \left(2+h\right)^{2}+2\times\left(2+h\right)-3 & f\left(2\right) &=\left(2\right)^{2}+2\times\left(2\right)-3\\
                    &= 4+4h+h^{2}+4+2h-3                        &                 &=4+4-3\\
                    &= h^{2}+6h+5                               &                 &=5
\end{align*}
Donc
\begin{align*}
\dfrac{f\left( 2 + h \right) - f\left( 2 \right)}{h}    &=\dfrac{\left(h^{2}+6h+5\right)-(5)}{h}\\
                                                        &=\dfrac{h^{2}+6h}{h}\\
                                                        &=\frac{h\left( h + 6 \right)}{h}\\
                                                        &=h+6
\end{align*}

Puis on calcule la limite de $\left(\dfrac{f\left(2+h\right)-f\left(2\right)}{h}\right)$ lorsque $h$ tend vers $0$ :

$$\lim_{h\to 0}\frac{f\left(2+h\right)-f\left(2\right)}{h}=\lim_{h\to 0}{(h+6)}=6$$

Le nombre dérivé de $f$ en $2$ est égal à $6$. Et on note $f'(2) = 6$.

\newpage

# Tangente à une courbe

## Définition : Tangente une courbe représentative d'une fonction

$A$ est un point d'abscisse $a$ appartenant à la courbe représentative d'une fonction $f$.

La **tangente** à la courbe au point $A$ d'abscisse $a$ est la droite :

- passant par A,
- de coefficient directeur le nombre dérivé $f'(a)$.

\begin{figure}
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[
width=14cm,height=10cm,axis lines=middle,xmin=-1.0,xmax=5.0,ymin=-1.0,ymax=6.0,ymajorgrids=true,xmajorgrids=true,
xtick={-2.0,-1.0,...,6.0},ytick={-1.0,0.0,...,6.0},]
\draw[line width=2.pt,color=green,smooth,samples=100,domain=-2.0:6.0] plot(\x,{0-0.25*((\x)-8.0)*((\x)+1.0)});
\draw [dashed,color=black,line width=1.pt] (2.,0.) -- (2.,4.5);
\draw [dashed,color=black,line width=1.pt] (0.,4.5) -- (2.,4.5);
\draw (2.,0.) node[anchor=south west] {$a$};
\draw (0,4.5) node[anchor=east] {$f(a)$};
\draw [color=red,line width=2.pt,domain=-2.:6.] plot(\x,{(--3.--0.75*\x)/1.});
\draw [color=red] (3,6) node[anchor=north east] {$y=f'(a)\times x+p$};
\draw [color=green] (4,5) node[anchor=south west] {$\mathcal{C}_f$};
\draw [fill=black] (2.,4.5) circle (2.0pt);
\draw[color=black] (2.,4.5) node[anchor=south east] {$A$};
\end{axis}
\end{tikzpicture}
\end{center}
\caption{Tangente à une courbe représentant une fonction $f$}
\end{figure}

## Méthode : Déterminer le coefficient directeur d'une tangente à une courbe

On considère la fonction $f$ définie sur $\mathbb{R}$ par $f\left( x \right) = x^{2} + 2x - 3$ dont le nombre dérivé en $2$ a été calculé plus haut.

> a) Déterminer le coefficient directeur de la tangente à la courbe représentative de $f$ au point $A$ de la courbe d'abscisse $2$.
> b) Construire la tangente à la courbe de la fonction $f$ en $2$.
> c) En s'aidant de la calculatrice graphique, reproduire la courbe de la fonction $f$
> d) Donner une équation de la tangente.

---

(a) On a vu que le nombre dérivé de $f$ en $2$ est égal à $6$. $f'(2)=6$

Ainsi la tangente à la courbe représentative de $f$ au point A de la courbe d'abscisse $2$ est la droite passant par $A$ et de coefficient directeur $6$.

\newpage

(b) On commence par placer le point $A$ de coordonnées $(2 ; f(2))$, avec $f(2) = 2^2 + 2 \times 2 - 3 = 5$.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[width=14cm,height=10cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-2,xmax=4,ymin=-10,ymax=15,xtick={-4.0,-3,...,4.0},ytick={-15.0,-10.0,...,20.0},]
\draw[line width=2.pt,color=green,smooth,samples=100,domain=-2:4] plot(\x,{(\x)^(2.0)+2.0*(\x)-3.0});
\draw [fill=black] (2.,5.) circle (2.5pt);
\draw[color=black] (2.0,5.0) node[anchor=south east] {$A$};
\draw[color=black] (-2,-5) node[anchor=north west] {$\mathcal{C}_f$};
\end{axis}
\end{tikzpicture}
\end{center}


On trace la tangente passant par A et de coefficient directeur $6$. Pour cela, on avance de $1$ dans le sens des abscisses puis de $6$ dans le sens des ordonnées.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\begin{axis}[width=14cm,height=10cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-2,xmax=4,ymin=-10,ymax=15,xtick={-4.0,-3,...,4.0},ytick={-15.0,-10.0,...,10,11,15,20.0},]
\draw[line width=2.pt,color=green,smooth,samples=100,domain=-2:4] plot(\x,{(\x)^(2.0)+2.0*(\x)-3.0});
\draw [line width=2.pt,color=blue!50,domain=-2:4] plot(\x,{(-7.--6.*\x)/1.});
\draw [dashed,color=blue,->,line width=1.pt] (2.,5.) -- (3.,5.);
\draw [dashed,color=red,->,line width=1.pt] (3.,5.) -- (3.,11.);
\draw [fill=black] (2.,5.) circle (2.5pt);
\draw[color=black] (2.0,5.0) node[anchor=south east] {$A$};
\draw [fill=black] (3.,11.) circle (2.5pt);
\draw[color=black] (3.0,11.0) node[anchor=west] {$B$};
\draw[color=black] (-2,-5) node[anchor=north west] {$\mathcal{C}_f$};
\draw[color=blue] (2.5,5) node[anchor=north] {$1$};
\draw[color=red] (3.0,8.0) node[anchor=west] {$6$};
\end{axis}
\end{tikzpicture}
\end{center}

\newpage

(c) A l'aide de la calculatrice, on a :

| ![](media/courbe(1)-casio.png){height=3cm} | ![](media/courbe(2)-casio.png){height=3cm} |
|:-:|:-:|
| ![](media/courbe(1)-ti.png){height=4cm} | ![](media/courbe(2)-ti.png){height=4cm} |

Table: La courbe $\mathcal{C}_f$ sur la calculatrice CASIO et TI

(d) Une équation de la tangente en 2 est de la forme $y = 6x + p$.

Pour calculer $p$, on sait que le point $A$ appartient à la tangente donc ses coordonnées $(2 ; 5)$ vérifient l'équation de la tangente $y = 6x + p$.

\begin{align*}
y_A &= 6 \times x_A + p\\
5 &= 6 \times 2 + p\\
5 &= 12 + p\\
p &= -7
\end{align*}

Une équation de tangente à la courbe représentative de $f$ au point $A$ d'abscisse $2$ est $y = 6x - 7$.

\newpage

### Remarques {-}

À l'aide de la calculatrice, il est possible de tracer la tangente à une courbe en un point.

Une fois la courbe tracée sur la calculatrice, saisir :

- TI-83 : Touches ```2nde``` + ```PGRM``` (Dessin) puis ```5: Tangente``` et saisir l'abscisse du point $A$, ici $2$. Puis ```ENTER```.

![Courbe et tangente avec TI](media/courbe(3)-ti.png){width=50%}

- Casio Graph 85 : Touches ```SHIFT``` + ```F4``` (Skech) puis ```Tang``` et saisir l'abscisse du point $A$ , ici $2$. Puis ```EXE``` + ```EXE```.

![Courbe et tangente avec Casio](media/courbe(3)-casio.png){width=50%}