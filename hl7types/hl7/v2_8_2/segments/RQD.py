"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RQD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX


class RQD(BaseModel):
    """HL7 v2 RQD segment.

    Attributes
    ----------
    rqd_1 : str | None
        RQD.1 (opt) - Requisition Line Number (SI)

    rqd_2 : CWE | None
        RQD.2 (opt) - Item Code - Internal (CWE)

    rqd_3 : CWE | None
        RQD.3 (opt) - Item Code - External (CWE)

    rqd_4 : CWE | None
        RQD.4 (opt) - Hospital Item Code (CWE)

    rqd_5 : str | None
        RQD.5 (opt) - Requisition Quantity (NM)

    rqd_6 : CWE | None
        RQD.6 (opt) - Requisition Unit of Measure (CWE)

    rqd_7 : CX | None
        RQD.7 (opt) - Cost Center Account Number (CX)

    rqd_8 : CWE | None
        RQD.8 (opt) - Item Natural Account Code (CWE)

    rqd_9 : CWE | None
        RQD.9 (opt) - Deliver To ID (CWE)

    rqd_10 : str | None
        RQD.10 (opt) - Date Needed (DT)
    """

    rqd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_1",
            "requisition_line_number",
            "RQD.1",
        ),
        serialization_alias="RQD.1",
        title="Requisition Line Number",
        description="Item #275",
    )

    rqd_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_2",
            "item_code_internal",
            "RQD.2",
        ),
        serialization_alias="RQD.2",
        title="Item Code - Internal",
        description="Item #276 | Table HL79999",
    )

    rqd_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_3",
            "item_code_external",
            "RQD.3",
        ),
        serialization_alias="RQD.3",
        title="Item Code - External",
        description="Item #277 | Table HL79999",
    )

    rqd_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_4",
            "hospital_item_code",
            "RQD.4",
        ),
        serialization_alias="RQD.4",
        title="Hospital Item Code",
        description="Item #278 | Table HL79999",
    )

    rqd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_5",
            "requisition_quantity",
            "RQD.5",
        ),
        serialization_alias="RQD.5",
        title="Requisition Quantity",
        description="Item #279",
    )

    rqd_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_6",
            "requisition_unit_of_measure",
            "RQD.6",
        ),
        serialization_alias="RQD.6",
        title="Requisition Unit of Measure",
        description="Item #280 | Table HL79999",
    )

    rqd_7: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_7",
            "cost_center_account_number",
            "RQD.7",
        ),
        serialization_alias="RQD.7",
        title="Cost Center Account Number",
        description="Item #281 | Table HL70319",
    )

    rqd_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_8",
            "item_natural_account_code",
            "RQD.8",
        ),
        serialization_alias="RQD.8",
        title="Item Natural Account Code",
        description="Item #282 | Table HL70320",
    )

    rqd_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_9",
            "deliver_to_id",
            "RQD.9",
        ),
        serialization_alias="RQD.9",
        title="Deliver To ID",
        description="Item #283 | Table HL79999",
    )

    rqd_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rqd_10",
            "date_needed",
            "RQD.10",
        ),
        serialization_alias="RQD.10",
        title="Date Needed",
        description="Item #284",
    )

    model_config = {"populate_by_name": True}
