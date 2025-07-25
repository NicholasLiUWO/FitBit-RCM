# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:46:11 2023

@author: Jansen Zhou
"""

import requests
import pandas as pd
import numpy as np
from datetime import datetime
import json
from pathlib import Path
import argparse
import time

# Create parser
parser = argparse.ArgumentParser(description="Info to send to FitBit Web API")

# Add arguments
parser.add_argument("user", type=str, help="User")
parser.add_argument("startDate", type=str, help="Start of study period: Format as YYYY-mm-dd")
parser.add_argument("endDate", type=str, help="End of study period: Format as YYYY-mm-dd")
parser.add_argument("AccessToken", type=str, help="Access Token (should have been obtained after setting up the account)")

# Parse arguments
args = parser.parse_args()

# Convert string to datetime.date
startdate = datetime.strptime(args.startDate, "%Y-%m-%d").date()
enddate = datetime.strptime(args.endDate, "%Y-%m-%d").date()
access_token=args.AccessToken
user=args.user

# In[1]:    
    
#Patient parameters to change
#Save path
base = Path('../TestExport') ##Change this path to whatever folder you want to save your results in 
base.mkdir(exist_ok=True)
daterange = pd.date_range(start=startdate, end=enddate)

HR_intraday_total = []
Daily_activity_summary_total = []
Calories_intraday_total = []
Distance_intraday_total = []
Elevation_intraday_total = []
Floors_intraday_total = []
Steps_intraday_total = []

# In[2]:

#get API data specified by uri
header = {'Authorization' : 'Bearer {}'.format(access_token)}
    
#activity data
AZM_summary = requests.get('https://api.fitbit.com/1/user/{user}/activities/active-zone-minutes/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
Activity_goals_daily = requests.get('https://api.fitbit.com/1/user/{user}/activities/goals/daily.json'.format(user=user), headers=header).json() #1 request
Activity_goals_weekly = requests.get('https://api.fitbit.com/1/user/{user}/activities/goals/weekly.json'.format(user=user), headers=header).json() #1 request
Activity_log_list = requests.get('https://api.fitbit.com/1/user/{user}/activities/list.json?afterDate={startdate}&sort=asc&offset=0&limit=100'.format(user=user, startdate=startdate), headers=header).json() #1 request
Activity_types = requests.get('https://api.fitbit.com/1/activities.json', headers=header).json() #1 request
#Favourite_activities = requests.get('https://api.fitbit.com/1/user/{user}/activities/favorite.json'.format(user=user), headers=header).json() #1 request
#Frequent_activities = requests.get('https://api.fitbit.com/1/user/{user}/activities/frequent.json'.format(user=user), headers=header).json() #1 request
Lifetime_stats = requests.get('https://api.fitbit.com/1/user/{user}/activities.json'.format(user=user), headers=header).json() #1 request
#Recent_activity_types = requests.get('https://api.fitbit.com/1/user/{user}/activities/recent.json'.format(user=user), headers=header).json() #1 request
    
Calories_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/calories/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
Distance_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/distance/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
Elevation_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/elevation/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
Floors_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/floors/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
Steps_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/steps/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request

activityCalories_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/activityCalories/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
caloriesBMR_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/caloriesBMR/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
minutesSedentary_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/minutesSedentary/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
minutesLightlyActive_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/minutesLightlyActive/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
minutesFairlyActive_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/minutesFairlyActive/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
minutesVeryActive_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/minutesVeryActive/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request

#body data
#Body_goals_weight = requests.get('https://api.fitbit.com/1/user/{user}/body/log/weight/goal.json'.format(user=user), headers=header).json() #1 request
#Body_goals_fat = requests.get('https://api.fitbit.com/1/user/{user}/body/log/fat/goal.json'.format(user=user), headers=header).json() #1 request
#Body_time_series_bmi = requests.get('https://api.fitbit.com/1/user/{user}/body/bmi/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
#Body_time_series_fat = requests.get('https://api.fitbit.com/1/user/{user}/body/fat/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
#Body_time_series_weight = requests.get('https://api.fitbit.com/1/user/{user}/body/weight/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
#Weight_time_series = requests.get('https://api.fitbit.com/1/user/{user}/body/log/weight/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
    
#RR and VO2 data
RR_summary = requests.get('https://api.fitbit.com/1/user/{user}/br/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
#VO2_summary = requests.get('https://api.fitbit.com/1/user/{user}/cardioscore/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request

#Heart data
#ECG_log_list = requests.get('https://api.fitbit.com/1/user/{user}/ecg/list.json?afterDate={startdate}&sort=asc&limit=10&offset=0'.format(user=user, startdate=startdate), headers=header).json() #1 request
HR_time_series = requests.get('https://api.fitbit.com/1/user/{user}/activities/heart/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
HRV_summary = requests.get('https://api.fitbit.com/1/user/{user}/hrv/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
    
#Sleep data
Sleep_goal = requests.get('https://api.fitbit.com/1.2/user/{user}/sleep/goal.json'.format(user=user), headers=header).json() #1 request
Sleep_log = requests.get('https://api.fitbit.com/1.2/user/{user}/sleep/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
Sleep_log_list = requests.get('https://api.fitbit.com/1.2/user/{user}/sleep/list.json?afterDate={startdate}&sort=asc&offset=0&limit=100'.format(user=user, startdate=startdate), headers=header).json() #1 request

#Oxygen saturation data
SpO2_summary = requests.get('https://api.fitbit.com/1/user/{user}/spo2/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
    
#Temperature data
#Temp_core = requests.get('https://api.fitbit.com/1/user/{user}/temp/core/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
#Temp_skin = requests.get('https://api.fitbit.com/1/user/{user}/temp/skin/date/{startdate}/{enddate}.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request

#intraday data
#AZM_intraday = requests.get('https://api.fitbit.com/1/user/{user}/activities/active-zone-minutes/date/{startdate}/{enddate}/1min.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
RR_intraday = requests.get('https://api.fitbit.com/1/user/{user}/br/date/{startdate}/{enddate}/all.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
HRV_intraday = requests.get('https://api.fitbit.com/1/user/{user}/hrv/date/{startdate}/{enddate}/all.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
SpO2_intraday = requests.get('https://api.fitbit.com/1/user/{user}/spo2/date/{startdate}/{enddate}/all.json'.format(user=user, startdate=startdate, enddate=enddate), headers=header).json() #1 request
print(RR_intraday)

for date in daterange:
    
    HR_intraday = requests.get('https://api.fitbit.com/1/user/{user}/activities/heart/date/{date}/1d/1min.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #28 requests
    HR_intraday_total.append(HR_intraday)
    Daily_activity_summary = requests.get('https://api.fitbit.com/1/user/{user}/activities/date/{date}.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #28 requests
    Daily_activity_summary_total.append(Daily_activity_summary)
    #Body_fat_log = requests.get('https://api.fitbit.com/1/user/{user}/body/log/fat/date/{date}.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #28 requests
    #Weight_log = requests.get('https://api.fitbit.com/1/user/{user}/body/log/weight/date/{date}.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #28 requests


#change or comment out if needed
time.sleep(600)
        
for date in daterange:
    Calories_intraday = requests.get('https://api.fitbit.com/1/user/{user}/activities/calories/date/{date}/1d/1min.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #recnum requests
    Calories_intraday_total.append(Calories_intraday)
    Distance_intraday = requests.get('https://api.fitbit.com/1/user/{user}/activities/distance/date/{date}/1d/1min.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #recnum requests
    Distance_intraday_total.append(Distance_intraday)
    Elevation_intraday = requests.get('https://api.fitbit.com/1/user/{user}/activities/elevation/date/{date}/1d/1min.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #recnum requests
    Elevation_intraday_total.append(Elevation_intraday)
    Floors_intraday = requests.get('https://api.fitbit.com/1/user/{user}/activities/floors/date/{date}/1d/1min.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #recnum requests
    Floors_intraday_total.append(Floors_intraday)
    Steps_intraday = requests.get('https://api.fitbit.com/1/user/{user}/activities/steps/date/{date}/1d/1min.json'.format(user=user, date=date.strftime("%Y-%m-%d")), headers=header).json() #recnum requests
    Steps_intraday_total.append(Steps_intraday)
                    
filenames = ("AZM_summary","Activity_goals_daily","Activity_goals_weekly","Activity_log_list","Activity_types","Lifetime_stats",
                      "Calories_time_series","Distance_time_series","Elevation_time_series","Floors_time_series","Steps_time_series",
                      "activityCalories_time_series","caloriesBMR_time_series","minutesSedentary_time_series","minutesLightlyActive_time_series","minutesFairlyActive_time_series","minutesVeryActive_time_series",
                      "RR_summary",
                      "HR_time_series","HRV_summary",
                      "Sleep_goal","Sleep_log","Sleep_log_list",
                      "SpO2_summary",
                      "RR_intraday","HRV_intraday","SpO2_intraday",
                      "HR_intraday","Daily_activity_summary",
                      "Calories_intraday","Distance_intraday","Elevation_intraday","Floors_intraday","Steps_intraday")

filelist = np.array([AZM_summary,Activity_goals_daily,Activity_goals_weekly,Activity_log_list,Activity_types,Lifetime_stats,
                      Calories_time_series,Distance_time_series,Elevation_time_series,Floors_time_series,Steps_time_series,
                      activityCalories_time_series,caloriesBMR_time_series,minutesSedentary_time_series,minutesLightlyActive_time_series,minutesFairlyActive_time_series,minutesVeryActive_time_series,
                      RR_summary,
                      HR_time_series,HRV_summary,
                      Sleep_goal,Sleep_log,Sleep_log_list,
                      SpO2_summary,
                      RR_intraday,HRV_intraday,SpO2_intraday,
                      HR_intraday_total,Daily_activity_summary_total,
                      Calories_intraday_total,Distance_intraday_total,Elevation_intraday_total,Floors_intraday_total,Steps_intraday_total], dtype=object)

##Write files out as separate json files
arr2 = np.stack((filenames, filelist), axis=1)

for name, file in arr2:
    jsonpath = base / ('{name}.json'.format(name=name))
    jsonpath.write_text(json.dumps(file, ensure_ascii=False, indent=4))


