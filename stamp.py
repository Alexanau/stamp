#!/usr/bin/python
import Image
import sys
import math
import getopt as g

def minsq(x):
  return int(math.ceil(math.sqrt(x)))

dx=0
dy=0
infile = ''
output = ''

optlist, args = g.getopt(sys.argv[1:],'o:i:x:y:')
for o,a in optlist:
  if o == '-x':
    dx = int(a)
  if o == '-y':
    dy = int(a)
  if o == '-i':
    infile = a
  if o == '-o':
    output = a

print infile
im = Image.open(infile).convert('RGB')

fh = sys.stdin
if len(args)>0:
  fh=open(args[0],'r')


data = []
size = 0;
for line in fh:
  for ch in line:
      data.append(ord(ch))
      size += 1
fh.close()

X = minsq(size/3)
Y = X
print "C", size
print ' ',X*Y*3,"<--avalable"
print "X",X
print "Y",Y

dX,dY = im.size

i = 0
for y in range(Y):
  for x in range(X):
    r,g,b = 0,0,0
    if i<len(data):
      r=data[i]
    i+=1
    if i<len(data):
      g=data[i]
    i+=1
    if i<len(data):
      b=data[i]
    i+=1
    im.putpixel(((x+dx)%dX,(dy+y)%dY),(r,g,b))
  
if len(output)>0:
  output += '.png'
  print 'Saving to',output
  im.save(output, "PNG")
