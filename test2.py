import  os
import sys
path=os.path.dirname(os.path.abspath(__file__))+'\\data'
print(path)
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)
for i in range(10):
    restart_program()