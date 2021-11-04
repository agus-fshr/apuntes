# Magnetismo
---

### Fuerza de Lorentz
$$\vec{F} = q \vec{v} \times \vec{B}$$
$$|\vec{F}| = q|\vec{v}||\vec{B}|sin(\theta)$$


### Particula con Velocidad en un Campo Magnetico Uniforme

#### 1. Caso $\vec{v} \perp \vec{B}$
<p align="center">
	<img src="https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/1989/2017/06/13230245/figure-23-05-02a.jpeg" width="300px" width="300px"/>
</p>

Cuando el vector velocidad y campo magnetico son ortogonales se da un Movimiento Circular Uniforme en el plano paralelo al campo magnetico y ortogonal a la velocidad. El mismo se puede modelar con las siguientes ecuaciones.
$$ |\vec{F}| = m \frac{v^2}{r} = qvB $$ 
Esto vale porque la Fuerza de Lorentz actua como fuerza central del MCU. Como esta es perpendicular a la velocidad, $\sin{\theta}$ valdra uno, y el producto vectorial se vuelve $qvB$.
$$qB = m \frac{v}{r} = m \omega$$
$$\omega = qB/m$$
Ademas, como $\omega = \frac{2\pi}{T}$
$$T = 2\pi \frac{m}{qB}$$
Aca es importante resaltar que ni el periodo $T$ ni la frecuencia angular $\omega$ dependen ni del radio $r$ del MCU ni de la rapidez $|\vec{v}|$.

#### 2. Caso $\vec{v} \nperp \vec{B}$
En este caso, la trayectoria que describe la particula es helicoidal. Se da un MCU en el plano ortogonal al campo magnetico y un MRU a lo largo del eje paralelo al campo magnetico.

<p align="center">
  <img src="https://cnx.org/resources/abc4bda78cb43c2105ccc3b5498e878159ed2b2a" height="300px" width="300px"/>
</p>

Esta trayectoria tiene un paso constante  definido por $p=v_{\parallel}T$. Si la carga se moviera paralela al campo magnetico, no habria una fuerza deflectora ya que $v_{\perp}$ seria cero.

#### 3. Caso $\vec{B} \parallel \vec{E}$
Ahora la trayectoria es una helice pero con paso variable. Esto se debe a que en el eje del vector velocidad, esta la fuerza electrica del campo electrico. Ahora, la fuerza total de Lorentz es
$$\vec{F} = q\vec{v}\times\vec{B} + q\vec{E}$$


### Selector de Velocidades
En el selector de velocidades, existe una superposicion de un campo electrico y uno electronico. Las fuerzas que aporta cada uno deben tener el mismo modulo y sentido contrario para evitar que la particula acelerada se desvie. La velocidad que se "selecciona" esta dada por las siguientes ecuaciones.

<p align="center">
  <img src="https://lh3.googleusercontent.com/proxy/TDwejoZ835tPxJtzxVY1-GiAziRTRiWe-4eakZ0U_3rDGlh3jlu9k-ZiWIAmnGO0PLMRhgp2ho0PRbwQsKaNz9bcatCE3LgJmFQ1SDIWWslRjhh-vCJ6" height="200px" width="300px"/>
</p>

$$\vec{F_E} = - \vec{F_B} \Rightarrow |\vec{F_E}| = |\vec{F_B}| = qE = qvB$$
$$v = \frac{B}{E}$$

### Espectrometro de Masas
El espectrometro de masas es un dispositivo qu epermite analizar con gran precicion la composicion de diferentes elementos quimicos e isotopos atomicos. El espectrometro de Bainbridge se compone de un selector de velocidades y otro tramo con solamente un campo magnetico y una pantalla.

<p align="center">
  <img src="http://i.stack.imgur.com/UDrwC.png" height="300px" width="350px"/>
</p>

El radio de la orbita es proporcional a la masa, por lo que iones de distina masa impactan en diferentes zonas de la placa. En la region de campo unicamente magnetico, las particulas experimentan una fuerza neta dada por $\vec{F}=q\vec{v}\times\vec{B}$. Aplicando dinamica del MCU, obtenemos 
$$qvB_0 = ma = m \frac{v^2}{r}$$
$$r = \frac{mv}{qB_0}$$

La razon $\frac{m}{q}$ es $B_0r\frac{B}{E}$ y, ademas, sabiendo que la velocidad de salida del selector de velocidades es $v=\frac{E}{B}$...
$$\frac{m}{q} = B_0 r \frac{B}{E}$$

### Fuerza Magnetica sobre un Conductor que Transporta Corriente
Se puede tomar la corriente como un conjunto de portadores de carga en movimiento. A cada uno de estos le aplicara una Fuerza de Lorentz.
