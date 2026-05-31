import importlib
import sys
import types

_all_ = {
    'AD', 'CD', 'CE', 'CF', 'CK', 'CM_ABS_RANGE', 'CM_AUI', 'CM_CCD', 'CM_DDI',
    'CM_DIN', 'CM_DLD', 'CM_DLT', 'CM_DTN', 'CM_EIP', 'CM_ELD', 'CM_LA1',
    'CM_MOC', 'CM_MSG', 'CM_NDL', 'CM_OCD', 'CM_OSP', 'CM_PCF', 'CM_PEN',
    'CM_PI', 'CM_PIP', 'CM_PLN', 'CM_PRL', 'CM_PTA', 'CM_RANGE', 'CM_RFR',
    'CM_RI', 'CM_RMC', 'CM_SPD', 'CM_SPS', 'CM_UVC', 'CM_VR', 'CM_WVI', 'CN',
    'CP', 'CQ', 'CX', 'DLN', 'DR', 'ED', 'EI', 'FC', 'FT', 'HD', 'JCC', 'MA',
    'MO', 'NA', 'PL', 'PPN', 'PT', 'QIP', 'QSC', 'RCD', 'RI', 'RP', 'SCV',
    'SN', 'TQ', 'TS', 'TX', 'VH', 'XAD', 'XCN', 'XON', 'XPN', 'XTN', 'varies'
}  # type: ignore


class _LazyModule(types.ModuleType):
    def __getattr__(self, name: str):  # type: ignore[misc]
        if name not in _all_:
            raise AttributeError(f'module {self.__name__!r} has no attribute {name!r}')
        mod = importlib.import_module(f'.{name}', self.__name__)
        cls = getattr(mod, name)
        self.__dict__[name] = cls
        return cls

    def __setattr__(self, name: str, value) -> None:  # type: ignore[override]
        if name in _all_ and isinstance(value, types.ModuleType):
            self.__dict__[name] = getattr(value, name)
        else:
            self.__dict__[name] = value


sys.modules[__name__].__class__ = _LazyModule
