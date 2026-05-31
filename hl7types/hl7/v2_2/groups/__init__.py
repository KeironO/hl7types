import importlib
import sys
import types

_all_ = {
    'ADR_A19_INSURANCE', 'ADR_A19_QUERY_RESPONSE', 'ADT_A01_INSURANCE',
    'ADT_A04_INSURANCE', 'ADT_A05_INSURANCE', 'ADT_A06_INSURANCE',
    'ADT_A07_INSURANCE', 'ADT_A08_INSURANCE', 'ADT_A13_INSURANCE',
    'ADT_A14_INSURANCE', 'ADT_A28_INSURANCE', 'ADT_A31_INSURANCE',
    'BAR_P01_INSURANCE', 'BAR_P01_VISIT', 'BAR_P02_PATIENT', 'MFN_M01_MF',
    'MFN_M02_MF_STAFF', 'MFN_M03_MF_TEST', 'MFR_M01_MF', 'MFR_M02_MF_STAFF',
    'MFR_M03_MF_TEST', 'NMD_N01_APP_STATS', 'NMD_N01_APP_STATUS',
    'NMD_N01_CLOCK', 'NMD_N01_CLOCK_AND_STATS_WITH_NOTES',
    'NMQ_N02_CLOCK_AND_STATISTICS', 'NMQ_N02_QRY_WITH_DETAIL',
    'NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT', 'ORF_R04_OBSERVATION',
    'ORF_R04_ORDER', 'ORF_R04_QUERY_RESPONSE', 'ORM_O01_CHOICE',
    'ORM_O01_ORDER', 'ORM_O01_ORDER_DETAIL', 'ORM_O01_PATIENT',
    'ORR_O02_CHOICE', 'ORR_O02_ORDER', 'ORR_O02_ORDER_DETAIL',
    'ORR_O02_PATIENT', 'ORU_R01_OBSERVATION', 'ORU_R01_ORDER_OBSERVATION',
    'ORU_R01_PATIENT', 'ORU_R01_PATIENT_RESULT'
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
