"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NTE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.FT import FT
from ..datatypes.XCN import XCN


class NTE(HL7Model):
    """HL7 v2 NTE segment.

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 (opt) - Set ID - NTE (SI)

    nte_2 : str | None
        NTE.2 (opt) - Source of Comment (ID)

    nte_3 : list[FT] | None
        NTE.3 (opt, rep) - Comment (FT)

    nte_4 : CWE | None
        NTE.4 (opt) - Comment Type (CWE)

    nte_5 : XCN | None
        NTE.5 (opt) - Entered By (XCN)

    nte_6 : str | None
        NTE.6 (opt) - Entered Date/Time (DTM)

    nte_7 : str | None
        NTE.7 (opt) - Effective Start Date (DTM)

    nte_8 : str | None
        NTE.8 (opt) - Expiration Date (DTM)
    """

    nte_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_1",
            "set_id_nte",
            "NTE.1",
        ),
        serialization_alias="NTE.1",
        title="Set ID - NTE",
        description="Item #96",
    )

    nte_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_2",
            "source_of_comment",
            "NTE.2",
        ),
        serialization_alias="NTE.2",
        title="Source of Comment",
        description="Item #97 | Table HL70105",
    )

    nte_3: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_3",
            "comment",
            "NTE.3",
        ),
        serialization_alias="NTE.3",
        title="Comment",
        description="Item #98",
    )

    nte_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_4",
            "comment_type",
            "NTE.4",
        ),
        serialization_alias="NTE.4",
        title="Comment Type",
        description="Item #1318 | Table HL70364",
    )

    nte_5: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_5",
            "entered_by",
            "NTE.5",
        ),
        serialization_alias="NTE.5",
        title="Entered By",
        description="Item #224",
    )

    nte_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_6",
            "entered_date_time",
            "NTE.6",
        ),
        serialization_alias="NTE.6",
        title="Entered Date/Time",
        description="Item #661",
    )

    nte_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_7",
            "effective_start_date",
            "NTE.7",
        ),
        serialization_alias="NTE.7",
        title="Effective Start Date",
        description="Item #1004",
    )

    nte_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_8",
            "expiration_date",
            "NTE.8",
        ),
        serialization_alias="NTE.8",
        title="Expiration Date",
        description="Item #2185",
    )

    model_config = {"populate_by_name": True}
