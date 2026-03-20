def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_seeded_activity_data(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in payload
    assert payload[expected_activity]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert payload[expected_activity]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_get_activities_disables_response_caching(client):
    # Arrange
    expected_cache_control = "no-store, no-cache, must-revalidate, max-age=0"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.headers["cache-control"] == expected_cache_control
    assert response.headers["pragma"] == "no-cache"
    assert response.headers["expires"] == "0"