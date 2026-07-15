"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: UB2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class UB2(HL7Model):
    """UB92 DATA (S6.4.10).

    Attributes
    ----------
    ub2_1 : str | None
        UB2.1 - Set ID - UB92 (SI) NA S6.4.10.1

    ub2_2 : str | None
        UB2.2 - Co-insurance days (9) (ST) NA S6.4.10.2

    ub2_3 : list[str] | None
        UB2.3 - Condition code (24-30) (ID) NA rep S6.4.10.3 | 0043 - CONDITION CODE

    ub2_4 : str | None
        UB2.4 - Covered days (7) (ST) NA S6.4.10.4

    ub2_5 : str | None
        UB2.5 - Non-covered days (8) (ST) NA S6.4.10.5

    ub2_6 : list[str] | None
        UB2.6 - Value amount and code (39-41) (CM) NA rep S6.4.10.6

    ub2_7 : list[str] | None
        UB2.7 - Occurrence code and date (32-35) (CM) NA rep S6.4.10.7

    ub2_8 : list[str] | None
        UB2.8 - Occurrence span code / dates (36) (CM) NA rep S6.4.10.8

    ub2_9 : list[str] | None
        UB2.9 - UB92 locator 2 (state) (ST) NA rep S6.4.10.9

    ub2_10 : list[str] | None
        UB2.10 - UB92 locator 11 (state) (ST) NA rep S6.4.10.10

    ub2_11 : str | None
        UB2.11 - UB92 locator 31 (national) (ST) NA S6.4.10.11

    ub2_12 : list[str] | None
        UB2.12 - Document control number (37) (ST) NA rep S6.4.10.12

    ub2_13 : list[str] | None
        UB2.13 - UB92 locator 49 (national) (ST) NA rep S6.4.10.13

    ub2_14 : list[str] | None
        UB2.14 - UB92 locator 56 (state) (ST) NA rep S6.4.10.14

    ub2_15 : str | None
        UB2.15 - UB92 locator 57 (national) (ST) NA S6.4.10.15

    ub2_16 : list[str] | None
        UB2.16 - UB92 Locator 78 (state) (ST) NA rep S6.4.10.16
    """

    ub2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_1",
            "set_id_ub92",
            "UB2.1",
        ),
        serialization_alias="UB2.1",
        title="Set ID - UB92",
        description="NA | Item #00553 | LEN:4",
    )

    ub2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_2",
            "co_insurance_days_9",
            "UB2.2",
        ),
        serialization_alias="UB2.2",
        title="Co-insurance days (9)",
        description="NA | Item #00554 | LEN:3",
    )

    ub2_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_3",
            "condition_code_24_30",
            "UB2.3",
        ),
        serialization_alias="UB2.3",
        title="Condition code (24-30)",
        description="NA | Item #00555 | Table 0043 - CONDITION CODE | LEN:2",
    )

    ub2_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_4",
            "covered_days_7",
            "UB2.4",
        ),
        serialization_alias="UB2.4",
        title="Covered days (7)",
        description="NA | Item #00556 | LEN:3",
    )

    ub2_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_5",
            "non_covered_days_8",
            "UB2.5",
        ),
        serialization_alias="UB2.5",
        title="Non-covered days (8)",
        description="NA | Item #00557 | LEN:4",
    )

    ub2_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_6",
            "value_amount_and_code_39_41",
            "UB2.6",
        ),
        serialization_alias="UB2.6",
        title="Value amount and code (39-41)",
        description="NA | Item #00558",
    )

    ub2_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_7",
            "occurrence_code_and_date_32_35",
            "UB2.7",
        ),
        serialization_alias="UB2.7",
        title="Occurrence code and date (32-35)",
        description="NA | Item #00559",
    )

    ub2_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_8",
            "occurrence_span_code_dates_36",
            "UB2.8",
        ),
        serialization_alias="UB2.8",
        title="Occurrence span code / dates (36)",
        description="NA | Item #00560",
    )

    ub2_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_9",
            "ub92_locator_2_state",
            "UB2.9",
        ),
        serialization_alias="UB2.9",
        title="UB92 locator 2 (state)",
        description="NA | Item #00561 | LEN:29",
    )

    ub2_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_10",
            "ub92_locator_11_state",
            "UB2.10",
        ),
        serialization_alias="UB2.10",
        title="UB92 locator 11 (state)",
        description="NA | Item #00562 | LEN:12",
    )

    ub2_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_11",
            "ub92_locator_31_national",
            "UB2.11",
        ),
        serialization_alias="UB2.11",
        title="UB92 locator 31 (national)",
        description="NA | Item #00563 | LEN:5",
    )

    ub2_12: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_12",
            "document_control_number_37",
            "UB2.12",
        ),
        serialization_alias="UB2.12",
        title="Document control number (37)",
        description="NA | Item #00564 | LEN:23",
    )

    ub2_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_13",
            "ub92_locator_49_national",
            "UB2.13",
        ),
        serialization_alias="UB2.13",
        title="UB92 locator 49 (national)",
        description="NA | Item #00565 | LEN:4",
    )

    ub2_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_14",
            "ub92_locator_56_state",
            "UB2.14",
        ),
        serialization_alias="UB2.14",
        title="UB92 locator 56 (state)",
        description="NA | Item #00566 | LEN:14",
    )

    ub2_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_15",
            "ub92_locator_57_national",
            "UB2.15",
        ),
        serialization_alias="UB2.15",
        title="UB92 locator 57 (national)",
        description="NA | Item #00567 | LEN:27",
    )

    ub2_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_16",
            "ub92_locator_78_state",
            "UB2.16",
        ),
        serialization_alias="UB2.16",
        title="UB92 Locator 78 (state)",
        description="NA | Item #00568 | LEN:2",
    )

    @field_validator("ub2_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
