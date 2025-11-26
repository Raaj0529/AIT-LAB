def low_temp(x):
    if x <= 20: return 1
    if 20 < x < 30: return (30 - x) / 10
    return 0

def medium_temp(x):
    if 20 < x < 30: return (x - 20) / 10
    if 30 <= x <= 40: return (40 - x) / 10
    return 0

def high_temp(x):
    if x < 30: return 0
    if 30 <= x < 40: return (x - 30) / 10
    if x >= 40: return 1
    return 0

def low_speed(mu):
    return mu * 20

def medium_speed(mu):
    return mu * 50

def high_speed(mu):
    return mu * 90

def fuzzy_fan_speed(temp):
    mu_low = low_temp(temp)
    mu_med = medium_temp(temp)
    mu_high = high_temp(temp)

    num = low_speed(mu_low) + medium_speed(mu_med) + high_speed(mu_high)
    den = mu_low + mu_med + mu_high

    if den == 0: return 0
    return num / den

t = float(input("Enter current temperature in C: "))
speed = fuzzy_fan_speed(t)
print("Recommended Fan Speed:", round(speed, 2), "%")

