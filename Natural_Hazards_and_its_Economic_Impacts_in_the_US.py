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


if __name__ == '__main__':
    print(tsunamis_data['State'])
    # print(earthquake_state[0])
