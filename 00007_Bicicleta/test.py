class Bicicleta:
  def kilometros_recorrido(self):
    self.kilometros_recorridos



bici = Bicicleta

def test_"Una bicicleta inicializa con 0 kilómetros recorridos":
  expect(bici.kilometros_recorridos).to eq 0


def test_"Una bicicleta tiene dos ruedas":
  expect(bici.cantidad_de_ruedas).to eq 2


def test_"Una bicicleta es ligera":
  expect(bici.ligero?).to be True


def test_"Una bicicleta que se conduce 20 kilómetros y luego 3 kilómetros tiene 23 kilómetros recorridos":
  bici.conducir!(20)
  expect(bici.kilometros_recorridos).to eq 20
  bici.conducir!(3)
  expect(bici.kilometros_recorridos).to eq 23


def test_"Una bicicleta sigue siendo ligera después de conducirla muchos kilómetros":
  bici.ligero?
  expect(bici.ligero?).to be True
