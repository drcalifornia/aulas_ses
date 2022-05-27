import random

if __name__=='__main__':
	marcas = ['Ford', 'Volkswagen', 'Chevrolet', 'Hiundai']
	cores = ['Prata', 'Preto', 'Branco', 'Vermelho']
	anos = [2010, 2012, 2015, 2018, 2019, 2020, 2021, 2022]
	carros = []
	print("Criando carros...")
	for i in range(random.randint(1, 10)):
		print("Carro número {}".format(i))
		carro = {
			'id':i,
			'marca':marcas[random.randint(0, len(marcas)-1)],
			'cor':cores[random.randint(0, len(cores)-1)],
			'ano':anos[random.randint(0, len(anos)-1)]
		}
		carros.append(carro)
	print(carros)