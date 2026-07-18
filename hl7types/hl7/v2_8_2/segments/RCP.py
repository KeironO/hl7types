"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RCP
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CQ import CQ
from ..datatypes.SRT import SRT

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class RCP(HL7Model):
    """Response Control Parameter (S5.5.6).

    Attributes
    ----------
    rcp_1 : str | None
        RCP.1 - Query Priority (ID) O S5.5.6.1 | 0091 - Query Priority

    rcp_2 : CQ | None
        RCP.2 - Quantity Limited Request (CQ) O S5.5.6.2 | 0126 - Quantity Limited Request

    rcp_3 : CNE | None
        RCP.3 - Response Modality (CNE) O S5.5.6.3 | 0394 - Response Modality

    rcp_4 : str | None
        RCP.4 - Execution and Delivery Time (DTM) C S5.5.6.4

    rcp_5 : str | None
        RCP.5 - Modify Indicator (ID) O S5.5.6.5 | 0395 - Modify Indicator

    rcp_6 : list[SRT] | None
        RCP.6 - Sort-by Field (SRT) O rep S5.5.6.6

    rcp_7 : list[str] | None
        RCP.7 - Segment group inclusion (ID) O rep S5.5.6.7 | 0391 - Segment Group
    """

    rcp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_1",
            "query_priority",
            "RCP.1",
        ),
        serialization_alias="RCP.1",
        title="Query Priority",
        description="O | Item #00027 | Table 0091 - Query Priority | LEN:1",
    )

    rcp_2: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_2",
            "quantity_limited_request",
            "RCP.2",
        ),
        serialization_alias="RCP.2",
        title="Quantity Limited Request",
        description="O | Item #00031 | Table 0126 - Quantity Limited Request",
    )

    rcp_3: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_3",
            "response_modality",
            "RCP.3",
        ),
        serialization_alias="RCP.3",
        title="Response Modality",
        description="O | Item #01440 | Table 0394 - Response Modality",
    )

    rcp_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_4",
            "execution_and_delivery_time",
            "RCP.4",
        ),
        serialization_alias="RCP.4",
        title="Execution and Delivery Time",
        description="C | Item #01441",
    )

    rcp_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_5",
            "modify_indicator",
            "RCP.5",
        ),
        serialization_alias="RCP.5",
        title="Modify Indicator",
        description="O | Item #01443 | Table 0395 - Modify Indicator | LEN:1",
    )

    rcp_6: Optional[List[SRT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_6",
            "sort_by_field",
            "RCP.6",
        ),
        serialization_alias="RCP.6",
        title="Sort-by Field",
        description="O | Item #01624",
    )

    rcp_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_7",
            "segment_group_inclusion",
            "RCP.7",
        ),
        serialization_alias="RCP.7",
        title="Segment group inclusion",
        description="O | Item #01594 | Table 0391 - Segment Group | LEN:256",
    )

    @field_validator("rcp_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
