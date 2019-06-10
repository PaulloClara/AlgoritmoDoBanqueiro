class Recurso(object):
  def __init__(self):
    self.__titulo = ''
    self.__quantidade = 0

  def add(self, quantidade):
    self.__quantidade += quantidade

  def init(self, titulo, quantidade):
    self.__titulo = titulo
    self.__quantidade = quantidade

  def titulo(self):
    return self.__titulo

  def quantidade(self):
    return self.__quantidade
