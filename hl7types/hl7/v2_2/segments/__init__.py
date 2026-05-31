import importlib
import sys
import types

_all_ = {
    'ACC', 'ADD', 'AL1', 'BHS', 'BLG', 'BTS', 'DG1', 'DSC', 'DSP', 'ERR',
    'EVN', 'FHS', 'FT1', 'FTS', 'GT1', 'IN1', 'IN2', 'IN3', 'MFA', 'MFE',
    'MFI', 'MRG', 'MSA', 'MSH', 'NCK', 'NK1', 'NPU', 'NSC', 'NST', 'NTE',
    'OBR', 'OBX', 'ODS', 'ODT', 'OM1', 'OM2', 'OM3', 'OM4', 'OM5', 'OM6',
    'ORC', 'PID', 'PR1', 'PRA', 'PV1', 'PV2', 'QRD', 'QRF', 'RQ1', 'RQD',
    'RXA', 'RXC', 'RXD', 'RXE', 'RXG', 'RXO', 'RXR', 'STF', 'UB1', 'UB2',
    'URD', 'URS'
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
