# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class BinProperties(BaseObject):
    """Wrapper for Vega-Lite BinProperties definition.
    
    Attributes
    ----------
    base: CFloat
        The number base to use for automatic bin determination (default is base 10).
    div: List(CFloat)
        Scale factors indicating allowable subdivisions.
    max: CFloat
        The maximum bin value to consider.
    maxbins: CFloat
        Maximum number of bins.
    min: CFloat
        The minimum bin value to consider.
    minstep: CFloat
        A minimum allowable step size (particularly useful for integer values).
    step: CFloat
        An exact step size to use between bins.
    steps: List(CFloat)
        An array of allowable step sizes to choose from.
    """
    base = T.CFloat(allow_none=True, default_value=None, help="""The number base to use for automatic bin determination (default is base 10).""")
    div = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Scale factors indicating allowable subdivisions.""")
    max = T.CFloat(allow_none=True, default_value=None, help="""The maximum bin value to consider.""")
    maxbins = T.CFloat(allow_none=True, default_value=None, min=2, help="""Maximum number of bins.""")
    min = T.CFloat(allow_none=True, default_value=None, help="""The minimum bin value to consider.""")
    minstep = T.CFloat(allow_none=True, default_value=None, help="""A minimum allowable step size (particularly useful for integer values).""")
    step = T.CFloat(allow_none=True, default_value=None, help="""An exact step size to use between bins.""")
    steps = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""An array of allowable step sizes to choose from.""")
    
    def __init__(self, base=None, div=None, max=None, maxbins=None, min=None, minstep=None, step=None, steps=None, **kwargs):
        kwds = dict(base=base, div=div, max=max, maxbins=maxbins, min=min, minstep=minstep, step=step, steps=steps)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(BinProperties, self).__init__(**kwargs)