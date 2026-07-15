"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PYE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN


class PYE(HL7Model):
    """Payee Information (S16.4.3).

    Attributes
    ----------
    pye_1 : str
        PYE.1 - Set ID - PYE (SI) R S16.4.3.1

    pye_2 : str
        PYE.2 - Payee Type (IS) R S16.4.3.2 | 0557 - Payee Type

    pye_3 : str | None
        PYE.3 - Payee Relationship to Invoice (Patient) (IS) C S16.4.3.3 | 0558 - Payee Relationship to Invoice

    pye_4 : list[XON] | None
        PYE.4 - Payee Identification List (XON) C rep S16.4.3.4

    pye_5 : list[XPN] | None
        PYE.5 - Payee Person Name (XPN) C rep S16.4.3.5

    pye_6 : list[XAD] | None
        PYE.6 - Payee Address (XAD) C rep S16.4.3.6

    pye_7 : str | None
        PYE.7 - Payment Method (IS) O S16.4.3.7 | 0570 - Payment Method Code
    """

    pye_1: str = Field(
        validation_alias=AliasChoices(
            "pye_1",
            "set_id_pye",
            "PYE.1",
        ),
        serialization_alias="PYE.1",
        title="Set ID - PYE",
        description="R | Item #01939 | LEN:4",
    )

    pye_2: str = Field(
        validation_alias=AliasChoices(
            "pye_2",
            "payee_type",
            "PYE.2",
        ),
        serialization_alias="PYE.2",
        title="Payee Type",
        description="R | Item #01940 | Table 0557 - Payee Type | LEN:6",
    )

    pye_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pye_3",
            "payee_relationship_to_invoice_patient",
            "PYE.3",
        ),
        serialization_alias="PYE.3",
        title="Payee Relationship to Invoice (Patient)",
        description=(
            "C | Item #01941 | Table 0558 - Payee Relationship to Invoice | LEN:2"
        ),
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
        description="C | Item #01942",
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
        description="C | Item #01943",
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
        description="C | Item #01944",
    )

    pye_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pye_7",
            "payment_method",
            "PYE.7",
        ),
        serialization_alias="PYE.7",
        title="Payment Method",
        description=(
            "O | Item #01945 | Table 0570 - Payment Method Code | LEN:80"
        ),
    )

    @field_validator("pye_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
