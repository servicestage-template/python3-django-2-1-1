"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from django.urls import path
from django.conf.urls.static import static
from . import helloworld

urlpatterns = [
    path('', helloworld.hello),

    # path('get/', get_example.get_form),
    # path('search/', get_example.get),
    # path('post/', post_example.post),
]

handler404 = helloworld.page_not_found



# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
