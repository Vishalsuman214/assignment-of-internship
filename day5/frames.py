import pandas as pd

#dataframe with a two dimensional list
list=[[1,'rahul'],[2,'priya'],[3,'ram'],[4,'prashant'],[5,'priyanka']]
df = pd.DataFrame(list, columns=['id', 'name'])
print(df)


#dataframe with a dictionary
dict={'name':['rahul','priya','ram','shubham','priyanka'],'age':[20,21,22,23,24],'city':['delhi','mumbai','pune','bangalore','hyderabad']}
df2 = pd.DataFrame(dict)
print("\n", df2)

#using list if lists
list=[['rahul',20,'delhi'],['ram',21,'mumbai'],['shubham',22,'pune'],['prashant',23,'bangalore'],['priyanka',24,'hyderabad']]
df3 = pd.DataFrame(list, columns=['name', 'age', 'city'])
print("\n", df3)

# using list of touples
list=[('pawan',20,'delhi'),('sachin',21,'mumbai'),('sanjay',22,'pune'),('prashant',23,'bangalore'),('priyanka',24,'hyderabad')]

df4 = pd.DataFrame(list)
print("\n", df4)


# using list of dictionaries
list=[{'name':'pawan','age':20,'city':'delhi'},{'name':'sachin','age':21,'city':'mumbai'},{'name':'sanjay','age':22,'city':'pune'},{'name':'prashant','age':23,'city':'bangalore'},{'name':'priyanka','age':24,'city':'hyderabad'}]

df5 = pd.DataFrame(list)
print("\n", df5)