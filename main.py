# print("\033[4mThis text\033[0m")

#20250509
#Depois é uma boa fazer um render dessas linhas ----
#que mude de tamanho conforme se altera o conteúdo da mensagem
#E centralizar o Bem vindo também

titulo = '''
    ------------------------------
       Bem vindo ao Saúde Amiga!
    -------------------------------
    Aperte o número de sua questão.'''

#20250510 -> Inserir conteúdo informacional no lugar da tabela conteúdo
alternativas = {
    0:[["Como faço meu cadastro?",""],["CONTEUDO"]],
    1:[["Como faço meu login?",""],["CONTEUDO"]],
    2:[["Como instalo o portal do HC?",""],["CONTEUDO"]],
    3:[["Como agendo?",""],["CONTEUDO"]],
    4:[["Como cancelo a consulta?",""],["CONTEUDO"]],
    5:[["Esqueci minha senha",""],["CONTEUDO"]],
    6:[["Como reclamar do aplicativo?",""],["CONTEUDO"]],
    7:[["Como vejo meus documentos?",""],["CONTEUDO"]],
    8:[["Como abro minha teleconsulta?"],["CONTEUDO"]],
    9:[["Ver receita"],["CONTEUDO"]],
    10:[["Ver Resultados"],["CONTEUDO"]]
}

historico = [0]
posicao_no_historico = 0

#Tabela de navegação rápida
#Dicionário de exemplo, sujeito e terá alterações
relacao_paginas = {0:[1,2,3], 1:[2,4,6], 4:[4,7,2]}

#Retorna todas as páginas que tem um tema a ver com o tema da página atual
def get_paginas_relacionadas_a_atual(ID_PAGINA_ATUAL):
    for paginas_colunas, paginas_relacionadas in relacao_paginas.items():
        if(paginas_colunas == ID_PAGINA_ATUAL):
            return(paginas_relacionadas)
    return []

def esta_voltando():
    # Procurar por uma ancora
    ancora_posicao = len(historico)
    for posicao in historico:
        ancora_posicao = ancora_posicao-1
        lista_pos_ancora = historico[ancora_posicao+1:]
        lista_pre_ancora = historico[:ancora_posicao]
        lista_pos_ancora.reverse
        if(lista_pre_ancora[-len(lista_pos_ancora):] == lista_pos_ancora):
            return True
    return False

def pegar_conteudo_multiplas_paginas(ids):
    conteudo_colecao = {}
    #20250510 -> Deve ter um jeito mais bonito de fazer essa procura, mas podemos deixar para refatorar depois
    #Talvez o que temos a aprender nessa sprint seja que, em uma corrida, menos é mais (e fiz mais do que menos nesse caso).
    for id in ids:
        for alternativas_ids, conteudos_e_titulo in alternativas.items():
            if alternativas_ids == id:
                conteudo_colecao[id] = conteudos_e_titulo
                break
    return conteudo_colecao

def render_paginas_relacionadas(num_janela):
    print('------------------------') #20250510 -> é uma boa ideia fazer um método para renderizar essas linhas
    print('Paginas Relacionadas') #20250510 -> Deve haver um método que pega as páginas relacionadas da tabela alternativas usando o get_paginas_relacionadas_a_atual() exibindo o titulo e o id 
    id_paginas_relacionadas = get_paginas_relacionadas_a_atual(num_janela)
    paginas_relacionadas_conteudo = pegar_conteudo_multiplas_paginas(id_paginas_relacionadas)
    for id, conjunto in paginas_relacionadas_conteudo.items():
        print(f"Insira {id} para acessar a página {conjunto[[0][0]][0]}\n")
    if id_paginas_relacionadas == []:
        print("Nenhuma página relacionada")

def render_footer_navegacao(num_janela):
    #20250509
    #Adicionar linha para separar da lista de opções
    #Adicionar alternativas de navegação da página (voltar, avançar, caso o usuário já tenha voltado; exibir página home)
    #Adicionar opções para o usuário acessar páginas relacionadas (como elas estão relacionadas?
    # Vai por temas semelhantes e coloca numa lista de relações e depois chamar um método que pega qual 'link' de página deve ser apresentado no footer desta)
    print('------------------------') #20250510 -> é uma boa ideia fazer um método para renderizar essas linhas
    print("Insira 'v' para voltar. ")
    print("Insira 'm' para voltar ao menu inicial. ")
    
    if(esta_voltando()):
        print("Insira 'a' para desfazer o voltar. ")
    

def render_titulo(num_janela):
    print(f'''
          ------------------------
          {alternativas.get(num_janela)[0][0]}
          ------------------------
          ''')

def render_corpo_mensagem(num_janela):
    print(f'''\n{alternativas.get(num_janela)[1][0]}''')

def exibir_informativo(num_janela, ancora, voltar):
   
    #Conteúdo relativo ao número da janela
    render_titulo(num_janela)
    render_corpo_mensagem(num_janela)
    
    #Conteúdo relativo ao footer de navegação
    render_footer_navegacao(num_janela)

    #exibir páginas que tem a ver com a atual janela, fazendo uso de uma tabela de relações
    render_paginas_relacionadas(num_janela)
    selecionar_alternativa(ancora, voltar)

def selecionar_alternativa(ancora, voltar):
    
    #20250510 - todo: Adicionar sistema de navegação (mover para a página selecionada ao apertar as teclas amostradinhas uii assim que eu gosto)
    #20250510 O processo de avançar ou retroceder no histórico deve depender dessa função
    alternativa_selecionada = input()
    #alternativa_selecionada = se for numero -> TABELA alternativas
    #alternativa_selecionada = se for letra -> ALTERAR historico
    #ele não ensinou esse método então n sei se é permitido fazer esse negócio
    if(alternativa_selecionada.isdigit()):
        ancora = 0
        voltar = 0
        alternativa_valor = int(alternativa_selecionada)  
        historico.append(alternativa_valor)
        exibir_informativo(alternativa_valor, ancora, voltar)
    else:
        # Essa parte do condicional aborda se a alternativa inserida é uma string (v, m, a)
        match alternativa_selecionada:
            case 'v':
                #voltar
                #Volta para o penúltimo item do histórico, já dizia Justin Timberlake what goes around comes around
                if(voltar == 0):
                    ancora = len(historico)-1
                voltar += 1
                alternativa_valor = historico[ancora - voltar]
                historico.append(alternativa_valor)
                exibir_informativo(alternativa_valor, ancora, voltar)
            case 'm':
                #menu principal
                render_menu_principal()
            case 'a':
                #todo: verificar se o esta_voltando verifica se o voltar está zerado ou não, se não essa merda vai dar erro
                if(esta_voltando()):
                    voltar -= 1
                    alternativa_valor = historico[ancora - voltar]
                    historico.append(alternativa_valor)
                    exibir_informativo(alternativa_valor, ancora, voltar)
                else:
                    selecionar_alternativa(ancora, voltar)
                #avançar
            case _:
                print("Por favor insira o número da página desejada ou a letra de atalho:")
                selecionar_alternativa(ancora, voltar)
                 

def render_menu_principal():
    ancora = 0
    voltar = 0
    print(titulo)
    for n, conteudo in alternativas.items():
        print(f"{n}...{conteudo[0][0]}")
    selecionar_alternativa(ancora, voltar)

def main():
    render_menu_principal()

if(__name__ == '__main__'):
    main()
