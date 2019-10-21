#!/usr/bin/python3

import matplotlib.pyplot as plt 

year = [1950,1970,1990,2010]
pop = [2.5,3.6,5.2,6.9]

plt.plot(year,pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],
['0','2B','4B','6B','8B','10B'])
plt.show()
