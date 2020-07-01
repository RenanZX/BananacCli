import math

class Processor:
  def __init__(self):
    pass

  def add(self,values):
    return sum(values)

  def sub(self,values):
      res = [-x for x in values[1:]]
      res.append(values[0])
      return sum(res)

  def mult(self,values):
      m = values[0]
      values.pop(0)
      for x in values:
        m*=x
      return m

  def div(self,values):
      d = values[0]
      values.pop(0)
      for x in values:
        d/=x
      return d

  def pot(self,values):
      p = values[0]
      values.pop(0)
      for x in values:
          p = pow(p,x)

      return p

  def raiz(self,values):
      p = values[0]
      values.pop(0)
      for x in values:
          p = pow(p,1/x)
      return p

  def ValidRex(self,regex):
    reglist = regex.split(" ")
    if len(reglist) <= 1 or not('-' in regex) :
      return False
    return True


  def process(self,regex):
    operators = []
    operations = []
    values = []
    countop = 0

    reglist = regex.split(" ")
    
    for x in reglist:
      if '-' in x:
        operations.append(x)
        operations.append(countop)
        countop = 0
      else:
        operators.append(float(x))
        countop += 1
    
    while operations:
      countop = operations.pop()
      op = operations.pop()
      while countop != 0:
        if not operators:
          values.append(operators.pop())
        countop-=1
      if countop == 0 and operators:
        while operators:
          values.append(operators.pop())
      if op == '-+':
        operators.append(self.add(values))
      if op == '--':
        operators.append(self.sub(values))
      if op == '-*':
        operators.append(self.mult(values))
      if op == '-/':
        operators.append(self.div(values))
      if op == '-**':
        operators.append(self.pot(values))
      if op == '-//':
        operators.append(self.raiz(values))

    return operators.pop()


class Function:

  def __init__(self, regex):
    self.proc = Processor()
    self.variables = regex[regex.find('(')+1:regex.find(')')].split(',')
    self.regex = regex[regex.find(':')+2:]

  def getArgs(self):
    return self.variables

  def process(self, fargs):
    args = fargs[fargs.find('(')+1:fargs.find(')')].split(',')
    lireg = self.regex.split(' ')
    ars = self.variables.copy()
    for x in args:
      ar = ars.pop(0)
      if not ar.isdigit():
        lireg[lireg.index(ar)] = x

    return self.proc.process(" ".join(lireg))
"""
class Function_Rec:
  def __init__(self, regex):
    self.proc = Processor()
    self.fbase = Function(regex[regex.find(':')+2:regex.find(';')])
    self.fit = regex[regex.find(';')+2:regex.find('recursive')].split(' ')

  def getListFunction(self):
    listf = self.fit

  def process(self,fargs):
    args = fargs[fargs.find('(')+1:fargs.find(')')].split(',')
    
    if args == fbase.getArgs():
      return fbase.process('')
    else:
      operators = []
      operations = []
      values = []
      countop = 0

      for x in reglist:
        if '-' in x:
          operations.append(x)
          operations.append(countop)
          countop = 0
        else:
          operators.append(x)
          countop += 1
    
"""

class Cmd:
  processor = Processor()
  function = 0
  ftype = 0

  def process(self,regex):
    #if not self.processor.ValidRex(regex):
    #  return "Erro! Expressão Inválida"
    
    if 'def f' in regex:
      if 'recursive' in regex:
        self.ftype = 1
      else:
        self.function = Function(regex)
      
      return ''
    else:
      if 'f' in regex:
        reg = regex.split(' ')
        for i in range(len(reg)):
          if 'f' in reg[i]:
            reg[i] = str(self.function.process(reg[i]))
        regex = " ".join(reg)

    return self.processor.process(regex)
