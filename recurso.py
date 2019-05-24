class Recurso(object):
  def __init__(self):
    self.__titulo = ''
    self.__quantidade = 0

  def init(self, titulo, msg='', quantidade='0'):
    self.__titulo = titulo
    if quantidade == '0':
      self.__quantidade = int(input(f'\n\t\tQuandidade de recurso {self.__titulo} {msg}\n\t\t> '))
    else:
      self.__quantidade = quantidade

  def obterTitulo(self):
    return self.__titulo

  def obterQuantidade(self):
    return self.__quantidade
