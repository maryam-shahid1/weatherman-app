from weather_reading import *
from weatherman import get_month
import os


class ParsingData:

    def parsing_file_data(self, file):
        file_content = file.readlines()
        file_size = len(file_content)
        list = []

        for i in range(1, file_size):
            data = file_content[i]
            reading = data.split(',')
            day = reading[0]
            max_temp = mean_temp = min_temp = mean_humidity = ''
            if reading[1] != '' and reading[1] != ',':
                max_temp = int(reading[1])
            if reading[2] != '' and reading[2] != ',':
                mean_temp = int(reading[2])
            if reading[3] != '' and reading[3] != ',':
                min_temp = int(reading[3])
            if reading[8] != '' and reading[8] != ',':
                mean_humidity = int(reading[8])

            list.append(WeatherReading(day, max_temp, mean_temp,
                                       min_temp, mean_humidity)) 
        return list

    def month_parsing(self, file_name):
        with open(file_name, "r") as file:
            file = open(file_name, "r")
            list = self.parsing_file_data(file)
        return list

    def year_parsing(self, filename):
        monthly_readings = []
        for i in range(1, 12):
            file_name = filename + '_' + get_month(i) + '.txt'
            if os.path.isfile(file_name):
                file = open(file_name)
                list = self.parsing_file_data(file)
                monthly_readings.append(list)
        return monthly_readings