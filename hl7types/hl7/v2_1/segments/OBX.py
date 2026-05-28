"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: OBX
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class OBX(BaseModel):
    """HL7 v2 OBX segment."""

    obx_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_1",
            "set_id_observation_simple",
            "OBX.1",
        ),
        serialization_alias="OBX.1",
        title="SET ID - OBSERVATION SIMPLE",
        description="Item #559",
    )

    obx_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_2",
            "value_type",
            "OBX.2",
        ),
        serialization_alias="OBX.2",
        title="VALUE TYPE",
        description="Item #676 | Table HL70125",
    )

    obx_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_3",
            "observation_identifier",
            "OBX.3",
        ),
        serialization_alias="OBX.3",
        title="OBSERVATION IDENTIFIER",
        description="Item #560",
    )

    obx_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_4",
            "observation_sub_id",
            "OBX.4",
        ),
        serialization_alias="OBX.4",
        title="OBSERVATION SUB-ID",
        description="Item #769",
    )

    obx_5: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_5",
            "observation_results",
            "OBX.5",
        ),
        serialization_alias="OBX.5",
        title="OBSERVATION RESULTS",
        description="Item #561",
    )

    obx_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_6",
            "units",
            "OBX.6",
        ),
        serialization_alias="OBX.6",
        title="UNITS",
        description="Item #562",
    )

    obx_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_7",
            "references_range",
            "OBX.7",
        ),
        serialization_alias="OBX.7",
        title="REFERENCES RANGE",
        description="Item #563",
    )

    obx_8: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_8",
            "abnormal_flags",
            "OBX.8",
        ),
        serialization_alias="OBX.8",
        title="ABNORMAL FLAGS",
        description="Item #564 | Table HL70078",
    )

    obx_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_9",
            "probability",
            "OBX.9",
        ),
        serialization_alias="OBX.9",
        title="PROBABILITY",
        description="Item #639",
    )

    obx_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_10",
            "nature_of_abnormal_test",
            "OBX.10",
        ),
        serialization_alias="OBX.10",
        title="NATURE OF ABNORMAL TEST",
        description="Item #565 | Table HL70080",
    )

    obx_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_11",
            "observ_result_status",
            "OBX.11",
        ),
        serialization_alias="OBX.11",
        title="OBSERV RESULT STATUS",
        description="Item #566 | Table HL70085",
    )

    obx_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "date_last_obs_normal_values",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="DATE LAST OBS NORMAL VALUES",
        description="Item #567",
    )

    model_config = {"populate_by_name": True}
