import pytest
from Nasa_Api_Testing import NasaApiTesting

api_testing = NasaApiTesting()


#Declaring variables in global scope to avoid repitition.
api_key = "api_key=DEMO_KEY"
start_date = "2015-09-07"
end_date = "2015-09-08"

#API Url structure: "base_url/start_date&end_date&api_key"

def test_fetch_api_with_invalid_type():
     """Testing API response other types other than string"""    
     with pytest.raises(TypeError):
          api_testing.make_request(1)   
     with pytest.raises(TypeError):
          api_testing.make_request(True)
     with pytest.raises(TypeError):   
          api_testing.make_request(2.0)   
     with pytest.raises(TypeError):
          api_testing.make_request([])
     with pytest.raises(TypeError):
          api_testing.make_request({})
     with pytest.raises(TypeError):
          response = api_testing.make_request(None)
     with pytest.raises(TypeError):
          response = api_testing.make_request()

def test_fetch_api_without_query_parameters():
     """Testing API response without API Key and other parameters"""
     api_key = "" # Value changed to fit the scope of function
     response = api_testing.make_request(api_key)
     assert response.status_code == 403 # Status code 403 = Invalid URL

def test_with_invalid_api_key():
    """Testing API response with invalid API Key"""
    api_key = "api_key=RANDOM_VALUE" # Value Changed to fit the scope of function
    response = api_testing.make_request(api_key)
    assert response.status_code == 403

def test_fetch_api_with_only_api():
    """Testing API response with only API key """      
    response = api_testing.make_request(api_key)
    assert response.status_code == 200 # Status code 200 = OK


def test_with_only_start_date_with_api_key():
     "Testing API response with start date only with API Key"
     response = api_testing.make_request(f'{start_date}&{api_key}')
     assert response.status_code == 200

def test_with_only_start_date_without_api_key():
     "Testing API response with start date only without API Key"
     response = api_testing.make_request(f'{start_date}')
     assert response.status_code == 403

def test_with_only_end_date_with_api_key():
     "Testing API response with end date only with API Key" 
     response = api_testing.make_request(f'{end_date}&{api_key}')
     assert response.status_code == 200

def test_with_only_end_date_without_api_key():
     "Testing API response with end date only without API Key"
     response = api_testing.make_request(f'{end_date}')
     assert response.status_code == 403

def test_with_invalid_date_format():
     "Testing API response invalid date format"
     start_date = "2015/09/07" # Value Changed to fit the scope of function
     end_date = "2015/09/08" # Value Changed to fit the scope of function
     response = api_testing.make_request(f'{start_date}&{end_date}&{api_key}')
     assert response.status_code == 403


def test_with_start_and_end_date():
     "Testing API response with start and end date with API Key"
     response = api_testing.make_request(f'{start_date}&{end_date}&{api_key}')
     assert response.status_code == 200

def test_with_start_and_end_date():
     "Testing API response with start and end date without API Key"
     
     response = api_testing.make_request(f'{start_date}&{end_date}')
     assert response.status_code == 403

def test_with_fetching_content():
     """Testing API for fetching content"""
     response = api_testing.make_request(f'{start_date}&{end_date}&{api_key}')
     data = response.json()
     assert len(data) > 0
     assert data['element_count'] > 0




     


    