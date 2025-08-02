from app import app

with app.test_client() as client:
    res = client.get('/api/cities?country=Canada')
    print(res.status_code)
    print(res.get_json())
