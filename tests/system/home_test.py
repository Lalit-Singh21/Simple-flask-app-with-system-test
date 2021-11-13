from tests.system.base_test import BaseTest
import json
#flask cant return dictionaries that's why using jsonify to convert string to json
class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/') # get request to our client with endpoint '/'
            self.assertEqual(resp.status_code, 200) #everything is ok
            #json.loads loads string and convert into a valid json representation
            self.assertEqual(json.loads(resp.get_data()),
                             {'message': 'Hello, world!'}, )
