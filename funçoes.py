from os import replace


def limpar_campo_cpf(cpf):
    return cpf.replace('.','').replace('-','')