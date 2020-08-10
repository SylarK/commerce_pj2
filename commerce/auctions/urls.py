from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newauction", views.newauction, name="newauction"),
    path("view/<str:item_title>", views.view_auction, name="view"),
    path("manwatchlist/<str:item_title>", views.man_watchlist, name='manwatchlist'),
    path("view_watchlist", views.view_watchlist, name='view_watchlist'),
    path("close/<str:item_title>", views.close, name='close'),
    path("return/<str:item_title>", views.return_home, name='return'),
    path("result", views.result, name='result')
]
