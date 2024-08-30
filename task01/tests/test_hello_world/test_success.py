from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    # def test_success(self):
    #     self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)

    def test_success(self):
        response = self.HANDLER.handle_request(dict(), dict())
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['message'], "Hello from Lambda")

