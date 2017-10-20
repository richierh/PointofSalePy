import sys, os

print 'sys.argv[0] = %s'%(sys.argv[0])       
pathname = os.path.dirname(sys.argv[0])        
print 'path =', pathname
print 'full path =', os.path.abspath(sys.argv[0])
