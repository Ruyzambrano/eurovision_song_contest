# Eurovision Song Contest Data Exploration

## Setup

```sh
pip install -r requirements.txt
```

if you are using mac:
```sh
brew install libomp
```

## Structure of the Repository

### [Aggregated Language Data](./aggregated_language_data/)

This contains the _main_ scripts used to produce the machine learning model.

**NOTE**: This directory contains a file, [outputs.txt](./aggregated_language_data/outputs/outputs.txt) that contain the latest runs and testing metrics for the models

### [Cleaning Data](./cleaning_data/)

This contains the scripts to clean and combine the datasets.

### [Data](./data/)

This contains the datasets from the World Bank and Eurovision, separated into directories for each country

### [Feature Selection](./feature_selection/)

This contains experimental scripts that use Regressive Feature Elimination pipelines

**NOTE**: This script takes an immense amount of computational power, it ran for over 24 hours on my local machine before I interrupted it

### [Logs](./logs/)

Contains preliminary outputs for early ML models built. These have been discounted because it contains data that should not have been included

### [Test Feature Selection](./test_feature_selection/)

This contains the first round of experiments that have been discounted

### [Visualisations](./visualisations/)

Contains some visualisations from the preliminary data exploration

### Other scripts in the root directory

These scripts are basic data exploration notebooks and visualisation scripts

## Eurovision Language Data

Clearly, there is a preference for English in the Eurovision Song Contest:

![Times a song has used x language](visualisations/eurovision/count_chart.png)
![Total points scored by songs with x language](visualisations/eurovision/points_chart.png)

However, using English does not always mean higher points:
![Average points for songs in x language](visualisations/eurovision/averages_chart.png)

## World Bank Data

### Refugees and Eurovision Final Place

Some countries showed some weak correlation between their success in Eurovision (red) versus the refugee population (blue):

> Austria
> ![Refugees and Austria](visualisations/combined/Austria/austria_refugee_population_by_country_or_territory_of_origin.png)

> Belgium
> ![Refugees and Belgium](visualisations/combined/Belgium/belgium_refugee_population_by_country_or_territory_of_origin.png)

> Croatia
> ![Refugees and Croatia](visualisations/combined/Croatia/croatia_refugee_population_by_country_or_territory_of_origin.png)

> Hungary
> ![Refugees and Hungary](visualisations/combined/Hungary/hungary_refugee_population_by_country_or_territory_of_origin.png)

Others, not so much:

> Romania
> ![Refugees and Romania](visualisations/combined/Romania/romania_refugee_population_by_country_or_territory_of_origin.png)

> Bosnia and Herzegovina
> ![Refugees and Bosnia and Herzegovina](visualisations/combined/Bosnia_and_Herzegovina/bosnia_and_herzegovina_refugee_population_by_country_or_territory_of_origin.png)
