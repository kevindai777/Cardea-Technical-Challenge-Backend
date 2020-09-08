# Cardea-Technical-Challenge-Backend

Instructions:
- In the main project directory...
- run "python3 manage.py makemigrations jobs"
- run "python3 manage.py migrate"
- run "python3 manage.py runserver"
- go to "http://localhost:8000/graphql" to see if it is running

Query Parameters:
- Job:
  - id (int)
  - title (str)

- Category:
  - id (int)
  - name (str)
  
- JobCategory:
  - id (int)
  - jobID (int)
  - categoryID (int)
