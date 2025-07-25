# FitBit-RCM
Code for downloading and working with FitBit API data. 

To use the code, ensure the following libraries are installed: 
- requests>=2.1
- pandas>=2.0
- numpy>=2.1

Libraries can be installed at command-line using pip:
```
pip install numpy pandas requests
```

To download the data, run WebAPI_export.py in your command-line using the following arguments:
```
python WebAPI_export.py user startDate endDate Folder AccessToken
```

  **user:** account username
  
  **Start Date:** Start of study period or time of interest: Format as YYYY-mm-dd
  
  **End Date:** End of study perior or time of interest: Format as YYYY-mm-dd
  
  **Folder:** Output folder for data - make sure that this folder exists or the script will not work
  
  **Access Token:** See FitBit API Data Set-Up document for how to generate an access token for a device

Example:
```
python WebAPI_export.py C4GNWR 2024-06-02 2024-06-27 ../Data/TestOutput eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BHWFAiLCJzdWIiOiJDNEdOV1IiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNzUzMjg3Nzg0LCJpYXQiOjE3MjE3NTE3ODR9.fShOEJRzu6iqhL-juyLBxYGzlqeo1W-LsvrblTbTi6I
```

**Please note the above access code and username are expired & are just there as an example** 

**Important Note:** To export WebAPI data, the code needs to start running 5 minutes before the top of an hour (ex. 3:00pm). This is because the Fitbit API has a maximum request limit of 150, and the code requires more than this to run. By running the code 5 minutes before the top of an hour, and then pausing the code in the middle for 10 minutes (included in the code), we are able to raise this request limit to 300, which is able to successfully extract all the data (this is because the request limit resets at the top of every hour).


Currently the following datatypes from FitBit are included:
- Activity Zone Minutes: AZM_summary
- Activity data:
    - Activity_goals_daily
    - Activity_goals_weekly
    - Activity_log_list
    - Activity_types
    - Lifetime_stats
    - Daily_activity_summary
    - Favourite_activities
    - Frequent_activities
    - Recent_activity_types 
- Walking data:
    - Distance_time_series
    - Elevation_time_series
    - Floors_time_series
    - Steps_time_series
    - Distance_intraday
    - Elevation_intraday
    - Floors_intraday
    - Steps_intraday
- Calorie data:
    - Calories_intraday
    - activityCalories_time_series
    - caloriesBMR_time_series
    - minutesSedentary_time_series
    - Calories_time_series
    - minutesLightlyActive_time_series
    - minutesFairlyActive_time_series
    - minutesVeryActive_time_series
- Vitals data:
    - RR_summary
    - HR_time_series
    - HR_intraday
    - HRV_summary
    - HRV_intraday
    - SpO2_summary
    - SpO2_intraday
    - RR_intraday
    - ECG_log_list
- Sleep data:
    - Sleep_goal
    - Sleep_log
    - Sleep_log_list

For a list of the different data-types from fitbit, check out their dev wiki here: https://dev.fitbit.com/build/reference/web-api/
More info on how to generate a token can be found here: https://dev.fitbit.com/build/reference/web-api/explore/

The code can be edited to add-in missing datatypes as well. 




