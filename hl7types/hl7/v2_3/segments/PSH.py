"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PSH
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PSH(HL7Model):
    """Product Summary Header (S7.11.4).

    Attributes
    ----------
    psh_1 : str
        PSH.1 - Report Type (ST) R S7.11.4.1

    psh_2 : str | None
        PSH.2 - Report Form Identifier (ST) O S8.6.2.26

    psh_3 : TS
        PSH.3 - Report Date (TS) R S7.11.4.3

    psh_4 : TS | None
        PSH.4 - Report Interval Start Date (TS) O S7.11.4.4

    psh_5 : TS | None
        PSH.5 - Report Interval End Date (TS) O S8.8.3.5

    psh_6 : CQ | None
        PSH.6 - Quantity Manufactured (CQ) O S7.11.4.6

    psh_7 : CQ | None
        PSH.7 - Quantity Distributed (CQ) O S7.11.4.7

    psh_8 : str | None
        PSH.8 - Quantity Distributed Method (ID) O S7.11.4.8 | 0329 - Quantity Method

    psh_9 : str | None
        PSH.9 - Quantity Distributed Comment (FT) O S7.11.4.9

    psh_10 : CQ | None
        PSH.10 - Quantity in Use (CQ) O S7.11.4.10

    psh_11 : str | None
        PSH.11 - Quantity in Use Method (ID) O S7.11.4.11 | 0329 - Quantity Method

    psh_12 : str | None
        PSH.12 - Quantity in Use Comment (FT) O S7.11.4.12

    psh_13 : list[str] | None
        PSH.13 - Number of Product Experience Reports Filed by Facility (NM) O rep S7.11.4.13

    psh_14 : list[str] | None
        PSH.14 - Number of Product Experience Reports Filed by Distributor (NM) O rep S7.11.4.14
    """

    psh_1: str = Field(
        validation_alias=AliasChoices(
            "psh_1",
            "report_type",
            "PSH.1",
        ),
        serialization_alias="PSH.1",
        title="Report Type",
        description="R | Item #01233 | LEN:60",
    )

    psh_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_2",
            "report_form_identifier",
            "PSH.2",
        ),
        serialization_alias="PSH.2",
        title="Report Form Identifier",
        description="O | Item #01234 | LEN:60",
    )

    psh_3: TS = Field(
        validation_alias=AliasChoices(
            "psh_3",
            "report_date",
            "PSH.3",
        ),
        serialization_alias="PSH.3",
        title="Report Date",
        description="R | Item #01235",
    )

    psh_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_4",
            "report_interval_start_date",
            "PSH.4",
        ),
        serialization_alias="PSH.4",
        title="Report Interval Start Date",
        description="O | Item #01236",
    )

    psh_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_5",
            "report_interval_end_date",
            "PSH.5",
        ),
        serialization_alias="PSH.5",
        title="Report Interval End Date",
        description="O | Item #01237",
    )

    psh_6: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_6",
            "quantity_manufactured",
            "PSH.6",
        ),
        serialization_alias="PSH.6",
        title="Quantity Manufactured",
        description="O | Item #01238",
    )

    psh_7: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_7",
            "quantity_distributed",
            "PSH.7",
        ),
        serialization_alias="PSH.7",
        title="Quantity Distributed",
        description="O | Item #01239",
    )

    psh_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_8",
            "quantity_distributed_method",
            "PSH.8",
        ),
        serialization_alias="PSH.8",
        title="Quantity Distributed Method",
        description="O | Item #01240 | Table 0329 - Quantity Method | LEN:1",
    )

    psh_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_9",
            "quantity_distributed_comment",
            "PSH.9",
        ),
        serialization_alias="PSH.9",
        title="Quantity Distributed Comment",
        description="O | Item #01241",
    )

    psh_10: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_10",
            "quantity_in_use",
            "PSH.10",
        ),
        serialization_alias="PSH.10",
        title="Quantity in Use",
        description="O | Item #01242",
    )

    psh_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_11",
            "quantity_in_use_method",
            "PSH.11",
        ),
        serialization_alias="PSH.11",
        title="Quantity in Use Method",
        description="O | Item #01243 | Table 0329 - Quantity Method | LEN:1",
    )

    psh_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_12",
            "quantity_in_use_comment",
            "PSH.12",
        ),
        serialization_alias="PSH.12",
        title="Quantity in Use Comment",
        description="O | Item #01244",
    )

    psh_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_13",
            "number_of_product_experience_reports_filed_by_facility",
            "PSH.13",
        ),
        serialization_alias="PSH.13",
        title="Number of Product Experience Reports Filed by Facility",
        description="O | Item #01245 | LEN:2",
    )

    psh_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_14",
            "number_of_product_experience_reports_filed_by_distributor",
            "PSH.14",
        ),
        serialization_alias="PSH.14",
        title="Number of Product Experience Reports Filed by Distributor",
        description="O | Item #01246 | LEN:2",
    )

    @field_validator("psh_13", "psh_14", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
