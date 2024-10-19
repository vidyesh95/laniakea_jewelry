"""
URL configuration for flipkartproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from app.views import ProductRegister, ProductUpdate, ProductDelete

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("userlogout/", views.userlogout, name="userlogout"),
    path("earringslist/", views.earringslist, name="earringslist"),
    path("cocktailringlist/", views.cocktailringlist, name="cocktailringlist"),
    path("necklacelist/", views.necklacelist, name="necklacelist"),
    path("banglelist/", views.banglelist, name="banglelist"),
    path("mangalsutralist/", views.mangalsutralist, name="mangalsutralist"),
    path("chainlist/", views.chainlist, name="chainlist"),
    path("engagementringlist/", views.engagementringlist, name="engagementringlist"),
    path("braceletlist/", views.braceletlist, name="braceletlist"),
    path("elfearcuffslist/", views.elfearcuffslist, name="elfearcuffslist"),
    path("weddingringslist/", views.weddingringslist, name="weddingringslist"),
    path("ankletslist/", views.ankletslist, name="ankletslist"),
    path("broochlist/", views.broochlist, name="broochlist"),
    path("solitaireringlist/", views.solitaireringlist, name="solitaireringlist"),
    path("toeringlist/", views.toeringlist, name="toeringlist"),
    path("medallionlist/", views.medallionlist, name="medallionlist"),
    path("hairpinlist/", views.hairpinlist, name="hairpinlist"),
    path("searchproduct/", views.searchproduct, name="searchproduct"),
    path(
        "request_password_reset/",
        views.request_password_reset,
        name="request_password_reset",
    ),
    path("reset_password/<username>/", views.reset_password, name="reset_password"),
    path("showpricerange/", views.showpricerange, name="showpricerange"),
    path("sortingbyprice/", views.sortingbyprice, name="sortingbyprice"),
    path("showcarts/", views.showcarts, name="showcarts"),
    path("addtocart/<int:productid>", views.addtocart, name="addtocart"),
    path("removecart/<int:productid>", views.removecart, name="removecart"),
    path("updateqty/<int:qv>/<int:productid>", views.updateqty, name="updateqty"),
    path("addaddress/", views.addaddress, name="addaddress"),
    path("showaddress/", views.showaddress, name="showaddress"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("make_payment/", views.make_payment, name="make_payment"),
    path("showorders/", views.showorders, name="showorders"),
    path("ProductRegister/", ProductRegister.as_view(), name="ProductRegister"),
    path("ProductList/", views.ProductList, name="ProductList"),
    path("ProductUpdate/<int:pk>", ProductUpdate.as_view(), name="ProductUpdate"),
    path("ProductDelete/<int:pk>", ProductDelete.as_view(), name="ProductDelete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
