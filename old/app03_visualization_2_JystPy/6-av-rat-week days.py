import justpy as jp
import pandas
from datetime import datetime
from pytz import utc 
import matplotlib.pyplot as plt

data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_average = data.groupby(['Weekday']).mean().reindex(cats) 

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },
  subtitle: {
    text: 'Average rating by week subtitle'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Date'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average ratings'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Average rating',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analisys of Course Reviews', classes='text-h3 text-center q-pa-md text-red', v_ripple={'center': True, 'color': 'orange-5'})
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analisys')
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = 'Average rating by week'

    hc.options.xAxis.categories = list(weekday_average.index)
    hc.options.series[0].data = list(weekday_average['Rating'])

    return wp

jp.justpy(app)
