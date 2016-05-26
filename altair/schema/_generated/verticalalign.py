# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class VerticalAlign(T.Enum):
    """One of ['top', 'middle', 'bottom']"""
    def __init__(self, default_value=T.Undefined, **metadata):
        super(VerticalAlign, self).__init__(['top', 'middle', 'bottom'],
                                    default_value=default_value,
                                    **metadata)