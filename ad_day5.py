import pandas as pd 
study_hour=[1,2,3,4]
practice_hour=[5,4,6,7]
name_of_student=["manikanta","kranti","john","priya"]
dict1={
    "study_hour":study_hour,
    "practice_hour":practice_hour,
    "name_of_student":name_of_student
}
print(dict1)
df=pd.DataFrame(dict1)
print(df)