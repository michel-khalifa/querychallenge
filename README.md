# **Query Challenge**
This API provides auto-complete suggestions for a list of cities. The search string is passed as in path string parameter. The endpoint returns a JSON response with an array of suggested matches.

## **Features**
* This REST service using the Connexion Python library
* Connexion is a framework on top of Flask to automatically handle the REST API requests based on Swagger 2.0 Specification files in YAML.
* Mapping of REST operations to Python functions (using the operationId in swagger.yml)
* Bundled Swagger UI (served on /ui/ path)
* Using sqlite for data storage
* Using swagger_tester and unittest for unit testing

## **Files**
* **swagger.yml**: REST API Swagger definition
* **app.py**: Main app file which read the swagger file and start the API endpoint
* **cities.py**: Handles cities suggestions function 
* **cities.db**: DB file that serves data to the REST API service
* **unitTest.py**: Unity test for the REST API service
