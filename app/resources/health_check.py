from flask_restful import Resource


class HealthCheck(Resource):

    @classmethod
    def get(cls):
        """
        Get method to simply check if the api is up
        :return:
        """
        return 'im Alive', 200
