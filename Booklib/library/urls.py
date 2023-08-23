from django.urls.conf import path

from . import views
from .views import detail

urlpatterns = [
    path("<int:book_id>",detail, name='detail'),
]