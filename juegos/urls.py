from django.urls import path, include
from.import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

#creamos un router que se encargara de las rutas de los viewsets
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet) #Registrar el viewset de categorias


urlpatterns= [
    path('index/', views.home, name='home'),
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('detalle_juego/<int:pk>/', views.detalle_juego, name='detalle_juego'),
    path('detalle_categoria/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='juegos/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='juegos/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='juegos/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='juegos/password_reset_complete.html'), name='password_reset_complete'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('carrito/actualizar/<int:producto_id>/', views.actualizar_cantidad_carrito, name='actualizar_cantidad_carrito'),
    path('api/categorias/', views.categorias_api, name='categorias_api'),
    path('api/categorias/int:pk/', views.categorias_api, name='categoria_detalle'),
    path('categorias-juegos/', views.listar_categorias_juegos, name='listar_categorias_juegos'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)), #incluir las rutas del router en la URL base 'api/'
]


