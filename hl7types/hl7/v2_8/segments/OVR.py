"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OVR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.TX import TX
from ..datatypes.XCN import XCN


class OVR(BaseModel):
    """HL7 v2 OVR segment."""

    ovr_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ovr_1",
            "business_rule_override_type",
            "OVR.1",
        ),
        serialization_alias="OVR.1",
        title="Business Rule Override Type",
        description="Item #1829 | Table HL70518",
    )

    ovr_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ovr_2",
            "business_rule_override_code",
            "OVR.2",
        ),
        serialization_alias="OVR.2",
        title="Business Rule Override Code",
        description="Item #1830 | Table HL70521",
    )

    ovr_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ovr_3",
            "override_comments",
            "OVR.3",
        ),
        serialization_alias="OVR.3",
        title="Override Comments",
        description="Item #1831",
    )

    ovr_4: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ovr_4",
            "override_entered_by",
            "OVR.4",
        ),
        serialization_alias="OVR.4",
        title="Override Entered By",
        description="Item #1832",
    )

    ovr_5: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ovr_5",
            "override_authorized_by",
            "OVR.5",
        ),
        serialization_alias="OVR.5",
        title="Override Authorized By",
        description="Item #1833",
    )

    model_config = {"populate_by_name": True}
