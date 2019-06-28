class Recurso(object):
  def __init__(self):
    self.titulo = ''
    self.quantidadeAlocada = 0
    self.quantidadeExistente = 0
    self.quantidadeDisponivel = 0
    self.tipoDeEntradaDeRecurso = ''

  def adicionar(self, quantidade):
    self.quantidadeDisponivel += quantidade

  def calcularRecursosDisponiveisOuExistentes(self):
    if self.tipoDeEntradaDeRecurso == 'existentes':
      self.quantidadeDisponivel = self.quantidadeExistente - self.quantidadeAlocada
    else:
      self.quantidadeExistente = self.quantidadeDisponivel + self.quantidadeAlocada

  def init(self, titulo, quantidade, tipoDeEntradaDeRecurso):
    self.titulo = titulo
    self.tipoDeEntradaDeRecurso = tipoDeEntradaDeRecurso
    if self.tipoDeEntradaDeRecurso in 'existentes':
      self.quantidadeExistente = quantidade
    else:
      self.quantidadeDisponivel = quantidade
