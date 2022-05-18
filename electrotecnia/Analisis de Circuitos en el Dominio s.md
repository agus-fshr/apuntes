# Analisis de Circuitos en el Dominio S
## $Z(s)$ e $Y(s)$
### Resistencias
La impedancia resistiva en el dominio del tiempo, asi como en el dominio de la frecuencia es $R$. Es independiente del tiempo, por lo que para la transformada de Laplace es una constante y no cambia. En terminos de admitancia $Y(s)$, resulta $\frac{1}{R}$ y la unidad de la admitancia es el _siemen_ ($S$). $$Z(s) = \frac{V(s)}{I(s)} = R$$
### Inductores
Para un inductor se sabe que $v(t) = L \frac{di}{dt}$. Transformando se obtiene $V(s) = L[sI(s) - i(0^-)]$. En situaciones donde la **energia inicial almacenada en el inductor es nula**, se tiene que $V(s) = sLI(s)$. Entonces, la impedancia de un inductor en el dominio de la frecuencia resulta $$Z(s) = \frac{V(s)}{I(s)} = sL$$
Esto, por ejemplo, en estado senoidal permanente se puede analizar diciendo que $j\omega$ y vemos que $Z(j\omega) = j\omega L$.

Cuando el inductor presenta una carga inicial es util representarlo por su modelo equivalente en frecuencia, que incluye una parte inductiva con carga inicial nula y una fuente de tension que proporcione la corriente adecuada.

![[inductor-en-frecuencia.png]]

En este modelo equivalente la condicion inicial del capacitor esta dada por $i(0^-)$ y debe aparecer una fuente tal que garantice ese valor.


### Capacitores
Tomando la ecuacion del capacitor $i=C\frac{dv}{dt}$ y transformando se obtiene $I(s) = C[sV(s) - v(0^-)]$. Esto podria ser una admitancia en paralelo con una fuente de corriente o una fuente de tension en serie con un capacitor de la impedancia $Z(s) = \frac{1}{sC}$.

![[capacitor-en-frecuencia.png]]

La condicion inicial de un capacitor esta dada por $v(0^-)$, que puede aparecer como una fuente de tension o de corriente, segun el modelo que elija.

![[modelos-equivalentes-frecuencia.png]]


## Analisis Nodal y de Malla en el Dominio S
Esto no tiene mucho secreto. Hay que tener en cuenta la energia inicialmente almacenada en el circuito y plantear los circuitos equivalentes. Se transforma todo, se plantea nodos o mallas. Se junta todo en la variable que se quiere despejar y se antitransforma.