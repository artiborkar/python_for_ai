
while True :
    user_input = input("Enter command for s/w (start/stop/pause) : ")


    match user_input :
        case "start":
            print("s/w starting.........")
        case "stop" :
            print("s/w is stopped")
        case "pause":
            print("s/w pause")
        case _ :
            print("unknow command , please enter the valied command")

    sw_stop = input("do you want to stop the program ? (yes/no):")
    if sw_stop == "yes":
        break