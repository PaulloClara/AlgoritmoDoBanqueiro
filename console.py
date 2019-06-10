class Console(object):
  def __init__(self):
    pass

  def obter(self, msg):
    valor = input(f'\t\t{msg}\n\t\t> ')
    self.quebraDeLinha()
    return valor

  def mostrar(self, msg, n='\n', t='\t\t\t'):
    print(f'{t}{msg}', end=n)

  def linha(self, quantidade):
    resultado = '=-' * quantidade + '='
    print(f'\t\t{resultado}')

  def quebraDeLinha(self, numeroDeLinhas=1):
    print('\n' * (numeroDeLinhas-1))
