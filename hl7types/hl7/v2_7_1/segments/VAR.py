"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: VAR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN


class VAR(BaseModel):
    """HL7 v2 VAR segment.

    Attributes
    ----------
    var_1 : EI
        VAR.1 (req) - Variance Instance ID (EI)

    var_2 : str
        VAR.2 (req) - Documented Date/Time (DTM)

    var_3 : str | None
        VAR.3 (opt) - Stated Variance Date/Time (DTM)

    var_4 : list[XCN] | None
        VAR.4 (opt, rep) - Variance Originator (XCN)

    var_5 : CWE | None
        VAR.5 (opt) - Variance Classification (CWE)

    var_6 : list[str] | None
        VAR.6 (opt, rep) - Variance Description (ST)
    """

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

    var_2: str = Field(
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

    var_3: Optional[str] = Field(
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

    var_4: Optional[List[XCN]] = Field(
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

    var_5: Optional[CWE] = Field(
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
