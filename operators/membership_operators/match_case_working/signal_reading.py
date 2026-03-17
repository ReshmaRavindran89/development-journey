# read signal
# read ->stop
# green ->go
# yellow ->wait

signal = input("Enter signal")
match signal:
    case "red":
        print("STOP")
    case "green":
        print("GO")
    case "yellow":
        print("WAIT")
    case _:
        print("INVALID")
        

