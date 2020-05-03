¿Acaso para la `Moto` no deberíamos preguntar si es `ligera?` en lugar de `ligero?`?

¡Puede ser! Pero si los mensajes se llaman distinto, no podemos tratar polimórficamente a los objetos. Por ejemplo, no podríamos saber cuántos medios de transporte ligeros hay en una colección de autos y motos, porque no habría un único mensaje -tendríamos `ligero?` y `ligera?`- que respondiera nuestra pregunta.

```ruby
ム transportes.count { |transporte| transporte.ligero? }
=> #¡Falla porque Moto no entiende el mensaje ligero?!

ム transportes.count { |transporte| transporte.ligera? }
=> #¡Falla porque Auto no entiende el mensaje ligera?!
```