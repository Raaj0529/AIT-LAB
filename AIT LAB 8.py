def bayes_weather(p_rain, p_e_given_rain, p_e_given_no_rain):
    p_no_rain = 1 - p_rain
    p_e = p_e_given_rain * p_rain + p_e_given_no_rain * p_no_rain
    return (p_e_given_rain * p_rain) / p_e

print("Weather Prediction")

p_rain = float(input("P(Rain): "))
p_cloud_given_rain = float(input("P(Cloudy | Rain): "))
p_cloud_given_no_rain = float(input("P(Cloudy | No-Rain): "))

p_rain_given_cloud = bayes_weather(p_rain, p_cloud_given_rain, p_cloud_given_no_rain)
print("\nP(Rain | Cloudy) =", round(p_rain_given_cloud, 4))
