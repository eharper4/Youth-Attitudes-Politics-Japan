import numpy as np
import matplotlib.pyplot as plt

#https://prtimes.jp/main/html/rd/p/000000036.000087626.html used data from this website
#Q : 政治に対して、「自分事・自分に直接関係のあること」として関心がありますか？
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
opinions = ['Concerned', 'Somewhat Concerned', 'Not very concerned', 'Not concerned'] #opinions=how much do politics concern you?
youth = [180.9,192.78,104.22,62.1] #in the study, 'Youth' are defined as under 30 years old. 540 members
ax.bar(opinions,youth)
plt.show()

#https://prtimes.jp/main/html/rd/p/000000036.000087626.html
#Using the same theme from above, let's expand the ages
#each line represents ppl under 20, in their 30s, and in their 40s, respectively. Each age group contains 90 participants. 
data = [[15.03, 35.01, 17.01, 23.04],
[23.04, 20.97, 29.97, 16.02],
[27, 35.01, 17.01, 10.98]]
colors = ['b', 'g', 'y']

X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

# Commented out these guys for now.
# ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
# ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
# ax.bar(X + 0.50, data[2], color = 'y', width = 0.25)

# Some minor refactoring.
# This is a for loop that uses an index.
# This should be good practice for a `for` loop if you're not familiar with them yet!
# For loops are used a LOT with arrays.
for index, item in enumerate(data):
  print(index)
  ax.bar(X + (index * 0.25), data[index], color = colors[index], width = 0.25)
  
  
plt.show()
