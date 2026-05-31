import importlib

_all_ = {
    'ACC', 'ADD', 'BHS', 'BLG', 'BTS', 'DG1', 'DSC', 'DSP', 'ERR', 'EVN',
    'FHS', 'FT1', 'FTS', 'GT1', 'IN1', 'MRG', 'MSA', 'MSH', 'NCK', 'NK1',
    'NPU', 'NSC', 'NST', 'NTE', 'OBR', 'OBX', 'ORC', 'ORO', 'PID', 'PR1',
    'PV1', 'QRD', 'QRF', 'RX1', 'UB1', 'URD', 'URS'
}  # type: ignore


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _all_:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
