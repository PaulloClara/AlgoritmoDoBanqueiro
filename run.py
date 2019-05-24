from processo import Processo
from recurso import Recurso


class App(object):
  def __init__(self):
    self.recursosDisponiveis = []
    self.tituloDosRecursos = []
    self.processos = []

  def run(self):
    self.preencherRecursosDisponiveis()
    self.criarProcessos()
    self.mostrarTabelaDeRecursosDisponiveis()
    self.mostrarTabelaDeRecursos('Alocados')
    self.mostrarTabelaDeRecursos('Maximos')
    self.mostrarTabelaDeRecursos('Necessarios')
    self.quebraDeLinha(2)

  def preencherRecursosDisponiveis(self):
    print('\t\t=-=-=-=-=-=-=-=-=-=-=-=')
    for index in range(int(input('\t\tQuantidade de recursos\n\t\t> '))):
      self.tituloDosRecursos.append(input(f'\n\t\tTitulo do recurso {index+1}\n\t\t> '))
    print('\n\t\t=-=-=-=-=-=-=-=-=-=-=-=')
    print('\n\n\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=', end='')
    for titulo in self.tituloDosRecursos:
      self.recursosDisponiveis.append(Recurso())
      self.recursosDisponiveis[-1].init(titulo, 'disponivel')
    print('\n\t\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

  def criarProcessos(self):
    self.quebraDeLinha(2)
    print('\t\t=-=-=-=-=-=-=-=-=')
    quantidadeDeProcessos = int(input('\t\tQuantos processos\n\t\t> '))
    print('\n\t\t=-=-=-=-=-=-=-=-=')
    self.quebraDeLinha(1)
    for index in range(quantidadeDeProcessos):
      self.processos.append(Processo())
      self.processos[-1].init(self.tituloDosRecursos)

  def mostrarTabelaDeRecursosDisponiveis(self):
    self.quebraDeLinha(3)
    quantidades = ''
    for recurso in self.recursosDisponiveis:
      quantidades += str(recurso.obterQuantidade()) + ' '
    print('\t\t\tRecursos Disponiveis')
    print('\t\t\t=-=-=-=-=-=-=-=-=-=-=')
    print(f'\t\t\t{" ".join(self.tituloDosRecursos)}')
    print(f'\t\t\t{quantidades}')
    print('\t\t\t=-=-=-=-=-=-=-=-=-=-=')

  def mostrarTabelaDeRecursos(self, tipoDeRecurso):
    self.quebraDeLinha(2)
    print(f'\t\t\tRecursos {tipoDeRecurso}')
    print('\t\t\t=-=-=-=-=-=-=-=-=-=-=')
    print(f'\t\t\t   {" ".join(self.tituloDosRecursos)}')
    for processo in self.processos:
      print(f'\t\t\t{processo.obterTitulo()}', end=' ')
      quantidades = ''
      for recurso in processo.obterRecursos(tipoDeRecurso):
        quantidades += str(recurso.obterQuantidade()) + ' '
      print(f'{quantidades}')
    print('\t\t\t=-=-=-=-=-=-=-=-=-=-=')

  def mostrarTabelaDeRecursosNecessarios(self):
    self.quebraDeLinha(2)


  def quebraDeLinha(self, numeroDeLinhas):
    print('\n' * numeroDeLinhas)


if __name__ == '__main__':
  App().run()
