import importlib

_NAMES = {
    'AD', 'CD', 'CE', 'CF', 'CK', 'CM_ABS_RANGE', 'CM_AUI', 'CM_CCD', 'CM_DDI',
    'CM_DIN', 'CM_DLD', 'CM_DLT', 'CM_DTN', 'CM_EIP', 'CM_ELD', 'CM_LA1',
    'CM_MOC', 'CM_MSG', 'CM_NDL', 'CM_OCD', 'CM_OSP', 'CM_PCF', 'CM_PEN',
    'CM_PI', 'CM_PIP', 'CM_PLN', 'CM_PRL', 'CM_PTA', 'CM_RANGE', 'CM_RFR',
    'CM_RI', 'CM_RMC', 'CM_SPD', 'CM_SPS', 'CM_UVC', 'CM_VR', 'CM_WVI', 'CN',
    'CP', 'CQ', 'CX', 'DLN', 'DR', 'ED', 'EI', 'FC', 'FT', 'HD', 'JCC', 'MA',
    'MO', 'NA', 'PL', 'PPN', 'PT', 'QIP', 'QSC', 'RCD', 'RI', 'RP', 'SCV',
    'SN', 'TQ', 'TS', 'TX', 'VH', 'XAD', 'XCN', 'XON', 'XPN', 'XTN', 'varies'
}


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _NAMES:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
