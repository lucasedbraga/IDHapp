import urllib3


class Requester:
    def __init__(self, url: str):
        self.http = urllib3.PoolManager()
        self.urlAPI = url

    def request(self):
        try:
            self.response = self.http.request('GET', self.urlAPI)
            if self.response.status == 200:
                print(f'Leitura realizada, Status: {self.response.status}')
            else:
                print(f'Erro na Leitura, Status: {self.response.status}')
            return self.response

        except Exception as e:
            return print(f'Erro na requisição {e}')


if __name__ == '__main__':
    link = 'https://servicodados.ibge.gov.br/api/v1/projecoes/populacao'
    print(Requester(link).request())
