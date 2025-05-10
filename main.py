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

ALTERNATIVAS = {
    0:["Como faço meu cadastro?",""],
    1:["Como faço meu login?",""],
    2:["Como instalo o portal do HC?",""],
    3:["Como agendo?",""],
    4:["Como cancelo a consulta?",""],
    5:["Esqueci minha senha",""],
    6:["Como reclamar do aplicativo?",""],
    7:["Como vejo meus documentos?",""],
    8:["Como abro minha teleconsulta?"],
    9:["Ver receita"],
    10:["Ver Resultados"]
}
HISTORICO = [0]
POSICAO_NO_HISTORICO = 0


def render_footer_navegacao():
    #20250509
    #Adicionar linha para separar da lista de opções
    #Adicionar alternativas de navegação da página (voltar, avançar, caso o usuário já tenha voltado; exibir página home)
    #Adicionar opções para o usuário acessar páginas relacionadas (como elas estão relacionadas?
    # Vai por temas semelhantes e coloca numa lista de relações e depois chamar um método que pega qual 'link' de página deve ser apresentado no footer desta)
def exibir_informativo(num_janela):
    print()
    render_footer_navegacao()

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



