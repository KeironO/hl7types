import importlib
import sys
import types

_all_ = {
    'ACC', 'ADD', 'AIG', 'AIL', 'AIP', 'AIS', 'AL1', 'APR', 'ARQ', 'AUT',
    'BHS', 'BLG', 'BTS', 'CDM', 'CM0', 'CM1', 'CM2', 'CSP', 'CSR', 'CSS',
    'CTD', 'CTI', 'DB1', 'DG1', 'DRG', 'DSC', 'DSP', 'EQL', 'ERQ', 'ERR',
    'EVN', 'FAC', 'FHS', 'FT1', 'FTS', 'GOL', 'GT1', 'IN1', 'IN2', 'IN3',
    'LCC', 'LCH', 'LDP', 'LOC', 'LRL', 'MFA', 'MFE', 'MFI', 'MRG', 'MSA',
    'MSH', 'NCK', 'NK1', 'NPU', 'NSC', 'NST', 'NTE', 'OBR', 'OBX', 'ODS',
    'ODT', 'OM1', 'OM2', 'OM3', 'OM4', 'OM5', 'OM6', 'ORC', 'PCR', 'PD1',
    'PDC', 'PEO', 'PES', 'PID', 'PR1', 'PRA', 'PRB', 'PRC', 'PRD', 'PSH',
    'PTH', 'PV1', 'PV2', 'QAK', 'QRD', 'QRF', 'RDF', 'RDT', 'RF1', 'RGS',
    'ROL', 'RQ1', 'RQD', 'RXA', 'RXC', 'RXD', 'RXE', 'RXG', 'RXO', 'RXR',
    'SCH', 'SPR', 'STF', 'TXA', 'UB1', 'UB2', 'URD', 'URS', 'VAR', 'VTQ'
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
