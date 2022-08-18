# Soluciones

Una solucion liquida es un sistema homogeneo formado por dos o mas componentes.

El soluto puede ser **volatil** o **no volatil**. Si es no volatil, puedo asegurar que en un equilibrio no va a tener tendencia a pasar a fase vapor.

El soluto tambien se puede clasificar como **ionico** (electrolito) o **no ionico** (no electrolito). Esto me sirve para analizar sus propiedades coligativas. La magnitud de estas propiedades va a depender del numero de particulas disueltas de soluto y no de la naturaleza de dicho soluto. Las propiedades coligativas son

- Descenso de la presion de vapor
- Ascenso ebulloscopico
- Descenso crioscopico
- Presion osmotica

## Factor de van't Hoff

Para estudiar estas propiedades coligativas se hace uso del *factor i*. Es la suma de los coeficientes estequiometricos que resultan de la disociacion del electrolito.

# Propiedades coligativas

## Descenso de la presion de vapor

La presion de vapor de una solucion es menor que la del solvente puro.

Si se tiene un solvente puro, las moleculas liquidas pasan a la fase de vapor hasta llegar al equilibrio. Si se agrega un soluto no volatil, sucedera lo mismo. La diferencia es que en el segundo caso habra menos moleculas de solvente en la superficie. Entonces, la velocidad de evaporacion sera menor, con la consiguiente menor presion de vapor.

*A mayor cantidad de particulas de soluto, menor sera la presion (mayor disminucion de presion de vapor).*

Hay un modelo matematico que permite estudiar esta propiedad coligativa. Recordemos...
$$P_{v,solucion} = P_{v,solvente} + P_{v,soluto} = P_{v,solvente}$$ porque el soluto es no volatil.

### Ley de Raoult

$$p = x_{sv}p^o$$

$p$: presion de vapor de la solucion
$p^o$: presion de vapor del solvente puro
$x_{sv}$: fraccion molar del solvente

Para saber si una solucion es ideal, debe cumplir la Ley de Raoult.

Podemos desarrollar un poco mas sobre la Ley de Raoult para llegar a expresoines mas utiles. El desarrollo esta en los slides de la presentacion, yo voy a copiar los resultados directamente.

Para calcular la fraccion molar, es importante recordar que en los solutos electrolitos, hay que multiplicar el numero de moles porque el factor de van't Hoff. En realidad, se le pone a todos el factor de van't Hoff, pero solamente en los electrolitos puede dar distinto de 1.

## Ascenso ebulloscopico

La temperatura de ebullicion de la solucion es mayor que la del solvente puro.

Una solucion ebulle cuando su presion de vapor es igual a la exterior, si tiene soluto, esta disminuye y habra que calentar aun mas la solucion. Por ende, aumenta su temperatura de ebullicion.

Esto se expresa como $$ T_{eb} - T_{eb}^o = \Delta T_{eb} = K_{eb}m $$

- $m$: molalidad de la solucion. Esta no varia con la temperatura.
- $K_{eb}$: constante ebulloscopica. Se define como el ascenso ebulloscopico de una solucion 1 molal. Depende solamente del solvente y esta tabulada en el cap. 14 del Whitten. *Constante de levacion del punto de ebullicion*

## Descenso crioscopico

La temperatura de congelacion de una solucion es menor que la del solvente puro.

Aca decidieron redefinir el $\Delta$ para   que les de positivo, porque lo llamaron descenso y no ascenso...

$$ T_c^o - T_c = \Delta T_c = K_c i m $$

- $m$: molalidad de nuevo
- $K_c$: constante crioscopica. Se define como el descenso crioscopico de una solucion de 1 molal. Esta tabulada en el cap. 14 del Whitten.

## Presion osmotica

Esto se da cuando se tiene un solvente puro y una solucion o bien dos soluciones de diferente concnetracion. Solo se da a traves de una membrana semipermeable.

$$ \pi = iMRT $$

- $\pi$: presion osmotica
- $M$: molaridad (ya que es a temperatura constante)
- $R$: constante de los gases ($0,082 L.amt.K^{-1}.mol^{-1}$)

