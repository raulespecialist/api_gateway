# Resume
We have at least 6 different types of data: email, phone
number, device, geolocation, and user data.
The challenge, if you accept it, is to design and prototype a simple API that
receives a request and enriches and aggregates the data in order to serve the
enriched data back to the user.
Data is as follows, 6 independent data sources with data ready to be enriched
based on different keys:
“email”, “phone_number”, “devices”, “geolocation”, “user_data”
When expecting a request we expect different keys that will be enriched
depending on the initial key

Propose an architecture to build the different services and logic from the API
Gateway to compile the response based on the requested data and matches with
the database. Propose it using API best practices, technology stack, proposed
data model and different endpoints, to get, upload, update and delete data from
the different services. Be sure to justify a low latency response.

# User story
### consultation service
We have at least 6 different types of data: email, phone
number, device, geolocation, and user data.
The challenge, if you accept it, is to design and prototype a simple API that
receives a request and enriches and aggregates the data in order to serve the
enriched data back to the user.
Data is as follows, 6 independent data sources with data ready to be enriched
based on different keys:
“email”, “phone_number”, “devices”, “geolocation”, “user_data”


When expecting a request we expect different keys that will be enriched
depending on the initial key


# Implementation

#### Clonar
 

    git clone https://github.com/raulespecialist/api_gateway.git
Enter in the directory

    cd api_gateway

Make a virtual env

    python -m venv .env 

Enter in the virtual env

    source .env/bin/activate

Inside the virtual environment (.env) update pip

    pip install --upgrade pip

Then install all the necessary requirements

    pip install -r requirements.txt

Start the API REST in port 8001

    python manage.py runserver 127.0.0.1:8000


Example of Request in cURL


    curl --location --request POST 'http://127.0.0.1:8000/users/' \
    
    --form 'user_email="meloadik@gmail.com"' \
    
    --form 'user_phone_number=" 8117904544"' \
    
    --form 'lat="20.97500"' \
    
    --form 'lng="89.61414"' \
    
    --form 'user_address="rfm mz5 lt4"'
