import ast
materias = ["História", "Física"]
alunos = {}
nomes_alunos = alunos.keys()
qtd_aluno = len(nomes_alunos)

def menu():
    opcao = input('''
.......................................................
                         3º DS
Menu
[1] Cadastrar Aluno.
[2] Listar Alunos.
[3] Criar/Recriar HTML.
[4] Sair.
.......................................................                   
Escolha uma opção acima: ''')
    
    if opcao == "1":
        cadastrarAluno()
    elif opcao == "2":
        listaSala()
    elif opcao == "3":
        refresh()
    elif opcao =='4':
        sair()
    else:
        while opcao not in ("1", "2", "3", "4"):
            print ("Erro! Tente novamente.")
            menu()


def cadastrarAluno():
    print("Cadastrar Aluno")
    # Declarando listas.
    notas = []
    aluno = []

    # Pegando os alunos já arquivados no txt (para modificação ou exclusão).
    with open("lista.txt", "r", encoding="utf-8") as arquivo:
        lista_notas_anterior = arquivo.read()

    if lista_notas_anterior:
        alunos = ast.literal_eval(lista_notas_anterior)
    else:
        alunos = {}

    # Pedindo o nome do aluno
    nome = (input("Informe o nome do aluno: "))

    # Recebendo as notas das matérias um de cada vez.
    for a in range (len(materias)):
        # Recebendo as notas do bimestre e calculando a média.
        for b in range (4):
            notas.append(float(input(f"Informe a nota do {b+1}º bimestre em {materias[a]}: ")))
            media = sum(notas)/4

        # Juntando a média com as notas do bimestre, armazenando os dados na lista "aluno" e apagando o conteúdo de "notas" para receber as notas da próxima matéria
        notas.append(media)
        aluno.append(notas)
        notas = []

    # Armazenando todas as notas do aluno dentro de um dicionário.
    alunos[nome] = aluno

    # Armazenando o aluno e suas notas no arquivo txt.
    with open ("lista.txt","w", encoding="utf-8") as arquivo:
        arquivo.write(f'{alunos}')

def listaSala():
    with open('lista.txt', 'r') as a:
         alunos_arq = a.read()
    if alunos_arq:
        alunos = ast.literal_eval(alunos_arq)
    else:
        alunos = {}
    
    sala = list(alunos.items())
    for aluno in sala:
        bim = slice(0, 4)
        print(f"Aluno(a) {aluno[0]}:\n{materias[0]}: {aluno[1][0][bim]}   Média = {aluno[1][0][4]}\n{materias[1]}: {aluno[1][1][bim]}   Média = {aluno[1][1][4]}\n")

def refresh():
    with open("lista.txt", "r", encoding="utf-8") as arquivo:
        lista_notas_anterior = arquivo.read()

    if lista_notas_anterior:
        alunos = ast.literal_eval(lista_notas_anterior)
        print("ENTREI A")
    else:
        alunos = {}
        print("ENTREI B")
    print(f"CONTEUDO as  {alunos}")
    criar_html(alunos)

def criar_html(alunos_):
    try:
        with open("lista.txt", "r",  encoding="utf-8") as arq:
            texto = arq.read()

        boletim = ast.literal_eval(texto)
    except:
        with open("lista.txt", "w", encoding="utf-8") as arq:
            arq.write("")
    pagina = open("boletim.html", "w", encoding="utf-8")
    pagina.write("""
            <!DOCTYPE html>
            <html lang="pt-br">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, intial-scale=1.0">
                    <title> Notas Aluno TESTE </title>
                    <style rel="stylesheet">
                    table, th, td{
                        border: solid;
                        border-collapse: collapse;
                        border-color: pink;
                        border-radius: 0;
                    }
                    </style>
                </head>
                <body>
    """)

    pagina.write("<table>")
    print(f"CONTEUDO {alunos}")
    for nome_aluno in (alunos.keys()):
        pagina.write(f"""
                <tr>
                    <td colspan="6" style="text-align: center">{nome_aluno}</td>
                </tr>
                <tr>
                    <th> Matéria </th>
                    <th> 1º Bimestre </th>
                    <th> 2º Bimestre </th>
                    <th> 3º Bimestre </th>
                    <th> 4º Bimestre</th>
                    <th> Média </th>
                </tr>
            """)

        for aluno, notas in alunos.items():
            for b in range(len(materias)):
                pagina.append(f"""
                    <tr>
                        <td> {materias[b]}</td>
                        <td> {notas[b][0]}</td>
                        <td> {notas[b][1]}</td>
                        <td> {notas[b][2]}</td>
                        <td> {notas[b][3]}</td>
                        <td> {notas[b][4]}</td>
                    </tr>
                """)

        pagina.write(f"""
                </table>
                </body>
            </html>
        """)
    

def sair():
    print(f'Até a próxima!')
    exit()      

def main():
    menu()

main()