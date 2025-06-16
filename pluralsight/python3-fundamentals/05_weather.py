temperature = 32
forcast = "raining"
raining = True

if temperature > 30:
    print("Stay inside")
else:
    print("Go outside")

if temperature > 30 or temperature < 20:
    print("Stay inside")
else:
    print("Go outside")

if temperature < 30 and forcast == "raining":
    print("Stay inside")
else:
    print("Go outside")

if not forcast == "raining":
    print("Go outside")
else:
    print("Stay inside")

if raining:
    print("Stay inside")
else:
    print("Go outside")

if not raining:
    print("Go outside")
else:
    print("Stay inside")
