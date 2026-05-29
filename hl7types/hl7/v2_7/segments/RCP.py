"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RCP
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CQ import CQ
from ..datatypes.SRT import SRT


class RCP(BaseModel):
    """HL7 v2 RCP segment.

    Attributes
    ----------
    rcp_1 : str | None
        RCP.1 (opt) - Query Priority (ID)

    rcp_2 : CQ | None
        RCP.2 (opt) - Quantity Limited Request (CQ)

    rcp_3 : CNE | None
        RCP.3 (opt) - Response Modality (CNE)

    rcp_4 : str | None
        RCP.4 (opt) - Execution and Delivery Time (DTM)

    rcp_5 : str | None
        RCP.5 (opt) - Modify Indicator (ID)

    rcp_6 : list[SRT] | None
        RCP.6 (opt, rep) - Sort-by Field (SRT)

    rcp_7 : list[str] | None
        RCP.7 (opt, rep) - Segment group inclusion (ID)
    """

    rcp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_1",
            "query_priority",
            "RCP.1",
        ),
        serialization_alias="RCP.1",
        title="Query Priority",
        description="Item #27 | Table HL70091",
    )

    rcp_2: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_2",
            "quantity_limited_request",
            "RCP.2",
        ),
        serialization_alias="RCP.2",
        title="Quantity Limited Request",
        description="Item #31 | Table HL70126",
    )

    rcp_3: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_3",
            "response_modality",
            "RCP.3",
        ),
        serialization_alias="RCP.3",
        title="Response Modality",
        description="Item #1440 | Table HL70394",
    )

    rcp_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_4",
            "execution_and_delivery_time",
            "RCP.4",
        ),
        serialization_alias="RCP.4",
        title="Execution and Delivery Time",
        description="Item #1441",
    )

    rcp_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_5",
            "modify_indicator",
            "RCP.5",
        ),
        serialization_alias="RCP.5",
        title="Modify Indicator",
        description="Item #1443 | Table HL70395",
    )

    rcp_6: Optional[List[SRT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_6",
            "sort_by_field",
            "RCP.6",
        ),
        serialization_alias="RCP.6",
        title="Sort-by Field",
        description="Item #1624",
    )

    rcp_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcp_7",
            "segment_group_inclusion",
            "RCP.7",
        ),
        serialization_alias="RCP.7",
        title="Segment group inclusion",
        description="Item #1594 | Table HL70391",
    )

    model_config = {"populate_by_name": True}
