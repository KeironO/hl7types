import importlib

_NAMES = {
    'ABS', 'ACC', 'ADD', 'AFF', 'AIG', 'AIL', 'AIP', 'AIS', 'AL1', 'APR',
    'ARQ', 'AUT', 'BHS', 'BLC', 'BLG', 'BPO', 'BPX', 'BTS', 'BTX', 'CDM',
    'CER', 'CM0', 'CM1', 'CM2', 'CNS', 'CON', 'CSP', 'CSR', 'CSS', 'CTD',
    'CTI', 'DB1', 'DG1', 'DRG', 'DSC', 'DSP', 'ECD', 'ECR', 'EDU', 'EQL',
    'EQP', 'EQU', 'ERQ', 'ERR', 'EVN', 'FAC', 'FHS', 'FT1', 'FTS', 'GOL',
    'GP1', 'GP2', 'GT1', 'IAM', 'IIM', 'IN1', 'IN2', 'IN3', 'INV', 'IPC',
    'ISD', 'LAN', 'LCC', 'LCH', 'LDP', 'LOC', 'LRL', 'MFA', 'MFE', 'MFI',
    'MRG', 'MSA', 'MSH', 'NCK', 'NDS', 'NK1', 'NPU', 'NSC', 'NST', 'NTE',
    'OBR', 'OBX', 'ODS', 'ODT', 'OM1', 'OM2', 'OM3', 'OM4', 'OM5', 'OM6',
    'OM7', 'ORC', 'ORG', 'OVR', 'PCR', 'PD1', 'PDA', 'PDC', 'PEO', 'PES',
    'PID', 'PR1', 'PRA', 'PRB', 'PRC', 'PRD', 'PSH', 'PTH', 'PV1', 'PV2',
    'QAK', 'QID', 'QPD', 'QRD', 'QRF', 'QRI', 'RCP', 'RDF', 'RDT', 'RF1',
    'RGS', 'RMI', 'ROL', 'RQ1', 'RQD', 'RXA', 'RXC', 'RXD', 'RXE', 'RXG',
    'RXO', 'RXR', 'SAC', 'SCH', 'SFT', 'SID', 'SPM', 'SPR', 'STF', 'TCC',
    'TCD', 'TQ1', 'TQ2', 'TXA', 'UB1', 'UB2', 'URD', 'URS', 'VAR', 'VTQ'
}


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _NAMES:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
