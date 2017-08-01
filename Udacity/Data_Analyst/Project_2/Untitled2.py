
# coding: utf-8

# In[1]:

from __future__ import division
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:

# Introduction

# In the movie, Titanic, crew members tried to allocate lifeboats to women and children,
# prioritizing higher class first. I want to know if the data truly reflects that.
# Of the surviving passengers, what is the survivability between Class, Sex, and age?


# In[3]:

# Data Wrangling Phase

# opening up the titanic_data as a Pandas DataFrame
filename = '/Users/tonynguyen/Desktop/Codes/Udacity/Data Analyst/Project 2/titanic_data.csv'
titanic_data = pd.read_csv(filename)

# Creating a new DataFrame using the columns that are needed to answer my
# question.
titanic_my_data = titanic_data[
    ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age']]
my_data = my_data = titanic_my_data.set_index('PassengerId')


# I converted the Sex column to true or false so I can easily find the total of
# male or female passengers. To do this I created a function that converts Male/female
# into booleans. Later on, I will use the sum of sex to dertermine how many males/females
# there are in my query.

def sex_true_false(df):
    """
    Convers Sex: Male/Female into booleans.
    """

    df.loc[df.Sex == 'female', 'Sex'] = True
    df.loc[df.Sex == 'male', 'Sex'] = False

sex_true_false(my_data)

# Through out the analysis, I mainly used my_data dataframe. However there are times
# where I needed to only look at surviors or deceased.
survivors = my_data.query('Survived!= 0')  # surviving passengers
deceased = my_data.query('Survived == 0')  # deceased passengers

# These codes drop any Nan data in the "Age". This is only used when comparing the
# passengers' age. 
my_data_dropna = my_data.dropna(subset = ["Age"]) 
survivors_dropna = survivors.dropna(subset = ["Age"]) 
deceased_dropna = deceased.dropna(subset = ["Age"]) 

# This code gives and "error" suggesting to use write a code.
# The code itself still works.


# In[4]:

# Exploration Phase

def by_class_describe(df):
    """
    Takes a data frame and returns the .describe() method.
    """
    test = df.groupby('Pclass')
    return test.describe()

# I could have continued to group the my_data by class and used .describe()
# to gather the data I needed, but I found it to be clutter with many other
# data and it was not visually simulating. To make it easier on the user. I
# created other fucntions to get the specific data, without being overwhelmed by
# unneeded data.

def total_passengers(df):
    """
    Input any data frame and returns the total passengers. Please use the
    data frame 'my_data' for the parameters.
    """
    survivors = my_data.query('Survived!= 0')
    deceased = my_data.query('Survived == 0')

    print ('Total/Survivors/Deceased: ' + str(len(df)),
           str(len(survivors)), str(len(deceased)))


def total_by_class(df):
    """
    Prints out the total by class in the format of (total, male, female).
    The data frames 'my_data', 'survivors', 'deceased'
    can be used to generate the desired results.
    """
    df_First_class = df.query('Pclass == 1')
    df_second_class = df.query('Pclass == 2')
    df_third_class = df.query('Pclass == 3')

    first_males = df_First_class.query('Sex == False')
    first_females = df_First_class.query('Sex == True')

    second_males = df_second_class.query('Sex == False')
    second_females = df_second_class.query('Sex == True')

    third_males = df_third_class.query('Sex == False')
    third_females = df_third_class.query('Sex == True')

    print("Total Passengers (total, male, female)\n" + "1st Class: " +
          str(len(df_First_class)) + ', ' + str(len(first_males)) + ', ' + str(len(first_females)) + "\n2st Class: " +
          str(len(df_second_class)) + ', ' + str(len(second_males)) + ', ' + str(len(second_females)) + "\n3rd Class: " +
          str(len(df_third_class)) + ', ' + str(len(third_males)) + ', ' + str(len(third_females)))


def survivability_as_whole(df):
    """
    Compares survivability of the entire passengers. Separates the data frame
    into class. Then divides the total surviving passengers of each class
    to the total passengers. To get the ratio of surviving passengers.
    Please use my_data as the parameters.
    """

    total = 891.0  # total passengers of our data between all classes
    survivors = my_data.query('Survived!= 0')

    first_class_survivors = len(survivors.query('Pclass == 1'))
    second_class_survivors = len(survivors.query('Pclass == 2'))
    third_class_survivors = len(survivors.query('Pclass == 3'))

    all_class = len(survivors) / len(my_data)
    first_class = first_class_survivors / total
    second_class = second_class_survivors / total
    third_class = third_class_survivors / total

    print('As a whole: ' + str(all_class) + '\nFirst Class: ' + str(first_class) +
          '\nSecond Class: ' + str(second_class) + '\nThird Class: ' + str(third_class))


def survivability_within_class(df1):
    """
    Compares the survivability at the class level. Takes the total passengers
    of a class, then compares it to surviving passengers of that class.
    Please use my_data as the parameters.
    """

    my_data = df1
    survivors = my_data.query('Survived!= 0')

    first_class = len(my_data.query('Pclass == 1'))
    second_class = len(my_data.query('Pclass == 2'))
    third_class = len(my_data.query('Pclass == 3'))

    first_class_survivors = len(survivors.query('Pclass == 1'))
    second_class_survivors = len(survivors.query('Pclass == 2'))
    third_class_survivors = len(survivors.query('Pclass == 3'))

    first_class = first_class_survivors / first_class
    second_class = second_class_survivors / second_class
    third_class = third_class_survivors / third_class

    print('First Class: ' + str(first_class) + '\nSecond Class: ' +
          str(second_class) + '\nThird Class: ' + str(third_class))


def class_sex_ratio_whole(df):
    """
    compares the survival rate of class (by sex) vs all passengers.
    Please use my_data as the perameters.
    """

    my_data = df
    total_passengers = len(my_data)
    survivors = my_data.query('Survived!= 0')
    first_class_survivors = (survivors.query('Pclass == 1'))
    second_class_survivors = (survivors.query('Pclass == 2'))
    third_class_survivors = (survivors.query('Pclass == 3'))

    first_total = len(first_class_survivors)
    first_females = first_class_survivors['Sex'].sum()
    first_males = first_total - first_females

    second_total = len(second_class_survivors)
    second_females = second_class_survivors['Sex'].sum()
    second_males = second_total - second_females

    third_total = len(third_class_survivors)
    third_females = third_class_survivors['Sex'].sum()
    third_males = third_total - third_females

    first_class_ratio = first_males / total_passengers, first_females / total_passengers
    second_class_ratio = second_males /         total_passengers, second_females / total_passengers
    third_class_ratio = third_males / total_passengers, third_females / total_passengers

    print('Male/Female Survival Ratio within Class')
    print(first_class_ratio)
    print(second_class_ratio)
    print(third_class_ratio)


def class_sex_ratio_by_class(df):
    """
    compares the survival rate of class (by sex) vs total passengers of that class.
    Please use my_data as the parameters.
    """

    my_data = df
    survivors = my_data.query('Survived!= 0')
    first_class_survivors = (survivors.query('Pclass == 1'))
    second_class_survivors = (survivors.query('Pclass == 2'))
    third_class_survivors = (survivors.query('Pclass == 3'))

    first_total = len(first_class_survivors)
    first_females = first_class_survivors['Sex'].sum()
    first_males = first_total - first_females

    second_total = len(second_class_survivors)
    second_females = second_class_survivors['Sex'].sum()
    second_males = second_total - second_females

    third_total = len(third_class_survivors)
    third_females = third_class_survivors['Sex'].sum()
    third_males = third_total - third_females

    first_class_ratio = first_males / first_total, first_females / first_total
    second_class_ratio = second_males / second_total, second_females / second_total
    third_class_ratio = third_males / third_total, third_females / third_total

    print('Male/Female Survival Ratio within Class')
    print(first_class_ratio)
    print(second_class_ratio)
    print(third_class_ratio)


def mean_of_age_whole(df):
    """
    Used to find the age mean of those who survived or died
    DF used can be: survivors_dropna, deceased_dropna, or my_data_dropna
    """
    return df['Age'].mean()


def mean_age(df):
    """
    Creates new a new data frame by sex, and returns the mean age from each sex
    """
    df_First_class = df.query('Pclass == 1')
    df_second_class = df.query('Pclass == 2')
    df_third_class = df.query('Pclass == 3')

    first_males = df_First_class.query('Sex == False')
    first_females = df_First_class.query('Sex == True')

    second_males = df_second_class.query('Sex == False')
    second_females = df_second_class.query('Sex == True')

    third_males = df_third_class.query('Sex == False')
    third_females = df_third_class.query('Sex == True')

    print("Passengers Average Age \n" + "1st Male: " +
          str(first_males['Age'].mean()) + '\n' + "1st Female: " + str(first_females['Age'].mean()) + "\n2st Male: " +
          str(second_males['Age'].mean()) + '\n' + "2st Female: " + str(second_females['Age'].mean()) + "\n3rd Male: " +
          str(third_males['Age'].mean()) + '\n' + "3rd Female: " + str(third_males['Age'].mean()) + '\n')
    


# In[5]:

# Plots using Seaborn

# Below is a box plot showing the difference between passengers who survived 
# and died, by class and violin plot depicting the age of those who died. 
# I chose to plot with seaborn because its categories reflected the data between class, age,
# and sex much better than metaplotlib.

def change_sex_values(df):
    """
    Earlier I changed the values of sex to make it easier for me to analyze
    the data frame better. However it made the plots more difficult to read, so
    I am changing it back to Female/Male
    """

    df.loc[df.Sex == True, 'Sex'] = 'Female'
    df.loc[df.Sex == False, 'Sex'] = 'Male'

change_sex_values(my_data)
change_sex_values(survivors)
change_sex_values(deceased)

# This code gives and "error" suggesting to use write a code.
# The code itself still works.


# In[6]:

dead_plot = sns.violinplot(
    x='Pclass', y='Age', hue="Sex", data=survivors_dropna, palette="Set2")
dead_plot.set_title("Deceased Passengers")

sns.plt.show()

# Using a violin graph, we can see the density of age between males/females and age.


# In[7]:

survivors_plot = sns.violinplot(
    x='Pclass', y='Age', hue="Sex", data=survivors_dropna)
survivors_plot.set_title('Surviving Passengers')

sns.plt.show()

# Here we can see that the surviving passengers have more density in age, especially with the female passengers. 
# By looking at these two graphs, it is difficult to say if age really did play a role with survivablity.


# In[8]:

all_data_box_plot = sns.countplot(x="Pclass", hue='Sex', data=my_data, facecolor=(0, 0, 0, 0),
                        linewidth=1,
                        edgecolor=sns.color_palette("dark", 1))

survivors_box_plot = sns.countplot(x="Pclass",hue='Sex', data=survivors)

sns.plt.show()

# The barplot shows the passengers to survived (solid colored) vs the total amount of passengers by class and sex. 
# We can see that a class does play a role when it comes to survivablilty. 1st class has the highest rate while third
# class has the lowest. We can also see that gender also plays a role with females having a higher chance of survival
# vs males.


# In[ ]:

# Limitation 

"""
The data provided is enough to find some correlations and make educated assumptions, but there are a few limitation 
when it came to the data. 

Probabily the biggest limitation is the data that is provided. How was the data gathered? How accurate is it? etc.
Knowing these information can factor in on the methods we used to answer our questions.

Missing data would be the next issue at hand. The missing data that would have been useful in answering my question 
is age. There are approximately 177 passengers where we do not have the age in our data. Due to these missing values,
it makes finding the correlation between survivability and age much harder and unreliable. Although I did not use it
to answer my question, other missing data are cabin room or any other passengers that wouldn't be in the passenger
logs (ie: stow aways).

Not knowing the preceedure of how crew members evacuated passengers affects limits are data as well. As the Titanic 
sank, preceedures could have change, or crew members could have acted inconsistantly from one another. Since it would
be near impossible to gather this data, any conclusion that I come to will always be subjective.

"""


# In[ ]:

# Conclusion

"""First I took a look some general numbers. The totals of all passengers, surviving passengers, and deceased passengers. Using the functions total_passengers and total_by_class. Already we can see  preliminary results. For example a there were more survivors in first class than third class.

Total Passengers dead and alive
1st Class: 216, 122, 94
2st Class: 184, 108, 76
3rd Class: 491, 347, 144

survived
total passengers by classes (total, male, female)
first class: (136, 45, 91)
second class: (87, 17, 70)
third class: (119, 47, 72)

Total Passengers Deceased
1st Class: 80, 77, 3
2st Class: 97, 91, 6
3rd Class: 372, 300, 72

Next, I used the survivability_as_whole function to find the percentage of passenger (by class) survived when compared as a whole. 37.26% of all passengers survived the sinking of the Titanic. 15.26% were from first class vs 13.35% from third class. From here one can assert that first class where prioritized first when evacuating the Titanic.

It is interesting to note that 2nd passengers has a lowest survival of 9.76%. Typically after 1st class, priority should go to 2nd passengers. I thought there might have been some discrepancy when comparing the surviving passenger and the whole.

survivability of classes as a whole
Of all Class 37.26%
1st Class 15.26%
2nd Class 9.76%
3rd Class 13.35%

Instead, I decided to compare the surviving passenger and the total of their respective class. (ie: first class survivors vs total first class passengers). By using survivability_within_class, we can see a more clear survivability rate.  At this point I would put forth that class does play a role with the survivability rate.

# survivability within classes
# 1st class survivability = 62.96%
# 2nd class survivability = 47.28%
# 3rd class survivability = 24.23%


After comparing the different totals, it was time too see if gender had a factor in survivability. I separated the data into groups, class, and class gender. I then compared that data to the whole total of passengers. This to had the expected results. Even though there were more men (as a whole and by class), women where prioritized when allocating for the life boats. 

Survivability of Sex (class vs wTotal)
Male/Female Survival Ratio within Class
Between all classes M:31.87% F:68.12
(0.050, 0.102)
(0.019, 0.078)
(0.052, 0.080)

I then compared the survivor data vs the class total. This also had showed that women had a higher survival rate, even within their own class.

Survivability of Sex (class vs cTotal)
1st Class M:33.08% F:66.91%
2nd Class M:19.54% F:80.45%
3rd Class M:39.49% F:60.50%

At this point I feel it safe to conclude were women prioritize first. This was reflected as a whole total  and the class total.

Now the hard part. Did age also play a role? I compared the average of all the survivors VS all the deceased, with the mean_of_age_whole function. On average the survivors were younger, but by only two years.

Age mean of survivors and deceased
All Age: 29.69
Survivor Age Mean: 28.34
Deceased Age Mean: 30.62

Then I separated the data by sex and compared the average age,  using the mean_age function. On average, surviving women were older then the surviving males, but not by much. Also, deceased females were younger than the surviving females on average.  This discrepancy was occurred within the class level as well. 

Passengers Average Age of Survivors
1st Male: 36.248
1st Female: 34.9390243902
2st Male: 16.022
2st Female: 28.0808823529
3rd Male: 22.2742105263
3rd Female: 22.2742105263

Passengers Average Age of the Deceased
1st Male: 44.5819672131
1st Female: 25.6666666667
2st Male: 33.369047619
2st Female: 36.0
3rd Male: 27.2558139535
3rd Female: 27.2558139535


It could be saidthat after a certain age (after saving the children), crew members tried to save any women regardless of their age. So there is possibly no (or a low) correlation between female survivability and age.

The men on the other had is a different story. Once again using mean_age and mean_of_age_whole function but with the survivors and deceased data frames. All the data consistently showed that the average age of the surviving males are younger than the deceased male, across all boards. There is a correlation between age and survivability when comparing males.

Age mean of Sex (survived and deceased)
Deceased Male: 31.61
Deceased Female: 25.04
Surviving Male: 27.27
Surviving Female: 28.84

"""


# In[ ]:




# In[ ]:



