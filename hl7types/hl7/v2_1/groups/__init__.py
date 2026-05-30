import importlib

_NAMES = {
    'ADR_A19_QUERY_RESPONSE', 'ADT_A17_PATIENT', 'BAR_P01_VISIT',
    'BAR_P02_PATIENT', 'ORM_O01_CHOICE', 'ORM_O01_ORDER',
    'ORM_O01_ORDER_DETAIL', 'ORM_O01_PATIENT', 'ORR_O02_CHOICE',
    'ORR_O02_ORDER', 'ORR_O02_ORDER_DETAIL', 'ORR_O02_PATIENT',
    'ORU_R01_OBSERVATION', 'ORU_R01_ORDER_OBSERVATION', 'ORU_R01_PATIENT',
    'ORU_R01_PATIENT_RESULT', 'ORU_R03_OBSERVATION',
    'ORU_R03_ORDER_OBSERVATION', 'ORU_R03_PATIENT', 'ORU_R03_PATIENT_RESULT'
}


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _NAMES:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
