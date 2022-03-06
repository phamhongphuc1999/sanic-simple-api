class ServiceType:
    USER = "user"


class EnvironmentType:
    PRODUCTION = "production"
    DEVELOPMENT = "development"


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - (%(name)s)[%(levelname)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'access': {
            'format': '%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: ' +
                      '%(request)s %(message)s %(status)d %(byte)d',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
}
