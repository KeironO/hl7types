"""Security-oriented XML parser boundary tests.

These tests do not prove the XML parser is safe in every respect. They freeze a
minimum contract: XML documents containing DTD/entity constructs must not be
successfully decoded into HL7 models.
"""
from __future__ import annotations

from xml.etree.ElementTree import ParseError

import pytest
from pydantic import ValidationError

from hl7types import decode_xml
from hl7types.hl7.v2_5_1.messages.ACK import ACK


def test_xml_decode_does_not_accept_external_entity_payload() -> None:
    xml = """<?xml version="1.0"?>
<!DOCTYPE ACK [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<ACK xmlns="urn:hl7-org:v2xml">
  <MSH>
    <MSH.7><TS.1>20240101120000</TS.1></MSH.7>
    <MSH.9><MSG.1>ACK</MSG.1></MSH.9>
    <MSH.10>MSG001</MSH.10>
    <MSH.11><PT.1>P</PT.1></MSH.11>
    <MSH.12><VID.1>2.5.1</VID.1></MSH.12>
  </MSH>
  <MSA>
    <MSA.1>AA</MSA.1>
    <MSA.2>&xxe;</MSA.2>
  </MSA>
</ACK>
"""

    with pytest.raises((ValueError, ParseError, ValidationError)):
        decode_xml(xml, msg_cls=ACK, strict=True)


def test_xml_decode_does_not_accept_entity_expansion_payload() -> None:
    xml = """<?xml version="1.0"?>
<!DOCTYPE ACK [
  <!ENTITY a "aaaaaaaaaa">
  <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
]>
<ACK xmlns="urn:hl7-org:v2xml">
  <MSH>
    <MSH.7><TS.1>20240101120000</TS.1></MSH.7>
    <MSH.9><MSG.1>ACK</MSG.1></MSH.9>
    <MSH.10>MSG001</MSH.10>
    <MSH.11><PT.1>P</PT.1></MSH.11>
    <MSH.12><VID.1>2.5.1</VID.1></MSH.12>
  </MSH>
  <MSA>
    <MSA.1>AA</MSA.1>
    <MSA.2>&b;</MSA.2>
  </MSA>
</ACK>
"""

    with pytest.raises((ValueError, ParseError, ValidationError)):
        decode_xml(xml, msg_cls=ACK, strict=True)
