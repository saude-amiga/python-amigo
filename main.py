# print("\033[4mThis text\033[0m")

#20250509
#Depois é uma boa fazer um render dessas linhas ----
#que mude de tamanho conforme se altera o conteúdo da mensagem
#E centralizar o Bem vindo também

TITULO = '''
    ------------------------------
       Bem vindo ao Saúde Amiga!
    -------------------------------
    Aperte o número de sua questão.'''

#20250510 -> Inserir conteúdo informacional no lugar da tabela conteúdo
ALTERNATIVAS = {
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

HISTORICO = [0]
POSICAO_NO_HISTORICO = 0

#Tabela de navegação rápida
#Dicionário de exemplo, sujeito e terá alterações
RELACAO_PAGINAS = {0:[1,2,3], 1:[2,4,6], 4:[4,7,2]}


#Retorna todas as páginas que tem um tema a ver com o tema da página atual
def get_paginas_relacionadas_a_atual(ID_PAGINA_ATUAL):
    for PAGINAS_COLUNAS, PAGINAS_RELACIONADAS in RELACAO_PAGINAS:
        if(PAGINAS_COLUNAS == ID_PAGINA_ATUAL):
            return(PAGINAS_RELACIONADAS)

def esta_voltando():
    CAMINHO_ATE_AQUI = []
    #todo: Refatorar, talvez esse método ainda não funcione tão bem
    TEM_PONTO_ANCORA = False

    #Adiciona o último item do histório
    CONTADOR = 1
    CAMINHO_ATE_AQUI.append(HISTORICO[len(HISTORICO)-CONTADOR])

    #Adiciona o penúltimo item do histório
    CONTADOR += 1
    CAMINHO_ATE_AQUI.append(HISTORICO[len(HISTORICO)-CONTADOR])

    while(len(HISTORICO) != CONTADOR):
        CONTADOR += 1
        CAMINHO_ATE_AQUI.append(HISTORICO[len(HISTORICO)-CONTADOR])

        #Compara o último item encontrado com o antipenúltimo
        if(CAMINHO_ATE_AQUI[len(CAMINHO_ATE_AQUI)-1] == CAMINHO_ATE_AQUI[len(CAMINHO_ATE_AQUI)-3]):
            #Se verdadeiro, o penúltimo item é o item âncora, e devemos ver se é possível fazer o caminho até a âncora a partir da âncora
            CAMINHO_ATE_AQUI.pop()
            #Se de fato o usuário estiver voltando, caminho até aqui deve ser igual a um caminho pré âncora.
            CAMINHO_PRE_ANCORA = HISTORICO[:-len(CAMINHO_ATE_AQUI)]
            ANCORA = CAMINHO_ATE_AQUI.pop()
            #Agora caminho até aqui tem apenas o caminho até o item âncora
            CAMINHO_ATE_AQUI.reverse()
            #Agora basta verificar se o caminho até aqui está presente na ponta no CAMINHO_PRE_ANCORA
            if(CAMINHO_PRE_ANCORA[-len(CAMINHO_ATE_AQUI):] == CAMINHO_ATE_AQUI):
                return True
    # CAMINHO ATE AQUI.APPEND
    # THEN LEN(HISTORICO)-2
    # IF LEN(HISTORICO)-3 == LEN(HISTORICO)-1 
    # PONTO ANCORA DETECTADO
    # PARA O LOOP, 
    # CONSEGUE INVERTER O CAMINHO ATE AQUI?
    #     SIM - PODE LIBERAR A FUNCAO DE VOLTAR
    #     RETURN TRUE
    #     NAO - N PODE LIBERAR A FUNCAO DE VOLTAR
    # AND SO ON AND SO ON
    return False

def pegar_conteudo_multiplas_paginas(ids):
    conteudo_colecao = {}
    #20250510 -> Deve ter um jeito mais bonito de fazer essa procura, mas podemos deixar para refatorar depois
    #Talvez o que temos a aprender nessa sprint seja que, em uma corrida, menos é mais (e fiz mais do que menos nesse caso).
    for id in ids:
        for alternativas_ids, conteudos_e_titulo in ALTERNATIVAS.items():
            if alternativas_ids == id:
                conteudo_colecao[id] = conteudos_e_titulo
                break
    return conteudo_colecao

def render_paginas_relacionadas(num_janela):
    print('------------------------') #20250510 -> é uma boa ideia fazer um método para renderizar essas linhas
    print('Paginas Relacionadas') #20250510 -> Deve haver um método que pega as páginas relacionadas da tabela alternativas usando o get_paginas_relacionadas_a_atual() exibindo o titulo e o id 
    ID_PAGINAS_RELACIONADAS = get_paginas_relacionadas_a_atual(num_janela)
    paginas_relacionadas_conteudo = pegar_conteudo_multiplas_paginas(ID_PAGINAS_RELACIONADAS)
    for id, conjunto in paginas_relacionadas_conteudo:
        print(f"Insira {id} para acessar a página {conjunto[[0][0]]}\n")

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
        print("Insira 'a' para avançar. ")
    #20250510 - todo: Adicionar sistema de navegação (mover para a página selecionada ao apertar as teclas amostradinhas uii assim que eu gosto)
    

def render_titulo(num_janela):
    print(f'''
          ------------------------
          {ALTERNATIVAS.get(num_janela)[0][0]}
          ------------------------
          ''')

def render_corpo_mensagem(num_janela):
    print(f'''\n{ALTERNATIVAS.get(num_janela)[1][0]}''')

def exibir_informativo(num_janela):
    #Conteúdo relativo ao número da janela
    render_titulo(num_janela)
    render_corpo_mensagem(num_janela)
    
    #Conteúdo relativo ao footer de navegação
    render_footer_navegacao()

    #exibir páginas que tem a ver com a atual janela, fazendo uso de uma tabela de relações
    render_paginas_relacionadas(num_janela)
    selecionar_alternativa()

def selecionar_alternativa():
    #20250510 O processo de avançar ou retroceder no histórico deve depender dessa função
    alternativa_selecionada = int(input())
    HISTORICO.append(alternativa_selecionada)
    exibir_informativo(alternativa_selecionada)

def render_menu_principal():
    print(TITULO)
    for n, conteudo in ALTERNATIVAS.items():
        print(f"{n}...{conteudo[0]}")
    #print(FOOTER)

def main():
    render_menu_principal()

if(__name__ == '__main__'):
    main()



