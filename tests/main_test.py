import os
from streamlit.testing.v1 import AppTest

class TestMain:
    def test_main(self):
        app = AppTest(os.path.join("app_streamlit.py"), default_timeout=45).run()
        assert True