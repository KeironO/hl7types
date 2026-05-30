import importlib

_NAMES = {
    'AD', 'AUI', 'CCD', 'CCP', 'CD', 'CF', 'CNE', 'CNN', 'CP', 'CQ', 'CSU',
    'CWE', 'CX', 'DDI', 'DIN', 'DLD', 'DLN', 'DLT', 'DR', 'DTN', 'ED', 'EI',
    'EIP', 'ELD', 'ERL', 'FC', 'FN', 'FT', 'HD', 'ICD', 'JCC', 'LA1', 'LA2',
    'MA', 'MO', 'MOC', 'MOP', 'MSG', 'NA', 'NDL', 'NR', 'OCD', 'OSD', 'OSP',
    'PIP', 'PL', 'PLN', 'PPN', 'PRL', 'PT', 'PTA', 'QIP', 'QSC', 'RCD', 'RFR',
    'RI', 'RMC', 'RP', 'RPT', 'SAD', 'SCV', 'SN', 'SPD', 'SPS', 'SRT', 'TQ',
    'TX', 'UVC', 'VH', 'VID', 'VR', 'WVI', 'WVS', 'XAD', 'XCN', 'XON', 'XPN',
    'XTN', 'varies'
}


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _NAMES:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
