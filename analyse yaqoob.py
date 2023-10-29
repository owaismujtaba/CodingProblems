import numpy as np
import pandas as pd
from pandas import Timedelta
import pdb
from matplotlib import pyplot as plt
from datetime import datetime

# input the filepath here 
# Note you should have date time and Frequency columns in the data file
# LIKE ['date', 'time', 'Frequency'] put the below variables manually in analysis function
# remove_first, first_n, second_n, third_n = 20, 5, 3, 3
# target_freq_limit = [350, 600, 350]
filepath = '/content/mar082023phox2bhypoxia9283.csv'

def read_file():
    """
    Reads a CSV file and processes the data.

    Parameters:
    - filepath (str): The path to the CSV file to read.

    Returns:
    - data (pandas.DataFrame): A DataFrame containing processed data with columns 'date', 'time', and 'Frequency'.
    """
    data = pd.read_csv(filepath)
    data = data[['time', 'Frequency']]
    print("Original Data File Dimentions",data.shape)
    data.reset_index(inplace=True)
    data['time'] = data['time'].map(map_time)    
    
    return data

def map_time(times):
    """
    Map and transform a list of time strings.
    Parameters:
    - times: A list of time strings to be transformed.
    Returns:
    - A new list of time strings after transformation.
    -4 because at ecach time point it add .NNN at the end so we remove it 
    """
    times = times[:len(times)-4]
    
    
    return times

def remove_first_n_minutes(df, n_minutes):
    '''
    Remove the first n minutes of data from the given DataFrame.
    
    Parameters:
    df (DataFrame): The original DataFrame containing a datetime column.
    n_minutes (int): The number of minutes to remove from the beginning of the data.

    Returns:
    DataFrame: The DataFrame with the first n minutes of data removed.
    '''

    # Make sure the DataFrame has a datetime column named 'timestamp'
    time_column = 'time'
    #pdb.set_trace()
    if time_column not in df:
        raise ValueError("DataFrame must have a 'timestamp' column.")

    # Ensure the 'timestamp' column is in datetime format
    df[time_column] = pd.to_datetime(df[time_column])
    print('removeing from ',df[time_column].min())
    # Filter the DataFrame for the first n minutes of data
    remaining_df = df[df[time_column] > df[time_column].min() + pd.Timedelta(minutes=n_minutes)]

    return remaining_df
  
def extract_first_n_minutes(df, n_minutes):
    """
    Extract the first n minutes of data from a DataFrame with a datetime column.

    Parameters:
    - df: DataFrame with a datetime column.
    - n_minutes: Number of minutes to extract.

    Returns:
    - DataFrame containing the data for the first n minutes.
    """
    # Make sure the DataFrame has a datetime column named 'timestamp'
    time_column = 'time'
    
    if time_column not in df:
        raise ValueError("DataFrame must have a 'timestamp' column.")

    # Ensure the 'timestamp' column is in datetime format
    df[time_column] = pd.to_datetime(df[time_column])
  
    # Filter the DataFrame for the first n minutes of data
    first_n_minutes_data = df[df[time_column] < df[time_column].min() + pd.Timedelta(minutes=n_minutes)]

    return first_n_minutes_data


def extract_components_from_data(data, remove_first, first_n, second_n, third_n):
    """
    Extract components from data in multiple steps.

    Args:
    - data: Data file Pandas DataFrame
    - remove_first: Number of minutes to remove from the beginning of the data.
    - first_n: Number of minutes to extract in the first step.
    - second_n: Number of minutes to extract in the second step.
    - third_n: Number of minutes to extract in the third step.

    Returns:
    - A list containing three DataFrames:
      1. Data for the first `first_n` minutes.
      2. Data for the next `second_n` minutes.
      3. Data for the last `third_n` minutes.
    """
    
    data = remove_first_n_minutes(data, remove_first)
    
    first_10__minutes_data = extract_first_n_minutes(data, first_n)
    data = remove_first_n_minutes(data, first_n)
    second_10_minutes_data = extract_first_n_minutes(data,second_n )
    data = data = remove_first_n_minutes(data, second_n)
    third_10_minutes_data = extract_first_n_minutes(data, third_n)
    
    return [first_10__minutes_data, second_10_minutes_data, third_10_minutes_data]

def merge_components(data, target_freq_limit = [350, 600, 350]):
    n_components = len(data)
    final_data = pd.DataFrame()
    for component in range(n_components):
        component_data = data[component]
        limit = target_freq_limit[component]
        component_data = component_data[component_data['Frequency'] < limit]
        if component == 0:
            final_data = component_data
        else:
            final_data = pd.concat([final_data, component_data])
    
    return final_data

    
def compute_means_by_minutes(df):
    result = df.groupby([df['time'].dt.hour, df['time'].dt.minute]).mean()
    #pdb.set_trace()
    return result

def plot(data):
    x = [ i for i in range(data.shape[0])]
    y = data['Frequency'].values
    
    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    
    plt.savefig('plot.png', dpi = 600)
       
def analysis(remove_first, first_n, second_n, third_n, target_freq_limit):
    data = read_file()
    # Put these values maunally
   
    
    data = extract_components_from_data(data, remove_first, first_n, second_n, third_n)
    data = merge_components(data, target_freq_limit)
    
    data = compute_means_by_minutes(data)
    plot(data)
    data.to_csv('data30min.csv')
    
    return data
    
