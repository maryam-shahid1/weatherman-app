# weatherman-app
WeatherMan App Readme

**Functionality:**  

+ weatherman.py:  
WeatherReading: Data structure to hold each weather reading.  
ParsingData: Class for parsing the files and populating the WeatherReading data structure with  correct data types.   
Main: Responsible for calling apppropriate methods to generate the required report.  

+ calculations.py  
ReportCalculations: Class for computing month or year report calculations given the WeatherReadings data structure.  

+ report.py:  
Report: Class for creating the reports given the Results data structure.  
Results: Data structure for holding the calculations results.   


**Commands to run project:**  

First, create a virtual environment and activate it using command:  
source virtual_env/bin/activate  

To get any year's report:  
python3 weatherman.py -e 2005   

To get any month's report:  
python3 weatherman.py -a 2006/4  

To get any month's report in the form of charts:  
python3 weatherman.py -c 2006/4  

To get multiple reports (any order can be followed):  
python3 weatherman.py -a year/month -e year -c year/month  

