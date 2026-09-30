def go_forward(seconds, speed=50):
    print("Forward for", seconds, "s at", speed, "% speed")


go_forward(2)            # speed is 50 (the default)
go_forward(2, 80)        # speed is 80
go_forward(3, speed=30)  # you can also write the name of the parameter
