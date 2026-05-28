"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: FAC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class FAC(BaseModel):
    """HL7 v2 FAC segment."""

    fac_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "fac_1",
            "facility_id_fac",
            "FAC.1",
        ),
        serialization_alias="FAC.1",
        title="Facility ID-FAC",
        description="Item #1262",
    )

    fac_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_2",
            "facility_type",
            "FAC.2",
        ),
        serialization_alias="FAC.2",
        title="Facility Type",
        description="Item #1263 | Table HL70331",
    )

    fac_3: list[XAD] = Field(
        default=...,
        validation_alias=AliasChoices(
            "fac_3",
            "facility_address",
            "FAC.3",
        ),
        serialization_alias="FAC.3",
        title="Facility Address",
        description="Item #1264",
    )

    fac_4: XTN = Field(
        default=...,
        validation_alias=AliasChoices(
            "fac_4",
            "facility_telecommunication",
            "FAC.4",
        ),
        serialization_alias="FAC.4",
        title="Facility Telecommunication",
        description="Item #1265",
    )

    fac_5: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_5",
            "contact_person",
            "FAC.5",
        ),
        serialization_alias="FAC.5",
        title="Contact Person",
        description="Item #1266",
    )

    fac_6: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_6",
            "contact_title",
            "FAC.6",
        ),
        serialization_alias="FAC.6",
        title="Contact Title",
        description="Item #1267",
    )

    fac_7: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_7",
            "contact_address",
            "FAC.7",
        ),
        serialization_alias="FAC.7",
        title="Contact Address",
        description="Item #1166",
    )

    fac_8: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_8",
            "contact_telecommunication",
            "FAC.8",
        ),
        serialization_alias="FAC.8",
        title="Contact Telecommunication",
        description="Item #1269",
    )

    fac_9: list[XCN] = Field(
        default=...,
        validation_alias=AliasChoices(
            "fac_9",
            "signature_authority",
            "FAC.9",
        ),
        serialization_alias="FAC.9",
        title="Signature Authority",
        description="Item #1270",
    )

    fac_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_10",
            "signature_authority_title",
            "FAC.10",
        ),
        serialization_alias="FAC.10",
        title="Signature Authority Title",
        description="Item #1271",
    )

    fac_11: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_11",
            "signature_authority_address",
            "FAC.11",
        ),
        serialization_alias="FAC.11",
        title="Signature Authority Address",
        description="Item #1272",
    )

    fac_12: XTN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_12",
            "signature_authority_telecommunication",
            "FAC.12",
        ),
        serialization_alias="FAC.12",
        title="Signature Authority Telecommunication",
        description="Item #1273",
    )

    model_config = {"populate_by_name": True}
