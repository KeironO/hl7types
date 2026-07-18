"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: URD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.XCN import XCN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class URD(HL7Model):
    """Results/update Definition (S5.10.4.3).

    Attributes
    ----------
    urd_1 : str | None
        URD.1 - R/U Date/Time (DTM) O S5.10.4.3.1

    urd_2 : str | None
        URD.2 - Report Priority (ID) O S5.10.4.3.2 | 0109 - Report priority

    urd_3 : list[XCN]
        URD.3 - R/U Who Subject Definition (XCN) R rep S5.10.4.3.3

    urd_4 : list[CWE] | None
        URD.4 - R/U What Subject Definition (CWE) O rep S5.10.4.3.4 | 0048 - What subject filter

    urd_5 : list[CWE] | None
        URD.5 - R/U What Department Code (CWE) O rep S5.10.4.3.5

    urd_6 : list[str] | None
        URD.6 - R/U Display/Print Locations (ST) O rep S5.10.4.3.6

    urd_7 : str | None
        URD.7 - R/U Results Level (ID) O S5.10.4.3.7 | 0108 - Query results level
    """

    urd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_1",
            "r_u_date_time",
            "URD.1",
        ),
        serialization_alias="URD.1",
        title="R/U Date/Time",
        description="O | Item #00045 | LEN:24",
    )

    urd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_2",
            "report_priority",
            "URD.2",
        ),
        serialization_alias="URD.2",
        title="Report Priority",
        description="O | Item #00046 | Table 0109 - Report priority | LEN:1",
    )

    urd_3: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "urd_3",
            "r_u_who_subject_definition",
            "URD.3",
        ),
        serialization_alias="URD.3",
        title="R/U Who Subject Definition",
        description="R | Item #00047",
    )

    urd_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_4",
            "r_u_what_subject_definition",
            "URD.4",
        ),
        serialization_alias="URD.4",
        title="R/U What Subject Definition",
        description="O | Item #00048 | Table 0048 - What subject filter",
    )

    urd_5: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_5",
            "r_u_what_department_code",
            "URD.5",
        ),
        serialization_alias="URD.5",
        title="R/U What Department Code",
        description="O | Item #00049",
    )

    urd_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_6",
            "r_u_display_print_locations",
            "URD.6",
        ),
        serialization_alias="URD.6",
        title="R/U Display/Print Locations",
        description="O | Item #00050 | LEN:20",
    )

    urd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_7",
            "r_u_results_level",
            "URD.7",
        ),
        serialization_alias="URD.7",
        title="R/U Results Level",
        description=(
            "O | Item #00051 | Table 0108 - Query results level | LEN:1"
        ),
    )

    @field_validator("urd_1", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
