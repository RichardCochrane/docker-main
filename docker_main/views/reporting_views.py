import os
import requests

from pyramid.view import view_config


@view_config(route_name='api.reporting_stats', renderer='templates/reports.jinja2')
def reporting_stats_view(request):
    reports_api_url = os.path.join(os.environ['REPORTS_API_URL'], 'api/stats')
    response = requests.get(reports_api_url)

    print 'RESPONSE: {} | {}'.format(response.status_code, response.content)
    return {'stats': response.json()['data']}
