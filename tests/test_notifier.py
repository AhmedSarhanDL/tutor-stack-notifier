import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_notify_success(async_client: AsyncClient):
    response = await async_client.post("/", json={"message": "Test notification"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "sent"
    assert data["message"] == "Test notification"


async def test_notify_empty_message(async_client: AsyncClient):
    response = await async_client.post("/", json={"message": ""})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "sent"
    assert data["message"] == ""


async def test_notify_validation(async_client: AsyncClient):
    # Test missing message field
    response = await async_client.post("/", json={})
    assert response.status_code == 422

    # Test invalid JSON
    response = await async_client.post("/", content="invalid json")
    assert response.status_code == 422
