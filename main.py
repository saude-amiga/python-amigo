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


def render_footer_navegacao():
    #20250509
    #Adicionar linha para separar da lista de opções
    #Adicionar alternativas de navegação da página (voltar, avançar, caso o usuário já tenha voltado; exibir página home)
    #Adicionar opções para o usuário acessar páginas relacionadas (como elas estão relacionadas?
    # Vai por temas semelhantes e coloca numa lista de relações e depois chamar um método que pega qual 'link' de página deve ser apresentado no footer desta)

def render_titulo(num_janela):
    print(f'''
          ------------------------
          {ALTERNATIVAS.get(num_janela)[0]}
          ------------------------
          ''')

def render_corpo_mensagem(num_janela):
    print(f'''''')

def exibir_informativo(num_janela):
    #Conteúdo relativo ao número da janela
    render_titulo(num_janela)
    render_corpo_mensagem(num_janela)
    
    #Conteúdo relativo ao footer de navegação
    render_footer_navegacao()

    #exibir páginas que tem a ver com a atual janela, fazendo uso de uma tabela de relações
    render_paginas_relacionadas(num_janela)

def selecionar_alternativa():
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



