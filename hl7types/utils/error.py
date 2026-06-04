from __future__ import annotations

import importlib
import re
from typing import Any

from pydantic import ValidationError

from hl7types._utils import version_to_module
from hl7types.hl7 import HL7Model

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

HL70060: set[str] = {
    "0",
    "100",
    "101",
    "102",
    "103",
    "200",
    "201",
    "202",
    "203",
    "204",
    "205",
    "206",
    "207",
}


def _import_from_version(version: str, kind: str, name: str) -> type[HL7Model] | None:
    mod_name = version_to_module(version)
    try:
        mod = importlib.import_module(f"hl7types.hl7.{mod_name}.{kind}.{name}")
        cls = getattr(mod, name, None)
        if isinstance(cls, type) and issubclass(cls, HL7Model):
            return cls
    except ModuleNotFoundError:
        pass
    return None


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


def _parse_version(version: str) -> tuple[int, ...]:
    return tuple(int(x) for x in version.split("."))


def err_from_pydantic_error(error: dict[str, Any], version: str) -> HL7Model:
    """Convert a single Pydantic error dict into a version-appropriate ``ERR`` segment.

    Parameters
    ----------
    error : dict
        A single error entry from ``ValidationError.errors()``.
    version : str
        The HL7 version string, e.g. ``"2.5.1"`` or ``"2.8.2"``. Determines
        the structure of the returned ``ERR`` segment.

    Returns
    -------
    HL7Model
        An ``ERR`` segment instance for the given version.

    Raises
    ------
    ValueError
        If no ``ERR`` segment class is found for the given version.
    """
    err_cls = _import_from_version(version, "segments", "ERR")
    if err_cls is None:
        raise ValueError(f"ERR segment not found for version {version!r}")

    code = _error_code_from_pydantic_error(error)
    display = HL70357[code]
    v = _parse_version(version)
    segment_id, field_position = _segment_and_field_from_loc(tuple(error.get("loc", ())))

    kwargs: dict[str, Any] = {}

    if v <= (2, 2):
        kwargs["err_1"] = [code, str(field_position)]

    elif v <= (2, 5):
        eld_cls = _import_from_version(version, "datatypes", "ELD")
        ce_cls = _import_from_version(version, "datatypes", "CE")
        if eld_cls is not None and ce_cls is not None:
            hl70060_code = code if code in HL70060 else "207"
            kwargs["err_1"] = [
                eld_cls(
                    eld_1=segment_id,
                    eld_2="1",
                    eld_3=str(field_position) if field_position is not None else None,
                    eld_4=ce_cls(ce_1=hl70060_code, ce_2=HL70357.get(hl70060_code), ce_3="HL70060"),
                )
            ]

    if v >= (2, 5):
        cwe_cls = _import_from_version(version, "datatypes", "CWE")
        if cwe_cls is not None:
            kwargs["err_3"] = cwe_cls(cwe_1=code, cwe_2=display, cwe_3="HL70357")

        kwargs["err_4"] = "E"

        erl_cls = _import_from_version(version, "datatypes", "ERL")
        if erl_cls is not None and segment_id is not None and field_position is not None:
            kwargs["err_2"] = [erl_cls(erl_1=segment_id, erl_2="1", erl_3=str(field_position))]

    return err_cls(**kwargs)


def errs_from_exception(exc: Exception, version: str) -> list[HL7Model]:
    """Convert an exception into a list of version-appropriate ``ERR`` segments.

    Only ``pydantic.ValidationError`` is handled. Any other exception type
    returns an empty list.

    Parameters
    ----------
    exc : Exception
        The exception to convert. Typically a ``pydantic.ValidationError``
        raised by ``decode_er7`` or direct model construction.
    version : str
        The HL7 version string, e.g. ``"2.5.1"`` or ``"2.8.2"``. Determines
        the structure of each returned ``ERR`` segment.

    Returns
    -------
    list[HL7Model]
        One ``ERR`` segment per violated field, or an empty list if ``exc``
        is not a ``ValidationError``.
    """
    if isinstance(exc, ValidationError):
        return [err_from_pydantic_error(error, version) for error in exc.errors() if error]
    return []
