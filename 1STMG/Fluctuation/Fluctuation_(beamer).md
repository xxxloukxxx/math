---
title: Échantillonnage / Fluctuation
subtitle: 1^ère^ STMG
lang: fr-FR
aspectratio: 1610
numbersections: true
navigation: empty
standalone: true
theme: Singapore
header-includes: |
  \usepackage{pgf,tikz,tkz-tab,pgfplots}
  \pgfplotsset{compat=1.15}
  \usepackage{mathrsfs}
  \usetikzlibrary{arrows}
---

# Simulation

On lance un dé à $6$ faces $n$ fois de suite et on observe le nombre de fois que le dé s'arrête sur la face "1".

On considère donc comme **"succès"** le fait d'obtenir un **1**.

Cette expérience suit une **loi de Bernoulli** de paramètre $p=\frac{1}{6}$.

---

On va simuler l'expérience à l'aide d'un programme qui renvoie une liste composée d'un échantillon de $n$ lancers de dé :

from random import *

```python
def echantillon(n):
    L=[]
    for i in range(n):
        x=randint(1,6)
        L.append(x)
    return L
```

---

On exécute le programme avec $n = 10$ :

```python
>>> echantillon(10)
[3, 1, 3, 1, 5, 2, 2, 6, 4, 6]
>>> 
```

---

On modifie ensuite le programme afin qu'il renvoie en sortie la fréquence de **"1"** obtenu pour un échantillon de taille $n$.

```python
def echantillon(n):
    c=0
    for i in range(n):
        x=randint(1,6)
        if (x==1):
            c=c+1
    return (c/n)
```

---

On exécute le programme avec des valeurs successives de $n$ de plus en plus grandes.

```python
>>> echantillon(10)
0.0
```

. . .

```python
>>> echantillon(100)
0.17
```

. . .

```python
>>> echantillon(1000)
0.171
```

. . .

```python
>>> echantillon(10000)
0.171
```

. . .

```python
>>> echantillon(100000)
0.16761
```

. . .

Les fréquences simulées semblent de rapprocher de la valeur théorique $\frac{1}{6}$.

---


On améliore encore le programme pour simuler $N$ échantillons de taille $n$ et afficher en sortie les fréquences obtenues :

```python
from random import *

def echantillon(n):
    c=0
    for i in range(n):
        x=randint(1,6)
        if (x==1):
            c=c+1
    return(c/n)
```

. . .

```python
def simulation(N,n):
    L=[]
    for i in range(N):
        f=echantillon(n)
        L.append(f)
    return(L)
```

---

On exécute le programme pour $10$ échantillons de taille $50$ :

```python
>>> simulation(10,50)
[0.18, 0.32, 0.12, 0.04, 0.12, 0.18, 0.16, 0.14, 0.22, 0.22]
```

On vient de calculer la fréquence d'aparition de $1$ sur $50$ lancers, ceci $10$ fois de suite.

# Fluctuation d'échantillonnage

La simulation précédente nous montre que si l'on réalise plusieurs échantillons de même taille, **la fréquence observée** de succès **fluctue**.

. . .

C'est ce qu'on appelle la **fluctuation d'échantillonnage**.

. . .

Plus la taille de l'échantillon est **grande**, plus les **fréquences** se rapprochent de la **probabilité théorique**.

---

Plus la taille de l'échantillon est **grande**, plus les **fréquences** se rapprochent de la **probabilité théorique**.

. . .

```python
>>> simulation(10,50)
[0.16, 0.04, 0.1, 0.22, 0.26, 0.14, 0.26, 0.06, 0.06, 0.2]
```

. . .

```python
>>> simulation(10,500)
[0.164, 0.17, 0.17, 0.16, 0.176, 0.16, 0.182, 0.168, 0.154, 0.162]
```

. . .

```python
>>> simulation(10,5000)
[0.1712, 0.1648, 0.168, 0.1566, 0.16, 0.1682, 0.1602, 0.1574, ...
... 0.1676, 0.166]
```

. . .

```python
>>> simulation(10,50000)
[0.16866, 0.16704, 0.16736, 0.1657, 0.16726, 0.16718, 0.1647, ...
... 0.16526, 0.16508, 0.16738]
```

. . .

On constate alors que le phénomène de **fluctuation** diminue.

---

Le nuage de points ci-dessous représente la simulation de $400$ échantillons de taille $50$.

\begin{center}
\begin{tikzpicture}
\begin{axis}[width=14cm,height=4.5cm,
xtick={0, 50,...,400},ytick={0, 0.08,...,0.4},y tick label style={/pgf/number format/.cd,fixed },xmin=0,xmax=400,ymin=0,ymax=0.38]
\draw[dashed] (0,0.08)--(400,0.08);
\draw[dashed] (0,0.30)--(400,0.30);
\addplot[color=red,mark=*,only marks,mark size=1] table[x=x, y=y] {simul-400-50.txt};
\end{axis}
\end{tikzpicture}
\end{center}

On peut lire que les fréquences fluctuent entre $0,08$ et $0,30$.

# Dispersion des résultats

$p$ est la **proportion théorique** dans un échantillon de taille $n$.

$s$ est **l'écart-type** de la série des fréquences obtenues. On pourra prendre $s\approx\dfrac{1}{2\sqrt{n}}$

. . .

En moyenne,

- 68% des fréquences appartiennent à l'intervalle $\left\lbrack p - s ; p + s \right\rbrack$.
\begin{center}
\begin{tikzpicture}
\begin{axis}[width=14cm,height=4.5cm,
xtick={0, 50,...,400},ytick={0, 1},y tick label style={/pgf/number format/.cd,fixed },xmin=-50,xmax=400,ymin=0,ymax=0.6,
axis lines=middle,]
\fill[blue!5] (0,0.2625) -- (400,0.2625) -- (400,0.4040)--(0,0.4040) -- cycle;
\draw[dashed] (0,0.33333)--(400,0.33333);
\draw (0,0.33333) node[anchor=east] {$p$};
\draw[dashed] (0,0.4040)--(400,0.4040);
\draw (0,0.4040) node[anchor=east] {$p+s$};
\draw[dashed] (0,0.2625)--(400,0.2625);
\draw (0,0.2625) node[anchor=east] {$p-s$};
\addplot[color=red,mark=*,only marks,mark size=1] table[x=x, y=y] {simul-400-50(2).txt};
\draw[color=black] (350,0) node[anchor=south west,fill=blue!5,draw] {$68\%$};
\end{axis}
\end{tikzpicture}
\end{center}

---

- 95% des fréquences appartiennent à l'intervalle $\left\lbrack p - 2s ; p + 2s \right\rbrack$.
\begin{center}
\begin{tikzpicture}
\begin{axis}[width=14cm,height=4.5cm,
xtick={0, 50,...,400},ytick={0, 1},y tick label style={/pgf/number format/.cd,fixed },xmin=-50,xmax=400,ymin=0,ymax=0.6,
axis lines=middle,]
\fill[blue!5] (0,0.1918) -- (400,0.1918) -- (400,0.4747)--(0,0.4747) -- cycle;
\draw[dashed] (0,0.3333)--(400,0.3333);
\draw (0,0.3333) node[anchor=east] {$p$};
\draw[dashed] (0,0.4747)--(400,0.4747);
\draw (0,0.4747) node[anchor=east] {$p+2s$};
\draw[dashed] (0,0.1918)--(400,0.1918);
\draw (0,0.1918) node[anchor=east] {$p-2s$};
\addplot[color=red,mark=*,only marks,mark size=1] table[x=x, y=y] {simul-400-50(2).txt};
\draw[color=black] (350,0) node[anchor=south west,fill=blue!5,draw] {$95\%$};
\end{axis}
\end{tikzpicture}
\end{center}

. . .

- 99% des fréquences appartiennent à l'intervalle $\left\lbrack p - 3s ; p + 3s \right\rbrack$.
\begin{center}
\begin{tikzpicture}
\begin{axis}[width=14cm,height=4.5cm,
xtick={0, 50,...,400},ytick={0, 1},y tick label style={/pgf/number format/.cd,fixed },xmin=-50,xmax=400,ymin=0,ymax=0.6,
axis lines=middle,]
\fill[blue!5] (0,0.1211) -- (400,0.1211) -- (400,0.5454)--(0,0.5454) -- cycle;
\draw[dashed] (0,0.3333)--(400,0.3333);
\draw (0,0.3333) node[anchor=east] {$p$};
\draw[dashed] (0,0.5454)--(400,0.5454);
\draw (0,0.5454) node[anchor=east] {$p+3s$};
\draw[dashed] (0,0.1211)--(400,0.1211);
\draw (0,0.1211) node[anchor=east] {$p-3s$};
\addplot[color=red,mark=*,only marks,mark size=1] table[x=x, y=y] {simul-400-50(2).txt};
\draw[color=black] (350,0) node[anchor=south west,fill=blue!5,draw] {$99\%$};
\end{axis}
\end{tikzpicture}
\end{center}
