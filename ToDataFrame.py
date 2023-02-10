import json
import pandas as pd

def stock_dataset_file_to_DataFrame(path: str, stockName: str) -> pd.DataFrame:
  """Reads a json file and returns a DataFrame with the data of the stockName

  Args:
      path (str): File path to the json file
      stockName (str): Name of the stock to be read to the DataFrame

  Raises:
      ValueError: If the stockName is not found in the dataset

  Returns:
      pd.DataFrame: DataFrame with the data of the stockName
  """
  
  
  #read the json file
  with open(path, 'r') as f:
    data = json.load(f)
    
  if stockName not in data:
    raise ValueError("Stock name not found in dataset")
  
  return pd.DataFrame(data[stockName], columns=["DateTime", "Value"])