
from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

# Create your models here.


class MeasureUnit(BaseModel):
    """Model definition for MeauserUnit."""

    description = models.CharField(
        'Description', max_length=60, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for MeauserUnit."""

        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'unidades de medidas'

    def __str__(self):
        """Unicode representation of MeauserUnit."""
        return self.description


class CategoryProduct(BaseModel):

    description = models.CharField(
        'Description', max_length=60, blank=True, null=False, unique=False)

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categorias de Prodcutos'

    def __str__(self):
        """Unicode representation of MeauserUnit."""
        return self.description


class Indicator(BaseModel):
    """Model definition for Indiacdor."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE,
        verbose_name='Indicador de oferta'
    )
    historical = HistoricalRecords()

    class Meta:
        """Meta definition for Indiacdor."""

        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de oferta'

    def __str__(self):
        """Unicode representation of Indicator."""
        return f'Oferta de la categoría {self.category_product} : {self.descount_value}%'


class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField(
        'Nombres de Producto',
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    description = models.TextField(
        'Descripcion del Producto', blank=False, null=False)
    image = models.ImageField(
        'imagen del Producto',
        upload_to='products/',
        blank=True,
        null=True
    )
    measure_unit = models.ForeignKey(
        MeasureUnit,
        on_delete=models.CASCADE,
        verbose_name='unidad de medida',
        null=True
    )
    category_product = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE,
        verbose_name='categoria de producto',
        null=True
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
