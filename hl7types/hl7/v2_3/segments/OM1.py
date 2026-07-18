"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OM1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM1(HL7Model):
    """General - fields that apply to most observations (S8.7.3).

    Attributes
    ----------
    om1_1 : str | None
        OM1.1 - Sequence Number - Test/ Observation Master File (NM) O S8.7.3

    om1_2 : CE
        OM1.2 - Producer's Test/Observation ID (CE) R S8.7.3.2

    om1_3 : list[str] | None
        OM1.3 - Permitted Data Types (ID) O rep S8.7.3.3 | 0125 - Value Type

    om1_4 : str
        OM1.4 - Specimen Required (ID) R S8.7.3.4 | 0136 - Yes/No Indicator

    om1_5 : CE
        OM1.5 - Producer ID (CE) R S8.7.3.5

    om1_6 : CE | None
        OM1.6 - Observation Description (CE) O S8.7.3.6

    om1_7 : CE | None
        OM1.7 - Other Test/Observation IDs for the Observation (CE) O S8.7.3.7

    om1_8 : list[str]
        OM1.8 - Other Names (ST) R rep S8.7.3.8

    om1_9 : str | None
        OM1.9 - Preferred Report Name for the Observation (ST) O S8.7.3.9

    om1_10 : str | None
        OM1.10 - Preferred Short Name or Mnemonic for Observation (ST) O S8.7.3.10

    om1_11 : str | None
        OM1.11 - Preferred Long Name for the Observation (ST) O S8.7.3.11

    om1_12 : str | None
        OM1.12 - Orderability (ID) O S8.7.3.12 | 0136 - Yes/No Indicator

    om1_13 : list[CE] | None
        OM1.13 - Identity of Instrument Used to Perfrom this Study (CE) O rep S8.7.3.13

    om1_14 : CE | None
        OM1.14 - Coded Representation of Method (CE) O S8.7.3.14

    om1_15 : str | None
        OM1.15 - Portable (ID) O S8.7.3.15 | 0136 - Yes/No Indicator

    om1_16 : list[CE] | None
        OM1.16 - Observation Producing Department/Section (CE) O rep S8.7.3.16

    om1_17 : str | None
        OM1.17 - Telephone Number of Section (TN) O S8.7.3.17

    om1_18 : str | None
        OM1.18 - Nature of Test/Observation (ID) O S8.7.3.18 | 0174 - Nature of Test/Observation

    om1_19 : CE | None
        OM1.19 - Report Subheader (CE) O S8.7.3.19

    om1_20 : str | None
        OM1.20 - Report Display Order (ST) O S8.7.3.20

    om1_21 : TS | None
        OM1.21 - Date/Time Stamp for any change in Def Attri for Obs (TS) NA S8.7.3.21

    om1_22 : TS | None
        OM1.22 - Effective Date/Time of Change in Test Proc. that make Results Non-Comparable (TS) NA S8.7.3.22

    om1_23 : str | None
        OM1.23 - Typical Turn-Around Time (NM) O S8.7.3.23

    om1_24 : str | None
        OM1.24 - Processing Time (NM) O S8.7.3.24

    om1_25 : list[str] | None
        OM1.25 - Processing Priority (ID) O rep S8.7.3.25 | 0168 - Processing Priority

    om1_26 : str | None
        OM1.26 - Reporting Priority (ID) O S8.7.3.26 | 0169 - Reporting Priority

    om1_27 : list[CE] | None
        OM1.27 - Outside Site(s) Where Observation may be Performed (CE) O rep S8.7.3.27

    om1_28 : AD | None
        OM1.28 - Address of Outside Site(s) (AD) O S8.7.3.28

    om1_29 : str | None
        OM1.29 - Phone Number of Outside Site (TN) O S8.7.3.29

    om1_30 : str | None
        OM1.30 - Confidentiality Code (ID) O S8.7.3.30 | 0177 - Confidentiality code

    om1_31 : CE | None
        OM1.31 - Observations Required to Interpret the Observation (CE) O S8.7.3.31

    om1_32 : str | None
        OM1.32 - Interpretation of Observations (TX) O S8.7.3.32

    om1_33 : CE | None
        OM1.33 - Contraindications to Observations (CE) O S8.7.3.33

    om1_34 : list[CE] | None
        OM1.34 - Reflex Tests/Observations (CE) O rep S8.7.3.34

    om1_35 : str | None
        OM1.35 - Rules that Trigger Reflex Testing (ST) O S8.7.3.35

    om1_36 : CE | None
        OM1.36 - Fixed Canned Message (CE) O S8.7.3.36

    om1_37 : str | None
        OM1.37 - Patient Preparation (TX) O S8.7.3.37

    om1_38 : CE | None
        OM1.38 - Procedure Medication (CE) O S8.7.3.38

    om1_39 : str | None
        OM1.39 - Factors that may Effect the Observation (TX) O S8.7.3.39

    om1_40 : list[str] | None
        OM1.40 - Test/Observation Performance Schedule (ST) O rep S8.7.3.40

    om1_41 : str | None
        OM1.41 - Description of Test Methods (TX) O S8.7.3.41

    om1_42 : CE | None
        OM1.42 - Kind of Quantity Observed (CE) O S8.7.3.42

    om1_43 : CE | None
        OM1.43 - Point versus Interval (CE) O S8.7.3.43

    om1_44 : str | None
        OM1.44 - Challenge information (TX) O S8.7.3.44

    om1_45 : CE | None
        OM1.45 - Relationship modifier (CE) O S8.7.3.45

    om1_46 : CE | None
        OM1.46 - Target anatomic site of test (CE) O S8.7.3.46

    om1_47 : CE | None
        OM1.47 - Modality of imaging measurement (CE) O S8.7.3.47
    """

    om1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_1",
            "sequence_number_test_observation_master_file",
            "OM1.1",
        ),
        serialization_alias="OM1.1",
        title="Sequence Number - Test/ Observation Master File",
        description="O | Item #00586 | LEN:4",
    )

    om1_2: CE = Field(
        validation_alias=AliasChoices(
            "om1_2",
            "producer_s_test_observation_id",
            "OM1.2",
        ),
        serialization_alias="OM1.2",
        title="Producer's Test/Observation ID",
        description="R | Item #00587",
    )

    om1_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_3",
            "permitted_data_types",
            "OM1.3",
        ),
        serialization_alias="OM1.3",
        title="Permitted Data Types",
        description="O | Item #00588 | Table 0125 - Value Type | LEN:12",
    )

    om1_4: str = Field(
        validation_alias=AliasChoices(
            "om1_4",
            "specimen_required",
            "OM1.4",
        ),
        serialization_alias="OM1.4",
        title="Specimen Required",
        description="R | Item #00589 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    om1_5: CE = Field(
        validation_alias=AliasChoices(
            "om1_5",
            "producer_id",
            "OM1.5",
        ),
        serialization_alias="OM1.5",
        title="Producer ID",
        description="R | Item #00590",
    )

    om1_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_6",
            "observation_description",
            "OM1.6",
        ),
        serialization_alias="OM1.6",
        title="Observation Description",
        description="O | Item #00591",
    )

    om1_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_7",
            "other_test_observation_ids_for_the_observation",
            "OM1.7",
        ),
        serialization_alias="OM1.7",
        title="Other Test/Observation IDs for the Observation",
        description="O | Item #00592",
    )

    om1_8: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "om1_8",
            "other_names",
            "OM1.8",
        ),
        serialization_alias="OM1.8",
        title="Other Names",
        description="R | Item #00593 | LEN:200",
    )

    om1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_9",
            "preferred_report_name_for_the_observation",
            "OM1.9",
        ),
        serialization_alias="OM1.9",
        title="Preferred Report Name for the Observation",
        description="O | Item #00594 | LEN:30",
    )

    om1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_10",
            "preferred_short_name_or_mnemonic_for_observation",
            "OM1.10",
        ),
        serialization_alias="OM1.10",
        title="Preferred Short Name or Mnemonic for Observation",
        description="O | Item #00595 | LEN:8",
    )

    om1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_11",
            "preferred_long_name_for_the_observation",
            "OM1.11",
        ),
        serialization_alias="OM1.11",
        title="Preferred Long Name for the Observation",
        description="O | Item #00596 | LEN:200",
    )

    om1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_12",
            "orderability",
            "OM1.12",
        ),
        serialization_alias="OM1.12",
        title="Orderability",
        description="O | Item #00597 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    om1_13: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_13",
            "identity_of_instrument_used_to_perfrom_this_study",
            "OM1.13",
        ),
        serialization_alias="OM1.13",
        title="Identity of Instrument Used to Perfrom this Study",
        description="O | Item #00598",
    )

    om1_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_14",
            "coded_representation_of_method",
            "OM1.14",
        ),
        serialization_alias="OM1.14",
        title="Coded Representation of Method",
        description="O | Item #00599",
    )

    om1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_15",
            "portable",
            "OM1.15",
        ),
        serialization_alias="OM1.15",
        title="Portable",
        description="O | Item #00600 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    om1_16: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_16",
            "observation_producing_department_section",
            "OM1.16",
        ),
        serialization_alias="OM1.16",
        title="Observation Producing Department/Section",
        description="O | Item #00601",
    )

    om1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_17",
            "telephone_number_of_section",
            "OM1.17",
        ),
        serialization_alias="OM1.17",
        title="Telephone Number of Section",
        description="O | Item #00602 | LEN:40",
    )

    om1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_18",
            "nature_of_test_observation",
            "OM1.18",
        ),
        serialization_alias="OM1.18",
        title="Nature of Test/Observation",
        description=(
            "O | Item #00603 | Table 0174 - Nature of Test/Observation | LEN:1"
        ),
    )

    om1_19: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_19",
            "report_subheader",
            "OM1.19",
        ),
        serialization_alias="OM1.19",
        title="Report Subheader",
        description="O | Item #00604",
    )

    om1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_20",
            "report_display_order",
            "OM1.20",
        ),
        serialization_alias="OM1.20",
        title="Report Display Order",
        description="O | Item #00605 | LEN:20",
    )

    om1_21: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_21",
            "date_time_stamp_for_any_change_in_def_attri_for_obs",
            "OM1.21",
        ),
        serialization_alias="OM1.21",
        title="Date/Time Stamp for any change in Def Attri for Obs",
        description="NA | Item #00606",
    )

    om1_22: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_22",
            "effective_date_time_of_change_in_test_proc_that_make_results_non_comparable",
            "OM1.22",
        ),
        serialization_alias="OM1.22",
        title=(
            "Effective Date/Time of Change in Test Proc. that make Results "
            "Non-Comparable"
        ),
        description="NA | Item #00607",
    )

    om1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_23",
            "typical_turn_around_time",
            "OM1.23",
        ),
        serialization_alias="OM1.23",
        title="Typical Turn-Around Time",
        description="O | Item #00608 | LEN:20",
    )

    om1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_24",
            "processing_time",
            "OM1.24",
        ),
        serialization_alias="OM1.24",
        title="Processing Time",
        description="O | Item #00609 | LEN:20",
    )

    om1_25: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_25",
            "processing_priority",
            "OM1.25",
        ),
        serialization_alias="OM1.25",
        title="Processing Priority",
        description=(
            "O | Item #00610 | Table 0168 - Processing Priority | LEN:40"
        ),
    )

    om1_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_26",
            "reporting_priority",
            "OM1.26",
        ),
        serialization_alias="OM1.26",
        title="Reporting Priority",
        description="O | Item #00611 | Table 0169 - Reporting Priority | LEN:5",
    )

    om1_27: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_27",
            "outside_site_s_where_observation_may_be_performed",
            "OM1.27",
        ),
        serialization_alias="OM1.27",
        title="Outside Site(s) Where Observation may be Performed",
        description="O | Item #00612",
    )

    om1_28: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_28",
            "address_of_outside_site_s",
            "OM1.28",
        ),
        serialization_alias="OM1.28",
        title="Address of Outside Site(s)",
        description="O | Item #00613",
    )

    om1_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_29",
            "phone_number_of_outside_site",
            "OM1.29",
        ),
        serialization_alias="OM1.29",
        title="Phone Number of Outside Site",
        description="O | Item #00614 | LEN:400",
    )

    om1_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_30",
            "confidentiality_code",
            "OM1.30",
        ),
        serialization_alias="OM1.30",
        title="Confidentiality Code",
        description=(
            "O | Item #00615 | Table 0177 - Confidentiality code | LEN:1"
        ),
    )

    om1_31: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_31",
            "observations_required_to_interpret_the_observation",
            "OM1.31",
        ),
        serialization_alias="OM1.31",
        title="Observations Required to Interpret the Observation",
        description="O | Item #00616",
    )

    om1_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_32",
            "interpretation_of_observations",
            "OM1.32",
        ),
        serialization_alias="OM1.32",
        title="Interpretation of Observations",
        description="O | Item #00617",
    )

    om1_33: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_33",
            "contraindications_to_observations",
            "OM1.33",
        ),
        serialization_alias="OM1.33",
        title="Contraindications to Observations",
        description="O | Item #00618",
    )

    om1_34: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_34",
            "reflex_tests_observations",
            "OM1.34",
        ),
        serialization_alias="OM1.34",
        title="Reflex Tests/Observations",
        description="O | Item #00619",
    )

    om1_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_35",
            "rules_that_trigger_reflex_testing",
            "OM1.35",
        ),
        serialization_alias="OM1.35",
        title="Rules that Trigger Reflex Testing",
        description="O | Item #00620 | LEN:80",
    )

    om1_36: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_36",
            "fixed_canned_message",
            "OM1.36",
        ),
        serialization_alias="OM1.36",
        title="Fixed Canned Message",
        description="O | Item #00621",
    )

    om1_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_37",
            "patient_preparation",
            "OM1.37",
        ),
        serialization_alias="OM1.37",
        title="Patient Preparation",
        description="O | Item #00622",
    )

    om1_38: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_38",
            "procedure_medication",
            "OM1.38",
        ),
        serialization_alias="OM1.38",
        title="Procedure Medication",
        description="O | Item #00623",
    )

    om1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_39",
            "factors_that_may_effect_the_observation",
            "OM1.39",
        ),
        serialization_alias="OM1.39",
        title="Factors that may Effect the Observation",
        description="O | Item #00624",
    )

    om1_40: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_40",
            "test_observation_performance_schedule",
            "OM1.40",
        ),
        serialization_alias="OM1.40",
        title="Test/Observation Performance Schedule",
        description="O | Item #00625 | LEN:60",
    )

    om1_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_41",
            "description_of_test_methods",
            "OM1.41",
        ),
        serialization_alias="OM1.41",
        title="Description of Test Methods",
        description="O | Item #00626",
    )

    om1_42: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_42",
            "kind_of_quantity_observed",
            "OM1.42",
        ),
        serialization_alias="OM1.42",
        title="Kind of Quantity Observed",
        description="O | Item #00937",
    )

    om1_43: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_43",
            "point_versus_interval",
            "OM1.43",
        ),
        serialization_alias="OM1.43",
        title="Point versus Interval",
        description="O | Item #00938",
    )

    om1_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_44",
            "challenge_information",
            "OM1.44",
        ),
        serialization_alias="OM1.44",
        title="Challenge information",
        description="O | Item #00939",
    )

    om1_45: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_45",
            "relationship_modifier",
            "OM1.45",
        ),
        serialization_alias="OM1.45",
        title="Relationship modifier",
        description="O | Item #00940",
    )

    om1_46: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_46",
            "target_anatomic_site_of_test",
            "OM1.46",
        ),
        serialization_alias="OM1.46",
        title="Target anatomic site of test",
        description="O | Item #00941",
    )

    om1_47: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_47",
            "modality_of_imaging_measurement",
            "OM1.47",
        ),
        serialization_alias="OM1.47",
        title="Modality of imaging measurement",
        description="O | Item #00942",
    )

    @field_validator("om1_1", "om1_23", "om1_24", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
