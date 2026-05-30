"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PPV_PCA.OBRanyHL7Segment_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class PPV_PCA_OBRanyHL7Segment_SUPPGRP(HL7Model):
    """HL7 v2 PPV_PCA.OBRanyHL7Segment_SUPPGRP group."""

    pass

    model_config = {"populate_by_name": True}
