"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
    """Facility (S7.12.6).

    Attributes
    ----------
    fac_1 : EI
        FAC.1 - Facility ID-FAC (EI) R S7.12.6.1

    fac_2 : str | None
        FAC.2 - Facility Type (ID) O S7.12.6.2 | 0331 - Facility Type

    fac_3 : list[XAD]
        FAC.3 - Facility Address (XAD) R rep S7.12.6.3

    fac_4 : XTN
        FAC.4 - Facility Telecommunication (XTN) R S7.12.6.4

    fac_5 : list[XCN] | None
        FAC.5 - Contact Person (XCN) O rep S7.12.6.5

    fac_6 : list[str] | None
        FAC.6 - Contact Title (ST) O rep S7.12.6.6

    fac_7 : list[XAD] | None
        FAC.7 - Contact Address (XAD) O rep S11.8.4.3

    fac_8 : list[XTN] | None
        FAC.8 - Contact Telecommunication (XTN) O rep S7.12.6.8

    fac_9 : list[XCN]
        FAC.9 - Signature Authority (XCN) R rep S7.12.6.9

    fac_10 : str | None
        FAC.10 - Signature Authority Title (ST) O S7.12.6.10

    fac_11 : list[XAD] | None
        FAC.11 - Signature Authority Address (XAD) O rep S7.12.6.11

    fac_12 : XTN | None
        FAC.12 - Signature Authority Telecommunication (XTN) O S7.12.6.12
    """

    fac_1: EI = Field(
        validation_alias=AliasChoices(
            "fac_1",
            "facility_id_fac",
            "FAC.1",
        ),
        serialization_alias="FAC.1",
        title="Facility ID-FAC",
        description="R | Item #01262",
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
        description="O | Item #01263 | Table 0331 - Facility Type | LEN:1",
    )

    fac_3: List[XAD] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "fac_3",
            "facility_address",
            "FAC.3",
        ),
        serialization_alias="FAC.3",
        title="Facility Address",
        description="R | Item #01264",
    )

    fac_4: XTN = Field(
        validation_alias=AliasChoices(
            "fac_4",
            "facility_telecommunication",
            "FAC.4",
        ),
        serialization_alias="FAC.4",
        title="Facility Telecommunication",
        description="R | Item #01265",
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
        description="O | Item #01266",
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
        description="O | Item #01267",
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
        description="O | Item #01166",
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
        description="O | Item #01269",
    )

    fac_9: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "fac_9",
            "signature_authority",
            "FAC.9",
        ),
        serialization_alias="FAC.9",
        title="Signature Authority",
        description="R | Item #01270",
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
        description="O | Item #01271",
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
        description="O | Item #01272",
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
        description="O | Item #01273",
    )

    model_config = {"populate_by_name": True}
