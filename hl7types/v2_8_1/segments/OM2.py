"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OM2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.DLT import DLT
from ..datatypes.RFR import RFR
from ..datatypes.TX import TX


class OM2(BaseModel):
    """HL7 v2 OM2 segment."""

    om2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_1",
            "sequence_number_test_observation_master_file",
            "OM2.1",
        ),
        serialization_alias="OM2.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
    )

    om2_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_2",
            "units_of_measure",
            "OM2.2",
        ),
        serialization_alias="OM2.2",
        title="Units of Measure",
        description="Item #627 | Table HL79999",
    )

    om2_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_3",
            "range_of_decimal_precision",
            "OM2.3",
        ),
        serialization_alias="OM2.3",
        title="Range of Decimal Precision",
        description="Item #628",
    )

    om2_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_4",
            "corresponding_si_units_of_measure",
            "OM2.4",
        ),
        serialization_alias="OM2.4",
        title="Corresponding SI Units of Measure",
        description="Item #629 | Table HL79999",
    )

    om2_5: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_5",
            "si_conversion_factor",
            "OM2.5",
        ),
        serialization_alias="OM2.5",
        title="SI Conversion Factor",
        description="Item #630",
    )

    om2_6: Optional[List[RFR]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_6",
            "reference_normal_range_for_ordinal_and_continuous_observations",
            "OM2.6",
        ),
        serialization_alias="OM2.6",
        title=(
            "Reference (Normal) Range for Ordinal and Continuous Observations"
        ),
        description="Item #631",
    )

    om2_7: Optional[List[RFR]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_7",
            "critical_range_for_ordinal_and_continuous_observations",
            "OM2.7",
        ),
        serialization_alias="OM2.7",
        title="Critical Range for Ordinal and Continuous Observations",
        description="Item #632",
    )

    om2_8: Optional[RFR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_8",
            "absolute_range_for_ordinal_and_continuous_observations",
            "OM2.8",
        ),
        serialization_alias="OM2.8",
        title="Absolute Range for Ordinal and Continuous Observations",
        description="Item #633",
    )

    om2_9: Optional[List[DLT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_9",
            "delta_check_criteria",
            "OM2.9",
        ),
        serialization_alias="OM2.9",
        title="Delta Check Criteria",
        description="Item #634",
    )

    om2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_10",
            "minimum_meaningful_increments",
            "OM2.10",
        ),
        serialization_alias="OM2.10",
        title="Minimum Meaningful Increments",
        description="Item #635",
    )

    model_config = {"populate_by_name": True}
