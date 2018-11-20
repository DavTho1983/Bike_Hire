from datetime import datetime, timedelta

import pandas as pd

from create_csv import createCSV


def get_average_journey_times(data):
    data = data.set_index([0]).T
    grouped_df = data.groupby(['Bike_ID'])
    average_bike_journey_times = []
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
            average_journey_time = sum(total_time, timedelta())/len(arrived)
        average_bike_journey_times.append(average_journey_time)
    average_average_bike_journey_time = sum(average_bike_journey_times, timedelta())/len(average_bike_journey_times)
    return average_average_bike_journey_time




def Main():
    create = createCSV()
    create.build_dataframe()
    data = pd.read_csv('data.csv', sep='\t', header=None)
    return get_average_journey_times(data)


if __name__ == '__main__':
    print(Main())