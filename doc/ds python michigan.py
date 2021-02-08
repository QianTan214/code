


*************************************************************************************
Week 1
*************************************************************************************




unpack tuples


format
# ===================================================================================

print('{}.{}.{}'.format(.,.,.,)




csv
# ===================================================================================

import csv
with open ('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
mpg[:3]



date and times
# ===================================================================================

import datetime as dt
import time as tm
tm.time()

dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow

dtnow.year
dtnow.month
dtnow.hour
dtnow.second


delta = dt.timedelta(days = 100)
delta

today = dt.date.today()
today - delta




map
# ===================================================================================

camel case

map returns a map object

map(function,iterable)

eg.
store1 = [10,5,4,5]
store2 = [5,6,5,3]
cheapest = map(min,store1,store2)
cheapest
for i in cheapest:
    print(i)


eg.
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))





lambda
# ===================================================================================

func = lambda a,b,c:a+b
func(1,2,3)

eg.
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x:x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda x: x.split()[0] + ' ' + x.split()[-1],people))

答案：
True
True
True
True
True





list comprehension
# ===================================================================================

l = [num for num in range(0,1000) if num % 2 == 0]

list comprehension is faster


eg.
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [i*j for i in range(10) for j in range(10)]

答案：
True



eg.
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids





numpy
# ===================================================================================

# Array Creation

import numpy as np

a = np.array([1,2,3])
print(a)
print(a.ndim)
a.dtype


import numpy as np

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
print(b.shape)


c = np.array([1.1,2.2,3])
c.dtype.name

d = np.zeros((2,3))
e = np.ones((2,3))

np.random.rand(2,3)
f = np.arange(10,50,2) # note it is arange
np.linspace(0,2,15)


# Array Operations

A = np.array([1,2,3,4])
B = np.array([10,20,30,40])
C = A-B
D = A*B

# elementwise and matrix product
a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
print(a*b)
print(a@b)

# upcasting

# mean, min, max
print(a.sum())
print(b.sum())
print(a.mean())

b = np.arange(1,16,1).reshape(3,5)



# Image Library

# PIL - python image library
from PIL import Image
from IPython.display import display
im = Image.open('1.JPG')
display(im)

# convert image to array
array = np.array(im)
print(array.shape)
array

mask = np.full(array.shape,255)

modified_array = array - mask
modified_array = modified_array*-1
modified_array = modified_array.astype(np.uint8)
modified_array


display(Image.fromarray(modified_array))

reshaped = np.reshape(modified_array,(1000,4000))
print(reshaped.shape)
display(Image.fromarray(reshaped))

# Indexing, Slicing and Iterating

a = np.array([[1,2],[3,4],[5,6]])
a[1,1]

print(a[[0,1,2],[0,1,1]]) # ????????????????????????????
print(a>5)
print(a[a>5]) # boolean masking


a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a[:2,1:3] # first argument is row, second is column


# Trying Numpy with Datasets

# genfromtxt function
wines = np.genfromtxt("datasets/winequality-red.csv", delimiter=";", skip_header = 1) 
wines[:,0]
wines[:,0:1]
wines[:,0:3]
wines[:,[0,2,4]]
wines[:,-1].mean() # mean of last column


graduate_admission = np.genfromtxt('dataset/Admission_Predict.csv', dtype=None, delimiter=",", skip_header=1, 
    names=('Series_No', 'GRE_Score', 'TOEFL_Score', 'University_Rating', 'SOP', 
    'LOR', 'CGPA', 'Research', 'Chance_of_Admit'))

graduate_admission.shape
graduate_admission['CGPA'][0:5]
len(graduate_admission[graduate_admission['Research'] == 1]) # boolean masking布尔过滤

print(graduate_admission[graduate_admission['Chance_of_Admit']>0.8]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit']>0.4]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit']<0.4]['GRE_Score'].mean())


head
tail






Regular Expression
# ===================================================================================

import re

text = "this is a good day"
re.search("good",text)

text = 'amy works diligently. amy gets good grades. our student amy is successful'
re.split("amy",text)

re.findall("amy",text)

text = 'amy works diligently. amy gets good grades. our student amy is successful'

re.search("^amy",text) # search returns a re.Match object



Patterns and Character Classes
# ===================================================================================

grades = "ACAAAABABCABBC"
re.findall("B",grades)

re.findall("[AB]",grades) # use square brackets

re.findall("[A][B-C]",grades) # [] set notation

re.findall("AB|AC",grades) # pipe operator, OR

re.findall("[^A]",grades)

re.findall("^[^A]",grades)




Quantifier
# ===================================================================================

re.findall("A{2,10}",grades)

re.findall("A{1,1}A{1,1}",grades)

re.findall("AA",grades) # default {1,1}



re.findall("A{2,2}A{2,2}",grades)

re.findall("A{2}",grades) # one value 2 for both

re.findall("A{1,10}B{1,10}C{1,10}",grades)

# quantifiers
# * sign 0 or more times
# ? sign one or more times
# + sign one or more times
with open("Week 1/ferpa.txt","r") as file:
    wiki = file.read()
wiki

re.findall("[a-zA-Z]{1,100}\[edit\]",wiki) # use \ to escape [] sign

# \w refers to any letter or digit
re.findall("[\w]{1,100}\[edit\]",wiki)

# \s refers to any whitespace character

re.findall("[\w]*\[edit\]",wiki) # * removes the 100 limit

re.findall("[\w ]*\[edit\]",wiki) # space after \w 

for title in re.findall("[\w ]*\[edit\]",wiki):
    print(re.split("[\[]]",title)[0])




Groups
# ===================================================================================


# group notation ()
import re
re.findall("([\w ]*)(\[edit\])",wiki)

for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())

for item in re.finditer("([\w ]*)(\[edit\])",wiki): # finditer
    print(item.group(1)) # group(0) is the whole match

# <> angle brackets

for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    print(item.groupdict()['title'])

print(item.groupdict())

# . refers to single character, which is not a newline
# \d refers to any digit
# \s refers to any whitespace character, like spaces and tabs

## Look-ahead and Look-behind

for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])",wiki):
    print(item)



Example: Wikipedia Data
# ===================================================================================
    

# Let's look at some more wikipedia data. Here's some data on universities in the US which are buddhist-based
import re
with open("Week 1/buddhist.txt","r",encoding='utf-8') as file:
    wiki=file.read()
wiki

pattern="""
(?P<title>.*)        #the university title
(–\ located\ in\ )   #an indicator of the location
(?P<city>\w*)        #city the university is in
(,\ )                #separator for the state
(?P<state>\w*)       #the state the city is located in"""

# Now when we call finditer() we just pass the re.VERBOSE flag as the last parameter, this makes it much
# easier to understand large regexes!
for item in re.finditer(pattern,wiki,re.VERBOSE):
    # We can get the dictionary returned for the item with .groupdict()
    print(item.groupdict())

# pound sign or hash mark




Example: New York Times and Hashtags
# ===================================================================================


# Here's another example from the New York Times which covers health tweets on news items. This data came from
# the UC Irvine Machine Learning Repository which is a great source of different kinds of data
with open("Week 1/nytimeshealth.txt","r",encoding='utf-8') as file:
    health=file.read()
health

pattern = '#[\w\d]*(?=\s)'
re.findall(pattern, health)

# We can see here that there were lots of ebola related tweeks in this particular dataset.












*************************************************************************************
Week 2
*************************************************************************************



Week 2
# ===================================================================================

2.1 Introduction to Pandas
# ===================================================================================

samples = np.random.normal(size=(4, 4))
samples



2.2 Series Data Structure
# ===================================================================================

# Python Bytes Podcast
# Data Skeptic Podcast

# One of the primary panda data types - Series

import pandas as pd

from random import normalvariate
N = 1000000
%timeit samples = [normalvariate(0, 1) for _ in range(N)]
%timeit np.random.normal(size=N)

students = ['alice','bob','charlie']

np.rdandom.seed(1234)

pd.Series(students)

rng = np.random.RandomState(1234)
rng.randn(10)

numbers = [1,2,3]

pd.Series(numbers)

# how Numpy and Pandas handle missing data

students = ['alice','bob', None]

pd.Series(students)

numbers = [1,2,None]

pd.Series(numbers) # NaN is not a number

# equality test between NaN and None

import numpy as np
np.nan == None

np.nan == np.nan # equality test to NaN itself

# numpy library isnan()
np.isnan(np.nan)

students_score = {'alice':'pphysics',
                 'bob':'chemistry',
                 'charlie':'english'}

s= pd.Series(students_score)
s

s.index # index object

students = [('alice','brown'), ('bob','white'),('charlie','green')]

pd.Series(students)

s = pd.Series(['physics','chemistry','english'],index = ['alice','bob','charlie'])
s

students_score = {'alice':'pphysics',
                 'bob':'chemistry',
                 'charlie':'english'}
s = pd.Series(students_score,index = ['alice','bob','sam'])
s



2.3 Query a Series
# ===================================================================================

# to query by numeric location,use iloc.
# to query by index label, use loc
# user [], indexing operator

# safer to use loc and iloc than use for instance [1],[2] ...

class_code = {99: 'physics',
             100: 'chemistry',
             101: 'english',
             102: 'historty'}
s = pd.Series(class_code)
s

s[0]

# in this case, s[0] will get an error

grades = pd.Series([90,80,70,60]) # works but slow
total = 0
for grade in grades:
    total += grade
print(total/len(grades))

import numpy as np
total = np.sum(grades)
print(total/len(grades))

# demonstrate which method is faster

numbers = pd.Series(np.random.randint(0,1000,10000)) # 10000 number of numbers between 0 and 1000
numbers.head()

len(numbers)

# magic functions % and click tab

# timeit function

%%timeit -n 100
total = 0
for number in numbers:
    total += number
total/len(numbers)

%%timeit -n 100
total = np.sum(numbers)
total/len(numbers)

# broadcasting

numbers.head()

numbers+=2
numbers.head()

# iteritem function

for label, value in numbers.iteritems(): # ??????????????????????
    numbers.at(label, value+2)
numbers.head()

%%timeit -n 10
s =pd.Series(np.random.randint(0,1000,10000))
for label, value in s.iteritems():
    s.loc[label] = value+2

# now try broadcasting method, much faster and concise

%%timeit -n 10
s =pd.Series(np.random.randint(0,1000,10000))
s+=2

s = pd.Series([1,2,3]) # mixed indexes
s.loc['history'] = 101
s

students_classes = pd.Series({'alice':'physics',
                 'bob':'chemistry',
                 'charlie':'english'})
students_classes

# the same indexes
kelly_classes = pd.Series(['philosopohy','arts','maths'],index=['kelly','kelly','kelly'])
kelly_classes

all_students_classes = students_classes.append(kelly_classes)
all_students_classes

students_classes # original Series doesnt change

all_students_classes.loc['kelly']




DataFrame

2.4 DataFrame Data Structure
# ===================================================================================

# index and multiply columns

import pandas as pd

record1 = ({'name':'alice',
           'class':'physics',
           'score':85})
record2 = ({'name':'bob',
           'class':'chemistry',
           'score':82})
record3 = ({'name':'helen',
           'class':'biology',
           'score':90})

df = pd.DataFrame([record1,record2,record3],index=['school1','school2','school1'])
df.head()

df.head()

# alt

students = [{'name':'alice',
           'class':'physics',
           'score':85},
            {'name':'bob',
           'class':'chemistry',
           'score':82},
            {'name':'helen',
           'class':'biology',
           'score':90}]

df = pd.DataFrame(students, index = ['school1','school2','school1'])
df.head()

# loc and iloc

df.loc['school2'] # return series

type(df.loc['school2'])

df.loc['school1']

type(df.loc['school1'])

df.loc['school1','name']

# transpose matrix

df.T

df.T.loc['name']

# df.loc[column_name] will get an error

# .loc always row selection

df['name']

df.loc(['school1'])

type(df['name'])

# chain operation together, better not use this method
df.loc['school1']['name']

print(type(df.loc['school1']))
print(type(df.loc['school1']['name']))


df.loc[:,['name','score']]

# drop operation, keep the original dataframe

df.drop('school1')

df

# drop has 2 optional parameters, inplace and axes. if inplace is true, dataframe will be updated
# instead of returning a copy. axis is 0 by default which means row axis. you can change to 1 if you want to
# drop a column

copy_df = df.copy()
copy_df

copy_df.drop('name',inplace=True,axis=1)
copy_df

# second method del

copy_df = df.copy()
copy_df

del copy_df['class']
copy_df

# adding new columns

df['classranking'] = None
df



2.5 DataFrame Indexing and Loading
# ===================================================================================

# import csv file into dataframe

# !后面是shell command

!cat Admission_Predict.csv

import pandas as pd
df=pd.read_csv('Week 2/Admission_Predict.csv')

df.head()

# index_col() function
df = pd.read_csv('Week 2/Admission_Predict.csv',index_col=0) # Serial No. as the row index

df.head()

# rename() function
new_df = df.rename(columns={'GRE Score':'GRE Score', 'SOP':'Statement of Purpose'})
new_df.head()

# check dataframe column names
# .columns is not a function, just an attribute
# note 'LOR ' there is a space
new_df.columns 

# strip() function, removes whitespaces
new_df = new_df.rename(mapper=str.strip, axis='columns')
new_df.head()

# rename() function doesnt change original dataframe

# alternative way of renaming
# change the original dataframe

cols = list(df.columns) # convert to a list

cols = [x.lower().strip() for x in cols]
df.columns = cols
df.head()

# can load other formats into dataframe, such as html web pages, databases, and other file formats
# csv file is the most common data format by far





2.6 Query a DataFrame
# ===================================================================================

# Series 1D, DataFrame 2D

# boolean masking, like bit masking
import pandas as pd
df=pd.read_csv('Week 2/Admission_Predict.csv')
df.head()

# index_col() function
df = pd.read_csv('Week 2/Admission_Predict.csv',index_col=0) # Serial No. as the row index
df.head()

df.columns

df.columns = [x.lower().strip() for x in df.columns]
df.head()

admit_mask=df['chance of admit'] > 0.7
admit_mask

# where() function
df.where(admit_mask).head()

# dropna() function
df.where(admit_mask).dropna().head()

# where() and dropna() combined

df[df['chance of admit']>0.7].head()

# It can be called with a string parameter to project a single column
df["gre score"].head()

# Or you can send it a list of columns as strings
df[["gre score","toefl score"]].head()

# Or you can send it a list of columns as strings
df[["gre score","toefl score"]].head()

# can not use and, have to use &
(df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9)

# error, have to use ()
df['chance of admit'] > 0.7 & df['chance of admit'] < 0.9

# gt() and lt() functions
df['chance of admit'].gt(0.7) & df['chance of admit'].lt(0.9)

# can chain gt() and lt()

df['chance of admit'].gt(0.7).lt(0.9)




2.7 Indexing DataFrames
# ===================================================================================

# row is axis 0, column is axis 1

# set_index() function, doesnt keep original index

import pandas as pd
df=pd.read_csv('Week 2/Admission_Predict.csv',index_col=0)
df.head()

# So we copy the indexed data into its own column
df['Serial Number'] = df.index
# Then we set the index to another column
df = df.set_index('Chance of Admit ')
df.head()

# reset_index() function removes index

df = df.reset_index()
df.head()

# multi-level indexing

# census dataset

df = pd.read_csv('Week 2/census.csv')
df.head()

# unique() function
df['SUMLEV'].unique()

df = df[df['SUMLEV']==50]
df.head()

columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012','BIRTHS2013',
                   'BIRTHS2014','BIRTHS2015','POPESTIMATE2010','POPESTIMATE2011',
                   'POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
df = df[columns_to_keep]
df.head()

df = df.set_index(['STNAME','CTYNAME'])
df.head()

# loc can take multiple arguments
df.loc['Michigan', 'Washtenaw County']

# create a list as index
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]

# I don't tend to use hierarchical indicies very much, 
# and instead just keep everything as columns and manipulate those.




2.8 Missing Values
# ===================================================================================

import pandas as pd

# Pandas is pretty good at detecting missing values directly from underlying data formats, like CSV files.
# Although most missing valuse are often formatted as NaN, NULL, None, or N/A, sometimes missing values are
# not labeled so clearly. For example, I've worked with social scientists who regularly used the value of 99
# in binary categories to indicate a missing value. The pandas read_csv() function has a parameter called
# na_values to let us specify the form of missing values. It allows scalar, string, list, or dictionaries to
# be used.

# Let's load a piece of data from a file called log.csv
df = pd.read_csv('Week 2/class_grades.csv')
df.head(10)

# isnull() function

mask = df.isnull()
mask.head(10)

# dropna() function
df.dropna().head(10)

# fillna() function

df.fillna(0,inplace=True)
df.head(10)

# log.csv file

df = pd.read_csv('Week 2/log.csv')
df.head(20)

# sort by index or by values

# sorted timestamp
df = df.set_index('time')
df = df.sort_index()
df.head()

# If we look closely at the output though we'll notice that the index 
# isn't really unique. Two users seem to be able to use the system at the same 
# time. Again, a very common case. Let's reset the index, and use some 
# multi-level indexing on time AND user together instead,
# promote the user name to a second level of the index to deal with that issue.

df = df.reset_index()
df = df.set_index(['time', 'user'])
df

# ffill method, forward filling
df = df.fillna(method='ffill')
df.head()

# replace() function

df = pd.DataFrame({'A': [1, 1, 2, 3, 4],
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
df

df.replace(1,100)

# change 2 values

df.replace([1, 3], [100, 300])

df = pd.read_csv('Week 2/log.csv')
df.head()

# replace() parameters
df.replace(to_replace='.*.html$',value='webpage',regex=True)

# One last note on missing values. 
# When you use statistical functions on DataFrames, these functions typically ignore missing values. 
# For instance if you try and calculate the mean value of a DataFrame, 
# the underlying NumPy function will ignore missing values. 





2.9 Example: Manipulating DataFrame
# ===================================================================================

import pandas as pd
df=pd.read_csv("Week 2/presidents.csv")
df.head()

# there is a bunch of footnotes in the "Born" column which might cause issues. 
# Let's start with cleaning up that name into firstname and lastname. I'm going to tackle this with
# a regex. So I want to create two new columns and apply a regex to the projection of the "President" column.

# Here's one solution, we could make a copy of the President column
df["First"]=df['President']
# Then we can call replace() and just have a pattern that matches the last name and set it to an empty string
df["First"]=df["First"].replace("[ ].*", "", regex=True) # [] refers to whitespace characters
df.head()

del(df['First']) # drop column inplace

df.head()

# use apply() function instead this time

# write a function

def splitname(row): # row is a single Series object
    row['First']=row['President'].split(" ")[0]
    row['Last']=row['President'].split(" ")[-1]
    return row
df = df.apply(splitname,axis='columns')
df.head()

# extract() function

del([df['First']])

del([df['Last']])

df.head()

# Series.str,extract()

pattern="(^[\w]*)(?:.* )([\w]*$)" # ??????????????

df['President'].str.extract(pattern).head()

pattern="(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)"

names=df["President"].str.extract(pattern).head()
names

# create new columns First and Last
df["First"]=names["First"]
df["Last"]=names["Last"]
df.head()

df["Born"]=df["Born"].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
df["Born"].head()

# to_datetime() function
df["Born"]=pd.to_datetime(df["Born"])
df["Born"].head()










*************************************************************************************
Week 3
*************************************************************************************


3.1 Merging DataFrames
# ===================================================================================

![Venn Diagram](merging1.png) # ?????????????

# Venn Diagram

![Union](merging2.png)

import pandas as pd

import pandas as pd

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])

staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])

student_df = student_df.set_index('Name')

print(staff_df.head())
print(student_df.head())

pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)

pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)

pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)

pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)

# We can also do it another way. The merge method has a couple of other interesting parameters. First, you
# don't need to use indices to join on, you can use columns as well. Here's an example. Here we have a
# parameter called "on", and we can assign a column that both dataframe has as the joining column

# First, lets remove our index from both of our dataframes
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

# Now lets merge using the on parameter
pd.merge(staff_df, student_df, how='right', on='Name')

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 
                          'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 
                            'Location': '512 Wilson Crescent'}])
pd.merge(staff_df, student_df, how='left', on='Name')

# above _x refers to left, _y refers to right

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 
                          'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 
                          'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 
                          'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 
                            'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 
                            'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 
                            'School': 'Engineering'}])

pd.merge(staff_df, student_df, how='inner', on=['First Name','Last Name'])

# merging refers to horizontal operation, concatenate refers to vertical top bottom

# %% magic function starts with %%

%%capture # supress warning messages
df_2011 = pd.read_csv("Week 3/college_scorecard/MERGED2011_12_PP.csv", error_bad_lines=False)
df_2012 = pd.read_csv("Week 3/college_scorecard/MERGED2012_13_PP.csv", error_bad_lines=False)
df_2013 = pd.read_csv("Week 3/college_scorecard/MERGED2013_14_PP.csv", error_bad_lines=False)

df_2011.head(3)

print(len(df_2011))
print(len(df_2012))
print(len(df_2013))

# concat() function

frames = [df_2011, df_2012, df_2013]
pd.concat(frames)

len(df_2011)+len(df_2012)+len(df_2013)

# concat() function has parameter 'keys'
pd.concat(frames, keys=['2011','2012','2013'])

# Now we have the indices as the year so we know what observations are from what year. You should know that
# concatenation also has inner and outer method. If you are concatenating two dataframes that do not have
# identical columns, and choose the outer method, some cells will be NaN. If you choose to do inner, then some
# observations will be dropped due to NaN values. You can think of this as analogous to the left and right
# joins of the merge() function.

Now you know how to merge and concatenate datasets together. You will find such functions very useful for combining data to get more complex or complicated results and to do analysis with. A solid understanding of how to merge data is absolutely essentially when you are procuring, cleaning, and manipulating data. It's worth knowing how to join different datasets quickly, and the different options you can use when joining datasets, and I would encourage you to check out the pandas docs for joining and concatenating data.





3.2 Pandas Idioms
# ===================================================================================

# idiomatic python

# vectorisation over iterative loops

# pandorable

# method chaining

import pandas as pd
import numpy as np
import timeit

df = pd.read_csv('Week 3/census.csv')
df.head()

# The first of the pandas idioms I would like to talk about is called method chaining. The general idea behind
# method chaining is that every method on an object returns a reference to that object. The beauty of this is
# that you can condense many different operations on a DataFrame, for instance, into one line or at least one
# statement of code.

# Here's the pandorable way to write code with method chaining. In this code I'm going to pull out the state
# and city names as a multiple index, and I'm going to do so only for data which has a summary level of 50,
# which in this dataset is county-level data. I'll rename a column too, just to make it a bit more readable.
(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

# where() doesnt drop missing values by default

# 上面多个语句要加括号，用多个'.'连接

# 下面是非pandorable way来执行上例
# First create a new dataframe from the original
df = df[df['SUMLEV']==50] # I'll use the overloaded indexing operator [] which drops nans
# Update the dataframe to have a new index, we use inplace=True to do this in place
df.set_index(['STNAME','CTYNAME'], inplace=True)
# Set the column names
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})

# compare pandorable and non-pandorable way

# Lets write a wrapper for our first function
def first_approach():
    global df
    # And we'll just paste our code right here
    return (df.where(df['SUMLEV']==50)
             .dropna()
             .set_index(['STNAME','CTYNAME'])
             .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

# Read in our dataset anew
df = pd.read_csv('Week 3/census.csv')

# And now lets run it
timeit.timeit(first_approach, number=10)

# this method is much faster, but it is time-readability trade-off
def second_approach():
    global df
    new_df = df[df['SUMLEV']==50]
    new_df.set_index(['STNAME','CTYNAME'], inplace=True)
    return new_df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})

# Read in our dataset anew
df = pd.read_csv('Week 3/census.csv')

# And now lets run it
timeit.timeit(second_approach, number=10)

# python function map()
# pandas function applymap(), rarely used
# use pandas function apply() heavily

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

df.apply(min_max, axis='columns').head()

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    # Create a new entry for max
    row['max'] = np.max(data)
    # Create a new entry for min
    row['min'] = np.min(data)
    return row
# Now just apply the function across the dataframe
df.apply(min_max, axis='columns')

# apply() heavily used with lambdas()

# 1 is columns, 0 is rows

rows = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013','POPESTIMATE2014', 
        'POPESTIMATE2015']
# Now we'll just apply this across the dataframe with a lambda
df.apply(lambda x: np.max(x[rows]), axis=1).head() # 可以写1，也可以写'column'

# The beauty of the apply function is that it allows flexibility in doing whatever manipulation that you
# desire, as the function you pass into apply can be any customized however you want. Let's say we want to
# divide the states into four categories: Northeast, Midwest, South, and West We can write a customized
# function that returns the region based on the state the state regions information is obtained from Wikipedia

def get_state_region(x):
    northeast = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 
                 'Rhode Island','Vermont','New York','New Jersey','Pennsylvania']
    midwest = ['Illinois','Indiana','Michigan','Ohio','Wisconsin','Iowa',
               'Kansas','Minnesota','Missouri','Nebraska','North Dakota',
               'South Dakota']
    south = ['Delaware','Florida','Georgia','Maryland','North Carolina',
             'South Carolina','Virginia','District of Columbia','West Virginia',
             'Alabama','Kentucky','Mississippi','Tennessee','Arkansas',
             'Louisiana','Oklahoma','Texas']
    west = ['Arizona','Colorado','Idaho','Montana','Nevada','New Mexico','Utah',
            'Wyoming','Alaska','California','Hawaii','Oregon','Washington']
    
    if x in northeast:
        return "Northeast"
    elif x in midwest:
        return "Midwest"
    elif x in south:
        return "South"
    else:
        return "West"

df['state_region'] = df['STNAME'].apply(lambda x: get_state_region(x))

df[['STNAME','state_region']].head()






3.3 Group by
# ===================================================================================

## 3.3.1 Splitting

# Let's look at some US census data
df = pd.read_csv('Week 3/census.csv')
df.head()

df['SUMLEV']==50

df[df['SUMLEV']==50].head()

df = df[df['SUMLEV']==50]
df.head()

df['STNAME'].head(5)

df['STNAME'].unique()

%%timeit -n 3

for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + 
          ' have an average population of ' + str(avg))

# use groupby(), groupby() returns a tuple

%%timeit -n 3
# For this method, we start by telling pandas we're interested in grouping by state name, this is the "split"
for group, frame in df.groupby('STNAME'):
    # You'll notice there are two values we set here. groupby() returns a tuple, where the first value is the
    # value of the key we were trying to group by, in this case a specific state name, and the second one is
    # projected dataframe that was found for that group
    
    # Now we include our logic in the "apply" step, which is to calculate an average of the census2010pop
    avg = np.average(frame['CENSUS2010POP'])
    # And print the results
    print('Counties in state ' + group + 
          ' have an average population of ' + str(avg))

# Let's look at some US census data
df = pd.read_csv('Week 3/census.csv')
df.head()

df = df.set_index('STNAME')
df.head()

# Let's look at some US census data
df = pd.read_csv('Week 3/census.csv')
df.head()

# Let's look at some US census data
df = pd.read_csv('Week 3/census.csv')
# And exclude state level summarizations, which have sum level value of 40
df = df[df['SUMLEV']==50]
df.head()

# Now, 99% of the time, you'll use group by on one or more columns. But you can also provide a function to
# group by and use that to segment your data.

# This is a bit of a fabricated example but lets say that you have a big batch job with lots of processing and
# you want to work on only a third or so of the states at a given time. We could create some function which
# returns a number between zero and two based on the first character of the state name. Then we can tell group
# by to use this function to split up our data frame. It's important to note that in order to do this you need
# to set the index of the data frame to be the column that you want to group by first.

# We'll create some new function called set_batch_number and if the first letter of the parameter is a capital
# M we'll return a 0. If it's a capital Q we'll return a 1 and otherwise we'll return a 2. Then we'll pass
# this function to the data frame

df = df.set_index('STNAME')

def set_batch_number(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

# The dataframe is supposed to be grouped by according to the batch number And we will loop through each batch
# group
for group, frame in df.groupby(set_batch_number):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

# new example

import pandas as pd
import numpy as np
df=pd.read_csv("Week 3/listings.csv")
df.head()

# So, how would I group by both of these columns? A first approach might be to promote them to a multiindex
# and just call groupby()
df=df.set_index(["cancellation_policy","review_scores_value"])

# When we have a multi-index we need to pass in the levels we are interested in grouping by
for group, frame in df.groupby(level=(0,1)):
    print(group)

def grouping_fun(item):
    # Check the "review_scores_value" portion of the index. item is in the format of
    # (cancellation_policy,review_scores_value
    if item[1] == 10.0:
        return (item[0],"10.0")
    else:
        return (item[0],"not 10.0")

for group, frame in df.groupby(by=grouping_fun):
    print(group)

df.head()

## 3.3.2 Aggregation

df=df.reset_index()
df.head()

# .agg() deprecated

df.groupby("cancellation_policy").agg({"review_scores_value":np.average})

# np.nanmean, ignore nan values
df.groupby("cancellation_policy").agg({"review_scores_value":np.nanmean})

# groupby generates an object, then apply agg() function on the object

# Take a moment to make sure you understand the previous cell, since it's somewhat complex. First we're doing
# a group by on the dataframe object by the column "cancellation_policy". This creates a new GroupBy object.
# Then we are invoking the agg() function on that object. The agg function is going to apply one or more
# functions we specify to the group dataframes and return a single row per dataframe/group. When we called
# this function we sent it two dictionary entries, each with the key indicating which column we wanted
# functions applied to. For the first column we actually supplied a tuple of two functions. Note that these
# are not function invocations, like np.nanmean(), or function names, like "nanmean" they are references to
# functions which will return single values. The groupby object will recognize the tuple and call each
# function in order on the same column. The results will be in a heirarchical index, but since they are
# columns they don't show as an index per se. Then we indicated another column and a single function we wanted
# to run.

## 查看列名的方法

df=pd.read_csv("Week 3/listings.csv")
df.head(1)

# 下面是查看所有列名的多种语法

print(df.columns.values)

# list(df)

print(df.columns.tolist())

## 3.3.3 Transformation

# agg() returns 1 value per column, transform() returns an object that is the same size as the group.

# First, lets define just some subset of columns we are interested in
cols=['cancellation_policy','review_scores_value']
# Now lets transform it, I'll store this in its own dataframe
transform_df=df[cols].groupby('cancellation_policy').transform(np.nanmean)
transform_df.head()

transform_df.rename({'review_scores_value':'mean_review_scores'}, axis='columns', inplace=True)
df=df.merge(transform_df, left_index=True, right_index=True)
df.head()

df['mean_diff']=np.absolute(df['review_scores_value']-df['mean_review_scores'])
df['mean_diff'].head()

## 3.3.4 Filtering

df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value'])>9.2)

## 3.3.5 Applying

df=pd.read_csv("Week 3/listings.csv")
df=df[['cancellation_policy','review_scores_value']]
df.head()

# In previous work we wanted to find the average review score of a listing and its deviation from the group
# mean. This was a two step process, first we used transform() on the groupby object and then we had to
# broadcast to create a new column. With apply() we could wrap this logic in one place
def calc_mean_review_scores(group):
    # group is a dataframe just of whatever we have grouped by, e.g. cancellation policy, so we can treat
    # this as the complete dataframe
    avg=np.nanmean(group["review_scores_value"])
    # now broadcast our formula and create a new column
    group["review_scores_mean"]=np.abs(avg-group["review_scores_value"])
    return group

# Now just apply this to the groups
df.groupby('cancellation_policy').apply(calc_mean_review_scores).head()




3.4 Scales
# ===================================================================================

# ratio scale: like heights and weights
# interval scale: there is no true zero
# ordinal scale: letter grades such as A+, A, B, C
# nominal scale: categories of data, but have no order with respect to one another, such as teams of sports

import pandas as pd

df=pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 
                       'ok', 'ok', 'ok', 'poor', 'poor'],
               columns=["Grades"])
df

df.dtypes

df['Grades'].astype('category').head()

my_categories=pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], 
                           ordered=True)
# then we can just pass this to the astype() function
grades=df["Grades"].astype(my_categories)
grades.head()

# Now we see that pandas is not only aware that there are 11 categories, but it is also aware of the order of
# those categoreies. So, what can you do with this? Well because there is an ordering this can help with
# comparisons and boolean masking. For instance, if we have a list of our grades and we compare them to a “C”
# we see that the lexicographical comparison returns results we were not intending. 

df[df["Grades"]>"C"]

# Sometimes it is useful to represent categorical values as each being a column with a true or a false as to
# whether the category applies. This is especially common in feature extraction, which is a topic in the data
# mining course. Variables with a boolean value are typically called dummy variables, and pandas has a built
# in function called get_dummies which will convert the values of a single column into multiple columns of
# zeros and ones indicating the presence of the dummy variable. I rarely use it, but when I do it's very
# handy.

import numpy as np

df=pd.read_csv("Week 3/census.csv")

df=df[df['SUMLEV']==50]

df=df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(np.average)

df.head()

# Now if we just want to make "bins" of each of these, we can use cut()
pd.cut(df,10)

# Here we see that states like alabama and alaska fall into the same category, while california and the
# disctrict of columbia fall in a very different category.

# Now, cutting is just one way to build categories from your data, and there are many other methods. For
# instance, cut gives you interval data, where the spacing between each category is equal sized. But sometimes
# you want to form categories based on frequency – you want the number of items in each bin to the be the
# same, instead of the spacing between bins. It really depends on what the shape of your data is, and what
# you’re planning to do with it.





# 3.5 Pivot Table
# ===================================================================================

A pivot table is a way of summarizing data in a DataFrame for a particular purpose. It makes heavy use of
the aggregation function. A pivot table is itself a DataFrame, where the rows represent one variable that
you're interested in, the columns another, and the cell's some aggregate value. A pivot table also tends to
includes marginal values as well, which are the sums for each column and row. This allows you to be able to
see the relationship between two variables at just a glance.

import pandas as pd
import numpy as np

df = pd.read_csv('Week 3/cwurData.csv')
df.head()

def create_category(ranking):
    if (ranking >= 1) & (ranking <= 100):
        return "First Tier Top Unversity"
    elif (ranking >= 101) & (ranking <= 200):
        return "Second Tier Top Unversity"
    elif (ranking >= 201) & (ranking <= 300):
        return "Third Tier Top Unversity"
    return "Other Top Unversity"

# Now we can apply this to a single column of data to create a new series
df['Rank_Level'] = df['world_rank'].apply(lambda x: create_category(x))
df.head()

# A pivot table allows us to pivot out one of these columns a new column headers and compare it against
# another column as row indices. Let's say we want to compare rank level versus country of the universities
# and we want to compare in terms of overall score

# To do this, we tell Pandas we want the values to be Score, and index to be the country and the columns to be
# the rank levels. Then we specify that the aggregation function, and here we'll use the NumPy mean to get the
# average rating for universities in that country

df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean]).head()

# We can see a  hierarchical dataframe where the index, or rows, are by country and the columns have two
# levels, the top level indicating that the mean value is being used and the second level being our ranks. In
# this example we only have one variable, the mean, that we are looking at, so we don't really need a
# heirarchical index.

# We notice that there are some NaN values, for example, the first row, Argentia. The NaN values indicate that
# Argentia has only observations in the "Other Top Unversities" category

# Now, pivot tables aren't limited to one function that you might want to apply. You can pass a named
# parameter, aggfunc, which is a list of the different functions to apply, and pandas will provide you with
# the result using hierarchical column names.  Let's try that same query, but pass in the max() function too

df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max]).head()

# So now we see we have both the mean and the max. As mentioned earlier, we can also summarize the values
# within a given top level column. For instance, if we want to see an overall average for the country for the
# mean and we want to see the max of the max, we can indicate that we want pandas to provide marginal values
df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max], 
               margins=True).head()

# A pivot table is just a multi-level dataframe, and we can access series or cells in the dataframe in a similar way 
# as we do so for a regular dataframe. 

# Let's create a new dataframe from our previous example
new_df=df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max], 
               margins=True)
# Now let's look at the index
print(new_df.index)
# And let's look at the columns
print(new_df.columns)

# We can see the columns are hierarchical. The top level column indices have two categories: mean and max, and
# the lower level column indices have four categories, which are the four rank levels. How would we query this
# if we want to get the average scores of First Tier Top Unversity levels in each country? We would just need
# to make two dataframe projections, the first for the mean, then the second for the top tier
new_df['mean']['First Tier Top Unversity'].head()

# We can see that the output is a series object which we can confirm by printing the type. Remember that when
# you project a single column of values out of a DataFrame you get a series.
type(new_df['mean']['First Tier Top Unversity'])

# What if we want to find the country that has the maximum average score on First Tier Top University level?
# We can use the idxmax() function.
new_df['mean']['First Tier Top Unversity'].idxmax()

# Now, the idxmax() function isn't special for pivot tables, it's a built in function to the Series object.
# We don't have time to go over all pandas functions and attributes, and I want to encourage you to explore
# the API to learn more deeply what is available to you.

# If you want to achieve a different shape of your pivot table, you can do so with the stack and unstack
# functions. Stacking is pivoting the lowermost column index to become the innermost row index. Unstacking is
# the inverse of stacking, pivoting the innermost row index to become the lowermost column index. An example
# will help make this clear

# Let's look at our pivot table first to refresh what it looks like
new_df.head()

# Now let's try stacking, this should move the lowermost column, so the tiers of the university rankings, to
# the inner most row
new_df=new_df.stack()
new_df.head()

# In the original pivot table, rank levels are the lowermost column, after stacking, rank levels become the
# innermost index, appearing to the right after country

# Now let's try unstacking
new_df.unstack().head()

# That seems to restore our dataframe to its original shape. What do you think would happen if we unstacked twice in a row?
new_df.unstack().unstack().head()

# We actually end up unstacking all the way to just a single column, so a series object is returned. This
# column is just a "value", the meaning of which is denoted by the heirarachical index of operation, rank, and
# country.

# pivot tables are incredibly useful when dealing with numeric data, especially if you're trying to 
# summarize the data in some form. You'll regularly be creating new pivot tables on slices of data, 
# whether you're exploring # the data yourself or preparing data for others to report on. 

# And of course, you can pass any function you want to the agg() function, including those you define yourself.





3.6 Date/Time Functionality
# ===================================================================================

In today's lecture, where we'll be looking at the time series and date functionally in pandas. Manipulating
dates and time is quite flexible in Pandas and thus allows us to conduct more analysis such as time series
analysis, which we will talk about soon. Actually, pandas was originally created by Wed McKinney to handle date and time data when he worked as a consultant for hedge funds.

import pandas as pd
import numpy as np



3.6.1 Timestamp
# ===================================================================================

# Pandas has four main time related classes. Timestamp, DatetimeIndex, Period, and PeriodIndex. First, let's
# look at Timestamp. It represents a single timestamp and associates values with points in time.

# For example, let's create a timestamp using a string 9/1/2019 10:05AM, and here we have our timestamp.
# Timestamp is interchangeable with Python's datetime in most cases.
pd.Timestamp('9/1/2019 10:05AM')

# We can also create a timestamp by passing multiple parameters such as year, month, date, hour,
# minute, separately
pd.Timestamp(2019, 12, 20, 0, 0)

# Timestamp also has some useful attributes, such as isoweekday(), which shows the weekday of the timestamp
# note that 1 represents Monday and 7 represents Sunday
pd.Timestamp(2019, 12, 20, 0, 0).isoweekday()

# You can find extract the specific year, month, day, hour, minute, second from a timestamp
pd.Timestamp(2019, 12, 20, 5, 2,23).second




3.6.2 Period
# ===================================================================================

# Suppose we weren't interested in a specific point in time and instead wanted a span of time. This is where
# the Period class comes into play. Period represents a single time span, such as a specific day or month.

# Here we are creating a period that is January 2016,
pd.Period('1/2016')

# You'll notice when we print that out that the granularity of the period is M for month, since that was the
# finest grained piece we provided. Here's an example of a period that is March 5th, 2016.
pd.Period('3/5/2016')

# Period objects represent the full timespan that you specify. Arithmetic on period is very easy and
# intuitive, for instance, if we want to find out 5 months after January 2016, we simply plus 5
pd.Period('1/2016') + 5

# From the result, you can see we get June 2016. If we want to find out two days before March 5th 2016, we
# simply subtract 2
pd.Period('3/5/2016') - 2

# The key here is that the period object encapsulates the granularity for arithmetic




3.6.3 DatetimeIndex and PeriodIndex
# ===================================================================================

# The index of a timestamp is DatetimeIndex. Let's look at a quick example. First, let's create our example
# series t1, we'll use the Timestamp of September 1st, 2nd and 3rd of 2016. When we look at the series, each
# Timestamp is the index and has a value associated with it, in this case, a, b and c.

t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), 
                             pd.Timestamp('2016-09-03')])
t1

# Looking at the type of our series index, we see that it's DatetimeIndex.
type(t1.index)

# Similarly, we can create a period-based index as well. 
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), 
                             pd.Period('2016-11')])
t2

# Looking at the type of the ts2.index, we can see that it's PeriodIndex. 
type(t2.index)





3.6.4 Convert to Datetime
# ===================================================================================

# Now, let's look into how to convert to Datetime. Suppose we have a list of dates as strings and we want to
# create a new dataframe

# I'm going to try a bunch of different date formats
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']

# And just some random data
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, 
                   columns=list('ab'))
ts3

# Using pandas to_datetime, pandas will try to convert these to Datetime and put them in a standard format.

ts3.index = pd.to_datetime(ts3.index)
ts3

# to_datetime also() has options to change the date parse order. For example, we 
# can pass in the argument dayfirst = True to parse the date in European date.

pd.to_datetime('4.7.12', dayfirst=True)




3.6.5 Timedelta
# ===================================================================================

# Timedeltas are differences in times. This is not the same as a a period, but conceptually similar. For
# instance, if we want to take the difference between September 3rd and  September 1st, we get a Timedelta of
# two days.
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')

# We can also do something like find what the date and time is for 12 days and three hours past September 2nd,
# at 8:10 AM.
pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')




3.6.6 Offset
# ===================================================================================

# Offset is similar to timedelta, but it follows specific calendar duration rules. Offset allows flexibility
# in terms of types of time intervals. Besides hour, day, week, month, etc it also has business day, end of
# month, semi month begin etc

# Let's create a timestamp, and see what day is that
pd.Timestamp('9/4/2016').weekday()

# Now we can now add the timestamp with a week ahead
pd.Timestamp('9/4/2016') + pd.offsets.Week()

# Now let's try to do the month end, then we would have the last day of Septemer
pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd()




3.6.7 Working with Dates in a Dataframe
# ===================================================================================

# Next, let's look at a few tricks for working with dates in a DataFrame. Suppose we want to look at nine
# measurements, taken bi-weekly, every Sunday, starting in October 2016. Using date_range, we can create this
# DatetimeIndex. In data_range, we have to either specify the start or end date. If it is not explicitly
# specified, by default, the date is considered the start date. Then we have to specify number of periods, and
# a frequency. Here, we set it to "2W-SUN", which means biweekly on Sunday

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
dates

# There are many other frequencies that you can specify. For example, you can do business day
pd.date_range('10-01-2016', periods=9, freq='B')

# Or you can do quarterly, with the quarter start in June
pd.date_range('04-01-2016', periods=12, freq='QS-JUN')

# Now, let's go back to our weekly on Sunday example and create a DataFrame using these dates, and some random
# data, and see what we can do with it.

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
df

# First, we can check what day of the week a specific date is. For example, here we can see that all the dates
# in our index are on a Sunday. Which matches the frequency that we set
df.index.weekday_name

# 不知为何上面error，可能是weekday_name deprecated

# We can also use diff() to find the difference between each date's value.
df.diff()

# Suppose we want to know what the mean count is for each month in our DataFrame. We can do this using
# resample. Converting from a higher frequency from a lower frequency is called downsampling (we'll talk about
# this in a moment)
df.resample('M').mean()

# Now let's talk about datetime indexing and slicing, which is a wonderful feature of the pandas DataFrame.
# For instance, we can use partial string indexing to find values from a particular year,
df['2017']

# Or we can do it from a particular month
df['2016-12']

# Or we can even slice on a range of dates For example, here we only want the values from December 2016
# onwards.
df['2016-12':]

df['2016']










*************************************************************************************
Week 4
*************************************************************************************


4.1 Basic Statistical Testing
# ===================================================================================

In this lecture we're going to review some of the basics of statistical testing in python. We're going to
talk about hypothesis testing, statistical significance, and using scipy to run student's t-tests.

# We use statistics in a lot of different ways in data science, and on this lecture, I want to refresh your
# knowledge of hypothesis testing, which is a core data analysis activity behind experimentation. The goal of
# hypothesis testing is to determine if, for instance, the two different conditions we have in an experiment 
# have resulted in different impacts

import numpy as np
import pandas as pd

from scipy import stats

# When we do hypothesis testing, we actually have two statements of interest: the first is our actual
# explanation, which we call the alternative hypothesis, and the second is that the explanation we have is not
# sufficient, and we call this the null hypothesis. Our actual testing method is to determine whether the null
# hypothesis is true or not. If we find that there is a difference between groups, then we can reject the null
# hypothesis and we accept our alternative.

# Let's see an example of this; we're going to use some grade data
df=pd.read_csv ('Week 4/grades.csv')
df.head()

# If we take a look at the data frame inside, we see we have six different assignments. Lets look at some
# summary statistics for this DataFrame
print("There are {} rows and {} columns".format(df.shape[0], df.shape[1]))

# For the purpose of this lecture, let's segment this population into two pieces. Let's say those who finish
# the first assignment by the end of December 2015, we'll call them early finishers, and those who finish it 
# sometime after that, we'll call them late finishers.

early_finishers=df[pd.to_datetime(df['assignment1_submission']) < '2016']
early_finishers.head()

# So, you have lots of skills now with pandas, how would you go about getting the late_finishers dataframe?
# Why don't you pause the video and give it a try.

# Here's my solution. First, the dataframe df and the early_finishers share index values, so I really just
# want everything in the df which is not in early_finishers
late_finishers=df[~df.index.isin(early_finishers.index)]
late_finishers.head()

# There are lots of other ways to do this. For instance, you could just copy and paste the first projection
# and change the sign from less than to greater than or equal to. This is ok, but if you decide you want to
# change the date down the road you have to remember to change it in two places. You could also do a join of
# the dataframe df with early_finishers - if you do a left join you only keep the items in the left dataframe,
# so this would have been a good answer. You also could have written a function that determines if someone is
# early or late, and then called .apply() on the dataframe and added a new column to the dataframe. This is a
# pretty reasonable answer as well.

# As you've seen, the pandas data frame object has a variety of statistical functions associated with it. If
# we call the mean function directly on the data frame, we see that each of the means for the assignments are
# calculated. Let's compare the means for our two populations

print(early_finishers['assignment1_grade'].mean())
print(late_finishers['assignment1_grade'].mean())

# Ok, these look pretty similar. But, are they the same? What do we mean by similar? This is where the
# students' t-test comes in. It allows us to form the alternative hypothesis ("These are different") as well
# as the null hypothesis ("These are the same") and then test that null hypothesis.

# When doing hypothesis testing, we have to choose a significance level as a threshold for how much of a
# chance we're willing to accept. This significance level is typically called alpha. #For this example, let's
# use a threshold of 0.05 for our alpha or 5%. Now this is a commonly used number but it's really quite
# arbitrary.

# The SciPy library contains a number of different statistical tests and forms a basis for hypothesis testing
# in Python and we're going to use the ttest_ind() function which does an independent t-test (meaning the
# populations are not related to one another). The result of ttest_index() are the t-statistic and a p-value.
# It's this latter value, the probability, which is most important to us, as it indicates the chance (between
# 0 and 1) of our null hypothesis being True.

# Let's bring in our ttest_ind function
from scipy.stats import ttest_ind

# Let's run this function with our two populations, looking at the assignment 1 grades
ttest_ind(early_finishers['assignment1_grade'], late_finishers['assignment1_grade'])

# So here we see that the probability is 0.18, and this is above our alpha value of 0.05. This means that we
# cannot reject the null hypothesis. The null hypothesis was that the two populations are the same, and we
# don't have enough certainty in our evidence (because it is greater than alpha) to come to a conclusion to
# the contrary. This doesn't mean that we have proven the populations are the same.

# Why don't we check the other assignment grades?
print(ttest_ind(early_finishers['assignment2_grade'], late_finishers['assignment2_grade']))
print(ttest_ind(early_finishers['assignment3_grade'], late_finishers['assignment3_grade']))
print(ttest_ind(early_finishers['assignment4_grade'], late_finishers['assignment4_grade']))
print(ttest_ind(early_finishers['assignment5_grade'], late_finishers['assignment5_grade']))
print(ttest_ind(early_finishers['assignment6_grade'], late_finishers['assignment6_grade']))

# Ok, so it looks like in this data we do not have enough evidence to suggest the populations differ with
# respect to grade. Let's take a look at those p-values for a moment though, because they are saying things
# that can inform experimental design down the road. For instance, one of the assignments, assignment 3, has a
# p-value around 0.1. This means that if we accepted a level of chance similarity of 11% this would have been
# considered statistically significant. As a research, this would suggest to me that there is something here
# worth considering following up on. For instance, if we had a small number of participants (we don't) or if
# there was something unique about this assignment as it relates to our experiment (whatever it was) then
# there may be followup experiments we could run.

# P-values have come under fire recently for being insuficient for telling us enough about the interactions
# which are happening, and two other techniques, confidence intervalues and bayesian analyses, are being used
# more regularly. One issue with p-values is that as you run more tests you are likely to get a value which
# is statistically significant just by chance.

# Lets see a simulation of this. First, lets create a data frame of 100 columns, each with 100 numbers
df1=pd.DataFrame([np.random.random(100) for x in range(100)])
df1.head()
# range()里代表行数

# Pause this and reflect -- do you understand the list comprehension and how I created this DataFrame? You
# don't have to use a list comprehension to do this, but you should be able to read this and figure out how it
# works as this is a commonly used approach on web forums.

# Ok, let's create a second dataframe
df2=pd.DataFrame([np.random.random(100) for x in range(100)])

# Are these two DataFrames the same? Maybe a better question is, for a given row inside of df1, is it the same
# as the row inside df2?

# Let's take a look. Let's say our critical value is 0.1, or and alpha of 10%. And we're going to compare each
# column in df1 to the same numbered column in df2. And we'll report when the p-value isn't less than 10%,
# which means that we have sufficient evidence to say that the columns are different.

# Let's write this in a function called test_columns
def test_columns(alpha=0.1):
    # I want to keep track of how many differ
    num_diff=0
    # And now we can just iterate over the columns
    for col in df1.columns:
        # we can run out ttest_ind between the two dataframes
        teststat,pval=ttest_ind(df1[col],df2[col])
        # and we check the pvalue versus the alpha
        if pval<=alpha:
            # And now we'll just print out if they are different and increment the num_diff
            print("Col {} is statistically significantly different at alpha={}, pval={}".format(col,alpha,pval))
            num_diff=num_diff+1
    # and let's print out some summary stats
    print("Total number different was {}, which is {}%".format(num_diff,float(num_diff)/len(df1.columns)*100))

# And now lets actually run this
test_columns()

# Interesting, so we see that there are a bunch of columns that are different! In fact, that number looks a
# lot like the alpha value we chose. So what's going on - shouldn't all of the columns be the same? Remember
# that all the ttest does is check if two sets are similar given some level of confidence, in our case, 10%.
# The more random comparisons you do, the more will just happen to be the same by chance. In this example, we
# checked 100 columns, so we would expect there to be roughly 10 of them if our alpha was 0.1.

# We can test some other alpha values as well
test_columns(0.05)

# So, keep this in mind when you are doing statistical tests like the t-test which has a p-value. Understand
# that this p-value isn't magic, that it's a threshold for you when reporting results and trying to answer
# your hypothesis. What's a reasonable threshold? Depends on your question, and you need to engage domain
# experts to better understand what they would consider significant.

# Just for fun, lets recreate that second dataframe using a non-normal distribution, I'll arbitrarily chose
# chi squared
df2=pd.DataFrame([np.random.chisquare(df=1,size=100) for x in range(100)])
test_columns()

# Now we see that all or most columns test to be statistically significant at the 10% level.



4.2 Other Forms of Structured Data
*************************************************************************************

# network diagram

# library networkX

# tree structure
























































































































































































































