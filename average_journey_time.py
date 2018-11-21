from datetime import datetime, timedelta

import pandas as pd

from create_csv import CreateCsv


def get_average_journey_times(data):
    data = data.set_index([0]).T
    grouped_df = data.groupby(['Bike_ID'])
    average_bike_journey_times = [] #The average journey times for each bike
    bike_journey_times_all_bikes = []
    journeys = 0
    for bike, item in grouped_df:
        arrived = []
        departed = []
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            for i in grouped_df.get_group(bike)['Arrival_Datetime']:
                arrived.append(datetime.fromisoformat(i))
            for i in grouped_df.get_group(bike)['Departure_Datetime']:
                departed.append(datetime.fromisoformat(i))
            arrived = arrived[1:]
            departed = departed[:-1]
            total_time = []
            for d, a in zip(departed, arrived):
                journey_time = a - d
                total_time.append(journey_time)
                bike_journey_times_all_bikes.append(journey_time)
            """Commented code refers to the average journey time for a particular bike"""
            # average_journey_time = sum(total_time, timedelta())/len(arrived)
            journeys += len(arrived)
        # average_bike_journey_times.append(average_journey_time)
    print(journeys)
    average_average_bike_journey_time = sum(bike_journey_times_all_bikes, timedelta())/journeys
    seconds = average_average_bike_journey_time.seconds
    days = average_average_bike_journey_time.days
    hours, seconds = divmod(seconds, 3600)
    hours = (days*24) + hours
    minutes, seconds = divmod(seconds, 60)

    """
        There is a possibility that there could be a larger numbers of hours than there are format places eg: hhh:mm:ss.
        In this case there is no cutoff because I thought it wasn't that meaningful to have just the remaining hours mod 
        100 so I decided to keep the data
    """

    average_average_bike_journey_time_formatted = f"{hours}:{minutes}:{seconds}"
    return average_average_bike_journey_time_formatted


def main():
    create = CreateCsv()
    create.build_csv()
    data = pd.read_csv('data.csv', sep='\t', header=None)
    return get_average_journey_times(data)


if __name__ == '__main__':
    print(main())