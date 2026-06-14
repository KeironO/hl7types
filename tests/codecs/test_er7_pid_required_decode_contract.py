"""Release contract tests for required PID fields during ER7 segment decoding.

The direct PID model constructor is already tested elsewhere. These tests ensure
the ER7 decoder applies the same required-field contract when a PID segment is
present on the wire but required fields are empty/missing.
"""
from __future__ import annotations

import pytest
from pydantic import ValidationError

from hl7types.codecs.er7.decoder import decode_er7_segment
from hl7types.hl7.v2_5_1.segments.PID import PID


@pytest.mark.parametrize(
    "wire, missing_field",
    [
        ("PID|1", "pid_3"),
        ("PID|1||12345^^^MRN^MR", "pid_5"),
    ],
)
def test_strict_er7_segment_decode_rejects_missing_pid_required_fields(
    wire: str,
    missing_field: str,
) -> None:
    with pytest.raises(ValidationError, match=missing_field):
        decode_er7_segment(wire, PID, strict=True)


def test_lenient_er7_segment_decode_warns_for_missing_pid_required_fields() -> None:
    with pytest.warns(UserWarning, match=r"PID.*pid_3|PID.*pid_5|missing required field"):
        pid = decode_er7_segment("PID|1", PID, strict=False)

    assert pid is not None
    # The important contract is not the exact placeholder value, but that this
    # path is only available in lenient mode and emits a warning.
    assert hasattr(pid, "pid_3")
    assert hasattr(pid, "pid_5")
