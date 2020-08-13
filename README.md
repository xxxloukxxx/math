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
- Les arbres et tableau de variations : http://math.et.info.free.fr/TikZ/index.html 
- Pour les schémas, : [app.diagrams.net](https://app.diagrams.net/) (à voir)
- images dans répertoire media
- faire propre et transférable
- Structuration succente
  - ```# pour les gros titres```
  - ```## def/prop/methode```
  - ```### remarques/autres```
- Utiliser les emulateurs de calculatrices TI ([CEMU](https://github.com/CE-Programming/CEmu)) et [Casio Graph 85](http://www.planet-casio.com/Fr/logiciels/dl_logiciel.php?id=19&file=1) pour les captures d'écrans


## Entête pour le Markdown vers pdf :

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

## Entête pour le Markdown vers Beamer :

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