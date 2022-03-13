from app.seed import transform_timestamp_now, format_timestamp_days


def test_transform_timestamp_now():
    assert transform_timestamp_now(), int


def test_format_timestamp_days():
    assert format_timestamp_days(1), int

#TODO testar api


