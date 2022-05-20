# Resumen para TP-3
## Resonancia
### Frecuencia de Resonancia
La frecuencia de resonancia es la frecuencia para la cual la impedancia es puramente resistiva.
$$Im(Z) = 0$$
Para circuitos RLC serie y paralelo es $$\omega_0 = \frac{1}{\sqrt{LC}}$$
### Factor de Calidad - Q
El factor de calidad es como decir la ganancia de la potencia. Es la salida sobre la entrada.

El factor de potencia para el sistema en RLC serie es $$Q = \frac{\omega_0 L}{R}$$El factor de potencia para el sistema en RLC paralelo es $$Q = \frac{1}{\omega_0RC}$$
En general es $$Q = \frac{\text{salida}}{\text{entrada}} \hspace{1cm} Q=\frac{1}{2\xi}$$ recordamos que $\xi = \frac{\alpha}{\omega_0}$


### Ancho de Banda
El ancho de banda es la diferencia entre las dos frecuencias en las que se da la potencia mitad. Se define como $$B_{\omega} = \omega_2 - \omega_1 \hspace{1cm} B_{\omega}=Q\omega_0$$
Para RLC serie se puede decir que $$\Delta B_{\omega} = \frac{R}{L}$$Para RLC paralelo se puede decir que $$\Delta B_{\omega} = \frac{1}{RC}$$
Si el factor de calidad es mayor o igual a 10 se puede decir que la curva de selectividad es simetrica y por lo tanto se puede definir dicho $\Delta B$ como el mismo para ambos lados de la frecuencia de resonancia.

Otra ecuacion que vale la pena recordar es (para Q>10)$$\omega_0^2 = \omega_1\omega_2$$
Tambien hay que recordar que en RLC serie por debajo de la frecuencia de resonancia el comportamiento del circuito es capacitivo, y por encima es inductivo. Para RLC paralelo es al reves.

## Respuesta en Frecuencia


## Transitorios