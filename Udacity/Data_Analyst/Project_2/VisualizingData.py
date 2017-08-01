import unicodecsv
from datetime import datetime as dt
from collections import defaultdict
import pandas

enrollments_filename = '/Users/tonynguyen/Desktop/Codes/Udacity/Data Analyst/enrollments.csv'
engagement_filename = '/Users/tonynguyen/Desktop/Codes/Udacity/Data Analyst/daily_engagement.csv'
submissions_filename = '/Users/tonynguyen/Desktop/Codes/Udacity/Data Analyst/project_submissions.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

def open_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = open_csv(enrollments_filename)
engagements = open_csv(engagement_filename)
submissions = open_csv(submissions_filename)


################################################################################
#                              Cleaning Codes                                  #
################################################################################

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')


# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

for engagement in engagements:
    engagement['utc_date'] = parse_date(engagement['utc_date'])

################################################################################
#                               Exercise one                                   #
################################################################################

#creating a set to hold the values of the needed information
unique_enrollment = set()
unique_engagement = set()
unique_submission = set()

#code to find the "account_key" and placing them in the set
for unique in enrollments:
    account = unique['account_key']
    unique_enrollment.add(account)

for unique in engagements:
    account = unique['acct']
    unique_engagement.add(account)

for unique in submissions:
    account = unique['account_key']
    unique_submission.add(account)

# print(len(unique_enrollment))
# print(len(unique_engagement))
# print(len(unique_submission))

### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows = 1640             # Replace this with your code
enrollment_num_unique_students = 1302  # Replace this with your code

engagement_num_rows = 136240             # Replace this with your code
engagement_num_unique_students = 1237  # Replace this with your code

submission_num_rows = 3642             # Replace this with your code
submission_num_unique_students = 743  # Replace this with your code

#found the number of rows using print(len(filename))

################################################################################
#                               Exercise Two                                   #
################################################################################

# The engagements csv has 'acct' instead of "account_key."  Code below fixes it

for update_header in engagements:
    update_header["account_key"] = update_header["acct"]
    del update_header["acct"]

#print(engagements[0])

################################################################################
#                               Exercise 2.5                                   #
################################################################################

# Getting unique sets by calling a function

def unique_students(docu):
    unique_set = set()
    for unique in docu:
        account = unique['account_key']
        unique_set.add(account)
    #print(len(unique_set))

#unique_students(engagements)

################################################################################
#                             Exercise Three                                   #
################################################################################

# unique_engagement and unique_enrollment should be the same. Print some values
# where there is a difference

difference_engangement_enrollments = list(unique_enrollment - unique_engagement)

#print (difference_engangement_enrollments)

# if engagements['account_key] in enrollment['account_key']

for test in enrollments:                    #creates an instances for every row
    difference = test['account_key']        #difference = the value of 'account_key'
    if difference not in unique_engagement: #if the difference is not in unique_engagement
        break
        print test                          #print all the difference

################################################################################
#                             Exercise Four                                    #
################################################################################

# finding all the instances of where cancel_date and join_date is not the same
# AND if they are not in unique_engagement

for is_in in enrollments:   #creates an instances for every row in enrollments
    difference = is_in['account_key']   # copies all the account_keys and puts it in difference
    counter = 0
    if difference not in unique_engagement: #if (account_key) is not in unique_engagement
        if is_in['cancel_date'] != is_in['join_date']: # if join_date != cancel_date
            break
            print is_in #print out the remaining instances

################################################################################
#                             Exercise Five                                    #
################################################################################
# removing test accounts from enrollments

# finding the test users
udacity_test_users = set() #creates an empty set to store account_key of test users
for test_users in enrollments: # creates an instances for each row
    if test_users["is_udacity"] == True: # searching for test users
        udacity_test_users.add(test_users['account_key']) # adding test users to udacity_test_users set

#removing test users

def removing(data): # creating a function
    non_udacity = [] # makes an empty list for nonm_test_users
    for student in data: # making an instance for each data
        if student['account_key'] not in udacity_test_users: # if account_key is not in test user's list
            non_udacity.append(student) # take non test users and put them in non_udacity
    return non_udacity # return all non test users

non_test_enrollments = removing(enrollments)
non_test_engagments = removing(engagements)
non_test_submissions = removing(submissions)

#print(len(non_test_enrollments))
#print(len(non_test_engagments))
#print(len(non_test_submissions))

################################################################################
#                             Exercise Six                                     #
################################################################################

# creating a dictionary for students who:
# have not cancled (ie: days_to_cancel == 0 (None))
# or students with days_to_cancel > 7
# find how many unique_paid_students there are

paid_students = {}
unique_paid_students = set()

# creating a dictionary for paid students
for students in non_test_enrollments: # creates a loop for each instances
    if students['days_to_cancel'] == None or students['days_to_cancel'] > 7: # if days_to_cancel == none or > 7
        account_key = students["account_key"] # copies students' account key
        enrollment_date = students["join_date"] # copies students' join date
        paid_students[account_key] = enrollment_date # creates a key (account_key) and sets join date as the value

        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date
print(len(paid_students))


################################################################################
#                             Exercise Seven                                   #
################################################################################
# Create a list of rows from the engagement table including only rows where
# the student is one of the paid students you just found, and the date is within
# one week of the student's join date.

# this code test if the join_date and engagement_date is within a week (not made by me)
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7

paid_engagement_in_first_week = []


# removing free trial

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paying_enrollments = remove_free_trial_cancels(non_test_enrollments)
paying_engagements = remove_free_trial_cancels(non_test_engagments)
paying_submissions = remove_free_trial_cancels(non_test_submissions)

paid_engagement_in_first_week = []
for engagement_record in paying_engagements:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print(len(paid_engagement_in_first_week))
# engagement date  = utc_date - from engagement
# join date = join_date - from enrollments


################################################################################
#                             Exercise 7.5                                     #
################################################################################

#figering out the avg minutes

engagement_by_account = defaultdict(list)
