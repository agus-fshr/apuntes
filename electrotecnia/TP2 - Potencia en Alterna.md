# TP2 - Potencia en Alterna
---
## Inductor con nucleo de hierro
En un inductor, cuando se agrega un nucleo de hierro, incrementa la inductancia L. Esto se debe a que los dipolos magneticos del hierro, al estar en un campo magnetico se reorientan favoreciendo al mismo. Es decir, con un nucleo de hierro se incrementa el campo magnetico que genera el efecto de inductancia.

En electronica se usa _soft iron_ porque no es deseado que el metal retenga el efecto del campo magnetico.


## Potencia Instantanea
La potencia instantanea que se suministra a cualquier dispositivo esta dada por el producto de la tension instantanea y la corriente instantanea. 
$$ p(t) = v(t)i(t) $$
Si el dispositivo es una **resistencia** entonces se puede decir que
$$p(t) = i^2(t)R = \frac{v^2(t)}{R}$$
Se recomienda no hacer esto, sobre todo con impedancias complejas.

En el caso de un dispositivo completamente **inductivo** se puede usar la identidad $V_L = L \frac{di}{dt}$ para decir que
$$p(t) = Li(t)\frac{di(t)}{dt} = \frac{1}{L}v(t)\int^{t}_{-\infty}v(t')dt'$$
_Nota: esto asume que la tension es cero en $t=-\infty$_

En el caso de una impedancia puramente **capacitiva** (y suponiendo lo mismo que en la inductancia)
$$p(t) = Cv(t)\frac{dv(t)}{dt} = \frac{1}{C}i(t)\int^{t}_{-\infty}i(t')dt'$$
**Linealidad**: la potencia instantanea total de un circuito es la suma directa de todas las potencias, ya sea en serie o en paralelo.

## Potencia promedio o activa
Para poder hablar de un promedio de la potencia instantanea hay que definir un periodo o intervalo en que se lleve a cabo el promedio. En general, tomamos un intervalo $t_2-t_1$.
Entonces, se define la potencia activa como
$$P = \frac{1}{t_2-t_1}\int^{t_2}_{t_1}p(t)dt$$
para formas de onda periodicas se puede reescribir como
$$P = \frac{1}{T}\int^{t_x + T}_{t_x}p(t)dt = \lim_{\tau \to \infty}\frac{1}{\tau}\int^{\tau / 2}_{-\tau / 2}p(t)dt$$
Si se supone una tension senoidal permanente dada por $v(t)=V_m\cos{(\omega t + \theta)}$ y $i(t) = I_m \cos{(\omega t + \phi)}$ la potencia instantanea resulta ser
$$ p(t) =V_mI_m\cos{(\omega t + \theta)}\cos{(\omega t + \phi)}$$
donde, reescribiendo el producto de cosenos, se obtiene
$$p(t)=\frac{1}{2}V_mI_m\cos{(\theta - \phi)} + \frac{1}{2}V_mI_m\cos{(2\omega t+\phi)}$$El segundo termino es un coseno. El valor promedio de coseno sobre un periodo es cero. Por lo tanto, se puede resumir la expresion de potencia media para circuitos de corriente alterna en
$$ P = \frac{1}{2}V_mI_m\cos{(\theta - \phi)} $$
Es importante recordar que $\theta$ es el angulo correspondiente a la tension y que $\phi$ es el correspondiente a la corriente. Por lo tanto $\theta - \phi$ corresponde a la diferencia de fase de la corriente con respecto a la tension. Para elementos no reactivos, esta diferencia es siempre cero y por eso la potencia media para resistencias es siempre $P_R = \frac{V_m^2}{2R} = \frac{1}{2}I^2_mR$ Por otro lado, en elementos puramente reactivos, el desfasaje es de $\pm90^\degree$ , por lo que su potencia media o activa es cero.

**Ejemplo: Encuentre la potencia promedio (activa) que se entrega a una impedancia$Z_L = 8-11j$  por la que circula una corriente $I=5 \angle 20° A.$**
_Esto se resuelve muy rapido recordando el parrafo anterior. La componente compleja de la impedancia no va a dar una potencia promedio, solo la parte real lo hace. Por lo tanto_
$$P = \frac{1}{2}(5^2)8 = 100W$$
## Transferencia de potencia maxima
Se da cuando $Z_L = Z_{th}^*$. Esto se conoce como el _teorema de transferencia de potencia maxima del estado senoidal permanente_. En esta ecuacion es destacable que $Z_L$ se refiere a la impedancia de carga (Load Impedance) y no a un inductor.

## Valores eficaces de corriente y de tension
Se define el valor RMS o eficaz de una magnitud $X$ como
$$ X_{ef} = \frac{X_{pico}}{\sqrt{2}}$$
La ventaja de usar valores eficaces es que permite simpliicar la expresion de la potencia activa o promedio. $$P = \frac{1}{2}I_m^2R = I_{ef}^2R = \frac{V_{ef}^2}{R}$$
_Nota: en aplicaciones se usa el valor eficaz en las areas de transmision o distribucion de potencia y con maquinaria rotatoria. Se usa el valor pico en aplicaciones de electronica y comuicaciones._

Para corrientes **no coherentes** hay que hacer unas distinciones. Para el calculo de la potencia media se dice que $$P = (I^2_{1ef} + I^2_{2ef} + ... = I^2_{Nef})R$$
y de ahi, tambien se puede decir que $$I_{ef} = \sqrt{I^2_{1ef} + I^2_{2ef} = ... + I^2_{Nef}}$$
## Potencia aparente y factor de potencia
La potencia aparente se define como el producto $V_{ef}I_{ef}$. Esta no es la potencia promedio. Es la potencia aparente. La potencia aparente se mide en las mismas unidades que la potencia real, pues el coseno es adimensional, sin embargo, para evitar confusiones, se dice que la unidad es VA o _volt-amperes_. Ademas, se define el factor de potencia $\text{fp}$ de modo que
$$\text{fp} = \frac{\text{potencia promedio}}{\text{potencia aparente}} = \frac{P}{V_{ef}I_{ef}} = \cos{(\theta - \phi)}$$
## Potencia compleja
