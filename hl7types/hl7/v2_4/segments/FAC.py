"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: FAC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class FAC(HL7Model):
    """HL7 v2 FAC segment.

    Attributes
    ----------
    fac_1 : EI
        FAC.1 (req) - Facility ID-FAC (EI)

    fac_2 : str | None
        FAC.2 (opt) - Facility Type (ID)

    fac_3 : list[XAD] | None
        FAC.3 (req, rep) - Facility Address (XAD) [optional: XAD has no required components]

    fac_4 : XTN
        FAC.4 (req) - Facility Telecommunication (XTN)

    fac_5 : list[XCN] | None
        FAC.5 (opt, rep) - Contact Person (XCN)

    fac_6 : list[str] | None
        FAC.6 (opt, rep) - Contact Title (ST)

    fac_7 : list[XAD] | None
        FAC.7 (opt, rep) - Contact Address (XAD)

    fac_8 : list[XTN] | None
        FAC.8 (opt, rep) - Contact Telecommunication (XTN)

    fac_9 : list[XCN] | None
        FAC.9 (req, rep) - Signature Authority (XCN) [optional: XCN has no required components]

    fac_10 : str | None
        FAC.10 (opt) - Signature Authority Title (ST)

    fac_11 : list[XAD] | None
        FAC.11 (opt, rep) - Signature Authority Address (XAD)

    fac_12 : XTN | None
        FAC.12 (opt) - Signature Authority Telecommunication (XTN)
    """

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

    fac_2: Optional[str] = Field(
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

    fac_3: Optional[List[XAD]] = Field(
        default=None,
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

    fac_5: Optional[List[XCN]] = Field(
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

    fac_6: Optional[List[str]] = Field(
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

    fac_7: Optional[List[XAD]] = Field(
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

    fac_8: Optional[List[XTN]] = Field(
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

    fac_9: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fac_9",
            "signature_authority",
            "FAC.9",
        ),
        serialization_alias="FAC.9",
        title="Signature Authority",
        description="Item #1270",
    )

    fac_10: Optional[str] = Field(
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

    fac_11: Optional[List[XAD]] = Field(
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

    fac_12: Optional[XTN] = Field(
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
