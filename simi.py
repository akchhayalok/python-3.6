def si(p,r,t)
  i= (p*r*t)/100
  return i
if __name__ == "__main__":

  print("Enter prinicipal, rate and time ")
  p = int(input("Enter Pricipal value: "))
  r = input("Rate: ")
  t = input("Time: ")
  SI = si(p,r,t)
  print(SI)
