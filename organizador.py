with open("clientes.txt", "r") as arquivo:
    clientes = []

    for v in arquivo:
        dados = {}
        pessoas = v.split(",")
        for i, n in enumerate(pessoas):
            match i:
                case 0:
                    dados['nome'] = n.capitalize()
                case 1:
                    dados['idade'] = n
                case 2:
                    dados['cidade'] = n.rstrip().title()

        clientes.append(dados.copy())    
        
    clientes_ordenados = sorted(clientes, key=lambda obj: obj["nome"])
    
            
with open('clientes_ordenados.txt', 'w') as arquivo2:
    arquivo2.write('Nome     |     Idade     |     Cidade\n')
    for i, l in enumerate(clientes_ordenados):
        for k, v in l.items():
            match k:
                case 'nome':
                    arquivo2.write(f'{v:<9} ')
                case 'idade':
                    arquivo2.write(f'{v:^15} ')
                case 'cidade':
                    arquivo2.write(f'{v:<11}\n')

    print(f'Foram registrados {i+1} clientes!')            
