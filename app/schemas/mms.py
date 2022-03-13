from pydantic import BaseModel

from app.schemas.coin import CoinEnum


class MmsSchema(BaseModel):
	pair: CoinEnum
	from_timestamp: int
	to_timestamp: int
	range: int