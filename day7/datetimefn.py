#Explore more datetime function and uses in pandas
import pandas as pd
df=pd.DataFrame({'date':['2021-01-01','2021-01-02','2021-01-03','2021-01-04','2021-01-05']})

df['Date'] = pd.to_datetime(df['date'])

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day


today=pd.Timestamp.today()
df['days_difference'] = (today - df['Date'])

df['plus_one_day'] = df['Date'] + pd.Timedelta(days=1)


print(df)