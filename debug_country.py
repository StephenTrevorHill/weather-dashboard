from app import app

with app.test_client() as client:
    res = client.get('/api/countries')
    print(res.status_code)
    print(res.get_json())
