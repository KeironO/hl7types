"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VAR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class VAR(BaseModel):
    """HL7 v2 VAR segment."""

    var_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "var_1",
            "variance_instance_id",
            "VAR.1",
        ),
        serialization_alias="VAR.1",
        title="Variance Instance ID",
        description="Item #1212",
    )

    var_2: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "var_2",
            "documented_date_time",
            "VAR.2",
        ),
        serialization_alias="VAR.2",
        title="Documented Date/Time",
        description="Item #1213",
    )

    var_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "var_3",
            "stated_variance_date_time",
            "VAR.3",
        ),
        serialization_alias="VAR.3",
        title="Stated Variance Date/Time",
        description="Item #1214",
    )

    var_4: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "var_4",
            "variance_originator",
            "VAR.4",
        ),
        serialization_alias="VAR.4",
        title="Variance Originator",
        description="Item #1215",
    )

    var_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "var_5",
            "variance_classification",
            "VAR.5",
        ),
        serialization_alias="VAR.5",
        title="Variance Classification",
        description="Item #1216",
    )

    var_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "var_6",
            "variance_description",
            "VAR.6",
        ),
        serialization_alias="VAR.6",
        title="Variance Description",
        description="Item #1217",
    )

    model_config = {"populate_by_name": True}
