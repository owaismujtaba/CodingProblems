class FibonacciNumber:
    def __init__(self):
        self.memorization = {}
        
    def calculate_fibonacchi(self,n):
        if n in self.memorization:
            return self.memorization[n]
        elif n < 2:
            return 1
        else:
            self.memorization[n] = self.calculate_fibonacchi(n-1) + self.calculate_fibonacchi(n-2)
            return self.memorization[n]

if __name__ == '__main__':
    obj = FibonacciNumber()
    print(obj.calculate_fibonacchi(100))
    print(obj.memorization)
    
    
import pdb
def extract_meaningfull_data(data):
  data = data[['date', 'time', 'Frequency']]
  return data

def map_time(times):
  return times[:7]

def extract_10_minutes(data):
  #pdb.set_trace()
  end_time = data['time'].iloc[0] + pd.Timedelta(minutes=10)
  #print(end_time)
  # Extract data from the beginning to the end time
  extracted_df = data[data['time'] <= end_time]
  #print(extracted_df)
  remaining_data = data[data['time'] > end_time]
  return extracted_df, remaining_data

def split_data(data, freq_limit):
  #freq_limit is the frequenct limit to include. above it are excluded
  
  # Extract  meaning full variables only
  data = extract_meaningfull_data(data)

  # Converting time to datwtime
  data['time'] = data['time'].map(map_time)
  data['time'] = pd.to_datetime(data['time'])

  # Exclude first 10 minutes
  _, data = extract_10_minutes(data)


  # Splitting data to three time intervals
  baseline_data, data = extract_10_minutes(data)
  hypercapinia_data, data = extract_10_minutes(data)
  recovery_data, data = extract_10_minutes(data)


  # Filtering baseline and recovery

  baseline_data = baseline_data[baseline_data['Frequency'] < freq_limit]
  recovery_data = recovery_data[recovery_data['Frequency'] < freq_limit]

  # Combinte all three data tables
  filtered_data = pd.concat([baseline_data, hypercapinia_data, recovery_data])

  return filtered_data