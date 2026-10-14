
import unittest
from unittest.mock import patch, MagicMock

import app


class VillageCareTests(unittest.TestCase):
    def setUp(self):
        self.client = app.app.test_client()

    def test_dashboard_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_assistant_page_loads(self):
        response = self.client.get("/assistant")
        self.assertEqual(response.status_code, 200)

    def test_empty_question_is_rejected(self):
        response = self.client.post(
            "/api/ask",
            json={"question": ""}
        )
        self.assertEqual(response.status_code, 400)

    def test_missing_question_is_rejected(self):
        response = self.client.post("/api/ask", json={})
        self.assertEqual(response.status_code, 400)

    def test_non_json_request_is_rejected(self):
        response = self.client.post(
            "/api/ask",
            data="hello",
            content_type="text/plain"
        )
        self.assertEqual(response.status_code, 415)

    def test_long_question_is_rejected(self):
        response = self.client.post(
            "/api/ask",
            json={"question": "a" * 1001}
        )
        self.assertEqual(response.status_code, 400)

    @patch.dict("os.environ", {"GEMINI_API_KEY": ""})
    def test_missing_api_key_is_handled(self):
        response = self.client.post(
            "/api/ask",
            json={"question": "How can I stay healthy?"}
        )
        self.assertEqual(response.status_code, 503)

    @patch("app.genai.Client")
    def test_successful_ai_response(self, mock_client):
        mock_response = MagicMock()
        mock_response.text = "Drink enough water."

        mock_client.return_value.models.generate_content.return_value = (
            mock_response
        )

        with patch.dict(
            "os.environ",
            {"GEMINI_API_KEY": "test-key"}
        ):
            response = self.client.post(
                "/api/ask",
                json={"question": "How can I stay healthy?"}
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["answer"],
            "Drink enough water."
        )


if __name__ == "__main__":
    unittest.main()
