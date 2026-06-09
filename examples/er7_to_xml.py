"""Decode an ER7 message and serialise it to HL7 v2 XML.

hl7types supports both directions of the ER7 <-> XML conversion.
This example shows the XML output format for an ACK message and
demonstrates that the round-trip through XML preserves field values.
"""

from hl7types import decode_er7, decode_xml
from hl7types.hl7.v2_5_1.messages import ACK

WIRE = (
    "MSH|^~\\&|LABORDAI|YSBYTY CWMTAFF|HIS|YSBYTY CWMTAFF|20260301120000||ACK|MSG000001|P|2.5.1\r"
    "MSA|AA|MSG000001|Derbyniwyd y neges (Message accepted, boyo)\r"
)


def main() -> None:
    # Decode ER7 -> typed model.
    msg = decode_er7(WIRE, msg_cls=ACK)

    # Serialise to HL7 v2 XML.
    xml_str = msg.model_dump_xml()
    print("=== HL7 v2 XML ===")
    print(xml_str)

    # Decode back from XML -> typed model and verify field values survived.
    msg2 = decode_xml(xml_str, ACK)
    print("=== Round-trip check ===")
    print(f"msa_1 (ack code):  {msg2.MSA.msa_1!r}")
    print(f"msa_2 (ctrl id):   {msg2.MSA.msa_2!r}")
    print(f"msa_3 (text):      {msg2.MSA.msa_3!r}")
    print(f"msh_3 (sending):   {msg2.MSH.msh_3.hd_1!r}")

    # Compact XML (no indentation) is available via pretty=False.
    compact = msg.model_dump_xml(pretty=False)
    print(f"\nCompact XML length: {len(compact)} chars")
    print(compact[:120], "...")


if __name__ == "__main__":
    main()
