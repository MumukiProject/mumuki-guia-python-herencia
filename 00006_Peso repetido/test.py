class Auto:
  def litro(self):
    self.litros



class Moto:
  def litro(self):
    self.litros



auto = Auto
moto = Moto
medio = MedioDeTransporte

def test_"Un auto inicializa con 40 litros de combustible":
  expect(auto.litros).to eq 40


def test_"Un auto no es ligero al iniciar":
  expect(auto.ligero?).to be False


def test_"Un auto gasta 0.05 litros por cada kilómetro que se lo conduce":
  auto.conducir!(500)
  expect(auto.litros).to eq (40 - (0.05 * 500))


def test_"Un auto es ligero después de conducirlo muchos kilómetros":
  auto.ligero?
  expect(auto.ligero?).to be True


def test_"Un auto tiene cuatro ruedas":
  expect(auto.cantidad_de_ruedas).to eq 4


def test_"Un auto pesa 800 kilos":
  expect(auto.peso).to eq 800


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


def test_"Una moto pesa 400 kilos":
  expect(moto.peso).to eq 400


def test_"ligero? en MedioDeTransporte es un método abstracto":
  expect(medio.ligero?).to eq None


def test_"conducir! en MedioDeTransporte es un método abstracto":
  expect(medio.conducir!(23)).to eq None


def test_"cantidad_de_ruedas en MedioDeTransporte es un método abstracto":
  expect(medio.cantidad_de_ruedas).to eq None
