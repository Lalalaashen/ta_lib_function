def get_ta(arr_tuple, ta_type, factor_list, factor_name, **kwargs):
    import talib
    from talib import abstract
    import numpy as np
    try:
        function_ = abstract.Function(ta_type)
        func = getattr(talib, ta_type.upper())
        res = func(*arr_tuple, **kwargs)
        if isinstance(res, tuple):
            for name, ele in zip(function_.info['output_names'], res):
                factor_list.append(ele.reshape((-1, 1)))
                factor_name.append('{}_{}'.format(ta_type, name))
        elif isinstance(res, np.ndarray):
            factor_list.append(res.reshape((-1, 1)))
            factor_name.append(ta_type)
    except Exception as e:
        print(ta_type, e)
