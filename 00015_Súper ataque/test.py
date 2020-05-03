class Zombi:
  def __init_(self):
    self.salud = 100


  def salu(self):
    self.salud


  def recibir_danio!(self, puntos):
    self.salud = [self.salud - puntos * 2, 0].max



bouba = Zombi
kiki = Zombi
zombisexual = Zombi
julian = Aliado
candelo = Aliado
juliana = Sobreviviente
persona = Persona

def test_"La energía inicial de una sobreviviente es 1000":
  expect(juliana.energia).to eq 1000


def test_"Si una sobreviviente ataca normalmente su energía no se reduce":
  juliana.atacar!(kiki, 5)
  expect(juliana.energia).to eq 1000


def test_"Si una sobreviviente bebe una bebida energética su energía aumenta un 25%":
  juliana.beber!
  expect(juliana.energia).to eq 1000 * 1.25


def test_"Si una sobreviviente ataca con 5 puntos de daño a un zombi su salud disminuye en 10 puntos":
  juliana.atacar!(bouba, 5)
  expect(bouba.salud).to eq 90


def test_"La energía inicial de un aliado es 500":
  expect(julian.energia).to eq 500


def test_"Si un aliado ataca su energía se reduce un 5%":
  julian.atacar!(kiki, 5)
  expect(julian.energia).to eq 500 * 0.95


def test_"Si un aliado bebe una bebida energética su energía aumenta un 10%":
  candelo.beber!
  expect(candelo.energia).to eq 500 * 1.10


def test_"Si un aliado ataca con 5 puntos de daño a un zombi su salud disminuye en 10 puntos":
  julian.atacar!(zombisexual, 5)
  expect(bouba.salud).to eq 90


def test_"beber! en Persona es un método abstracto":
  expect(persona.beber!).to eq None

