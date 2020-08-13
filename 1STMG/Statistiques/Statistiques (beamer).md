---
title: Statistiques
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

# Rappels : Proportion et pourcentage

## Proportion d'une sous-population

---

### Exemple

Sur les $480$ élèves inscrits en classe de 1^ère^, $108$ d'entre eux ont choisi la filière STMG.

. . .

\begin{center}
\tikzset{every picture/.style={line width=0.75pt}}
\begin{tikzpicture}[x=0.6pt,y=0.6pt,xscale=.5,yscale=.5]
\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (100,66) .. controls (100,40.59) and (120.59,20) .. (146,20) -- (404,20) .. controls (429.41,20) and (450,40.59) .. (450,66) -- (450,204) .. controls (450,229.41) and (429.41,250) .. (404,250) -- (146,250) .. controls (120.59,250) and (100,229.41) .. (100,204) -- cycle ;
\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (130,124) .. controls (130,110.75) and (140.75,100) .. (154,100) -- (296,100) .. controls (309.25,100) and (320,110.75) .. (320,124) -- (320,196) .. controls (320,209.25) and (309.25,220) .. (296,220) -- (154,220) .. controls (140.75,220) and (130,209.25) .. (130,196) -- cycle ;
\draw (225,130) node [align=left] {\begin{minipage}[lt]{102pt}\setlength\topsep{0pt}\begin{center}{\scriptsize STMG = 108}\end{center}\end{minipage}};
\draw (275, 50) node [align=left] {\begin{minipage}[lt]{129pt}\setlength\topsep{0pt}\begin{center}{\scriptsize Premières = 480}\end{center}\end{minipage}};
\end{tikzpicture}
\end{center}

. . .

La **population totale** des élèves de 1^ère^, notée $N$, est égale à $480$. C'est la population de référence.

. . .

La **sous-population** des élèves de STMG, notée $n$, est égale à $108$.

. . .

La **proportion** d'élèves de STMG parmi tous les élèves de première, notée $p$, est : $$p=\dfrac{n}{N}=\dfrac{108}{480}=\dfrac{9}{40}=0,225$$

. . .

Cette proportion peut s'exprimer en pourcentage : $p=22,5\%$

---

## Pourcentage d'un nombre

. . .

### Exemple {-}

Parmi les $480$ élèves de 1^ère^, $15\%$ ont choisi l'option "Arts plastiques".

$15\%$ de $480$ ont choisi l'option "Arts plastiques", soit :

. . .

$15\%\times 480=\dfrac{15}{100} \times 480=72$ élèves.

---

## Méthode : Associer proportion et pourcentage

Une société de $75$ employés compte $12\%$ de cadres et le reste d'ouvriers.

$35$ employés de cette société sont des femmes et $5$ d'entre elles sont cadres.

. . .

> a) Calculer l'effectif des cadres.
> b) Calculer la proportion de femmes dans cette société.
> c) Calculer la proportion, en $\%$, de cadres parmi les femmes. Les femmes cadres sont-elles sous ou surreprésentées dans cette société ?

---

(a) $12\%$ de $75=\dfrac{12}{100}\times 75=9$.

Cette société compte 9 cadres.

. . .

(b) $n=35$ femmes et $N=75$ employés

La proportion de femmes est donc égale à $p=\dfrac{35}{75}=\dfrac{7}{15}\approx 0,47=47\%$.

. . .

(c) $n=5$ femmes cadres et $N=35$ femmes. La population de référence n'est plus la même.

La proportion de cadres parmi les femmes est égale à $p=\dfrac{5}{35}=\dfrac{1}{7}\approx 0,14=14\%$.

. . .

Or $14\% > 12\%$ donc les femmes cadres sont surreprésentées dans cette société.

---

## Proportion d'une proportion

### Exemple {-}

Dans un car, il y a $40\%$ de scolaires. Et **parmi les scolaires**, $60\%$ sont des filles.

. . .

\begin{center}
\tikzset{every picture/.style={line width=0.75pt}}
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.75,xscale=0.75]
\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (100,106) .. controls (100,91.64) and (111.64,80) .. (126,80) -- (274,80) .. controls (288.36,80) and (300,91.64) .. (300,106) -- (300,184) .. controls (300,198.36) and (288.36,210) .. (274,210) -- (126,210) .. controls (111.64,210) and (100,198.36) .. (100,184) -- cycle ;
\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (150,128) .. controls (150,118.06) and (158.06,110) .. (168,110) -- (272,110) .. controls (281.94,110) and (290,118.06) .. (290,128) -- (290,182) .. controls (290,191.94) and (281.94,200) .. (272,200) -- (168,200) .. controls (158.06,200) and (150,191.94) .. (150,182) -- cycle ;
\draw  [fill={rgb, 255:red, 255; green, 193; blue, 247 }  ,fill opacity=1 ] (190,142) .. controls (190,135.37) and (195.37,130) .. (202,130) -- (268,130) .. controls (274.63,130) and (280,135.37) .. (280,142) -- (280,178) .. controls (280,184.63) and (274.63,190) .. (268,190) -- (202,190) .. controls (195.37,190) and (190,184.63) .. (190,178) -- cycle ;
\draw (125,195) node [align=left] {\begin{minipage}[lt]{34pt}\setlength\topsep{0pt}\begin{center}CAR\end{center}\end{minipage}};
\draw (170,120) node [align=left] {\begin{minipage}[lt]{27.2pt}\setlength\topsep{0pt}\begin{center}S\end{center}\end{minipage}};
\draw (210,140) node [align=left] {\begin{minipage}[lt]{27.2pt}\setlength\topsep{0pt}\begin{center}F\end{center}\end{minipage}};
\draw (100,60) node [align=left] {\begin{minipage}[lt]{68pt}\setlength\topsep{0pt}\begin{center}40\% de CAR\end{center}\end{minipage}};
\draw (250,60) node [align=left] {\begin{minipage}[lt]{54.4pt}\setlength\topsep{0pt}\begin{center}60\% de S\end{center}\end{minipage}};
\draw (138,72) -- (160.34,105.5);
\draw [shift={(162,108)}, rotate = 236.31] [fill={rgb,255:red,0;green,0;blue,0}][line width=0.08] [draw opacity=0] (8.93,-4.29) -- (0,0) -- (8.93,4.29) -- cycle;
\draw (227,72) -- (213.73,125.09);
\draw [shift={(213,128)}, rotate = 284.04] [fill={rgb,255:red,0;green,0;blue,0}][line width=0.08] [draw opacity=0] (8.93,-4.29) -- (0,0) -- (8.93,4.29) -- cycle;
\end{tikzpicture}
\end{center}

. . .

L'ensemble $F$ des filles est inclus dans l'ensemble $S$ des scolaires et on a : 

$$p_{F}=60\%\text{ de }S$$

. . .

L'ensemble $S$, des scolaires, est inclus dans l'ensemble $\text{CAR}$, de toutes les personnes dans le car, et on a : 

$$p_{S}=40\%\text{ de CAR}$$

---

\begin{center}
\tikzset{every picture/.style={line width=0.75pt}}
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (100,106) .. controls (100,91.64) and (111.64,80) .. (126,80) -- (274,80) .. controls (288.36,80) and (300,91.64) .. (300,106) -- (300,184) .. controls (300,198.36) and (288.36,210) .. (274,210) -- (126,210) .. controls (111.64,210) and (100,198.36) .. (100,184) -- cycle ;
\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (150,128) .. controls (150,118.06) and (158.06,110) .. (168,110) -- (272,110) .. controls (281.94,110) and (290,118.06) .. (290,128) -- (290,182) .. controls (290,191.94) and (281.94,200) .. (272,200) -- (168,200) .. controls (158.06,200) and (150,191.94) .. (150,182) -- cycle ;
\draw  [fill={rgb, 255:red, 255; green, 193; blue, 247 }  ,fill opacity=1 ] (190,142) .. controls (190,135.37) and (195.37,130) .. (202,130) -- (268,130) .. controls (274.63,130) and (280,135.37) .. (280,142) -- (280,178) .. controls (280,184.63) and (274.63,190) .. (268,190) -- (202,190) .. controls (195.37,190) and (190,184.63) .. (190,178) -- cycle ;
\draw (125,195) node [align=left] {\begin{minipage}[lt]{34pt}\setlength\topsep{0pt}\begin{center}CAR\end{center}\end{minipage}};
\draw (170,120) node [align=left] {\begin{minipage}[lt]{27.2pt}\setlength\topsep{0pt}\begin{center}S\end{center}\end{minipage}};
\draw (210,140) node [align=left] {\begin{minipage}[lt]{27.2pt}\setlength\topsep{0pt}\begin{center}F\end{center}\end{minipage}};
\draw (100,60) node [align=left] {\begin{minipage}[lt]{68pt}\setlength\topsep{0pt}\begin{center}40\% de CAR\end{center}\end{minipage}};
\draw (250,60) node [align=left] {\begin{minipage}[lt]{54.4pt}\setlength\topsep{0pt}\begin{center}60\% de S\end{center}\end{minipage}};
\draw (138,72) -- (160.34,105.5);
\draw [shift={(162,108)}, rotate = 236.31] [fill={rgb,255:red,0;green,0;blue,0}][line width=0.08] [draw opacity=0] (8.93,-4.29) -- (0,0) -- (8.93,4.29) -- cycle;
\draw (227,72) -- (213.73,125.09);
\draw [shift={(213,128)}, rotate = 284.04] [fill={rgb,255:red,0;green,0;blue,0}][line width=0.08] [draw opacity=0] (8.93,-4.29) -- (0,0) -- (8.93,4.29) -- cycle;
\end{tikzpicture}
\end{center}

. . .

La proportion de scolaires filles dans le $\text{CAR}$ est donc égale à : 

$$60\%\text{ de }40\%=60\% \times 40\%=0,6\times 0,4=0,24=24\%$$

---

## Méthode : Calculer une proportion de proportion

Sur $67$ millions d'habitants en France, $66\%$ de la population est en âge de travailler (15-64 ans).

La population active représente $70\%$ de la population en âge de travailler.

. . .

> a) Calculer la proportion de population active par rapport à la population totale.
> b) Combien de français compte la population active ?

---

(a) $F$ est la population française.

$T$ est la population en âge de travailler.

$A$ est la population active.

. . .

La proportion de $A$ parmi $T$ est $70\%$.

La proportion de $T$ parmi $F$ est $66\%$.

. . .

La proportion de $A$ parmi $F$ est donc égale à : $70\%\times 66\%=0,7\times 0,66=0,462=46,2\%$.

$46,2\%$ des français sont actifs.

. . .

(b) $46,2\%$ de $67=0,462\times 67=30,954$. La France compte environ 31 millions d'actifs.

---

# Fréquence conditionnelle, fréquence marginale

---

## Méthode : Calculer une fréq. conditionnelle et une fréq. marginale

Dans une entreprise qui compte $360$ employés, on compte $60\%$ d'hommes et parmi ceux-là, $12,5\%$ sont des cadres.

Par ailleurs, $87,5\%$ des femmes de cette entreprise sont ouvrières ou techniciennes.

. . .

> a) Compléter le tableau.

                          Hommes   Femmes   Total
  ----------------------- -------- -------- -------
  Cadres                                    
  Ouvriers, techniciens                     
  Total                                     360

> b) À l'aide de ce tableau, déterminer la **fréquence marginale** de cadres.
> c) Déterminer la **fréquence conditionnelle** des "ouvriers, techniciens" _parmi les hommes_.

---

(a) On compte $60\%$ d'hommes : $60\%\times 360=216$ hommes et donc $360-216=144$ femmes.

Parmi les hommes, $12,5\%$ sont des cadres : $12,5\%\times 216=27$.

Parmi les femmes, $87,5\%$ sont "ouvrières ou techniciennes" : $87,5\%\times 144=126$

. . .

                              Hommes   Femmes   Total
  ----------------------- --------- --------- ----------
  Cadres                  **27**    18        45
  Ouvriers, techniciens   189       **126**   315
  Total                   **216**   **144**   360


---

(b) La **fréquence marginale** se lit en **marge** du tableau.

. . .

                              Hommes   Femmes   Total
  ----------------------- --------- --------- ----------
  Cadres                  27         18        **45**
  Ouvriers, techniciens   189        126       315
  Total                   216        144       **360**

. . .

On compte **360** employés en tout et **45** sont des cadres.

La **fréquence marginale** de cadres est donc égale à : $\dfrac{45}{360}=0,125=12,5\%$.

---

(c) La **fréquence conditionnelle** restreint l'effectif total. Ici, on ne considère que les hommes car la _condition_ est **"parmi les hommes"**.

. . .

La **fréquence conditionnelle** se lit sur _une ligne_ ou _une colonne_ intérieure du tableau.

Ici, on ne va donc considérer que la colonne concernant les hommes.

. . .

                          Hommes    Femmes   Total
  ----------------------- --------- -------- ---------
  Cadres                  27        18       45
  Ouvriers, techniciens   **189**   126      315
  Total                   **216**   144      360

. . .

On compte $216$ hommes en tout et parmi eux, $189$ sont des ouvriers, techniciens.

La **fréquence conditionnelle** "d'ouvriers, techniciens" _parmi les hommes_ est donc de : $$\dfrac{189}{216}=0,875=87,5\%$$