# FitBit-RCM
Code for downloading and working with FitBit API data. 

To use the code, ensure the following libraries are installed: 
- requests>=2.1
- pandas>=2.0
- numpy>=2.1

To download the data, run WebAPI_export.py in your command-line using the following arguments:

  **user:** account username
  
  **Start Date:** Start of study period or time of interest: Format as YYYY-mm-dd
  
  **End Date:** End of study perior or time of interest: Format as YYYY-mm-dd
  
  **Folder:** Output folder for data
  
  **Access Token:** See FitBit API Data Set-Up document for how to generate an access token for a device

Example:
```
python WebAPI_export.py C4GNWR 2024-06-02 2024-06-27 ../Data/TestOutput eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BHWFAiLCJzdWIiOiJDNEdOV1IiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNzUzMjg3Nzg0LCJpYXQiOjE3MjE3NTE3ODR9.fShOEJRzu6iqhL-juyLBxYGzlqeo1W-LsvrblTbTi6I
```

**Please note the above access code and username are expired & are just there as an example** 


