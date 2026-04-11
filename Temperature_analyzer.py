temp = float(input(" Enter a temperature in Celsius:  ").strip())
if temp < 0 :
    print("The temperature is below freezing.")
elif temp <= 30:
    print("The temperature is at the moderate.")
else :
    print("The temperature is high.")
if temp > 25:
    print("The temperature is above the average human body temperature.")
if temp %2 == 0:
        print("The temperature is an even number.")
else:
     print("The temperature is an odd number.")