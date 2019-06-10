from console import Console
from recurso import Recurso
from processo import Processo


class App(object):
  def __init__(self):
    self.console = Console()
    self.processos = []
    self.ordemDeExecucao = []
    self.tituloDosRecursos = []
    self.tituloDosProcessos = []
    self.recursosDisponiveis = []
    self.estado = 'Seguro'
    self.executando = True

  def run(self):
    self.console.quebraDeLinha(2)
    self.criarRecursosDisponiveis()
    self.criarProcessos()
    self.mostrarTabelaDeRecursos('Alocados')
    self.console.quebraDeLinha(2)
    self.mostrarTabelaDeRecursos('Maximos')
    self.console.quebraDeLinha(2)
    self.mostrarTabelaDeRecursosDisponiveis()
    self.console.quebraDeLinha(2)
    self.mostrarTabelaDeRecursos('Necessarios')
    self.console.quebraDeLinha(2)
    self.verificarEstado()
    self.mostrarEstado()
    self.console.quebraDeLinha(2)
    self.console.mostrar(' -> '.join(self.ordemDeExecucao))
    self.console.quebraDeLinha(2)

  def verificarEstado(self):
    continuar = True
    quantidadeDeProcessosOK = 0
    while continuar and quantidadeDeProcessosOK != len(self.processos):
      continuar = False
      for processo in self.processos:
        if processo.status():
          continue
        recursosDoProcesso = processo.recursos('Necessarios')
        quantidadeDeRecursos = len(self.tituloDosRecursos)
        for index in range(quantidadeDeRecursos):
          quantidadeDeRecursosDisponivel = self.recursosDisponiveis[index].quantidade()
          if quantidadeDeRecursosDisponivel >= recursosDoProcesso[index].quantidade():
            processoOK = True
          else:
            processoOK = False
            break
        if processoOK:
          self.ordemDeExecucao.append(processo.titulo())
          recursosLiberados = processo.run()
          for index in range(len(self.recursosDisponiveis)):
            self.recursosDisponiveis[index].add(recursosLiberados[index].quantidade())
          quantidadeDeProcessosOK += 1
          continuar = True
          break

  def mostrarTabelaDeRecursosDisponiveis(self):
    self.console.quebraDeLinha(1)
    linha = '  '
    for recurso in self.recursosDisponiveis:
      linha += str(recurso.quantidade()) + '  '
    self.console.mostrar('Recursos Disponiveis', t='\t\t')
    self.console.linha(14)
    self.console.mostrar(f'  {"  ".join(self.tituloDosRecursos)}')
    self.console.mostrar(f'{linha}')
    self.console.linha(14)

  def mostrarTabelaDeRecursos(self, tipoDeRecurso):
    self.console.quebraDeLinha(1)
    self.console.mostrar(f'Recursos {tipoDeRecurso}', t='\t\t')
    self.console.linha(14)
    self.console.mostrar(f'    {"  ".join(self.tituloDosRecursos)}')
    for processo in self.processos:
      linha = processo.titulo() + '  '
      for recurso in processo.recursos(tipoDeRecurso):
        linha += str(recurso.quantidade()) + '  '
      self.console.mostrar(linha)
    self.console.linha(14)

  def mostrarEstado(self):
    cores = { 'S': '\033[1;32m', 'I': '\033[1;31m' }
    for processo in self.processos:
      if not processo.status():
        self.estado = 'Inseguro'
    self.console.linha(4)
    self.console.mostrar(f'{cores[self.estado[0]]}{self.estado}', '\033[0;0m\n', '\t\t')
    self.console.linha(4)

  def criarRecursosDisponiveis(self):
    self.console.linha(11)
    numeroDeRecursos = int(self.console.obter('Quantidade de recursos'))
    for index in range(numeroDeRecursos):
      titulo = self.console.obter(f'Titulo do recurso {index+1}')
      self.tituloDosRecursos.append(titulo)
    self.console.linha(11)
    self.console.quebraDeLinha(2)
    self.console.linha(17)
    for titulo in self.tituloDosRecursos:
      pergunta = f'Quantidade de recurso "{titulo}" Disponivel'
      quantidade = int(self.console.obter(pergunta))
      recurso = Recurso()
      recurso.init(titulo, quantidade)
      self.recursosDisponiveis.append(recurso)
    self.console.linha(17)

  def criarProcessos(self):
    self.console.quebraDeLinha(3)
    quantidadeDeProcessos = int(self.console.obter('Quantidade de processos'))
    self.console.linha(10)
    for index in range(quantidadeDeProcessos):
      titulo = self.console.obter(f'Titulo do processo {index+1}')
      self.tituloDosProcessos.append(titulo)
    self.console.linha(10)
    self.console.quebraDeLinha(3)
    for index in range(quantidadeDeProcessos):
      processo = Processo()
      processo.init(self.tituloDosProcessos[index], self.tituloDosRecursos)
      self.processos.append(processo)


if __name__ == '__main__':
  App().run()
