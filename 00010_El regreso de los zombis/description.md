¿Creíste que habíamos terminado con los zombis? ¡Nada más alejado de la realidad! :fearful: 

[Cuando surgieron los `SuperZombi`](https://staging.mumuki.io/exercises/4297-programacion-con-objetos-clases-e-instancias-super-zombi), notamos que parte de su comportamiento era compartido con un `Zombi` común: ambos pueden `gritar`, decirnos su `salud`, y responder si están `sin_vida?` de la misma forma. Pero hasta allí llegan las similitudes: `recibir_danio!` y `sabe_correr?` tienen implementaciones distintas, y además, un `SuperZombi` puede `regenerarse!`, a diferencia de un `Zombi`.

¡Esto nos da una nueva posibilidad! Podemos hacer que `SuperZombi` herede de `Zombi` para:

* Evitar **repetir la lógica** de aquellos métodos que son iguales, ya que se pueden implementar únicamente en la superclase `Zombi`
* **Redefinir** en `SuperZombi` aquellos métodos cuya implementación sea distinta a la de `Zombi`
* Implementar **únicamente** en `SuperZombi` el comportamiento que es exclusivo a esa clase

> ¿Te animás? ¡Marcá las respuestas correctas!