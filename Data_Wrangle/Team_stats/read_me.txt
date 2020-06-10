These file are used to measure the quality of the team and of the actors.

Problem: Team/Actors data is pulled from SQL queries and copied/pasted into a master Excel file. The Excel file would contain
         thounsands of rows of data with formulas. The amount of data/formlas causes greater response lag from the file.
         As a result, the Excel file will become unusable due to extreme lag.
         

         
 Solution: Team_Stats.py will automatically calculate the necessary metrics and paste the data into the master excel file. 
           Since python will be doing all the calculations, the need for excel formulas will be reduced. This will make the
           Excel file faster to run.
           
Instructions: 1) Download all necessary files on to the desktop (csv files can be obained from the SQL queries see:   https://github.com/tonylnguyen/Codes/tree/master/Data_Wrangle/SQL_Queries)

(on mac)            a) Master Excel File
                    b) disagreements.csv
                    c) actors_metrics.csv
                    d) metrics.csv
                    
                2) Audit the disagreements.csv to ensure there are no false postitives
                
                3) press cmd+space to search for terminal
                
                4) in terminal type  "python " (with the space) and drag in the team_stats.py into termina and press enter
                
                5) code will return "It has been done Lord Vador" if everything was successful
                
Requirements: Python, numpy, pandas, openpyxl


Please notify Tony Nguyen for any issues.
