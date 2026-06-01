"""
Auto-generated HAPI-equivalent primitive datatype validators.
Do not edit manually.
"""
from __future__ import annotations

import re as _re

from typing import Annotated

from pydantic import AfterValidator

_SI_RE = _re.compile(r"^\d*$")


def _validate_si(v: str) -> str:
    if not _SI_RE.match(v):
        raise ValueError(f"SI must be empty or a non-negative integer, got {v!r}")
    return v


SI_t = Annotated[str, AfterValidator(_validate_si)]

_NM_RE = _re.compile(r"^(\+|\-)?\d*\.?\d*$")


def _validate_nm(v: str) -> str:
    if not _NM_RE.match(v):
        raise ValueError(f"NM must be empty or numeric, got {v!r}")
    return v


NM_t = Annotated[str, AfterValidator(_validate_nm)]

_DT_RE = _re.compile(r"^(\d{4}([01]\d(\d{2})?)?)?$")


def _validate_dt(v: str) -> str:
    if not _DT_RE.match(v):
        raise ValueError(f"DT must be empty or a valid HL7 date (YYYY[MM[DD]]), got {v!r}")
    return v


DT_t = Annotated[str, AfterValidator(_validate_dt)]

_TM_RE = _re.compile(
    r"^([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?([\+\-]\d{4})?$"
)


def _validate_tm(v: str) -> str:
    if not _TM_RE.match(v):
        raise ValueError(
            f"TM must be empty or a valid HL7 time ([HH[MM[SS[.S...]]]][+/-ZZZZ]), got {v!r}"
        )
    return v


TM_t = Annotated[str, AfterValidator(_validate_tm)]

_DTM25_RE = _re.compile(
    r"^(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?"
    r"([\+\-]\d{4})?$"
)


def _validate_dtm(v: str) -> str:
    if not _DTM25_RE.match(v):
        raise ValueError(
            f"DTM must be empty or a valid HL7 v2.5 datetime "
            f"(YYYY[MM[DD[HH[MM[SS[.S...]]]]]][+/-ZZZZ]), got {v!r}"
        )
    return v


DTM_t = Annotated[str, AfterValidator(_validate_dtm)]

def _validate_nulldt(v: str) -> str:
    if v != "":
        raise ValueError(f"NULLDT is a withdrawn datatype and must be empty, got {v!r}")
    return v


NULLDT_t = Annotated[str, AfterValidator(_validate_nulldt)]

_DTM_PRE25_RE = _re.compile(
    r"^(\d{4}([01]\d(\d{2}([012]\d[0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?"
    r"([\+\-]\d{4})?$"
)


def _validate_ts_pre25(v: str) -> str:
    if not _DTM_PRE25_RE.match(v):
        raise ValueError(
            f"TS.1 must be empty or a valid HL7 pre-v2.5 datetime "
            f"(YYYY[MM[DD[HHMM[SS[.S...]]]]]][+/-ZZZZ]), got {v!r}"
        )
    return v


TSComponentOne_t = Annotated[str, AfterValidator(_validate_ts_pre25)]
