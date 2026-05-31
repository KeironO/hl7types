import importlib

_all_ = {
    'AD', 'AUI', 'CCD', 'CCP', 'CD', 'CE', 'CF', 'CK', 'CN', 'CNE', 'CNN',
    'CP', 'CQ', 'CSU', 'CWE', 'CX', 'DDI', 'DIN', 'DLD', 'DLN', 'DLT', 'DR',
    'DTN', 'ED', 'EI', 'EIP', 'ELD', 'FC', 'FN', 'FT', 'HD', 'JCC', 'LA1',
    'LA2', 'MA', 'MO', 'MOC', 'MOP', 'MSG', 'NA', 'NDL', 'NR', 'OCD', 'OSD',
    'OSP', 'PCF', 'PI', 'PIP', 'PL', 'PLN', 'PN', 'PPN', 'PRL', 'PT', 'PTA',
    'QIP', 'QSC', 'RCD', 'RFR', 'RI', 'RMC', 'RP', 'SAD', 'SCV', 'SN', 'SPD',
    'SPS', 'SRT', 'TQ', 'TS', 'TX', 'TX_CHALLENGE', 'UVC', 'VH', 'VID', 'VR',
    'WVI', 'WVS', 'XAD', 'XCN', 'XON', 'XPN', 'XTN', 'varies'
}  # type: ignore


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _all_:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
