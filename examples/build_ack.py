"""Construct ACK messages and serialise them to ER7."""

from hl7types import decode_er7
from hl7types.hl7.v2_5_1.datatypes import CWE, HD, MSG, PT, TS, VID
from hl7types.hl7.v2_5_1.messages import ACK
from hl7types.hl7.v2_5_1.segments import ERR, MSA, MSH

original_id = "MSG000001"


# Build a positive ACK.
msh_pos = MSH(
    msh_3=HD(hd_1="HIS"),
    msh_4=HD(hd_1="YSBYTY CWMTAFF"),
    msh_5=HD(hd_1="LABORDAI"),
    msh_6=HD(hd_1="YSBYTY CWMTAFF"),
    msh_7=TS(ts_1="20260301120000"),
    msh_9=MSG(msg_1="ACK"),
    msh_10="ACK000001",
    msh_11=PT(pt_1="P"),
    msh_12=VID(vid_1="2.5.1"),
)

ack_pos = ACK(
    MSH=msh_pos,
    MSA=MSA(msa_1="AA", msa_2=original_id),
)

# Convert the typed ACK model to ER7 text.
er7_pos = ack_pos.model_dump_er7()

print("Positive ACK:")
for segment in er7_pos.split("\r"):
    print(segment)


# Build a negative ACK with an ERR segment.
msh_neg = MSH(
    msh_3=HD(hd_1="HIS"),
    msh_4=HD(hd_1="YSBYTY CWMTAFF"),
    msh_5=HD(hd_1="LABORDAI"),
    msh_6=HD(hd_1="YSBYTY CWMTAFF"),
    msh_7=TS(ts_1="20260301120000"),
    msh_9=MSG(msg_1="ACK"),
    msh_10="ACK000002",
    msh_11=PT(pt_1="P"),
    msh_12=VID(vid_1="2.5.1"),
)

ack_neg = ACK(
    MSH=msh_neg,
    MSA=MSA(msa_1="AE", msa_2=original_id, msa_3="Nid yw'r claf i'w gael (Patient not found)"),
    ERR=[
        ERR(
            err_3=CWE(cwe_1="207", cwe_2="Application internal error", cwe_3="HL70357"),
            err_4="E",
        )
    ],
)

# Convert the typed negative ACK model to ER7 text.
er7_neg = ack_neg.model_dump_er7()

print("\nNegative ACK:")
for segment in er7_neg.split("\r"):
    print(segment)


print("\nRound-trip decode:")

# Decode the ER7 text back into a typed ACK model.
msg = decode_er7(er7_pos, msg_cls=ACK)

# Read values back from the typed model.
print("ACK code:", msg.MSA.msa_1)
print("Original control ID:", msg.MSA.msa_2)
print("Receiving application:", msg.MSH.msh_3.hd_1)
print("Sending application:", msg.MSH.msh_5.hd_1)
