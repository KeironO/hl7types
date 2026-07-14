v2.2 Messages
=============

.. _hl7-v2_2-ACK:

ACK General acknowledgment message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR

.. _hl7-v2_2-ADR_A19:

ADR_A19 HL7 v2 ADR_A19 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADR_A19.ADR_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QUERY_RESPONSE``
     - List[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_2-ADR_A19_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-ADT_A01:

ADT_A01 HL7 v2 ADT_A01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_2-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A02:

ADT_A02 HL7 v2 ADT_A02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A03:

ADT_A03 HL7 v2 ADT_A03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A04:

ADT_A04 HL7 v2 ADT_A04 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A04_INSURANCE <hl7-v2_2-ADT_A04_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A05:

ADT_A05 HL7 v2 ADT_A05 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_2-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A06:

ADT_A06 HL7 v2 ADT_A06 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_2-MRG>`]
     - optional
     - MERGE PATIENT INFORMATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_2-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A07:

ADT_A07 HL7 v2 ADT_A07 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_2-MRG>`]
     - optional
     - MERGE PATIENT INFORMATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A07_INSURANCE <hl7-v2_2-ADT_A07_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A08:

ADT_A08 HL7 v2 ADT_A08 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A08_INSURANCE <hl7-v2_2-ADT_A08_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A09:

ADT_A09 HL7 v2 ADT_A09 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS

.. _hl7-v2_2-ADT_A10:

ADT_A10 HL7 v2 ADT_A10 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS

.. _hl7-v2_2-ADT_A11:

ADT_A11 HL7 v2 ADT_A11 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS

.. _hl7-v2_2-ADT_A12:

ADT_A12 HL7 v2 ADT_A12 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS

.. _hl7-v2_2-ADT_A13:

ADT_A13 HL7 v2 ADT_A13 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A13_INSURANCE <hl7-v2_2-ADT_A13_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A14:

ADT_A14 HL7 v2 ADT_A14 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A14_INSURANCE <hl7-v2_2-ADT_A14_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A15:

ADT_A15 HL7 v2 ADT_A15 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS

.. _hl7-v2_2-ADT_A16:

ADT_A16 HL7 v2 ADT_A16 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS

.. _hl7-v2_2-ADT_A17:

ADT_A17 HL7 v2 ADT_A17 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A18:

ADT_A18 HL7 v2 ADT_A18 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A18.ADT_A18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_2-MRG>`]
     - optional
     - MERGE PATIENT INFORMATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT

.. _hl7-v2_2-ADT_A20:

ADT_A20 HL7 v2 ADT_A20 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``NPU``
     - :ref:`NPU <hl7-v2_2-NPU>`
     - required
     - BED STATUS UPDATE

.. _hl7-v2_2-ADT_A21:

ADT_A21 HL7 v2 ADT_A21 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A22:

ADT_A22 HL7 v2 ADT_A22 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A22.ADT_A22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A23:

ADT_A23 HL7 v2 ADT_A23 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A23.ADT_A23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A24:

ADT_A24 HL7 v2 ADT_A24 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_2-PV1>`]
     - optional
     - PATIENT VISIT

.. _hl7-v2_2-ADT_A25:

ADT_A25 HL7 v2 ADT_A25 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A25.ADT_A25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A26:

ADT_A26 HL7 v2 ADT_A26 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A26.ADT_A26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A27:

ADT_A27 HL7 v2 ADT_A27 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A27.ADT_A27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A28:

ADT_A28 HL7 v2 ADT_A28 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A28_INSURANCE <hl7-v2_2-ADT_A28_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A29:

ADT_A29 HL7 v2 ADT_A29 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A29.ADT_A29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A30:

ADT_A30 HL7 v2 ADT_A30 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A30.ADT_A30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     - MERGE PATIENT INFORMATION

.. _hl7-v2_2-ADT_A31:

ADT_A31 HL7 v2 ADT_A31 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     - NEXT OF KIN
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     - PATIENT ALLERGY INFORMATION
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     - DIAGNOSIS
   * - ``PR1``
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     - PROCEDURES
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     - GUARANTOR
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A31_INSURANCE <hl7-v2_2-ADT_A31_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     - ACCIDENT
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     - UB82 DATA
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     - UB92 DATA

.. _hl7-v2_2-ADT_A32:

ADT_A32 HL7 v2 ADT_A32 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A32.ADT_A32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A33:

ADT_A33 HL7 v2 ADT_A33 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A33.ADT_A33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT

.. _hl7-v2_2-ADT_A34:

ADT_A34 HL7 v2 ADT_A34 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A34.ADT_A34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     - MERGE PATIENT INFORMATION

.. _hl7-v2_2-ADT_A35:

ADT_A35 HL7 v2 ADT_A35 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A35.ADT_A35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     - MERGE PATIENT INFORMATION

.. _hl7-v2_2-ADT_A36:

ADT_A36 HL7 v2 ADT_A36 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A36.ADT_A36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     - MERGE PATIENT INFORMATION

.. _hl7-v2_2-ADT_A37:

ADT_A37 HL7 v2 ADT_A37 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_2-PV1>`]
     - optional
     - PATIENT VISIT

.. _hl7-v2_2-BAR_P01:

BAR_P01 HL7 v2 BAR_P01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``VISIT``
     - List[:ref:`BAR_P01_VISIT <hl7-v2_2-BAR_P01_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_2-BAR_P02:

BAR_P02 HL7 v2 BAR_P02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PATIENT``
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_2-BAR_P02_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_2-DFT_P03:

DFT_P03 HL7 v2 DFT_P03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     - EVENT TYPE
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     - PATIENT IDENTIFICATION
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_2-PV1>`]
     - optional
     - PATIENT VISIT
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     - PATIENT VISIT - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     - OBSERVATION RESULT
   * - ``FT1``
     - List[:ref:`FT1 <hl7-v2_2-FT1>`]
     - required
     - FINANCIAL TRANSACTION

.. _hl7-v2_2-DSR_P04:

DSR_P04 HL7 v2 DSR_P04 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_P04.DSR_P04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-DSR_Q01:

DSR_Q01 HL7 v2 DSR_Q01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_Q01.DSR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-DSR_Q03:

DSR_Q03 HL7 v2 DSR_Q03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_Q03.DSR_Q03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - Optional[:ref:`MSA <hl7-v2_2-MSA>`]
     - optional
     - MESSAGE ACKNOWLEDGMENT
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-DSR_R03:

DSR_R03 HL7 v2 DSR_R03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_R03.DSR_R03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - Optional[:ref:`MSA <hl7-v2_2-MSA>`]
     - optional
     - MESSAGE ACKNOWLEDGMENT
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-MFD_M01:

MFD_M01 HL7 v2 MFD_M01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M01.MFD_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     - MASTER FILE ACKNOWLEDGEMENT

.. _hl7-v2_2-MFD_M02:

MFD_M02 HL7 v2 MFD_M02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M02.MFD_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     - MASTER FILE ACKNOWLEDGEMENT

.. _hl7-v2_2-MFD_M03:

MFD_M03 HL7 v2 MFD_M03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M03.MFD_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     - MASTER FILE ACKNOWLEDGEMENT

.. _hl7-v2_2-MFK_M01:

MFK_M01 HL7 v2 MFK_M01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     - MASTER FILE ACKNOWLEDGEMENT

.. _hl7-v2_2-MFK_M02:

MFK_M02 HL7 v2 MFK_M02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M02.MFK_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     - MASTER FILE ACKNOWLEDGEMENT

.. _hl7-v2_2-MFK_M03:

MFK_M03 HL7 v2 MFK_M03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M03.MFK_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     - MASTER FILE ACKNOWLEDGEMENT

.. _hl7-v2_2-MFN_M01:

MFN_M01 HL7 v2 MFN_M01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M01.MFN_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MF``
     - List[:ref:`MFN_M01_MF <hl7-v2_2-MFN_M01_MF>`]
     - required
     - MF

.. _hl7-v2_2-MFN_M02:

MFN_M02 HL7 v2 MFN_M02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MF_STAFF``
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_2-MFN_M02_MF_STAFF>`]
     - required
     - MF_STAFF

.. _hl7-v2_2-MFN_M03:

MFN_M03 HL7 v2 MFN_M03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M03.MFN_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MF_TEST``
     - List[:ref:`MFN_M03_MF_TEST <hl7-v2_2-MFN_M03_MF_TEST>`]
     - required
     - MF_TEST

.. _hl7-v2_2-MFQ_M01:

MFQ_M01 HL7 v2 MFQ_M01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M01.MFQ_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-MFQ_M02:

MFQ_M02 HL7 v2 MFQ_M02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M02.MFQ_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-MFQ_M03:

MFQ_M03 HL7 v2 MFQ_M03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M03.MFQ_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-MFR_M01:

MFR_M01 HL7 v2 MFR_M01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M01.MFR_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MF``
     - List[:ref:`MFR_M01_MF <hl7-v2_2-MFR_M01_MF>`]
     - required
     - MF
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-MFR_M02:

MFR_M02 HL7 v2 MFR_M02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M02.MFR_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MF_STAFF``
     - List[:ref:`MFR_M02_MF_STAFF <hl7-v2_2-MFR_M02_MF_STAFF>`]
     - required
     - MF_STAFF
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-MFR_M03:

MFR_M03 HL7 v2 MFR_M03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M03.MFR_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     - MASTER FILE IDENTIFICATION
   * - ``MF_TEST``
     - List[:ref:`MFR_M03_MF_TEST <hl7-v2_2-MFR_M03_MF_TEST>`]
     - required
     - MF_TEST
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-NMD_N01:

NMD_N01 HL7 v2 NMD_N01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.NMD_N01.NMD_N01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     - List[:ref:`NMD_N01_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_2-NMD_N01_CLOCK_AND_STATS_WITH_NOTES>`]
     - required
     - CLOCK_AND_STATS_WITH_NOTES

.. _hl7-v2_2-NMQ_N02:

NMQ_N02 HL7 v2 NMQ_N02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.NMQ_N02.NMQ_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRY_WITH_DETAIL``
     - Optional[:ref:`NMQ_N02_QRY_WITH_DETAIL <hl7-v2_2-NMQ_N02_QRY_WITH_DETAIL>`]
     - optional
     - QRY_WITH_DETAIL
   * - ``CLOCK_AND_STATISTICS``
     - List[:ref:`NMQ_N02_CLOCK_AND_STATISTICS <hl7-v2_2-NMQ_N02_CLOCK_AND_STATISTICS>`]
     - required
     - CLOCK_AND_STATISTICS

.. _hl7-v2_2-NMR_N02:

NMR_N02 HL7 v2 NMR_N02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.NMR_N02.NMR_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     - ERROR
   * - ``QRD``
     - Optional[:ref:`QRD <hl7-v2_2-QRD>`]
     - optional
     - QUERY DEFINITION
   * - ``CLOCK_AND_STATS_WITH_NOTES_ALT``
     - List[:ref:`NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT <hl7-v2_2-NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT>`]
     - required
     - CLOCK_AND_STATS_WITH_NOTES_ALT

.. _hl7-v2_2-ORF_R04:

ORF_R04 HL7 v2 ORF_R04 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORF_R04.ORF_R04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``QUERY_RESPONSE``
     - List[:ref:`ORF_R04_QUERY_RESPONSE <hl7-v2_2-ORF_R04_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``ORDER``
     - List[:ref:`ORF_R04_ORDER <hl7-v2_2-ORF_R04_ORDER>`]
     - required
     - ORDER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-ORM_O01:

ORM_O01 HL7 v2 ORM_O01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORM_O01.ORM_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_2-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``PATIENT``
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_2-ORM_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORM_O01_ORDER <hl7-v2_2-ORM_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_2-ORR_O02:

ORR_O02 HL7 v2 ORR_O02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORR_O02.ORR_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     - MESSAGE ACKNOWLEDGMENT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_2-NTE>`]]
     - optional
     - NOTES AND COMMENTS
   * - ``PATIENT``
     - Optional[:ref:`ORR_O02_PATIENT <hl7-v2_2-ORR_O02_PATIENT>`]
     - optional
     - PATIENT

.. _hl7-v2_2-ORU_R01:

ORU_R01 HL7 v2 ORU_R01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``PATIENT_RESULT``
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_2-ORU_R01_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-QRY_A19:

QRY_A19 HL7 v2 QRY_A19 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_A19.QRY_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER

.. _hl7-v2_2-QRY_P04:

QRY_P04 HL7 v2 QRY_P04 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_P04.QRY_P04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-QRY_Q01:

QRY_Q01 HL7 v2 QRY_Q01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_Q01.QRY_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-QRY_Q02:

QRY_Q02 HL7 v2 QRY_Q02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_Q02.QRY_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     - QUERY FILTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-QRY_R02:

QRY_R02 HL7 v2 QRY_R02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_R02.QRY_R02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     - QUERY DEFINITION
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - required
     - QUERY FILTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     - CONTINUATION POINTER

.. _hl7-v2_2-UDM_Q05:

UDM_Q05 HL7 v2 UDM_Q05 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     - MESSAGE HEADER
   * - ``URD``
     - :ref:`URD <hl7-v2_2-URD>`
     - required
     - RESULTS/UPDATE DEFINITION
   * - ``URS``
     - Optional[:ref:`URS <hl7-v2_2-URS>`]
     - optional
     - UNSOLICITED SELECTION
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     - DISPLAY DATA
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - required
     - CONTINUATION POINTER
