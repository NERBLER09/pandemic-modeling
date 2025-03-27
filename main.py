# Variables that determine the population
population = 100
infected_pop = population - (population*0.98) 
recovered_pop = 0
healthy_pop = population - infected_pop

# time-frame
total_days = 100 # Setting it to 0 defaults into running until for max days
max_days = 1000

# Rates are done in deciamal form of percentages
infection_rate = 0.05
recovered_infection_rate = 0.0002
recovery_rate = 0.785

ran_days = 0
for day in range(max_days):
    ran_days = ran_days + 1

    infected = population * infection_rate
    recovered = infected * recovery_rate

    infected_pop = infected_pop - recovered
    infected_pop = infected_pop + infected
    recovered_pop = recovered_pop + recovered
    healthy_pop = population - infected_pop + recovered_pop

    # Calculates if it fits within the population range

    if(infected_pop == population):
        print(f"After {ran_days} days, there are no healthy people in the population.")
        break
    elif(recovered_pop == population):
        print(f"Everyone recvered ffrom the infection, after {ran_days} days.")
        break
    else:
        print(f"Day {ran_days}")
        print(f"Healthy Pop: {healthy_pop}")
        print(f"Infected Pop: {infected_pop}")
        print(f"Recoverd Pop: {recovered_pop}")
        print("--------------------------------------------------")

    if(ran_days == total_days):
        break