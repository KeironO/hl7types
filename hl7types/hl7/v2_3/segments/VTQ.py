"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VTQ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.QSC import QSC


class VTQ(HL7Model):
    """Virtual Table Query Request (S2.24.17).

    Attributes
    ----------
    vtq_1 : str | None
        VTQ.1 - Query tag (ST) O S2.24.16

    vtq_2 : str
        VTQ.2 - Query/ Response Format Code (ID) R S2.24.16 | 0106 - Query/Response Format Code

    vtq_3 : CE
        VTQ.3 - VT Query Name (CE) R S2.24.17.3

    vtq_4 : CE
        VTQ.4 - Virtual Table Name (CE) R S2.24.17.4

    vtq_5 : list[QSC] | None
        VTQ.5 - Selection Criteria (QSC) O rep S2.24.17.5
    """

    vtq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vtq_1",
            "query_tag",
            "VTQ.1",
        ),
        serialization_alias="VTQ.1",
        title="Query tag",
        description="O | Item #00696 | LEN:32",
    )

    vtq_2: str = Field(
        validation_alias=AliasChoices(
            "vtq_2",
            "query_response_format_code",
            "VTQ.2",
        ),
        serialization_alias="VTQ.2",
        title="Query/ Response Format Code",
        description=(
            "R | Item #00697 | Table 0106 - Query/Response Format Code | LEN:1"
        ),
    )

    vtq_3: CE = Field(
        validation_alias=AliasChoices(
            "vtq_3",
            "vt_query_name",
            "VTQ.3",
        ),
        serialization_alias="VTQ.3",
        title="VT Query Name",
        description="R | Item #00698",
    )

    vtq_4: CE = Field(
        validation_alias=AliasChoices(
            "vtq_4",
            "virtual_table_name",
            "VTQ.4",
        ),
        serialization_alias="VTQ.4",
        title="Virtual Table Name",
        description="R | Item #00699",
    )

    vtq_5: Optional[List[QSC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vtq_5",
            "selection_criteria",
            "VTQ.5",
        ),
        serialization_alias="VTQ.5",
        title="Selection Criteria",
        description="O | Item #00700",
    )

    model_config = ConfigDict(populate_by_name=True)
