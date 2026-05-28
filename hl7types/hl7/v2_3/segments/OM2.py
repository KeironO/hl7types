"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OM2
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TX import TX


class OM2(BaseModel):
    """HL7 v2 OM2 segment."""

    om2_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_1",
            "sequence_number_test_observation_master_file",
            "OM2.1",
        ),
        serialization_alias="OM2.1",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om2_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_2",
            "units_of_measure",
            "OM2.2",
        ),
        serialization_alias="OM2.2",
        title="Units of Measure",
        description="Item #627",
    )

    om2_3: list[str] | None = Field(
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

    om2_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_4",
            "corresponding_si_units_of_measure",
            "OM2.4",
        ),
        serialization_alias="OM2.4",
        title="Corresponding SI Units of Measure",
        description="Item #629",
    )

    om2_5: TX | None = Field(
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

    om2_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_6",
            "reference_normal_range_ordinal_continuous_obs",
            "OM2.6",
        ),
        serialization_alias="OM2.6",
        title="Reference (Normal) Range - Ordinal & Continuous Obs",
        description="Item #631",
    )

    om2_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_7",
            "critical_range_for_ordinal_continuous_obs",
            "OM2.7",
        ),
        serialization_alias="OM2.7",
        title="Critical Range for Ordinal & Continuous Obs",
        description="Item #632",
    )

    om2_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om2_8",
            "absolute_range_for_ordinal_continuous_obs",
            "OM2.8",
        ),
        serialization_alias="OM2.8",
        title="Absolute Range for Ordinal & Continuous Obs",
        description="Item #633",
    )

    om2_9: list[str] | None = Field(
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

    om2_10: str | None = Field(
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
