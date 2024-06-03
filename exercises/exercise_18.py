# Your solution to Exercise 18
name = input("do you remember the persons name")
if name == "yes":
  ex = input("is it an ex")
  if ex == "yes":
    drunk = input("are you drunk")
    if drunk == "yes":
      rekindle = input("do you want to rekindle")
      if rekindle == "yes":
        print("dont say hi")
      else:
        print("say hi")
    else:
      car = input("are you in a car with brad pitt or rihanna")
      if car == "yes":
        print("say hi")
      else:
        print("dont say hi")
  else:
    friend = input("is it a friend's ex")
    if friend == "yes":
      print("dont say hi")
    else:
      frenemy = input("is it a friend or enemy")
      if frenemy == "yes":
        car = input("are you in a car with brad pitt or rihanna")
        if car == "yes":
          print("say hi")
        else:
          print("dont say hi")
      else:
        bank = input("are you robbing a bank")
        if bank == "yes":
          print("dont say hi")
        else:
          bathrobe = input("are you in a bathrobe")
          if bathrobe == "yes":
            print("dont say hi")
          else:
            print("say hi")
else:
  escape = input("can you escape")
  if escape == "yes":
    print("run")
  else:
    call = input("can you pretend to gat a call")
    if call == "yes":
      print("hello doctor what are my results")
    else:
      glass = input("are you wearing sunglasses")
      if glass == "yes":
        print("keep walking")
      else:
        print("address the person with a nickname")
