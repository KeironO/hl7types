"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OM1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.TS import TS


class OM1(HL7Model):
    """HL7 v2 OM1 segment.

    Attributes
    ----------
    om1_1 : str | None
        OM1.1 (opt) - Segment Type ID (ST)

    om1_2 : str | None
        OM1.2 (opt) - Sequence Number - Test/ Observation Master File (NM)

    om1_3 : CE
        OM1.3 (req) - Producer's test / observation ID (CE)

    om1_4 : list[str] | None
        OM1.4 (opt, rep) - Permitted Data Types (ID)

    om1_5 : str
        OM1.5 (req) - Specimen Required (ID)

    om1_6 : CE
        OM1.6 (req) - Producer ID (CE)

    om1_7 : str | None
        OM1.7 (opt) - Observation Description (TX)

    om1_8 : CE | None
        OM1.8 (opt) - Other test / observation IDs for the observation (CE)

    om1_9 : list[str]
        OM1.9 (req, rep) - Other Names (ST)

    om1_10 : str | None
        OM1.10 (opt) - Preferred Report Name for the Observation (ST)

    om1_11 : str | None
        OM1.11 (opt) - Preferred Short Name or Mnemonic for Observation (ST)

    om1_12 : str | None
        OM1.12 (opt) - Preferred Long Name for the Observation (ST)

    om1_13 : str | None
        OM1.13 (opt) - Orderability (ID)

    om1_14 : list[CE] | None
        OM1.14 (opt, rep) - Identity of instrument used to perform this study (CE)

    om1_15 : list[CE] | None
        OM1.15 (opt, rep) - Coded Representation of Method (CE)

    om1_16 : str | None
        OM1.16 (opt) - Portable (ID)

    om1_17 : list[str] | None
        OM1.17 (opt, rep) - Observation producing department / section (ID)

    om1_18 : str | None
        OM1.18 (opt) - Telephone Number of Section (TN)

    om1_19 : str
        OM1.19 (req) - Nature of test / observation (ID)

    om1_20 : CE | None
        OM1.20 (opt) - Report Subheader (CE)

    om1_21 : str | None
        OM1.21 (opt) - Report Display Order (ST)

    om1_22 : TS
        OM1.22 (req) - Date / time stamp for any change in definition for obs (TS)

    om1_23 : TS | None
        OM1.23 (opt) - Effective date / time of change (TS)

    om1_24 : str | None
        OM1.24 (opt) - Typical Turn-around Time (NM)

    om1_25 : str | None
        OM1.25 (opt) - Processing Time (NM)

    om1_26 : list[str] | None
        OM1.26 (opt, rep) - Processing Priority (ID)

    om1_27 : str | None
        OM1.27 (opt) - Reporting Priority (ID)

    om1_28 : list[CE] | None
        OM1.28 (opt, rep) - Outside Site(s) Where Observation may be Performed (CE)

    om1_29 : list[AD] | None
        OM1.29 (opt, rep) - Address of Outside Site(s) (AD)

    om1_30 : list[str] | None
        OM1.30 (opt, rep) - Phone Number of Outside Site (TN)

    om1_31 : str | None
        OM1.31 (opt) - Confidentiality Code (ID)

    om1_32 : list[CE] | None
        OM1.32 (opt, rep) - Observations required to interpret the observation (CE)

    om1_33 : str | None
        OM1.33 (opt) - Interpretation of Observations (TX)

    om1_34 : list[CE] | None
        OM1.34 (opt, rep) - Contraindications to Observations (CE)

    om1_35 : list[CE] | None
        OM1.35 (opt, rep) - Reflex tests / observations (CE)

    om1_36 : str | None
        OM1.36 (opt) - Rules that Trigger Reflex Testing (ST)

    om1_37 : list[CE] | None
        OM1.37 (opt, rep) - Fixed Canned Message (CE)

    om1_38 : str | None
        OM1.38 (opt) - Patient Preparation (TX)

    om1_39 : CE | None
        OM1.39 (opt) - Procedure Medication (CE)

    om1_40 : str | None
        OM1.40 (opt) - Factors that may affect the observation (TX)

    om1_41 : list[str] | None
        OM1.41 (opt, rep) - Test / observation performance schedule (ST)

    om1_42 : str | None
        OM1.42 (opt) - Description of Test Methods (TX)
    """

    om1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_1",
            "segment_type_id",
            "OM1.1",
        ),
        serialization_alias="OM1.1",
        title="Segment Type ID",
        description="Item #585",
    )

    om1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_2",
            "sequence_number_test_observation_master_file",
            "OM1.2",
        ),
        serialization_alias="OM1.2",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om1_3: CE = Field(
        validation_alias=AliasChoices(
            "om1_3",
            "producer_s_test_observation_id",
            "OM1.3",
        ),
        serialization_alias="OM1.3",
        title="Producer's test / observation ID",
        description="Item #587",
    )

    om1_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_4",
            "permitted_data_types",
            "OM1.4",
        ),
        serialization_alias="OM1.4",
        title="Permitted Data Types",
        description="Item #588 | Table HL70125",
    )

    om1_5: str = Field(
        validation_alias=AliasChoices(
            "om1_5",
            "specimen_required",
            "OM1.5",
        ),
        serialization_alias="OM1.5",
        title="Specimen Required",
        description="Item #589 | Table HL70136",
    )

    om1_6: CE = Field(
        validation_alias=AliasChoices(
            "om1_6",
            "producer_id",
            "OM1.6",
        ),
        serialization_alias="OM1.6",
        title="Producer ID",
        description="Item #590",
    )

    om1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_7",
            "observation_description",
            "OM1.7",
        ),
        serialization_alias="OM1.7",
        title="Observation Description",
        description="Item #591",
    )

    om1_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_8",
            "other_test_observation_ids_for_the_observation",
            "OM1.8",
        ),
        serialization_alias="OM1.8",
        title="Other test / observation IDs for the observation",
        description="Item #592",
    )

    om1_9: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "om1_9",
            "other_names",
            "OM1.9",
        ),
        serialization_alias="OM1.9",
        title="Other Names",
        description="Item #593",
    )

    om1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_10",
            "preferred_report_name_for_the_observation",
            "OM1.10",
        ),
        serialization_alias="OM1.10",
        title="Preferred Report Name for the Observation",
        description="Item #594",
    )

    om1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_11",
            "preferred_short_name_or_mnemonic_for_observation",
            "OM1.11",
        ),
        serialization_alias="OM1.11",
        title="Preferred Short Name or Mnemonic for Observation",
        description="Item #595",
    )

    om1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_12",
            "preferred_long_name_for_the_observation",
            "OM1.12",
        ),
        serialization_alias="OM1.12",
        title="Preferred Long Name for the Observation",
        description="Item #596",
    )

    om1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_13",
            "orderability",
            "OM1.13",
        ),
        serialization_alias="OM1.13",
        title="Orderability",
        description="Item #597 | Table HL70136",
    )

    om1_14: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_14",
            "identity_of_instrument_used_to_perform_this_study",
            "OM1.14",
        ),
        serialization_alias="OM1.14",
        title="Identity of instrument used to perform this study",
        description="Item #598",
    )

    om1_15: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_15",
            "coded_representation_of_method",
            "OM1.15",
        ),
        serialization_alias="OM1.15",
        title="Coded Representation of Method",
        description="Item #599",
    )

    om1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_16",
            "portable",
            "OM1.16",
        ),
        serialization_alias="OM1.16",
        title="Portable",
        description="Item #600 | Table HL70136",
    )

    om1_17: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_17",
            "observation_producing_department_section",
            "OM1.17",
        ),
        serialization_alias="OM1.17",
        title="Observation producing department / section",
        description="Item #601",
    )

    om1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_18",
            "telephone_number_of_section",
            "OM1.18",
        ),
        serialization_alias="OM1.18",
        title="Telephone Number of Section",
        description="Item #602",
    )

    om1_19: str = Field(
        validation_alias=AliasChoices(
            "om1_19",
            "nature_of_test_observation",
            "OM1.19",
        ),
        serialization_alias="OM1.19",
        title="Nature of test / observation",
        description="Item #603 | Table HL70174",
    )

    om1_20: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_20",
            "report_subheader",
            "OM1.20",
        ),
        serialization_alias="OM1.20",
        title="Report Subheader",
        description="Item #604",
    )

    om1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_21",
            "report_display_order",
            "OM1.21",
        ),
        serialization_alias="OM1.21",
        title="Report Display Order",
        description="Item #605",
    )

    om1_22: TS = Field(
        validation_alias=AliasChoices(
            "om1_22",
            "date_time_stamp_for_any_change_in_definition_for_obs",
            "OM1.22",
        ),
        serialization_alias="OM1.22",
        title="Date / time stamp for any change in definition for obs",
        description="Item #606",
    )

    om1_23: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_23",
            "effective_date_time_of_change",
            "OM1.23",
        ),
        serialization_alias="OM1.23",
        title="Effective date / time of change",
        description="Item #607",
    )

    om1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_24",
            "typical_turn_around_time",
            "OM1.24",
        ),
        serialization_alias="OM1.24",
        title="Typical Turn-around Time",
        description="Item #608",
    )

    om1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_25",
            "processing_time",
            "OM1.25",
        ),
        serialization_alias="OM1.25",
        title="Processing Time",
        description="Item #609",
    )

    om1_26: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_26",
            "processing_priority",
            "OM1.26",
        ),
        serialization_alias="OM1.26",
        title="Processing Priority",
        description="Item #610 | Table HL70168",
    )

    om1_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_27",
            "reporting_priority",
            "OM1.27",
        ),
        serialization_alias="OM1.27",
        title="Reporting Priority",
        description="Item #611 | Table HL70169",
    )

    om1_28: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_28",
            "outside_site_s_where_observation_may_be_performed",
            "OM1.28",
        ),
        serialization_alias="OM1.28",
        title="Outside Site(s) Where Observation may be Performed",
        description="Item #612",
    )

    om1_29: Optional[List[AD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_29",
            "address_of_outside_site_s",
            "OM1.29",
        ),
        serialization_alias="OM1.29",
        title="Address of Outside Site(s)",
        description="Item #613",
    )

    om1_30: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_30",
            "phone_number_of_outside_site",
            "OM1.30",
        ),
        serialization_alias="OM1.30",
        title="Phone Number of Outside Site",
        description="Item #614",
    )

    om1_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_31",
            "confidentiality_code",
            "OM1.31",
        ),
        serialization_alias="OM1.31",
        title="Confidentiality Code",
        description="Item #615 | Table HL70177",
    )

    om1_32: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_32",
            "observations_required_to_interpret_the_observation",
            "OM1.32",
        ),
        serialization_alias="OM1.32",
        title="Observations required to interpret the observation",
        description="Item #616",
    )

    om1_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_33",
            "interpretation_of_observations",
            "OM1.33",
        ),
        serialization_alias="OM1.33",
        title="Interpretation of Observations",
        description="Item #617",
    )

    om1_34: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_34",
            "contraindications_to_observations",
            "OM1.34",
        ),
        serialization_alias="OM1.34",
        title="Contraindications to Observations",
        description="Item #618",
    )

    om1_35: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_35",
            "reflex_tests_observations",
            "OM1.35",
        ),
        serialization_alias="OM1.35",
        title="Reflex tests / observations",
        description="Item #619",
    )

    om1_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_36",
            "rules_that_trigger_reflex_testing",
            "OM1.36",
        ),
        serialization_alias="OM1.36",
        title="Rules that Trigger Reflex Testing",
        description="Item #620",
    )

    om1_37: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_37",
            "fixed_canned_message",
            "OM1.37",
        ),
        serialization_alias="OM1.37",
        title="Fixed Canned Message",
        description="Item #621",
    )

    om1_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_38",
            "patient_preparation",
            "OM1.38",
        ),
        serialization_alias="OM1.38",
        title="Patient Preparation",
        description="Item #622",
    )

    om1_39: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_39",
            "procedure_medication",
            "OM1.39",
        ),
        serialization_alias="OM1.39",
        title="Procedure Medication",
        description="Item #623",
    )

    om1_40: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_40",
            "factors_that_may_affect_the_observation",
            "OM1.40",
        ),
        serialization_alias="OM1.40",
        title="Factors that may affect the observation",
        description="Item #624",
    )

    om1_41: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_41",
            "test_observation_performance_schedule",
            "OM1.41",
        ),
        serialization_alias="OM1.41",
        title="Test / observation performance schedule",
        description="Item #625",
    )

    om1_42: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_42",
            "description_of_test_methods",
            "OM1.42",
        ),
        serialization_alias="OM1.42",
        title="Description of Test Methods",
        description="Item #626",
    )

    @field_validator("om1_2", "om1_24", "om1_25", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
