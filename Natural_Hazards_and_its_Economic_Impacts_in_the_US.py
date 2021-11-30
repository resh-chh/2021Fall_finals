r"""
597PR Fall 2021 Final Project

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


def yearly_event_count_summary(natural_disasters_order: list, natural_disasters_data: list):
    yearly_event_count = pd.DataFrame({
        'Year': range(2000, 2022)
    })
    for disaster_name in natural_disasters_order:
        disaster_data_index = natural_disasters_order.index(disaster_name)
        disaster = natural_disasters_data[disaster_data_index]
        yearly_disaster_count = disaster.groupby(['Year']).size().reset_index(name=disaster_name)
        yearly_event_count = pd.merge(yearly_event_count, yearly_disaster_count, how='left').fillna(0)
        yearly_event_count = yearly_event_count.astype({disaster_name: 'Int16'})
    yearly_event_count['Total'] = yearly_event_count['Hurricanes'] + yearly_event_count['Tornadoes'] + \
                                  yearly_event_count['Wildfires'] + yearly_event_count['Tsunamis'] + \
                                  yearly_event_count['Earthquakes'] + yearly_event_count['Volcanoes']
    print(yearly_event_count)
    return yearly_event_count


def plot_yearwise_stacked_bar_graph(event_counter: pd.DataFrame, event1: str, event2: str):
    plt.bar(event_counter['Year'], event_counter[event1], color='r')
    plt.bar(event_counter['Year'], event_counter[event2], color='b', bottom=event_counter[event1])
    plt.legend([event1, event2])
    plt.xticks(rotation=45)
    plt.show()


def yearwise_statewise_event_summary_plot(event_dataset_list: list, year_val: int, event_list: list):
    dataset_length = len(event_dataset_list)
    length_of_dataset = 0
    while length_of_dataset < dataset_length:
        if length_of_dataset == 0:
            statewise_event = event_dataset_list[length_of_dataset][event_dataset_list[length_of_dataset]['Year'] ==
                                            year_val].groupby(['State']).size().reset_index\
                (name=event_list[length_of_dataset])
            statewise_event = statewise_event.astype({event_list[length_of_dataset]: 'Int16'})
        else:
            statewise_event = pd.merge(statewise_event, event_dataset_list[length_of_dataset][event_dataset_list
                                        [length_of_dataset]['Year'] ==year_val].groupby(['State'])
                                       .size().reset_index(name=event_list[length_of_dataset]), how='outer').fillna(0)
            statewise_event = statewise_event.astype({event_list[length_of_dataset]: 'Int16'})
        length_of_dataset += 1
    print(statewise_event)



if __name__ == '__main__':
    natural_disasters_order = ['Hurricanes', 'Tornadoes', 'Wildfires', 'Tsunamis', 'Earthquakes', 'Volcanoes']
    natural_disasters_data = [hurricanes_data, tornadoes_data, wildfires_data, tsunamis_data, earthquake_data, volcanoes_data]
    yearly_event_summary = yearly_event_count_summary(natural_disasters_order, natural_disasters_data)
    plot_yearwise_stacked_bar_graph(yearly_event_summary, 'Earthquakes', 'Tsunamis')
    yearwise_statewise_event_summary_plot([earthquake_data, tsunamis_data], 2018,['Earthquakes', 'Tsunamis'])
