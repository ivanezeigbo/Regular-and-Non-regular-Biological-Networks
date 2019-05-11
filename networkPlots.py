import matplotlib.pyplot as plt

x = [64, 81, 100, 121, 144, 169, 196, 225, 256]

reg_div_pun = [45.66, 53.63, 45.35, 89.01, 121.52, 113.78, 135.94, 149.12, 161.08]
reg_hom_pun = [146.51, 184.44, 128.07, 248.45, 182.31, 184.05, 161.72, 217.72, 182.17]
reg_div_non = [9.67, 11.18, 25.21, 23.17, 29.56, 35.23, 45.13, 38.55, 53.56]
reg_hom_non = [47.76, 55.33, 80.78, 83.25, 63.37, 72.52, 76.19, 73.59, 70.8]

irreg_div_pun = [48.91, 67.15, 85.61, 109.2, 130.94, 127.92, 143.17, 167.25, 171.31]
irreg_hom_pun = [8.97, 20.11, -51.08, -8.39, -42.47, -14.44, 5.99, -20.09, 5.67]
irreg_div_non = [15.28, 16.89, 24.96, 30.41, 39.46, 49.84, 49.35, 60.91, 71.95]
irreg_hom_non = [56.42, 41.61, 49.39, 25.54, 66.29, 45.21, 49.18, 42.43, 36.1]


fig = plt.figure()

plt.plot(x, reg_div_pun, 'bo-', label='Regular Heterogeneous Network (Treatment)')
plt.plot(x, reg_hom_pun, 'ro-', label='Regular Homogeneous Network (Treatment)')
plt.plot(x, reg_div_non, 'go-', label='Regular Heterogeneous Network (Control)')
plt.plot(x, reg_hom_non, 'yo-', label='Regular Homogeneous Network (Control)')

plt.plot(x, irreg_div_pun, 'mo-.', label='Irregular Heterogeneous Network (Treatment)')
plt.plot(x, irreg_hom_pun, 'co-.', label='Irregular Homogeneous Network (Treatment)')
plt.plot(x, irreg_div_non, 'ko-.', label='Irregular Heterogeneous Network (Control)')
plt.plot(x, irreg_hom_non, 'o-.', label='Irregular Homogeneous Network (Control)')

fig.suptitle('Average Payoff for 64 <= N <= 256', fontsize=14)
plt.xlabel('Number of Agents (N)', fontsize=12)
plt.ylabel('Average Payoff', fontsize=12)
#fig.savefig('test.jpg')
fig.legend(loc='best')

plt.show()

x1 = [n for n in range(9)]
plt.plot(x1, x, 'bo-')
plt.plot(x1, irreg_div_pun, 'ro-')
plt.show()

