from typing import Union, Dict, Any


def get_value_name(value: Union[Dict, Any], separate_slice: bool = False) -> Any:
    """

    :param value: can be dict, dict with 'args' key - mean this is {'arg': {'args': 'product_quantity'}, 'slice': 1}
            or {'arg': 'product_quantity', 'slice': 1} or 'product_quantity'
    :param separate_slice:
    :return:
    """
    args = None
    if isinstance(value, dict):
        if 'arg' in value:
            args = value['arg']['args'] if 'args' in value['arg'] else value['arg']
        elif 'func' in value:
            args = value['func']['l_value']['args']
    if not args:
        args = value['args']
    if not separate_slice:
        if 'slice' in value:
            args = f"{args}[\'{value['slice']}\']" if isinstance(value['slice'], str) \
                else f"{args}[{value['slice']}]"
        return args, None
    else:
        _slice = value.get('slice', None)
        return args, _slice


def is_int(value: Union[str, int]) -> int:
    try:
        return int(value)
    except Exception as e:
        raise e
