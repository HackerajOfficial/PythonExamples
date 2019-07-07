#Some thing design new
#in this concept using function we can write any code with specific extension
import os
f = open('test.py','w')

f.write(u"print('Hello World')\nprint('Hello World')\nprint('Hello World')")

f.close()
os.system('python test.py')
