from __future__ import division
import numpy as np
import pandas as pd
import seaborn as sns


# In the movie, Titanic, crew members tried to allocate lifeboats to women and children,
# prioritizing higher class first. I want to know if the data truly reflects that.
# Of the surviving passengers, what is the survivability between Class,
# Sex, and age?

##########################################################################
# Data Wrangling Phase
##########################################################################

# opening up the titanic_data as a Pandas DataFrame
filename = '/Users/tonynguyen/Desktop/Codes/Udacity/Data Analyst/Project 2/titanic_data.csv'
titanic_data = pd.read_csv(filename)

# Creating a new DataFrame using the columns that are needed to answer my
# question.
titanic_my_data = titanic_data[
    ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age']]
my_data = titanic_my_data


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

# Through out the analsis, I mainly used my_data dataframe. However there are times
# where I needed to only look at surviors or deceased.
survivors = my_data.query('Survived!= 0')  # surviving passengers
deceased = my_data.query('Survived == 0')  # deceased passengers

my_data_dropna = my_data.dropna(subset=["Age"])
survivors_dropna = survivors.dropna(subset=["Age"])
deceased_dropna = deceased.dropna(subset=["Age"])


##########################################################################
# Exploration Phase
##########################################################################

def by_class_describe(df):
    """
    Takes a data frame and returns the .describe() method.
    """
    test = df.groupby('Pclass')
    print test.describe()

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
    second_class_ratio = second_males / \
        total_passengers, second_females / total_passengers
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
    DF used can be: survivors, deceased, or my data
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

##########################################################################
# Plots using Seaborn
##########################################################################

# Below is a box plot showing the difference between passengers who survived
# and died, by class and violin plot depicting the age of those who died.
# Please


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

dead_plot = sns.violinplot(
    x='Pclass', y='Age', hue="Sex", data=survivors_dropna, palette="Set2")
dead_plot.set_title("Deceased Passengers")

survivors_plot = sns.violinplot(
    x='Pclass', y='Age', hue="Sex", data=survivors_dropna)
survivors_plot.set_title('Surviving Passengers')


# all_data_box_plot = sns.countplot(x="Pclass", hue='Sex', data=my_data, facecolor=(0, 0, 0, 0),
#                        linewidth=1,
#                        edgecolor=sns.color_palette("dark", 1))

#survivors_box_plot = sns.countplot(x="Pclass",hue='Sex', data=survivors)

#sns.plt.show()
##########################################################################
# My conclusion
##########################################################################

print titanic_data
