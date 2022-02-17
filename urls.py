from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/", views.list_of_item, name="list"),
    path("listing/<int:listing_id>", views.listing, name="item"),
    path("create/",views.create_listing,name="create"),
    path("category/", views.category, name="category"),
    path("category/<int:category_id>", views.show_category, name="listcategory"),
    path("comment/<int:listing_id>", views.add_comm, name="addcomment"),
    path("watchlist/", views.watch_list, name="watchlist"),
    path("addwish/<int:listing_id>", views.add_wish, name="addwish"),
    path("wishlist/<int:listing_id>", views.wish, name="wishl"),
    path("removewish/<int:listing_id>", views.remove_wish, name="remove_wish"),
    path("bid/<int:listing_id>", views.bid, name="addbid"),
    path("sell/<int:listing_id>", views.sell, name="sell")
]
