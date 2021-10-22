# miun-web3-mom6-rest
Miun Webbutveckling 3 Moment 6

## Host
https://web3mom6rest.eliaseriksson.eu/

## Running with django development server
The development server is not intended for production use. Instead a proper web server should be used.
This application is hosted at https://web3mom6rest.eliaseriksson.eu/ with NGINX + uWSGI but apache2 + mod_wsgi is another option.
1. Clone this repository with `git clone https://github.com/EliasEriksson/miun-web3-mom6-rest`.
2. navigate into the repository with `cd miun-web3-mom6-rest`.
3. Create a virtual environment with `python3 -m venv venv` (windows: `python -m venv venv`).
4. Activate the virtual environment with `source venv/bin/activate` (windows (cmd): `venv/Scripts/activate.bat`).
5. Install dependencies with `python -m pip install -r requirements.txt`.
6. Navigate to django root with `cd rest_root`.
7. Generate a django secret key 
`python -c "from django.core.management.utils import get_random_secret_key as gen;print(gen())"`.
8. Add the file `rest_root/rest/credentials.json` with the the following content but with your database credentials 
   and your generated django secret key.
   ```json
   {
       "database": {
           "NAME": "you database name",
           "USER": "you database user",
           "PASSWORD": "your database users password",
           "HOST": "your database host address",
           "PORT": "3306"
       },
       "secret_key": "your django secret key"
   }
   ```
9. Change the DEBUG setting from `False` to `True` in `rest_root/rest/settings.py`.
10. From within `rest_root/` create new migrations with `python manage.py makemigrations`.
11. Apply the migrations with `python manage.py migrate`.
12. Run the development server with `python manage.py runserver`

## Available URIs
* `https://web3mom5rest.eliaseriksson.eu/courses/`
  * Supported methods:
    * GET 
    * POST
    * OPTIONS
    * HEAD
* `https://web3mom5rest.eliaseriksson.eu/courses/<courseID>/` 
  * `courseID` is an integer.
  * Supported request methods:
    * GET
    * PUT
    * PATCH
    * DELETE
    * HEAD
    * OPTIONS
* `https://web3mom5rest.eliaseriksson.eu/jobs/`
  * Supported methods:
    * GET 
    * POST
    * OPTIONS
    * HEAD
* `https://web3mom5rest.eliaseriksson.eu/jobs/<jobID>/` 
  * `jobID` is an integer.
  * Supported request methods:
    * GET
    * PUT
    * PATCH
    * DELETE
    * HEAD
    * OPTIONS
* `https://web3mom5rest.eliaseriksson.eu/courses/`
  * Supported methods:
    * GET 
    * POST
    * OPTIONS
    * HEAD
* `https://web3mom5rest.eliaseriksson.eu/webpages/<webpagesID>/` 
  * `webpagesID` is an integer.
  * Supported request methods:
    * GET
    * PUT
    * PATCH
    * DELETE
    * HEAD
    * OPTIONS
