"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
    """Stored Procedure Request Definition (S2.24.20).

    Attributes
    ----------
    spr_1 : str | None
        SPR.1 - Query tag (ST) O S2.24.16

    spr_2 : str
        SPR.2 - Query/ Response Format Code (ID) R S2.24.16 | 0106 - Query/Response Format Code

    spr_3 : CE
        SPR.3 - Stored procedure name (CE) R S2.24.20.3

    spr_4 : list[QIP] | None
        SPR.4 - Input parameter list (QIP) O rep S2.24.20
    """

    spr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spr_1",
            "query_tag",
            "SPR.1",
        ),
        serialization_alias="SPR.1",
        title="Query tag",
        description="O | Item #00696 | LEN:32",
    )

    spr_2: str = Field(
        validation_alias=AliasChoices(
            "spr_2",
            "query_response_format_code",
            "SPR.2",
        ),
        serialization_alias="SPR.2",
        title="Query/ Response Format Code",
        description=(
            "R | Item #00697 | Table 0106 - Query/Response Format Code | LEN:1"
        ),
    )

    spr_3: CE = Field(
        validation_alias=AliasChoices(
            "spr_3",
            "stored_procedure_name",
            "SPR.3",
        ),
        serialization_alias="SPR.3",
        title="Stored procedure name",
        description="R | Item #00704",
    )

    spr_4: Optional[List[QIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "spr_4",
            "input_parameter_list",
            "SPR.4",
        ),
        serialization_alias="SPR.4",
        title="Input parameter list",
        description="O | Item #00705",
    )

    model_config = {"populate_by_name": True}
