from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Proveedor/', views.proveedoresView, name='proveedor'),
    url(r'^Proveedor/Guardar', views.CrearProveedor.as_view(), name='crear'),
    url(r'^Proveedor/Actualizar', views.ActualizarProveedor.as_view(), name='actualizar'),
    url(r'^Proveedor/Consultar/(?P<nit>[\w\-]+)/$', views.ConsultarProveedor.as_view(), name='consultar'),
    url(r'^Proveedor/Eliminar/(?P<nit>[\w\-]+)$', views.EliminarProveedor.as_view(), name='eliminar'),
    url(r'^Proveedor/Listar', views.ListarProveedores.as_view(), name='listar'),
]
