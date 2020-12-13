# Projet .. faire des Math au lycée

A faire pour chaque chapitre :

- Objectifs de fin de chapitre ```2nd-degre_objectifs-fin-chapitre.md```
- Un cours classique ```2nd-degre.md```
- Un cours en beamer ```2nd-degre_(beamer).md```
- Fiche d'exercices ```2nd-degre_exercices.md```
- Slide de correction ```2nd-degre_correction.md```
  - avec lien vers vidéo de correction
- Un QCM ?
- Une evaluation ?
- Des Flashcards (voir [Anki](https://apps.ankiweb.net/)) ou en md/Beamer ?

Pour cela :

- utiliser un max le markdown
- pandoc pour le pdf : il faut que ```pandoc test.md -o test.pdf``` soit suffissant ... sans ```tartenpion.yaml```
- pandoc pour le beamer : il faut que ```pandoc test.md -o test.pdf -t beamer``` soit suffissant (theme au choix : singapore ou autre)
- Tikz pour les figures ... on peut faire vraiment pleins de choses avec (voir 1STMG/Fluctuation par ex)
- Les arbres et tableau de variations : <http://math.et.info.free.fr/TikZ/index.html>
- Pour les schémas, : [app.diagrams.net](https://app.diagrams.net/) (à voir)
- images dans répertoire media
- faire propre et transférable
- Structuration succente
  - ```# pour les gros titres```
  - ```## def/prop/methode```
  - ```### remarques/autres```
- Utiliser les emulateurs de calculatrices TI ([CEMU](https://github.com/CE-Programming/CEmu)) et [Casio Graph 85](http://www.planet-casio.com/Fr/logiciels/dl_logiciel.php?id=19&file=1) pour les captures d'écrans

## Entête pour le Markdown vers pdf

```
---
title: Fonction dérivée
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
```

## Entête pour le Markdown vers Beamer

```
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
```

## Entête pour le Markdown vers MARP

```
---
marp: true
theme: default
header: 'Généralités sur les fonctions'
footer: '2GT - Lycée Paul Painlevé'
---

# Généralités sur les fonctions

![bg right:40% 90%](img/mug.png)

---

<!-- paginate: true -->

# Définition

Soit $\mathscr{D}_f$ une partie de l'ensemble $\mathbb{R}$.
Une fonction $f$ définie sur $\mathscr{D}_f$, associe à tout nombre $x$ de $\mathscr{D}_f$, un unique nombre, noté $f(x)$.
$\mathscr{D}_f$ est l'ensemble de définition de $f$.

---

## Notation

>$\begin{aligned}
f: \mathscr{D}_f & \mapsto \mathbb{R}\\
               x & \mapsto f(x)
\end{aligned}$

ou

Soit $f$ une fonction définie sur $\mathscr{D}_f$ tel que $f(x) = ...$
```

## Exemple pour une fiche d'exercices

```
---
title: Exercices - Fonction inverse
subtitle: 1^ère^ STMG
lang: fr-FR
documentclass: scrartcl
geometry: "left=1.0cm,right=1.0cm,top=1.5cm,bottom=2.5cm"
standalone: true
output: pdf_document
header-includes:
  - \usepackage{pgf,tikz,tkz-tab,pgfplots}
  - \pgfplotsset{compat=1.15}
  - \usepackage{mathrsfs}
  - \usetikzlibrary{arrows}
  - \usepackage{multicol}
  - \newcommand{\hideFromPandoc}[1]{#1}
  - \hideFromPandoc{
      \let\Begin\begin
      \let\End\end
    }
---

\setlength{\columnsep}{0.5cm}
\setlength{\columnseprule}{0.5pt}
\Begin{multicols}{2}

## Etudier une fonction polynôme $P(x)$ de degré au plus 3

![](ex/19.png){width=45%}

![](ex/20.png){width=45%}

![](ex/22.png){width=45%}

![](ex/23.png){width=45%}
\vfill\null\columnbreak

![](ex/24.png){width=45%}

![](ex/25-1.png){width=45%}
![](ex/25-2.png){width=45%}
\vfill\null\columnbreak

![](ex/47.png){width=45%}

![](ex/50.png){width=45%}

## Etudier une fonction de la forme : $x\mapsto\dfrac{k}{x}$

![](ex/27-1.png){width=45%}
![](ex/27-2.png){width=45%}
\vfill\null\columnbreak

![](ex/28.png){width=45%}

![](ex/29.png){width=45%}

![](ex/30-31.png){width=45%}
\vfill\null\columnbreak

![](ex/51.png){width=45%}

\End{multicols}
```

## Exemple pour les "Objectifs de fin de chapitre"

```
---
title: Fluctuation (p.xxx)
subtitle: 1^ère^ STMG
lang: fr-FR
documentclass: scrartcl
geometry: "left=1.5cm,right=1.5cm,top=1.5cm,bottom=2.5cm"
numbersections: false
standalone: false
output: pdf_document
header-includes:
 - \usepackage{pgf,tikz,tkz-tab,pgfplots}
 - \pgfplotsset{compat=1.15}
 - \usepackage{mathrsfs}
 - \usetikzlibrary{arrows}
---

# Objectifs de fin de chapitre

- [ ] sdq sdqf
  - Exercices : 45 - 46 - 89 - 99 à 127
  - Exercices : 45 - 46 - 89 - 99 à 127
- [ ] qqsd fq
  - Exercices : 45 - 46 - 89 - 99 à 127
- [ ] qfsdqf sdqf
  - Exercices : 45 - 46 - 89 - 99 à 127

![Intervalle de fluctuation](https://images.schoolmouv.fr/maths-1re-cours13-img01.png){width=75%}
```

## Des trucs en math

- 4 [articles](https://kogler.wordpress.com/tag/latex/) qui vont bien

$\begin{aligned}
f: \mathscr{D}_f & \mapsto \mathbb{R}\\
               x & \mapsto f(x)
\end{aligned}$

$\lVert\overrightarrow{u}\rVert= 1$

$$\begin{pmatrix}2\\3\end{pmatrix}$$

$$\boxed{u=1}$$

$\left\lVert \overrightarrow{AH}^2 - 4\overrightarrow{AO}^2 \right\rVert= \left\lVert(\overrightarrow{AH} - 2\overrightarrow{AO})(\overrightarrow{AH} + 2\overrightarrow{AO}) \right\rVert= 0$

$\left\|\dfrac{x}{2}\right\| \text{ et } \left\lVert \dfrac{1}{3}\overrightarrow{AB} \right\rVert^2=\dfrac{1}{3}\times \left(AB\right)^2$

$\left\lVert \sum\limits_{k=1}^n \alpha_k \right\rVert$

$$
\sigma(s,i) = \left\{
    \begin{array}{ll}
        \tau_{si} & \text{si } \{s,i\} \in E \\
        \infty & \text{sinon.}
    \end{array}
\right.
$$

$$
\underbrace{\ln \left( \frac{5}{6} \right)}_{\simeq -0.1823}
< \overbrace{\exp \left(\frac{1}{2} \right)}^{\simeq 1.6487}
$$

En géométrie, un angle droit est un angle exactement de $90^\circ$

$\alpha=30^\circ \Rightarrow$

$$\boxed{\forall p=1,\ldots,n}$$

$\lim\limits_{x \to +\infty} f(x)$

$\sum\limits_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$

$$\oiiint$$

- Des arbres (en tout cas un arbre)

> ```latex
> \begin{tikzpicture}[xscale=1,yscale=1]
> \draw (0,0)--(-2,0.5) node[midway, below, sloped]{0.B4};
> \draw (0,1)--(-2,0.5) node[midway, above, sloped]{0.B3};
> \draw (0,2)--(-2,2.5) node[midway, below, sloped]{0.B2};
> \draw (0,3)--(-2,2.5) node[midway, above, sloped]{0.B1};
> \draw (-2,0.5)--(-4,1.5) node[midway, below, sloped]{0.A2};
> \draw (-2,2.5)--(-4,1.5) node[midway, above, sloped]{0.A1};
> \draw (0,0) node[fill=white]{$\overline{B4}$};
> \draw (0,1) node[fill=white]{$B3$};
> \draw (0,2) node[fill=white]{$\overline{B2}$};
> \draw (0,3) node[fill=white]{$B1$};
> \draw (-2,0.5) node[fill=white]{$\overline{A2}$};
> \draw (-2,2.5) node[fill=white]{$A1$};
> \end{tikzpicture}
> ```

- Tableau de variations : [`tabvar`](http://www.bakoma-tex.com/doc/latex/tkz-tab/tkzdoc-tab.pdf)
