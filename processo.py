from recurso import Recurso
from console import Console

class Processo(object):
  def __init__(self):
    self.__console = Console()
    self.__recursosMaximos = []
    self.__recursosAlocados = []
    self.__recursosNecessarios = []
    self.__titulo = ''
    self.__executado = False

  def run(self):
    if not self.status():
      self.__executado = True
      return self.__recursosAlocados
    return 0

  def status(self):
    return self.__executado

  def init(self, tituloDoProcesso, tituloDosRecursos):
    self.__titulo = tituloDoProcesso
    self.__console.linha(27)
    for titulo in tituloDosRecursos:
      pergunta = f'Quandidade de recurso "{titulo}" máximo para o processo "{self.__titulo}"'
      quantidade = int(self.__console.obter(pergunta))
      recurso = Recurso()
      recurso.init(titulo, quantidade)
      self.__recursosMaximos.append(recurso)
    self.__console.linha(27)
    self.__console.quebraDeLinha(1)
    self.__console.linha(27)
    for titulo in tituloDosRecursos:
      pergunta = f'Quandidade de recurso "{titulo}" alocado para o processo "{self.__titulo}"'
      quantidade = int(self.__console.obter(pergunta))
      recurso = Recurso()
      recurso.init(titulo, quantidade)
      self.__recursosAlocados.append(recurso)
    self.__console.linha(27)
    self.__console.quebraDeLinha(2)
    for index in range(len(tituloDosRecursos)):
      quantidade = self.__recursosMaximos[index].quantidade()
      quantidade -= self.__recursosAlocados[index].quantidade()
      recurso = Recurso()
      recurso.init(tituloDosRecursos[index], quantidade)
      self.__recursosNecessarios.append(recurso)

  def recursos(self, tipoDeRecurso):
    if tipoDeRecurso == 'Alocados':
      return self.__recursosAlocados
    elif tipoDeRecurso == 'Maximos':
      return self.__recursosMaximos
    else:
      return self.__recursosNecessarios

  def titulo(self):
    return self.__titulo
