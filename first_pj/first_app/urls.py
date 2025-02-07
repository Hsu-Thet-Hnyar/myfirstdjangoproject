from django.urls import path
from first_app.views import first,second,third,fourth,fifth


urlpatterns = [
    path('A/', first ,name="Hello"),
    path('B/', second ,name="Home"),
    path('C/', third ,name="Toys for girls"),
    path('D/', fourth ,name="Toys for boys"),
    path('E/', fifth ,name="Contact"),

]