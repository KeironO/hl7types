"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: GP2
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class GP2(HL7Model):
    """Grouping/Reimbursement - Procedure Line Item (S6.5.16).

    Attributes
    ----------
    gp2_1 : CWE | None
        GP2.1 - Revenue Code (CWE) O S6.5.1.41 | 0456 - Revenue code

    gp2_2 : str | None
        GP2.2 - Number of Service Units (NM) O S6.5.16.2

    gp2_3 : CP | None
        GP2.3 - Charge (CP) O S6.5.16.3

    gp2_4 : CWE | None
        GP2.4 - Reimbursement Action Code (CWE) O S6.5.16.4 | 0459 - Reimbursement Action Code

    gp2_5 : CWE | None
        GP2.5 - Denial or Rejection Code (CWE) O S6.5.16.5 | 0460 - Denial or Rejection Code

    gp2_6 : list[CWE] | None
        GP2.6 - OCE Edit Code (CWE) O rep S6.5.16.6 | 0458 - OCE Edit Code

    gp2_7 : CWE | None
        GP2.7 - Ambulatory Payment Classification Code (CWE) O S6.5.16.7 | 0466 - Ambulatory Payment Classification Code

    gp2_8 : list[CWE] | None
        GP2.8 - Modifier Edit Code (CWE) O rep S6.5.16.8 | 0467 - Modifier Edit Code

    gp2_9 : CWE | None
        GP2.9 - Payment Adjustment Code (CWE) O S6.5.16.9 | 0468 - Payment Adjustment Code

    gp2_10 : CWE | None
        GP2.10 - Packaging Status Code (CWE) O S6.5.16.10 | 0469 - Packaging Status Code

    gp2_11 : CP | None
        GP2.11 - Expected CMS Payment Amount (CP) O S6.5.16.11

    gp2_12 : CWE | None
        GP2.12 - Reimbursement Type Code (CWE) O S6.5.16.12 | 0470 - Reimbursement Type Code

    gp2_13 : CP | None
        GP2.13 - Co-Pay Amount (CP) O S6.5.16.13

    gp2_14 : str | None
        GP2.14 - Pay Rate per Service Unit (NM) O S6.5.16.14
    """

    gp2_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_1",
            "revenue_code",
            "GP2.1",
        ),
        serialization_alias="GP2.1",
        title="Revenue Code",
        description="O | Item #01600 | Table 0456 - Revenue code",
    )

    gp2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_2",
            "number_of_service_units",
            "GP2.2",
        ),
        serialization_alias="GP2.2",
        title="Number of Service Units",
        description="O | Item #01604",
    )

    gp2_3: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_3",
            "charge",
            "GP2.3",
        ),
        serialization_alias="GP2.3",
        title="Charge",
        description="O | Item #01605",
    )

    gp2_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_4",
            "reimbursement_action_code",
            "GP2.4",
        ),
        serialization_alias="GP2.4",
        title="Reimbursement Action Code",
        description="O | Item #01606 | Table 0459 - Reimbursement Action Code",
    )

    gp2_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_5",
            "denial_or_rejection_code",
            "GP2.5",
        ),
        serialization_alias="GP2.5",
        title="Denial or Rejection Code",
        description="O | Item #01607 | Table 0460 - Denial or Rejection Code",
    )

    gp2_6: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_6",
            "oce_edit_code",
            "GP2.6",
        ),
        serialization_alias="GP2.6",
        title="OCE Edit Code",
        description="O | Item #01608 | Table 0458 - OCE Edit Code",
    )

    gp2_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_7",
            "ambulatory_payment_classification_code",
            "GP2.7",
        ),
        serialization_alias="GP2.7",
        title="Ambulatory Payment Classification Code",
        description=(
            "O | Item #01609 | Table 0466 - Ambulatory Payment Classification "
            "Code"
        ),
    )

    gp2_8: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_8",
            "modifier_edit_code",
            "GP2.8",
        ),
        serialization_alias="GP2.8",
        title="Modifier Edit Code",
        description="O | Item #01610 | Table 0467 - Modifier Edit Code",
    )

    gp2_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_9",
            "payment_adjustment_code",
            "GP2.9",
        ),
        serialization_alias="GP2.9",
        title="Payment Adjustment Code",
        description="O | Item #01611 | Table 0468 - Payment Adjustment Code",
    )

    gp2_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_10",
            "packaging_status_code",
            "GP2.10",
        ),
        serialization_alias="GP2.10",
        title="Packaging Status Code",
        description="O | Item #01617 | Table 0469 - Packaging Status Code",
    )

    gp2_11: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_11",
            "expected_cms_payment_amount",
            "GP2.11",
        ),
        serialization_alias="GP2.11",
        title="Expected CMS Payment Amount",
        description="O | Item #01618",
    )

    gp2_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_12",
            "reimbursement_type_code",
            "GP2.12",
        ),
        serialization_alias="GP2.12",
        title="Reimbursement Type Code",
        description="O | Item #01619 | Table 0470 - Reimbursement Type Code",
    )

    gp2_13: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_13",
            "co_pay_amount",
            "GP2.13",
        ),
        serialization_alias="GP2.13",
        title="Co-Pay Amount",
        description="O | Item #01620",
    )

    gp2_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_14",
            "pay_rate_per_service_unit",
            "GP2.14",
        ),
        serialization_alias="GP2.14",
        title="Pay Rate per Service Unit",
        description="O | Item #01621",
    )

    @field_validator("gp2_2", "gp2_14", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
