# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import  wraps

def set_timeout(timeout=20):
    def _set_socket_timeout(function):
        def wrapper(*args, **kwargs):
            import socket
            default = socket.getdefaulttimeout()
            socket.setdefaulttimeout(timeout)
            try:
                result = function(*args, **kwargs)
            finally:
                socket.setdefaulttimeout(default)
            return result
        return wrapper
    return _set_socket_timeout
