LOI DE BERNOULLI (Partie 2)

***- sauf STD2A -***

I. [Simulation]{.underline}

On lance un dé à 6 faces n fois de suite et on observe le nombre de fois
que le dé s'arrête sur la face « 1 ».

On considère donc comme « succès » le fait d'obtenir un 1.

Cette expérience suit une loi de Bernoulli de paramètre *p* =
$\frac{1}{6}$.

On va simuler l'expérience à l'aide d'un programme qui renvoie une liste
composée d'un échantillon de n lancers de dé :

![Description : Capture d'écran 2019-06-06 à
22](media/image1.png){width="2.4541666666666666in"
height="1.9152777777777779in"}

On exécute le programme avec n = 10 :

![Description : Capture d'écran 2019-06-06 à
22](media/image2.png){width="3.4229166666666666in"
height="0.7541666666666667in"}

On modifie ensuite le programme afin qu'il renvoie en sortie la
fréquence de « 1 » obtenu pour un échantillon de taille n.

![Description : Capture d'écran 2019-06-06 à
22](media/image3.png){width="2.6694444444444443in" height="2.3in"}

On exécute le programme avec des valeurs successives de n de plus en
plus grandes.

![Description : Capture d'écran 2019-06-06 à
22](media/image4.png){width="2.754166666666667in"
height="2.307638888888889in"}

Les fréquences simulées semblent de rapprocher de la valeur théorique
$\frac{1}{6}$.

On améliore encore le programme pour simuler N échantillons de taille n
et afficher en sortie les fréquences obtenues :

![Description : Capture d'écran 2019-06-06 à
22](media/image5.png){width="3.2694444444444444in"
height="3.222916666666667in"}

On exécute le programme pour 10 échantillons de taille 50 :

![Description : Capture d'écran 2019-06-06 à
22](media/image6.png){width="5.7in" height="0.7076388888888889in"}

II\. [Fluctuation d'échantillonnage]{.underline}

La simulation précédente nous montre que si l'on réalise plusieurs
échantillons de même taille, la fréquence observée de succès fluctue.

C'est ce qu'on appelle la fluctuation d'échantillonnage.

Plus la taille de l'échantillon est grande, plus les fréquences se
rapprochent de la probabilité théorique.

![Description : Capture d'écran 2019-06-06 à
22](media/image7.png){width="6.684722222222222in"
height="0.6305555555555555in"}

On constate alors que le phénomène de fluctuation diminue.

Le nuage de points ci-dessous représente la simulation de 400
échantillons de taille 50.

On peut lire que les fréquences fluctuent entre 0,08 et 0,30.

![Description : Capture d'écran 2019-06-06 à
22](media/image8.png){width="3.792361111111111in"
height="2.122916666666667in"}

III\. [Dispersion des résultats]{.underline}

p est la proportion théorique dans un échantillon de taille $n$.

s est l'écart-type de la série des fréquences obtenues. On pourra
prendre s $\approx$ $\frac{1}{2\sqrt{n}}$

En moyenne,

\- 68% des fréquences appartiennent à l'intervalle \[p -- s ; p + s\].

\- 95% des fréquences appartiennent à l'intervalle \[p -- 2s ; p + 2s\].

![](media/image9.png){width="3.6555555555555554in"
height="2.011111111111111in"}- 99% des fréquences appartiennent à
l'intervalle \[p -- 3s ; p + 3s\].

![](media/image10.png){width="3.71875in" height="2.0493055555555557in"}

![](media/image11.png){width="3.470833333333333in"
height="1.9131944444444444in"}

![](media/image12.png){width="5.209722222222222in"
height="1.0298611111111111in"}
