from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
import requests
import json

token = "ya29.a0AeTM1ifZ43kezmqE2Z7wP6tk0oprm6Ivxu4pibyDF0tOHRv1MEXElOyev_56LHBd1VRuEgzHQ2FHgCkHDQ6EXAlEI-KVXuCyYQvtfvGvROe-5xK0CLnGyO0eLi2--rI0pbuKdZytiVIWI2QFnbNDfVTq3qzTzJEaCgYKASYSARASFQHWtWOmnX3TlS-hi-yxB8jVi_2bFA0166"


def readObject():
  with open('v3.json') as json_file:
    data = json.load(json_file)

    csv_file = open('acessosv3.csv', 'w+', encoding='utf-8')
    csv_file.write('Domínio,Acessos\n')
    for keys in data:
      dominio = keys['Dominio']
      acessos = createUrl(token, keys['ID'], "Sessions", "2023-01-01",
                          "2023-01-31")
      csv_file.write(f'{dominio},{acessos}\n')
      print(acessos)
    csv_file.close()


def createUrl(token, ids, metrics, startDate, endDate):
  try:
    url = f"https://www.googleapis.com/analytics/v3/data/ga?access_token={token}&ids=ga%3A{ids}&metrics=ga%3A{metrics}&start-date={startDate}&end-date={endDate}"
    # return url
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers,
                                data=payload).json()

    for row in response['rows']:
      return row[0]
  except:
    return 0


readObject()
