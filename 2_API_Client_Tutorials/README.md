# API
API - Application Programming Interface

Web API
- there exists a DB with data that I cannot (typically access with a sql query)
- instead we have to send a request for data using a url, maybe some authorization headers, maybe some parameters, etc...


# API Client
- In Python, an API Client is a class object that allows us to make requests using Pythonic methods, ex:
    - `data = client.get_data()`


# Steps
- Identify authorization type
- Identify the base url
- Identify different endpoints
    - Identify endpoint parameters
- Read docs for various API Calls
    - Identify exception errors
