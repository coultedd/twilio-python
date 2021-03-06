# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class FormTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.forms(form_type="form-app-push").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://authy.twilio.com/v1/Forms/form-app-push',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "form_type": "form-sms",
                "forms": {
                    "create_factor": {},
                    "verify_factor": {},
                    "create_challenge": {}
                },
                "form_meta": {},
                "url": "https://authy.twilio.com/v1/Forms/form-sms"
            }
            '''
        ))

        actual = self.client.authy.v1.forms(form_type="form-app-push").fetch()

        self.assertIsNotNone(actual)
