"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CM0
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class CM0(HL7Model):
    """HL7 v2 CM0 segment.

    Attributes
    ----------
    cm0_1 : str | None
        CM0.1 (opt) - Set ID - CM0 (SI)

    cm0_2 : EI
        CM0.2 (req) - Sponsor Study ID (EI)

    cm0_3 : list[EI] | None
        CM0.3 (opt, rep) - Alternate Study ID (EI)

    cm0_4 : str
        CM0.4 (req) - Title of Study (ST)

    cm0_5 : list[XCN] | None
        CM0.5 (opt, rep) - Chairman of Study (XCN)

    cm0_6 : str | None
        CM0.6 (opt) - Last IRB Approval Date (DT)

    cm0_7 : str | None
        CM0.7 (opt) - Total Accrual to Date (NM)

    cm0_8 : str | None
        CM0.8 (opt) - Last Accrual Date (DT)

    cm0_9 : list[XCN] | None
        CM0.9 (opt, rep) - Contact for Study (XCN)

    cm0_10 : XTN | None
        CM0.10 (opt) - Contact's Telephone Number (XTN)

    cm0_11 : list[XAD] | None
        CM0.11 (opt, rep) - Contact's Address (XAD)
    """

    cm0_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_1",
            "set_id_cm0",
            "CM0.1",
        ),
        serialization_alias="CM0.1",
        title="Set ID - CM0",
        description="Item #1010",
    )

    cm0_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "cm0_2",
            "sponsor_study_id",
            "CM0.2",
        ),
        serialization_alias="CM0.2",
        title="Sponsor Study ID",
        description="Item #1011",
    )

    cm0_3: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_3",
            "alternate_study_id",
            "CM0.3",
        ),
        serialization_alias="CM0.3",
        title="Alternate Study ID",
        description="Item #1036",
    )

    cm0_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "cm0_4",
            "title_of_study",
            "CM0.4",
        ),
        serialization_alias="CM0.4",
        title="Title of Study",
        description="Item #1013",
    )

    cm0_5: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_5",
            "chairman_of_study",
            "CM0.5",
        ),
        serialization_alias="CM0.5",
        title="Chairman of Study",
        description="Item #1014",
    )

    cm0_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_6",
            "last_irb_approval_date",
            "CM0.6",
        ),
        serialization_alias="CM0.6",
        title="Last IRB Approval Date",
        description="Item #1015",
    )

    cm0_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_7",
            "total_accrual_to_date",
            "CM0.7",
        ),
        serialization_alias="CM0.7",
        title="Total Accrual to Date",
        description="Item #1016",
    )

    cm0_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_8",
            "last_accrual_date",
            "CM0.8",
        ),
        serialization_alias="CM0.8",
        title="Last Accrual Date",
        description="Item #1017",
    )

    cm0_9: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_9",
            "contact_for_study",
            "CM0.9",
        ),
        serialization_alias="CM0.9",
        title="Contact for Study",
        description="Item #1018",
    )

    cm0_10: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_10",
            "contact_s_telephone_number",
            "CM0.10",
        ),
        serialization_alias="CM0.10",
        title="Contact's Telephone Number",
        description="Item #1019",
    )

    cm0_11: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_11",
            "contact_s_address",
            "CM0.11",
        ),
        serialization_alias="CM0.11",
        title="Contact's Address",
        description="Item #1020",
    )

    @field_validator("cm0_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("cm0_6", "cm0_8", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("cm0_7", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
