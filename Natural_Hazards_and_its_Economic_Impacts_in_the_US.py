r"""
597PR Fall 2021 Final Project

Topic: Natural Hazards and its Economic Impacts in the United States

Description:
    This project focuses on assessing the interrelation between Natural Disasters
    and their impact on the Economy specifically in the United States of America.

References:
    1. Date parser for pandas: https://github.com/iSchool-597PR/Examples_2021Fall/blob/main/week_09/pandas_pt2.ipynb
    2. Economic Impacts of Natural Disasters: https://www.journals.uchicago.edu/doi/10.1093/reep/rez004
    ** Other examples shown in class from Github may also have been referred

"""
import pandas as pd
from importing_data_files import *
import matplotlib.pyplot as plt
from IPython.display import display
import numpy as np
import datetime


def yearly_event_summary(natural_disasters_order: list, natural_disasters_data: list) -> (pd.DataFrame, pd.DataFrame):
    """
    Calculates the count of each type of disaster in every year, from 2000 - 2021.

    :param natural_disasters_order: list of disaster event types
    :param natural_disasters_data: list of data sets for each disaster event in order
    :return: dataframe containing count of disaster events of every type for every year from 2000 - 2021
    >>> order = ['Hurricanes', 'Tornadoes', 'Wildfires', 'Tsunamis', 'Earthquakes', 'Volcanoes']
    >>> hurricane = {'Year': [2000, 2001, 2002], 'Total_Damage': [500000, 1100642, 1102750]}
    >>> hurricane = pd.DataFrame.from_dict(hurricane)
    >>> data = [hurricane, hurricane, hurricane, hurricane, hurricane, hurricane]
    >>> yearly_event_summary(order, data)
    (    Year  Hurricanes  Tornadoes  ...  Volcanoes  Total_Damage  Damage_Percentage
    0   2000    500000.0   500000.0  ...   500000.0     3000000.0          18.495283
    1   2001   1100642.0  1100642.0  ...  1100642.0     6603852.0          40.713370
    2   2002   1102750.0  1102750.0  ...  1102750.0     6616500.0          40.791347
    3   2003         0.0        0.0  ...        0.0           0.0           0.000000
    4   2004         0.0        0.0  ...        0.0           0.0           0.000000
    5   2005         0.0        0.0  ...        0.0           0.0           0.000000
    6   2006         0.0        0.0  ...        0.0           0.0           0.000000
    7   2007         0.0        0.0  ...        0.0           0.0           0.000000
    8   2008         0.0        0.0  ...        0.0           0.0           0.000000
    9   2009         0.0        0.0  ...        0.0           0.0           0.000000
    10  2010         0.0        0.0  ...        0.0           0.0           0.000000
    11  2011         0.0        0.0  ...        0.0           0.0           0.000000
    12  2012         0.0        0.0  ...        0.0           0.0           0.000000
    13  2013         0.0        0.0  ...        0.0           0.0           0.000000
    14  2014         0.0        0.0  ...        0.0           0.0           0.000000
    15  2015         0.0        0.0  ...        0.0           0.0           0.000000
    16  2016         0.0        0.0  ...        0.0           0.0           0.000000
    17  2017         0.0        0.0  ...        0.0           0.0           0.000000
    18  2018         0.0        0.0  ...        0.0           0.0           0.000000
    19  2019         0.0        0.0  ...        0.0           0.0           0.000000
    20  2020         0.0        0.0  ...        0.0           0.0           0.000000
    <BLANKLINE>
    [21 rows x 9 columns],     Year  Hurricanes  Tornadoes  ...  Earthquakes  Volcanoes  Total_Count
    0   2000           1          1  ...            1          1            6
    1   2001           1          1  ...            1          1            6
    2   2002           1          1  ...            1          1            6
    3   2003           0          0  ...            0          0            0
    4   2004           0          0  ...            0          0            0
    5   2005           0          0  ...            0          0            0
    6   2006           0          0  ...            0          0            0
    7   2007           0          0  ...            0          0            0
    8   2008           0          0  ...            0          0            0
    9   2009           0          0  ...            0          0            0
    10  2010           0          0  ...            0          0            0
    11  2011           0          0  ...            0          0            0
    12  2012           0          0  ...            0          0            0
    13  2013           0          0  ...            0          0            0
    14  2014           0          0  ...            0          0            0
    15  2015           0          0  ...            0          0            0
    16  2016           0          0  ...            0          0            0
    17  2017           0          0  ...            0          0            0
    18  2018           0          0  ...            0          0            0
    19  2019           0          0  ...            0          0            0
    20  2020           0          0  ...            0          0            0
    <BLANKLINE>
    [21 rows x 8 columns])
    """
    yearly_event_count = pd.DataFrame({
        'Year': range(2000, 2021)
    })
    yearly_damage_summary = pd.DataFrame({
        'Year': range(2000, 2021)
    })
    for disaster_name in natural_disasters_order:
        disaster_data_index = natural_disasters_order.index(disaster_name)
        disaster = natural_disasters_data[disaster_data_index]
        disaster = disaster[disaster['Year'] < 2021]
        yearly_disaster_count = disaster.groupby(['Year']).size().reset_index(name=disaster_name)
        yearly_disaster_damage = disaster.groupby(['Year']).sum().fillna(0)

        yearly_disaster_damage = yearly_disaster_damage[['Total_Damage']].rename(columns={'Total_Damage': disaster_name}).reset_index()

        yearly_damage_summary = pd.merge(yearly_damage_summary, yearly_disaster_damage, left_on='Year', right_on='Year', how='left').fillna(0)
        yearly_event_count = pd.merge(yearly_event_count, yearly_disaster_count, how='left').fillna(0)
        yearly_event_count = yearly_event_count.astype({disaster_name: 'Int16', 'Year': 'Int16'})

    yearly_event_count['Total_Count'] = yearly_event_count['Hurricanes'] + yearly_event_count['Tornadoes'] + \
                                        yearly_event_count['Wildfires'] + yearly_event_count['Tsunamis'] + \
                                        yearly_event_count['Earthquakes'] + yearly_event_count['Volcanoes']
    yearly_damage_summary['Total_Damage'] = yearly_damage_summary['Hurricanes'] + yearly_damage_summary['Tornadoes'] + \
                                            yearly_damage_summary['Wildfires'] + yearly_damage_summary['Tsunamis'] + \
                                            yearly_damage_summary['Earthquakes'] + yearly_damage_summary['Volcanoes']
    # Calculating yearly percentage of damage caused from total damage done throughout the years
    total_damage = yearly_damage_summary[['Total_Damage']].sum()
    yearly_damage_summary['Damage_Percentage'] = yearly_damage_summary['Total_Damage'] * 100 / total_damage['Total_Damage']
    return yearly_damage_summary, yearly_event_count


def plot_yearwise_stacked_bar_graph(event_counter: pd.DataFrame, event1: str, event2: str):
    """
    Plot the years when the two natural disaster occurred against the number of natural disasters
    every year.

    :param event_counter:Dataframe containing the data regarding the number of natural disasters
            which occured every year
    :param event1: 1st natural disaster to be plotted
    :param event2: 2nd natural disaster to be plotted
    """
    plt.figure(figsize=(15, 8))
    plt.xlabel("Year")
    plt.ylabel("Number of Disasters")
    plt.title("Number of Natural Disasters per year")
    plt.bar(event_counter['Year'], event_counter[event1], color='r')
    plt.bar(event_counter['Year'], event_counter[event2], color='b', bottom=event_counter[event1])
    plt.legend([event1, event2])
    plt.xticks(rotation=45)
    plt.show()


def yearwise_statewise_event_summary_plot(event_dataset_list: list, year_list: list,
                                          disaster_list: list) -> pd.DataFrame:
    """
    Find if the two natural disasters occur in the same state in the US for the all years when they
    occurred together. If yes, then create a dataframe of all the states and the number of natural
    disaster occurrences in that state for each year.

    :param event_dataset_list: list of dataframes of the two natural disasters in question
    :param year_list: List of all the years when the two natural disasters occurred together
    :param disaster_list: list of the two natural disasters in question
    :return: dataframe containing the states,years and the number of times the two natural disasters
             occurred in same state in the same year.
    >>> years = [2000,2002]
    >>> list_of_disaster = ['Earthquakes','Tsunamis']
    >>> earthquakes = {'Year': [2000, 2001, 2002], 'State': ['HI','AK','AK']}
    >>> earthquakes = pd.DataFrame.from_dict(earthquakes)
    >>> tsunamis = {'Year': [2000, 2002, 2003], 'State': ['HI','CA','AK']}
    >>> tsunamis = pd.DataFrame.from_dict(tsunamis)
    >>> yearwise_statewise_event_summary_plot([earthquakes,tsunamis], years, list_of_disaster)
      State  Earthquakes  Tsunamis  Year
    0    HI            1         1  2000
    """
    yearly_statewise_event = pd.DataFrame(columns=['State', disaster_list[0], disaster_list[1], 'Year'])

    for year in year_list:
        dataset_length = len(event_dataset_list)
        length_of_dataset = 0
        statewise_event = pd.DataFrame(columns=['State'])
        while length_of_dataset < dataset_length:
            statewise_event = pd.merge(statewise_event, event_dataset_list[length_of_dataset][event_dataset_list
                                            [length_of_dataset]['Year'] == year].groupby(['State'])
                                           .size().reset_index(name=disaster_list[length_of_dataset]), how='outer').fillna(0)
            statewise_event = statewise_event.astype({disaster_list[length_of_dataset]: 'Int16'})
            length_of_dataset += 1
        for index, row in statewise_event.iterrows():
            if row[disaster_list[0]] == 0 or row[disaster_list[1]] == 0:
                statewise_event = statewise_event.drop(index=index)
        statewise_event['Year'] = year

        yearly_statewise_event = pd.concat([statewise_event, yearly_statewise_event]).sort_values('Year')

    # print(yearly_statewise_event)
    return yearly_statewise_event


def calculate_percentage_change_in_GDP(GDP_data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates change in percentage for GDP throughout the years considering
    the year 2000 as the base. Change for every year is calculated by
    measuring the difference in GDP for that year from the year 2000.

    :param GDP_data: dataframe containing the GDP data throughout the years for United States
    :return: dataframe containing year wise percentage change between 2000 and every other year until 2021
    >>> US_GDP = {'2000': [10250952], '2001': [10581929], '2002': [10929108], '2003': [11456450], '2004': [12217196],'2005': [13039197], '2006': [13815583], '2007': [14474228], '2008': [14769862], '2009': [14478067], '2010': [15048970], '2011': [15599731], '2012': [16253970], '2013': [16843196], '2014': [17550687], '2015': [18206023], '2016': [18695106], '2017': [19479623], '2018': [20527159], '2019': [21372582], '2020': [20893746]}
    >>> US_GDP = pd.DataFrame.from_dict(US_GDP)
    >>> calculate_percentage_change_in_GDP(US_GDP)
        Year  ...  GDP_change_in_percentage
    0   2000  ...                      0.00
    1   2001  ...                      3.23
    2   2002  ...                      3.28
    3   2003  ...                      4.83
    4   2004  ...                      6.64
    5   2005  ...                      6.73
    6   2006  ...                      5.95
    7   2007  ...                      4.77
    8   2008  ...                      2.04
    9   2009  ...                     -1.98
    10  2010  ...                      3.94
    11  2011  ...                      3.66
    12  2012  ...                      4.19
    13  2013  ...                      3.63
    14  2014  ...                      4.20
    15  2015  ...                      3.73
    16  2016  ...                      2.69
    17  2017  ...                      4.20
    18  2018  ...                      5.38
    19  2019  ...                      4.12
    20  2020  ...                     -2.24
    <BLANKLINE>
    [21 rows x 4 columns]

    """
    GDP_for_US = GDP_data.iloc[0]
    base_GDP_for_2000 = GDP_for_US['2000']
    base_GDP = base_GDP_for_2000
    total_GDP = {2000: base_GDP}
    percentage_change_in_GDP_from_2000 = {2000: 0}
    percentage_change_in_GDP = {2000: 0}
    for year in range(2001, 2021):
        subsequent_GDP = GDP_for_US[str(year)]
        change_in_GDP_from_2000 = subsequent_GDP - base_GDP_for_2000
        change_in_GDP = subsequent_GDP - base_GDP
        percentage_change_from_2000 = change_in_GDP_from_2000 * 100 / base_GDP_for_2000
        percentage_change = change_in_GDP * 100 / base_GDP
        percentage_change_from_2000 = round(percentage_change_from_2000, 2)
        percentage_change = round(percentage_change, 2)
        total_GDP[year] = subsequent_GDP
        percentage_change_in_GDP_from_2000[year] = percentage_change_from_2000
        percentage_change_in_GDP[year] = percentage_change
        base_GDP = subsequent_GDP
    total_GDP = pd.DataFrame.from_dict(total_GDP, orient='index', columns=['GDP_for_US'])
    percentage_change_in_GDP_from_2000 = pd.DataFrame.from_dict(percentage_change_in_GDP_from_2000, orient='index',
                                                      columns=['GDP_change_in_percentage_from_2000'])
    percentage_change_in_GDP_from_2000 = pd.merge(total_GDP, percentage_change_in_GDP_from_2000, left_index=True, right_index=True, how='outer')
    percentage_change_in_GDP = pd.DataFrame.from_dict(percentage_change_in_GDP, orient='index',
                                                      columns=['GDP_change_in_percentage'])
    percentage_change_in_GDP = pd.merge(percentage_change_in_GDP_from_2000, percentage_change_in_GDP, left_index=True, right_index=True, how='outer')
    percentage_change_in_GDP.index.name = 'Year'
    percentage_change_in_GDP.reset_index(inplace=True)
    return percentage_change_in_GDP


def find_combined_disaster_year(disaster_list: list, event_counter: pd.DataFrame) -> list:
    """
    Find the list of years in which the two natural disasters occurred together

    :param disaster_list: list of the natural disasters in question
    :param event_counter: dataframe containing the number of times the natural disasters have
                     occurred in each year
    :return:list of years in which the two natural disasters have occurred together
    >>> list_of_disasters = ['Earthquakes','Tsunamis']
    >>> disaster_occurrence = {'Year': [2000, 2002, 2003], 'Earthquakes': [43,9,91], 'Tsunamis' : [45,1,9]}
    >>> disaster_occurrence = pd.DataFrame.from_dict(disaster_occurrence)
    >>> find_combined_disaster_year(list_of_disasters,disaster_occurrence)
       Year  Earthquakes  Tsunamis
    0  2000           43        45
    1  2002            9         1
    2  2003           91         9
    [2000, 2002, 2003]
    """
    year_list = []
    print(event_counter)
    for year in event_counter['Year']:
        year_val = event_counter.loc[event_counter['Year'] == year]
        for event1 in year_val[disaster_list[0]]:
            for event2 in year_val[disaster_list[1]]:
                if event1 != 0 and event2 != 0:
                    year_list.append(year)
    # print(year_list)
    return year_list


def retrieve_information_required_by_state(natural_disasters_order: list, natural_disasters_data: list, state_codes: pd.DataFrame, start_year: int, end_year: int, information_col: str) -> pd.DataFrame:
    """
    Dynamic Function to retrieve data grouped by states in the United States in a span of defined years.

    :param natural_disasters_order: list of disaster event types
    :param natural_disasters_data: list of data sets for each disaster event in order
    :param state_codes: dataframe containing dataset with State names and their codes
    :param start_year: year from where the information is required
    :param end_year: end year till where the information is required
    :param information_col: column that is required to be grouped by states
    :return: dataframe containing information column required from every Natural disaster grouped by State
    >>> order = ['Hurricanes', 'Tornadoes', 'Wildfires', 'Tsunamis', 'Earthquakes', 'Volcanoes']
    >>> hurricane = {'Year': [2000, 2001, 2002], 'Total_Damage': [500000, 1100642, 1102750], 'State': ['AL', 'AK', 'AZ']}
    >>> hurricane = pd.DataFrame.from_dict(hurricane)
    >>> data = [hurricane, hurricane, hurricane, hurricane, hurricane, hurricane]
    >>> state = {'State': ['AL', 'AK', 'AZ'], 'State_Name': ['Alabama', 'Alaska', 'Arizona']}
    >>> state = pd.DataFrame.from_dict(state)
    >>> retrieve_information_required_by_state(order, data, state, 2000, 2002, 'Total_Damage')
      State State_Name  Hurricanes  ...  Earthquakes  Volcanoes    Total
    0    AL    Alabama      500000  ...       500000     500000  3000000
    1    AK     Alaska     1100642  ...      1100642    1100642  6603852
    2    AZ    Arizona     1102750  ...      1102750    1102750  6616500
    <BLANKLINE>
    [3 rows x 9 columns]

    """
    information_retrieved = state_codes[['State', 'State_Name']]
    for disaster_name in natural_disasters_order:
        disaster_data_index = natural_disasters_order.index(disaster_name)
        disaster = natural_disasters_data[disaster_data_index]
        disaster = disaster[disaster['Year'] <= end_year]
        disaster = disaster[start_year <= disaster['Year']]
        disaster_information = disaster.groupby(['State']).sum().replace(np.nan,  0)
        disaster_information = disaster_information[[information_col]].rename(columns={information_col: disaster_name}).reset_index()
        information_retrieved = pd.merge(information_retrieved, disaster_information, left_on='State', right_on='State', how='left')
    information_retrieved = information_retrieved.replace(np.nan, 0)
    information_retrieved['Total'] = information_retrieved['Hurricanes'] + information_retrieved['Tornadoes'] + \
                                     information_retrieved['Wildfires'] + information_retrieved['Tsunamis'] + \
                                     information_retrieved['Earthquakes'] + information_retrieved['Volcanoes']
    return information_retrieved


def find_disaster_occurrence_within_days(disaster1: pd.DataFrame, disaster2: pd.DataFrame,
                                         disasters_acc_state: pd.DataFrame, disaster_list : list) -> pd.DataFrame:
    """
    Find if the two natural disasters occur within 5 days of each other. If yes, store the year of
    occurrence, state in which the disasters occurred and the begin dates of both the natural disasters
    in a dataframe.

    :param disaster1: dataframe of the first natural disaster
    :param disaster2: dataframe of the second natural disaster
    :param disasters_acc_state: dataframe containing the states,years and the number of times the
                two natural disasters occurred in same state in the same year.
    :param disaster_list: list of the two natural disasters in question
    :return:
    """
    disaster_occurrence_by_date = pd.DataFrame(columns=('Year', 'State',
                            disaster_list[0] + ' Begin_Date', disaster_list[1] + ' Begin_Date'))

    for index1, row1 in disasters_acc_state.iterrows():
        disaster1_by_dates = disaster1.loc[(disaster1['Year'] == row1['Year']) &
                                           (disaster1['State'] == row1['State'])]
        disaster2_by_dates = disaster2.loc[(disaster2['Year'] == row1['Year']) &
                                           (disaster2['State'] == row1['State'])]
        for index, row in disaster1_by_dates.iterrows():
            for value in disaster2_by_dates['BEGIN_DATE'].values:
                if row['BEGIN_DATE'] <= value <= row['BEGIN_DATE']+datetime.timedelta(days=5):
                    dict = {'Year': row1['Year'], 'State': row1['State'],
                            disaster_list[0] + ' Begin_Date': row['BEGIN_DATE'],
                            disaster_list[1] + ' Begin_Date': value}
                    disaster_occurrence_by_date = disaster_occurrence_by_date.append(dict, ignore_index=True)
    disaster_occurrence_by_date.set_index('Year', inplace=True)

    return disaster_occurrence_by_date

