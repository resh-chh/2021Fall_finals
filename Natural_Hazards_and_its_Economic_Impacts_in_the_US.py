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

"""
import csv
import pandas as pd

if __name__ == '__main__':
    earthquake_data = pd.read_csv("data/earthquakes.tsv", sep='\t', header=0)
    tsunamis_data = pd.read_csv('data/tsunamis.tsv', sep='\t', header=0)
    volcanoes_data = pd.read_csv('data/volcanoes.tsv', sep='\t', header=0)
    tornadoes_data = pd.read_csv('data/tornadoes.csv', header=0)
    hurricanes_data = pd.read_csv('data/hurricanes.csv', header=0)
    wildfires_data = pd.read_csv('data/wildfires.csv', header=0)
    GDP_by_state_data = pd.read_csv('data/GDP_by_state.csv', header=0)
