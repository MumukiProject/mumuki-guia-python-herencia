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


def test_"Un micro sin pasajeros pesa 1200":
  expect(micro.peso).to eq 1200


def test_"Si en un micro suben siete pasajeros y bajan tres quedan cuatro pasajeros":
  7. times { micro.sube_pasajero! }
  expect(micro.pasajeros).to eq 7
  3. times { micro.baja_pasajero! }
  expect(micro.pasajeros).to eq 4


def test_"Un micro con cuatro pasajeros pesa 1520":
  expect(micro.peso).to eq 1520


def test_"Un micro no es ligero cuando tiene pasajeros":
  micro.diez_pasajeros
  expect(micro.ligero?).to be False


def test_"Un micro gasta 0.2 litros por cada kilómetro que se lo conduce":
  micro.conducir!(20)
  expect(micro.litros).to eq (100 - (20 * 0.2))
