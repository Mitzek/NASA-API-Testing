import requests


class NasaApiTesting:

 def make_request(self, query_parameters: str ):
    """Make a request to fetch content via an NASA Api for a list of Asteroids
        
            API Query Parameters:

            Parameter  | Type       | Default                   | Desc.
            start_date | YYYY-MM-DD | None                      | Starting date for asrteroid search
            end_date   | YYYY-MM-DD | 7 days after start_date   | End date for asrteroid search
            api_key    | string     | DEMO_KEY                  | api.nasa.gov key for expanded usage
    """

    if not isinstance(query_parameters, str): 
        raise TypeError("query paramters must be a string value") # Raising error incase the query parameters are not string
    
    try:

            base_url = "https://api.nasa.gov/neo/rest/v1/feed"
            response = requests.get(f'{base_url}?{query_parameters}')
            return response

    except:
            print("Failed to load URL")


    
