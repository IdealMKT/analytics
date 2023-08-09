from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
import os
import json
import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api-anal.json"


def sample_run_report(property_id):
  client = BetaAnalyticsDataClient()

  request = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[Dimension(name="sessionDefaultChannelGrouping")],
    metrics=[Metric(name="Sessions")],
    date_ranges=[DateRange(start_date="2023-07-01", end_date="2023-07-31")],
  )

  response = client.run_report(request)

  for row in response.rows:
   # if row.dimension_values[0].value == "Sessions":
      print(row.metric_values[0])
      return row.metric_values[0].value


def readObject():

  try:
    with open('v4.json') as json_file:
      data = json.load(json_file)

      csv_file = open('acessos.csv', 'w+', encoding='utf-8')
      csv_file.write('Domínio,Acessos\n')
      for keys in data:
        dominio = keys['Dominio']
        acessos = sample_run_report(keys["ID"])
        # print(f'{dominio},{acessos}\n')
        print(dominio, acessos)
        csv_file.write(f'{dominio},{acessos}\n')
      csv_file.close()
  except AssertionError as e:
    print(e)
    csv_file.write(f'{dominio}," erro "\n')


readObject()