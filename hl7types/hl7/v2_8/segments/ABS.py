"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ABS
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.XCN import XCN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class ABS(HL7Model):
    """Abstract (S6.5.12).

    Attributes
    ----------
    abs_1 : XCN | None
        ABS.1 - Discharge Care Provider (XCN) O S6.5.12.1 | 0010 - Physician ID

    abs_2 : CWE | None
        ABS.2 - Transfer Medical Service Code (CWE) O S6.5.12.2 | 0069 - Hospital Service

    abs_3 : CWE | None
        ABS.3 - Severity of Illness Code (CWE) O S6.5.12.3 | 0421 - Severity of Illness Code

    abs_4 : str | None
        ABS.4 - Date/Time of Attestation (DTM) O S6.5.12.4

    abs_5 : XCN | None
        ABS.5 - Attested By (XCN) O S6.5.12.5

    abs_6 : CWE | None
        ABS.6 - Triage Code (CWE) O S6.5.12.6 | 0422 - Triage Code

    abs_7 : str | None
        ABS.7 - Abstract Completion Date/Time (DTM) O S6.5.12.7

    abs_8 : XCN | None
        ABS.8 - Abstracted By (XCN) O S6.5.12.8

    abs_9 : CWE | None
        ABS.9 - Case Category Code (CWE) O S6.5.12.9 | 0423 - Case Category Code

    abs_10 : str | None
        ABS.10 - Caesarian Section Indicator (ID) O S6.5.12.10 | 0136 - Yes/no Indicator

    abs_11 : CWE | None
        ABS.11 - Gestation Category Code (CWE) O S6.5.12.11 | 0424 - Gestation Category Code

    abs_12 : str | None
        ABS.12 - Gestation Period - Weeks (NM) O S6.5.12.12

    abs_13 : CWE | None
        ABS.13 - Newborn Code (CWE) O S6.5.12.13 | 0425 - Newborn Code

    abs_14 : str | None
        ABS.14 - Stillborn Indicator (ID) O S6.5.12.14 | 0136 - Yes/no Indicator
    """

    abs_1: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_1",
            "discharge_care_provider",
            "ABS.1",
        ),
        serialization_alias="ABS.1",
        title="Discharge Care Provider",
        description="O | Item #01514 | Table 0010 - Physician ID",
    )

    abs_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_2",
            "transfer_medical_service_code",
            "ABS.2",
        ),
        serialization_alias="ABS.2",
        title="Transfer Medical Service Code",
        description="O | Item #01515 | Table 0069 - Hospital Service",
    )

    abs_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_3",
            "severity_of_illness_code",
            "ABS.3",
        ),
        serialization_alias="ABS.3",
        title="Severity of Illness Code",
        description="O | Item #01516 | Table 0421 - Severity of Illness Code",
    )

    abs_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_4",
            "date_time_of_attestation",
            "ABS.4",
        ),
        serialization_alias="ABS.4",
        title="Date/Time of Attestation",
        description="O | Item #01517",
    )

    abs_5: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_5",
            "attested_by",
            "ABS.5",
        ),
        serialization_alias="ABS.5",
        title="Attested By",
        description="O | Item #01518",
    )

    abs_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_6",
            "triage_code",
            "ABS.6",
        ),
        serialization_alias="ABS.6",
        title="Triage Code",
        description="O | Item #01519 | Table 0422 - Triage Code",
    )

    abs_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_7",
            "abstract_completion_date_time",
            "ABS.7",
        ),
        serialization_alias="ABS.7",
        title="Abstract Completion Date/Time",
        description="O | Item #01520",
    )

    abs_8: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_8",
            "abstracted_by",
            "ABS.8",
        ),
        serialization_alias="ABS.8",
        title="Abstracted By",
        description="O | Item #01521",
    )

    abs_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_9",
            "case_category_code",
            "ABS.9",
        ),
        serialization_alias="ABS.9",
        title="Case Category Code",
        description="O | Item #01522 | Table 0423 - Case Category Code",
    )

    abs_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_10",
            "caesarian_section_indicator",
            "ABS.10",
        ),
        serialization_alias="ABS.10",
        title="Caesarian Section Indicator",
        description="O | Item #01523 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    abs_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_11",
            "gestation_category_code",
            "ABS.11",
        ),
        serialization_alias="ABS.11",
        title="Gestation Category Code",
        description="O | Item #01524 | Table 0424 - Gestation Category Code",
    )

    abs_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_12",
            "gestation_period_weeks",
            "ABS.12",
        ),
        serialization_alias="ABS.12",
        title="Gestation Period - Weeks",
        description="O | Item #01525",
    )

    abs_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_13",
            "newborn_code",
            "ABS.13",
        ),
        serialization_alias="ABS.13",
        title="Newborn Code",
        description="O | Item #01526 | Table 0425 - Newborn Code",
    )

    abs_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "abs_14",
            "stillborn_indicator",
            "ABS.14",
        ),
        serialization_alias="ABS.14",
        title="Stillborn Indicator",
        description="O | Item #01527 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    @field_validator("abs_4", "abs_7", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("abs_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
