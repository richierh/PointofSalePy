import os

#print (os.path.realpath(__file__))
#print ("hello")
#print (os.getcwd())
#print (os.chdir("/home/pmc/"))
#print (os.path.realpath(__file__))
l = "/PosPy/mainframe/icons/Toolbars/koleksitoolbar.py"
c = os.path.realpath(l)
print (os.path.realpath(l))
print (os.listdir("./PosPy/mainframe/icons/Toolbars"))
rk = os.listdir("./PosPy/mainframe/icons/Toolbars")
print (list(rk))
r = list(rk)
print (r[1])