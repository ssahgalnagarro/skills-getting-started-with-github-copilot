"""
Test suite for the Mergington High School Activities API
"""
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_root_redirect():
    """Test that the root endpoint redirects to the static files"""
    response = client.get("/", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities():
    """Test getting all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data
    
    # Check structure of an activity
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_signup_for_activity():
    """Test signing up for an activity"""
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "test@mergington.edu"}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data
    assert "test@mergington.edu" in data["message"]
    assert "Chess Club" in data["message"]


def test_signup_for_nonexistent_activity():
    """Test signing up for a non-existent activity"""
    response = client.post(
        "/activities/NonExistent Club/signup",
        params={"email": "test@mergington.edu"}
    )
    assert response.status_code == 404
    
    data = response.json()
    assert data["detail"] == "Activity not found"


def test_activities_data_structure():
    """Test that activities have the correct data structure"""
    response = client.get("/activities")
    data = response.json()
    
    for activity_name, activity_data in data.items():
        assert isinstance(activity_name, str)
        assert isinstance(activity_data, dict)
        
        # Check required fields
        required_fields = ["description", "schedule", "max_participants", "participants"]
        for field in required_fields:
            assert field in activity_data, f"Missing field '{field}' in activity '{activity_name}'"
        
        # Check data types
        assert isinstance(activity_data["description"], str)
        assert isinstance(activity_data["schedule"], str)
        assert isinstance(activity_data["max_participants"], int)
        assert isinstance(activity_data["participants"], list)


def test_multiple_signups():
    """Test signing up multiple students for the same activity"""
    # Sign up first student
    response1 = client.post(
        "/activities/Programming Class/signup",
        params={"email": "student1@mergington.edu"}
    )
    assert response1.status_code == 200
    
    # Sign up second student
    response2 = client.post(
        "/activities/Programming Class/signup",
        params={"email": "student2@mergington.edu"}
    )
    assert response2.status_code == 200
    
    # Verify both students are in the activity
    response = client.get("/activities")
    data = response.json()
    participants = data["Programming Class"]["participants"]
    assert "student1@mergington.edu" in participants
    assert "student2@mergington.edu" in participants
