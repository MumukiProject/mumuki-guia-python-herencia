¿Y cuál es la gracia de tener un `Micro` si no puede trasladar a nadie? `Micro` debe entender también los mensajes `sube_pasajero!` y `baja_pasajero!`, que incrementan o disminuyen en uno la cantidad de `self.pasajeros` a bordo.

¡Momento! :raised_hand: ¿Por qué no definirlo en la clase abstracta `MedioDeTransporte`? Porque muchas clases heredan de ella, y **no nos interesa** que el resto de los medios de transporte implementen la lógica de traslado de pasajeros. ¡No entran más de dos personas en una `Moto` o `Bicicleta`!

> Es tu turno: agregá los métodos `sube_pasajero!`y `baja_pasajero!` a la clase `Micro`.
