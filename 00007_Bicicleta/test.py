class Bicicleta
  def kilometros_recorridos
    @kilometros_recorridos
  end
end

bici = Bicicleta.new

it "Una bicicleta inicializa con 0 kilómetros recorridos" do
  expect(bici.kilometros_recorridos).to eq 0
end

it "Una bicicleta tiene dos ruedas" do
  expect(bici.cantidad_de_ruedas).to eq 2
end

it "Una bicicleta es ligera" do
  expect(bici.ligero?).to be true
end

it "Una bicicleta que se conduce 20 kilómetros y luego 3 kilómetros tiene 23 kilómetros recorridos" do
  bici.conducir!(20)
  expect(bici.kilometros_recorridos).to eq 20
  bici.conducir!(3)
  expect(bici.kilometros_recorridos).to eq 23
end

it "Una bicicleta sigue siendo ligera después de conducirla muchos kilómetros" do
  bici.ligero?
  expect(bici.ligero?).to be true
end