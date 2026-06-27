from __future__ import annotations

import warnings
from typing import Callable

__all__ = ["NonStandardDateWarning", "_apply_dt_fallback"]


class NonStandardDateWarning(UserWarning):
    """Emitted when a fallback parser normalises a non-HL7 date/datetime value."""


def _apply_dt_fallback(
    v: str,
    *,
    parser: Callable[[str], str] | None,
    datatype: str,
    field_path: str,
) -> str: # noqa
    """Call *parser* to normalise *v*; warn on success; raise ``ValueError`` on failure.

    Parameters
    ----------
    v:
        Raw non-HL7 string that failed the standard regex check.
    parser:
        User-supplied callable that converts *v* to a valid HL7 DT/DTM string.
        ``None`` means no fallback is configured.
    datatype:
        ``"DT"`` or ``"DTM"``, used in warning/error messages.
    field_path:
        HL7 dot-notation path of the field being validated, e.g. ``"TS.1"``.
    """
    if parser is None:
        raise ValueError(f"{v!r} is not empty or a valid HL7 {datatype}")
    try:
        normalised = parser(v)
    except Exception as exc:
        raise ValueError(
            f"Fallback {datatype} parser failed for {v!r} at {field_path}: {exc}"
        ) from exc
    warnings.warn(
        NonStandardDateWarning(
            f"Non-standard {datatype} value {v!r} at {field_path} was accepted "
            f"and normalised to {normalised!r} by the fallback parser."
        ),
        stacklevel=6,
    )
    return normalised
