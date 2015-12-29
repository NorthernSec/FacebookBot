import requests
import sys


GOOGLEURL='http://ajax.googleapis.com/ajax/services/search/web'

def google_search(query):
  args = {'q': query,    'v': '1.0',  'start': 0,    'rsz': 8,
          'safe': "off", 'filter': 1, 'hl': 'en'}
  data = requests.get(GOOGLEURL, params=args).json()
  if 'responseStatus' not in data:
    return 'response does not have a responseStatus'
  if data['responseStatus'] != 200:
    return data.get('responseDetails', 'responseStatus is not 200')
  results = []
  if 'results' in data['responseData']:
    for r in data['responseData']['results']:
      results.append( (r['title'], r['content'], r['url']) )
  return results
