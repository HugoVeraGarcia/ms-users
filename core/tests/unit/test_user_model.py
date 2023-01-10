import pytest
from core.models import User

@pytest.mark.django_db
def test_user_create():
    
    USERNAME = 'Test User'
    EMAIL = 'test@test.com'
    PASSWORD = 'test'

    user = User.objects.create(
        name = USERNAME,
        email = EMAIL,
        password= PASSWORD
    )

    assert user.id == 1
