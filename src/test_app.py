from fastapi.testclient import TestClient
from syspulse.server import app

client = TestClient(app)

def test_health_endpoint() -> None:
    """Test the health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK", "message": "SysPulse is live!"}

def test_memory_metrics_endpoint() -> None:
    """Test the memory metrics endpoint."""
    response = client.get("/api/metrics/memory")
    assert response.status_code == 200
    data = response.json()
    assert "total_gb" in data
    assert "used_gb" in data
    assert "free_gb" in data
    assert "percent" in data
    assert isinstance(data["percent"], (int, float))

def test_disk_metrics_endpoint() -> None:
    """Test the disk metrics endpoint."""
    response = client.get("/api/metrics/disk")
    assert response.status_code == 200
    data = response.json()
    assert "total_gb" in data
    assert "used_gb" in data
    assert "free_gb" in data
    assert "percent" in data
    assert isinstance(data["percent"], (int, float))

def test_cpu_metrics_endpoint() -> None:
    """Test the CPU metrics endpoint."""
    response = client.get("/api/metrics/cpu")
    assert response.status_code == 200
    data = response.json()
    assert "cpu_percent" in data
    assert isinstance(data["cpu_percent"], (int, float)) 