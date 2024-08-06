import pandas as pd
df=pd.read_csv('adult.csv')
df.head()

#How many people of each race are represented in this dataset? 
#This should be a Pandas series with race names as the index labels. (race column)
race_counts=df['race'].value_counts()
print(race_counts)



#average men What is the average age of men?
avg_men=df[df['gender']=='Male']
average=avg_men['age'].mean()
print(average)



#What is the percentage of people who have a Bachelor's degree?
bachelors_count = df[df['education'] == "Bachelors"].shape[0]
total=len(df)
# Calculating the percentage
percentage_bachelors = (bachelors_count / total) * 100
print(percentage_bachelors)

#What percentage of people with advanced education 
#(Bachelors, Masters, or Doctorate) make more than 50K?

advance=df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
new_adv=advance[advance['income']==">50K"]
updated=len(new_adv)/len(advance)*100
print(updated)


#What percentage of people without advanced education make more than 50K?

advanced=df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]
new_advanced=advanced[advanced['income']==">50K"]
updated_value=len(new_advanced)/len(advanced)*100
print(updated_value)

#What is the minimum number of hours a person works per week?
min_hrs=df['hours-per-week'].min()
print(min_hrs) 

#What percentage of the people who work 
#the minimum number of hours per week have a salary of more than 50K? 

min_hours_per_week = df['hours-per-week'].min()
min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
high_income_min_hours_workers = min_hours_workers[min_hours_workers['income'] ==">50K"]
percentage_high_income_min_hours = (len(high_income_min_hours_workers) / len(min_hours_workers)) * 100
print(percentage_high_income_min_hours)


#What country has the highest percentage of people that earn >50K and what is that percentage?
high_income = df[df['income'] ==">50K"]
total_by_country = df['native-country'].value_counts()
high_income_by_country = high_income['native-country'].value_counts()
percentage_high_income_by_country = (high_income_by_country / total_by_country) * 100
max_percentage_country = percentage_high_income_by_country.idxmax()
max_percentage = percentage_high_income_by_country.max()
print(max_percentage_country)


#Identify the most popular occupation for those who earn >50K in India.
high_amt=df[(df['income'] ==">50K") & (df['native-country'] == 'India')]
occ=high_amt['occupation'].mode()[0]
print(occ)