from __future__ import unicode_literals

from lxml import objectify

from .mixins import BaseModel


class Category(BaseModel):
    _name_ = "category"
    resource = 'categories'


class Product(BaseModel):
    _name_ = "product"
    resource = "products"
    read_only = ['manufacturer_name', 'quantity']

    def set_features(self, features):
        for feature, value in features.iteritems():
            if value:
                product_feature, created = ProductFeature.objects.get_or_create(name=feature, commit=True)
                product_feature_id = product_feature.id.text

                product_feature_value, created = ProductFeatureValue.objects.get_or_create(
                    id_feature=product_feature_id,
                    value=value,
                    commit=True)

                product_feature_value_id = product_feature_value.id.text

                product_feature_node = objectify.E.product_feature()
                product_feature_node.append(objectify.E.id(product_feature_id))
                product_feature_node.append(objectify.E.id_feature_value(product_feature_value_id))
                self.associations.product_features.append(product_feature_node)


class ProductFeature(BaseModel):
    _name_ = "product_feature"
    resource = "product_features"


class ProductFeatureValue(BaseModel):
    _name_ = "product_feature_value"
    resource = "product_feature_values"


class Languages(BaseModel):
    _name_ = "language"
    resource = 'languages'
