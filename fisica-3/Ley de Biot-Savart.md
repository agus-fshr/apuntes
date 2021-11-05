# Ley de Biot-Savart
---
Es una ley experimental que describe las caracteristicas del campo magnetico en algun punto del espacio, generado por un conductor con corriente.
Se considera al conductor formado por elementos de corriente $id\vec{s}$ que aportan en el punto a determinar el campo de induccion magnetica un $d\vec{B}$

- $d\vec{B}$ es perpendicular a $d\vec{s}$
- $d\vec{B}$ es perpendicular a $\vec{r}$
- $|d\vec{B}|\propto i$
- $|d\vec{B}|\propto \frac{1}{|\vec{r}|^2}$
- $|d\vec{B}|\propto \sin(\theta)$, siendo $\theta$ el angulo entre $\vec{r}$ y $d\vec{s}$

<p align="center">
	<img src="https://i.imgur.com/w4BWKUS.png" width="400px" width="400px"/>
</p>

Esto se traduce a la expresion 
$$d\vec{B} = \frac{\mu_0}{4\pi}\frac{id\vec{s}\times\vec{r}}{|\vec{r}^2|^2}$$
Para determinar el $\vec{B}$ en un punto, se deben supar las contribuciones de cada elemento de corriente que forman la corriente del conductor en dicho lugar. Esto significa que se debe integrar la expresion de arriba.
> Ley de Biot-Savart
> $$\vec{B} = \frac{\mu_0i}{4\pi}\int\frac{d\vec{s}\times\vec{r}}{|\vec{r}^2|^2}$$
> $$d\vec{B} = \frac{\mu_0}{4\pi}\frac{id\vec{s}\times(\vec{r}-\vec{r_0})}{|\vec{r}-\vec{r_0}|^3}$$

Recordar
> Permeabilidad magnetica del vacio ($\mu_0$)
> $$\mu_0 = 4\pi 10^{-7}\frac{Tm}{A}=4\pi 10^{-7}\frac{N}{A^2}$$