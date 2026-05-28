"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PYE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN


class PYE(BaseModel):
    """HL7 v2 PYE segment."""

    pye_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pye_1",
            "set_id_pye",
            "PYE.1",
        ),
        serialization_alias="PYE.1",
        title="Set ID - PYE",
        description="Item #1939",
    )

    pye_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pye_2",
            "payee_type",
            "PYE.2",
        ),
        serialization_alias="PYE.2",
        title="Payee Type",
        description="Item #1940 | Table HL70557",
    )

    pye_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pye_3",
            "payee_relationship_to_invoice_patient",
            "PYE.3",
        ),
        serialization_alias="PYE.3",
        title="Payee Relationship to Invoice (Patient)",
        description="Item #1941 | Table HL70558",
    )

    pye_4: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pye_4",
            "payee_identification_list",
            "PYE.4",
        ),
        serialization_alias="PYE.4",
        title="Payee Identification List",
        description="Item #1942",
    )

    pye_5: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pye_5",
            "payee_person_name",
            "PYE.5",
        ),
        serialization_alias="PYE.5",
        title="Payee Person Name",
        description="Item #1943",
    )

    pye_6: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pye_6",
            "payee_address",
            "PYE.6",
        ),
        serialization_alias="PYE.6",
        title="Payee Address",
        description="Item #1944",
    )

    pye_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pye_7",
            "payment_method",
            "PYE.7",
        ),
        serialization_alias="PYE.7",
        title="Payment Method",
        description="Item #1945 | Table HL70570",
    )

    model_config = {"populate_by_name": True}
