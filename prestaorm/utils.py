from lxml import etree, objectify


class classproperty(object):

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


class CustomLookup(etree.CustomElementClassLookup):

    def __init__(self, model):
        from .mixins import Node
        self.node = Node
        self.model = model

    def lookup(self, node_type, document, namespace, name):
        if name == self.model._name_:
            return self.model
        return self.node


def convert_to_model_instances(xml, model):
    children = etree.XML(xml).getchildren()
    if children:
        return [convert_to_model_instance(etree.tostring(item), model)
                for item in children[0].getchildren()]
    return []


def convert_to_model_instance(xml, model, unwrap=False):
    parser = objectify.makeparser()
    parser.set_element_class_lookup(CustomLookup(model))

    obj = objectify.fromstring(xml, parser)
    if unwrap:
        return obj.getchildren()[0]
    return obj
