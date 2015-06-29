from __future__ import unicode_literals

from .mixins import BaseModel


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
