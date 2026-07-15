"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
    """Override Segment (S2.14.11).

    Attributes
    ----------
    ovr_1 : CWE | None
        OVR.1 - Business Rule Override Type (CWE) O S2.14.11.1 | 0518 - Override Type

    ovr_2 : CWE | None
        OVR.2 - Business Rule Override Code (CWE) O S2.14.11.2 | 0521 - Override Code

    ovr_3 : str | None
        OVR.3 - Override Comments (TX) O S2.14.11.3

    ovr_4 : XCN | None
        OVR.4 - Override Entered By (XCN) O S2.14.11.4

    ovr_5 : XCN | None
        OVR.5 - Override Authorized By (XCN) O S2.14.11.5
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
        description="O | Item #01829 | Table 0518 - Override Type",
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
        description="O | Item #01830 | Table 0521 - Override Code",
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
        description="O | Item #01831",
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
        description="O | Item #01832",
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
        description="O | Item #01833",
    )

    model_config = {"populate_by_name": True}
