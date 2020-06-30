Happy Hiker Service (Python)
Sends you a customized email every morning, with information of interest such as the upcoming weather forecast.
Setup
Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:
cd ~/Desktop/hiker
Create and activate a new Anaconda virtual environment, perhaps named "briefings-env":
conda create -n takeahike-env python=3.7
conda activate takeahike-env
Then, from within the virtual environment, install package dependencies:
pip install -r requirements.txt
Obtain API Keys from the Open Weather, and SendGrid services. Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:
# .env example

APP_ENV="development" # or set to "production" on Heroku server

OPEN_WEATHER_API_KEY="___________"
MY_ZIP="10017"

SENDGRID_API_KEY="_______________"
MY_EMAIL_ADDRESS="hello@example.com"

MY_NAME="Jon Snow"
IMPORTANT: remember to save the ".env" file :-D

Before committing, add the .env filepath to your ".gitignore" file to ensure it does not get tracked in version control or uploaded to GitHub.
Usage
From within the virtual environment, ensure you can run the happy hiker file to select a park, get the weather, and receive an email.
python -m app.happy_hiker # note the module-syntax invocation

