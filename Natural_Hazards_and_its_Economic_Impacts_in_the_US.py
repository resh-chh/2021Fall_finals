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

if __name__ == '__main__':
    earthquake_file = open("data/earthquakes.tsv")
    tsunamis_file = open('data/tsunamis.tsv')
    volcanoes_file = open('data/volcanoes.tsv')
    tornadoes_data = open('data/tornadoes.csv')
    hurricanes_data = open('data/hurricanes.csv')
    wildfires_data = open('data/wildfires.csv')
    GDP_by_state_data = open('data/GDP_by_state.csv')
    earthquake_data = csv.reader(earthquake_file, delimiter="\t")
    tsunamis_data = csv.reader(tsunamis_file, delimiter="\t")
    volcanoes_data = csv.reader(volcanoes_file, delimiter="\t")

