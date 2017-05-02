from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.signals import ON_CONNECT


from tests import TESTS

cover = """
def cover(func, in_data):
    return bool(func(in_data))
"""

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            "python": "checkio",
            "js": "housePassword",
        },
        cover_code={
            "python-27": cover,
            "python-3": cover,
            "js-node": cover,
        }
    ).on_ready)
