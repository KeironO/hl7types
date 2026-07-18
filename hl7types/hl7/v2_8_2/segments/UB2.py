"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: UB2
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.OCD import OCD
from ..datatypes.OSP import OSP
from ..datatypes.UVC import UVC

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class UB2(HL7Model):
    """Uniform Billing Data (S6.5.11).

    Attributes
    ----------
    ub2_1 : str | None
        UB2.1 - Set ID - UB2 (SI) O S6.5.11.1

    ub2_2 : str | None
        UB2.2 - Co-Insurance Days (9) (ST) O S6.5.11.2

    ub2_3 : list[CWE] | None
        UB2.3 - Condition Code (24-30) (CWE) O rep S6.5.11.3 | 0043 - Condition Code

    ub2_4 : str | None
        UB2.4 - Covered Days (7) (ST) O S6.5.11.4

    ub2_5 : str | None
        UB2.5 - Non-Covered Days (8) (ST) O S6.5.11.5

    ub2_6 : list[UVC] | None
        UB2.6 - Value Amount & Code (39-41) (UVC) O rep S6.5.11.6

    ub2_7 : list[OCD] | None
        UB2.7 - Occurrence Code & Date (32-35) (OCD) O rep S6.5.11.7

    ub2_8 : list[OSP] | None
        UB2.8 - Occurrence Span Code/Dates (36) (OSP) O rep S6.5.11.8

    ub2_9 : list[str] | None
        UB2.9 - Uniform Billing Locator 2 (state) (ST) O rep S6.5.11.9

    ub2_10 : list[str] | None
        UB2.10 - Uniform Billing Locator 11 (state) (ST) O rep S6.5.11.10

    ub2_11 : str | None
        UB2.11 - Uniform Billing Locator 31 (national) (ST) O S6.5.11.11

    ub2_12 : list[str] | None
        UB2.12 - Document Control Number (ST) O rep S6.5.11.12

    ub2_13 : list[str] | None
        UB2.13 - Uniform Billing Locator 49 (national) (ST) O rep S6.5.11.13

    ub2_14 : list[str] | None
        UB2.14 - Uniform Billing Locator 56 (state) (ST) O rep S6.5.11.14

    ub2_15 : str | None
        UB2.15 - Uniform Billing Locator 57 (sational) (ST) O S6.5.11.15

    ub2_16 : list[str] | None
        UB2.16 - Uniform Billing Locator 78 (state) (ST) O rep S6.5.11.16

    ub2_17 : str | None
        UB2.17 - Special Visit Count (NM) O S6.5.11.17
    """

    ub2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_1",
            "set_id_ub2",
            "UB2.1",
        ),
        serialization_alias="UB2.1",
        title="Set ID - UB2",
        description="O | Item #00553 | LEN:4",
    )

    ub2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_2",
            "co_insurance_days_9",
            "UB2.2",
        ),
        serialization_alias="UB2.2",
        title="Co-Insurance Days (9)",
        description="O | Item #00554 | LEN:3",
    )

    ub2_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_3",
            "condition_code_24_30",
            "UB2.3",
        ),
        serialization_alias="UB2.3",
        title="Condition Code (24-30)",
        description="O | Item #00555 | Table 0043 - Condition Code",
    )

    ub2_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_4",
            "covered_days_7",
            "UB2.4",
        ),
        serialization_alias="UB2.4",
        title="Covered Days (7)",
        description="O | Item #00556 | LEN:3",
    )

    ub2_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_5",
            "non_covered_days_8",
            "UB2.5",
        ),
        serialization_alias="UB2.5",
        title="Non-Covered Days (8)",
        description="O | Item #00557 | LEN:4",
    )

    ub2_6: Optional[List[UVC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_6",
            "value_amount_code_39_41",
            "UB2.6",
        ),
        serialization_alias="UB2.6",
        title="Value Amount & Code (39-41)",
        description="O | Item #00558",
    )

    ub2_7: Optional[List[OCD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_7",
            "occurrence_code_date_32_35",
            "UB2.7",
        ),
        serialization_alias="UB2.7",
        title="Occurrence Code & Date (32-35)",
        description="O | Item #00559",
    )

    ub2_8: Optional[List[OSP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_8",
            "occurrence_span_code_dates_36",
            "UB2.8",
        ),
        serialization_alias="UB2.8",
        title="Occurrence Span Code/Dates (36)",
        description="O | Item #00560",
    )

    ub2_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_9",
            "uniform_billing_locator_2_state",
            "UB2.9",
        ),
        serialization_alias="UB2.9",
        title="Uniform Billing Locator 2 (state)",
        description="O | Item #00561 | LEN:29",
    )

    ub2_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_10",
            "uniform_billing_locator_11_state",
            "UB2.10",
        ),
        serialization_alias="UB2.10",
        title="Uniform Billing Locator 11 (state)",
        description="O | Item #00562 | LEN:12",
    )

    ub2_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_11",
            "uniform_billing_locator_31_national",
            "UB2.11",
        ),
        serialization_alias="UB2.11",
        title="Uniform Billing Locator 31 (national)",
        description="O | Item #00563 | LEN:5",
    )

    ub2_12: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_12",
            "document_control_number",
            "UB2.12",
        ),
        serialization_alias="UB2.12",
        title="Document Control Number",
        description="O | Item #00564 | LEN:23",
    )

    ub2_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_13",
            "uniform_billing_locator_49_national",
            "UB2.13",
        ),
        serialization_alias="UB2.13",
        title="Uniform Billing Locator 49 (national)",
        description="O | Item #00565 | LEN:4",
    )

    ub2_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_14",
            "uniform_billing_locator_56_state",
            "UB2.14",
        ),
        serialization_alias="UB2.14",
        title="Uniform Billing Locator 56 (state)",
        description="O | Item #00566 | LEN:14",
    )

    ub2_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_15",
            "uniform_billing_locator_57_sational",
            "UB2.15",
        ),
        serialization_alias="UB2.15",
        title="Uniform Billing Locator 57 (sational)",
        description="O | Item #00567 | LEN:27",
    )

    ub2_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_16",
            "uniform_billing_locator_78_state",
            "UB2.16",
        ),
        serialization_alias="UB2.16",
        title="Uniform Billing Locator 78 (state)",
        description="O | Item #00568 | LEN:2",
    )

    ub2_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_17",
            "special_visit_count",
            "UB2.17",
        ),
        serialization_alias="UB2.17",
        title="Special Visit Count",
        description="O | Item #00815 | LEN:3",
    )

    @field_validator("ub2_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ub2_17", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
