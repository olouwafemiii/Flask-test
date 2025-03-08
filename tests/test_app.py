import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
from app.models import User, db
from werkzeug.security import generate_password_hash


@pytest.fixture
def client():
    """A test Client for the app"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        
        hashed_password = generate_password_hash("testpassword")
        test_user = User(email="test@example.com", password_hash=hashed_password)
        db.session.add(test_user)
        db.session.commit()
    
        yield app.test_client()
    
        db.session.remove()
        db.drop_all()

def test_register(client):
    """Test the register route"""
    response = client.post('/auth/register', json={
            "email": "unique@example.com",
            "password": "testpassword"
        })
    assert response.status_code == 201
    assert "email" in response.json
    assert response.json["email"] == "unique@example.com"

def test_login(client):
    """Test the login route"""
    response = client.post('/auth/login', json={
            "email": "test@example.com",
            "password": "testpassword"
        })
    assert response.status_code == 200
    assert "token" in response.json
