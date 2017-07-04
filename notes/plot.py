import matplotlib.pyplot as plt


weeks = [2, 3, 4, 5, 7]
results = [3750468.5, 2313164, 1243763.5, 1235252.5, 747312]
plt.plot(weeks, results)

plt.xlabel('Week number')
plt.ylabel('Money spent')
plt.title('Money spent per week number.')
plt.grid(True)
plt.savefig('leased_buses.png')
plt.show()