¡Es la hora de movilizarse! Todos los días la gente necesita trasladarse a distintos lugares, ya sea a pie, en tren, en bicicleta... Nosotros no podíamos quedarnos atrás: vamos a implementar nuestros propios [medios de transporte](https://es.wikipedia.org/wiki/Anexo:Medios_de_transporte) en Objetos.

Empecemos por uno simple, el `Auto` :oncoming_automobile: . Las instancias de la clase `Auto` se inicializan con 40 `self.litros` de combustible.

¿Qué sabe hacer un `Auto`? Puede decirnos si es `ligero?`, que es verdadero cuando la cantidad de `self.litros` es menor a 20. Su combustible disminuye a medida que se desplaza: se puede `conducir!` una cierta cantidad de kilómetros, y los `self.litros` disminuyen a razón de 0.05 por cada kilómetro.

También sabe responder su `cantidad_de_ruedas`: siempre es 4, porque no contamos la rueda de auxilio :stuck_out_tongue: .

> Veamos si se entiende: definí la clase `Auto`, que sepa entender los mensajes `__init__`, `ligero?`, `conducir!` y `cantidad_de_ruedas`.
