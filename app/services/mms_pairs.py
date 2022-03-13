from app.schemas.mms import MmsSchema
from app.utils.mongodb import mms_collection


class MmsPairsService:

    @staticmethod
    def get_mms(params: MmsSchema):

        """
        This function represents a class that is used to query a database
        :param params: MmsSchema
        :return:
        example: [{
            "pair": "BRLBTC",
            "mms": 121212.121
        }]
        """

        result = []

        mms_pairs = mms_collection.find(
            {"timestamp": {"$gt": params.from_timestamp, "$lt": params.to_timestamp}},
            {"pair": params.pair.value, f'mms_{ params.range }': True}
        ).limit(params.range)

        for mms_pair in mms_pairs:
            result.append({
                "pair": mms_pair.get("pair"),
                "mms": mms_pair.get(f'mms_{params.range}')
            })

        return result