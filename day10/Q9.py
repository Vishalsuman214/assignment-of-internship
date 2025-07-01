import matplotlib.pyplot as plt


subjects = ['Math', 'Python', 'CN', 'DBMS']
sem1 = [78, 85, 82, 80]
sem2 = [88, 90, 85, 86]

x = range(len(subjects))

plt.plot(x, sem1, marker='o', label='Semester 1')
plt.plot(x, sem2, marker='s', label='Semester 2')

plt.xticks(x, subjects)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Semester Result Comparison")
plt.legend()
plt.show()
