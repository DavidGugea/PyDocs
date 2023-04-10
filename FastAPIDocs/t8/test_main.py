from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")

    print("starting test")

    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

    print("test successful")

if __name__ == "__main__":
    test_read_main()
