:bulb: Una forma de organizar las clases cuando programamos en Objetos es definir una **jerarquía**. En nuestro caso podemos pensar que `Moto` y `Auto` se pueden englobar en algo más grande y que las incluye, la idea de `MedioDeTransporte`.

Muchas veces esa jerarquía se puede visualizar en el mundo real: por ejemplo, `Perro` y `Gato` entran en la categoría `Mascota`, mientras que `Cóndor` y `Halcón` se pueden clasificar como `Ave`. Cuando programemos, la jerarquía que utilicemos dependerá de nuestro modelo y de las abstracciones que utilicemos.

Si tenemos abstracciones para `Moto` y `Auto`, ¿alguna vez instanciaremos un objeto de la clase `MedioDeTransporte`? ¡Probablemente no! ¿Por qué querríamos ser tan genéricos con nuestras clases si podemos ser específicos?

En el ejemplo con animales ocurre parecido: si definimos implementaciones específicas para `Cóndor`, `Halcón`, `Perro` y `Gato`, no va a haber un objeto de la clase `Ave` o `Mascota` en nuestro sistema.

A esas clases, como `MedioDeTransporte` o `Ave`, se las llama **clases abstractas** porque, a diferencia de las **clases concretas** (como `Moto` o `Auto`), nunca las instanciamos, en criollo, no creamos objetos con esa clase. Sirven para especificar qué métodos deben implementar aquellas clases que estén más _abajo_ en la jerarquía.

```python
class Ave:
  def volar!



class Condor < Ave:
  def volar!
    self.energia -= 20



class Halcon < Ave:
  def volar!
    self.energia -= 35


```

El símbolo `<` significa "hereda de": por ejemplo, `Cóndor` hereda de `Ave`, que está _más arriba_ en la jerarquía. En la clase abstracta `Ave`, el método `volar!` **no tiene comportamiento** porque el comportamiento lo implementan las clases concretas `Halcón` y `Cóndor`. Entonces, decimos que `volar!` es un **método abstracto**.

> ¡Uf! ¡Eso fue un montón! :fearful: A ver si quedó claro. Marcá las opciones correctas:
