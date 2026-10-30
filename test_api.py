import unittest

from fastapi.testclient import TestClient

from main import app


class ApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        self.addCleanup(self.client.close)

    def test_root(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello from FastAPI!"})

    def test_health(self) -> None:
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_item_id(self) -> None:
        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1})

    def test_invalid_item_id(self) -> None:
        for item_id in ("0", "-1", "abc"):
            with self.subTest(item_id=item_id):
                self.assertEqual(self.client.get(f"/items/{item_id}").status_code, 422)

    def test_item_preview(self) -> None:
        item = {"name": "Notebook", "price": 12.5}
        response = self.client.post("/items", json=item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), item)

    def test_invalid_item(self) -> None:
        for item in ({"name": "", "price": 1}, {"name": "Notebook", "price": -1}, {}):
            with self.subTest(item=item):
                self.assertEqual(self.client.post("/items", json=item).status_code, 422)


if __name__ == "__main__":
    unittest.main()