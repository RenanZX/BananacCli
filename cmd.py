import math

def add(values):
   return sum(values)

def sub(values):
    res = [-x for x in values[1:]]
    res.append(values[0])
    return sum(res)

def mult(values):
    m = values[0]
    values.pop(0)
    for x in values:
       m*=x
    return m

def div(values):
    d = values[0]
    values.pop(0)
    for x in values:
       d/=x
    return d

def pot(values):
    p = values[0]
    values.pop(0)
    for x in values:
        p = pow(p,x)

    return p

def raiz(values):
    p = values[0]
    values.pop(0)
    for x in values:
        p = pow(p,1/x)
    return p

def process(regex):
    exps = regex.count(" -")
    if(exps == 1):
      args = [float(x) for x in regex[0:regex.find(" -")].split(" ")]
      if("-+" in regex):
          return add(args)
      if("--" in regex):
          return sub(args)
      if("-**" in regex):
          return pot(args)
      if("-//" in regex):
          return raiz(args)
      if("-*" in regex):
          return mult(args)
      if("-/" in regex):
          return div(args)
    elif(exps > 1):
      res = []
      for i in range(exps):
        subregex = regex[0:regex.find("-")+2]
        args = [float(x) for x in subregex[0:subregex.find(" -")].split(" ")]
        if("-+" in subregex):
          res.append(add(args))
        if("--" in subregex):
          res.append(sub(args))
        if("-**" in subregex):
          res.append(pot(args))
        if("-//" in subregex):
          res.append(raiz(args))
        if("-*" in subregex):
          res.append(mult(args))
        if("-/" in subregex):
          res.append(div(args))
        regex = regex[regex.find("-")+3:]
        if(regex[0] == '-'):
            if("-+" in regex):
              return add(res)
            if("--" in regex):
              return sub(res)
            if("-**" in regex):
              return pot(res)
            if("-//" in regex):
              return raiz(res)
            if("-*" in regex):
              return mult(res)
            if("-/" in regex):
              return div(res)
      return res
          
    return "Erro expressão inválida"


def processf(args,argsf,regexf):
  if(regexf == ''):
      return "Funcao indefinida"
  
  lireg = list(regexf)
  ars = argsf.copy()
  for x in args:
    ar = ars.pop(0)
    for i in range(len(lireg)):
      if(lireg[i] == ar):
          lireg[i] = x
  
  reg = "".join(lireg)
  return process(reg)