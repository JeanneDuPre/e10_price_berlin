# Find the cheapest gas station

The goal of this project is to find the cheapest gas station within a 5 km radius. 

### Structure
1. I made hourly API queries from tankerkoenig (19.10.2023 - now).
2. The API queries were automated via github actions.
   [![Cheapest gas station](https://github.com/JeanneDuPre/e10_price_berlin/actions/workflows/cheapest_gas_station.yml/badge.svg)](https://github.com/JeanneDuPre/e10_price_berlin/actions/workflows/cheapest_gas_station.yml)
3. Data cleaning and data aggregation from JSON to CSV
4. The results are visualized in a streamlit dashboard. 
5. Upon request, a Telegram bot gives me information about which gas station is the cheapest for the specified period.


