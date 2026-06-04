from __future__ import annotations

import re
from typing import Any

from pydantic import ValidationError

from hl7types.hl7.v2_5.datatypes.CWE import CWE
from hl7types.hl7.v2_5.datatypes.ERL import ERL
from hl7types.hl7.v2_5.segments.ERR import ERR

HL70357: dict[str, str] = {
    "0": "Message accepted",
    "100": "Segment sequence error",
    "101": "Required field missing",
    "102": "Data type error",
    "103": "Table value not found",
    "104": "Value too long",
    "198": "Non-Conformant Cardinality",
    "199": "Other HL7 Error",
    "200": "Unsupported message type",
    "201": "Unsupported event code",
    "202": "Unsupported processing id",
    "203": "Unsupported version id",
    "204": "Unknown key identifier",
    "205": "Duplicate key identifier",
    "206": "Application record locked",
    "207": "Application error",
}


def _error_code_from_pydantic_error(error: dict[str, Any]) -> str:
    error_type = str(error.get("type", ""))
    message = str(error.get("msg", "")).lower()

    if error_type == "missing":
        return "101"

    if error_type in {"string_too_long", "too_long"}:
        return "104"

    if "not in table" in message:
        return "103"

    if (
        "valid hl7 datetime" in message
        or "valid hl7 date" in message
        or "valid hl7 time" in message
        or "wrong data type" in message
    ):
        return "102"

    if error_type in {
        "int_parsing",
        "float_parsing",
        "bool_parsing",
        "date_parsing",
        "datetime_parsing",
        "time_parsing",
        "string_type",
        "int_type",
        "float_type",
        "bool_type",
        "date_type",
        "datetime_type",
        "time_type",
    }:
        return "102"

    return "199"


def _segment_and_field_from_loc(loc: tuple[Any, ...]) -> tuple[str | None, int | None]:
    if not loc:
        return None, None

    first = str(loc[0])
    match = re.fullmatch(r"([a-zA-Z]{3})_(\d+)", first)

    if not match:
        return None, None

    return match.group(1).upper(), int(match.group(2))


def _err_location_from_pydantic_loc(loc: tuple[Any, ...]) -> ERL | None:
    segment_id, field_position = _segment_and_field_from_loc(loc)

    if segment_id is None or field_position is None:
        return None

    return ERL(
        erl_1=segment_id,
        erl_2="1",
        erl_3=str(field_position),
    )


def err_from_pydantic_error(error: dict[str, Any]) -> ERR:
    code = _error_code_from_pydantic_error(error)
    display = HL70357[code]

    location = _err_location_from_pydantic_loc(tuple(error.get("loc", ())))
    return ERR(
        err_2=[location] if location is not None else None,
        err_3=CWE(
            cwe_1=code,
            cwe_2=display,
            cwe_3="HL70357",
        ),
        err_4="E",
    )


def errs_from_exception(exc: Exception) -> list[ERR]:
    if isinstance(exc, ValidationError):
        return [err_from_pydantic_error(error) for error in exc.errors() if error]
