---
title: Fonctions et équations du 2^nd^ degré
subtitle: 1^ère^ Spécialité Math
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
  \usepackage{multicol}
  \newcommand{\hideFromPandoc}[1]{#1}
  \hideFromPandoc{
    \let\Begin\begin
    \let\End\end
  }
---


\begin{tikzpicture}
   \tkzTabInit{$x$ / .75 , $f$ / 1}{$0$, $+\infty$}
   \tkzTabLine{z, +, }
\end{tikzpicture}

\begin{tikzpicture}
   \tkzTabInit{$x$ / .75 , $f$ / 1.5}{$0$, $+\infty$}
   \tkzTabVar{-/ $0$,+/ $+\infty$}
\end{tikzpicture}


\newpage

---

H1
==============

H2 - A
--------------

\Begin{multicols}{2}

### H3 - a
Blah blah blah...

### H3 - b
Blah blah blah...

### H3 - c
Blah blah blah...

### H3 - a
Blah blah blah...

### H3 - b
Blah blah blah...

### H3 - c
Blah blah blah...

### H3 - a
Blah blah blah...

### H3 - b
Blah blah blah...

### H3 - c
Blah blah blah...

\End{multicols}

H2 - B
--------------
Blah blah blah...