from console import Console
from recurso import Recurso
from processo import Processo


class App(object):
  def __init__(self):
    self.console = Console()
    self.recursos = []
    self.processos = []
    self.ordemDeExecucao = []
    self.tituloDosRecursos = []
    self.tituloDosProcessos = []
    self.estado = 'Seguro'
    self.executando = True

  def run(self):
    self.console.quebraDeLinha(2)
    self.criarRecursos()
    self.criarProcessos()
    self.calcularRecursosDisponiveisOuExistentes()
    self.mostrarTabelaDeProcessosERecursos('Alocados')
    self.console.quebraDeLinha(2)
    self.mostrarTabelaDeProcessosERecursos('Maximos')
    self.console.quebraDeLinha(2)
    self.mostrarTabelaDeProcessosERecursos('Necessarios')
    self.console.quebraDeLinha(2)
    self.mostrarTabelaDeRecursos('Disponiveis')
    self.console.quebraDeLinha(2)
    self.mostrarTabelaDeRecursos('Existentes')
    self.console.quebraDeLinha(2)
    self.verificarEstado()
    self.mostrarEstado()
    self.console.quebraDeLinha(2)
    self.console.mostrar(' -> '.join(self.ordemDeExecucao))
    self.console.quebraDeLinha(2)

  def verificarEstado(self):
    continuar = True
    quantidadeDeProcessos = len(self.processos)
    quantidadeDeProcessosOK = 0
    quantidadeDeRecursos = len(self.recursos)
    while continuar and quantidadeDeProcessos > quantidadeDeProcessosOK:
      continuar = False
      for processo in self.processos:
        if processo.status() == 'Finalizado':
          continue
        recursosNecessarios = processo.recursosNecessarios
        for index in range(quantidadeDeRecursos):
          quantidadeDeRecursosDisponivel = self.recursos[index].quantidadeDisponivel
          if quantidadeDeRecursosDisponivel >= recursosNecessarios[index]['quantidade']:
            processoOK = True
          else:
            processoOK = False
            break
        if processoOK:
          self.ordemDeExecucao.append(processo.titulo)
          recursosLiberados = processo.run()
          for index in range(quantidadeDeRecursos):
            self.recursos[index].adicionar(recursosLiberados[index]['quantidade'])
          quantidadeDeProcessosOK += 1
          continuar = True
          break

  def calcularRecursosDisponiveisOuExistentes(self):
    for processo in self.processos:
      recursosAlocados = processo.recursosAlocados
      for index in range(len(recursosAlocados)):
        self.recursos[index].quantidadeAlocada += recursosAlocados[index]['quantidade']
    for recurso in self.recursos:
      recurso.calcularRecursosDisponiveisOuExistentes()

  # Inits
  def criarRecursos(self):
    self.console.linha(11)
    quantidadeDeRecursosos = int(self.console.obter('Quantidade de recursos'))
    for index in range(quantidadeDeRecursosos):
      titulo = self.console.obter(f'Titulo do recurso {index+1}')
      self.tituloDosRecursos.append(titulo)
    self.console.linha(11)
    self.console.quebraDeLinha(2)
    self.console.linha(17)
    tipoDeEntradaDeRecurso = self.console.obter('Recursos Existentes ou Disponiveis').lower()
    self.console.linha(17)
    self.console.quebraDeLinha(2)
    self.console.linha(17)
    for titulo in self.tituloDosRecursos:
      pergunta = f'Quantidade de recurso "{titulo}" {tipoDeEntradaDeRecurso}'
      quantidade = int(self.console.obter(pergunta))
      recurso = Recurso()
      recurso.init(titulo, quantidade, tipoDeEntradaDeRecurso)
      self.recursos.append(recurso)
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

  # Saidas
  def mostrarTabelaDeProcessosERecursos(self, tipoDeRecurso):
    self.console.quebraDeLinha(1)
    self.console.mostrar(f'Recursos {tipoDeRecurso}', t='\t\t')
    self.console.linha(14)
    self.console.mostrar(f'    {"  ".join(self.tituloDosRecursos)}')
    for processo in self.processos:
      linha = processo.titulo + '  '
      if tipoDeRecurso == 'Alocados':
        recursos = processo.recursosAlocados
      elif tipoDeRecurso == 'Maximos':
        recursos = processo.recursosMaximos
      else:
        recursos = processo.recursosNecessarios
      for recurso in recursos:
        linha += str(recurso['quantidade']) + '  '
      self.console.mostrar(linha)
    self.console.linha(14)

  def mostrarTabelaDeRecursos(self, tipoDeRecurso):
    self.console.quebraDeLinha(1)
    linha = '  '
    for recurso in self.recursos:
      if tipoDeRecurso == 'Disponiveis':
        linha += str(recurso.quantidadeDisponivel) + '  '
      else:
        linha += str(recurso.quantidadeExistente) + '  '
    self.console.mostrar(f'Recursos {tipoDeRecurso}', t='\t\t')
    self.console.linha(14)
    self.console.mostrar(f'  {"  ".join(self.tituloDosRecursos)}')
    self.console.mostrar(f'{linha}')
    self.console.linha(14)

  def mostrarEstado(self):
    cores = { 'S': '\033[1;32m', 'I': '\033[1;31m' }
    for processo in self.processos:
      if processo.status() != 'Finalizado':
        self.estado = 'Inseguro'
    self.console.linha(4)
    self.console.mostrar(f'{cores[self.estado[0]]}{self.estado}', '\033[0;0m\n', '\t\t')
    self.console.linha(4)


if __name__ == '__main__':
  App().run()
