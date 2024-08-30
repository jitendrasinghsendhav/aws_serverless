from tests.test_helloworld import HelloworldLambdaTestCase


class TestSuccess(HelloworldLambdaTestCase):
    def test_success(self):
        expected_response = {
            "statusCode": 200,
            "body": "hello from lambda"
        }
        actual_response = self.HANDLER.handle_request(dict(), dict())
        self.assertEqual(actual_response, expected_response)
