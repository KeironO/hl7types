import importlib
import sys
import types

_all_ = {
    'AD', 'AUI', 'CCD', 'CCP', 'CD', 'CE', 'CF', 'CNE', 'CNN', 'CP', 'CQ',
    'CSU', 'CWE', 'CX', 'DDI', 'DIN', 'DLD', 'DLN', 'DLT', 'DR', 'DTN', 'ED',
    'EI', 'EIP', 'ELD', 'ERL', 'FC', 'FN', 'HD', 'ICD', 'JCC', 'LA1', 'LA2',
    'MA', 'MO', 'MOC', 'MOP', 'MSG', 'NA', 'NDL', 'NR', 'OCD', 'OSD', 'OSP',
    'PIP', 'PL', 'PLN', 'PPN', 'PRL', 'PT', 'PTA', 'QIP', 'QSC', 'RCD', 'RFR',
    'RI', 'RMC', 'RP', 'RPT', 'SAD', 'SCV', 'SN', 'SPD', 'SPS', 'SRT', 'TQ',
    'TS', 'UVC', 'VH', 'VID', 'VR', 'WVI', 'WVS', 'XAD', 'XCN', 'XON', 'XPN',
    'XTN', 'varies'
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
