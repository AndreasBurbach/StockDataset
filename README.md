# Stock Dataset

This dataset contains up to 20 stocks and stock market indices. The data was read in every 1-3 seconds with a Raspberry Pi 4 and saved as JSON.

The data contains the values of the shares from 9 am to 6pm german time. So because it's all collected in Germany the data is from the Frankfurt stock market.
To read the data as DataFrame with pandas, feel free to use my python script.

The JSON was built with a dictionary in python according to the following scheme:


	{ "Stock1":
	 [ [DateTime("%Y-%m-%d %H:%M:%S.%f"), Value],
	   [DateTime("%Y-%m-%d %H:%M:%S.%f"), Value],
	   ...]
	  "Stock2": ...
	}