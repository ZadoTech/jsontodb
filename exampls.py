def loop():
  fe = False
  try:
    ask = input("$ ")
  except:
    fe = True
    pass
  try:
    print ask
  except:
    fe = True
    pass
  if fe != False:
    print "Error Happend..."

print "Testing use Command\n"
print "Type hlp to See help"
print "or try type 'JDB(FILENAME).add(KEY, DATA)'"
print "and then 'JDB(FILENAME).refresh()'"
print " "
hlp = "  IO: View example.py to see more help"

try:
  loop()
except:
  pass
while True:
  loop()
