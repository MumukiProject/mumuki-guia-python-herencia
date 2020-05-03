class Auto
  def litros
    @litros
  end
end

auto = Auto.new

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