from __future__ import absolute_import

class an_object(object):
    def __init__(self, param, value="default", *args, **kwargs):
        super(an_object, self).__init__(*args, **kwargs)
        self.param = param
        self.value = value

    def __repr__(self):
        return '{0.__class__.__name__}(param={0.param!r}, value={0.value!r})'.format(self)
