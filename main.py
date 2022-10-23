import requests
from flask import Flask

app = Flask(__name__)


class APIService:
    def __init__(self, ipAdress):
        self.mainUrl = f'http://${ipAdress}:30120'
        self.playersUrl = f'${self.mainUrl}/players.json'
        self.players_data = []
        self.info_data = []

    def connectToAPI(self):
        self.players_data = requests.get(self.playersUrl).json()
        self.info_data = requests.get(self.playersUrl).json()


@app.route('/myfivemserver/<serverip>')
def myfivemserver(serverip):
    apiservice = APIService(serverip)

    return '<code>' \
           f'${apiservice.info_data}' \
           f'${apiservice.players_data}' \
           '</code>'


if __name__ == "__main__":
    app.run()
