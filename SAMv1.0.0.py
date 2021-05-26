# Importações de funções

from tkinter import Tk, Label, Button, Entry, font, StringVar, OptionMenu
from shutil import move
from getpass import getuser
from random import shuffle
from functools import partial


# Função para criação do documento de texto e importação para área de trabalho


def bt_click():
    global lb5, lb6, lb7, bt_fim, d, a, sup, v

    sup = v.get()

    try:
        a = 'Atendimento ' + ed1.get() + '.txt'
        arquivo = open(a, 'w+')
        arquivo.close()
    except:
        lb5 = Label(janela, text='\nHouve uma falha na criação do arquivo!')
        lb5.grid(row=10, column=2, sticky='W')
    else:
        lb5 = Label(janela, text='\nArquivo criado com sucesso!')
        lb5.grid(row=10, column=2, sticky='W')
        try:
            arquivo = open(a, 'at')
            arquivo.write(f'Atendente: {ed1.get()} ; Supervisor: {sup}')
            arquivo.close()
        except:
            lb7 = Label(janela, text='Houve uma falha ao passar informações para o arquivo!')
            lb7.grid(row=11, column=2, sticky='W')
        else:
            lb7 = Label(janela, text='Informações incluídas com sucesso!')
            lb7.grid(row=11, column=2, sticky='W')
            lb6 = Label(janela)
            lb_a['text'] = '\n\n\nVendedor: ' + ed1.get()
            lb_b['text'] = 'Supervisor : ' + sup
            bt0.destroy()
            ed1.destroy()
            supervisores.destroy()
            bt_fim = Button(janela, text='Iniciar Avaliação', command=bt_fim_click)
            bt_fim.grid(row=8, column=2, sticky='W')


# Função para randomizar as questões e apresentá-las na interface


def bt_fim_click():
    global quests, lb5, lb6, lb7, bt_a, bt_b, bt_c, bt_d, resposta, cond, lb_save, cond_quest, bt_save, lb_intruções1, \
        lb_intruções2, lb_intruções3, lb_b

    lb_title.grid(columnspan=2)
    lb_save['text'] = ''
    bt_save.grid_remove()

    if len(quests) != 0:
        if len(quests) == 10:
            lb_confirmar = Label(janela, height=2)
            lb_confirmar.grid(row=16)
            lb_intruções1 = Label(janela,
                                  text='\n\nInstruções: 1 - Clique na letra correspondente a opção escolhida',
                                  font=font_texto)
            lb_intruções1.grid(row=17, column=2, sticky='W')
            lb_intruções2 = Label(janela, text=' ' * 20 + '2 - Clique no botão "Confirmar"', font=font_texto)
            lb_intruções2.grid(row=18, column=2, sticky='W')
            lb_intruções3 = Label(janela, text=' ' * 20 + '3 - Clique no botão "Próxima Questão"', font=font_texto)
            lb_intruções3.grid(row=19, column=2, sticky='W')
            lb5.destroy()
            lb6.destroy()
            lb7.destroy()
            bt_a = Button(janela, text='A')
            bt_a['command'] = partial(status_bt, bt_a)
            bt_a.grid(row=3, column=2, sticky='W')
            bt_b = Button(janela, text='B')
            bt_b['command'] = partial(status_bt, bt_b)
            bt_b.grid(row=6, column=2, sticky='W')
            bt_c = Button(janela, text='C')
            bt_c['command'] = partial(status_bt, bt_c)
            bt_c.grid(row=7, column=2, sticky='W')
            lb_c['font'] = font_texto
            lb_c['height'] = '5'
            lb_c.grid(row=7, column=2, sticky='W')
            lb_d.grid(row=8, column=2, sticky='W')
            lb_d['height'] = '1'
            bt_d = Button(janela, text='D')
            bt_d['command'] = partial(status_bt, bt_d)
            bt_d.grid(row=8, column=2, sticky='W')
            lb_fim['height'] = '2'
            bt_fim['text'] = 'Confirmar'
            bt_fim['command'] = próxima_questão
            lb2 = Label(janela, height=2)
            lb2.grid(row=13, column=2)
            bt_fim.grid(row=14, column=2, sticky='E')
            lb_fim.grid(row=14, column=2)

        cond = quests[0]
        cond_quest = quests[0]
        lb_fim['text'] = 'A opção escolhida foi: '
        lb_save['text'] = ''

        if cond == 1:
            lb_title['text'] = '1 - Como deve ser lido sobre a multa e fidelização no checklist?'
            lb_a['text'] = '     - Apenas informar o valor de R$140.'
            lb_b['text'] = '     - Apenas informar o valor de R$11,66 por meses restantes do término.'
            lb_c['text'] = '     - Passar todas informações conforme o checklist de forma clara.'
            lb_d['text'] = '     - Passar todas informações o mais rápido possível para que o cliente não desligue' \
                           ' a chamada.'
            quests.pop(0)

        elif cond == 2:
            lb_title['text'] = '2 - Ao ser questionado sobre cancelamento, o que deve ser respondido ao cliente?'
            lb_a['text'] = '     - Informar apenas o valor cheio da multa pró rata.'
            lb_b['text'] = '     - Informar que será calculado uma multa pró rata de R$11,66 por meses que não ' \
                           'usou do\n plano e logo após contra argumentar dizendo que o cliente não vai querer ' \
                           'cancelar.'
            lb_c['text'] = '     - Informar que será calculado uma multa pró rata de R$11,66 por meses que não usou' \
                           ' do plano\n e esperar o cliente responder que concorda.                               ' \
                           '                                               '
            lb_d['text'] = '     - Apenas informar que pode fazer o cancelamento quando quiser.'
            quests.pop(0)

        elif cond == 3:
            lb_title['text'] = '3- Caso aconteça do cliente se despedir e não responder mais o contato,\n o que deve' \
                               ' ser feito?'
            lb_a['text'] = '     - Chamar o cliente no mínimo 3 vezes e encerrar a chamada por falta de comunicação.'
            lb_b['text'] = '     - Encerrar a chamada.'
            lb_c['text'] = '     - Ficar um pouco mais na linha para aumentar o TMA.'
            lb_d['text'] = '     - Ficar chamando o cliente até ele retornar ou encerrar a chamada.'
            quests.pop(0)

        elif cond == 4:
            lb_title['text'] = '4 - Sobre o primeiro pagamento da fatura, é correto afirmar que:'
            lb_a['text'] = '     - O primeiro mês será gratuito.'
            lb_b['text'] = '     - Todo o período até o primeiro pagamento é grátis.'
            lb_c['text'] = '     - O período até o primeiro pagamento subtraído 30 dias é grátis.'
            lb_d['text'] = '     - Ele utilizará sem pagar nada até a primeira data de pagamento.'
            quests.pop(0)

        elif cond == 5:
            lb_title['text'] = '5 - Durante a venda você está passando as informações do checklist e de \nrepente a ' \
                               'ligação cai, o que fazer nesta situação?'
            lb_a['text'] = '     - Ser ágil e salvar a venda imediatamente.'
            lb_b['text'] = '     - Não salvar a venda e chamar o supervisor para falar que acabou de perder uma venda.'
            lb_c['text'] = '     - Utilizar o reagendamento automático e passar o número do cliente para o supervisor.'
            lb_d['text'] = '     - Salvar a venda e não tabular.'
            quests.pop(0)

        elif cond == 6:
            lb_title['text'] = '6 - Durante a venda o cliente diz que está com pressa e não tem tempo \ntempo para ' \
                               'ouvir as informações, o que fazer nesta situação?'
            lb_a['text'] = '     - Informar que está terminando e continuar a passagem das informações.'
            lb_b['text'] = '     - Fazer a pergunta de migração adicionando ao final "sem a passagem das ' \
                           '\ninformações importantes."                                                         ' \
                           '                     '
            lb_c['text'] = '     - Passar as informações de forma acelerada pra dar tempo de passar todas as ' \
                           '\ninformações e o cliente não desligar.                                               ' \
                           '                   '
            lb_d['text'] = '     - Agradecer o cliente e salvar a venda.'
            quests.pop(0)

        elif cond == 7:
            lb_title['text'] = '7 -  Tendo em vista que a maior quantidade de NCG acontece por conta de \nerro de ' \
                               'cadastro, marque a opção que NÃO ajuda a evitar este tipo de erro.'
            lb_a['text'] = '     - Chamar o supervisor para conferir se há erros de digitação.'
            lb_b['text'] = '     - Em caso de dúvida ao escrever nomes incomuns, pedir o cliente para soletrar.'
            lb_c['text'] = '     - Ter atenção redobrada ao fazer o cadastro e quando for confirmar os dados\n do ' \
                           'cliente conferir novamente se está tudo digitado de forma correta.      '
            lb_d['text'] = '     - Confiar no seu atendimento sem questionar se está correto ou não.'
            quests.pop(0)

        elif cond == 8:
            lb_title['text'] = '8 - Caso o cliente informe que o RG é o mesmo número do CPF,\n o que fazer nesta ' \
                               'situação?'
            lb_a['text'] = '     - Cadastrar no campo do RG o número do CPF.'
            lb_b['text'] = '     - Pedir ao cliente que busque o documento para falar a numeração correta.'
            lb_c['text'] = '     - Agradecer o cliente e encerrar a chamada.'
            lb_d['text'] = '     - Chamar o supervisor para falar com o cliente.'
            quests.pop(0)

        elif cond == 9:
            lb_title['text'] = '9 - O cliente disse que não aceita a oferta por a internet ser pouca pra ele,\n como ' \
                               'contornar está situação?'
            lb_a['text'] = '     - Informar sobre o claro clube, que o mesmo terá vários GBs de graça.'
            lb_b['text'] = '     - Informar sobre o 4.5g e suas condições como contra argumentação.'
            lb_c['text'] = '     - Oferecer mais internet para suprir a necessidade do cliente.'
            lb_d['text'] = '     - Todas alternativas estão corretas.'
            quests.pop(0)

        elif cond == 10:
            lb_title['text'] = '10 - Qual a forma correta de informar sobre o desconto ao cliente?'
            lb_a['text'] = '     - Basta pagar no débito e o senhor já garante o desconto de 5 reais.'
            lb_b['text'] = '     - Basta receber a fatura pelo whatsapp e o senhor já garante o desconto.'
            lb_c['text'] = '     - Cadastrando a forma de pagamento no débito em conta corrente junto com o ' \
                           'recebimento\n da fatura no e-mail e o senhor garante mais 5 reais de desconto.         ' \
                           '                            '
            lb_d['text'] = '     - Todas as alternativas estão corretas.'
            quests.pop(0)

    else:
        lb_intruções3['text'] = ''
        lb_intruções2['text'] = ''
        lb_intruções1['text'] = ''
        bt_save.destroy()
        lb_a['text'] = ''
        lb_b['text'] = ''
        lb_c['text'] = ''
        lb_d['text'] = ''
        bt_a.destroy()
        bt_b.destroy()
        bt_c.destroy()
        bt_d.destroy()
        lb_fim['text'] = 'Aperte "F11" ou "Esc" para finalizar   '
        bt_fim['text'] = 'Finalizar'
        bt_fim.grid(row=14, column=3)
        bt_fim['command'] = lambda: janela.destroy()
        gabarito()


# Função com teste lógico para definir a quantidade de erros e acertos


def gabarito():
    global cond_quest, resposta, gabarito_quests, gabarito_respostas, bt_a, bt_b, bt_c, bt_d, bt_fim, quests, a, d

    try:
        d = 'C:Users\s' + getuser() + '\Desktop'
        d = d[0:2] + '/' + d[2:]
        d = d[0:9] + d[10:]
        move(a, d)
    except:
        lb6 = Label(janela, text=f'Houve uma falha ao mover o arquivo {a}')
        lb6.grid(row=12, column=2, sticky='W')
    else:
        lb6 = Label(janela, text=f'Arquivo {a} movido com sucesso!')
        lb6.grid(row=12, column=2, sticky='W')

    erros = 0
    for pos, q in enumerate(gabarito_quests):
        if q == 1 and gabarito_respostas[pos] not in 'C':
            erros += 1
        elif q == 2 and gabarito_respostas[pos] not in 'B':
            erros += 1
        elif q == 3 and gabarito_respostas[pos] not in 'A':
            erros += 1
        elif q == 4 and gabarito_respostas[pos] not in 'D':
            erros += 1
        elif q == 5 and gabarito_respostas[pos] not in 'C':
            erros += 1
        elif q == 6 and gabarito_respostas[pos] not in 'A':
            erros += 1
        elif q == 7 and gabarito_respostas[pos] not in 'D':
            erros += 1
        elif q == 8 and gabarito_respostas[pos] not in 'B':
            erros += 1
        elif q == 9 and gabarito_respostas[pos] not in 'B':
            erros += 1
        elif q == 10 and gabarito_respostas[pos] not in 'C':
            erros += 1
    acertos = 10 - erros
    if acertos == 10:
        lb_title['text'] = f'Parabéns! Você acertou {acertos} questões e errou {erros}'
    else:
        lb_title['text'] = f'Você acertou {acertos} questões e errou {erros}'


# Função responsável por salvar as questões e respostas em listas separadas


def gabarito_append():
    global gabarito_respostas, gabarito_respostas

    gabarito_quests.append(cond_quest)
    gabarito_respostas.append(resposta)


# Função para salvar a resposta da questão e criação do botão para próxima questão


def próxima_questão():
    global d, a, resposta, cont, lb_save, quests, cond_quest, bt_save

    bt_save.grid(row=16, column=2, sticky='E')

    try:
        arquivo = open(a, 'at')
        arquivo.write(f'\n{cond_quest} - {resposta}')
        arquivo.close()
    except:
        lb_save = Label(janela, text='Erro ao salvar a resposta!')
        lb_save.grid(row=15, column=2, sticky='E')
    else:
        lb_save = Label(janela, text='Resposta salva com sucesso!')
        lb_save.grid(row=15, column=2, sticky='E')

    gabarito_append()


# Função para definir a entrada de dados correspondente a opção da questão escolhida pelo atendente


def status_bt(bt=''):
    global bt_a, bt_b, bt_c, bt_d, resposta

    if bt == bt_a:
        bt = 'A'
        lb_fim['text'] = 'A opção escolhida foi: A'
    elif bt == bt_b:
        bt = 'B'
        lb_fim['text'] = 'A opção escolhida foi: B'
    elif bt == bt_c:
        bt = 'C'
        lb_fim['text'] = 'A opção escolhida foi: C'
    elif bt == bt_d:
        bt = 'D'
        lb_fim['text'] = 'A opção escolhida foi: D'
    resposta = bt


# Janela principal e configuração de saída

janela = Tk()
janela.attributes('-fullscreen', True)

janela.bind('<Escape>', lambda e: janela.destroy())
janela.bind('<F11>', lambda e: janela.destroy())

janela.title('SAM - System Assistant Management')

# Configuração da fonte e labels de borda

font_titulo = font.Font(family='Lucida Grande', size=15)
font_texto = font.Font(family='Lucida Grande', size=12)

marca_dagua = Label(janela, text='SAMv1.0.0 developed by Samuel Nunes')
marca_dagua.grid(row=0, column=0)

lb_borda_horizontal = Label(janela, width=14)
lb_borda_horizontal.grid(row=0, column=1)
lb_borda_vertical = Label(janela, height=8)
lb_borda_vertical.grid(row=1, column=0)
lb_save = Label(janela)
lb_d = Label(janela, height=5, font=font_texto)

lb5 = lb6 = lb7 = bt_fim = bt_a = bt_b = bt_c = bt_d = d = a = sup = cond = bt_save = cond_quest = 0
lb_intruções1 = lb_intruções2 = lb_intruções3 = resposta = 0

# Tela 1 / Capa

lb_title = Label(janela, text='Digite seu nome no campo "Vendedor" e selecione seu supervisor \nLogo após clique em '
                              '"Salvar" e depois em "Iniciar Avaliação"', font=font_titulo, height=6)
lb_title.grid(row=2, column=2)

lb_a = Label(janela, text='\n\n\n\nVendedor', font=font_texto)
lb_a.grid(row=3, column=2, sticky='W')

ed1 = Entry(janela, width=50)
ed1.grid(row=4, column=2, sticky='W', columnspan=2)

lb1 = Label(janela, height='2')
lb1.grid(row=5)

lb_b = Label(janela, text='Supervisor: ', font=font_texto)
lb_b.grid(row=6, column=2, sticky='W')

lb_c = Label(janela)
lb_c.grid(row=7)

bt0 = Button(janela, width=10, text='Salvar', command=bt_click)
bt0.grid(row=13, column=2, sticky='W')

bt_save = Button(janela, text='Próxima Questão', command=bt_fim_click)

lb_fim = Label(janela, height=8, text='\n' * 6 + 'Boa Prova!', font=font_titulo)
lb_fim.grid(row=13, column=2)

lista_sup = ['Samuel Nunes de Souza', 'Nubia Fernandes Palmeira', 'Vynne Thomas Hermsdorf Barreto', 'Luis Gustavo '
             'Pereira Dias Oliva', 'Guilherme Alexsander de Souza', 'Lucas Daniel Santos Zuba', 'Anderson Adriel Silva'
             ' Duarte', 'Isabela de Souza Suterio', 'Pablo Teles dos Santos', 'Gustavo Pereira Lopes', 'SELECIONE...']

v = StringVar(janela)
v.set(lista_sup[10])

supervisores = OptionMenu(janela, v, *lista_sup)
supervisores.config(width=35)
supervisores.grid(row=7, column=2, sticky='W')

# Criando a lista para randomização das questões e lista para validar as respostas

quests = list(range(1, 11))
shuffle(quests)
gabarito_quests = list()
gabarito_respostas = list()

# Configuração para exclusão de widgets e loop da janela

janela.protocol("WM_DELETE_WINDOW", janela.iconify)
janela.mainloop()
