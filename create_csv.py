import datetime
import random

import pandas as pd


class CreateCsv:
    def build_csv(self):
        columns = ['Station_ID', 'Bike_ID', 'Arrival_Datetime', 'Departure_Datetime']
        bike_hire = pd.DataFrame(columns=columns, index=None)

        """
            If there were 10000 bikes and 100 records,
            we would probably not get enough data to track
            a particular bike between stations to get average
            journey times. This way of generating dummy data means
            that, even tho a bike can have a numbered ID from 1 to 10000,
            there are only 10 bikes to choose from.
         """

        bike_ids = []
        for i in range(10):
            bike_ids.append(random.randrange(1, 10000))

        for i in range(1000):
            arrival = self.get_random_arrival_time()
            bike_hire.loc[i] = [
                self.get_random_station_id(),
                self.get_random_bike_id(bike_ids),
                arrival.isoformat(),
                self.get_random_departure_time(arrival).isoformat()
            ]

        bike_hire = bike_hire.sort_values(by='Arrival_Datetime', ascending=True)
        bike_hire = bike_hire.reset_index().T.drop(['index'])
        data_csv = bike_hire.to_csv('data.csv', sep='\t', encoding='utf-8', date_format=str, header=False)
        return data_csv

    def get_random_station_id(self):
        random_station_id = random.randrange(1, 1000)
        return random_station_id

    def get_random_bike_id(self, bike_ids):
        random_bike_id = random.choice(bike_ids)
        return random_bike_id

    def get_random_arrival_time(self):
        now = datetime.datetime.now().replace(microsecond=0)
        random_no_days = random.randrange(0, 29)
        random_no_hours = random.randrange(0, 23)
        random_no_minutes = random.randrange(0, 59)
        random_no_seconds = random.randrange(0, 59)
        arrival_datetime = now - datetime.timedelta(days=random_no_days,
                                                    hours=random_no_hours,
                                                    minutes=random_no_minutes,
                                                    seconds=random_no_seconds)
        return arrival_datetime

    def get_random_departure_time(self, arrival_datetime):
        random_no_hours = random.randrange(0, 24)
        random_no_minutes = random.randrange(0, 59)
        random_no_seconds = random.randrange(0, 59)
        departure_datetime = arrival_datetime + datetime.timedelta(hours=random_no_hours,
                                                                   minutes=random_no_minutes,
                                                                   seconds=random_no_seconds)
        return departure_datetime


create = CreateCsv()
if __name__ == '__main__':
    create.build_csv()
