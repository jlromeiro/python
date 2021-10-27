with open('emails.txt', 'r') as arquivo:
    listaDic = {'nome': ' ', 'email': ' '}
    linhas = arquivo.readlines()
    # print(linhas)
    a = linhas.__len__()
    print(a)
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
