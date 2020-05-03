¡Genial! :grin: 

**Redefinir** el método de una superclase, como hicimos con `peso`, nos permite **modificar el comportamiento** que definió la superclase originalmente. De ese modo, declarar `peso` en `MedioDeTransporte` nos permite agrupar la lógica unificada de `Auto` y `Moto` - pero a la vez, podemos contemplar los casos en los que requiramos otro comportamiento, como en `Bicicleta`.