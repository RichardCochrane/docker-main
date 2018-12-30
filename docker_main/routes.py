def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('api.send_email', '/api/email')
    config.add_route('api.update_reporting', '/api/report/update')
    config.add_route('api.reporting_stats', '/api/report/stats')
