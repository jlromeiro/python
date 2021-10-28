with open('emails.txt', 'r') as arquivo:
    listaDic = {'nome': ' ', 'email': ' '}
    emailss = arquivo.readlines()

    a = 0
    b = 0
    for x in range(1, 10):
        nome = emailss.split('@')
        #listaDic['nome'] = nome[0]
        #listaDic['email'] = nome[2]
       # print(nome)
        # print(email)
        # print(linhas)
        #a = linhas.__len__()
        print(nome)
        print()

arquivo.close()


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
