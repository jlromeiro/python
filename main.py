# passo 1

# arquivo = open('emails.txt', 'r')
# print(arquivo.read())

# passo 2
# arquivo = open('emails.txt', 'r')
# lines = arquivo.read()
# print(lines)

# passo 3
# arquivo = open('emails.txt', 'r')
# lines = arquivo.readlines()

# for line in lines:
#     print(line)

# passo 4
# arquivo = open('emails.txt', 'r')
# lines = arquivo.readlines()

# for line in lines:
#     nome = line.split('@')[0]
#     email = line
#     print(nome, email)


# passo 5
# arquivo = open('emails.txt', 'r')
# lines = arquivo.readlines()

# lista_de_emails = {}

# for line in lines:
#     nome = line.split('@')[0]
#     email = line
#     item = f"nome: {nome}, email: {email}"
#     print(item)



# passo 6
# arquivo = open('emails.txt', 'r')
# lines = arquivo.readlines()

# lista_de_emails = {}

# for i, line in enumerate(lines):
#     nome = line.split('@')[0]
#     email = line
#     item = f"nome: {nome}, email: {email}"
#     print(i, item)

# passo 7
arquivo = open('emails.txt', 'r')
lines = arquivo.readlines()

lista_de_emails = {}

for i, line in enumerate(lines):
    nome = line.split('@')[0]
    email = line
    item = f"nome: {nome}, email: {email}"
    lista_de_emails[i] = "{" + item + "}"

print(lista_de_emails)


# with open('emails.txt', 'r') as arquivo:
#     listaDic = {'nome': ' ', 'email': ' '}
#     emailss = arquivo.readlines()

#     a = 0
#     b = 0
#     for x in range(1, 10):
#         nome = emailss.split('@')
#         #listaDic['nome'] = nome[0]
#         #listaDic['email'] = nome[2]
#        # print(nome)
#         # print(email)
#         # print(linhas)
#         #a = linhas.__len__()
#         print(nome)
#         print()

# arquivo.close()


"""
Tarefa:
Na raiz do projeto, existe um arquivo chamado emails.txt, faça um programa que:
- leia este arquivo,
- tranforme essa lista de emails em um dicionário com chave valor, como exemplo abaixo:

pegar um email, exemplo a_vanessinha_1990@hotmail.com

{
    nome:"a_vanessinha_1990",
    email:"a_vanessinha_1990@hotmail.com"
}

- e por fim, retornar este objeto 

"""
