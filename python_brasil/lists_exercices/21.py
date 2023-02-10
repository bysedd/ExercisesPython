"""
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
VECTRA etc). Carregue outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros
faz com um litro de combustível. Calcule e mostre:

    a. O modelo do carro mais econômico;
    b. Quantos litros de combustível cada um dos carros cadastrados consome para
        percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,
        25 o litro. Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais próxima possível ao
        exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

    Comparativo de Consumo de Combustível

    Veículo 1
    Nome: fusca
    Km por litro: 7
    Veículo 2
    Nome: gol
    Km por litro: 10
    Veículo 3
    Nome: uno
    Km por litro: 12.5
    Veículo 4
    Nome: Vectra
    Km por litro: 9
    Veículo 5
    Nome: Peugeot
    Km por litro: 14.5

    Relatório Final
    1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
    2 - gol             -   10.0 -  100.0 litros - R$ 225.00
    3 - uno             -   12.5 -   80.0 litros - R$ 180.00
    4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
    5 - peugeot        -   14.5 -   69.0 litros - R$ 155.17
    O menor consumo é do peugeot.
"""

vehicles = []

for vehicle in range(5):
    print(f"Vehicle {vehicle + 1}")
    nome = input("Name: ").capitalize().strip()
    kml = float(input("Kilometer per liter: "))
    vehicles.append({"nome": nome, "kml": kml})

print("\nFinal Report")
for i, vehicle in enumerate(vehicles):
    liters_total = 1000 / vehicle["kml"]
    total_price = liters_total * 2.25
    print(
        f"{i + 1} - {vehicle['nome']:<15} - {vehicle['kml']:>6} - "
        f"{round(liters_total, 1):>6} liters - ${total_price:.2f}"
    )

reduced_consumption = max(vehicles, key=lambda v: v["kml"])
print(f"The lowest consumption is the {reduced_consumption['nome']}.")
