import datetime
import os
import requests

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config


@view_config(route_name='api.send_email')
def send_email_view(request):
    mail_api_url = os.path.join(os.environ['MAIL_API_URL'], 'api/create')

    data = {
        'recipient_address': 'info@docker.co.za',
        'sender_address': request.GET['email_address'],
        'subject': request.GET['subject'],
        'body': request.GET['body']
    }
    response = requests.get(mail_api_url, json=data)
    print 'RESPONSE: {} | {}'.format(response.status_code, response.content)
    return HTTPFound(request.route_path('home'))


@view_config(route_name='api.update_reporting')
def update_reporting_view(request):
    reports_api_url = os.path.join(os.environ['REPORTS_API_URL'], 'api/update')
    data = {
        'created_at': datetime.datetime.now().isoformat(),
        'subject': request.GET['subject']
    }

    response = requests.get(reports_api_url, json=data)

    print 'RESPONSE: {} | {}'.format(response.status_code, response.content)
    return HTTPFound(request.route_path('home'))
