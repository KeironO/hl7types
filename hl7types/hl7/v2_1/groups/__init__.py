import importlib
import sys
import types

_all_ = {
    'ADR_A19_QUERY_RESPONSE', 'ADT_A17_PATIENT', 'BAR_P01_VISIT',
    'BAR_P02_PATIENT', 'ORM_O01_CHOICE', 'ORM_O01_ORDER',
    'ORM_O01_ORDER_DETAIL', 'ORM_O01_PATIENT', 'ORR_O02_CHOICE',
    'ORR_O02_ORDER', 'ORR_O02_ORDER_DETAIL', 'ORR_O02_PATIENT',
    'ORU_R01_OBSERVATION', 'ORU_R01_ORDER_OBSERVATION', 'ORU_R01_PATIENT',
    'ORU_R01_PATIENT_RESULT', 'ORU_R03_OBSERVATION',
    'ORU_R03_ORDER_OBSERVATION', 'ORU_R03_PATIENT', 'ORU_R03_PATIENT_RESULT'
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
