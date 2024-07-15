texto = ''
while texto != 'cancelar':
    sexo = input('SEXO [M/F]:\n').upper()
    if sexo == 'M':
        texto = 'cancelar'
        sexo = '\033[4;36;40mMASCULINO\033[m'
    elif sexo == 'F':
        texto = 'cancelar'
        sexo = '\033[4;35;40mFEMININO\033[m'    
    else:
        print('\033[4;31;40mINSIRA OS DADOS CORRETAMENTE!\033[m')
print(f'SEXO SELECIONADO: {sexo}.')
