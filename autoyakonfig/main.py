#!/usr/bin/env python
import argparse

import yakonfig

from autoyakonfig.auto import Autoconfig
from autoyakonfig.objects import an_object

def main():
    conf = Autoconfig(an_object)
    parser = argparse.ArgumentParser()
    args = yakonfig.parse_args(parser, [conf])
    config = yakonfig.get_global_config()
    print "The global configuration:"
    print config
    print
    obj = conf(config)
    print "The object:"
    print obj
