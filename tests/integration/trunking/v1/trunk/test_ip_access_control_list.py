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


class IpAccessControlListTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 17 Jul 2015 21:25:15 +0000",
                "date_updated": "Fri, 17 Jul 2015 21:25:15 +0000",
                "friendly_name": "aaaa",
                "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists.create(ip_access_control_list_sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        values = {
            'IpAccessControlListSid': "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 17 Jul 2015 21:25:15 +0000",
                "date_updated": "Fri, 17 Jul 2015 21:25:15 +0000",
                "friendly_name": "aaaa",
                "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists.create(ip_access_control_list_sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertIsNotNone(actual)

    def test_read_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists?PageSize=50&Page=0",
                "ip_access_control_lists": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Fri, 17 Jul 2015 21:25:15 +0000",
                        "date_updated": "Fri, 17 Jul 2015 21:25:15 +0000",
                        "friendly_name": "aaaa",
                        "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "last_page_uri": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists?PageSize=50&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists?PageSize=50&Page=0"
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists?PageSize=50&Page=0",
                "ip_access_control_lists": [],
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "uri": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists?PageSize=50&Page=0"
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists.list()
        
        self.assertIsNotNone(actual)
