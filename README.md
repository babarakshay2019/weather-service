## How To Start ?

### Prepare test_assignment

1. Create a virtual environment
2. Activate the virtual environment
3. cd into weather_service
4. Execute the following command: pip install -r requirements.txt
5. update database username password and database name at the settings.
6. Execute the migrations of django follow the command **python manage.py migrate**
7. Execute the command **python manage.py fetch_cities** to fetch all canadian cities at once.
8. Now, run the project: **python manage.py runserver**

  You may also run **docker-compose** up as the application is dockerized.



The application include two API's one for fetching and filter the cities from  list of cities and   

### endpoints


#### 1. fetch and search cities

* URL - http://<hostname>/open-weather-map/
* METHOD - GET
* param - {"name": "ajax"}


#### 2. fetch weather data from latitudes and longitudes.

* URL - http://<hostname>/open-weather-map/weatherdata
* METHOD - GET
* param - {"lat": 123.11, "lon":121.27362}

## NOTE

I have not covered the timezone compatibility as the projects having different air-ports code with different timezones
right now the project will work with UTC timezone for all.