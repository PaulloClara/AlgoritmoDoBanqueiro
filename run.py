from processo import Processo
from recurso import Recurso


class App(object):
  def __init__(self):
    self.recursosDisponiveis = []
    self.tituloDosRecursos = []
    self.tituloDosProcessos = []
    self.processos = []
    self.estado = 'Seguro'

  def run(self):
    self.quebraDeLinha(5)
    self.preencherRecursosDisponiveis()
    self.criarProcessos()
    self.mostrarTabelaDeRecursos('Alocados')
    self.mostrarTabelaDeRecursos('Maximos')
    self.mostrarTabelaDeRecursosDisponiveis()
    self.mostrarTabelaDeRecursos('Necessarios')
    self.verificarEstado()
    self.mostrarEstado()
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
    self.quebraDeLinha(1)
    print('\t\t=-=-=-=-=-=-=-=-=-=-=')
    quantidadeDeProcessos = int(input('\t\tQuantos processos\n\t\t> '))
    for index in range(quantidadeDeProcessos):
      self.tituloDosProcessos.append(input(f'\n\t\tTitulo do processo {index+1}\n\t\t> '))
    print('\n\t\t=-=-=-=-=-=-=-=-=-=-=')
    for index in range(quantidadeDeProcessos):
      self.processos.append(Processo())
      self.processos[-1].init(self.tituloDosProcessos[index], self.tituloDosRecursos)

  def verificarEstado(self):
    continuar = True
    quantidadeDeProcessosOK = 0
    while continuar and quantidadeDeProcessosOK != len(self.processos):
      continuar = False
      for processo in self.processos:
        if processo.status():
          continue
        recursosDoProcesso = processo.obterRecursos('Necessarios')
        for index in range(len(self.tituloDosRecursos)):
          if self.recursosDisponiveis[index].obterQuantidade() >= recursosDoProcesso[index].obterQuantidade():
            processoOK = True
          else:
            processoOK = False
            break
        if processoOK:
          recursosLiberados = processo.run()
          for index in range(len(self.recursosDisponiveis)):
            self.recursosDisponiveis[index].add(recursosLiberados[index].obterQuantidade())
          quantidadeDeProcessosOK += 1
          continuar = True
          break

  def mostrarTabelaDeRecursosDisponiveis(self):
    self.quebraDeLinha(1)
    quantidades = ''
    for recurso in self.recursosDisponiveis:
      quantidades += str(recurso.obterQuantidade()) + ' '
    print('\t\t\tRecursos Disponiveis')
    print('\t\t\t=-=-=-=-=-=-=-=-=-=-=')
    print(f'\t\t\t{" ".join(self.tituloDosRecursos)}')
    print(f'\t\t\t{quantidades}')
    print('\t\t\t=-=-=-=-=-=-=-=-=-=-=')

  def mostrarTabelaDeRecursos(self, tipoDeRecurso):
    self.quebraDeLinha(1)
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

  def mostrarEstado(self):
    cores = { 'S': '\033[1;32m', 'I': '\033[1;31m' }
    for processo in self.processos:
      if not processo.status():
        self.estado = 'Inseguro'
    self.quebraDeLinha(3)
    print('\t\t=-=-=-=-=')
    print(f'\t\t{cores[self.estado[0]]}{self.estado}', end='\033[0;0m')
    print('\n\t\t=-=-=-=-=')

  def quebraDeLinha(self, numeroDeLinhas):
    print('\n' * numeroDeLinhas)


if __name__ == '__main__':
  App().run()
