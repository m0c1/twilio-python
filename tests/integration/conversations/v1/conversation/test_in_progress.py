# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class InProgressTestCase(IntegrationTestCase):

    def test_read_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.conversations.v1.conversations \
                                        .in_progress.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Conversations/InProgress',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "conversations": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-05-12T21:08:50Z",
                        "duration": 60,
                        "end_time": "2015-05-12T21:09:50Z",
                        "links": {
                            "participants": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                        },
                        "sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "start_time": "2015-05-12T21:08:50Z",
                        "status": "completed",
                        "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://conversations.twilio.com/v1/Conversations/InProgress?PageSize=50&Page=0",
                    "key": "conversations",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Conversations/InProgress?PageSize=50&Page=0"
                }
            }
            '''
        ))
        
        actual = self.client.conversations.v1.conversations \
                                             .in_progress.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "conversations": [],
                "meta": {
                    "first_page_url": "https://conversations.twilio.com/v1/Conversations/InProgress?PageSize=50&Page=0",
                    "key": "conversations",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Conversations/InProgress?PageSize=50&Page=0"
                }
            }
            '''
        ))
        
        actual = self.client.conversations.v1.conversations \
                                             .in_progress.list()
        
        self.assertIsNotNone(actual)
