# Read prompt

prompt = input("Enter prompt: ")
match prompt:
    case "start":
        print("system starting")
    case "stop":
        print("system stoping")
    case "restart":
        print("restarting")
    case _:
        print("invalid prompt")
        