class Moto
  def litros
    @litros
  end
end

moto = Moto.new

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