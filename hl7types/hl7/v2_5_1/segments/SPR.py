"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SPR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.QIP import QIP


class SPR(HL7Model):
    """Stored Procedure Request Definition (S5.10.5.5).

    Attributes
    ----------
    spr_1 : str | None
        SPR.1 (opt) - Query Tag (ST) S5.10.5.1.1

    spr_2 : str
        SPR.2 (req) - Query/Response Format Code (ID) S5.10.5.1.2 | 0106 - Query/response format code

    spr_3 : CE
        SPR.3 (req) - Stored Procedure Name (CE) S5.10.5.5.3

    spr_4 : list[QIP] | None
        SPR.4 (opt, rep) - Input Parameter List (QIP) S5.10.5.2.3
    """

    spr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spr_1",
            "query_tag",
            "SPR.1",
        ),
        serialization_alias="SPR.1",
        title="Query Tag",
        description="Item #696",
    )

    spr_2: str = Field(
        validation_alias=AliasChoices(
            "spr_2",
            "query_response_format_code",
            "SPR.2",
        ),
        serialization_alias="SPR.2",
        title="Query/Response Format Code",
        description="Item #697 | Table HL70106",
    )

    spr_3: CE = Field(
        validation_alias=AliasChoices(
            "spr_3",
            "stored_procedure_name",
            "SPR.3",
        ),
        serialization_alias="SPR.3",
        title="Stored Procedure Name",
        description="Item #704",
    )

    spr_4: Optional[List[QIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spr_4",
            "input_parameter_list",
            "SPR.4",
        ),
        serialization_alias="SPR.4",
        title="Input Parameter List",
        description="Item #705",
    )

    model_config = {"populate_by_name": True}
