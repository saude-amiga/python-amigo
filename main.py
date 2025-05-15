titulo = '''
    ------------------------------
       Bem vindo ao Saúde Amiga!
    -------------------------------
    Aperte o número de sua questão.'''

alternativas = {
    0: [["Como faço meu cadastro?", ""], ["Para se cadastrar, acesse o aplicativo ou site do Saúde Amiga, clique em 'Cadastrar', preencha seus dados pessoais e siga as instruções na tela."]],
    1: [["Como faço meu login?", ""], ["Para fazer login, informe seu CPF e senha cadastrados na tela inicial do aplicativo ou site do Saúde Amiga."]],
    2: [["Como instalo o portal do HC?", ""], ["Você pode instalar o portal do HC baixando o aplicativo na loja do seu celular (Google Play ou App Store) ou acessando o site oficial pelo navegador."]],
    3: [["Como agendo?", ""], ["Para agendar uma consulta, acesse o menu 'Agendamentos', escolha o serviço desejado, selecione a data e horário disponíveis e confirme a marcação."]],
    4: [["Como cancelo a consulta?", ""], ["Para cancelar uma consulta, vá até 'Meus Agendamentos', selecione a consulta que deseja cancelar e clique em 'Cancelar'. Confirme a operação para finalizar."]],
    5: [["Esqueci minha senha", ""], ["Na tela de login, clique em 'Esqueci minha senha' e siga as instruções para redefinir sua senha usando seu e-mail ou telefone cadastrado."]],
    6: [["Como reclamar do aplicativo?", ""], ["Para registrar uma reclamação, acesse o menu 'Ajuda' ou 'Fale Conosco' no aplicativo e envie sua mensagem detalhando o problema encontrado."]],
    7: [["Como vejo meus documentos?", ""], ["Seus documentos estão disponíveis na área 'Meus Documentos' do aplicativo. Basta acessar o menu e selecionar a opção correspondente."]],
    8: [["Como abro minha teleconsulta?"], ["No horário agendado, acesse 'Meus Agendamentos', selecione a teleconsulta e clique em 'Iniciar Consulta' para entrar na sala virtual."]],
    9: [["Ver receita"], ["Para visualizar sua receita, acesse 'Minhas Receitas' no menu principal e selecione a receita desejada para abrir os detalhes."]],
    10: [["Ver Resultados"], ["Seus resultados de exames estão disponíveis em 'Meus Resultados'. Basta acessar o menu e escolher o exame para visualizar o resultado."]]
}

historico = [0]
posicao_no_historico = 0
relacao_paginas = {
    0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Cadastro: relacionado a login, instalação, agendamento, etc.
    1: [0, 5],                           # Login: relacionado a cadastro e esqueci minha senha
    2: [0, 3],                           # Instalar portal: relacionado a cadastro e agendamento
    3: [0, 2, 4, 8],                     # Agendar: relacionado a cadastro, instalação, cancelar, teleconsulta
    4: [3],                              # Cancelar consulta: relacionado a agendamento
    5: [1],                              # Esqueci senha: relacionado a login
    6: [],                               # Reclamar: sem relação direta
    7: [9, 10],                          # Ver documentos: relacionado a receitas e resultados
    8: [3],                              # Teleconsulta: relacionado a agendamento
    9: [7],                              # Ver receita: relacionado a documentos
    10: [7]                              # Ver resultados: relacionado a documentos
}

def get_paginas_relacionadas_a_atual(ID_PAGINA_ATUAL):
    for paginas_colunas, paginas_relacionadas in relacao_paginas.items():
        if(paginas_colunas == ID_PAGINA_ATUAL):
            return(paginas_relacionadas)
    return []

def esta_voltando():
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
    for id in ids:
        for alternativas_ids, conteudos_e_titulo in alternativas.items():
            if alternativas_ids == id:
                conteudo_colecao[id] = conteudos_e_titulo
                break
    return conteudo_colecao

def render_paginas_relacionadas(num_janela):
    print('------------------------') 
    print('Paginas Relacionadas') 
    id_paginas_relacionadas = get_paginas_relacionadas_a_atual(num_janela)
    paginas_relacionadas_conteudo = pegar_conteudo_multiplas_paginas(id_paginas_relacionadas)
    for id, conjunto in paginas_relacionadas_conteudo.items():
        print(f"Insira {id} para acessar a página {conjunto[[0][0]][0]}\n")
    if id_paginas_relacionadas == []:
        print("Nenhuma página relacionada")

def render_footer_navegacao(num_janela):
    print('------------------------') 
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
    render_titulo(num_janela)
    render_corpo_mensagem(num_janela)
    render_footer_navegacao(num_janela)
    render_paginas_relacionadas(num_janela)
    selecionar_alternativa(ancora, voltar)

def selecionar_alternativa(ancora, voltar):
    alternativa_selecionada = input()
    if(alternativa_selecionada.isdigit()):
        ancora = 0
        voltar = 0
        alternativa_valor = int(alternativa_selecionada)  
        historico.append(alternativa_valor)
        exibir_informativo(alternativa_valor, ancora, voltar)
    else:
        match alternativa_selecionada:
            case 'v':
                if(voltar == 0):
                    ancora = len(historico)-1
                voltar += 1
                alternativa_valor = historico[ancora - voltar]
                historico.append(alternativa_valor)
                exibir_informativo(alternativa_valor, ancora, voltar)
            case 'm':
                render_menu_principal()
            case 'a':
                if(esta_voltando()):
                    voltar -= 1
                    alternativa_valor = historico[ancora - voltar]
                    historico.append(alternativa_valor)
                    exibir_informativo(alternativa_valor, ancora, voltar)
                else:
                    selecionar_alternativa(ancora, voltar)
            case _:
                print("Por favor insira o número da página desejada ou a letra de atalho (minúscula):")
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
