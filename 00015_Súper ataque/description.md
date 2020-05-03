¡Suficientes ruedas por hoy! Para terminar, volvamos un momento a la invasión zombi. Veamos parte del comportamiento de `Sobreviviente` y `Aliado`:

```ruby
class Sobreviviente
  def initialize
    @energia = 1000
  end

  def energia
    @energia
  end
  
  def beber!
    @energia *= 1.25
  end

  def atacar!(zombi, danio)
    zombi.recibir_danio!(danio)
  end
end

class Aliado
  def initialize
    @energia = 500
  end

  def energia
    @energia
  end

  def beber!
    @energia *= 1.10
  end

  def atacar!(zombi, danio)
    zombi.recibir_danio!(danio)
    @energia *= 0.95
  end
end
```

Como verás, tenemos distintos grados de similitud en el código:

* `energia` es igual para ambas clases, porque sólo devuelve la energía;
* **Una parte** de `atacar!` coincide: en la que el zombi `recibe_danio!`, pero en `Aliado` reduce energía y en `Sobreviviente` no;
* `beber!` es diferente para ambas clases.

> Último esfuerzo: definí una clase abstracta `Persona` que agrupe el comportamiento que se repite y hacé que las clases `Sobreviviente` y `Aliado` hereden de ella. Finalmente, implementá en esas clases el código que es propio de cada una de ellas. ¡No olvides usar `super`!