"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: QAK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class QAK(HL7Model):
    """Query Acknowledgment (S5.5.2).

    Attributes
    ----------
    qak_1 : str | None
        QAK.1 - Query Tag (ST) C S5.5.2.1

    qak_2 : str | None
        QAK.2 - Query Response Status (ID) O S5.5.2.2 | 0208 - Query Response Status

    qak_3 : CWE | None
        QAK.3 - Message Query Name (CWE) O S5.5.2.3 | 0471 - Query Name

    qak_4 : str | None
        QAK.4 - Hit Count Total (NM) O S5.5.2.4

    qak_5 : str | None
        QAK.5 - This payload (NM) O S5.5.2.5

    qak_6 : str | None
        QAK.6 - Hits remaining (NM) O S5.5.2.6
    """

    qak_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_1",
            "query_tag",
            "QAK.1",
        ),
        serialization_alias="QAK.1",
        title="Query Tag",
        description="C | Item #00696",
    )

    qak_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_2",
            "query_response_status",
            "QAK.2",
        ),
        serialization_alias="QAK.2",
        title="Query Response Status",
        description=(
            "O | Item #00708 | Table 0208 - Query Response Status | LEN:2"
        ),
    )

    qak_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_3",
            "message_query_name",
            "QAK.3",
        ),
        serialization_alias="QAK.3",
        title="Message Query Name",
        description="O | Item #01375 | Table 0471 - Query Name",
    )

    qak_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_4",
            "hit_count_total",
            "QAK.4",
        ),
        serialization_alias="QAK.4",
        title="Hit Count Total",
        description="O | Item #01434",
    )

    qak_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_5",
            "this_payload",
            "QAK.5",
        ),
        serialization_alias="QAK.5",
        title="This payload",
        description="O | Item #01622",
    )

    qak_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_6",
            "hits_remaining",
            "QAK.6",
        ),
        serialization_alias="QAK.6",
        title="Hits remaining",
        description="O | Item #01623",
    )

    @field_validator("qak_4", "qak_5", "qak_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
