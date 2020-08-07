from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newauction", views.newauction, name="newauction"),
    path("view/<str:item_title>", views.view_auction, name="view"),
    path("manwatchlist/<str:item_title>", views.man_watchlist, name='manwatchlist')
]
