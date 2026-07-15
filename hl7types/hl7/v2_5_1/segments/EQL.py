"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EQL
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class EQL(HL7Model):
    """Embedded Query Language (S5.10.5.1).

    Attributes
    ----------
    eql_1 : str | None
        EQL.1 - Query Tag (ST) O S5.10.5.1.1

    eql_2 : str
        EQL.2 - Query/Response Format Code (ID) R S5.10.5.1.2 | 0106 - Query/response format code

    eql_3 : CE
        EQL.3 - EQL Query Name (CE) R S5.10.5.1.3

    eql_4 : str
        EQL.4 - EQL Query Statement (ST) R S5.10.5.1.4
    """

    eql_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eql_1",
            "query_tag",
            "EQL.1",
        ),
        serialization_alias="EQL.1",
        title="Query Tag",
        description="O | Item #00696 | LEN:32",
    )

    eql_2: str = Field(
        validation_alias=AliasChoices(
            "eql_2",
            "query_response_format_code",
            "EQL.2",
        ),
        serialization_alias="EQL.2",
        title="Query/Response Format Code",
        description=(
            "R | Item #00697 | Table 0106 - Query/response format code | LEN:1"
        ),
    )

    eql_3: CE = Field(
        validation_alias=AliasChoices(
            "eql_3",
            "eql_query_name",
            "EQL.3",
        ),
        serialization_alias="EQL.3",
        title="EQL Query Name",
        description="R | Item #00709",
    )

    eql_4: str = Field(
        validation_alias=AliasChoices(
            "eql_4",
            "eql_query_statement",
            "EQL.4",
        ),
        serialization_alias="EQL.4",
        title="EQL Query Statement",
        description="R | Item #00710 | LEN:4096",
    )

    model_config = {"populate_by_name": True}
