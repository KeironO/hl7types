import importlib

_all_ = {
    'AD', 'CE', 'CK_ACCOUNT_NO', 'CK_PAT_ID', 'CM_ABS_RANGE', 'CM_AUI',
    'CM_BATCH_TOTAL', 'CM_CCD', 'CM_DDI', 'CM_DIN', 'CM_DLD', 'CM_DLT',
    'CM_DTN', 'CM_EIP', 'CM_ELD', 'CM_FILLER', 'CM_FINANCE', 'CM_GROUP_ID',
    'CM_INTERNAL_LOCATION', 'CM_JOB_CODE', 'CM_LA1', 'CM_LICENSE_NO', 'CM_MOC',
    'CM_MSG', 'CM_NDL', 'CM_OCD', 'CM_OSP', 'CM_PAT_ID', 'CM_PAT_ID_0192',
    'CM_PCF', 'CM_PEN', 'CM_PIP', 'CM_PLACER', 'CM_PLN', 'CM_POSITION',
    'CM_PRACTITIONER', 'CM_PTA', 'CM_RANGE', 'CM_RFR', 'CM_RI', 'CM_RMC',
    'CM_SPD', 'CM_SPS', 'CM_UVC', 'CM_VR', 'CN_PERSON', 'CN_PHYSICIAN',
    'CQ_QUANTITY', 'FT', 'PN', 'TQ', 'TS', 'TX', 'varies'
}  # type: ignore


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _all_:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
