# print("\033[4mThis text\033[0m")

TITULO = '''
    -------------------------
    Bem vindo ao Saúde Amiga!
    -------------------------'''

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
HISTORICO = []
POSICAO_NO_HISTORICO = 0

def render_menu_principal():
    print(TITULO)
    for n, conteudo in ALTERNATIVAS.items():
        print(f"{n}...{conteudo[0]}")
    #print(FOOTER)

def main():
    render_menu_principal()

if(__name__ == '__main__'):
    main()



