from __future__ import annotations

import pytest
from pydantic import ValidationError

from hl7types.hl7.v2_6.datatypes import LA1


def test_basic_max_length() -> None:
    with pytest.raises(ValidationError):
        LA1(la1_3="abcdefghijklmnopqrstuvwxyz")
