class Auto:
  def litro(self):
    self.litros



auto = Auto

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
