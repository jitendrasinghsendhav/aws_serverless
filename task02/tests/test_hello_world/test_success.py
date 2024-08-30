import json
from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):
   
    def test_success(self):
        event = {'rawPath': '/hello'}
        response = self.HANDLER.handle_request(event, dict())
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['message'], "Hello from Lambda")
