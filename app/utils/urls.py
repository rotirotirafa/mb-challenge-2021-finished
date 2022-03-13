from flask_restful import Api

from app.resources.health_check import HealthCheck
from app.resources.mms import Mms
from app.settings import BASE_PATH


def build_urls(app):
    """
    This function is responsible to build urls for flask using resources from flask_restful
    :param app:
    :return: app
    """

    api = Api()

    api.add_resource(HealthCheck, f'/{BASE_PATH}/health-check')
    api.add_resource(Mms, f'/{BASE_PATH}/<string:pair>/mms')

    return api.init_app(app)
