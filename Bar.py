import numpy as np
import matplotlib.pyplot as plt

#Bar Chart 
data = {'C':20,'C++':15,'Java':30,'Python':35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))

plt.bar(courses,values,color='maroon',width=0.4)

plt.xlabel("Courses Offered")
plt.ylabel("No, Of students enrolled")
plt.title("students entrolled in different courses")
plt.show()