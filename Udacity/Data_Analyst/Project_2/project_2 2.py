from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In the movie, Titanic, crew members tried to allocate lifeboats to women and children,
# prioritizing higher class first. I want to know if the data truly reflects that.
# Of the surviving passengers, what is the survivability between Class, Sex, and age?
# How does it differ from those that did not survive?


##########################################################################
# Data Wrangling Phase
##########################################################################

# Please replace filename with the path of your titanic data
# opening up the titanic_data as a Pandas DataFrame
filename = '/Users/tonynguyen/Desktop/Codes/Udacity/Data Analyst/Project 2/titanic_data.csv'
titanic_data = pd.read_csv(filename)

# Creating a new DataFrame using the columns that are needed to answer my
# question.
titanic_my_data = titanic_data[
    ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age']]
my_data = titanic_my_data.set_index('PassengerId')


def sex_true_false(df):
    """
    I originally wanted to use the .count() method but ran into issues when using it
    with a Pandas DataFrame. By setting the Sex column to True/False, it was easier
    for me to distinguish better between male/female.
    """

    df.loc[df.Sex == 'female', 'Sex'] = True
    df.loc[df.Sex == 'male', 'Sex'] = False

sex_true_false(my_data)


# Creatring new dataframes to better organize the data
survivors = my_data.query('Survived!= 0')  # surviving passengers
deceased = my_data.query('Survived == 0')  # deceased passengers

##########################################################################
# Exploration Phase
##########################################################################


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

# Below is a box plot and scatter plot depicting the age of those who died. Please
# Note: The ages of some passengers have no value, the graphs displayed only depict
# those that do. This should not be too much of a problem because the data that is
# already present shows a correlation between survivability and age. (see
# blox plots)


def change_sex_values(df):
    """
    Earlier I changed the values of sex to make it easier for me to analyze
    the data frame better. However it made the plots more difficult to read, so
    I am changing it back to Female/Male
    """

    df.loc[df.Sex == True, 'Sex'] = 'Female'
    df.loc[df.Sex == False, 'Sex'] = 'Male'

change_sex_values(survivors)
change_sex_values(deceased)


# I chose to plot with seaborn because it reflected the data between class, age,
# and sex much better than metaplotlib.

# dead_plot = sns.boxplot(x=deceased['Pclass'], y=deceased[
#                        'Age'], hue=deceased["Sex"], palette="Set2")
# dead_plot.set_title("Deceased Passengers")

# survivors_plot = sns.boxplot(x='Pclass', y=
#                             'Age', hue="Sex", data=survivors)
# survivors_plot.set_title('Surviving Passengers')

plt.show()


##########################################################################
# My conclusion
##########################################################################
"""

First I took a look some general numbers. The totals of all passengers,
surviving passengers, and deceased passengers. Using the functions
total_passengers and total_by_class. Already we can see  preliminary results.
For example a there were more survivors in first class than third class.

Total Passengers dead and alive
1st Class:
    216, 122, 94
2st Class:
    184, 108, 76
3rd Class:
    491, 347, 144

total passengers survived
#total passengers by classes (total, male, female)
first class:
    (136, 45, 91)
second class:
    (87, 17, 70)
third class:
    (119, 47, 72)

Total Passengers deceased
1st Class:
    80, 77, 3
2st Class:
    97, 91, 6
3rd Class:
    372, 300, 72

Next, I used the survivability_as_whole function to find the percentage of
passenger(by class) survived when compared as a whole. 37.26 % of all
passengers survived the sinking of the Titanic. 15.26 % were from first class
vs 13.35 % from third class. From here one can assert that first class were
prioritized first when evacuating the Titanic.

It is interesting to note that 2nd passengers have the lowest survival of 9.76
% . Typically after 1st class, priority should go to 2nd passengers. I thought
there might have been some discrepancy when comparing the surviving passenger
and the whole.

# survivability of classes as a whole
# Of all Class 37.26%
# 1st Class 15.26%
# 2nd Class 9.76%
# 3rd Class 13.35%

Instead, I decided to compare the surviving passenger and the total of their
respective class. (ie: first class survivors vs total first class passengers).
By using survivability_within_class, we can see a more clear survivability rate.

# survivability within classes
# 1st class survivability = 62.96%
# 2nd class survivability = 47.28%
# 3rd class survivability = 24.23%


After comparing cTotal and wTotal, it was time to see if gender had a factor
in survivability. I separated the data into groups, class, and class gender.
I then compared that data to the wTotal passengers. This to had the expected
results. Even though there were more men(as a whole and by class) women were
prioritized when allocating for the life boats.

# Survivability of Sex (class vs wTotal)
# Male/Female Survival Ratio within Class
# Between all classes M:31.87% F:68.12
#(0.050, 0.102)
#(0.019, 0.078)
#(0.052, 0.080)

I then compared the survivor data vs the cTotal. This also had shown that
women had a higher survival rate, even within their own class.

# Survivability of Sex (class vs cTotal)
# 1st Class M:33.08% F:66.91%
# 2nd Class M:19.54% F:80.45%
# 3rd Class M:39.49% F:60.50%

At this point I feel it safe to conclude were prioritize first. This was
reflected as a wTotal and cTotal.

Now the hard part. Did age also play a role? Our data did not have the age
for all the passengers so the results are not the most accurate.
I compared the average of all the survivors VS all the deceased. On average
 the survivors were younger.

# Age means of survivors and deceased
# Survivor Age Mean: 28.34
# Deceased Age Mean: 30.62

Then I separated the data by sex and compared the average age. Surviving women
were older then the surviving males, but not by much. Also, deceased females
were younger than the surviving females on average.  This discrepancy was
occurred at the class level as well.

It could be that after a certain age(after saving the children), crew members
tried to save any women regardless of their age. So there is possibly no
(or a low) correlation between female survivability and age.

The men on the other had is a different story. All the data consistently showed
that the average age of the survivability males is younger than the deceased
male, across all boards. There is a correlation between age and survivability
when comparing males.

# Age mean of Sex
# Deceased Male: 31.61
# Deceased Female: 25.04
# Surviving Male: 27.27
# Surviving Female: 28.84


# Average age of those survived
# 1st Male: 36.24
# 1st Female: 34.939
# 2st Male: 16.02
# 2st Female: 28.08
# 3rd Male: 22.27
# 3rd Female: 22.27

# Average age of those deceased
# 1st Male: 44.58
# 1st Female: 25.66
# 2nd Male: 33.36
# 2st Female: 36.0
# 3rd Male: 27.25
# 3rd Female: 27.25

I chose to graph the surviving passengers and the deceased passengers. So we can
visually see the difference. I chose to use seaborn's box plot because it was
better able to reflect class and gender. If you compare the two graphs, you can
see that crew members most likely did prioritize women and youths first, in
order of class.
"""
