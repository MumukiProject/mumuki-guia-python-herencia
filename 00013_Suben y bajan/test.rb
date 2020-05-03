class Micro
  def litros
    @litros
  end
  
  def pasajeros
    @pasajeros
  end
  
  def diez_pasajeros
    @pasajeros = 10
  end
end

micro = Micro.new

it "Un micro inicializa con 100 litros" do
  expect(micro.litros).to eq 100
end

it "Un micro inicializa con 0 pasajeros" do
  expect(micro.pasajeros).to eq 0
end

it "Un micro tiene seis ruedas" do
  expect(micro.cantidad_de_ruedas).to eq 6
end

it "Un micro es ligero cuando no tiene pasajeros" do
  expect(micro.ligero?).to be true
end

it "Si en un micro suben siete pasajeros y bajan tres quedan cuatro pasajeros" do
  7. times { micro.sube_pasajero! }
  expect(micro.pasajeros).to eq 7
  3. times { micro.baja_pasajero! }
  expect(micro.pasajeros).to eq 4
end

it "Un micro no es ligero cuando tiene pasajeros" do
  micro.diez_pasajeros
  expect(micro.ligero?).to be false
end

it "Un micro gasta 0.2 litros por cada kilómetro que se lo conduce" do
  micro.conducir!(20)
  expect(micro.litros).to eq (100 - (20 * 0.2))
end