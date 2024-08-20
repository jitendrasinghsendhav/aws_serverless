from tests.test_helloworld import HelloworldLambdaTestCase


class TestSuccess(HelloworldLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)

