from app import app

def client():
    return app.test_client()

def test_home_renders_math():
    response = client().get("/")
    assert response.status_code == 200
    assert b"5" in response.data

def test_add_route_computes_sum():
    response = client().get("/add/7/5")
    assert response.status_code == 200
    assert b"12" in response.data

def test_subtract_route_computes_difference():
    response = client().get("/subtract/9/4")
    assert response.status_code == 200
    assert b"5" in response.data

def test_multiply_route_computes_product():
    response = client().get("/multiply/6/7")
    assert response.status_code == 200
    assert b"42" in response.data