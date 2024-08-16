'''
Sistema para ajudar no erro do sistema SPX
'''
from abc import ABC, abstractmethod
#from selenium import webdriver



class Spx(ABC):
    """
    Criar um algoritmo que, recebe as seguintes informações:

    1 - Seria uma AT ou TO?
    2 - Número da AT/TO

    Em seguida, deverá receber o link da AT/TO
    """
    def __init__(self):
        self.taskid = input('Cole o código VT: ')
        if self.taskid[:2] != 'VT':
            print('Ocorreu um erro, digite a task_id corretamente!')
    @abstractmethod
    def opcao(self, modo):
        pass 
    def creditos(self):
        print('Sistema desenvolvido por Davi dos Santos[Ops28415]\nLinkedIn: /in/davisantosrj')


class ComandoSpx(Spx):
    # Comandos do Sys

    def opcao(self, modo):
        target = modo
        modo = modo[:2]
        if modo != 'AT' and modo != 'TO':
            print('Selecione uma opção válida! AT ou TO.')
        else:
            if modo == 'AT':
                try:
                    task_at = target
                    if task_at[:2] != 'AT':
                        print('Isso não é uma AT!')
                    else:
                        link_at = 'https://spx.shopee.com.br/#/mercadao/audit-list/at-to-detail?task_id=' + self.taskid + '&target_id=' + task_at + '&audit_target_type=2'
                        print(f'Link para voltar a conferência: {link_at}')
                        #navegador = webdriver.Chrome()
                        #navegador.get(link_at)
                except TypeError:
                    print('Ocorreu um erro, tente novamente!')
            elif modo == 'TO':
                try:
                    task_to = target
                    if task_to[:2] != 'TO':
                        print('Isso não é uma TO!')
                    else:
                        link_to = 'https://spx.shopee.com.br/#/mercadao/audit-list/at-to-detail?task_id=' + self.taskid + '&target_id=' + task_to + '&audit_target_type=3'
                        print(f'Link para voltar a conferência: {link_to}')
                except TypeError:
                    print('Ocorreu um erro')
comando_spx = ComandoSpx()
comando_spx.opcao(input('Cole sua AT/TO: '))