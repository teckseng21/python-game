import random
def grid():
  return [['-' for _ in  range(5)] for _ in  range(5)]
def place_treasure():
  return random.randint(0,4),random.randint(0,4)
  
def give_hints(tr, tc, gr, gc):
  if gr<tr:
    return("Move down")
  elif gr>tr:
    return("Move up")
  elif gc<tc:
    return("Move right")
  elif gc>tc:
    return("Move left")
    
ger=grid()
tr,tc=place_treasure()

print (ger)
while True:
  print ("\n Current Grid:")
  for row in ger:
   print (" ".join(row))
  try:
    gr=int(input("Enter the row number(0-4): "))
    gc=int(input("Enter the column number(0-4): "))
  except ValueError:
    print("Please enter the numbers between 0 and 4.")
    continue
  
  if gr not in range(5) or gc not in range(5):
    print("Invalid input Please chose a row and column between the numbers 0 to 4!")
    continue
  if ger[gr][gc]=='X':
    print("You have already guessed this position, try a different spot.")
    continue
  if gr==tr and gc==tc:
    print("Congrats! You found the treasure!!")
    break
  else:
    ger[gr][gc]='X'
    hints=give_hints(tr, tc, gr, gc)
    print(hints)