"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: AIG
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class AIG(HL7Model):
    """Appointment Information - General Resource (S10.6.5).

    Attributes
    ----------
    aig_1 : str
        AIG.1 - Set ID - AIG (SI) R S10.6.5.1

    aig_2 : str | None
        AIG.2 - Segment Action Code (ID) C S10.6.3.2 | 0206 - Segment action code

    aig_3 : CWE | None
        AIG.3 - Resource ID (CWE) C S10.6.5.3

    aig_4 : CWE
        AIG.4 - Resource Type (CWE) R S10.6.5.4

    aig_5 : list[CWE] | None
        AIG.5 - Resource Group (CWE) O rep S10.6.5.5

    aig_6 : str | None
        AIG.6 - Resource Quantity (NM) O S10.6.5.6

    aig_7 : CNE | None
        AIG.7 - Resource Quantity Units (CNE) O S10.6.5.7

    aig_8 : str | None
        AIG.8 - Start Date/Time (DTM) C S10.6.4.4

    aig_9 : str | None
        AIG.9 - Start Date/Time Offset (NM) C S10.6.4.5

    aig_10 : CNE | None
        AIG.10 - Start Date/Time Offset Units (CNE) C S10.6.4.6

    aig_11 : str | None
        AIG.11 - Duration (NM) O S10.6.4.7

    aig_12 : CNE | None
        AIG.12 - Duration Units (CNE) O S10.6.4.8

    aig_13 : CWE | None
        AIG.13 - Allow Substitution Code (CWE) C S10.6.4.9 | 0279 - Allow Substitution Codes

    aig_14 : CWE | None
        AIG.14 - Filler Status Code (CWE) C S10.6.2.25 | 0278 - Filler status codes
    """

    aig_1: str = Field(
        validation_alias=AliasChoices(
            "aig_1",
            "set_id_aig",
            "AIG.1",
        ),
        serialization_alias="AIG.1",
        title="Set ID - AIG",
        description="R | Item #00896 | LEN:4",
    )

    aig_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_2",
            "segment_action_code",
            "AIG.2",
        ),
        serialization_alias="AIG.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment action code | LEN:1"
        ),
    )

    aig_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_3",
            "resource_id",
            "AIG.3",
        ),
        serialization_alias="AIG.3",
        title="Resource ID",
        description="C | Item #00897",
    )

    aig_4: CWE = Field(
        validation_alias=AliasChoices(
            "aig_4",
            "resource_type",
            "AIG.4",
        ),
        serialization_alias="AIG.4",
        title="Resource Type",
        description="R | Item #00898",
    )

    aig_5: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_5",
            "resource_group",
            "AIG.5",
        ),
        serialization_alias="AIG.5",
        title="Resource Group",
        description="O | Item #00899",
    )

    aig_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_6",
            "resource_quantity",
            "AIG.6",
        ),
        serialization_alias="AIG.6",
        title="Resource Quantity",
        description="O | Item #00900",
    )

    aig_7: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_7",
            "resource_quantity_units",
            "AIG.7",
        ),
        serialization_alias="AIG.7",
        title="Resource Quantity Units",
        description="O | Item #00901",
    )

    aig_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_8",
            "start_date_time",
            "AIG.8",
        ),
        serialization_alias="AIG.8",
        title="Start Date/Time",
        description="C | Item #01202",
    )

    aig_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_9",
            "start_date_time_offset",
            "AIG.9",
        ),
        serialization_alias="AIG.9",
        title="Start Date/Time Offset",
        description="C | Item #00891",
    )

    aig_10: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_10",
            "start_date_time_offset_units",
            "AIG.10",
        ),
        serialization_alias="AIG.10",
        title="Start Date/Time Offset Units",
        description="C | Item #00892",
    )

    aig_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_11",
            "duration",
            "AIG.11",
        ),
        serialization_alias="AIG.11",
        title="Duration",
        description="O | Item #00893",
    )

    aig_12: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_12",
            "duration_units",
            "AIG.12",
        ),
        serialization_alias="AIG.12",
        title="Duration Units",
        description="O | Item #00894",
    )

    aig_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_13",
            "allow_substitution_code",
            "AIG.13",
        ),
        serialization_alias="AIG.13",
        title="Allow Substitution Code",
        description="C | Item #00895 | Table 0279 - Allow Substitution Codes",
    )

    aig_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_14",
            "filler_status_code",
            "AIG.14",
        ),
        serialization_alias="AIG.14",
        title="Filler Status Code",
        description="C | Item #00889 | Table 0278 - Filler status codes",
    )

    @field_validator("aig_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("aig_6", "aig_9", "aig_11", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("aig_8", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
