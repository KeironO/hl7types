"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: REL
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class REL(HL7Model):
    """Clinical Relationship Segment (S12.4.5).

    Attributes
    ----------
    rel_1 : str | None
        REL.1 - Set ID -REL (SI) C S12.4.5.1

    rel_2 : CWE
        REL.2 - Relationship Type (CWE) R S12.4.5.2

    rel_3 : EI
        REL.3 - This Relationship Instance Identifier (EI) R S12.4.5.3

    rel_4 : EI
        REL.4 - Source Information Instance Identifier (EI) R S12.4.5.4

    rel_5 : EI
        REL.5 - Target Information Instance Identifier (EI) R S12.4.5.5

    rel_6 : EI | None
        REL.6 - Asserting Entity Instance ID (EI) O S12.4.5.6

    rel_7 : XCN | None
        REL.7 - Asserting Person (XCN) O S12.4.5.7

    rel_8 : XON | None
        REL.8 - Asserting Organization (XON) O S12.4.5.8

    rel_9 : XAD | None
        REL.9 - Assertor Address (XAD) O S12.4.5.9

    rel_10 : XTN | None
        REL.10 - Assertor Contact (XTN) O S12.4.5.10

    rel_11 : DR | None
        REL.11 - Assertion Date Range (DR) O S12.4.5.11

    rel_12 : str | None
        REL.12 - Negation Indicator (ID) O S12.4.5.12 | 0136 - Yes/no Indicator

    rel_13 : CWE | None
        REL.13 - Certainty of Relationship (CWE) O S12.4.5.13

    rel_14 : str | None
        REL.14 - Priority No (NM) O S12.4.5.14

    rel_15 : str | None
        REL.15 - Priority  Sequence No (rel preference for consideration) (NM) O S12.4.5.15

    rel_16 : str | None
        REL.16 - Separability Indicator (ID) O S12.4.5.16 | 0136 - Yes/no Indicator
    """

    rel_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_1",
            "set_id_rel",
            "REL.1",
        ),
        serialization_alias="REL.1",
        title="Set ID -REL",
        description="C | Item #02240 | LEN:4",
    )

    rel_2: CWE = Field(
        validation_alias=AliasChoices(
            "rel_2",
            "relationship_type",
            "REL.2",
        ),
        serialization_alias="REL.2",
        title="Relationship Type",
        description="R | Item #02241",
    )

    rel_3: EI = Field(
        validation_alias=AliasChoices(
            "rel_3",
            "this_relationship_instance_identifier",
            "REL.3",
        ),
        serialization_alias="REL.3",
        title="This Relationship Instance Identifier",
        description="R | Item #02242",
    )

    rel_4: EI = Field(
        validation_alias=AliasChoices(
            "rel_4",
            "source_information_instance_identifier",
            "REL.4",
        ),
        serialization_alias="REL.4",
        title="Source Information Instance Identifier",
        description="R | Item #02243",
    )

    rel_5: EI = Field(
        validation_alias=AliasChoices(
            "rel_5",
            "target_information_instance_identifier",
            "REL.5",
        ),
        serialization_alias="REL.5",
        title="Target Information Instance Identifier",
        description="R | Item #02244",
    )

    rel_6: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_6",
            "asserting_entity_instance_id",
            "REL.6",
        ),
        serialization_alias="REL.6",
        title="Asserting Entity Instance ID",
        description="O | Item #02245",
    )

    rel_7: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_7",
            "asserting_person",
            "REL.7",
        ),
        serialization_alias="REL.7",
        title="Asserting Person",
        description="O | Item #02246",
    )

    rel_8: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_8",
            "asserting_organization",
            "REL.8",
        ),
        serialization_alias="REL.8",
        title="Asserting Organization",
        description="O | Item #02247",
    )

    rel_9: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_9",
            "assertor_address",
            "REL.9",
        ),
        serialization_alias="REL.9",
        title="Assertor Address",
        description="O | Item #02248",
    )

    rel_10: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_10",
            "assertor_contact",
            "REL.10",
        ),
        serialization_alias="REL.10",
        title="Assertor Contact",
        description="O | Item #02249",
    )

    rel_11: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_11",
            "assertion_date_range",
            "REL.11",
        ),
        serialization_alias="REL.11",
        title="Assertion Date Range",
        description="O | Item #02250",
    )

    rel_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_12",
            "negation_indicator",
            "REL.12",
        ),
        serialization_alias="REL.12",
        title="Negation Indicator",
        description="O | Item #02251 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    rel_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_13",
            "certainty_of_relationship",
            "REL.13",
        ),
        serialization_alias="REL.13",
        title="Certainty of Relationship",
        description="O | Item #02252",
    )

    rel_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_14",
            "priority_no",
            "REL.14",
        ),
        serialization_alias="REL.14",
        title="Priority No",
        description="O | Item #02253",
    )

    rel_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_15",
            "priority_sequence_no_rel_preference_for_consideration",
            "REL.15",
        ),
        serialization_alias="REL.15",
        title="Priority  Sequence No (rel preference for consideration)",
        description="O | Item #02254",
    )

    rel_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_16",
            "separability_indicator",
            "REL.16",
        ),
        serialization_alias="REL.16",
        title="Separability Indicator",
        description="O | Item #02255 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    @field_validator("rel_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("rel_14", "rel_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
