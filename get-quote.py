import random
def master():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1 
  rnd = random.randint(0, last)
  for x in range(3):
    x = x + 1
    print(quotes[x], end = '')

if __name__== "__main__":
  master()

