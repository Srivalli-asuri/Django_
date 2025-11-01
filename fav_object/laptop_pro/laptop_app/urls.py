from django.urls import path
from . import views
 


urlpatterns=[
    path("create/",view=views.create_user),
    path("get_user/",view=views.get_user),
    path("update_user/",view=views.update_user),
    path("edit_user/<int:id>",view=views.edit_user),
    path("delete_user/<int:id>",view=views.delete_user)
]


