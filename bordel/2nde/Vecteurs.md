---
title : Vecteurs
author : TODARO Cédric
date : \today
abstract : Petit esssai avec des vecteurs
lang: fr-FR
aspectratio : 54
navigation : horizontal
section-titles : false
theme : Boadilla
header-includes: |
  \usepackage[utf8]{inputenc}
  \usepackage[T1]{fontenc}
  \usepackage{pgf,tikz,pgfplots}
  \pgfplotsset{compat=1.15}
  \usepackage{mathrsfs}
  \usetikzlibrary{arrows}
  \usepackage{graphics}
  \usepackage{siunitx}
  \usepackage[c]{esvect}
  \newcommand\norm[1]{\left\lVert#1\right\rVert}
  \pagestyle{empty}
---

# Section 1

# Essai 1111

\centering
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=.5cm,y=.5cm]
\begin{axis}[x=.5cm,y=.5cm,axis lines=middle,ymajorgrids=true,xmajorgrids=true,xmin=-4,xmax=4,ymin=-5,ymax=4,]
\clip(-10,-5) rectangle (11,4);
\draw [->,line width=2.pt] (-3,0) -- (0,2);
\end{axis}
\end{tikzpicture}

# Une autre diapo

Pour voir é et avec les accents è É et autre èà ä etxc

# Avec des maths

$x^2-4x+3=0\Leftrightarrow\Delta=b^2-4ac=...$

---

Ou sans titre

---

## Des apparitions

Par étapes :

> - d'abord…
> - ensuite…
> - enfin…

---

Ou avec une image

![image](https://image.shutterstock.com/image-photo/white-transparent-leaf-on-mirror-260nw-1029171697.jpg)

---

Alors le markDown ça pete ...

... ou pas

* Bien ... oui oui *oui*
* Vraiment __bien__
  * Surper _bien_

# tableau

|   t1   | sdqsd |       T2 |  | plop |
|:------:|-------|---------:|--|:-----|
| patate | prune |    autre |  |      |
|  Chou  | navet | carottes |  |      |

On verra

---

Lien 

![plop](https://steemitimages.com/DQmXsUhr1QvYsmUWjN3oDgfoMGp3zJzE8Wahq4s1PgdcUMg/shark.png)

![image](https://image.shutterstock.com/image-photo/white-transparent-leaf-on-mirror-260nw-1029171697.jpg)

---

Et maintenant en Beamer

# Fin

# Fin merci

Youhhhhhhhhhhh

[![](https://media.tenor.com/images/fe6714436a6f3ec36bfe4b4a99f5dee5/tenor.gif)](https://media.tenor.com/images/fe6714436a6f3ec36bfe4b4a99f5dee5/tenor.gif)

# Level 1

## Level 2

plopplpop

## LEvel 2

-> etcetcetc <-

---

Prout

---

::: incremental

- Eat spaghetti
- Drink wine

:::

or

::: nonincremental

- Eat spaghetti
- Drink wine

:::

---

:::::::::::::: {.columns}
::: {.column width="40%"}
![](https://media.tenor.com/images/fe6714436a6f3ec36bfe4b4a99f5dee5/tenor.gif)
:::
::: {.column width="60%"}

Un texte assez long pour voir 

## Avec des blocs

> - plop *sqdqsdqsdqsdqs*
>   - plop plop

:::
::::::::::::::

