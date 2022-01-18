def init_zip_configuration_in_(app_config):
    app_config['zip'] = {}
    app_config['zip'].update(
        {'name': 'zip',
         'config': {}
         })
    return app_config
