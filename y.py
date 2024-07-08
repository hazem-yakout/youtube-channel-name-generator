while True:
 print("Welcome to the youtube channel name generator")
 nickName = input("what is your nickName?")
 channel = input("what is your channel about?")
 print(f"you could name your channel({channel} with {nickName})")
 choice = input("do you need to continue in the app?\n").strip().lower()
 if choice == "no":
      break
print("program is exited.")

