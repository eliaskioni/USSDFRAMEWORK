"""
This test initial screen
"""
from ussdframework.tests import UssdTestCase


class TestInitialHandler(UssdTestCase.BaseUssdTestCase):
    validation_error_message = {
        'initial_screen': {
            'next_screen': {"next_screen": ['invalid_screen is missing in ussdframework journey']},
            'variables': {'file': ['This field is required.'],
                          'namespace': ['This field is required.']},
            'ussd_report_session': {
                "session_key": ['This field is required.'],
                'validate_response': ['This field is required.'],
                'request_conf': ['This field is required.'],
            }
        }
    }
