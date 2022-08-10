# Motivacion

Dada la rampa $r(t) = tu(t)$, si la quisieramos derivar vemos que la derivada no esta definida en el punto de $t=0$.

Supongamos un espacio vectorial $\mathcal{V} = \mathcal{K}^n$ y sea $B$ una base ortonormal de dicho espacio con producto interno. Ahora puedo considerar un vector cualquiera $v$ y una funcion que a $v$ le asigna su producto interno $<\omega, v>$. A su vez, le asigna a cualquier vector su producto interno. Formalmente, $$ T_{\omega}(v) = <\omega, v> $$

Esta transformacion lineal $T$ exhibe la propiedad de linealidad. Ahora algo mas interesante.

Al ser $\omega \in \mathcal{V}$ se debe poder escribir como combinacion lineal de miembros de la previamente mencionada base ortonormal de $\mathcal{V}$. Entonces, $<\omega, v_j> = \alpha _j$ donde $\alpha _j$ es el escalar asociado a la base ortonormal y su combinacion lineal. Otra manera de expresar esto es $T_{\omega}(v_j) = \alpha _j$

# Funciones Generalizadas

## Formacion del Concepto

Si tengo una senal $x$, como puedo hacer para fabricar una transformacion lineal que me permita reconstruirla de tal manera que pueda ver su derivada. Vamos a buscar ahora una funcion que nos permita expresar el producto interno y que tenga linealidad: la integral.

$$ T_{x}(\phi) = \int x(t) \phi (t) dt = <x, \phi>$$

Para que la integral siempre converja para cualquier $x$ lo que necesito es que la funcion $\phi$ pertenezca a la clase de funciones que admiten derivadas de todos los ordenes y que se anulan fuera de cierto intervalo. Entonces, ahora digo que $x$ es una funcion continua a trozos. Lo de $\phi$ se nota como $\phi \in \mathcal{C}_0^{\infty}$. Este espacio es el de funciones de prueba infinitamente diferenciables y que se anulan fuera del intervalo         [$- \alpha \phi , \alpha \phi$].

## Definicion Formal

> Una funcion generalizada es una funcoinal lineal (continua) sobre el conjunto de las funciones de prueba $\mathcal{C}_0^{\infty}$

Esta siguiente anotacion es totalmente al margen pero aclaro que $\mathcal{C}_0^{\infty}$ se dice que es un $K$-espacio vectorial porque actua sobre el conjunto $K$.

## Ejemplo

Veamos el caso de $<\mu, \phi>$.
$$ <\mu, \phi> = \int^{\infty}_{\infty} \mu (t) \phi (t) dt = \int_0^{\infty} \phi (t) dt$$

# Funcion Generalizada Regular

Sea $g$ una distribucion (funcion generalizada) si existe $y$ funcion continua a trozos tal que $$ <g, \phi> = <y, \phi>= \int^{\infty}_{\infty} y(t) \phi (t) dt \forall \phi \in \mathcal{C}_0^{\infty}$$ se dice que $g$ es regular

# Propiedades de Funciones Generalizadas
## Igualdad de Funciones Generalizadas

Considero $g$ y $g' \in \mathcal{D}$ ($\mathcal{D}$ es el espacio de funciones generalizadas) Defino que $g = g'$ si $$ <g,\phi> = <g^\prime, \phi> \forall \phi \in \mathcal{C}_0^{\infty} $$.

Si se tienen $x_1$ y $x_2$ funciones continuas a trozos y $\alpha_1$ y $\alpha_2 \in K$. Entonces, $$ <\alpha_1 x_1, \alpha_2 x_2, \phi> =\int^{\infty}_{-\infty} (\alpha_1 x_1(t), \alpha_2 x_2(t))\phi(t) dt $$. Luego, por linealidad resulta que $$ \alpha_1 <x_1, \phi> + \alpha_2 <x_2, \phi> $$

Aca medio que rafa hace lo mismo pero en lugar de $x$ les pone $g$ y ahora esta definido el producto por un escalar y la linealidad para las funciones generalizadas. Esto porque $(\mathcal{D}, +, ., K)$ resulta un espacio vectorial.

## Funcion Generalizada Singular
Un ejemplo tipico es el de la delta de dirac. $<\delta, \phi> = \phi (0)$

## Producto de una Funcion Generalizada por una Funcion de prueba

$\Phi \in \mathcal{C}^{\infty}_0$ y $x$ funcion continua a trozos. Luego $$ <\gamma x,\Phi> = \int^{\infty}_{-\infty}\gamma(t) x(t) \phi(t) dt = \int^{\infty}_{-\infty} x(t) \gamma(t) \phi(t) dt  $$ Esto se puede hacer porque tanto $\phi$ como $\gamma \in \mathcal{C}^{\infty}_0$

De nuevo, aca se copia lo mismo pero dandolo como definicion. No lo hago porque no me da la velocidad.

**Un ejemplo:** $$ <\sin (t) \delta, \phi> = <\delta, \sin(t) \phi> =\sin(t) \phi(t) |_{t=0} = 0 = <0, \phi> $$ Esta es la funcion generalizada nula. El coseno resulta ser la funcion generalizada identica. No lo voy a demostrar porque es identico a lo de recien pero viene por el lado de que $\cos(0)=1$

# Derivada Generalizada

Ahora considero $x$ continua y $x^\prime$ continua a trozos. $$<x^\prime, \phi> = \int_{-\infty}^{\infty} x^\prime(t)\phi(t) dt $$. Ahora tengo el gustazo de integrar por partes.
$$ x(t)\phi(t) | ^{\infty}_{-\infty} = \lim_{a \to \infty} x(a)\phi(a) - \lim_{b \to -\infty} x(b)\phi(b) $$.

Sea $g \in \mathcal{D}$ defino su derivada generalizada $g^\prime$ como $$ <g^\prime, \phi> = - <g, \phi^\prime> \forall \phi \in \mathcal{C}^{\infty}_0 $$ 

### Derivada de la Rampa Unitaria

De esta manera, vamos a buscar la derivada generalizada de la rampa unitaria.
$$ <r^\prime, \phi> = -<r, \phi^\prime> = \int^{\infty}_{\infty} r(t) \phi^\prime(t) dt$$
$$ \int^{\infty}_{0} t\phi^\prime(t) dt = -(t\phi(t)|^{\infty}_0 - \int^{\infty}_0 \phi dt) = \int_0^{\infty} \phi(t) dt =\int_{-\infty}^{\infty}u(t)\phi(t)dt = <u(t), \phi(t)> $$
Ahora podes mirar lo primero y ultimo que escribimos y vas a ver que $r^\prime = u$. Despues Rafa calculo la derivada de $u(t)$ para mostrar que da $\delta(t)$ pero yo no lo voy a hacer.

### Derivada $n$-esima
Lo que si me voy a dignar a hacer es mostar la propiedad de la derivada $n$-esima.
$$ <g^{(n)}, \phi> = (-1)^n <g, \phi^{}(n)> $$

# La Delta de Dirac
Quizas no sea el lugar correcto para decir esto pero aclaro. La nocion de que
*la delta de Dirac es una funcion que vale cero en todos lados salvo en uno donde es infinito y que si la integras da cero*
es erronea. Asi seria si la delta fuera una funcion, pero no lo es. *Es una imagen pictorica* segun Rafa, aunque el senor piensa que se lo que me esta diciendo. Despues de decir esto se hacen un par de aclaraciones y definiciones sobre por que la delta funciona como lo hace pero no lo copie. En todo caso, Marcos lo copio textual.
Lo que si voy a tirar aca es que
$$<\delta(t-t_0), \phi> = \phi(to)$$
$$ \delta(at) = \frac{1}{|a|} \delta(t) $$
$$ \delta^{(n)}(at) = \frac{1}{|a|} (\frac{1}{a})^n \delta^{(n)}(t) $$
$$ \delta^\prime(-t) = -\delta^\prime(t) $$
Aca Rafa desarrolla un par de ejemplos que estan en la presentacion pero para esto es mejor confiar y ver que dice Nelly, asi que tampoco lo anoto.
