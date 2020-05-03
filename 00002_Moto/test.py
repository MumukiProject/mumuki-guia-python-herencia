class Moto:
  def litro(self):
    self.litros



moto = Moto

def test_"Una moto inicializa con 20 litros de combustible":
  expect(moto.litros).to eq 20


def test_"Una moto no es ligera al iniciar":
  expect(moto.ligero?).to be False


def test_"Una moto gasta 0.1 litros por cada kilómetro que se la conduce":
  moto.conducir!(150)
  expect(moto.litros).to eq (20 - (0.1 * 150))


def test_"Una moto es ligera después de conducirla muchos kilómetros":
  moto.ligero?
  expect(moto.ligero?).to be True


def test_"Una moto tiene cuatro ruedas":
  expect(moto.cantidad_de_ruedas).to eq 2
