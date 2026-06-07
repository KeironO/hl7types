"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OVR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.XCN import XCN


class OVR(HL7Model):
    """HL7 v2 OVR segment.

    Attributes
    ----------
    ovr_1 : CWE | None
        OVR.1 (opt) - Business Rule Override Type (CWE)

    ovr_2 : CWE | None
        OVR.2 (opt) - Business Rule Override Code (CWE)

    ovr_3 : str | None
        OVR.3 (opt) - Override Comments (TX)

    ovr_4 : XCN | None
        OVR.4 (opt) - Override Entered By (XCN)

    ovr_5 : XCN | None
        OVR.5 (opt) - Override Authorized By (XCN)
    """

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

    ovr_3: Optional[str] = Field(
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
