class Micro:
  def litro(self):
    self.litros


  def pasajero(self):
    self.pasajeros


  def diez_pasajero(self):
    self.pasajeros = 10



micro = Micro

def test_"Un micro inicializa con 100 litros":
  expect(micro.litros).to eq 100


def test_"Un micro inicializa con 0 pasajeros":
  expect(micro.pasajeros).to eq 0


def test_"Un micro tiene seis ruedas":
  expect(micro.cantidad_de_ruedas).to eq 6


def test_"Un micro es ligero cuando no tiene pasajeros":
  expect(micro.ligero?).to be True


def test_"Un micro no es ligero cuando tiene pasajeros":
  micro.diez_pasajeros
  expect(micro.ligero?).to be False


def test_"Un micro gasta 0.2 litros por cada kilómetro que se lo conduce":
  micro.conducir!(20)
  expect(micro.litros).to eq (100 - (20 * 0.2))
