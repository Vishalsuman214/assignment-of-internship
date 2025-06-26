import pandas as pd

df=pd.DataFrame({
    'email':['user1@example.com', 'user2@example.com'],
    'mobile':['9876543210', '999@99999'],
    'city':['Delhi', 'Mumbai234'],
    'price':['$40*','$50 added'],
    'pasword':['hello@123', 'hello123']
    
})
df['mobile'] = df['mobile'].str.replace(r'\D','', regex=True)
df['city'] = df['city'].str.replace(r'[^a-zA-Z]','', regex=True)
df['price'] = df['price'].str.replace(r'\D','', regex=True).astype(int)
df['pasword'] = df['pasword'].str.replace(r'\W','', regex=True)
df['email'] = df['email'].str.replace(r'@.*','', regex=True)

    
print(df)

