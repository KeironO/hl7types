"""Security-oriented profile parser boundary tests.

These tests freeze a minimum contract: conformance profile XML documents
containing DTD/entity constructs must not be successfully parsed.
"""
from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from hl7types.profiles.parser import parse_profile, parse_tables


def _write_tmp(tmp_path: Path, content: str, name: str = "profile.xml") -> Path:
    p = tmp_path / name
    p.write_text(textwrap.dedent(content))
    return p


_MINIMAL_PROFILE = """\
    <?xml version="1.0"?>
    {preamble}
    <HL7v2xConformanceProfile HL7Version="2.5.1">
      <MetaData Name="Test Profile"/>
      <HL7v2xStaticDef MsgType="ACK" EventType="A01" MsgStructID="ACK_A01"/>
    </HL7v2xConformanceProfile>
"""

_MINIMAL_TABLE = """\
    <?xml version="1.0"?>
    {preamble}
    <HL7Tables>
      <hl7table id="0001">
        <tableElement code="AA"/>
      </hl7table>
    </HL7Tables>
"""


def test_parse_profile_rejects_external_entity(tmp_path: Path) -> None:
    preamble = """<!DOCTYPE x [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>"""
    path = _write_tmp(tmp_path, _MINIMAL_PROFILE.format(preamble=preamble))
    with pytest.raises(Exception):
        parse_profile(path)


def test_parse_profile_rejects_entity_expansion(tmp_path: Path) -> None:
    preamble = """<!DOCTYPE x [
      <!ENTITY a "aaaaaaaaaa">
      <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
    ]>"""
    path = _write_tmp(tmp_path, _MINIMAL_PROFILE.format(preamble=preamble))
    with pytest.raises(Exception):
        parse_profile(path)


def test_parse_tables_rejects_external_entity(tmp_path: Path) -> None:
    preamble = """<!DOCTYPE x [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>"""
    path = _write_tmp(tmp_path, _MINIMAL_TABLE.format(preamble=preamble), "tables.xml")
    with pytest.raises(Exception):
        parse_tables(path)


def test_parse_tables_rejects_entity_expansion(tmp_path: Path) -> None:
    preamble = """<!DOCTYPE x [
      <!ENTITY a "aaaaaaaaaa">
      <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
    ]>"""
    path = _write_tmp(tmp_path, _MINIMAL_TABLE.format(preamble=preamble), "tables.xml")
    with pytest.raises(Exception):
        parse_tables(path)
