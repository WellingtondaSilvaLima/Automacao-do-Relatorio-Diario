import datetime as dt

# Cria uma variável com a data atual e formatação pt-br
agora = dt.datetime.now()
hoje = agora.strftime('%d/%m/%Y')

# Todos os "with" adicionam ao final de cada arquivo a formatação de cabeçalho
# No "for" ele cria cada linha do relatório
with open('instalacao.txt', 'a') as arquivo:
    arquivo.write('\n\n\n\n\n\n')
    arquivo.write('*'*92)
    arquivo.write(f'\n{hoje}\n')
    arquivo.write('*'*92)
    for i in range(1, 21):
        arquivo.write(f'''
	{i}-
____________________________________________________________________________________________
''')


with open('atendimento.txt', 'a') as arquivo:
    arquivo.write('\n\n\n\n\n\n')
    arquivo.write('*'*92)
    arquivo.write(f'\n{hoje}\n')
    arquivo.write('*'*92)
    for i in range(1, 21):
        arquivo.write(f'''
{i}-
____________________________________________________________________________________________
''')


with open('geracao_online.txt', 'a') as arquivo:
    arquivo.write('\n\n\n\n\n\n')
    arquivo.write('*'*92)
    arquivo.write(f'\n{hoje}\n')
    arquivo.write('*'*92)
    for i in range(1, 21):
        arquivo.write(f'''
*** cliente com liberação para cadastro do SIM CLUB****

{i}-

	Telefone: 
	Contato: 
	Pacote: 
	Licença: 
	Login: 
	Senha: 
*** cliente com liberação para cadastro de cursos – ESCOLA MESTRE AUTOMOTIVO****

[ ] Verde
[ ] Vermelho

Vendedor: 
____________________________________________________________________________________________
''')


    









