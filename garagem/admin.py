from django.contrib import admin

from garagem.models import Categoria, Marca, Veiculo, Acessorio, Cor, Modelo

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome', 'nacionalidade')
    list_filter = ('nome',)
    ordering = ('nome', 'nacionalidade')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Acessorio)
class AcessorioAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'modelo', 'cor')
    search_fields = ('descricao', 'modelo__nome', 'marca__nome', 'categoria__descricao', 'cor__descricao', 'acessorio__descricao')
    list_filter = ('acessorio', 'cor','modelo__marca','modelo__categoria', 'modelo__nome' )
    ordering = ('descricao', 'cor', 'acessorio')
    list_per_page = 25