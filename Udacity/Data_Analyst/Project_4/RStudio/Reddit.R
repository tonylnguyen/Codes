reddit_data <- read.csv('reddit.csv')

#this groups the employment.status data, and returns how many values are in
#the respective categories
table(reddit_data$employment.status)

#we can do the same thing with table in the summary fucntion as well
summary(reddit_data)

str(reddit_data)

#dealing with Factor data
levels(reddit_data$age.range) # prints out the 7 levels (options) of ages

library(ggplot2) #this imports the ggplot to package (just like in python)
age <- qplot(data = reddit_data,  x = age.range)
qplot(data = reddit_data, x = income.range)

#notice that the plot is not arranged in any particular order , below is how you fix it


is.factor(reddit_data$age.range)
ordered_age <- ordered(reddit_data$age.range, levels = c("Under 18","18-24","25-34","35-44","45-54","55-64","65 or Above"))

qplot(data = reddit_data,  x = ordered_age)


levels(reddit_data$income.range)
# OR
reddit_data$income.range <- ordered(reddit_data$income.range, levels = c("Under $20,000","$20,000 - $29,999","$30,000 - $39,999",
                                             "$40,000 - $49,999","$50,000 - $69,999","$70,000 - $99,999",
                                             "$100,000 - $149,999","$150,000 or more"))
