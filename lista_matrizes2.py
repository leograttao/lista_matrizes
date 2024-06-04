def cadastro():
    cliente = []

    while True:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        renda_mensal = float(input("Renda Mensal: "))
        
        pessoa = [nome, cpf, idade, renda_mensal]
        cliente.append(pessoa)
        
        continuar = input("Deseja cadastrar mais uma pessoa? (s/n): ")
        
        if continuar == "s":
            continue
        elif continuar == "n":
            break
    
    return cliente

def imprimirCliente(cliente):
    for pessoa in cliente:
        print(f"Nome: {pessoa[0]}, CPF: {pessoa[1]}, Idade: {pessoa[2]}, Renda Mensal: {pessoa[3]}")
    
def calcularMedias(cliente):
    total_idade = 0
    total_renda = 0.0
    
    for pessoa in cliente:
        total_idade += pessoa[2]
        total_renda += pessoa[3]
    
    media_idade = total_idade / len(cliente)
    media_renda = total_renda / len(cliente)
    
    return media_idade, media_renda

cliente = cadastro()
print("\nPessoas cadastradas:")
imprimirCliente(cliente)

media_idade, media_renda = calcularMedias(cliente)
print(f"\nMédia de Idade: {media_idade:.2f}")
print(f"Média de Renda Mensal: {media_renda:.2f}")