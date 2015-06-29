import copy

from lxml import etree, objectify

from .mixins import Node
from .utils import classproperty

# class PsBase(MixinRepr):

#     def append(self, _name, _value=None, **kwargs):
#         node = PsNode(_name, _value, **kwargs)
#         self._xml.append(node._xml)
#         return self

#     def delete(self, tag):
#         self._xml.delete(tag)
#         return self

#     def __getattr__(self, name):
#         if name not in ['_xml', 'read_only']:
#             xml = self._xml.__getattr__(name)
#             return PsObject(xml, xml=True)
#         return super(PsBase, self).__getattr__(name)

#     def __setattr__(self, name, value):
#         if name not in ['_xml']:
#             root = self._xml.__getattr__(name)
#             if type(value) is list:
#                 for item in root.getchildren():
#                     root.remove(item)

#                 for item in value:
#                     root.append(item._xml)
#             else:

#                 if len(root.findall('language')) > 0:
#                     value = self._language(root, value)
#                 return self._xml.__setattr__(name, value)

#         return super(PsBase, self).__setattr__(name, value)


# class PsNode(PsBase):

#     def __init__(self, _name, _value=None, **kwargs):
#         self._xml = etree.Element(_name)

#         for k, v in kwargs.items():
#             self._xml.attrib[k] = v

#         if _value is not None:
#             self._xml.text = u"%s" % _value


# class PsObject(PsBase):
#     languages_ids = [1, 4, 5]
#     _model = None

#     def __init__(self, data, xml=False, model=None):
#         self._xml = None
#         if model:
#             self._model = model

#         if xml:
#             self._xml = data
#         else:
#             try:
#                 self._xml = objectify.fromstring(data)
#             except etree.XMLSyntaxError:
#                 print " **** Error **** "
#                 print data

#     def _language(self, root, value):
#         result = []
#         _root = etree.Element(root.tag)
#         for i in self.languages_ids:
#             lang = etree.SubElement(_root, 'language')
#             lang.attrib['id'] = "%s" % i
#             lang.text = value
#             result.append(lang)
#         root = _root
#         return root

#     def get_resource(self,):
#         resource = "%ss" % self._xml.tag
#         if resource == 'categorys':
#             resource = 'categories'
#         return resource

#     def get_xml(self, to_save=True):
#         root = etree.Element(self.get_resource())
#         xml = copy.copy(self._xml)

#         read_only = getattr(self, 'read_only', [])
#         for attrib in read_only:

#             attribute = getattr(xml, attrib, None)
#             print attrib, attribute
#             if attribute is not None:
#                 xml.remove(attribute)

#         root.append(xml)
#         return PsObject(root, xml=True)

#     def save(self,):
#         from .wservice import Prestashop
#         prestashop = Prestashop()

#         resource = self.get_resource()
#         xml = self.get_xml()

#         if self.id:
#             return prestashop.update(resource, xml, self.id)
#         else:
#             return prestashop.create(resource, xml)

#     def __iter__(self,):
#         return iter([PsObject(i, xml=True) for i in self._xml.getchildren()])

#     def __getitem__(self, key):
#         return [i for i in self.__iter__()][key]
