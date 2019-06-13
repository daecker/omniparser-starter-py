

import json
import statistics
import pandas
import os

def calculate_latest_closing_price_from_json(x):
    with open(x,"r") as f:
        file_contents = f.read()
        #print (type(file_contents))
        #print (file_contents)
    
    stock_price = json.loads(file_contents)
    print(stock_price)
    print(type(stock_price))

    # need last refreshed date and "4. closing price"



if __name__ == "__main__":
    print("PARSING SOME STOCK PRICES HERE...")
  
    aapl_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_aapl.json")

    print(aapl_filepath)
    close_price = calculate_latest_closing_price_from_json(aapl_filepath)
    print(close_price)
