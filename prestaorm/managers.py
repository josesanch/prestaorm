import copy

from .service import Api
from .utils import convert_to_model_instance, convert_to_model_instances


class BaseManager(object):

    def __init__(self, model):
        self.model = model
        self._values = []
        self._filter = {}
        self._sort = []
        self._limits = []

    def create(self,):
        return convert_to_model_instance(
            self.service.new(self.model.resource),
            self.model,
            unwrap=True)

    def get_or_create(self, commit=False, **kwargs):
        obj = self.get(**kwargs)
        if obj:
            return (obj, False)

        obj = self.create()
        for k, v in kwargs.items():
            node = getattr(obj, k)

            if node.find('language') is not None:
                node.set_language(v)
            else:
                setattr(obj, k, v)

        if commit:
            obj = obj.save()

        return (obj, True)

    def _to_models(self, items, list=True):
        fn = convert_to_model_instances if list else convert_to_model_instance
        return fn(items, self.model)

    def get(self, pk=None, **kwargs):
        if pk is not None:
            return self._to_models(self.service.get(pk, self.model.resource), False)

        return self.filter(**kwargs).first()

    @property
    def service(self,):
        if hasattr(self, '_service'):
            return self._service
        self._service = Api()
        return self._service

    def __iter__(self,):
        return [i for i in self.all()]

    def all(self,):
        return self._to_models(
            self.service.get_list(self.model.resource, params=self.get_params()))

    def __repr__(self,):
        return str(self.all())

    def get_params(self,):
        params = {'display': 'full'}
        if self._values:
            params['display'] = "[{}]".format(','.join(self._values))

        if self._sort:
            params['sort'] = "[{}]".format(','.join(self._sort))

        if self._limits:
            offset = self._limits.start
            limit = self._limits.stop
            if offset:
                limit = limit - offset

            params['limit'] = ':'.join(map(str, [i for i in [limit, offset] if i is not None]))

        if self._filter:
            for k, v in self._filter.items():
                params["filter[{}]".format(k)] = v

        return params

    def values(self, *args):
        clone = copy.copy(self)
        clone._values = args
        return clone

    def filter(self, *args, **kwargs):
        clone = copy.copy(self)
        for k, v in kwargs.items():
            self._filter[k] = v
        return clone

    def order_by(self, args):
        clone = copy.copy(self)
        clone._sort = args
        return clone

    def __getitem__(self, slice):
        clone = copy.copy(self)
        clone._limits = slice
        return clone

    def __len__(self,):
        return len(self.all())

    def first(self,):
        items = self.all()
        if len(items) > 0:
            return items[0]
