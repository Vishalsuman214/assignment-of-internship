import pandas as pd



df1 = pd.DataFrame({'id':[1,2,3], 'name':['a','b','c'], 'age':[25,30,35]})
df2 = pd.DataFrame({'id':[4,5,6], 'name':['d','e','f'], 'age':[40,45,50]})
df3 = pd.DataFrame({'id':[7,8,9], 'name':['g','h','i'], 'age':[55,60,65]})


concatenated_df = pd.concat([df1, df2], axis=0, ignore_index=True)
print("Concatenated DataFrame:")
print(concatenated_df)



merged_df = pd.merge(concatenated_df, df3, on='id', how='outer')
print("\nMerged DataFrame:")
print(merged_df)



# merge() offers more explicit control over the join keys (columns or indices) and defaults to an inner join.
# merge() more flaxible
# it combine columns


#join() defaults to index-based joining and performs a left join by default, making it convenient when indices are the natural join keys
# join() index-based 
# it combine index
