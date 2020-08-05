from dotenv import load_dotenv
from os import environ 

load_dotenv()

from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    APP_MESSAGE=environ.get("APP_MESSAGE")
)

@app.route('/')
def hello_world():
    text="Flask has a message for you:<br/><b> {}</b>".format(app.config['APP_MESSAGE'])
    return text

if __name__ == '__main__':
    app.run()
