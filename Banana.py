import cmd

while(True):
  command = input("Cmd: ")
  if("-q" in command):
    break
  if("-h" in command):
    f = open("help.txt",'r')
    print(f.read())
    f.close()
  else:
    if("def f" in command):
      argsf = command[command.find('(')+1:command.find(')')].split(",")
      regexf = command[command.find(':')+1:]
    else:
      regex = command
      if("f" in regex):
        args = regex[regex.find('(')+1:regex.find(')')].split(",")
        print(cmd.processf(args,argsf,regexf))
      else:
        print(cmd.process(regex))