import importlib
import sys
import types

_all_ = {
    'AD', 'AUI', 'CCD', 'CCP', 'CD', 'CE', 'CF', 'CK', 'CN', 'CNE', 'CNS',
    'CP', 'CQ', 'CSU', 'CWE', 'CX', 'DDI', 'DIN', 'DLD', 'DLN', 'DLT', 'DR',
    'DTN', 'ED', 'EI', 'EIP', 'ELD', 'FC', 'FN', 'FT', 'HD', 'JCC', 'LA1',
    'LA2', 'MA', 'MO', 'MOC', 'MOP', 'MSG', 'NA', 'NDL', 'NR', 'OCD', 'OSD',
    'OSP', 'PCF', 'PI', 'PIP', 'PL', 'PLN', 'PN', 'PPN', 'PRL', 'PT', 'PTA',
    'QIP', 'QSC', 'RCD', 'RFR', 'RI', 'RMC', 'RP', 'SCV', 'SN', 'SPD', 'SPS',
    'TQ', 'TS', 'TX', 'TX_CHALLENGE', 'UVC', 'VH', 'VID', 'VR', 'WVI', 'WVS',
    'XAD', 'XCN', 'XON', 'XPN', 'XTN', 'varies'
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
