from __future__ import absolute_import
from yakonfig import Configurable, ConfigurationError

class Autoconfig(Configurable):
    def __init__(self, cls, *args, **kwargs):
        super(Autoconfig, self).__init__(*args, **kwargs)
        self.cls = cls
        self.name = cls.__name__
        ctor = getattr(cls, '__init__')
        defaults = ctor.__defaults__
        code = ctor.__code__
        last_param = code.co_argcount
        first_param = last_param - len(defaults)
        names = code.co_varnames[first_param:last_param]
        self.defaults = dict(zip(names, defaults))
        self.required = code.co_varnames[1:first_param]
        self.all_params = code.co_varnames[1:last_param]

    @property
    def config_name(self):
        return self.name

    @property
    def default_config(self):
        return self.defaults

    def add_arguments(self, parser):
        for k,v in self.defaults.iteritems():
            parser.add_argument('--{}'.format(k),
                                help='default={}'.format(v))
        for k in self.required:
            parser.add_argument('--{}'.format(k),
                                help='required')

    @property
    def runtime_keys(self):
        return {k: k for k in self.all_params}

    def check_config(self, config, name):
        for k in self.required:
            if k not in config:
                raise ConfigurationError(
                    'missing configuration for {} in {}'
                    .format(k, name))

    def __call__(self, config):
        c = config[self.config_name]
        args = []
        for k in self.all_params:
            args.append(c[k])
        return self.cls(*args)
