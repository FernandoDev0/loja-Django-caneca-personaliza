from django.db import models


class ConfiguracaoLoja(models.Model):
    nome_loja = models.CharField(max_length=100, default="Da Fran pra Você ☕")
    slogan = models.CharField(max_length=200, default="Canecas personalizadas feitas à mão, com amor e história")
    whatsapp = models.CharField(max_length=20, default="5517999999999", help_text="Formato: 55 + DDD + Número")
    instagram = models.CharField(max_length=50, default="@dafranpravoce")
    aviso_topo = models.CharField(
        max_length=255, 
        default="Envio para todo o Brasil 🇧🇷 • Feito à mão com carinho • Garantia contra quebra 📦"
    )
    garantia_texto = models.CharField(
        max_length=255, 
        default="Garantia da Fran: se chegar quebrada, eu mando outra imediatamente. Sem burocracia."
    )
    tempo_producao = models.CharField(max_length=100, default="Até 3 dias úteis após aprovação da arte")
    banner_cta_titulo = models.CharField(max_length=150, default="Bora criar a sua? 💖")
    banner_cta_subtitulo = models.TextField(
        default="Me chama no WhatsApp que a gente cria juntas a caneca dos seus sonhos com arte exclusiva!"
    )
    sobre_fran = models.TextField(
        default="Oi, eu sou a Fran! E eu transformo um simples café num presente inesquecível. Cada caneca é estampada à mão no meu ateliê, cuidando de cada tom e detalhe como se fosse pra mim."
    )

    class Meta:
        verbose_name = "Configuração da Loja"
        verbose_name_plural = "Configuração da Loja"

    def __str__(self):
        return self.nome_loja

    def get_whatsapp_url(self, texto=""):
        import urllib.parse
        msg = texto or f"Olá, {self.nome_loja}! Quero pedir minha caneca personalizada 💕"
        return f"https://wa.me/{self.whatsapp}?text={urllib.parse.quote(msg)}"


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    tag_destaque = models.CharField(max_length=50, blank=True, help_text="Ex: A mais pedida 💕, Presente perfeito")
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    preco_antigo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    descricao_curta = models.CharField(max_length=255)
    descricao_completa = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="produtos/", blank=True, null=True)
    imagem_fallback = models.CharField(max_length=255, default="images/canecas_trio.webp")
    foco_imagem = models.CharField(max_length=50, default="center")
    caracteristicas = models.TextField(
        blank=True, 
        help_text="Uma por linha (ex: Cerâmica resinada AAA+, Capacidade 325ml, Pode ir ao micro-ondas)"
    )
    em_destaque = models.BooleanField(default=True)
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["ordem", "id"]

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"

    @property
    def lista_caracteristicas(self):
        if self.caracteristicas:
            return [c.strip() for c in self.caracteristicas.split("\n") if c.strip()]
        return [
            "Cerâmica resinada Premium AAA+",
            "Capacidade de 325ml",
            "Pode ir ao micro-ondas e lava-louças",
            "Estampa fotográfica que não desbota",
            "Embalada em caixa especial de presente",
        ]

    def get_whatsapp_msg(self):
        import urllib.parse
        msg = f"Olá, Fran! Quero pedir a {self.nome} (R$ {self.preco:.2f}) 💖"
        return urllib.parse.quote(msg)


class Depoimento(models.Model):
    cliente_nome = models.CharField(max_length=100)
    produto_comprado = models.CharField(max_length=100, default="Caneca com Foto")
    cidade = models.CharField(max_length=100, blank=True, default="Cliente Verificada")
    texto = models.TextField()
    estrelas = models.PositiveSmallIntegerField(default=5)
    foto = models.ImageField(upload_to="depoimentos/", blank=True, null=True)
    imagem_fallback = models.CharField(max_length=255, blank=True)
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"
        ordering = ["ordem", "id"]

    def __str__(self):
        return f"{self.cliente_nome} ({self.produto_comprado})"


class PassoProcesso(models.Model):
    numero = models.PositiveIntegerField(default=1)
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, default="coffee", help_text="coffee, sparkles, printer, gift, truck")
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Passo do Ateliê"
        verbose_name_plural = "Passos do Ateliê"
        ordering = ["ordem", "numero"]

    def __str__(self):
        return f"{self.numero}. {self.titulo}"


class PassoComoPedir(models.Model):
    numero = models.PositiveIntegerField()
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, default="whatsapp")
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Como Pedir (Passo)"
        verbose_name_plural = "Como Pedir (Passos)"
        ordering = ["numero"]

    def __str__(self):
        return f"Passo {self.numero}: {self.titulo}"


class FAQ(models.Model):
    pergunta = models.CharField(max_length=255)
    resposta = models.TextField()
    icone = models.CharField(max_length=50, default="help-circle")
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Pergunta Frequente"
        verbose_name_plural = "Perguntas Frequentes (FAQ)"
        ordering = ["ordem", "id"]

    def __str__(self):
        return self.pergunta


class ItemGaleria(models.Model):
    titulo = models.CharField(max_length=120)
    legenda = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to="galeria/", blank=True, null=True)
    imagem_fallback = models.CharField(max_length=255, default="images/cliente_cozinha.webp")
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Item da Galeria"
        verbose_name_plural = "Galeria de Clientes"
        ordering = ["ordem", "id"]

    def __str__(self):
        return self.titulo
