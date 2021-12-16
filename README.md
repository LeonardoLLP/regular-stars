# Regular stars
[Dirección del repositorio]
## Proceso a seguir
En teoría, podemos usar la fórmula de los polígonos regulares para calcular las rotaciones necesarias para realizar la estrella. La fórmula de los ángulos de un polígono regular es
a = (180 * (n - 2)) / n.

Sin embargo, si queremos que realize rotaciones extra (para que forme estrellas), tendremos que hacer que gire más veces. Es decir, reducir el ángulo en 360 / n hace que realize una rotación más. Sin embargo, podemos simplificar los cálculos realizando esta operación con el ángulo exterior.

Como la tortuga se mueve desde uno extremo del segmento, necesita el ángulo exterior a girar. La fórmula en cuestión es

a = 180 - x * full_rotations % n

Multiplicamos el ángulo externo por full_rotations. Esto hace que se cierre más cuantas más rotaciones hallamos especificado. Tiene que estar entre 1 y n (mayor que n es lo mismo que volver a 1 hasta n)

Antes de imprimir, desplazamos la tortuga para ver la figura en el centro. La x es fácil, pero la y puede ser muy complicada de hallar, ya que el radio total de la circunferencia más pequeña que contiene a la figura puede variar mucho. La fórmula hallada fue a base de provar con factores que creía que afectaban a las dimensiones de la figura multiplicados por coeficientes también obtenidos mediante pruebas.



