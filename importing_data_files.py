r"""
This script focuses on reading all the input data files into pandas Dataframes
and formatting the columns as per their data types for the main processing.
"""
import pandas as pd

dateparser = lambda x: pd.to_datetime(x, errors='coerce', format='%m/%d/%Y')

storm_dtypes = {'EVENT_ID': 'Int64',
                'DEATHS_DIRECT': 'Int16',
                'INJURIES_DIRECT': 'Int16',
                'DAMAGE_PROPERTY_NUM': 'float64',
                'DAMAGE_CROPS_NUM': 'float64',
                'EPISODE_ID': 'Int64',
                'CZ_FIPS': 'Int16',
                'INJURIES_INDIRECT': 'Int16',
                'DEATHS_INDIRECT': 'Int16',
                'TOR_LENGTH': 'float16',
                'TOR_WIDTH': 'float16',
                'BEGIN_LAT': 'float16',
                'BEGIN_LON': 'float16',
                'END_LAT': 'float16',
                'END_LON': 'float16'}

hurricanes_data = pd.read_csv('data/hurricanes.csv', header=0,
                              dtype=storm_dtypes,
                              date_parser=dateparser,
                              parse_dates=['BEGIN_DATE', 'END_DATE'])
# Extracting the year for the event
hurricanes_data['Year'] = pd.DatetimeIndex(hurricanes_data['BEGIN_DATE']).year
# Converting the Begin date column into datetime format
hurricanes_data['BEGIN_DATE'] = hurricanes_data['BEGIN_DATE'].astype('datetime64[ns]')
# Calculating total damage caused in $Mil
hurricanes_data['Total_Damage'] = (hurricanes_data['DAMAGE_PROPERTY_NUM'] + hurricanes_data['DAMAGE_CROPS_NUM']) / 10000000


tornadoes_data = pd.read_csv('data/tornadoes.csv', header=0,
                             dtype=storm_dtypes,
                             date_parser=dateparser,
                             parse_dates=['BEGIN_DATE', 'END_DATE'])
# Extracting the year for the event
tornadoes_data['Year'] = pd.DatetimeIndex(tornadoes_data['BEGIN_DATE']).year
# Calculating total damage caused in $Mil
tornadoes_data['Total_Damage'] = (tornadoes_data['DAMAGE_PROPERTY_NUM'] + tornadoes_data['DAMAGE_CROPS_NUM']) / 10000000
# Converting the Begin_date column into datetime format
tornadoes_data['BEGIN_DATE'] = tornadoes_data['BEGIN_DATE'].astype('datetime64[ns]')

wildfires_data = pd.read_csv('data/wildfires.csv', header=0, dtype=storm_dtypes,
                             date_parser=dateparser,
                             parse_dates=['BEGIN_DATE', 'END_DATE'])
# Extracting the year for the event
wildfires_data['Year'] = pd.DatetimeIndex(wildfires_data['BEGIN_DATE']).year
# Calculating total damage caused in $Mil
wildfires_data['Total_Damage'] = (wildfires_data['DAMAGE_PROPERTY_NUM'] + wildfires_data['DAMAGE_CROPS_NUM']) / 10000000
# Converting the Begin_date column into datetime format
wildfires_data['BEGIN_DATE'] = wildfires_data['BEGIN_DATE'].astype('datetime64[ns]')

earthquake_data = pd.read_csv("data/earthquakes.tsv", sep='\t', header=0,
                              usecols=['Year', 'Mo', 'Dy', 'Hr', 'Mn', 'Sec', 'Tsu', 'Location Name',
                                       'State', 'Mag', 'Total Deaths', 'Total Missing', 'Total Injuries',
                                       'Total Damage ($Mil)', 'Total Houses Destroyed',
                                       'Total Houses Damaged'],
                              dtype={'Year': 'Int16',
                                     'Mo': 'Int8',
                                     'Dy': 'Int8',
                                     'Hr': 'Int8',
                                     'Mn': 'Int8',
                                     'Sec': 'float16',
                                     'Tsu': 'Int16',
                                     'Location Name': str,
                                     'State': str,
                                     'Mag': 'float16',
                                     'Total Deaths': 'Int16',
                                     'Total Missing': 'Int16',
                                     'Total Injuries': 'Int16',
                                     'Total Damage ($Mil)': 'float16',
                                     'Total Houses Destroyed': 'float16',
                                     'Total Houses Damaged': 'float16'
                                     })
# Creating a Begin_date column using the Year, Mo and Dy columns and converting it into datetime format
cols = ["Mo","Dy", "Year"]
earthquake_data['BEGIN_DATE'] = earthquake_data[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
earthquake_data['BEGIN_DATE'] = earthquake_data['BEGIN_DATE'].astype('datetime64[ns]')

earthquake_data.rename(columns={'Total Damage ($Mil)': 'Total_Damage'}, inplace=True)


tsunamis_data = pd.read_csv('data/tsunamis.tsv', sep='\t', header=0,
                            usecols=['Year', 'Mo', 'Dy', 'Hr', 'Mn', 'Sec', 'Earthquake Magnitude',
                                     'Location Name', 'State', 'Maximum Water Height (m)',
                                     'Number of Runups', 'Total Injuries', 'Total Damage ($Mil)',
                                     'Total Houses Destroyed'],
                            dtype={'Year': 'Int16',
                                   'Mo': 'Int8',
                                   'Dy': 'Int8',
                                   'Hr': 'Int8',
                                   'Mn': 'Int8',
                                   'Sec': 'float16',
                                   'Earthquake Magnitude': 'float16',
                                   'Location Name': str,
                                   'State': str,
                                   'Maximum Water Height (m)': 'float16',
                                   'Number of Runups': 'Int8',
                                   'Total Injuries': 'Int8',
                                   'Total Damage ($Mil)': 'float16',
                                   'Total Houses Destroyed': 'Int16'
                                   })
tsunamis_data.rename(columns={'Total Damage ($Mil)': 'Total_Damage'}, inplace=True)
# Creating a Begin_date column using the Year, Mo and Dy columns and converting it into datetime format
tsunamis_data['BEGIN_DATE'] = tsunamis_data[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
tsunamis_data['BEGIN_DATE'] = tsunamis_data['BEGIN_DATE'].astype('datetime64[ns]')


volcanoes_data = pd.read_csv('data/volcanoes.tsv', sep='\t', header=0,
                             usecols=['Year', 'Mo', 'Dy', 'Tsu', 'Eq', 'Name', 'Location', 'State',
                                      'Elevation (m)', 'Type', 'Total Deaths', 'Total Missing',
                                      'Total Injuries', 'Total Damage ($Mil)', 'Total Houses Destroyed'],
                             dtype={'Year': 'Int16',
                                    'Mo': 'Int8',
                                    'Dy': 'Int8',
                                    'Tsu': 'Int16',
                                    'Eq': 'Int16',
                                    'Name': str,
                                    'Location': str,
                                    'State': str,
                                    'Elevation (m)': 'Int16',
                                    'Type': str,
                                    'Total Deaths': 'Int16',
                                    'Total Missing': 'Int16',
                                    'Total Injuries': 'Int16',
                                    'Total Damage ($Mil)': 'float16',
                                    'Total Houses Destroyed': 'float16',
                                    }
                             )

volcanoes_data.rename(columns={'Total Damage ($Mil)': 'Total_Damage'}, inplace=True)
# Creating a Begin_date column using the Year, Mo and Dy columns and converting it into datetime format
volcanoes_data['BEGIN_DATE'] = volcanoes_data[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
volcanoes_data['BEGIN_DATE'] = volcanoes_data['BEGIN_DATE'].astype('datetime64[ns]')

GDP_by_state_data = pd.read_csv('data/GDP_by_state.csv', header=0,
                                dtype={'GeoName': str})

state_codes = pd.read_csv('data/state_codes.csv', header=0,
                          dtype={'State': str,
                                 'Code': str})
state_codes.rename(columns={'State': 'State_Name', 'Code': 'State'}, inplace=True)
