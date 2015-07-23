from __future__ import unicode_literals

from .mixins import BaseModel


class Category(BaseModel):
    _name_ = "category"
    resource = 'categories'


class Product(BaseModel):
    _name_ = "product"
    resource = "products"
    read_only = ['manufacturer_name', 'quantity']

    def set_features(self, features):
        result = {}
        for feature, value in features.iteritems():
            if value:
                product_feature, created = ProductFeature.get_or_create(name=feature, commit=True)
                product_feature_id = product_feature.id.text

                product_feature_value, created = ProductFeatureValue.get_or_create(
                    feature_id=product_feature_id,
                    name=value,
                    commit=True)

                product_feature_value_id = product_feature_value.id.text
                result[product_feature_id] = product_feature_value_id

        return result


class ProductFeature(BaseModel):
    _name_ = "product_feature"
    resource = "product_features"


class ProductFeatureValue(BaseModel):
    _name_ = "product_feature_value"
    resource = "product_feature_values"


class Languages(BaseModel):
    _name_ = "language"
    resource = 'languages'
