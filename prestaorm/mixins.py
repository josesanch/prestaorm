import copy

from lxml import etree, objectify

from .managers import BaseManager
from .utils import classproperty


class MixinRepr(object):

    def __repr__(self,):
        return self.__str__()

    # def __int__(self):
    #     if type(self._xml) in [objectify.IntElement]:
    #         return int(self._xml)

    def __str__(self,):
        return etree.tostring(self, pretty_print=True)


class MixinXml(object):

    def set_language(self, value, id=None):
        for item in self.getchildren():
            if not id or item.get('id') == id:
                obj = objectify.E.language(value, id=item.get('id'))
                self.remove(item)
                self.append(obj)

        return self


class MixinModelActions(object):

    def get_xml(self, to_save=True):
        prestashop = etree.Element("prestashop")
        xml = copy.copy(self)

        read_only = getattr(self, 'read_only', [])
        for attrib in read_only:
            attribute = getattr(xml, attrib, None)
            if attribute is not None:
                xml.remove(attribute)

        prestashop.append(xml)
        return etree.tostring(prestashop)

    def save(self,):
        manager = self.get_manager()
        resource = self.resource
        xml = self.get_xml()

        if self.id is not None:
            return manager.service.update(resource, xml, self.id.text)
        else:
            return manager.service.create(resource, xml)


class Node(MixinXml,
           MixinRepr,
           objectify.ObjectifiedElement):
    pass


class BaseModel(MixinModelActions,
                Node):
    _default_manager = BaseManager

    @classproperty
    def objects(cls):
        return cls().get_manager()

    def get_manager(self,):
        return self._default_manager(model=self.__class__)
