r"""
This script focuses on reading all the input data files into pandas Dataframes
and formatting the columns as per their data types for the main processing.
"""
import pandas as pd

dateparser = lambda x: pd.to_datetime(x, errors='coerce', format='%m/%d/%Y')

storm_dtypes = {'EVENT_ID': 'Int64',
                'DEATHS_DIRECT': 'Int16',
                'INJURIES_DIRECT': 'Int16',
                'DAMAGE_PROPERTY_NUM': 'Int64',
                'DAMAGE_CROPS_NUM': 'Int64',
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
hurricanes_data['Year'] = pd.DatetimeIndex(hurricanes_data['BEGIN_DATE']).year

tornadoes_data = pd.read_csv('data/tornadoes.csv', header=0,
                             dtype=storm_dtypes,
                             date_parser=dateparser,
                             parse_dates=['BEGIN_DATE', 'END_DATE'])
tornadoes_data['Year'] = pd.DatetimeIndex(tornadoes_data['BEGIN_DATE']).year

wildfires_data = pd.read_csv('data/wildfires.csv', header=0, dtype=storm_dtypes,
                             date_parser=dateparser,
                             parse_dates=['BEGIN_DATE', 'END_DATE'])
wildfires_data['Year'] = pd.DatetimeIndex(wildfires_data['BEGIN_DATE']).year

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

GDP_by_state_data = pd.read_csv('data/GDP_by_state.csv', header=0,
                                dtype={'GeoName': str})

state_codes = pd.read_csv('data/state_codes.csv', header=0,
                          dtype={'State': str,
                                 'Code': str})
