class Auto
  def litros
    @litros
  end
end

class Moto
  def litros
    @litros
  end
end

auto = Auto.new
moto = Moto.new
medio = MedioDeTransporte.new

it "Un auto inicializa con 40 litros de combustible" do
  expect(auto.litros).to eq 40
end

it "Un auto no es ligero al iniciar" do
  expect(auto.ligero?).to be false
end

it "Un auto gasta 0.05 litros por cada kilómetro que se lo conduce" do
  auto.conducir!(500)
  expect(auto.litros).to eq (40 - (0.05 * 500))
end

it "Un auto es ligero después de conducirlo muchos kilómetros" do
  auto.ligero?
  expect(auto.ligero?).to be true
end

it "Un auto tiene cuatro ruedas" do
  expect(auto.cantidad_de_ruedas).to eq 4
end

it "Una moto inicializa con 20 litros de combustible" do
  expect(moto.litros).to eq 20
end

it "Una moto no es ligera al iniciar" do
  expect(moto.ligero?).to be false
end

it "Una moto gasta 0.1 litros por cada kilómetro que se la conduce" do
  moto.conducir!(150)
  expect(moto.litros).to eq (20 - (0.1 * 150))
end

it "Una moto es ligera después de conducirla muchos kilómetros" do
  moto.ligero?
  expect(moto.ligero?).to be true
end

it "Una moto tiene cuatro ruedas" do
  expect(moto.cantidad_de_ruedas).to eq 2
end

it "ligero? en MedioDeTransporte es un método abstracto" do
  expect(medio.ligero?).to eq nil
end

it "conducir! en MedioDeTransporte es un método abstracto" do
  expect(medio.conducir!(23)).to eq nil
end

it "cantidad_de_ruedas en MedioDeTransporte es un método abstracto" do
  expect(medio.cantidad_de_ruedas).to eq nil
end