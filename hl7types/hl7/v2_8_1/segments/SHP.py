"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SHP
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class SHP(HL7Model):
    """Shipment (S7.18.2).

    Attributes
    ----------
    shp_1 : EI
        SHP.1 - Shipment ID (EI) R S7.18.2.1

    shp_2 : list[EI] | None
        SHP.2 - Internal Shipment ID (EI) O rep S7.18.2.2

    shp_3 : CWE | None
        SHP.3 - Shipment Status (CWE) O S7.18.2.3 | 0905 - Shipment Status

    shp_4 : str
        SHP.4 - Shipment Status Date/Time (DTM) R S7.18.2.4

    shp_5 : str | None
        SHP.5 - Shipment Status Reason (TX) O S7.18.2.5

    shp_6 : CWE | None
        SHP.6 - Shipment Priority (CWE) O S7.18.2.6 | 0906 - ActPriority

    shp_7 : list[CWE] | None
        SHP.7 - Shipment Confidentiality (CWE) O rep S7.18.2.7 | 0907 - Confidentiality

    shp_8 : str | None
        SHP.8 - Number of Packages in Shipment (NM) O S7.18.2.8

    shp_9 : list[CWE] | None
        SHP.9 - Shipment Condition (CWE) O rep S7.18.2.9 | 0544 - Container Condition

    shp_10 : list[CWE] | None
        SHP.10 - Shipment Handling Code (CWE) O rep S7.18.2.10 | 0376 - Special Handling Code

    shp_11 : list[CWE] | None
        SHP.11 - Shipment Risk Code (CWE) O rep S7.18.2.11 | 0489 - Risk Codes
    """

    shp_1: EI = Field(
        validation_alias=AliasChoices(
            "shp_1",
            "shipment_id",
            "SHP.1",
        ),
        serialization_alias="SHP.1",
        title="Shipment ID",
        description="R | Item #02317",
    )

    shp_2: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_2",
            "internal_shipment_id",
            "SHP.2",
        ),
        serialization_alias="SHP.2",
        title="Internal Shipment ID",
        description="O | Item #02318",
    )

    shp_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_3",
            "shipment_status",
            "SHP.3",
        ),
        serialization_alias="SHP.3",
        title="Shipment Status",
        description="O | Item #02319 | Table 0905 - Shipment Status",
    )

    shp_4: str = Field(
        validation_alias=AliasChoices(
            "shp_4",
            "shipment_status_date_time",
            "SHP.4",
        ),
        serialization_alias="SHP.4",
        title="Shipment Status Date/Time",
        description="R | Item #02320",
    )

    shp_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_5",
            "shipment_status_reason",
            "SHP.5",
        ),
        serialization_alias="SHP.5",
        title="Shipment Status Reason",
        description="O | Item #02321",
    )

    shp_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_6",
            "shipment_priority",
            "SHP.6",
        ),
        serialization_alias="SHP.6",
        title="Shipment Priority",
        description="O | Item #02322 | Table 0906 - ActPriority",
    )

    shp_7: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_7",
            "shipment_confidentiality",
            "SHP.7",
        ),
        serialization_alias="SHP.7",
        title="Shipment Confidentiality",
        description="O | Item #02323 | Table 0907 - Confidentiality",
    )

    shp_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_8",
            "number_of_packages_in_shipment",
            "SHP.8",
        ),
        serialization_alias="SHP.8",
        title="Number of Packages in Shipment",
        description="O | Item #02324",
    )

    shp_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_9",
            "shipment_condition",
            "SHP.9",
        ),
        serialization_alias="SHP.9",
        title="Shipment Condition",
        description="O | Item #02325 | Table 0544 - Container Condition",
    )

    shp_10: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_10",
            "shipment_handling_code",
            "SHP.10",
        ),
        serialization_alias="SHP.10",
        title="Shipment Handling Code",
        description="O | Item #02326 | Table 0376 - Special Handling Code",
    )

    shp_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_11",
            "shipment_risk_code",
            "SHP.11",
        ),
        serialization_alias="SHP.11",
        title="Shipment Risk Code",
        description="O | Item #02327 | Table 0489 - Risk Codes",
    )

    @field_validator("shp_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("shp_8", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
