voltage = float(input("Battery voltage in V: "))

if voltage >= 7.4:
    print("Battery OK - ready for the competition.")
elif voltage >= 7.0:
    print("Battery OK - but charge it after this lesson.")
else:
    print("Battery low - charge it now!")
