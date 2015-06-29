import requests


class BaseService(object):

    def __init__(self, key=None, base_url=None):
        if key:
            self.key = key

        if base_url:
            self.base_url = base_url

    def new(self, resource=None):
        return self.request(resource, params={'schema': 'blank'})

    def get(self, pk, resource=None, **kwargs):
        return self.request(url="{}/{}".format(resource, pk), **kwargs)

    def get_list(self, resource=None, **kwargs):
        return self.request(url=resource, **kwargs)

    def create(self, resource, xml):
        return self.request(
            method='post',
            url=resource,
            data=xml
        )

    def update(self, resource, xml, pk):
        return self.request(
            method='put',
            url="{}/{}".format(resource, pk),
            data=xml
        )

    def request(self, url=None, method='get', **kwargs):
        fn = getattr(requests, method)

        return fn(
            "{}{}".format(self.base_url, url),
            auth=(self.key, ''),
            **kwargs
        ).content


class Api(BaseService):
    key = None
    base_url = None

    @classmethod
    def config(cls, url, key):
        cls.base_url = url
        cls.key = key
