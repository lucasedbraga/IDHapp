import json

from postman import Requester


class DataHandler:
    def __init__(self, url):
        self.response = Requester(url).request()
        self.data = self.json_data()

    def json_data(self):
        try:
            return json.loads(self.response.data.decode('utf-8'))
        except Exception as e:
            print(f'Erro {e}')
if __name__ == '__main__':
    link = 'https://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
    dh = DataHandler(link)
    print(dh.data)
    print(dh.data['horario'])
