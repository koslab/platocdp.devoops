from zope.interface import implements, Interface
from zope.component import adapts
from tidylib import tidy_document
from repoze.xmliter.utils import getHTMLSerializer
from plone.transformchain.interfaces import ITransform

class DisableThemeForAjax(object):
    implements(ITransform)
    adapts(Interface, Interface) # any context, any request

    order = 8849

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def _transform(self, result):
        if self.request.get('ajax_load'):
            self.request.response.setHeader('X-Theme-Disabled', True)
        return result

    def transformString(self, result, encoding):
        return self._transform(result)

    def transformUnicode(self, result, encoding):
        return self._transform(result)

    def transformIterable(self, result, encoding):
        return [self._transform(s) for s in result]


class TidyTransform(object):
    implements(ITransform)
    adapts(Interface, Interface) # any context, any request

    order = 8851

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def tidy(self, data):
        document, errors = tidy_document(data, {
            'input-xml': True, 'output-xml': True,
            'preserve-entities': True, 'numeric-entities': True
        })
        if errors:
            print errors
        return document

    def transformString(self, result, encoding):
        return self.tidy(result)

    def transformUnicode(self, result, encoding):
        return self.tidy(result)

    def transformIterable(self, result, encoding):
        return [self.tidy(s) for s in result]

