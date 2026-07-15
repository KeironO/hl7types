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
    """GENERAL - fields that apply to most observations (S7.6.4).

    Attributes
    ----------
    om1_1 : str | None
        OM1.1 - Segment Type ID (ST) NA S7.6.9.1

    om1_2 : str | None
        OM1.2 - Sequence Number - Test/ Observation Master File (NM) NA S7.6.9.2

    om1_3 : CE
        OM1.3 - Producer's test / observation ID (CE) R S7.6.4.3

    om1_4 : list[str] | None
        OM1.4 - Permitted Data Types (ID) NA rep S7.6.4.4 | 0125 - VALUE TYPE

    om1_5 : str
        OM1.5 - Specimen Required (ID) R S7.6.4.5 | 0136 - Y/N Indicator

    om1_6 : CE
        OM1.6 - Producer ID (CE) R S7.6.4.6

    om1_7 : str | None
        OM1.7 - Observation Description (TX) NA S7.6.4.7

    om1_8 : CE | None
        OM1.8 - Other test / observation IDs for the observation (CE) NA S7.6.4.8

    om1_9 : list[str]
        OM1.9 - Other Names (ST) R rep S7.6.4.9

    om1_10 : str | None
        OM1.10 - Preferred Report Name for the Observation (ST) NA S7.6.4.10

    om1_11 : str | None
        OM1.11 - Preferred Short Name or Mnemonic for Observation (ST) NA S7.6.4.11

    om1_12 : str | None
        OM1.12 - Preferred Long Name for the Observation (ST) NA S7.6.4.12

    om1_13 : str | None
        OM1.13 - Orderability (ID) NA S7.6.4.13 | 0136 - Y/N Indicator

    om1_14 : list[CE] | None
        OM1.14 - Identity of instrument used to perform this study (CE) NA rep S7.6.4.14

    om1_15 : list[CE] | None
        OM1.15 - Coded Representation of Method (CE) NA rep S7.6.4.15

    om1_16 : str | None
        OM1.16 - Portable (ID) NA S7.6.4.16 | 0136 - Y/N Indicator

    om1_17 : list[str] | None
        OM1.17 - Observation producing department / section (ID) NA rep S7.6.4.17

    om1_18 : str | None
        OM1.18 - Telephone Number of Section (TN) NA S7.6.4.18

    om1_19 : str
        OM1.19 - Nature of test / observation (ID) R S7.6.4.19 | 0174 - NATURE OF TEST/OBSERVATION

    om1_20 : CE | None
        OM1.20 - Report Subheader (CE) NA S7.6.4.20

    om1_21 : str | None
        OM1.21 - Report Display Order (ST) NA S7.6.4.21

    om1_22 : TS
        OM1.22 - Date / time stamp for any change in definition for obs (TS) R S7.6.4.22

    om1_23 : TS | None
        OM1.23 - Effective date / time of change (TS) NA S7.6.4.23

    om1_24 : str | None
        OM1.24 - Typical Turn-around Time (NM) NA S7.6.4.24

    om1_25 : str | None
        OM1.25 - Processing Time (NM) NA S7.6.4.25

    om1_26 : list[str] | None
        OM1.26 - Processing Priority (ID) NA rep S7.6.4.26 | 0168 - PROCESSING PRIORITY

    om1_27 : str | None
        OM1.27 - Reporting Priority (ID) NA S7.6.4.27 | 0169 - REPORTIN PRIORITY

    om1_28 : list[CE] | None
        OM1.28 - Outside Site(s) Where Observation may be Performed (CE) NA rep S7.6.4.28

    om1_29 : list[AD] | None
        OM1.29 - Address of Outside Site(s) (AD) NA rep S7.6.4.29

    om1_30 : list[str] | None
        OM1.30 - Phone Number of Outside Site (TN) NA rep S7.6.4.30

    om1_31 : str | None
        OM1.31 - Confidentiality Code (ID) NA S7.6.4.31 | 0177 - CONFIDENTIALITY CODE

    om1_32 : list[CE] | None
        OM1.32 - Observations required to interpret the observation (CE) NA rep S7.6.4.32

    om1_33 : str | None
        OM1.33 - Interpretation of Observations (TX) NA S7.6.4.33

    om1_34 : list[CE] | None
        OM1.34 - Contraindications to Observations (CE) NA rep S7.6.4.34

    om1_35 : list[CE] | None
        OM1.35 - Reflex tests / observations (CE) NA rep S7.6.4.35

    om1_36 : str | None
        OM1.36 - Rules that Trigger Reflex Testing (ST) NA S7.6.4.36

    om1_37 : list[CE] | None
        OM1.37 - Fixed Canned Message (CE) NA rep S7.6.4.37

    om1_38 : str | None
        OM1.38 - Patient Preparation (TX) NA S7.6.4.38

    om1_39 : CE | None
        OM1.39 - Procedure Medication (CE) NA S7.6.4.39

    om1_40 : str | None
        OM1.40 - Factors that may affect the observation (TX) NA S7.6.4.40

    om1_41 : list[str] | None
        OM1.41 - Test / observation performance schedule (ST) NA rep S7.6.4.41

    om1_42 : str | None
        OM1.42 - Description of Test Methods (TX) NA S7.6.4.42
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
        description="NA | Item #00585 | LEN:3",
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
        description="NA | Item #00586 | LEN:4",
    )

    om1_3: CE = Field(
        validation_alias=AliasChoices(
            "om1_3",
            "producer_s_test_observation_id",
            "OM1.3",
        ),
        serialization_alias="OM1.3",
        title="Producer's test / observation ID",
        description="R | Item #00587",
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
        description="NA | Item #00588 | Table 0125 - VALUE TYPE | LEN:12",
    )

    om1_5: str = Field(
        validation_alias=AliasChoices(
            "om1_5",
            "specimen_required",
            "OM1.5",
        ),
        serialization_alias="OM1.5",
        title="Specimen Required",
        description="R | Item #00589 | Table 0136 - Y/N Indicator | LEN:1",
    )

    om1_6: CE = Field(
        validation_alias=AliasChoices(
            "om1_6",
            "producer_id",
            "OM1.6",
        ),
        serialization_alias="OM1.6",
        title="Producer ID",
        description="R | Item #00590",
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
        description="NA | Item #00591",
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
        description="NA | Item #00592",
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
        description="R | Item #00593 | LEN:200",
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
        description="NA | Item #00594 | LEN:30",
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
        description="NA | Item #00595 | LEN:8",
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
        description="NA | Item #00596 | LEN:200",
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
        description="NA | Item #00597 | Table 0136 - Y/N Indicator | LEN:1",
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
        description="NA | Item #00598",
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
        description="NA | Item #00599",
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
        description="NA | Item #00600 | Table 0136 - Y/N Indicator | LEN:1",
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
        description="NA | Item #00601 | LEN:1",
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
        description="NA | Item #00602 | LEN:40",
    )

    om1_19: str = Field(
        validation_alias=AliasChoices(
            "om1_19",
            "nature_of_test_observation",
            "OM1.19",
        ),
        serialization_alias="OM1.19",
        title="Nature of test / observation",
        description=(
            "R | Item #00603 | Table 0174 - NATURE OF TEST/OBSERVATION | LEN:1"
        ),
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
        description="NA | Item #00604",
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
        description="NA | Item #00605 | LEN:20",
    )

    om1_22: TS = Field(
        validation_alias=AliasChoices(
            "om1_22",
            "date_time_stamp_for_any_change_in_definition_for_obs",
            "OM1.22",
        ),
        serialization_alias="OM1.22",
        title="Date / time stamp for any change in definition for obs",
        description="R | Item #00606",
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
        description="NA | Item #00607",
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
        description="NA | Item #00608 | LEN:20",
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
        description="NA | Item #00609 | LEN:20",
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
        description=(
            "NA | Item #00610 | Table 0168 - PROCESSING PRIORITY | LEN:40"
        ),
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
        description="NA | Item #00611 | Table 0169 - REPORTIN PRIORITY | LEN:5",
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
        description="NA | Item #00612",
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
        description="NA | Item #00613",
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
        description="NA | Item #00614 | LEN:400",
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
        description=(
            "NA | Item #00615 | Table 0177 - CONFIDENTIALITY CODE | LEN:1"
        ),
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
        description="NA | Item #00616",
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
        description="NA | Item #00617",
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
        description="NA | Item #00618",
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
        description="NA | Item #00619",
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
        description="NA | Item #00620 | LEN:80",
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
        description="NA | Item #00621",
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
        description="NA | Item #00622",
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
        description="NA | Item #00623",
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
        description="NA | Item #00624",
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
        description="NA | Item #00625 | LEN:60",
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
        description="NA | Item #00626",
    )

    @field_validator("om1_2", "om1_24", "om1_25", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
