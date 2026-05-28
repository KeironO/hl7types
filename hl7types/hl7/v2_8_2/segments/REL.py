"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: REL
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class REL(BaseModel):
    """HL7 v2 REL segment."""

    rel_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_1",
            "set_id_rel",
            "REL.1",
        ),
        serialization_alias="REL.1",
        title="Set ID -REL",
        description="Item #2240",
    )

    rel_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rel_2",
            "relationship_type",
            "REL.2",
        ),
        serialization_alias="REL.2",
        title="Relationship Type",
        description="Item #2241",
    )

    rel_3: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "rel_3",
            "this_relationship_instance_identifier",
            "REL.3",
        ),
        serialization_alias="REL.3",
        title="This Relationship Instance Identifier",
        description="Item #2242",
    )

    rel_4: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "rel_4",
            "source_information_instance_identifier",
            "REL.4",
        ),
        serialization_alias="REL.4",
        title="Source Information Instance Identifier",
        description="Item #2243",
    )

    rel_5: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "rel_5",
            "target_information_instance_identifier",
            "REL.5",
        ),
        serialization_alias="REL.5",
        title="Target Information Instance Identifier",
        description="Item #2244",
    )

    rel_6: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_6",
            "asserting_entity_instance_id",
            "REL.6",
        ),
        serialization_alias="REL.6",
        title="Asserting Entity Instance ID",
        description="Item #2245",
    )

    rel_7: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_7",
            "asserting_person",
            "REL.7",
        ),
        serialization_alias="REL.7",
        title="Asserting Person",
        description="Item #2246",
    )

    rel_8: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_8",
            "asserting_organization",
            "REL.8",
        ),
        serialization_alias="REL.8",
        title="Asserting Organization",
        description="Item #2247",
    )

    rel_9: XAD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_9",
            "assertor_address",
            "REL.9",
        ),
        serialization_alias="REL.9",
        title="Assertor Address",
        description="Item #2248",
    )

    rel_10: XTN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_10",
            "assertor_contact",
            "REL.10",
        ),
        serialization_alias="REL.10",
        title="Assertor Contact",
        description="Item #2249",
    )

    rel_11: DR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_11",
            "assertion_date_range",
            "REL.11",
        ),
        serialization_alias="REL.11",
        title="Assertion Date Range",
        description="Item #2250",
    )

    rel_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_12",
            "negation_indicator",
            "REL.12",
        ),
        serialization_alias="REL.12",
        title="Negation Indicator",
        description="Item #2251 | Table HL70136",
    )

    rel_13: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_13",
            "certainty_of_relationship",
            "REL.13",
        ),
        serialization_alias="REL.13",
        title="Certainty of Relationship",
        description="Item #2252",
    )

    rel_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_14",
            "priority_no",
            "REL.14",
        ),
        serialization_alias="REL.14",
        title="Priority No",
        description="Item #2253",
    )

    rel_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_15",
            "priority_sequence_no_rel_preference_for_consideration",
            "REL.15",
        ),
        serialization_alias="REL.15",
        title="Priority  Sequence No (rel preference for consideration)",
        description="Item #2254",
    )

    rel_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rel_16",
            "separability_indicator",
            "REL.16",
        ),
        serialization_alias="REL.16",
        title="Separability Indicator",
        description="Item #2255 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
