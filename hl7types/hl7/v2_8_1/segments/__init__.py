import importlib
import sys
import types

_all_ = {
    'ABS', 'ACC', 'ADD', 'ADJ', 'AFF', 'AIG', 'AIL', 'AIP', 'AIS', 'AL1',
    'APR', 'ARQ', 'ARV', 'AUT', 'BHS', 'BLC', 'BLG', 'BPO', 'BPX', 'BTS',
    'BTX', 'BUI', 'CDM', 'CDO', 'CER', 'CM0', 'CM1', 'CM2', 'CNS', 'CON',
    'CSP', 'CSR', 'CSS', 'CTD', 'CTI', 'DB1', 'DG1', 'DMI', 'DON', 'DRG',
    'DSC', 'DSP', 'ECD', 'ECR', 'EDU', 'EQP', 'EQU', 'ERR', 'EVN', 'FAC',
    'FHS', 'FT1', 'FTS', 'GOL', 'GP1', 'GP2', 'GT1', 'Hxx', 'IAM', 'IAR',
    'IIM', 'ILT', 'IN1', 'IN2', 'IN3', 'INV', 'IPC', 'IPR', 'ISD', 'ITM',
    'IVC', 'IVT', 'LAN', 'LCC', 'LCH', 'LDP', 'LOC', 'LRL', 'MFA', 'MFE',
    'MFI', 'MRG', 'MSA', 'MSH', 'NCK', 'NDS', 'NK1', 'NPU', 'NSC', 'NST',
    'NTE', 'OBR', 'OBX', 'ODS', 'ODT', 'OM1', 'OM2', 'OM3', 'OM4', 'OM5',
    'OM6', 'OM7', 'ORC', 'ORG', 'OVR', 'PAC', 'PCE', 'PCR', 'PD1', 'PDA',
    'PDC', 'PEO', 'PES', 'PID', 'PKG', 'PMT', 'PR1', 'PRA', 'PRB', 'PRC',
    'PRD', 'PRT', 'PSG', 'PSH', 'PSL', 'PSS', 'PTH', 'PV1', 'PV2', 'PYE',
    'QAK', 'QID', 'QPD', 'QRD', 'QRF', 'QRI', 'RCP', 'RDF', 'RDT', 'REL',
    'RF1', 'RFI', 'RGS', 'RMI', 'ROL', 'RQ1', 'RQD', 'RXA', 'RXC', 'RXD',
    'RXE', 'RXG', 'RXO', 'RXR', 'RXV', 'SAC', 'SCD', 'SCH', 'SCP', 'SDD',
    'SFT', 'SGH', 'SGT', 'SHP', 'SID', 'SLT', 'SPM', 'STF', 'STZ', 'TCC',
    'TCD', 'TQ1', 'TQ2', 'TXA', 'UAC', 'UB1', 'UB2', 'URD', 'URS', 'VAR',
    'VND', 'ZL7', 'Zxx'
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
