# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_cols, countries):
    """
    Reads data from an Excel file and performs necessary preprocessing.

    Parameters:
    - excel_url (str): URL of the Excel file.
    - sheet_name (str): Name of the sheet containing data.
    - new_cols (list): List of columns to select from the data.
    - countries (list): List of countries to include in the analysis.

    Returns:
    - data_read (DataFrame): Preprocessed data.
    - data_transpose (DataFrame): Transposed data.
    """
    data_read = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
    data_read = data_read[new_cols]
    data_read.set_index('Country Name', inplace=True)
    data_read = data_read.loc[countries]

    return data_read, data_read.T

# The Excel URL below indicates GDP growth (annual %)
excel_url_GDP = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel'
# The Excel URL below indicates arable land (% of land area)
excel_url_arable_land = 'https://api.worldbank.org/v2/en/indicator/AG.LND.ARBL.ZS?downloadformat=excel'
# The Excel URL below indicates forest area (% of land area)
excel_url_forest_area = 'https://api.worldbank.org/v2/en/indicator/AG.LND.FRST.ZS?downloadformat=excel'
# The Excel URL below indicates Urban population growth (annual %)
excel_url_urban = 'https://api.worldbank.org/v2/en/indicator/SP.URB.GROW?downloadformat=excel'
# The Excel URL below indicates electricity production from oil, gas, and coal sources (% of total)
excel_url_electricity = 'https://api.worldbank.org/v2/en/indicator/EG.ELC.FOSL.ZS?downloadformat=excel'
# The Excel URL below indicates Agriculture, forestry, and fishing, value added (% of GDP)
excel_url_agriculture = 'https://api.worldbank.org/v2/en/indicator/NV.AGR.TOTL.ZS?downloadformat=excel'
# The Excel URL below indicates CO2 emissions (metric tons per capita)
excel_url_CO2 = 'https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=excel'

# Parameters for reading and transposing data
sheet_name = 'Data'
new_cols = ['Country Name', '1984', '1990', '1995', '2000', '2005', '2010', '2015', '2020', '2022']
countries = [ 'South Africa', 'China', 'India', 'United States', 'Germany', 'France', 'United Kingdom', 'Japan', 'Mexico', 'Indonesia', 'Argentina', 'Nigeria', 'Italy', 'Pakistan']

# Read and transpose arable land data
data_arable_land, data_arable_land_transpose = read_data_excel(excel_url_arable_land, sheet_name, new_cols, countries)
# Read and transpose forest area data
data_forest_area, data_forest_area_transpose = read_data_excel(excel_url_forest_area, sheet_name, new_cols, countries)
# Read and transpose GDP data
data_GDP, data_GDP_transpose = read_data_excel(excel_url_GDP, sheet_name, new_cols, countries)
# Read and transpose Urban population growth data
data_urban_read, data_urban_transpose = read_data_excel(excel_url_urban, sheet_name, new_cols, countries)
# Read and transpose electricity production data
data_electricity_read, data_electricity_transpose = read_data_excel(excel_url_electricity, sheet_name, new_cols, countries)
# Read and transpose agriculture data
data_agriculture_read, data_agriculture_transpose = read_data_excel(excel_url_agriculture, sheet_name, new_cols, countries)
# Read and transpose CO2 emissions data
data_CO2, data_CO2_transpose = read_data_excel(excel_url_CO2, sheet_name, new_cols, countries)


# Print the transposed data
print(data_GDP_transpose)

# Describe the statistics of GDP growth (annual %)
GDP_statistics = data_GDP_transpose.describe()
print(GDP_statistics)

def multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    """
    Plots multiple line plots.

    Parameters:
    - x_data (array-like): X-axis data.
    - y_data (list of array-like): Y-axis data for multiple lines.
    - xlabel (str): X-axis label.
    - ylabel (str): Y-axis label.
    - title (str): Plot title.
    - labels (list): List of labels for each line.
    - colors (list): List of colors for each line.
    """
    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=10)

    for i in range(len(y_data)):
        plt.plot(x_data, y_data[i], label=labels[i], color=colors[i])

    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.legend(bbox_to_anchor=(1.02, 1))
    plt.show()

# Display data
print(data_agriculture_read)
print(data_agriculture_transpose)

# The function below constructs a bar plot
def bar_plot(labels_array, width, y_data, y_label, label, title, rotation=0):
    """
    Plot a grouped bar plot.

    Parameters:
    - labels_array (array-like): X-axis labels.
    - width (float): Width of each bar group.
    - y_data (list of array-like): Y-axis data for each bar.
    - y_label (str): Y-axis label.
    - label (list): Labels for each bar group.
    - title (str): Plot title.
    - rotation (float): Rotation angle for X-axis labels.
    """
    x = np.arange(len(labels_array))
    fig, ax = plt.subplots(figsize=(8, 6), dpi=200)

    for i in range(len(y_data)):
        plt.bar(x + width * i, y_data[i], width, label=label[i])

    plt.title(title, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.xlabel(None)
    plt.xticks(x + width * (len(y_data) - 1) / 2, labels_array, rotation=rotation)

    plt.legend()
    ax.tick_params(bottom=False, left=True)

    plt.show()

# Each of the preprocessed and transposed dataframes are printed below
print(data_urban_read)
print(data_urban_transpose)

# Define a function to construct a scatter plot
def scatter_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    """
    Constructs a scatter plot.

    Parameters:
    - x_data (list): X-axis data.
    - y_data (list of lists): Y-axis data for multiple lines.
    - xlabel (str): X-axis label.
    - ylabel (str): Y-axis label.
    - title (str): Title of the plot.
    - labels (list): Labels for each line.
    - colors (list): Colors for each line.
    """
    plt.figure(figsize=(8, 6), dpi=200)
    plt.title(title, fontsize=10)

    for i in range(len(y_data)):
        plt.scatter(x_data, y_data[i], label=labels[i], color=colors[i], s=50)  # 's' is the marker size

    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.legend(bbox_to_anchor=(1.02, 1))
    plt.show()
    return

# Define a function to create a correlation heatmap
def correlation_heatmap(data, corr, title):
    """
    Displays a correlation heatmap for the given data.

    Parameters:
    - data (DataFrame): Input data.
    - corr (DataFrame): Correlation matrix.
    - title (str): Title for the heatmap.
    """
    plt.figure(figsize=(8, 6), dpi=200)
    plt.imshow(corr, cmap='cividis', interpolation='none')
    plt.colorbar()

    # Show all ticks and label them with the dataframe column name
    plt.xticks(range(len(data.columns)), data.columns, rotation=90, fontsize=10)
    plt.yticks(range(len(data.columns)), data.columns, rotation=0, fontsize=10)

    plt.title(title, fontsize=10)

    # Loop over data dimensions and create text annotations
    labels = corr.values
    for i in range(labels.shape[0]):
        for j in range(labels.shape[1]):
            plt.text(j, i, '{:.2f}'.format(labels[i, j]),
                     ha="center", va="center", color="white")

    plt.show()

# Plot a multiple line plot for GDP growth (annual %) for selected countries
x_data_gdp = data_GDP_transpose.index
y_data_gdp = [data_GDP_transpose[country] for country in countries]
xlabel_gdp = 'Years'
ylabel_gdp = '(%) GDP Growth'
labels_gdp = countries
colors_gdp = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_gdp = 'Annual (%) GDP Growth for Selected Countries'

# Plot the line plots for GDP of selected countries
multiple_plot(x_data_gdp, y_data_gdp, xlabel_gdp, ylabel_gdp, title_gdp, labels_gdp, colors_gdp)
# The parameters for producing grouped bar plots of Agriculture, forestry, and fishing, value added (% of GDP)
labels_array = countries
width = 0.2
y_data = [
    data_agriculture_read['1990'],
    data_agriculture_read['1995'],
    data_agriculture_read['2000'],
    data_agriculture_read['2005']
]
y_label = '% of GDP'
label = ['Year 1990', 'Year 1995', 'Year 2000', 'Year 2005']
title = 'Agriculture, forestry, and fishing, value added (% of GDP)'

# The parameters are passed into the defined function and produce the desired plot
bar_plot(labels_array, width, y_data, y_label, label, title,  rotation=55)

# Extract data for urban population growth
urban_growth_data = data_urban_transpose.loc[:, countries]

# Print urban population growth data
print("Urban Population Growth Data:")
print(urban_growth_data)

# Plot a multiple line plot for Urban Population Growth (%) for selected countries
x_data_urban = urban_growth_data.index
y_data_urban = [urban_growth_data[country] for country in countries]
xlabel_urban = 'Years'
ylabel_urban = '(%) Urban Population Growth'
labels_urban = countries
colors_urban = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_urban = 'Annual (%) Urban Population Growth for Selected Countries'

# Plot the line plots for Urban Population Growth of selected countries
multiple_plot(x_data_urban, y_data_urban, xlabel_urban, ylabel_urban, title_urban, labels_urban, colors_urban)
# Create a dataframe for Mexico using selected indicators
data_Mexico = {
    'Urban pop. growth': data_urban_transpose['Mexico'],
    'Electricity production': data_electricity_transpose['Mexico'],
    'Agric. forestry and Fisheries': data_agriculture_transpose['Mexico'],
    'CO2 Emissions': data_CO2_transpose['Mexico'],
    'Forest Area': data_forest_area_transpose['Mexico'],
    'GDP Annual Growth': data_GDP_transpose['Mexico']
}
df_Mexico = pd.DataFrame(data_Mexico)

# Display the dataframe and correlation matrix
print(df_Mexico)
corr_Mexico = df_Mexico.corr()
print(corr_Mexico)

# Display the correlation heatmap for Mexico
correlation_heatmap(df_Mexico, corr_Mexico, 'Mexico')

# Create a dataframe for China using selected indicators
data_China = {
    'Urban pop. growth': data_urban_transpose['China'],
    'Electricity production': data_electricity_transpose['China'],
    'Agric. forestry and Fisheries': data_agriculture_transpose['China'],
    'CO2 Emissions': data_CO2_transpose['China'],
    'Forest Area': data_forest_area_transpose['China'],
    'GDP Annual Growth': data_GDP_transpose['China']
}
df_Chaina = pd.DataFrame(data_China)

# Display the dataframe and correlation matrix
print(df_Chaina)
corr_Chaina = df_Chaina.corr()
print(corr_Chaina)

# Display the correlation heatmap for China
correlation_heatmap(df_Chaina, corr_Chaina, 'China')

# Plot a multiple line plot for Electricity Production (annual %) for selected countries
x_data_electricity = data_electricity_transpose.index
y_data_electricity = [data_electricity_transpose[country] for country in countries]
xlabel_electricity = 'Years'
ylabel_electricity = '(%) Electricity Production'
labels_electricity = countries
colors_electricity = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_electricity = 'Annual (%) of Electricity Production of different Countries'

# Plot the line plots for Electricity Production of selected countries
multiple_plot(x_data_electricity, y_data_electricity, xlabel_electricity, ylabel_electricity, title_electricity, labels_electricity, colors_electricity)


# Plot a multiple line plot for Urban land (annual %) for selected countries
x_data_urban_land = data_arable_land_transpose.index
y_data_urban_land = [data_arable_land_transpose[country] for country in countries]
xlabel_urban_land = 'Years'
ylabel_urban_land = '(%) Urban land'
labels_urban_land = countries
colors_urban_land = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_urban_land = 'Annual (%) of Urban land of different Countries'

# Plot the line plots for Urban land of selected countries
multiple_plot(x_data_urban_land, y_data_urban_land, xlabel_urban_land, ylabel_urban_land, title_urban_land, labels_electricity, colors_urban_land)

# parameters for producing multiple plots of CO2 emissions (metric tons per capita)
x_data = data_CO2_transpose.index # the  row index is used as the values for the x-axis
y_data = [data_CO2_transpose['Germany'], 
          data_CO2_transpose['United States'], 
          data_CO2_transpose['Nigeria'],
          data_CO2_transpose['China'], 
          data_CO2_transpose['Pakistan'], 
          data_CO2_transpose['India']]
xlabel = 'Year'
ylabel = 'metric tons'
labels = ['Germany', 'USA', 'UK', 'Nigeria', 'China', 'Pakistan', 'India']
colors = ['red', 'magenta', 'blue', 'yellow', 'green', 'purple', 'black']
title = 'CO2 emissions (metric tons per capita)'

# the attributes are passed into the function and returned to give the desired plot
multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)
