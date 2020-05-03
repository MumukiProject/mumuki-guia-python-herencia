¡Suficientes ruedas por hoy! Para terminar, volvamos un momento a la invasión zombi. Veamos parte del comportamiento de `Sobreviviente` y `Aliado`:

```python
class Sobreviviente:
  def __init_(self):
    self.energia = 1000


  def energi(self):
    self.energia


  def beber!
    self.energia *= 1.25


  def atacar!(self, zombi, danio):
    zombi.recibir_danio!(danio)



class Aliado:
  def __init_(self):
    self.energia = 500


  def energi(self):
    self.energia


  def beber!
    self.energia *= 1.10


  def atacar!(self, zombi, danio):
    zombi.recibir_danio!(danio)
    self.energia *= 0.95


```

Como verás, tenemos distintos grados de similitud en el código:

* `energia` es igual para ambas clases, porque sólo devuelve la energía;
* **Una parte** de `atacar!` coincide: en la que el zombi `recibe_danio!`, pero en `Aliado` reduce energía y en `Sobreviviente` no;
* `beber!` es diferente para ambas clases.

> Último esfuerzo: definí una clase abstracta `Persona` que agrupe el comportamiento que se repite y hacé que las clases `Sobreviviente` y `Aliado` hereden de ella. Finalmente, implementá en esas clases el código que es propio de cada una de ellas. ¡No olvides usar `super`!
