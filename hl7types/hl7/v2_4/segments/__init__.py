import importlib
import sys
import types

_all_ = {
    'ABS', 'ACC', 'ADD', 'AFF', 'AIG', 'AIL', 'AIP', 'AIS', 'AL1', 'APR',
    'ARQ', 'AUT', 'BHS', 'BLC', 'BLG', 'BTS', 'CDM', 'CM0', 'CM1', 'CM2',
    'CNS', 'CSP', 'CSR', 'CSS', 'CTD', 'CTI', 'DB1', 'DG1', 'DRG', 'DSC',
    'DSP', 'ECD', 'ECR', 'EDU', 'EQL', 'EQP', 'EQU', 'ERQ', 'ERR', 'EVN',
    'FAC', 'FHS', 'FT1', 'FTS', 'GOL', 'GP1', 'GP2', 'GT1', 'IAM', 'IN1',
    'IN2', 'IN3', 'INV', 'ISD', 'LAN', 'LCC', 'LCH', 'LDP', 'LOC', 'LRL',
    'MFA', 'MFE', 'MFI', 'MRG', 'MSA', 'MSH', 'NCK', 'NDS', 'NK1', 'NPU',
    'NSC', 'NST', 'NTE', 'OBR', 'OBX', 'ODS', 'ODT', 'OM1', 'OM2', 'OM3',
    'OM4', 'OM5', 'OM6', 'OM7', 'ORC', 'ORG', 'PCR', 'PD1', 'PDA', 'PDC',
    'PEO', 'PES', 'PID', 'PR1', 'PRA', 'PRB', 'PRC', 'PRD', 'PSH', 'PTH',
    'PV1', 'PV2', 'QAK', 'QID', 'QPD', 'QRD', 'QRF', 'QRI', 'RCP', 'RDF',
    'RDT', 'RF1', 'RGS', 'RMI', 'ROL', 'RQ1', 'RQD', 'RXA', 'RXC', 'RXD',
    'RXE', 'RXG', 'RXO', 'RXR', 'SAC', 'SCH', 'SID', 'SPR', 'STF', 'TCC',
    'TCD', 'TXA', 'UB1', 'UB2', 'URD', 'URS', 'VAR', 'VTQ'
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
