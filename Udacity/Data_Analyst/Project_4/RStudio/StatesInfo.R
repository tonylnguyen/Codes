getwd() # tells us where the current directory is

setwd(#directory here) # sets a new directory

# this loads the stateData.csv into the variable stateInfo
statesInfo <- read.csv('stateData.csv'),

# examples of ways to query stateInfo with a certain collumn
# subset(file name, collumn + value of collumn)
subset(statesInfo, state.region == 1),
# OR
# file name[row, collumn]
statesInfo[statesInfo$state.region == 1, ],

region_one <- statesInfo[statesInfo$state.region == 1, ],

# states with life expectancy > 72.5

statesInfo[statesInfo$life.exp > 72.5, ]