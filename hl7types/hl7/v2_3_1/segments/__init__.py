import importlib

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


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _all_:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
