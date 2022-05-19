# Circuitos Resonantes
Se dice que un circuito entra en resonancia cuando la impedancia que ve el generador es puramente resistiva.

![[rlc-impedancia-que-ve-el-generador.png]]
_En esta imagen "la impedancia que ve el generador" esta la que esta a la derecha de la marca verde._

Planteando mallas resulta que $$v(t) = i(t)[R+j(\omega L -\frac{1}{\omega C})]$$
Para que entre en resonancia tiene que cumplirse la condicion de que $Z(j \omega) = R$. Entonces, $$\omega L - \frac{1}{\omega C} = 0 \Rightarrow \omega_0^2=\frac{1}{LC}$$
Cuando el circuito se excite con la frecuencia $\omega _0$ se dice que entra en resonancia. Cuando se da esta condicion voy a tener $$v(t) =IR \Rightarrow v_Rv(t)$$
Y, a la vez, $v_L = LX_L \angle 90\degree$ y, tambien, $v_C = IX_C \angle -90\degree$. 

Tambien, vamos a ver tres potencias, correspondientes a cada componente. Estas se calculan como siempre. En la resistencia habra una perdida de energia, mientras que entre el capacitor y el inductor habra un intercambio de energia.

## Factor de Calidad
El factor de calidad $Q$ se puede definir tanto para un circuito como para un componente. Se define como el siguiente cociente $$Q=\frac{\text{Potencia Reactiva}}{\text{Potencia Activa}}$$
Este termino sirve para saber que tan similar es el sistema que se tiene al modelo ideal. Por ejemplo, una bobina con un alto factor de calidad, se comporta mucho mas como bobina que como resistencia.

Para el circuito analizado previamente resultaria$$Q = \frac{I^2X_L}{I^2R}$$
_Nota: aca se podria trabajar tanto con $X_L$ como con $X_C$ pero como generalmente el factor de calidad se asocia con las bobinas, optamos por esa opcion_

Simplificando, queda $Q|_{\omega_0} = \frac{X_L}{R}$ y de ahi $\frac{\omega_0 L}{R}$. Recordemos que por $R$ estamos haciendo referencia a la componente resistiva de todo el circuito, modelada como una sola resistencia.

Ademas de esto, si nos damos cuenta de que $X_LI = V_L$, tambien podemos plantear el factor de calidad en terminos de tensiones y decir que resulta $Q=\frac{V_L}{V}$.


### Valores esperados de Q
Cuando se busca que un circuito trabaje en resonancia se espera hallar valores de $Q$ a partir de 10. Desde ese punto se puede asumir que va a trabajar de manera eficiente para filtros y otras aplicaciones de resonancia.

### Adicionales sobre Q
Partiendo de la expresion obtenida antes $Q=\frac{V_L}{V}$, se puede reescribir como $$V_L = QV(t)$$
Esto es muy importante ya que cuando el circuito entra en resonancia las tensiones en la bobina y el capacitor son $Q$ veces la tension pico de la fuente. En circuitos resonantes, $Q$ suele estar alrededor de 10 (incluso hasta 50). Esto es clave para tener en cuenta a la hora de disenar circuitos. Hay que tener mucho cuidado con alcanzar frecuencias de resonancia.

## Comportamiento en la Region cercana a la Resonancia
Dijimos que para un circuito RLC serie en resonancia se cumple la siguiente ecuacion $$Z=R+j(\omega L - \frac{1}{\omega C})$$ Esto se puede reescribir como $$|Z_T = \sqrt{R^2 + (\frac{\omega^2LC-1}{\omega C})^2}| \hspace{2cm} \angle Z_T = \tan^{-1}(\frac{Im(Z)}{Re(Z)})$$
Para la frecuencia de resonancia $\omega _0$ el angulo de fase es cero y el modulo es exactamente $R$.

A continuacion se grafica la parte reactiva de la impedancia (reactancia) en funcion de la frecuencia

![[reactancia-en-funcion-de-f-rlc-serie.png]]
_En verde, la reactancia inductiva. En rosa, la reactancia capacitiva. En negro, la curva definitiva de la reactancia._

De este grafico podemos extraer que para frecuencias menores a la de resonancia, el circuito se comporta como una impedancia capacitiva. En la misma frecuencia de resonancia, obviamente, sera puramente resistiva. Y, finalmente, para frecuencias mayores, sera inductiva.

El modulo de la impedancia en funcion de la frecuencia se veria algo asi

![[modulo-de-z-en-funcion-de-f-rlc-serie.png]]

Intuitivamente, el grafico de la corriente sera similar a este pero invertido.
![[i-en-funcion-de-f-rlc-serie.png]]

Ahora es un buen momento para definir el ancho de banda y la selectividad de un circuito.

## Ancho de Banda y Selectividad
Si se grafica la corriente en valor absoluto se obtiene una campana con la forma de $|Z|$ pero invertida. Lo mismo con la curva de potencia. La potencia se hace maxima en la frecuencia de resonancia. Esta curva de la que estamos hablando se llama **curva de selectividad**. Esta curva no es perfectamente simetrica, pero si consideramos que el $Q\geq 10$ entonces la podemos tomar como tal.

Se definen ahora dos frecuencias $\omega_1$ y $\omega_2$ que se llaman _frecuencias mitad_. Son las frecuencias para las cuales la potencia entregada es exactamente la mitad de la maxima. Al no ser simetrica la curva de selectividad, $\omega_0$ no tiene por que estar centrada respecto de estas dos.

![[intro-ancho-de-banda.png]]

El ancho de banda $B$ se define como la diferencia (positiva) de las frecuencias mitad. $$B=\omega_2 - \omega_1$$ Si el ancho de banda es chico, significa que el circuito tendra una alta selectividad. Esto es equivalente a decir que esta funcionando como un filtro.


## Variacion de los Parametros de un Circuito y Curvas de Selectividad

![[curvas-de-q-con-r.png]]

En el grafico se observan tres curvas para tres circuitos que resuenan a la misma frecuencia pero con distintas resistencias $R$. Cuanto mas chico sea el $R$, mayor $Q$ vamos a encontrar.

![[curvas-de-q-con-lc.png]]

En este caso se mantiene constante la $R$ y se varian $L$ y $C$. La corriente no va a variar en este caso, solamente el $Q$.

Estas variaviones se pueden combinar. Lo importante es saber que aumentar $R$ hace mas baja la acmpana y aumentar $L$ la hace mas ancha.


## Sobre $\omega_1$ y $\omega_2$
Cuando el circuito este funcionando en una de estas dos frecuencias, la potencia entregada sera la mitad de la maxima y la corriente que circula sera 0,707 veces la maxima.

Haciendo un par de despejes matematicos que no son muy interesantes queda que $$R = \pm(\omega_1L - \frac{1}{\omega_1C})$$Restando ambos resultados entre si, resulta la expresion$$L(\omega_2 + \omega_1) = \frac{1}{C}(\frac{1}{\omega_1} + \frac{1}{\omega_2}) \hspace{1cm} \Rightarrow \hspace{1cm} \omega_1\omega_2=\frac{1}{LC}=\omega_0^2$$Sumando ambos resultados para $R$ entre si, resulta la expresion $$B_{\omega} = \frac{R}{L}$$ Tambien, recordando que $Q=\frac{\omega_0L}{R}$, podemos ver facilmente que $$B_{\omega}=\omega_0Q \hspace{1cm} \Leftrightarrow \hspace{1cm} Q=\frac{\omega_0}{B_{\omega}}$$
## Calculando $\omega_1$ y $\omega_2$
Partiendo de las dos ecuaciones anteriores$$\omega_1\omega_2=\omega_0^2 \hspace{1cm} \wedge \hspace{1cm} (\omega_2 - \omega_1)Q=\omega_0$$ Se puede llegar a la siguiente expresion para $\omega_1$ $$\omega_1 = \omega_0(-\frac{1}{2Q} + \sqrt{(\frac{1}{2Q})^2 + 1})$$ de manera analoga, para $\omega_2$ se tiene $$\omega_2 = \omega_0(\frac{1}{2Q} + \sqrt{(\frac{1}{2Q})^2 + 1})$$
Tambien podemos expresar estas dos frecuencias en terminos de ecuaciones que estudiamos en el analisis de la respuesta de circuitos en regimen transitorio. Recordamos que un circuito de segundo orden puede tener 3 respuestas transitorias (sobreamortiguado, amortiguado y subamortiguado).

En particular, en un circuito subamortiguado, donde las raices son $-\alpha \pm j\omega_0$, vamos a escribir $\omega_{1,2}$ en funcion de estas. Tambien vale la pena recordar que para un circuitlo RLC serie $\alpha = \frac{R}{2L}$. $$\omega_{1,2} \mp \alpha + \sqrt{\alpha^2+\omega_0^2}$$


## Modelos del Inductor
![[modelos-del-inductor.png]]

Tengo que poder trabajar con cualquiera de los dos, segun sea mas comodo y obtener el mismo resultado. Las impedancias y admitancias de cada modelo deben ser iguales. Asi puedo hallar relaciones entre las reactancias para el modelo serie y paralelo. $$R_S=\frac{R_PX_{L_P}^2}{R_P^2+X_{L_P}^2} \hspace{1cm} X_{L_S}=\frac{R_P^2X_{L_P}}{R_P^2+X_{L_P}^2}$$Tambien hay una relacion entre el factor de calidad de cada uno de estos modelos.$$Q_{s_{coil}} = \frac{X_{L_S}}{R_s} = \frac{R_P}{X_{L_P}}=Q_{P_{coil}}$$
## Circuito Resonante RLC Paralelo
Si en el RLC serie vimos que la tension era $Q$ veces la de la fuente (en resonancia), en los paralelo se da el mismo efecto pero con la corriente. Esto vale tanto en el capacitor como en el inductor.

En los serie, la grafica de $|Z|$ era una campana invertida, en los paralelo es una campana no invertida. En resonancia, la impedancia es maxima. A frecuencias por debajo de $\omega_0$ sera inductivo el comportamiento del circuito, mientras que a altas, seria capacitivo.

En estos circuitos $\alpha = \frac{1}{2RC}$, pero las ecuaciones que incluyen $\alpha$ siguen valiendo. Tambien, $B_{\omega} = \frac{1}{RC}$. Mutiplicando esto por 1 se llega a $B_{\omega} = \frac{\omega_0}{Q_P}$.