import matplotlib.pyplot as plt

"""
cubes plot exercises.  

"""

first_five = [1,2,3,4,5]
first_five_cubes = [1,8,27,64, 125]


plt.plot(first_five, first_five_cubes)
plt.show()

first_five_thousand = list(range(1,5001))
first_five_thousand_cubes = [x**3 for x in first_five_thousand]
plt.scatter(first_five_thousand, first_five_thousand_cubes, c=first_five_thousand_cubes, cmap=plt.cm.ocean)
plt.title("cube curve")
plt.xlabel("numbers")
plt.ylabel("cubes")
plt.savefig("colormapcubes.png",bbox_inches = 'tight')
plt.show()