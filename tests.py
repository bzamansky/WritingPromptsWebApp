import unittest
from api import initialPrompt
from unittest.mock import patch
import mocks

class TestingApiCalls(unittest.TestCase):
    # def testInitialPrompt(self):
    #     self.assertIsNotNone(api.initialPrompt())

    def testytest(self):
        self.assertEqual(3, 3)

    # def testInputPrompt(self):
    #     self.assertIsNotNone(api.promptFromInput("forests"))

    # @patch('api.openai.Completion.create')
    # def testInitialPrompt(self, mockcreate):
    #     mockcreate.return_value = mocks.mocked_api_data[0]
    #     self.assertEqual(
    #         initialPrompt(), 
    #         mockcreate.return_value['choices'][0]["text"]
    #     )

if __name__ == '__main__':
    unittest.main()