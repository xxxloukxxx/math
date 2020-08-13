---
title:  'This is the title'
subtitle: "This is the subtitle"
theme : "Madrid"
header-includes: |

    \usepackage{pgf,tikz,pgfplots}
    \pgfplotsset{compat=1.15}
    \usepackage{mathrsfs}
    \usetikzlibrary{arrows}
    \usetikzlibrary{calc}
    \usepackage{}
abstract: This is a pandoc test ... 
---

# Pourquoi ?

## Parce que

* Le code source est lisible
* Il est *git*able
* Le résultat est le même que *Beamer*

## Du code

La coloration de code est très simple.

### Un Hello World!

Prout

~~~python
for i in range(100):
  print(i)
~~~

## Essai

\definecolor{zzttqq}{rgb}{0.6,0.2,0.}
\definecolor{ududff}{rgb}{0.30196078431372547,0.30196078431372547,1.}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.75cm,y=0.75cm]
\tikzstyle{every node}=[font=\fontsize{5}{6}\selectfont]
\begin{axis}[
x=0.75cm,y=0.75cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-4.0,
xmax=4.5,
ymin=-4.0,
ymax=4.0,
xtick={-4.0,-3.0,...,4.0},
ytick={-4.0,-3.0,...,4.0},]
\clip(-4.,-4.) rectangle (4.5,4.);
\fill[line width=2.pt,color=zzttqq,fill=zzttqq,fill opacity=0.10000000149011612] (-1.,1.) -- (1.,2.) -- (3.,-1.) -- (-2.,-1.) -- cycle;
\draw [line width=2.pt,color=zzttqq] (-1.,1.)-- (1.,2.);
\draw [line width=2.pt,color=zzttqq] (1.,2.)-- (3.,-1.);
\draw [line width=2.pt,color=zzttqq] (3.,-1.)-- (-2.,-1.);
\draw [line width=2.pt,color=zzttqq] (-2.,-1.)-- (-1.,1.);
\begin{scriptsize}
\draw[color=ududff] (-0.9029862832523686,1.2442735325913157) node {$A$};
\draw[color=ududff] (1.0912243929381173,2.24816190019741) node {$B$};
\draw[color=ududff] (3.099001128150307,-0.7499371435991685) node {$C$};
\draw[color=ududff] (-1.9068746508584635,-0.7499371435991685) node {$D$};
\end{scriptsize}
\end{axis}
\end{tikzpicture}

---

\begin{tikzpicture}
\tikzstyle{every node}=[font=\fontsize{5}{6}\selectfont]
\draw [help lines] (0,0) grid (3,3);
\coordinate (a) at (rnd,rnd);
\coordinate (b) at (3-rnd,3-rnd);
\draw (a) -- (b);
\node (c) at (1,2) {x};
\draw let \p1 = ($ (a)!(c)!(b) - (c) $),
          \n1 = {veclen(\x1,\y1)}
        in circle [at=(c), radius=\n1];
\end{tikzpicture}

---

## Des énumérations

* Apache
* BSD
* GPL
    - GPLv2
    - GPLv3
* MIT

## Des listes numérotées

1. Récupérer le projet
2. Installer `pandoc` 
3. Installer les dépendances

    a. `texlive-latex-base` 
    b. `latex-beamer` 

4. Installer un lecteur ( `impressive` )
5. `make run` 

## Des citations

Celle-ci est de [*Mitch Resnick*](https://en.wikipedia.org/wiki/Mitchel_Resnick).

> If you learn to read, you can then read to learn.\
> If you learn to code, you can then code to learn.[^ted]

[^ted]: \tiny<http://www.ted.com/talks/mitch_resnick_let_s_teach_kids_to_code.html>

## Des apparitions

Par étapes :

> - d'abord…
> - ensuite…
> - enfin…

## D'autres apparitions

D'abord un paragraphe…

. . .

Puis un autre

*(ça ne marche pas avec pandoc 1.9.4.2, mais ça marche avec 1.12.2.1, vérifiez
votre version)*

## Mise en forme

| Il y a 2 types de personnes :
|   ceux qui comprennent la récursivité et
|   ceux qui ne comprennent pas qu'il y a 2 types de personnes :
|     ceux qui comprennent la récursivité et
|     ceux qui ne comprennent pas qu'il y a 2 types de personnes :
|       ceux qui comprennent la récursivité et
|       ceux qui…

# Spécial \LaTeX /Beamer

## Du spécifique

Certaines choses n'existent pas nativement en *Pandoc Markdown*, il suffit donc
d'utiliser du \LaTeX.

## Des blocks spécifiques

\begin{alertblock}{Alerte}
Ceci est une alerte
\end{alertblock}

\begin{exampleblock}{Exemple}
Ceci est un exemple
\end{exampleblock}

## Images

Les images sont supportées par *Markdown*, mais on ne peut pas spécifier la taille. Il est donc pratique d'utiliser directement \LaTeX.

----

## Des maths

Avec des formules :

\center$\displaystyle\frac{\pi}{4}=\int_0^1 \sqrt{1-x^2}\mathrm dx$

# À vous

## Essayez

    sudo apt-get install pandoc \
                         texlive-latex-base \
                         texlive-lang-french \
                         latex-beamer \
                         impressive
    git clone http://git.rom1v.com/mdbeamer.git
    cd mdbeamer
    make run

## Un thème en 2 minutes

Définissez vos 3 couleurs :

\scriptsize

~~~latex
\definecolor{Color1}{HTML}{25567B}
\definecolor{Color2}{HTML}{033E6B}
\definecolor{Color3}{HTML}{66A3D2}
~~~

\normalsize

Changez les logos :

# Voir aussi

## Des liens

\scriptsize

pandoc
  ~ <http://johnmacfarlane.net/pandoc/demo/example9/pandocs-markdown.html>
pour beamer
  ~ <http://johnmacfarlane.net/pandoc/demo/example9/producing-slide-shows-with-pandoc.html>
en français
  ~ <http://enacit1.epfl.ch/markdown-pandoc/>
