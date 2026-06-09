"""Parse an inbound ADT^A01 patient admission message."""

from hl7types import decode_er7

# This is a small ADT^A01 admission message in ER7 format.
#
# ADT^A01 means "admit / visit notification". It is commonly used when a
# patient is admitted to hospital.
wire = (
    "MSH|^~\\&|HIS|YSBYTY CWMTAFF|ADT|YSBYTY CWMTAFF|20260301090000||ADT^A01^ADT_A01|MSG000001|P|2.5.1\r"
    "EVN||20260301090000\r"
    "PID|1||CYM12345^^^YSBYTY CWMTAFF^MR||PRICE^RHODRI^^^MR||19850315|M"
    "|||3 STRYD FAWR^^PONTYPRIDD^^CF37 1AB^GBR^H||07700 900123^PRN^PH\r"
    "PV1|1|I|UNED DRAIG^YSTAFELL 3^GWELY 2||||DR001^DRAGONHEART^GWENLLIAN^^^DR||||||||||||YMWELIAD001^^^YSBYTY CWMTAFF^VN\r"
)


# Decode the ER7 text into a typed HL7 model.
#
# The decoder uses MSH.9 and MSH.12 to work out the message type and version.
# Here, that means ADT_A01 for HL7 v2.5.1.
msg = decode_er7(wire)


# PID.3 contains patient identifiers.
#
# It is repeating, so hl7types represents it as a list.
# This example reads the first identifier as the medical record number.
patient_id = msg.PID.pid_3[0]
mrn = patient_id.cx_1
assigning_authority = patient_id.cx_4.hd_1 if patient_id.cx_4 else None


# PID.5 contains patient names.
#
# It is also repeating, so this example reads the first name.
patient_name = msg.PID.pid_5[0]
surname = patient_name.xpn_1.fn_1 if patient_name.xpn_1 else None
given_name = patient_name.xpn_2
title = patient_name.xpn_5


# PID.7 is date of birth and PID.8 is administrative sex.
date_of_birth = msg.PID.pid_7.ts_1 if msg.PID.pid_7 else None
sex = msg.PID.pid_8


# PV1 contains visit information.
#
# PV1.2 is patient class. In this example, "I" means inpatient.
patient_class = msg.PV1.pv1_2


# PV1.3 is assigned patient location.
#
# The PL datatype splits the location into ward, room and bed components.
location = msg.PV1.pv1_3
ward = location.pl_1 if location else None
room = location.pl_2 if location else None
bed = location.pl_3 if location else None


# PV1.7 is the attending doctor.
#
# It is repeating, so this example reads the first doctor.
attending_doctor = msg.PV1.pv1_7
attending_id = attending_doctor[0].xcn_1 if attending_doctor else None
attending_surname = attending_doctor[0].xcn_2.fn_1 if attending_doctor else None


# PV1.19 is the visit number.
visit_number = msg.PV1.pv1_19
visit_id = visit_number.cx_1 if visit_number else None


print("Patient:", title, given_name, surname)
print("MRN:", mrn)
print("Assigning authority:", assigning_authority)
print("Date of birth:", date_of_birth)
print("Sex:", sex)
print("Patient class:", patient_class)
print("Location:", ward, "/", room, "/", bed)
print("Attending doctor ID:", attending_id)
print("Attending doctor surname:", attending_surname)
print("Visit ID:", visit_id)
