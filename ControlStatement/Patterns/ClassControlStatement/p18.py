command = input("Enter command..")

match command:
  case "start": print("System starting...")
  case "stop": print("System shuttingdown..")
  case "reboot": print("System rebooting")
  case _: print("Invalid command....")