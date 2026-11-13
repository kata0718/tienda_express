from django.contrib import admin
from .models import Categoria, Producto


class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 1


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo_clasificacion', 'activa', 'total_productos_asociados']
    search_fields = ['nombre', 'codigo_clasificacion']
    list_filter = ['activa', 'codigo_clasificacion']
    inlines = [ProductoInline]

    @admin.display(description='Total Productos')
    def total_productos_asociados(self, obj):
        return obj.productos.count()


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo_sku', 'nombre', 'marca', 'categoria', 'precio', 'stock', 'disponible']
    search_fields = ['codigo_sku', 'nombre', 'marca',
                     'categoria__nombre', 'categoria__codigo_clasificacion']
    list_filter = ['disponible', 'categoria', 'categoria__codigo_clasificacion', 'fecha_ingreso']
    list_editable = ['disponible']
    actions = ['marcar_disponible', 'marcar_agotado']

    @admin.action(description='Marcar productos como disponibles')
    def marcar_disponible(self, request, queryset):
        n = queryset.update(disponible=True)
        self.message_user(request, f'{n} producto(s) marcado(s) como disponible.')

    @admin.action(description='Marcar productos como agotados')
    def marcar_agotado(self, request, queryset):
        n = queryset.update(disponible=False)
        self.message_user(request, f'{n} producto(s) marcado(s) como agotado.')