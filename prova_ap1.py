# Você é responsável por desenvolver um sistema simples de controle de notas de alunos. 
# O sistema deve permitir que o professor insira as notas (3 notas) dos alunos e, ao final, 
# exiba a situação de cada um deles (Aprovado, Recuperação ou Reprovado) com base nas regras a seguir:
# •	Média maior ou igual a 7: Aprovado
# •	Média entre 5 e 6.9: Recuperação
# •	Média abaixo de 5: Reprovado
alunos = {
    'jose': [10.0, 3.7, 9.5],
    'luis': [10.0, 4.7, 10.0],
    'joao': [10.0, 3.0, 4.0],
    'joana': [10.0, 5.0, 7.0],
    'lucia': [9.0, 5.5, 6.4],
    'vitor': [8.0, 3.0, 1.0],
    'marcelo': [3.0, 4.0, 7.5],
    'bruno': [8.0, 6.0, 7.5],
    }
# Usando for loop em cada item do dicionario aluno acima:
# 1 - (1.5) Calcular a média de cada aluno.   
# 2 - (1.5) Verificar a situação de cada aluno com base nas regras descritas e exiba a descricao.
for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    
    if media >= 7:
        situacao = "Aprovado"
    elif 5 <= media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    print(f"{aluno.capitalize()} - Média: {media:.2f} - Situação: {situacao}")

# Você deve desenvolver um sistema para uma loja virtual que armazena e processa pedidos de produtos. 
# A loja tem um catálogo de produtos com nome e preço.
precos = {
    'camiseta': 100.00,
    'tenis': 900.00,
    'meia': 45.00,
    'blusa': 245.00,
    'calça': 145.00,
    'luva': 18.00,
    }
# O Sistema no final do dia tem o nome e os items comprados por pessoa
compras ={
    'matheu': ['camiseta', 'luva'],
    'luiza': ['tenis'],
    'amanda': ['tenis', 'camiseta'],
    'hugo': ['blusa', 'meia', 'calça'],
    'alexandre': ['blusa', 'meia', 'calça', 'tenis'],
}
# 3 - (1.5) Usando o for loop no dicionario de compras, calcule o valor total da compra de cada comprador.
for comprador, itens in compras.items():
    total = sum(precos[item] for item in itens)
    print(f"{comprador.capitalize()} - Total da compra: R${total:.2f}")


# 4 - (1.5) Ao final, o sistema deve aplicar um desconto com base no valor total da compra e exibir qual foi o desconto e o valor final.
# Compras maiores que 1.000 tem desconto de 10%
# Compras entre 500 e 1.000 tem desconto de 5%
# Compras abaixo de 500, Sem Desconto
for comprador, itens in compras.items():
    total = sum(precos[item] for item in itens)
    
    if total > 1000:
        desconto = total * 0.10
    elif total >= 500:
        desconto = total * 0.05
    else:
        desconto = 0
    
    valor_final = total - desconto
    print(f"{comprador.capitalize()} - Valor total: R${total:.2f}, Desconto: R${desconto:.2f}, Valor final: R${valor_final:.2f}")


# Você foi contratado para desenvolver um sistema de gerenciamento de estoque para uma pequena loja. 
# O estoque esta com as seguintes quantidades definidas por produto.
estoque = {
    'camiseta': 1000,
    'tenis': 500,
    'meia': 2000,
    'blusa': 20,
    'calça': 15,
    'luva': 18,
    }
# 5 - (1.0) Faça um programa que receba do usuário através de um input, um cadastro de um novo produto (chapeu)
# Cadastre esse produto com um novo item do dicionario estoque.
produto_novo = input("chapeu:")
quantidade_nova = int(input(f"Digite a quantidade de {produto_novo}: "))
estoque[produto_novo] = quantidade_nova
print(f"Produto {produto_novo} cadastrado com sucesso! Quantidade: {quantidade_nova}")


# 6 - (1.0) Faça um programa que receba do usuário através de um input, a compra de um produto (camiseta)
# Compra realizada de 800 camisetas
# Atualize o estoque e mostre a quantidade que restou
produto_comprado = 'camiseta'
quantidade_comprada = 800
if estoque[produto_comprado] >= quantidade_comprada:
    estoque[produto_comprado] -= quantidade_comprada
    print(f"Compra realizada. Restam {estoque[produto_comprado]} {produto_comprado}(s) no estoque.")
else:
    print("Estoque insuficiente!")





# 7 - (1.0) Faça um programa que receba do usuário através de um input, a compra de um produto (luva)
# Compra realizada de 20 luva
# Atualize o estoque e mostre a quantidade que restou e se nao tiver o estoque suficiente avise 
produto_comprado = 'luva'
quantidade_comprada = 20
if estoque[produto_comprado] >= quantidade_comprada:
    estoque[produto_comprado] -= quantidade_comprada
    print(f"Compra realizada. Restam {estoque[produto_comprado]} {produto_comprado}(s) no estoque.")
else:
    print(f"Estoque insuficiente! Restam apenas {estoque[produto_comprado]} {produto_comprado}(s).")





# 8 - (1.0) Faça um programa que receba do usuário através de um input, de uma atualizacao de um produto (chapeu)
# Atualizar o estoque com o novo abastecimento
# Abastecimento do estoque de chapeu em 100 unidades





# 9 - (1.5) Crie um pacote com o nome "pacote_auxiliar" e um modulo com o nome modulo.
# Coloque dentro desse pacote uma funcão: 
# nome da funcao: calcular_media
# parametros de entrada: 4 numeros float
# parametro de saida: media desses quatros numeros
# Importe a funcao e execute ela aqui com os seguintes numeros (9.3, 10.6, 348.9, 1000.99)
# Mostre o resultado da chamada da funcao

from pacote_auxiliar.modulo import calcular_media
media = calcular_media(9.3, 10.6, 348.9, 1000.99)
print(f"Média calculada: {media:.2f}")




# 10 - (1.5) Subir o repositorio corretamente no Github.