"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PEO
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class PEO(HL7Model):
    """Product Experience Observation (S7.12.2).

    Attributes
    ----------
    peo_1 : list[CWE] | None
        PEO.1 - Event Identifiers Used (CWE) O rep S7.12.2.1 | 9999 - no table for CE

    peo_2 : list[CWE] | None
        PEO.2 - Event Symptom/Diagnosis Code (CWE) O rep S7.12.2.2 | 9999 - no table for CE

    peo_3 : str
        PEO.3 - Event Onset Date/Time (DTM) R S7.12.2.3

    peo_4 : str | None
        PEO.4 - Event Exacerbation Date/Time (DTM) O S7.12.2.4

    peo_5 : str | None
        PEO.5 - Event Improved Date/Time (DTM) O S7.12.2.5

    peo_6 : str | None
        PEO.6 - Event Ended Data/Time (DTM) O S7.12.2.6

    peo_7 : list[XAD] | None
        PEO.7 - Event Location Occurred Address (XAD) O rep S7.12.2.7

    peo_8 : list[str] | None
        PEO.8 - Event Qualification (ID) O rep S7.12.2.8 | 0237 - Event Qualification

    peo_9 : str | None
        PEO.9 - Event Serious (ID) O S7.12.2.9 | 0238 - Event Seriousness

    peo_10 : str | None
        PEO.10 - Event Expected (ID) O S7.12.2.10 | 0239 - Event Expected

    peo_11 : list[str] | None
        PEO.11 - Event Outcome (ID) O rep S7.12.2.11 | 0240 - Event Consequence

    peo_12 : str | None
        PEO.12 - Patient Outcome (ID) O S7.12.2.12 | 0241 - Patient Outcome

    peo_13 : list[str] | None
        PEO.13 - Event Description from Others (FT) O rep S7.12.2.13

    peo_14 : list[str] | None
        PEO.14 - Event Description from Original Reporter (FT) O rep S7.12.2.14

    peo_15 : list[str] | None
        PEO.15 - Event Description from Patient (FT) O rep S7.12.2.15

    peo_16 : list[str] | None
        PEO.16 - Event Description from Practitioner (FT) O rep S7.12.2.16

    peo_17 : list[str] | None
        PEO.17 - Event Description from Autopsy (FT) O rep S7.12.2.17

    peo_18 : list[CWE] | None
        PEO.18 - Cause Of Death (CWE) O rep S7.12.2.18 | 9999 - no table for CE

    peo_19 : list[XPN] | None
        PEO.19 - Primary Observer Name (XPN) O rep S7.12.2.19

    peo_20 : list[XAD] | None
        PEO.20 - Primary Observer Address (XAD) O rep S7.12.2.20

    peo_21 : list[XTN] | None
        PEO.21 - Primary Observer Telephone (XTN) O rep S7.12.2.21

    peo_22 : str | None
        PEO.22 - Primary Observer's Qualification (ID) O S7.12.2.22 | 0242 - Primary Observer's Qualification

    peo_23 : str | None
        PEO.23 - Confirmation Provided By (ID) O S7.12.2.23 | 0242 - Primary Observer's Qualification

    peo_24 : str | None
        PEO.24 - Primary Observer Aware Date/Time (DTM) O S7.12.2.24

    peo_25 : str | None
        PEO.25 - Primary Observer's identity May Be Divulged (ID) O S7.12.2.25 | 0243 - Identity May Be Divulged
    """

    peo_1: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_1",
            "event_identifiers_used",
            "PEO.1",
        ),
        serialization_alias="PEO.1",
        title="Event Identifiers Used",
        description="O | Item #01073 | Table 9999 - no table for CE",
    )

    peo_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_2",
            "event_symptom_diagnosis_code",
            "PEO.2",
        ),
        serialization_alias="PEO.2",
        title="Event Symptom/Diagnosis Code",
        description="O | Item #01074 | Table 9999 - no table for CE",
    )

    peo_3: str = Field(
        validation_alias=AliasChoices(
            "peo_3",
            "event_onset_date_time",
            "PEO.3",
        ),
        serialization_alias="PEO.3",
        title="Event Onset Date/Time",
        description="R | Item #01075",
    )

    peo_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_4",
            "event_exacerbation_date_time",
            "PEO.4",
        ),
        serialization_alias="PEO.4",
        title="Event Exacerbation Date/Time",
        description="O | Item #01076",
    )

    peo_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_5",
            "event_improved_date_time",
            "PEO.5",
        ),
        serialization_alias="PEO.5",
        title="Event Improved Date/Time",
        description="O | Item #01077",
    )

    peo_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_6",
            "event_ended_data_time",
            "PEO.6",
        ),
        serialization_alias="PEO.6",
        title="Event Ended Data/Time",
        description="O | Item #01078",
    )

    peo_7: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_7",
            "event_location_occurred_address",
            "PEO.7",
        ),
        serialization_alias="PEO.7",
        title="Event Location Occurred Address",
        description="O | Item #01079",
    )

    peo_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_8",
            "event_qualification",
            "PEO.8",
        ),
        serialization_alias="PEO.8",
        title="Event Qualification",
        description=(
            "O | Item #01080 | Table 0237 - Event Qualification | LEN:1"
        ),
    )

    peo_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_9",
            "event_serious",
            "PEO.9",
        ),
        serialization_alias="PEO.9",
        title="Event Serious",
        description="O | Item #01081 | Table 0238 - Event Seriousness | LEN:1",
    )

    peo_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_10",
            "event_expected",
            "PEO.10",
        ),
        serialization_alias="PEO.10",
        title="Event Expected",
        description="O | Item #01082 | Table 0239 - Event Expected | LEN:1",
    )

    peo_11: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_11",
            "event_outcome",
            "PEO.11",
        ),
        serialization_alias="PEO.11",
        title="Event Outcome",
        description="O | Item #01083 | Table 0240 - Event Consequence | LEN:1",
    )

    peo_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_12",
            "patient_outcome",
            "PEO.12",
        ),
        serialization_alias="PEO.12",
        title="Patient Outcome",
        description="O | Item #01084 | Table 0241 - Patient Outcome | LEN:1",
    )

    peo_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_13",
            "event_description_from_others",
            "PEO.13",
        ),
        serialization_alias="PEO.13",
        title="Event Description from Others",
        description="O | Item #01085",
    )

    peo_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_14",
            "event_description_from_original_reporter",
            "PEO.14",
        ),
        serialization_alias="PEO.14",
        title="Event Description from Original Reporter",
        description="O | Item #01086",
    )

    peo_15: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_15",
            "event_description_from_patient",
            "PEO.15",
        ),
        serialization_alias="PEO.15",
        title="Event Description from Patient",
        description="O | Item #01087",
    )

    peo_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_16",
            "event_description_from_practitioner",
            "PEO.16",
        ),
        serialization_alias="PEO.16",
        title="Event Description from Practitioner",
        description="O | Item #01088",
    )

    peo_17: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_17",
            "event_description_from_autopsy",
            "PEO.17",
        ),
        serialization_alias="PEO.17",
        title="Event Description from Autopsy",
        description="O | Item #01089",
    )

    peo_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_18",
            "cause_of_death",
            "PEO.18",
        ),
        serialization_alias="PEO.18",
        title="Cause Of Death",
        description="O | Item #01090 | Table 9999 - no table for CE",
    )

    peo_19: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_19",
            "primary_observer_name",
            "PEO.19",
        ),
        serialization_alias="PEO.19",
        title="Primary Observer Name",
        description="O | Item #01091",
    )

    peo_20: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_20",
            "primary_observer_address",
            "PEO.20",
        ),
        serialization_alias="PEO.20",
        title="Primary Observer Address",
        description="O | Item #01092",
    )

    peo_21: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_21",
            "primary_observer_telephone",
            "PEO.21",
        ),
        serialization_alias="PEO.21",
        title="Primary Observer Telephone",
        description="O | Item #01093",
    )

    peo_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_22",
            "primary_observer_s_qualification",
            "PEO.22",
        ),
        serialization_alias="PEO.22",
        title="Primary Observer's Qualification",
        description=(
            "O | Item #01094 | Table 0242 - Primary Observer's Qualification | "
            "LEN:1"
        ),
    )

    peo_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_23",
            "confirmation_provided_by",
            "PEO.23",
        ),
        serialization_alias="PEO.23",
        title="Confirmation Provided By",
        description=(
            "O | Item #01095 | Table 0242 - Primary Observer's Qualification | "
            "LEN:1"
        ),
    )

    peo_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_24",
            "primary_observer_aware_date_time",
            "PEO.24",
        ),
        serialization_alias="PEO.24",
        title="Primary Observer Aware Date/Time",
        description="O | Item #01096",
    )

    peo_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "peo_25",
            "primary_observer_s_identity_may_be_divulged",
            "PEO.25",
        ),
        serialization_alias="PEO.25",
        title="Primary Observer's identity May Be Divulged",
        description=(
            "O | Item #01097 | Table 0243 - Identity May Be Divulged | LEN:2"
        ),
    )

    @field_validator("peo_3", "peo_4", "peo_5", "peo_6", "peo_24", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
