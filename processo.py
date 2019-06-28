from console import Console

class Processo(object):
  def __init__(self):
    self.titulo = ''
    self.recursosMaximos = []
    self.recursosAlocados = []
    self.recursosNecessarios = []
    self.__console = Console()
    self.__finalizado = False

  def run(self):
    if not self.__finalizado:
      self.__finalizado = True
      return self.recursosAlocados
    return 0

  def status(self):
    if self.__finalizado:
      return 'Finalizado'
    return 'Ativo'

  def init(self, tituloDoProcesso, tituloDosRecursos):
    self.titulo = tituloDoProcesso
    self.__console.linha(27)
    for titulo in tituloDosRecursos:
      pergunta = f'Quandidade de recurso "{titulo}" máximo para o processo "{self.titulo}"'
      quantidade = int(self.__console.obter(pergunta))
      recurso = { 'titulo': titulo, 'quantidade': quantidade }
      self.recursosMaximos.append(recurso)
    self.__console.linha(27)
    self.__console.quebraDeLinha(1)
    self.__console.linha(27)
    for titulo in tituloDosRecursos:
      pergunta = f'Quandidade de recurso "{titulo}" alocado para o processo "{self.titulo}"'
      quantidade = int(self.__console.obter(pergunta))
      recurso = { 'titulo': titulo, 'quantidade': quantidade }
      self.recursosAlocados.append(recurso)
    self.__console.linha(27)
    self.__console.quebraDeLinha(2)
    quantidadeDeRecursos = len(tituloDosRecursos)
    for index in range(quantidadeDeRecursos):
      quantidade = self.recursosMaximos[index]['quantidade']
      quantidade -= self.recursosAlocados[index]['quantidade']
      titulo = tituloDosRecursos[index]
      recurso = { 'titulo': titulo, 'quantidade': quantidade }
      self.recursosNecessarios.append(recurso)
