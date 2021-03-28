import random
def master():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1 
  rnd = random.randint(0, last)
  for(i = 0; i < 2; i++){
  print(quotes[rnd])
  }
  
  

if __name__== "__main__":
  master()
