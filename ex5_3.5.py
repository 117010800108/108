#for i in range(11):
 #   if i in[0,5,10]:
  #      print('+ - - - - + - - - - +')
   # else:
    #    print('|         |         |')
for i in range(11):
    if i%5==0:
        print('+','-'*4,'+','-'*4,'+')
    else:
        print('|',' '*4,'|',' '*4,'|')
