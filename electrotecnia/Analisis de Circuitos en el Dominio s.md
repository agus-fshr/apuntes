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

## Tecnicas Adicionales de Analisis de Circuitos
Si se piensa en los componentes pasivos como impedancias, valen todas las tecnicas de analisis de circuitos usadas con anterioridad. Thevenin, Norton, superposicion, ...

## Polos, ceros y funciones de transferencia
La funcion de transferencia $H(s)$ se define como la proporcion entre la salida y la entrada
$$H(s) = \frac{V_{sal}}{V_{ent}}$$
Una vez que conocemos la funcion de transferencia de un circuito podemos determinar con facilidad la salida que resulta de cualquier entrada. Lo unico que hay que hacer es mutiplicar $H(s)$ por la cantidad de entrada y tomar la transformada inversa de Laplace de la expresion que resulta de dicho producto. Tambien ofrece mucha informacion acerca de la estabilidad de un sistema.

Una practica util es la de indentificar las _frecuencias criticas_, es decir, los ceros del denominador de la funcion de transferencia. Esto ayuda a construir las curvas de respuesta.

## Convolucion
En la practica, puede suceder que nos encontremos circuitos a los que se les pueden conectar fuentes arbitrarias y que requieren una forma eficiente de determinar la nueva salida cada vez. Esto se vuelve facil si podemos caracterizar el circuito basico mediante una funcion de transferencia llamada **funcion del sistema**.

Los pasos a seguir para analizar un circuito de esta manera son...
1. Determinar la funcion de sistema del circuito
2. Obtener la transformada de Laplace y la funcion forzada que se aplicara
3. Mutiplicar la trasformada y la funcion del sistema entre si
4. Obtener la antitransformada del producto a fin de encontrar la respuesta de salida.

### Respuesta al Impulso
La respuesta al impulso es una propiedad descriptiva muy importante de cualquier circuito electrico. Es la respuesta obtenida cuando la funcion forzada que se aplica al mismo es $\delta(t)$. 

En este caso, sabiendo que la transformada de Laplace de $\delta(t)$ es $1$, podemos ver facilmente que $H(s) = Y(s)$, por lo que $h(t) = y(t)$. Mas interesante es analizar que pasa si se realiza un corrimiento en el tiempo sobre esta misma funcion forzada de entrada. Esto solamente resulta en un corrimiento igual en la respuetsa del circuito. Ahora, supongamos que la intensidad del impulso sea numericamente igual al valor de $x(t)$ cuando $t=\lambda$. Esto es multiplicar por una constante. Por lo tanto, la salida vera el mismo efecto. Integrando sobre todos los posibles valores del corrimiento $\lambda$ obtenemos en la salida la integral del producto de convolucion, para la misma entrada $x(t)$. $$y(t) = x(t)*h(t) = \int^{\infty}_{-\infty}x(\lambda)h(t-\lambda)d\lambda$$
Esto quiere decir que la salida es igual a la entrada convolucionada con la respuesta al impulso.

## Convolucion y Sistemas Realizables
Los sistemas realizables son aquellos que existen o podrian existir. Tienen una propiedad que modifica ligeramente la convolucion. Basicamente, es poner la condicion de que lo que vas a _convolucionar_ sea causal. Es decir que, ahora, los limites de la intefral van desde cero hasta infinito.

## Comentarios Adicionales sobre las Funciones de Transferencia
Un dato no menor es que la funcion de respuesta al impulso $h(t)$ forma un par de trasformadas de Laplace con la funcion de transferencia de un circuito, $H(s)$.$$h(t) = H(s)$$
## Plano de Frecuencia Compleja
Se puede construir la constelacion de polos y ceros ploteando estos puntos criticos sobre el plano complejo y macando los polos con un simbolo $\times$ y los ceros con una o. Teniendo la constelacion es facil rearmar la funcion $Z(s)$ que la genera ya que los ceros en $z_0$ se ubican en el numerador como $z-z_0$ y para los polos, lo mismo, pero en el denominador.

Si tengo una funcion de transferencia para un circuito que exhibe polos, puedo hallar la respuesta natural del circuito como la sumatoria de los coeficientes $A_n$ mutiplicados por la forma funcional $e^{s_nt}$ donde $s_n$ son los polos de la funcion de transferencia. Cada uno de los coeficientes se tiene que calcular en base a las condiciones iniciales dadas para el circuito. Si lo que quiero es la respuesta de una tension de salida $V_0$, tomare la funcion de transferencia $H(s) = \frac{V_o(s)}{V_{source}(s)}$. Recordar que en el numerador va la respuesta que quiero estudiar y en el denominador la funcion forzada que me la genere. Los polos de la funcion de transferencia se conocen como _frecuencias naturales_. Si se trabaja con un circuito que no tiene fuentes independientes se puede ubicar una en cualquier lugar, pero los polos deben ser los mismos para todas las ubicaciones. Si la red ya contiene una fuente, esa misma debe igualarse a cero e insertar otra en un punto mas conveniente.