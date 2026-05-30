import importlib

_NAMES = {
    'ACC', 'ADD', 'AL1', 'BHS', 'BLG', 'BTS', 'DG1', 'DSC', 'DSP', 'ERR',
    'EVN', 'FHS', 'FT1', 'FTS', 'GT1', 'IN1', 'IN2', 'IN3', 'MFA', 'MFE',
    'MFI', 'MRG', 'MSA', 'MSH', 'NCK', 'NK1', 'NPU', 'NSC', 'NST', 'NTE',
    'OBR', 'OBX', 'ODS', 'ODT', 'OM1', 'OM2', 'OM3', 'OM4', 'OM5', 'OM6',
    'ORC', 'PID', 'PR1', 'PRA', 'PV1', 'PV2', 'QRD', 'QRF', 'RQ1', 'RQD',
    'RXA', 'RXC', 'RXD', 'RXE', 'RXG', 'RXO', 'RXR', 'STF', 'UB1', 'UB2',
    'URD', 'URS'
}


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _NAMES:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
