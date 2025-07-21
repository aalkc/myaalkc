"""
Test main application
"""

def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Welcome to Amanat Al-Kalima Company ERP System" in data["message"]


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "aalkc-erp-backend"