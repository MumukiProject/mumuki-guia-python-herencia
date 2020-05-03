¡Nuevamente tenemos problemas con el `peso`! :tired_face: No alcanza con que el `Micro` lo calcule utilizando únicamente sus ruedas, porque descubrimos que además depende de la cantidad de `@pasajeros` que esté trasladando.

Y eso nos pone en un problema interesante: de la forma actual, el peso está mal calculado. Pero redefinir `peso` en `Micro` implicaría repetir la lógica de `cantidad_de_ruedas * 200`. ¿Hay otra posibilidad?

¡Sí! El mensaje `super`. Al utilizar `super` en el método de una subclase, **se evalúa el método con el mismo nombre de su superclase**. Por ejemplo...

```python
class Saludo
  def saludar
    "Buen día"
  end
end

class SaludoFormal < Saludo
  def saludar
    super + " señoras y señores"
  end
end
```

De esta forma, al enviar el mensaje `saludar` a `SaludoFormal`, `super` **invoca** el método `saludar` de su superclase, `Saludo`. :wave:

```python
ム mi_saludo = SaludoFormal.new
ム mi_saludo.saludar
=> "Buen día señoras y señores"
```

> ¡Ahora te toca a vos! Agregá el método `peso` a `Micro`, de modo que se calcule como la `cantidad_de_ruedas` multiplicado por 200, sumado a la cantidad de `@pasajeros` por 80. ¡Recordá utilizar `super` para evitar repetir lógica!
