import os
import requests

urls = {
    'green_tripdata_2021-01.parquet':'https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2021-01.parquet',
    'green_tripdata_2021-02.parquet':'https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2021-02.parquet',
    'green_tripdata_2021-03.parquet':'https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2021-03.parquet',
}

os.makedirs('data')

for filename, url in urls.items(): 
    r = requests.get(url, allow_redirects=True)

    open(os.path.join('data', filename), 'wb').write(r.content)