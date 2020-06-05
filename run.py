from flask import Flask
from config import Config


app = Flask(__name__)

#Configuration
app.config.from_object(Config)

import routes




if __name__ == '__main__':
    app.run(debug=True)