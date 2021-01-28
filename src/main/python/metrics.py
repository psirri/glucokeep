"""
metrics.py -- Contains functions to calculate data visualization metrics.
Copyright (C) 2021  Paul Sirri <paulsirri@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np
from datetime import datetime, timedelta
import matplotlib.cbook as cbook


def get_time_in_range(glucose_interpolated):
    """
    <54
    54-70
    70-180
    180-250
    >250
    """
    counts = {
        'very above': 0,
        'above': 0,
        'target': 0,
        'below': 0,
        'very below': 0
    }

    for glucose in glucose_interpolated:
        if glucose < 54:
            counts['very below'] += 1
        elif 54 <= glucose < 70:
            counts['below'] += 1
        elif 70 <= glucose <= 180:
            counts['target'] += 1
        elif 180 < glucose <= 250:
            counts['above'] += 1
        elif 250 < glucose:
            counts['very above'] += 1

    time_in_range = {}
    for zone, count in counts.items():
        time_in_range[zone] = count / len(glucose_interpolated) * 100

    return time_in_range


def interpolate_glucose(glucose_events):
    # transpose the data to allow convenient access to columns
    glucose_events_t = list(zip(*glucose_events))

    # convert from native dateTime objects to timestamp floats
    timeseries_as_floats = [event_time.timestamp() for event_time in glucose_events_t[0]]
    start_time = timeseries_as_floats[0]
    end_time = timeseries_as_floats[-1]

    # the frequency of how often to make an interpolation estimation
    sampling_resolution = 10 * len(timeseries_as_floats)

    # create a list of equally-spaced time values in given range, formatted as floats
    t = np.linspace(start_time, end_time, sampling_resolution)

    # use piecewise linear interpolation to estimate glucose levels between measurements
    glucose_interpolated = np.interp(t, timeseries_as_floats, glucose_events_t[1])

    # convert the list of equally-spaced time values to dateTime objects
    time_interpolated = [datetime.fromtimestamp(event_time) for event_time in t]

    return glucose_interpolated, time_interpolated


def group_events_by_hour_in_day(events):
    # transpose the data to allow convenient access to columns
    events_t = list(zip(*events))

    # list of formatted DateTime objects
    time_series = events_t[0]

    # list of categories for each event type, represented by integers:
    # 0 = glucose, 1 = carbs, 2 = exercise, 3 = fast-acting insulin, 4 = long-acting insulin
    event_types = events_t[1]

    # list of floats values that quantify the corresponding event
    values = events_t[2]

    # list of integers that generalize exercise intensity (0 = light, 1 = moderate, 2 = heavy)
    exercise_intensities = events_t[3]

    # round to nearest hour-of-day to calculate particular metrics
    time_series_rounded_to_hour_in_day = [t.hour for t in time_series]

    # zip the lists back together
    events_using_hourly_timeseries = list(
        zip(time_series_rounded_to_hour_in_day, event_types,
            values, exercise_intensities))

    # group events by hour for evaluation and plotting
    events_grouped_by_hour_in_day = {i: [] for i in range(24)}
    for event in events_using_hourly_timeseries:
        events_grouped_by_hour_in_day[int(event[0])].append(event)

    return events_grouped_by_hour_in_day


def group_glucose_by_hour_in_day(events):
    # group events to the nearest hour for evaluation and plotting
    events_grouped_by_hour_in_day = group_events_by_hour_in_day(events)

    # extract only the glucose measurement from all events
    glucose_grouped_by_hour_in_day = {i: [] for i in range(24)}
    for hour_in_day, list_of_events in events_grouped_by_hour_in_day.items():
        for event in list_of_events:
            if event[1] == 0:
                # this is a glucose event, save the measurement to new dictionary
                glucose_grouped_by_hour_in_day[hour_in_day].append(event[2])

    return glucose_grouped_by_hour_in_day


def group_interp_glucose_by_hour_in_day(glucose_interpolated, time_interpolated):
    # round to nearest hour-of-day to calculate particular metrics
    time_series_rounded_to_hour_in_day = [t.hour for t in time_interpolated]

    # zip the lists back together
    events_using_hourly_timeseries = list(
        zip(time_series_rounded_to_hour_in_day, glucose_interpolated))

    # group events by hour for evaluation and plotting
    glucose_grouped_by_hour_in_day = {i: [] for i in range(24)}
    for event in events_using_hourly_timeseries:
        glucose_grouped_by_hour_in_day[int(event[0])].append(event[1])

    return glucose_grouped_by_hour_in_day


def get_iqr(glucose_grouped_by_hour_in_day, q1=25, q3=75):
    stats = {}
    for hour_in_day, hour_data in glucose_grouped_by_hour_in_day.items():
        # Compute the boxplot stats (as in the default matplotlib implementation)
        stat = cbook.boxplot_stats(hour_data)[0]
        if len(hour_data) < 2:
            stat = {
                'mean': -50,
                'iqr': -50,
                'cilo': -50,
                'cihi': -50,
                'whishi': -50,
                'whislo': -50,
                'fliers': [],
                'q1': -50,
                'med': -50,
                'q3': -50
            }
        else:

            q1_val, q3_val = np.nanpercentile(hour_data, [q1, q3])
            temp = [value for value in hour_data if q1_val <= value <= q3_val]

            stat = cbook.boxplot_stats(temp)[0]

            if len(temp) < 4:
                stat = {
                    'mean': -50,
                    'iqr': -50,
                    'cilo': -50,
                    'cihi': -50,
                    'whishi': -50,
                    'whislo': -50,
                    'fliers': [],
                    'q1': -50,
                    'med': -50,
                    'q3': -50
                }

            else:
                stat['q1'], stat['q3'] = np.nanpercentile(temp, [0, 100])

        stats[hour_in_day] = stat
    return stats


def calculate_percentile(data, rng=(25, 75)):
    # first group (Q1)
    q1 = np.percentile(data, rng[0], interpolation='midpoint')

    # third group (Q3)
    q3 = np.percentile(data, rng[1], interpolation='midpoint')

    # interquartile range (IQR)
    iqr = q3 - q1

    return iqr
