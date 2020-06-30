# Happy Hiker Service (Python)
Sends you a customized email with information of interest such as the upcoming weather forecast, park features, and trail map.

# Getting Started: 
Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

    cd ~/Desktop/hiker

# Installing:
Create and activate a new Anaconda virtual environment, perhaps named "takeahike-env":
 
    conda create -n takeahike-env python=3.7

    conda activate takeahike-env

Then, from within the virtual environment, install package dependencies:

    pip install -r requirements.txt

Obtain API Keys from the Open Weather and SendGrid services. 

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

   #.env example

    APP_ENV="development" # or set to "production" on Heroku server

    OPEN_WEATHER_API_KEY="___________"
    MY_ZIP="10017"

    SENDGRID_API_KEY="_______________"
    MY_EMAIL_ADDRESS="hello@example.com"

    MY_NAME="Happy Hiker"

IMPORTANT: remember to save the ".env" file :-D

Before committing, add the .env filepath to your ".gitignore" file to ensure it does not get tracked in version control or uploaded to GitHub.

From within the virtual environment, ensure you can run the happy hiker file to select a park, get the weather, and receive an email.
python -m app.happy_hiker # note the module-syntax invocation
 
# Running the tests:
To run, enter:

    python -m app.happy_hiker

A list of parks pulled from the .csv file will generate.  Input your choice of park to retreive its local forecast.  You will then be prompted to input your email address and name.  Once entered into the command line, an email will follow containing your park choice, weather forecast, park features and a downloadable map.

# Happy Hiking!

# Built With:
Python

Anaconda

Visual Studio Code

html

SendGrid

OpenWeather

# Versioning:
GitHub Desktop used for versioning.

For the versions available, see the tags on this repository.

# Authors:
dak529

CZnyu

jkg363

# License:
This project is licensed under the MIT License - see the LICENSE.md file for details

# Acknowledgments:
Code adapted from: prof-rossetti

SOURCE: https://github.com/prof-rossetti/intro-to-python/tree/master/exercises/web-requests

SOURCE: https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/api-client/

# README.md Template from:
SOURCE: README-Template.md https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
