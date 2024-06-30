from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserView.as_view(), name="UserView"),
    path('users/<int:id>', views.showUserDetails, name="UserDetails" ),
    path('services/', views.ServiceView.as_view(), name='ServiceView'),
    path('services/<str:type>', views.showServiceDetails, name="ServiceDetails"),
    path('create/', views.createSubscription, name="createSub"),
    path('subscription/', views.SubscriptionCreateView.as_view(), name="SubscriptionPage")
    

]
