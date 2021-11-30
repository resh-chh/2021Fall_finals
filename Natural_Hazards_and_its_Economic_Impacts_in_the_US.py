r"""
597PR Fall 2021 Final Project

Topic: Natural Hazards and its Economic Impacts in the United States

Instructor: John Weible, jweible@illinois.edu

Collaborators:
    1. Rashmi Chhabria, rashmic2@illinois.edu
    2. Anushri Bhagwath, anushri5@illinois.edu

Description:
    This project focuses on assessing the interrelation between Natural Disasters
    and their impact on the Economy specifically in the United States of America.

Datasets:
    1.	Natural Hazards - https://www.ngdc.noaa.gov/hazard/hazards.shtml
    2.	World Development Indicators - https://databank.worldbank.org/source/world-development-indicators

Hypotheses:
    Hypothesis I: Natural Disasters are directly correlated with the economy
    and affect the country’s GDP - PPP (gross domestic product based on purchasing power parity)
    Hypothesis II: One natural disaster can lead to another, for instance,
    Hurricanes can set off more destructive Earthquakes.

References:
    1. Date parser for pandas: https://github.com/iSchool-597PR/Examples_2021Fall/blob/main/week_09/pandas_pt2.ipynb

"""
import pandas as pd
from importing_data_files import *
import matplotlib.pyplot as plt


def yearly_event_count_summary(natural_disasters_order: list, natural_disasters_data: list) -> pd.DataFrame:
    """
    Calculates the count of each type of disaster in every year, from 2000 - 2021.

    :param natural_disasters_order: list of disaster event types
    :param natural_disasters_data: list of data sets for each disaster event in order
    :return: dataframe containing count of disaster events of every type for every year from 2000 - 2021
    """
    yearly_event_count = pd.DataFrame({
        'Year': range(2000, 2022)
    })
    for disaster_name in natural_disasters_order:
        disaster_data_index = natural_disasters_order.index(disaster_name)
        disaster = natural_disasters_data[disaster_data_index]
        yearly_disaster_count = disaster.groupby(['Year']).size().reset_index(name=disaster_name)
        yearly_event_count = pd.merge(yearly_event_count, yearly_disaster_count, how='left').fillna(0)
        yearly_event_count = yearly_event_count.astype({disaster_name: 'Int16', 'Year': 'Int16'})
    yearly_event_count['Total'] = yearly_event_count['Hurricanes'] + yearly_event_count['Tornadoes'] + \
                                  yearly_event_count['Wildfires'] + yearly_event_count['Tsunamis'] + \
                                  yearly_event_count['Earthquakes'] + yearly_event_count['Volcanoes']
    # print(yearly_event_count)
    return yearly_event_count


def plot_yearwise_stacked_bar_graph(event_counter: pd.DataFrame, event1: str, event2: str):
    """

    :param event_counter:
    :param event1:
    :param event2:
    """
    plt.bar(event_counter['Year'], event_counter[event1], color='r')
    plt.bar(event_counter['Year'], event_counter[event2], color='b', bottom=event_counter[event1])
    plt.legend([event1, event2])
    plt.xticks(rotation=45)
    plt.show()


def yearwise_statewise_event_summary_plot(event_dataset_list: list, year_val: int, disaster_list: list):
    dataset_length = len(event_dataset_list)
    length_of_dataset = 0
    statewise_event = pd.DataFrame(columns=['State'])
    while length_of_dataset < dataset_length:
        statewise_event = pd.merge(statewise_event, event_dataset_list[length_of_dataset][event_dataset_list
                                        [length_of_dataset]['Year'] ==year_val].groupby(['State'])
                                       .size().reset_index(name=event_list[length_of_dataset]), how='outer').fillna(0)
        statewise_event = statewise_event.astype({disaster_list[length_of_dataset]: 'Int16'})
        length_of_dataset += 1
    print(statewise_event)
    return statewise_event


def calculate_percentage_change_in_GDP(GDP_data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates change in percentage for GDP throughout the years considering
    the year 2000 as the base. Change for every year is calculated by
    measuring the difference in GDP for that year from the year 2000.

    :param GDP_data: dataframe containing the GDP data throughout the years for United States
    :return: dataframe containing year wise percentage change between 2000 and every other year until 2021
    """
    GDP_for_US = GDP_data.iloc[0]
    base_GDP = GDP_for_US['2000']
    percentage_change_in_GDP = {2000: 0}
    for year in range(2001, 2021):
        subsequent_GDP = GDP_for_US[str(year)]
        change_in_GDP = subsequent_GDP - base_GDP
        percentage_change = change_in_GDP * 100 / base_GDP
        percentage_change = round(percentage_change, 2)
        percentage_change_in_GDP[year] = percentage_change
    percentage_change_in_GDP = pd.DataFrame.from_dict(percentage_change_in_GDP, orient='index',
                                                      columns=['GDP_change_in_percentage'])
    # print(percentage_change_in_GDP)
    return percentage_change_in_GDP


def find_combined_disaster_year(disaster_list: list, event_counter: pd.DataFrame):
    year_list = []
    for year in event_counter['Year']:
        year_val = event_counter.loc[event_counter['Year'] == year]
        for event1 in year_val[disaster_list[0]]:
            for event2 in year_val[disaster_list[1]]:
                if event1 != 0 and event2 != 0:
                    year_list.append(year)
    # print(year_list)
    return year_list


if __name__ == '__main__':
    natural_disasters_order = ['Hurricanes', 'Tornadoes', 'Wildfires', 'Tsunamis', 'Earthquakes', 'Volcanoes']
    natural_disasters_data = [hurricanes_data, tornadoes_data, wildfires_data, tsunamis_data, earthquake_data,
                              volcanoes_data]
    yearly_event_summary = yearly_event_count_summary(natural_disasters_order, natural_disasters_data)

    # plot the graph to show the occurrence of earthquakes and tsunamis each year from 2000-2021
    plot_yearwise_stacked_bar_graph(yearly_event_summary, 'Earthquakes', 'Tsunamis')
    # find the list of years in which earthquakes and tsunamis occurred at the same time
    event_list = ['Earthquakes', 'Tsunamis']
    disaster_years = find_combined_disaster_year(event_list, yearly_event_summary)
    # find the states in which the disasters occurred according to the years
    yearwise_statewise_event_summary = yearwise_statewise_event_summary_plot([earthquake_data, tsunamis_data], 2018,
                                                                             ['Earthquakes', 'Tsunamis'])

    percentage_change_in_GDP = calculate_percentage_change_in_GDP(GDP_by_state_data)
    event_summary_with_GDP = pd.merge(yearly_event_summary, percentage_change_in_GDP, left_on='Year', right_index=True,
                                      how='left')
    event_summary_with_GDP = event_summary_with_GDP.set_index('Year')
    # print(event_summary_with_GDP)
    # plt.plot(event_summary_with_GDP)
    # plt.show()
