# Frecuencia Compleja y Transformada de Laplace
## 14.1 - Frecuencia Compleja
Comenzamos por considerar una tension dada por una senoidal amortiguada exponencialmente (para esto se supone $\sigma < 0$ aunque podria no ser el caso). $$v(t) = V_me^{\sigma t}\cos{(\omega t + \theta)}$$
A partir de esta ecuacion se pueden dar varias situaciones. Una es la de $\sigma = 0$. Entonces se obtendria una tension senoidal comun $V_m\cos{(\omega t + \theta)}$. Otro caso posible es que $\omega = 0$. En este tendria una tension exponencial dada por $V_m\cos{(\theta)e^{\sigma t}} = v_0e^{\sigma t}$. Finalmente, podria darse el caso de que tanto $\sigma$ como $\omega$ se anulen. En ese caso tendria nada mas que una tension consatnte $V_m\cos{(\theta)} = V_0$.

De estos ejemplos se puede ver que de solo considerar una senoide amortiguada exponencialmente se pueden cubrir muchos casos distintos. Entonces, podria resultar conveniente considerar mas tensiones como exponenciales, sobre todo, con exponente complejo.$$v(t) = V_0e^{j \omega t}$$
Lo unico que vamos a decir sobre $\sigma$ hasta este punto es que es la parte real de la frecuencia compleja. Esto es distinto de la frecuencia real. Tambien se llama a $\sigma$ con el nombre de _frecuencia neperiana_.

Una funcoin expoencial de frecuencia compleja seguira la siguiente forma general $$f(t) = Ke^{st}$$ donde $s$ es la frecuencia compleja $\sigma + i\omega$.

Esta ultima expresion permite describir distintos tipos de fuentes. Por ejemplo una fuente de corriente directa, el caso de una tension dada por una exponencial e, incluso, pasando por las definiciones complejas de las funciones, tensiones dadas por funciones trigonometricas.$$cos(\omega t + \theta) \Rightarrow K_{1,2}e^{\pm j(\omega t + \theta)} = \frac{1}{2}V_me^{\pm j(\omega t + \theta)}$$
### El caso senoidal amortiguado exponencialmente
Aca lo unico que hay que hacer es aplicar la identidad de Euler para llegar a una expresion util. Por ejemplo, en el libro se muestra que $v(t) = V_me^{\sigma t}\cos{(\omega t + \theta)}$ queda como $$v(t)=\frac{1}{2}V_me^{j\theta}e^{j(\sigma + j\omega t)} + \frac{1}{2}V_me^{-j\theta}e^{j(\sigma - j\omega)t}$$
Vemos en esa expresion que se pueden juntar los exponentes de las $e$ y resulta que se forma $s_1=s_2^*$.

### La relacion de S con la realidad
Si me dan un valor de $K = a+bi$ y un valor de $s=x+yi$ puedo decir que tendria la forma de $$2|K|e^{Re(s)}\cos{(Im(s)t + \text{ang}(a+bi))}$$
Para que sean cantidadres reales, cada frecuencia compleja debe ir con su conjugada.

La parte real de $s$ se asocia con la variacion exponencial. Si es negativa, la funcion disminuye a medida que $t$ aumenta. Si es positiva, la funcion crece. Finalmente, si es cero  eso significa que la amplitud senoidal es constante.

La parte imaginaria de $s$ describe la variacion senoidal y corresponde de manera especifica a la frecuencia en radianes. Lo importante es que a mayor $|s|$, con mayor rapidez cambia la funcion.

A partir de ahora hay que tener en cuenta que $s$ es la frecuencia compleja, $\sigma$ es la frecuencia neperiana, que $\omega$ es la frecuencia radian y, finalmente, que $f=\frac{\omega}{2\pi}$ es la frecuencia ciclica.

La unidad de la frecuencia neperiana es nepers por segundo.
La frecuenia radian se mide en radianes por segundo.
La frecuencia compleja se mide en unidades que se denominan nepers complejos por segundo o radianes compejos por segundo. 


## Funcion Forzada Senoidal Amortiguada
