# Frecuencia Compleja y Transformada de Laplace
## Frecuencia Compleja
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
Un par de frecuencias complejas conjugadas se asocian con una senoide o con una senoide amortiguada por una exponencial. Es util recordar que $Re(z) = \frac{1}{2}(z+z^*)$.
La parte real de la funcion forzada compleja produce la parte real de la respuesta y lo analogo vale para la parte imaginaria.

La manera en que se trabaja esto con circuitos es planteado las ecuaciones integrodiferenciales para el circuito, luego llamando a cada $V = Re(V_me^{st})$. Despues, hay que sacar factor comun para deshacernos de los factores comunes de $e^st$ y los $Re()$. Una vez hecho eso se despeja la magnitud que se busca resolver y se la escribe de nuevo en el dominio del tiempo.


## Transformada de Laplace
Existe una manera que permite desarrollas cualquier funcion como una suma de formas de onda exponenciales, cada una con su propia frecuencia compleja. Este metodo se conoce como la transformada de Laplace y se define como $$F(s) = \int^{\infty}_{-\infty}e^{-st}dt$$
Esta transformada convierte las funciones del dominio del tiempo al dominio de la frecuencia. Para demostrar su validez hay que trabajar con la transformada de Fourier. Asimismo, se define la transformada inversa de Laplace como $$f(t) = \frac{1}{2\pi j}\int^{\sigma_0+j\infty}_{\sigma_0-j\infty}e^{st}F(s)ds$$
La constante real $\sigma_0$ se incluye en los limites de integracion para garantizar la convergencia de la integral impropia. Por suerte, esta ultima integral se puede evitar con el uso de tecnicas que se explicaran mas adelante.

### Condiciones para realizar la transformada de Laplace
Por lo general, se trabajara con funciones que cumplan las siguientes condiciones
- La funcion $v(t)$ es integrable en todo intervalo finito $t_1 < t < t_2$ donde $0 \leq t_1 < t_2 < \infty$.
- $\lim_{t \to \infty} e^{\sigma_0t} |v(t)|$ existe para algun valor de $\sigma_0$.

A continuacion una serie de transformadas comunes.
$$u(t) \Leftrightarrow \frac{1}{s}$$
$$\delta (t) \Leftrightarrow 1$$
$$e^{-\alpha t} \Leftrightarrow \frac{1}{s-\alpha}$$
$$tu(t) \Leftrightarrow \frac{1}{s^2}$$
$$\sin(\omega t u(t)) \Leftrightarrow \frac{\omega}{s^2+\omega^2}$$
$$\cos(\omega t u(t)) \Leftrightarrow \frac{s}{s^2 + \omega^2}$$
Cuando se tenga un cociente de polinomios a antitransformar, mientras el grado del denominador sea superior al del numerador, conviene hacer fracciones simples y antitransformar cada termino del polinomio resultante.


### Datos piolas de Laplace
Cuando todas las condiciones iniciales son cero, diferenciar con respecto al tiempo se vuelve simplemente multiplicar por $s$ en el dominio de la frecuencia.

De manera analoga, la integracion en el dominio del tiempo se corresponde con la division por $s$ en el dominio de la frecuencia.

El desplazamiento en el tiempo se aplica de la siguiente manera $$f(t-a)u(t-a) \Leftrightarrow e^{-as}F(s) \hspace{3cm} (a \geq 0)$$
## La prueba de Routh
Sea la funcion de un sistema en el dominio $s$ $$H(s) = \frac{N(s)}{D(s)}$$
El polinomi del denominador puede escribirse somo $a_ns^n + a_{n-1}s^{n-1} + ...$ Si los coeficientes $a_n$ son positivos y diferentes de cero, el procedimiento de Routh ordena los coeficientes como $$a_n \hspace{1cm} a_{n-2} \hspace{1cm} a_{n-4} \hspace{1cm} ...$$ $$a_{n-1} \hspace{1cm} a_{n-3} \hspace{1cm} a_{n-5} \hspace{1cm} ...$$
Luego, se genera una tercera fila $$\frac{a_{n-1}a_{n-2} - a_na_{n-3}}{a_{n-1}} \hspace{1cm} \frac{a_{n-1}a_{n-4} - a_na_{n-5}}{a_{n-1}}$$
Despues de esto, se genera una cuarta fila, multiplicando de la misma manera la segunda y tercera filas. Esto se repite hasta tener $n+1$ filas. El numero de cambios de signo que hay en la primera columna indica la cantidad de polos que tiene la componente real positiva. Cualquier cambio de signos indica que el sistema es inestable.

## Teorema del Valor Inicial
El valor inicial de la funcion de tiempo $f(t)$ se obtiene multiplicando primero su transformada de Laplace $F(s)$ por $s$ y luego dejando que $s$ tienda a infinito. El valor inicial de $f(t)$ que se obtiene es el limite por la derecha.

Esto sirve pare verificar los resultados de una transformacion o de una transformacion inversa.


## Teorema del Valor Final
No es tan util como el de valor inicial porque solamente se puede usar con algunas transformadas. Este teorema solamente vale para las $F(s)$ con polos con parte real negativa o en el origen. $$\lim_{t \to \infty}f(t) = \lim_{s \to 0}[sF(s)]$$
La condicion mencionada previamente para este teorema es tal que garantiza la existencia de $f(\infty)$. El producto $sF(s)$ tiene todos sus polos dentro del semiplano izquierdo.