Una ventaja de la herencia es que nos permite agrupar comportamiento en la superclase que, de otra forma, tendríamos repetido en las subclases. ¡Es exactamente lo que nos ocurre con `peso`! ¡Qué casualidad! :smirk: 

Como el cálculo de `peso` es igual para todos los `MedioDeTransporte` que tenemos, podemos **pasarlo tal como está a la superclase** y, como `Auto` y `Moto` heredan de ella, van a seguir entendiendo el mensaje de la misma forma que antes. ¡En serio!

Nada de lo anterior cambia: `MedioDeTransporte` sigue siendo una clase abstracta, pero en ella, `peso` es un **método concreto**, ya que se define su comportamiento para todas las subclases. ¡Y dejamos de repetir esa lógica!

> Veamos si se entiende: quitá el método `peso` de `Auto` y `Moto` y agregalo a `MedioDeTransporte`.