from __future__ import unicode_literals

from django.db import models

from .mixins import BaseModel


class PsAttachment(models.Model):
    id_attachment = models.IntegerField(primary_key=True)
    file = models.CharField(max_length=40)
    file_name = models.CharField(max_length=128)
    file_size = models.BigIntegerField()
    mime = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'ps_attachment'


class PsAttachmentLang(models.Model):
    id_attachment = models.IntegerField(primary_key=True)
    id_lang = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'ps_attachment_lang'


class PsProductAttachment(models.Model):
    id_product = models.IntegerField(primary_key=True)
    id_attachment = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ps_product_attachment'


class PsProduct(models.Model):
    id_product = models.IntegerField(primary_key=True)
    id_supplier = models.IntegerField(blank=True, null=True)
    id_manufacturer = models.IntegerField(blank=True, null=True)
    id_category_default = models.IntegerField(blank=True, null=True)
    id_shop_default = models.IntegerField()
    id_tax_rules_group = models.IntegerField()
    on_sale = models.IntegerField()
    online_only = models.IntegerField()
    ean13 = models.CharField(max_length=13, blank=True)
    upc = models.CharField(max_length=12, blank=True)
    ecotax = models.DecimalField(max_digits=17, decimal_places=6)
    quantity = models.IntegerField()
    minimal_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=6)
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=6)
    unity = models.CharField(max_length=255, blank=True)
    unit_price_ratio = models.DecimalField(max_digits=20, decimal_places=6)
    additional_shipping_cost = models.DecimalField(max_digits=20, decimal_places=2)
    reference = models.CharField(max_length=32, blank=True)
    supplier_reference = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=64, blank=True)
    width = models.DecimalField(max_digits=20, decimal_places=6)
    height = models.DecimalField(max_digits=20, decimal_places=6)
    depth = models.DecimalField(max_digits=20, decimal_places=6)
    weight = models.DecimalField(max_digits=20, decimal_places=6)
    out_of_stock = models.IntegerField()
    quantity_discount = models.IntegerField(blank=True, null=True)
    customizable = models.IntegerField()
    uploadable_files = models.IntegerField()
    text_fields = models.IntegerField()
    active = models.IntegerField()
    redirect_type = models.CharField(max_length=3)
    id_product_redirected = models.IntegerField()
    available_for_order = models.IntegerField()
    available_date = models.DateField()
    condition = models.CharField(max_length=11)
    show_price = models.IntegerField()
    indexed = models.IntegerField()
    visibility = models.CharField(max_length=7)
    cache_is_pack = models.IntegerField()
    cache_has_attachments = models.IntegerField()
    is_virtual = models.IntegerField()
    cache_default_attribute = models.IntegerField(blank=True, null=True)
    date_add = models.DateTimeField()
    date_upd = models.DateTimeField()
    advanced_stock_management = models.IntegerField()
    pack_stock_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ps_product'


class Category(BaseModel):
    _name_ = "category"
    resource = 'categories'


class Product(BaseModel):
    _name_ = "product"
    resource = "products"
    read_only = ['manufacturer_name', 'quantity']


class ProductFeature(BaseModel):
    _name_ = "product_feature"
    resource = "product_features"


class ProductFeatureValue(BaseModel):
    _name_ = "product_feature_value"
    resource = "product_feature_values"


class Languages(BaseModel):
    _name_ = "language"
    resource = 'languages'
