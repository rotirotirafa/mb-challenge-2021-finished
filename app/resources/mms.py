from flask_restful import Resource, request

from app.exceptions import TimeRangeIsNotValid, PairNotAllowed
from app.schemas.mms import MmsSchema
from app.services.mms_pairs import MmsPairsService
from app.settings import ALLOWED_PAIRS
from app.utils import verify_if_timestamp_is_more_than_year


class Mms(Resource):
    """
    Get Mms from Pairs.
    parameters:
      - in: body
        from: integer
        to: integer
        range: integer
      - in: path
        pair: str
    responses:
      200:
        description: Success
        body:
            [{
            timestamp: int
            mms: float
        },...],
      400:
        description: Error
    """

    methods = ['GET']

    mms_pairs_service = MmsPairsService()

    @staticmethod
    def request_params_to_dict():
        return request.args.to_dict()

    @staticmethod
    def response_error(message, error_code):
        return {'message': str(message)}, error_code

    @classmethod
    def get(cls, pair: str):
        try:
            if pair in ALLOWED_PAIRS:
                params = cls.request_params_to_dict()

                verify_if_timestamp_is_more_than_year(int(params.get('from')))

                mms_query_schema = MmsSchema(
                    pair=pair,
                    from_timestamp=params.get('from'),
                    to_timestamp=params.get('to'),
                    range=params.get('range')
                )

                mms_response = MmsPairsService().get_mms(mms_query_schema)

                return mms_response, 200
            raise PairNotAllowed('This Pair not Allowed', 'Pair not Allowed')

        except TimeRangeIsNotValid as message:
            return cls.response_error(message, error_code=400)

        except PairNotAllowed as message:
            return cls.response_error(message, error_code=400)

        except Exception as ex:
            return cls.response_error(ex, error_code=400)