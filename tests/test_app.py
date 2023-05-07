from app import app

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Enter your question or prompt:" in response.data

def test_results():
    with app.test_client() as client:
        response = client.post('/results', data={'user_input': 'What is machine learning?'})
        assert response.status_code == 200
        assert b"What is machine learning?" in response.data
