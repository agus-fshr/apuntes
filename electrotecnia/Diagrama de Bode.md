# Diagrama de Bode
En respuesta en frecuencia, habiamos definido una funcion de transferencia $H(s)$. En particular vamos a trabajar con la funcion transferencia de ganancia de tension en la frecuencia $j\omega$ $$H(j\omega) = \frac{V_{OUT}(j\omega)}{V_{IN}(j\omega)}$$El diagrama de Bode es una manera de graficar la respuesta en frecuencia que tiene la funcion transferencia de un circuito. Lo que tiene de especial es que trabaja tanto con el modulo como con la fase de la respuesta en frecuencia.

Lo especial es que el **modulo** de la funcion de transferencia se va a trabajar en la unidad **dB o decibel** y se va a representar sobre el eje de las frecuencias con una **escala logaritmica**. Para la **fase** se va a trabajar sobre el mismo eje y en cuando al eje de la fase, se trabajara en **grados**. Esta representacion permite incluir un mayor rango de frecuencias para tener un estudio mas abarcativo de la respuesta en frecuencia de un circuito.

El decibel (dB) se define como $10\log{(\frac{P_{OUT}}{P_{IN}})}$, en criollo es _10 veces el logaritmo de la ganancia de potencia_.$$P_{OUT} = \frac{V_{out}^2}{Z_{out}} \hspace{1cm} P_{IN} = \frac{V_{in}^2}{Z_{out}}$$De esta expresion se puede ver que $dB = \log{(\frac{V_o^2}{V_i^2})} = 20\log{(\frac{V_o}{V_i})}$ Entonces $$|H(j\omega)||_{dB} = 20\log{|H(j\omega)|}$$Notese que duplicar el $|H(s)|$ genera un aumento de 6dB. Dividir al medio es un decremento de 6dB. Lo mas importante es ver que cuando se trabaja con potencias el logaritmo va multiplicado por 10. Con tensiones va por 20. Entonces las potencias medias son las que representan un decremento de 3dB respecto de la potencia maxima.

## Diagrama de Bode de la Funcion Transferencia
La funcion de transferencia $H(s)$ veremos que puede estar formada por 4 factores basicos.

- $H(j\omega) = k$
- $H(j\omega) = (j\omega)^{\pm n}$ ; $s^{\pm n}$
- $H(j\omega) = (1+j\frac{\omega}{T})^{\pm n}$
- $H(j\omega) =[1 + 2\xi(j\frac{\omega}{\omega_0}) + (j\frac{\omega}{\omega_0})^2]^{\pm n}$ _Esto es funcion cuadratica que es dos polos, segun cuanto valga xi. Pueden ser dos reales coincidentes o no, o dos complejos conjugados. Eso depende de xi_

Entonces la funcion de transferencia resulta una combinacion lo mas variada que uno quiera de dichos factores basicos. $$H(s)=k\frac{s}{(1+\frac{s}{T})[1 + 2\xi(j\frac{\omega}{\omega_0}) + (j\frac{\omega}{\omega_0})^2]}$$
Cuando $H(s)=k$ tengo dos posibilidades. Si $k>1$ la funcion transferencia, en dB es un valor positivo. De lo contrario (obviamente, sin contar el cero), seria negativo. Tambien, en estos casos $\angle H(s) = \tan^-1(\frac{Im}{Re}) = 0$.

Para fuciones de transferencia de la forma $H(s)=(j\omega)^{n}$, va a quedar $n20\log{(\omega)}$. El numero que multiplica al logaritmo es la pendiente de la recta que queda en el diagrama y se dice que la funcion de transferencia tiene una subida/bajada de $20n$ dB por decada (dB/dec).

Para la funcion basica $H(s) = (1 + j\frac{\omega}{T})^{\pm n}$

## Trabajando en octavas
Si se quiere analizar la funcion de transferencia en un rango reducido de frecuencias se pude trabajar en octavas, en lugar de decadas. Las octavas aumentan y disminuyen en un factor de 2. Esto da una vision mas ampliada alrededor de una frecuencia especifica. La subida y bajada por octava funciona de la misma manera que en las decadas. Quiero decir, se calcula de la misma manera, solo que ahora es por octava en lugar de por decada.