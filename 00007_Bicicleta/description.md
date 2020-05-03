Silenciosamente se acerca el transporte más ecológico de todos: la `Bicicleta`. :bike: ¿Qué sabe hacer una `Bicicleta`? ¡Lo mismo que cualquier `MedioDeTransporte`, obvio! Por eso hereda de esa clase. Pero su comportamiento ya no es tan similar al de `Auto` y `Moto`.

Para empezar, su `cantidad_de_ruedas` es 2, y siempre es `ligero?`. No lleva combustible, por lo que ya no lleva cuenta de los litros: al `conducir!` una cantidad de kilómetros, los suma a una cuenta de `self.kilometros_recorridos`. Al inicializarse, una `Bicicleta` lleva 0 `self.kilometros_recorridos`.

> Todo va sobre ruedas: definí una clase `Bicicleta` que herede de `MedioDeTransporte` y que entienda los mensajes `__init__`, `cantidad_de_ruedas`, `ligero?` y `conducir!`.
