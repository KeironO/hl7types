"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RQD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX


class RQD(HL7Model):
    """Requisition Detail (S4.11.1).

    Attributes
    ----------
    rqd_1 : str | None
        RQD.1 - Requisition Line Number (SI) O S4.11.1.1

    rqd_2 : CWE | None
        RQD.2 - Item Code - Internal (CWE) C S4.11.1.2 | 9999 - no table for CE

    rqd_3 : CWE | None
        RQD.3 - Item Code - External (CWE) C S4.11.1.3 | 9999 - no table for CE

    rqd_4 : CWE | None
        RQD.4 - Hospital Item Code (CWE) C S4.11.1.4 | 9999 - no table for CE

    rqd_5 : str | None
        RQD.5 - Requisition Quantity (NM) O S4.11.1.5

    rqd_6 : CWE | None
        RQD.6 - Requisition Unit of Measure (CWE) O S4.11.1.6 | 9999 - no table for CE

    rqd_7 : CX | None
        RQD.7 - Cost Center Account Number (CX) O S17.4.6.2 | 0319 - Department Cost Center

    rqd_8 : CWE | None
        RQD.8 - Item Natural Account Code (CWE) O S17.4.2.19 | 0320 - Item Natural Account Code

    rqd_9 : CWE | None
        RQD.9 - Deliver To ID (CWE) O S4.11.1.9 | 9999 - no table for CE

    rqd_10 : str | None
        RQD.10 - Date Needed (DT) O S4.11.1.10
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
        description="O | Item #00275 | LEN:4",
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
        description="C | Item #00276 | Table 9999 - no table for CE",
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
        description="C | Item #00277 | Table 9999 - no table for CE",
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
        description="C | Item #00278 | Table 9999 - no table for CE",
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
        description="O | Item #00279",
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
        description="O | Item #00280 | Table 9999 - no table for CE",
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
        description="O | Item #00281 | Table 0319 - Department Cost Center",
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
        description="O | Item #00282 | Table 0320 - Item Natural Account Code",
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
        description="O | Item #00283 | Table 9999 - no table for CE",
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
        description="O | Item #00284",
    )

    @field_validator("rqd_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("rqd_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("rqd_10", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
