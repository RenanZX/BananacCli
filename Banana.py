from cmd import Cmd

Exe = Cmd()

while(True):
  command = input("Cmd: ")
  if("-q" in command):
    break
  if("-h" in command):
    f = open("help.txt",'r')
    print(f.read())
    f.close()
  else:
    print(Exe.process(command))