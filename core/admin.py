from django.contrib import admin
from .models import (
    ConfiguracaoLoja,
    Produto,
    Depoimento,
    PassoProcesso,
    PassoComoPedir,
    FAQ,
    ItemGaleria
)

admin.site.site_header = "Ateliê Da Fran pra Você - Painel Administrativo"
admin.site.site_title = "Da Fran pra Você"
admin.site.index_title = "Gestão da Loja de Canecas Personalizadas"


@admin.register(ConfiguracaoLoja)
class ConfiguracaoLojaAdmin(admin.ModelAdmin):
    list_display = ('nome_loja', 'whatsapp', 'instagram', 'tempo_producao')

    def has_add_permission(self, request):
        # Permite apenas um registro de configuração
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'preco_antigo', 'tag_destaque', 'em_destaque', 'ativo', 'ordem')
    list_editable = ('preco', 'preco_antigo', 'tag_destaque', 'em_destaque', 'ativo', 'ordem')
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ('nome', 'descricao_curta', 'descricao_completa')
    list_filter = ('em_destaque', 'ativo')


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'produto_comprado', 'estrelas', 'cidade', 'ativo', 'ordem')
    list_editable = ('estrelas', 'ativo', 'ordem')
    search_fields = ('cliente_nome', 'texto', 'produto_comprado')
    list_filter = ('estrelas', 'ativo')


@admin.register(PassoProcesso)
class PassoProcessoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'titulo', 'icone', 'ativo', 'ordem')
    list_editable = ('titulo', 'icone', 'ativo', 'ordem')


@admin.register(PassoComoPedir)
class PassoComoPedirAdmin(admin.ModelAdmin):
    list_display = ('numero', 'titulo', 'icone', 'ativo', 'ordem')
    list_editable = ('titulo', 'ativo', 'ordem')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'ativo', 'ordem')
    list_editable = ('ativo', 'ordem')
    search_fields = ('pergunta', 'resposta')


@admin.register(ItemGaleria)
class ItemGaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'legenda', 'ativo', 'ordem')
    list_editable = ('ativo', 'ordem')
