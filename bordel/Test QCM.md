---
documentclass : article
geometry : margin=2cm
output : pdf_document
header-includes: |
  \usepackage{pgf,tikz,pgfplots}
  \pgfplotsset{compat=1.15}
  \usepackage{mathrsfs}
  \usetikzlibrary{arrows}
  \pagestyle{empty}
---

\twocolumn[
Blah Blabh
qfkdjqdsmlkfjqmf
qdfkjqmsdflqjmdfq
sd d fqsdf qsdf qsdf qsdf qsdf q sf qsdsq fqsdf qsdf qsdfd fqsdf sqdfqsdf sqdfqsdf qsdf qsdf qsdf qsdfdff qsdf qsdf qsdf qdsf qdsf sqd qsdfqsdfqjksdlkqsdfjmqsdkf
]


1. Qui est le plus fort ?
  - [ ] Ragnaros
  - [ ] Banana

2. plop ?
  - [ ] pate
  - [ ] riz
  - [ ] carotte ... bon


\definecolor{qqffqq}{rgb}{0.,1.,0.}
\definecolor{qqqqff}{rgb}{0.,0.,1.}
\definecolor{ffqqqq}{rgb}{1.,0.,0.}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.8cm,y=0.8cm]
\begin{axis}[
x=0.8cm,y=0.8cm,
axis lines=middle,
ymajorgrids=true,
xmajorgrids=true,
xmin=-5.0,
xmax=5.0,
ymin=-4.0,
ymax=4.0,
xtick={-5.0,-4.0,...,5.0},
ytick={-4.0,-3.0,...,4.0},]
\clip(-5.,-4.) rectangle (5.,4.);
\draw [line width=2.pt,color=ffqqqq,domain=-5.:5.] plot(\x,{(--1.--0.3333333333333333*\x)/1.});
\draw [line width=2.pt,color=qqqqff,domain=-5.:5.] plot(\x,{(--7.-2.*\x)/3.});
\draw [line width=2.pt,color=qqffqq,domain=-5.:5.] plot(\x,{(--3.-6.*\x)/3.});
\begin{scriptsize}
\draw [fill=black] (0.,1.) circle (1.5pt);
\draw [fill=black] (3.,2.) circle (1.5pt);
\draw [fill=black] (-1.,3.) circle (1.5pt);
\draw [fill=black] (2.,1.) circle (1.5pt);
\draw [fill=black] (2.,-3.) circle (1.5pt);
\end{scriptsize}
\end{axis}
\end{tikzpicture}

3. Patate ?
  - [ ] Oui
  - [ ] Peut-etre
  - [ ] Non

4. Encore des question
  - [ ] plaopzae
  - [ ] palaezraz

1. Qui est le plus fort ?
  - [ ] Ragnaros
  - [ ] Banana

2. plop ?
  - [ ] pate
  - [ ] riz
  - [ ] carotte ... bon

3. Patate ?
  - [ ] Oui
  - [ ] Peut-etre
  - [ ] Non

4. Encore des question
  - [ ] plaopzae
  - [ ] palaezraz

1. Qui est le plus fort ?
  - [ ] Ragnaros
  - [ ] Banana

2. plop ?
  - [ ] pate
  - [ ] riz
  - [ ] carotte ... bon

3. Patate ?
  - [ ] Oui
  - [ ] Peut-etre
  - [ ] Non

4. Encore des question
  - [ ] plaopzae
  - [ ] palaezraz

1. Qui est le plus fort ?
  - [ ] Ragnaros
  - [ ] Banana

2. plop ?
  - [ ] pate
  - [ ] riz
  - [ ] carotte ... bon

\onecolumn

1. Qui est le plus fort ?
  - [ ] Ragnaros
  - [ ] Banana

2. plop ?
  - [ ] pate
  - [ ] riz
  - [ ] carotte ... bon

3. Patate ?
  - [ ] Oui
  - [ ] Peut-etre
  - [ ] Non

4. Encore des question
  - [ ] plaopzae
  - [ ] palaezraz

1. Qui est le plus fort ?
  - [ ] Ragnaros
  - [ ] Banana

2. plop ?
  - [ ] pate
  - [ ] riz
  - [ ] carotte ... bon

