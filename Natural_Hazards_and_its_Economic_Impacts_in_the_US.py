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
from importing_data_files import *


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


if __name__ == '__main__':
    natural_disasters_order = ['Hurricanes', 'Tornadoes', 'Wildfires', 'Tsunamis', 'Earthquakes', 'Volcanoes']
    natural_disasters_data = [hurricanes_data, tornadoes_data, wildfires_data, tsunamis_data, earthquake_data, volcanoes_data]
    yearly_event_summary = yearly_event_count_summary(natural_disasters_order, natural_disasters_data)
