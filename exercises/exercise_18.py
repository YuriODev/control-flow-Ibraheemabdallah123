# Your solution to Exercise 18
name = input("do you remember the persons name")
if name == "yes":
  ex = input("is it an ex")
  if ex == "yes":
    drunk = input("are you drunk")
    if drunk == "yes":
      rekindle = input("do you want to rekindle")
      if rekindle == "yes":
        print("Don't say hi.")
      else:
        print("Say hi.")
    else:
      car = input("are you in a car with brad pitt or rihanna")
      if car == "yes":
        print("Say hi.")
      else:
        print("Don't say hi")
  else:
    friend = input("is it a friend's ex")
    if friend == "yes":
      print("Don't say hi.")
    else:
      frenemy = input("is it a friend or enemy")
      if frenemy == "yes":
        car = input("are you in a car with brad pitt or rihanna")
        if car == "yes":
          print("Say hi.")
        else:
          print("Don't say hi.")
      else:
        bank = input("are you robbing a bank")
        if bank == "yes":
          print("Don't say hi.")
        else:
          bathrobe = input("are you in a bathrobe")
          if bathrobe == "yes":
            print("Don't say hi.")
          else:
            print("Say hi.")
else:
  escape = input("can you escape")
  if escape == "yes":
    print("Run for it.")
  else:
    call = input("can you pretend to gat a call")
    if call == "yes":
      print("Hello doctor. What are my test results")
    else:
      glass = input("are you wearing sunglasses")
      if glass == "yes":
        print("Keep walking.")
      else:
        print("Address the person using an amusing nickname such as Sarge, Slugger or Master Blaster.")
