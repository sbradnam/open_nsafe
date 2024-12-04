import os
from streamlit.testing.v1 import AppTest

class TestMain:
    def test_main(self):
        app = AppTest(os.path.join("open_nsafe", "__main__.py"), default_timeout=45).run()
        assert True