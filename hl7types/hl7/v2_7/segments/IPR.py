"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: IPR
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class IPR(BaseModel):
    """HL7 v2 IPR segment."""

    ipr_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipr_1",
            "ipr_identifier",
            "IPR.1",
        ),
        serialization_alias="IPR.1",
        title="IPR Identifier",
        description="Item #2030",
    )

    ipr_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipr_2",
            "provider_cross_reference_identifier",
            "IPR.2",
        ),
        serialization_alias="IPR.2",
        title="Provider Cross Reference Identifier",
        description="Item #2031",
    )

    ipr_3: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipr_3",
            "payer_cross_reference_identifier",
            "IPR.3",
        ),
        serialization_alias="IPR.3",
        title="Payer Cross Reference Identifier",
        description="Item #2032",
    )

    ipr_4: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipr_4",
            "ipr_status",
            "IPR.4",
        ),
        serialization_alias="IPR.4",
        title="IPR Status",
        description="Item #2033 | Table HL70571",
    )

    ipr_5: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipr_5",
            "ipr_date_time",
            "IPR.5",
        ),
        serialization_alias="IPR.5",
        title="IPR Date/Time",
        description="Item #2034",
    )

    ipr_6: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipr_6",
            "adjudicated_paid_amount",
            "IPR.6",
        ),
        serialization_alias="IPR.6",
        title="Adjudicated/Paid Amount",
        description="Item #2035",
    )

    ipr_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipr_7",
            "expected_payment_date_time",
            "IPR.7",
        ),
        serialization_alias="IPR.7",
        title="Expected Payment Date/Time",
        description="Item #2036",
    )

    ipr_8: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ipr_8",
            "ipr_checksum",
            "IPR.8",
        ),
        serialization_alias="IPR.8",
        title="IPR Checksum",
        description="Item #2037",
    )

    model_config = {"populate_by_name": True}
