# URL-Shortener
This is an api built on flask for creating a shortened url of the original url submitted by the user

To run the application, you need to install dependencies first.

Taking a linux environment as a point of reference, first you need to clone this repo.

```
git clone https://github.com/DevTotti/URL-Shortener.git
```

then navigate to the folder

```bash
cd URL-Shortener
```

then you have to setup a vitrual environment

```bash
python3 -m venv env

source env/bin/activate
```

Now that is done, we need to install all dependencies needed for the app

```bash
pip install -r requirements.txt
```

Now we are all set. There is a .env file that contains the credentials, you have to create a new env file or change the ```credentials.env``` to jus ```.env``` and set your credentials.

#Usage
To run the server, by default the server runs on 5000 but you can change it to anything. You can do this by reading the comment in ```app.py``` line 89

When all is set, run the server using

```
python app.py
```

#Routes
NAME     			      | END POINT            |  PARAMS / BODY DATA
------------------------- | -------------        | ---------------
Shorten URL [POST]    	  | /                    |{`url`}
Access original url [GET] | /<short_url>         |<short_url>


I hope you found it easy

Paul


