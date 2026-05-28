"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDF
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.RCD import RCD


class RDF(BaseModel):
    """HL7 v2 RDF segment."""

    rdf_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rdf_1",
            "number_of_columns_per_row",
            "RDF.1",
        ),
        serialization_alias="RDF.1",
        title="Number of Columns per Row",
        description="Item #701",
    )

    rdf_2: list[RCD] = Field(
        default=...,
        validation_alias=AliasChoices(
            "rdf_2",
            "column_description",
            "RDF.2",
        ),
        serialization_alias="RDF.2",
        title="Column Description",
        description="Item #702",
    )

    model_config = {"populate_by_name": True}
