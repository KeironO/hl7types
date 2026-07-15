v2.4 Messages
=============

.. _hl7-v2_4-ACK:

ACK: General acknowledgment message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR

.. _hl7-v2_4-ACK_N02:

ACK_N02: Application management data message (unsolicited)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ACK_N02.ACK_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA

.. _hl7-v2_4-ADR_A19:

ADR_A19:  Patient query
~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADR_A19.ADR_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``QUERY_RESPONSE``
     - list[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_4-ADR_A19_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-ADT_A01:

ADT_A01: Admit / visit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_4-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_4-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_4-PDA>`
     - O
     - PDA

.. _hl7-v2_4-ADT_A02:

ADT_A02:  Transfer a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``PDA``
     - :ref:`PDA <hl7-v2_4-PDA>`
     - O
     - PDA

.. _hl7-v2_4-ADT_A03:

ADT_A03:  Discharge/end visit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A03_PROCEDURE <hl7-v2_4-ADT_A03_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``PDA``
     - :ref:`PDA <hl7-v2_4-PDA>`
     - O
     - PDA

.. _hl7-v2_4-ADT_A04:

ADT_A04:  Register a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.4

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_4-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_4-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_4-PDA>`
     - O
     - PDA

.. _hl7-v2_4-ADT_A05:

ADT_A05:  Pre-admit a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_4-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_4-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2

.. _hl7-v2_4-ADT_A06:

ADT_A06:  Change an outpatient to an inpatient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A06_PROCEDURE <hl7-v2_4-ADT_A06_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A06_INSURANCE <hl7-v2_4-ADT_A06_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2

.. _hl7-v2_4-ADT_A07:

ADT_A07:  Change an inpatient to an outpatient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.7

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A06_PROCEDURE <hl7-v2_4-ADT_A06_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A06_INSURANCE <hl7-v2_4-ADT_A06_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2

.. _hl7-v2_4-ADT_A08:

ADT_A08:  Update patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.8

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_4-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_4-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_4-PDA>`
     - O
     - PDA

.. _hl7-v2_4-ADT_A09:

ADT_A09:  Patient departing - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1

.. _hl7-v2_4-ADT_A10:

ADT_A10:  Patient arriving - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.10

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1

.. _hl7-v2_4-ADT_A11:

ADT_A11:  Cancel admit/visit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.11

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1

.. _hl7-v2_4-ADT_A12:

ADT_A12:  Cancel transfer
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.12

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1

.. _hl7-v2_4-ADT_A13:

ADT_A13:  Cancel discharge/end visit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.13

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_4-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_4-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_4-PDA>`
     - O
     - PDA

.. _hl7-v2_4-ADT_A14:

ADT_A14:  Pending admit
~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.14

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_4-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_4-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2

.. _hl7-v2_4-ADT_A15:

ADT_A15:  Pending transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1

.. _hl7-v2_4-ADT_A16:

ADT_A16:  Pending discharge
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG

.. _hl7-v2_4-ADT_A17:

ADT_A17:  Swap patients
~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A18:

ADT_A18:  Merge patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A18.ADT_A18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1

.. _hl7-v2_4-ADT_A20:

ADT_A20:  Bed status update
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``NPU``
     - :ref:`NPU <hl7-v2_4-NPU>`
     - R
     - NPU

.. _hl7-v2_4-ADT_A21:

ADT_A21:  Patient goes on a "leave of absence"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A22:

ADT_A22:  Patient returns from a "leave of absence"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.22

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A22.ADT_A22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A23:

ADT_A23:  Delete a patient record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.23

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A23.ADT_A23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A24:

ADT_A24:  Link patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - O
     - PV1
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1

.. _hl7-v2_4-ADT_A25:

ADT_A25:  Cancel pending discharge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.25

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A25.ADT_A25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A26:

ADT_A26:  Cancel pending transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.26

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A26.ADT_A26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A27:

ADT_A27:  Cancel pending admit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.27

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A27.ADT_A27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A28:

ADT_A28:  Add person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.28

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_4-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_4-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2

.. _hl7-v2_4-ADT_A29:

ADT_A29:  Delete person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.29

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A29.ADT_A29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A30:

ADT_A30:  Merge person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A30.ADT_A30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A31:

ADT_A31:  Update person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.31

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_4-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_4-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_4-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_4-UB2>`
     - O
     - UB2

.. _hl7-v2_4-ADT_A32:

ADT_A32:  Cancel patient arriving - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.32

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A32.ADT_A32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A33:

ADT_A33:  Cancel patient departing - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.33

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A33.ADT_A33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX

.. _hl7-v2_4-ADT_A34:

ADT_A34:  Merge patient information - patient ID only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.34

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A34.ADT_A34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A35:

ADT_A35:  Merge patient information - account number only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.35

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A35.ADT_A35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A36:

ADT_A36:  Merge patient information - patient ID and account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.36

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A36.ADT_A36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A37:

ADT_A37:  Unlink patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - O
     - PV1
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1

.. _hl7-v2_4-ADT_A38:

ADT_A38: Cancel pre-admit
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A38.ADT_A38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG

.. _hl7-v2_4-ADT_A39:

ADT_A39: Merge person - patient ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A39.ADT_A39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_4-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-ADT_A40:

ADT_A40: Merge patient - patient identifier list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.40

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A40.ADT_A40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_4-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-ADT_A41:

ADT_A41: Merge account - patient account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.41

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A41.ADT_A41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_4-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-ADT_A42:

ADT_A42: Merge visit - visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.42

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A42.ADT_A42
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_4-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-ADT_A43:

ADT_A43: Move patient information - patient identifier list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A43.ADT_A43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A43_PATIENT <hl7-v2_4-ADT_A43_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-ADT_A44:

ADT_A44: Move account information - patient account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.44

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A44.ADT_A44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A43_PATIENT <hl7-v2_4-ADT_A43_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-ADT_A45:

ADT_A45: Move visit information - visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A45.ADT_A45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MERGE_INFO``
     - list[:ref:`ADT_A45_MERGE_INFO <hl7-v2_4-ADT_A45_MERGE_INFO>`]
     - R
     - MERGE_INFO

.. _hl7-v2_4-ADT_A46:

ADT_A46: Change Patient ID
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.46

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A46.ADT_A46
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A47:

ADT_A47: Change patient identifier list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.47

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A47.ADT_A47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A48:

ADT_A48: Change alternate patient ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.48

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A48.ADT_A48
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A49:

ADT_A49: Change patient account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.49

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A49.ADT_A49
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG

.. _hl7-v2_4-ADT_A50:

ADT_A50: Change visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A50.ADT_A50
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1

.. _hl7-v2_4-ADT_A51:

ADT_A51: Change alternate visit ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.51

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A51.ADT_A51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - R
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1

.. _hl7-v2_4-ADT_A52:

ADT_A52: Cancel leave of absence for a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A52.ADT_A52
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2

.. _hl7-v2_4-ADT_A53:

ADT_A53: Cancel patient returns from a leave of absence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.53

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A53.ADT_A53
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2

.. _hl7-v2_4-ADT_A54:

ADT_A54: Change attending doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A54.ADT_A54
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2

.. _hl7-v2_4-ADT_A55:

ADT_A55: Cancel change attending doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.55

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A55.ADT_A55
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2

.. _hl7-v2_4-ADT_A60:

ADT_A60:  Update allergy information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A60.ADT_A60
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - O
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``IAM``
     - list[:ref:`IAM <hl7-v2_4-IAM>`]
     - O
     - IAM

.. _hl7-v2_4-ADT_A61:

ADT_A61: Change consulting doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A61.ADT_A61
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2

.. _hl7-v2_4-ADT_A62:

ADT_A62: Cancel change consulting doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.62

.. py:class:: hl7types.hl7.v2_4.messages.ADT_A62.ADT_A62
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2

.. _hl7-v2_4-BAR_P01:

BAR_P01: Add patient accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``VISIT``
     - list[:ref:`BAR_P01_VISIT <hl7-v2_4-BAR_P01_VISIT>`]
     - R
     - VISIT

.. _hl7-v2_4-BAR_P02:

BAR_P02: Purge patient accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`BAR_P02_PATIENT <hl7-v2_4-BAR_P02_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-BAR_P05:

BAR_P05: Update account
~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.BAR_P05.BAR_P05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``VISIT``
     - list[:ref:`BAR_P05_VISIT <hl7-v2_4-BAR_P05_VISIT>`]
     - R
     - VISIT

.. _hl7-v2_4-BAR_P06:

BAR_P06: End account
~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.BAR_P06.BAR_P06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`BAR_P06_PATIENT <hl7-v2_4-BAR_P06_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-BAR_P10:

BAR_P10: BAR/ACK -Transmit  Ambulatory Payment  Classification(APC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.BAR_P10.BAR_P10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``GP1``
     - :ref:`GP1 <hl7-v2_4-GP1>`
     - R
     - GP1
   * - ``PROCEDURE``
     - list[:ref:`BAR_P10_PROCEDURE <hl7-v2_4-BAR_P10_PROCEDURE>`]
     - O
     - PROCEDURE

.. _hl7-v2_4-CRM_C01:

CRM_C01: CRM - Register a patient on a clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C01.CRM_C01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CRM_C02:

CRM_C02: CRM - Cancel a patient registration on clinical trial (for clerical mistakes onl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C02.CRM_C02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CRM_C03:

CRM_C03: CRM - Correct/update registration information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C03.CRM_C03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CRM_C04:

CRM_C04: CRM - Patient has gone off a clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C04.CRM_C04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CRM_C05:

CRM_C05: CRM - Patient enters phase of clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C05.CRM_C05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CRM_C06:

CRM_C06: CRM - Cancel patient entering a phase (clerical mistake)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C06.CRM_C06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CRM_C07:

CRM_C07: CRM - Correct/update phase information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C07.CRM_C07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CRM_C08:

CRM_C08: CRM - Patient has gone off phase of clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_4.messages.CRM_C08.CRM_C08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_4-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CSU_C09:

CSU_C09: CSU - Automated time intervals for reporting, like monthly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7

.. py:class:: hl7types.hl7.v2_4.messages.CSU_C09.CSU_C09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_4-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CSU_C10:

CSU_C10: CSU - Patient completes the clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_4.messages.CSU_C10.CSU_C10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_4-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CSU_C11:

CSU_C11: CSU - Patient completes a phase of the clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_4.messages.CSU_C11.CSU_C11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_4-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-CSU_C12:

CSU_C12: CSU - Update/correction of patient order/result information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_4.messages.CSU_C12.CSU_C12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_4-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-DFT_P03:

DFT_P03: Post detail financial transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - O
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``COMMON_ORDER``
     - list[:ref:`DFT_P03_COMMON_ORDER <hl7-v2_4-DFT_P03_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``FINANCIAL``
     - list[:ref:`DFT_P03_FINANCIAL <hl7-v2_4-DFT_P03_FINANCIAL>`]
     - R
     - FINANCIAL
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`DFT_P03_INSURANCE <hl7-v2_4-DFT_P03_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC

.. _hl7-v2_4-DFT_P11:

DFT_P11: Post detail financial transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.DFT_P11.DFT_P11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_4-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - O
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_4-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_4-DB1>`]
     - O
     - DB1
   * - ``COMMON_ORDER``
     - list[:ref:`DFT_P11_COMMON_ORDER <hl7-v2_4-DFT_P11_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_4-DRG>`
     - O
     - DRG
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`DFT_P11_INSURANCE <hl7-v2_4-DFT_P11_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``FINANCIAL``
     - list[:ref:`DFT_P11_FINANCIAL <hl7-v2_4-DFT_P11_FINANCIAL>`]
     - R
     - FINANCIAL

.. _hl7-v2_4-DOC_T12:

DOC_T12: Document query
~~~~~~~~~~~~~~~~~~~~~~~

Section 9

.. py:class:: hl7types.hl7.v2_4.messages.DOC_T12.DOC_T12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``RESULT``
     - list[:ref:`DOC_T12_RESULT <hl7-v2_4-DOC_T12_RESULT>`]
     - R
     - RESULT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-DSR_Q01:

DSR_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.DSR_Q01.DSR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-DSR_Q03:

DSR_Q03: Deferred response to a query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6

.. py:class:: hl7types.hl7.v2_4.messages.DSR_Q03.DSR_Q03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - O
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-EAC_U07:

EAC_U07: Automated equipment command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.EAC_U07.EAC_U07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``ECD``
     - list[:ref:`ECD <hl7-v2_4-ECD>`]
     - R
     - ECD
   * - ``SAC``
     - :ref:`SAC <hl7-v2_4-SAC>`
     - O
     - SAC
   * - ``CNS``
     - :ref:`CNS <hl7-v2_4-CNS>`
     - O
     - CNS
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-EAN_U09:

EAN_U09: Automated equipment notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.EAN_U09.EAN_U09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``NOTIFICATION``
     - list[:ref:`EAN_U09_NOTIFICATION <hl7-v2_4-EAN_U09_NOTIFICATION>`]
     - R
     - NOTIFICATION
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-EAR_U08:

EAR_U08: Automated equipment response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.EAR_U08.EAR_U08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``COMMAND_RESPONSE``
     - list[:ref:`EAR_U08_COMMAND_RESPONSE <hl7-v2_4-EAR_U08_COMMAND_RESPONSE>`]
     - R
     - COMMAND_RESPONSE
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-EDR_R07:

EDR_R07: Enhanced Display Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.EDR_R07.EDR_R07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-EQQ_Q04:

EQQ_Q04: EQQ - Embedded query language query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.EQQ_Q04.EQQ_Q04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQL``
     - :ref:`EQL <hl7-v2_4-EQL>`
     - R
     - EQL
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-ERP_R09:

ERP_R09: Event Replay Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.ERP_R09.ERP_R09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_4-ERQ>`
     - R
     - ERQ
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-ESR_U02:

ESR_U02: Automated equipment status request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.ESR_U02.ESR_U02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-ESU_U01:

ESU_U01: Automated equipment status update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.ESU_U01.ESU_U01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``ISD``
     - list[:ref:`ISD <hl7-v2_4-ISD>`]
     - O
     - ISD
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-INR_U06:

INR_U06: Automated equipment inventory request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.INR_U06.INR_U06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``INV``
     - list[:ref:`INV <hl7-v2_4-INV>`]
     - R
     - INV
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-INU_U05:

INU_U05: INU/ACK  - Automated equipment inventory update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.INU_U05.INU_U05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``INV``
     - list[:ref:`INV <hl7-v2_4-INV>`]
     - R
     - INV
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-LSU_U12:

LSU_U12: Automated equipment log/service update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.LSU_U12.LSU_U12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``EQP``
     - list[:ref:`EQP <hl7-v2_4-EQP>`]
     - R
     - EQP
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-LSU_U13:

LSU_U13: Automated equipment log/service request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.13

.. py:class:: hl7types.hl7.v2_4.messages.LSU_U13.LSU_U13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``EQP``
     - list[:ref:`EQP <hl7-v2_4-EQP>`]
     - R
     - EQP
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-MDM_T01:

MDM_T01: Original document notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T01.MDM_T01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA

.. _hl7-v2_4-MDM_T02:

MDM_T02: Original document notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T02.MDM_T02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - R
     - OBX

.. _hl7-v2_4-MDM_T03:

MDM_T03: Document status change notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.3

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T03.MDM_T03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA

.. _hl7-v2_4-MDM_T04:

MDM_T04: Document status change notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.4

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T04.MDM_T04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - R
     - OBX

.. _hl7-v2_4-MDM_T05:

MDM_T05: Document addendum notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.5

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T05.MDM_T05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA

.. _hl7-v2_4-MDM_T06:

MDM_T06: Document addendum notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.6

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T06.MDM_T06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - R
     - OBX

.. _hl7-v2_4-MDM_T07:

MDM_T07: Document edit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.7

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T07.MDM_T07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA

.. _hl7-v2_4-MDM_T08:

MDM_T08: Document edit notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.8

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T08.MDM_T08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - R
     - OBX

.. _hl7-v2_4-MDM_T09:

MDM_T09: Document replacement notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.9

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T09.MDM_T09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA

.. _hl7-v2_4-MDM_T10:

MDM_T10: Document replacement notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.10

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T10.MDM_T10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_4-OBX>`]
     - R
     - OBX

.. _hl7-v2_4-MDM_T11:

MDM_T11: Document cancel notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.5.11

.. py:class:: hl7types.hl7.v2_4.messages.MDM_T11.MDM_T11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - R
     - TXA

.. _hl7-v2_4-MFK_M01:

MFK_M01: Master file not otherwise specified (for backward compatibility only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_4-MFA>`]
     - O
     - MFA

.. _hl7-v2_4-MFN_M01:

MFN_M01: Master file not otherwise specified (for backward compatibility only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M01.MFN_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF``
     - list[:ref:`MFN_M01_MF <hl7-v2_4-MFN_M01_MF>`]
     - R
     - MF

.. _hl7-v2_4-MFN_M02:

MFN_M02: Master file - Staff Practitioner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_STAFF``
     - list[:ref:`MFN_M02_MF_STAFF <hl7-v2_4-MFN_M02_MF_STAFF>`]
     - R
     - MF_STAFF

.. _hl7-v2_4-MFN_M03:

MFN_M03: Master file - Test/Observation (for backward compatibility only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M03.MFN_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_TEST``
     - list[:ref:`MFN_M03_MF_TEST <hl7-v2_4-MFN_M03_MF_TEST>`]
     - R
     - MF_TEST

.. _hl7-v2_4-MFN_M04:

MFN_M04: Master files charge description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M04.MFN_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_CDM``
     - list[:ref:`MFN_M04_MF_CDM <hl7-v2_4-MFN_M04_MF_CDM>`]
     - R
     - MF_CDM

.. _hl7-v2_4-MFN_M05:

MFN_M05: Patient location master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M05.MFN_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_LOCATION``
     - list[:ref:`MFN_M05_MF_LOCATION <hl7-v2_4-MFN_M05_MF_LOCATION>`]
     - R
     - MF_LOCATION

.. _hl7-v2_4-MFN_M06:

MFN_M06: Clinical study with phases and schedules master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M06.MFN_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_CLIN_STUDY``
     - list[:ref:`MFN_M06_MF_CLIN_STUDY <hl7-v2_4-MFN_M06_MF_CLIN_STUDY>`]
     - R
     - MF_CLIN_STUDY

.. _hl7-v2_4-MFN_M07:

MFN_M07: Clinical study without phases but with schedules master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M07.MFN_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_CLIN_STUDY_SCHED``
     - list[:ref:`MFN_M07_MF_CLIN_STUDY_SCHED <hl7-v2_4-MFN_M07_MF_CLIN_STUDY_SCHED>`]
     - R
     - MF_CLIN_STUDY_SCHED

.. _hl7-v2_4-MFN_M08:

MFN_M08: Test/observation (Numeric) master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M08.MFN_M08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_TEST_NUMERIC``
     - list[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_4-MFN_M08_MF_TEST_NUMERIC>`]
     - R
     - MF_TEST_NUMERIC

.. _hl7-v2_4-MFN_M09:

MFN_M09: Test/Observation (Categorical) master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M09.MFN_M09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_TEST_CATEGORICAL``
     - list[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_4-MFN_M09_MF_TEST_CATEGORICAL>`]
     - R
     - MF_TEST_CATEGORICAL

.. _hl7-v2_4-MFN_M10:

MFN_M10: Test /observation batteries master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M10.MFN_M10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_TEST_BATTERIES``
     - list[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_4-MFN_M10_MF_TEST_BATTERIES>`]
     - R
     - MF_TEST_BATTERIES

.. _hl7-v2_4-MFN_M11:

MFN_M11: Test/calculated observations master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M11.MFN_M11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_TEST_CALCULATED``
     - list[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_4-MFN_M11_MF_TEST_CALCULATED>`]
     - R
     - MF_TEST_CALCULATED

.. _hl7-v2_4-MFN_M12:

MFN_M12: Master file notification message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFN_M12.MFN_M12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_OBS_ATTRIBUTES``
     - list[:ref:`MFN_M12_MF_OBS_ATTRIBUTES <hl7-v2_4-MFN_M12_MF_OBS_ATTRIBUTES>`]
     - R
     - MF_OBS_ATTRIBUTES

.. _hl7-v2_4-MFQ_M01:

MFQ_M01: Master file not otherwise specified (for backward compatibility only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFQ_M01.MFQ_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-MFQ_M02:

MFQ_M02: Master file - Staff Practitioner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.1

.. py:class:: hl7types.hl7.v2_4.messages.MFQ_M02.MFQ_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-MFQ_M03:

MFQ_M03: Master file - Test/Observation (for backward compatibility only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.8.2

.. py:class:: hl7types.hl7.v2_4.messages.MFQ_M03.MFQ_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-MFQ_M04:

MFQ_M04: Master files charge description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_4.messages.MFQ_M04.MFQ_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-MFQ_M05:

MFQ_M05: Patient location master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.1

.. py:class:: hl7types.hl7.v2_4.messages.MFQ_M05.MFQ_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-MFQ_M06:

MFQ_M06: Clinical study with phases and schedules master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.11.1

.. py:class:: hl7types.hl7.v2_4.messages.MFQ_M06.MFQ_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-MFR_M01:

MFR_M01: Master file not otherwise specified (for backward compatibility only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8

.. py:class:: hl7types.hl7.v2_4.messages.MFR_M01.MFR_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``MFI``
     - :ref:`MFI <hl7-v2_4-MFI>`
     - R
     - MFI
   * - ``MF_QUERY``
     - list[:ref:`MFR_M01_MF_QUERY <hl7-v2_4-MFR_M01_MF_QUERY>`]
     - R
     - MF_QUERY
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-NMD_N02:

NMD_N02: Application management data message (unsolicited)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14

.. py:class:: hl7types.hl7.v2_4.messages.NMD_N02.NMD_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     - list[:ref:`NMD_N02_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_4-NMD_N02_CLOCK_AND_STATS_WITH_NOTES>`]
     - R
     - CLOCK_AND_STATS_WITH_NOTES

.. _hl7-v2_4-NMQ_N01:

NMQ_N01: Application management query message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14

.. py:class:: hl7types.hl7.v2_4.messages.NMQ_N01.NMQ_N01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRY_WITH_DETAIL``
     - :ref:`NMQ_N01_QRY_WITH_DETAIL <hl7-v2_4-NMQ_N01_QRY_WITH_DETAIL>`
     - O
     - QRY_WITH_DETAIL
   * - ``CLOCK_AND_STATISTICS``
     - list[:ref:`NMQ_N01_CLOCK_AND_STATISTICS <hl7-v2_4-NMQ_N01_CLOCK_AND_STATISTICS>`]
     - R
     - CLOCK_AND_STATISTICS

.. _hl7-v2_4-NMR_N01:

NMR_N01: Application management query message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14

.. py:class:: hl7types.hl7.v2_4.messages.NMR_N01.NMR_N01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - O
     - QRD
   * - ``CLOCK_AND_STATS_WITH_NOTES_ALT``
     - list[:ref:`NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT <hl7-v2_4-NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT>`]
     - R
     - CLOCK_AND_STATS_WITH_NOTES_ALT

.. _hl7-v2_4-OMD_O03:

OMD_O03: OMD - Diet order
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OMD_O03.OMD_O03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMD_O03_PATIENT <hl7-v2_4-OMD_O03_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER_DIET``
     - list[:ref:`OMD_O03_ORDER_DIET <hl7-v2_4-OMD_O03_ORDER_DIET>`]
     - R
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - list[:ref:`OMD_O03_ORDER_TRAY <hl7-v2_4-OMD_O03_ORDER_TRAY>`]
     - O
     - ORDER_TRAY

.. _hl7-v2_4-OMG_O19:

OMG_O19: OMG - General clinical order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OMG_O19.OMG_O19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMG_O19_PATIENT <hl7-v2_4-OMG_O19_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMG_O19_ORDER <hl7-v2_4-OMG_O19_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-OML_O21:

OML_O21: OML - Laboratory order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OML_O21.OML_O21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OML_O21_PATIENT <hl7-v2_4-OML_O21_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER_GENERAL``
     - list[:ref:`OML_O21_ORDER_GENERAL <hl7-v2_4-OML_O21_ORDER_GENERAL>`]
     - R
     - ORDER_GENERAL

.. _hl7-v2_4-OMN_O07:

OMN_O07: OMN - Non-stock requisition order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OMN_O07.OMN_O07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMN_O07_PATIENT <hl7-v2_4-OMN_O07_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMN_O07_ORDER <hl7-v2_4-OMN_O07_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-OMP_O09:

OMP_O09: OMP - Pharmacy/treatment order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OMP_O09.OMP_O09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMP_O09_PATIENT <hl7-v2_4-OMP_O09_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMP_O09_ORDER <hl7-v2_4-OMP_O09_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-OMS_O05:

OMS_O05: OMS - Stock requisition order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OMS_O05.OMS_O05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMS_O05_PATIENT <hl7-v2_4-OMS_O05_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMS_O05_ORDER <hl7-v2_4-OMS_O05_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-ORD_O04:

ORD_O04: ORD - Diet order acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORD_O04.ORD_O04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORD_O04_RESPONSE <hl7-v2_4-ORD_O04_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-ORF_R04:

ORF_R04: ORF - Response to query; transmission of requested observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7

.. py:class:: hl7types.hl7.v2_4.messages.ORF_R04.ORF_R04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``RESPONSE``
     - list[:ref:`ORF_R04_RESPONSE <hl7-v2_4-ORF_R04_RESPONSE>`]
     - R
     - RESPONSE
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-ORG_O20:

ORG_O20: General clinical order response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORG_O20.ORG_O20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORG_O20_RESPONSE <hl7-v2_4-ORG_O20_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-ORL_O22:

ORL_O22: ORL - General Laboratory Order Acknowledgment Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORL_O22.ORL_O22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORL_O22_RESPONSE <hl7-v2_4-ORL_O22_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-ORM_O01:

ORM_O01: ORM - Order message (also RDE, RDS, RGV, RAS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORM_O01.ORM_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`ORM_O01_PATIENT <hl7-v2_4-ORM_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`ORM_O01_ORDER <hl7-v2_4-ORM_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-ORN_O08:

ORN_O08: ORN - Non-stock requisition acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORN_O08.ORN_O08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORN_O08_RESPONSE <hl7-v2_4-ORN_O08_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-ORP_O10:

ORP_O10: ORP - Pharmacy/treatment order acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORP_O10.ORP_O10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORP_O10_RESPONSE <hl7-v2_4-ORP_O10_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-ORR_O02:

ORR_O02: ORR - Order response (also RRE, RRD, RRG, RRA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORR_O02.ORR_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORR_O02_RESPONSE <hl7-v2_4-ORR_O02_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-ORS_O06:

ORS_O06: ORS - Stock requisition acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ORS_O06.ORS_O06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RSPONSE``
     - :ref:`ORS_O06_RSPONSE <hl7-v2_4-ORS_O06_RSPONSE>`
     - O
     - RSPONSE

.. _hl7-v2_4-ORU_R01:

ORU_R01: Unsolicited transmission of an observation message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7

.. py:class:: hl7types.hl7.v2_4.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PATIENT_RESULT``
     - list[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_4-ORU_R01_PATIENT_RESULT>`]
     - R
     - PATIENT_RESULT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-OSQ_Q06:

OSQ_Q06: Query for order status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OSQ_Q06.OSQ_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-OSR_Q06:

OSR_Q06: Query for order status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.OSR_Q06.OSR_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``RESPONSE``
     - :ref:`OSR_Q06_RESPONSE <hl7-v2_4-OSR_Q06_RESPONSE>`
     - O
     - RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-OUL_R21:

OUL_R21: OUL - Unsolicited laboratory observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7

.. py:class:: hl7types.hl7.v2_4.messages.OUL_R21.OUL_R21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - :ref:`NTE <hl7-v2_4-NTE>`
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OUL_R21_PATIENT <hl7-v2_4-OUL_R21_PATIENT>`
     - O
     - PATIENT
   * - ``VISIT``
     - :ref:`OUL_R21_VISIT <hl7-v2_4-OUL_R21_VISIT>`
     - O
     - VISIT
   * - ``ORDER_OBSERVATION``
     - list[:ref:`OUL_R21_ORDER_OBSERVATION <hl7-v2_4-OUL_R21_ORDER_OBSERVATION>`]
     - R
     - ORDER_OBSERVATION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-PEX_P07:

PEX_P07: PEX - Unsolicited initial individual product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7

.. py:class:: hl7types.hl7.v2_4.messages.PEX_P07.PEX_P07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``VISIT``
     - :ref:`PEX_P07_VISIT <hl7-v2_4-PEX_P07_VISIT>`
     - O
     - VISIT
   * - ``EXPERIENCE``
     - list[:ref:`PEX_P07_EXPERIENCE <hl7-v2_4-PEX_P07_EXPERIENCE>`]
     - R
     - EXPERIENCE

.. _hl7-v2_4-PEX_P08:

PEX_P08: PEX - Unsolicited update individual product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.1

.. py:class:: hl7types.hl7.v2_4.messages.PEX_P08.PEX_P08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``VISIT``
     - :ref:`PEX_P07_VISIT <hl7-v2_4-PEX_P07_VISIT>`
     - O
     - VISIT
   * - ``EXPERIENCE``
     - list[:ref:`PEX_P07_EXPERIENCE <hl7-v2_4-PEX_P07_EXPERIENCE>`]
     - R
     - EXPERIENCE

.. _hl7-v2_4-PGL_PC6:

PGL_PC6: PGL - PC/ Goal Add
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PGL_PC6.PGL_PC6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_4-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_4-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_4-PGL_PC7:

PGL_PC7: PGL - PC/ Goal Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.1

.. py:class:: hl7types.hl7.v2_4.messages.PGL_PC7.PGL_PC7
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_4-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_4-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_4-PGL_PC8:

PGL_PC8: PGL - PC/ Goal Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.1

.. py:class:: hl7types.hl7.v2_4.messages.PGL_PC8.PGL_PC8
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_4-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_4-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_4-PMU_B01:

PMU_B01: Add personnel record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.PMU_B01.PMU_B01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_4-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - list[:ref:`ORG <hl7-v2_4-ORG>`]
     - O
     - ORG
   * - ``AFF``
     - list[:ref:`AFF <hl7-v2_4-AFF>`]
     - O
     - AFF
   * - ``LAN``
     - list[:ref:`LAN <hl7-v2_4-LAN>`]
     - O
     - LAN
   * - ``EDU``
     - list[:ref:`EDU <hl7-v2_4-EDU>`]
     - O
     - EDU

.. _hl7-v2_4-PMU_B02:

PMU_B02: Update personnel record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.2

.. py:class:: hl7types.hl7.v2_4.messages.PMU_B02.PMU_B02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_4-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - list[:ref:`ORG <hl7-v2_4-ORG>`]
     - O
     - ORG
   * - ``AFF``
     - list[:ref:`AFF <hl7-v2_4-AFF>`]
     - O
     - AFF
   * - ``LAN``
     - list[:ref:`LAN <hl7-v2_4-LAN>`]
     - O
     - LAN
   * - ``EDU``
     - list[:ref:`EDU <hl7-v2_4-EDU>`]
     - O
     - EDU

.. _hl7-v2_4-PMU_B03:

PMU_B03: Delete personnel re cord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.PMU_B03.PMU_B03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - R
     - STF

.. _hl7-v2_4-PMU_B04:

PMU_B04: Active practicing person
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.PMU_B04.PMU_B04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_4-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - :ref:`ORG <hl7-v2_4-ORG>`
     - O
     - ORG

.. _hl7-v2_4-PMU_B05:

PMU_B05: Deactivate practicing person
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.5

.. py:class:: hl7types.hl7.v2_4.messages.PMU_B05.PMU_B05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_4-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - :ref:`ORG <hl7-v2_4-ORG>`
     - O
     - ORG

.. _hl7-v2_4-PMU_B06:

PMU_B06: Terminate practicing person
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.6

.. py:class:: hl7types.hl7.v2_4.messages.PMU_B06.PMU_B06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_4-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_4-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - :ref:`ORG <hl7-v2_4-ORG>`
     - O
     - ORG

.. _hl7-v2_4-PPG_PCG:

PPG_PCG: PPG - PC/ Pathway (Goal-Oriented) Add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PPG_PCG.PPG_PCG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_4-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_4-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_4-PPG_PCH:

PPG_PCH: PPG - PC/ Pathway (Goal-Oriented) Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.4

.. py:class:: hl7types.hl7.v2_4.messages.PPG_PCH.PPG_PCH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_4-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_4-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_4-PPG_PCJ:

PPG_PCJ: PPG - PC/ Pathway (Goal-Oriented) Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.4

.. py:class:: hl7types.hl7.v2_4.messages.PPG_PCJ.PPG_PCJ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_4-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_4-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_4-PPP_PCB:

PPP_PCB: PPP - PC/ Pathway (Problem-Oriented) Add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PPP_PCB.PPP_PCB
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_4-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_4-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_4-PPP_PCC:

PPP_PCC: PPP - PC/ Pathway (Problem-Oriented) Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.3

.. py:class:: hl7types.hl7.v2_4.messages.PPP_PCC.PPP_PCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_4-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_4-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_4-PPP_PCD:

PPP_PCD: PPP - PC/ Pathway (Problem-Oriented) Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.3

.. py:class:: hl7types.hl7.v2_4.messages.PPP_PCD.PPP_PCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_4-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_4-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_4-PPR_PC1:

PPR_PC1: PPR - PC/ Problem Add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PPR_PC1.PPR_PC1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_4-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_4-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_4-PPR_PC2:

PPR_PC2: PPR - PC/ Problem Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.2

.. py:class:: hl7types.hl7.v2_4.messages.PPR_PC2.PPR_PC2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_4-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_4-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_4-PPR_PC3:

PPR_PC3: PPR - PC/ Problem Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.2

.. py:class:: hl7types.hl7.v2_4.messages.PPR_PC3.PPR_PC3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_4-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_4-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_4-PPT_PCL:

PPT_PCL: PTV - PC/ Pathway (Goal-Oriented) Query Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PPT_PCL.PPT_PCL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PPT_PCL_PATIENT <hl7-v2_4-PPT_PCL_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-PPV_PCA:

PPV_PCA: PGR - PC/ Goal Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PPV_PCA.PPV_PCA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PPV_PCA_PATIENT <hl7-v2_4-PPV_PCA_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-PRR_PC5:

PRR_PC5: PRR - PC/ Problem Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PRR_PC5.PRR_PC5
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PRR_PC5_PATIENT <hl7-v2_4-PRR_PC5_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-PTR_PCF:

PTR_PCF: PTR - PC/ Pathway (Problem-Oriented) Query Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.PTR_PCF.PTR_PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PTR_PCF_PATIENT <hl7-v2_4-PTR_PCF_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_4-QBP_K13:

QBP_K13: query by parameter/tabular response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.QBP_K13.QBP_K13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`QBP_K13_ROW_DEFINITION <hl7-v2_4-QBP_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q11:

QBP_Q11: query by parameter/segment pattern response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q11.QBP_Q11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q13:

QBP_Q13: quey by parameter/tabluar response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q13.QBP_Q13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q13_QBP <hl7-v2_4-QBP_Q13_QBP>`
     - O
     - QBP
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q15:

QBP_Q15: query by parameter/display response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q15.QBP_Q15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q21:

QBP_Q21: QBP - Get person demographics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q21.QBP_Q21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q22:

QBP_Q22: QBP - Find candidates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.57

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q22.QBP_Q22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q23:

QBP_Q23: QBP - Get corresponding identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.58

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q23.QBP_Q23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q24:

QBP_Q24: QBP - Allocate identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.59

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q24.QBP_Q24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Q25:

QBP_Q25: QBP - Personnel Information by Segment Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Q25.QBP_Q25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Qnn:

QBP_Qnn: HL7 v2 QBP_Qnn message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Qnn.QBP_Qnn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z73:

QBP_Z73: Information about Phone Calls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z73.QBP_Z73
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP

.. _hl7-v2_4-QBP_Z75:

QBP_Z75: Tabular Patient List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.7.2

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z75.QBP_Z75
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q13_QBP <hl7-v2_4-QBP_Q13_QBP>`
     - O
     - QBP
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z77:

QBP_Z77: Tabular Patient List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.7.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z77.QBP_Z77
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q13_QBP <hl7-v2_4-QBP_Q13_QBP>`
     - O
     - QBP
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z79:

QBP_Z79: Dispense Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.6.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z79.QBP_Z79
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z81:

QBP_Z81: Dispense History
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.1.1.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z81.QBP_Z81
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z85:

QBP_Z85: Pharmacy Information Comprehensive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.1.2.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z85.QBP_Z85
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z87:

QBP_Z87: Dispense Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.2.1.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z87.QBP_Z87
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z89:

QBP_Z89: Lab Results History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.2.3.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z89.QBP_Z89
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z91:

QBP_Z91: Who Am I
~~~~~~~~~~~~~~~~~

Section 5.9.3.1.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z91.QBP_Z91
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q13_QBP <hl7-v2_4-QBP_Q13_QBP>`
     - O
     - QBP
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z93:

QBP_Z93: Tabular Dispense History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.3.2.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z93.QBP_Z93
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q13_QBP <hl7-v2_4-QBP_Q13_QBP>`
     - O
     - QBP
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z95:

QBP_Z95: Tabular Dispense History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.4.1.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z95.QBP_Z95
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q13_QBP <hl7-v2_4-QBP_Q13_QBP>`
     - O
     - QBP
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z97:

QBP_Z97: Dispense History
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.5.1

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z97.QBP_Z97
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QBP_Z99:

QBP_Z99: Who Am I
~~~~~~~~~~~~~~~~~

Section 5.3.1.2

.. py:class:: hl7types.hl7.v2_4.messages.QBP_Z99.QBP_Z99
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q13_QBP <hl7-v2_4-QBP_Q13_QBP>`
     - O
     - QBP
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QCK_Q02:

QCK_Q02: Query sent for deferred response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.QCK_Q02.QCK_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - O
     - QAK

.. _hl7-v2_4-QCN_J01:

QCN_J01: Cancel query/acknowledge message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.QCN_J01.QCN_J01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QID``
     - :ref:`QID <hl7-v2_4-QID>`
     - R
     - QID

.. _hl7-v2_4-QCN_J02:

QCN_J02: Cancel subscription/acknowledge message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.4.7

.. py:class:: hl7types.hl7.v2_4.messages.QCN_J02.QCN_J02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QID``
     - :ref:`QID <hl7-v2_4-QID>`
     - R
     - QID

.. _hl7-v2_4-QRY_A19:

QRY_A19:  Patient query
~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.QRY_A19.QRY_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF

.. _hl7-v2_4-QRY_PC4:

QRY_PC4: PRQ - PC/ Problem Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.QRY_PC4.QRY_PC4
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF

.. _hl7-v2_4-QRY_PC9:

QRY_PC9: PGQ - PC/ Goal Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.7

.. py:class:: hl7types.hl7.v2_4.messages.QRY_PC9.QRY_PC9
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF

.. _hl7-v2_4-QRY_PCE:

QRY_PCE: PTQ - PC/ Pathway (Problem-Oriented) Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.9

.. py:class:: hl7types.hl7.v2_4.messages.QRY_PCE.QRY_PCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF

.. _hl7-v2_4-QRY_PCK:

QRY_PCK: PTU - PC/ Pathway (Goal-Oriented) Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.11

.. py:class:: hl7types.hl7.v2_4.messages.QRY_PCK.QRY_PCK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF

.. _hl7-v2_4-QRY_Q01:

QRY_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.QRY_Q01.QRY_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QRY_Q02:

QRY_Q02: Query sent for deferred response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.QRY_Q02.QRY_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QRY_Q26:

QRY_Q26: pharmacy/treatment order query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.13

.. py:class:: hl7types.hl7.v2_4.messages.QRY_Q26.QRY_Q26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QRY_Q27:

QRY_Q27: pharmacy/treatment administration information query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.14

.. py:class:: hl7types.hl7.v2_4.messages.QRY_Q27.QRY_Q27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QRY_Q28:

QRY_Q28: pharmacy/treatment dispense information query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.15

.. py:class:: hl7types.hl7.v2_4.messages.QRY_Q28.QRY_Q28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QRY_Q29:

QRY_Q29: pharmacy/treatment encoded order information query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.16

.. py:class:: hl7types.hl7.v2_4.messages.QRY_Q29.QRY_Q29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QRY_Q30:

QRY_Q30: pharmacy/treatment dose information query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.17

.. py:class:: hl7types.hl7.v2_4.messages.QRY_Q30.QRY_Q30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QRY_R02:

QRY_R02: QRY - Query for results of observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.QRY_R02.QRY_R02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - R
     - QRF

.. _hl7-v2_4-QRY_T12:

QRY_T12: Document query
~~~~~~~~~~~~~~~~~~~~~~~

Section 12

.. py:class:: hl7types.hl7.v2_4.messages.QRY_T12.QRY_T12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF

.. _hl7-v2_4-QSB_Q16:

QSB_Q16: QSB - Create subscription
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.QSB_Q16.QSB_Q16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QSB_Z83:

QSB_Z83: ORU Subscription
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.7.3.1

.. py:class:: hl7types.hl7.v2_4.messages.QSB_Z83.QSB_Z83
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-QVR_Q17:

QVR_Q17: QVR - Query for previous events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.QVR_Q17.QVR_Q17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RAR_RAR:

RAR_RAR: RAR - Pharmacy administration information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RAR_RAR.RAR_RAR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`RAR_RAR_DEFINITION <hl7-v2_4-RAR_RAR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RAS_O17:

RAS_O17: RAS - Pharmacy/treatment administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RAS_O17.RAS_O17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RAS_O17_PATIENT <hl7-v2_4-RAS_O17_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RAS_O17_ORDER <hl7-v2_4-RAS_O17_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-RCI_I05:

RCI_I05: Request for patient clinical information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RCI_I05.RCI_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RCI_I05_PROVIDER <hl7-v2_4-RCI_I05_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``OBSERVATION``
     - list[:ref:`RCI_I05_OBSERVATION <hl7-v2_4-RCI_I05_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RCL_I06:

RCL_I06: Request/receipt of clinical data listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RCL_I06.RCL_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RCL_I06_PROVIDER <hl7-v2_4-RCL_I06_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RDE_O11:

RDE_O11: RDE - Pharmacy/treatment encoded order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RDE_O11.RDE_O11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDE_O11_PATIENT <hl7-v2_4-RDE_O11_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDE_O11_ORDER <hl7-v2_4-RDE_O11_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-RDR_RDR:

RDR_RDR: RDR - Pharmacy dispense information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.RDR_RDR.RDR_RDR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`RDR_RDR_DEFINITION <hl7-v2_4-RDR_RDR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RDS_O13:

RDS_O13: RDS - Pharmacy/treatment dispense
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RDS_O13.RDS_O13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDS_O13_PATIENT <hl7-v2_4-RDS_O13_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDS_O13_ORDER <hl7-v2_4-RDS_O13_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-RDY_K15:

RDY_K15: query by parameter/display response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.RDY_K15.RDY_K15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-REF_I12:

REF_I12:  Patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.REF_I12.REF_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_4-REF_I12_AUTHORIZATION_CONTACT>`
     - O
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_4-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_4-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_4-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_4-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_4-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-REF_I13:

REF_I13: Modify patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.3

.. py:class:: hl7types.hl7.v2_4.messages.REF_I13.REF_I13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_4-REF_I12_AUTHORIZATION_CONTACT>`
     - O
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_4-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_4-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_4-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_4-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_4-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-REF_I14:

REF_I14: Cancel patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.4

.. py:class:: hl7types.hl7.v2_4.messages.REF_I14.REF_I14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_4-REF_I12_AUTHORIZATION_CONTACT>`
     - O
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_4-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_4-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_4-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_4-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_4-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-REF_I15:

REF_I15: Request patient referral status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.5

.. py:class:: hl7types.hl7.v2_4.messages.REF_I15.REF_I15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_4-REF_I12_AUTHORIZATION_CONTACT>`
     - O
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_4-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_4-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_4-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_4-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_4-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RER_RER:

RER_RER: RER - Pharmacy encoded order information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RER_RER.RER_RER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`RER_RER_DEFINITION <hl7-v2_4-RER_RER_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RGR_RGR:

RGR_RGR: RGR - Pharmacy dose information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RGR_RGR.RGR_RGR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``DEFINTION``
     - list[:ref:`RGR_RGR_DEFINTION <hl7-v2_4-RGR_RGR_DEFINTION>`]
     - R
     - DEFINTION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RGV_O15:

RGV_O15: RGV - Pharmacy/treatment give
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RGV_O15.RGV_O15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RGV_O15_PATIENT <hl7-v2_4-RGV_O15_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RGV_O15_ORDER <hl7-v2_4-RGV_O15_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_4-ROR_ROR:

ROR_ROR: ROR - Pharmacy prescription order query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.ROR_ROR.ROR_ROR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`ROR_ROR_DEFINITION <hl7-v2_4-ROR_ROR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RPA_I08:

RPA_I08: Request for treatment authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RPA_I08.RPA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RPA_I08_AUTHORIZATION <hl7-v2_4-RPA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RPA_I08_PROVIDER <hl7-v2_4-RPA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`RPA_I08_INSURANCE <hl7-v2_4-RPA_I08_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RPA_I08_PROCEDURE <hl7-v2_4-RPA_I08_PROCEDURE>`]
     - R
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RPA_I08_OBSERVATION <hl7-v2_4-RPA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RPA_I08_VISIT <hl7-v2_4-RPA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RPI_I01:

RPI_I01: Request for insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RPI_I01.RPI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPI_I01_PROVIDER <hl7-v2_4-RPI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_4-RPI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RPI_I04:

RPI_I04: Request for patient demographic data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RPI_I04.RPI_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPI_I04_PROVIDER <hl7-v2_4-RPI_I04_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RPI_I04_GUARANTOR_INSURANCE <hl7-v2_4-RPI_I04_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RPL_I02:

RPL_I02: Request/receipt of patient selection display list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RPL_I02.RPL_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPL_I02_PROVIDER <hl7-v2_4-RPL_I02_PROVIDER>`]
     - R
     - PROVIDER
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RPR_I03:

RPR_I03: Request/receipt of patient selection list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RPR_I03.RPR_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPR_I03_PROVIDER <hl7-v2_4-RPR_I03_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - list[:ref:`PID <hl7-v2_4-PID>`]
     - O
     - PID
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQA_I08:

RQA_I08: Request for treatment authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RQA_I08.RQA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_4-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_4-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_4-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_4-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_4-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_4-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQA_I09:

RQA_I09: Request for modification to an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.3

.. py:class:: hl7types.hl7.v2_4.messages.RQA_I09.RQA_I09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_4-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_4-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_4-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_4-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_4-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_4-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQA_I10:

RQA_I10: Request for resubmission of an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.4

.. py:class:: hl7types.hl7.v2_4.messages.RQA_I10.RQA_I10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_4-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_4-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_4-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_4-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_4-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_4-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQA_I11:

RQA_I11: Request for cancellation of an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.5

.. py:class:: hl7types.hl7.v2_4.messages.RQA_I11.RQA_I11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_4-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_4-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_4-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_4-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_4-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_4-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQC_I05:

RQC_I05: Request for patient clinical information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RQC_I05.RQC_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RQC_I05_PROVIDER <hl7-v2_4-RQC_I05_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQC_I06:

RQC_I06: Request/receipt of clinical data listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.6

.. py:class:: hl7types.hl7.v2_4.messages.RQC_I06.RQC_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RQC_I05_PROVIDER <hl7-v2_4-RQC_I05_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQI_I01:

RQI_I01: Request for insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RQI_I01.RQI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_4-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_4-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQI_I02:

RQI_I02: Request/receipt of patient selection display list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.2

.. py:class:: hl7types.hl7.v2_4.messages.RQI_I02.RQI_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_4-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_4-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQI_I03:

RQI_I03: Request/receipt of patient selection list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.3

.. py:class:: hl7types.hl7.v2_4.messages.RQI_I03.RQI_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_4-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_4-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQI_I07:

RQI_I07: Unsolicited insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.7

.. py:class:: hl7types.hl7.v2_4.messages.RQI_I07.RQI_I07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_4-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_4-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQP_I04:

RQP_I04: Request for patient demographic data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RQP_I04.RQP_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQP_I04_PROVIDER <hl7-v2_4-RQP_I04_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RQQ_Q09:

RQQ_Q09: RQQ - event replay query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.RQQ_Q09.RQQ_Q09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_4-ERQ>`
     - R
     - ERQ
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RRA_O18:

RRA_O18: RRA - Pharmacy/treatment administration acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RRA_O18.RRA_O18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRA_O18_RESPONSE <hl7-v2_4-RRA_O18_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-RRD_O14:

RRD_O14: RRD - Pharmacy/treatment dispense acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RRD_O14.RRD_O14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRD_O14_RESPONSE <hl7-v2_4-RRD_O14_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-RRE_O12:

RRE_O12: RRE - Pharmacy/treatment encoded order acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RRE_O12.RRE_O12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRE_O12_RESPONSE <hl7-v2_4-RRE_O12_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-RRG_O16:

RRG_O16: RRG - Pharmacy/treatment give acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.RRG_O16.RRG_O16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRG_O16_RESPONSE <hl7-v2_4-RRG_O16_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_4-RRI_I12:

RRI_I12:  Patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.messages.RRI_I12.RRI_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - O
     - MSA
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_4-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT``
     - :ref:`RRI_I12_AUTHORIZATION_CONTACT <hl7-v2_4-RRI_I12_AUTHORIZATION_CONTACT>`
     - O
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - list[:ref:`RRI_I12_PROVIDER_CONTACT <hl7-v2_4-RRI_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``ACC``
     - :ref:`ACC <hl7-v2_4-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_4-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_4-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_4-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RRI_I12_PROCEDURE <hl7-v2_4-RRI_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RRI_I12_OBSERVATION <hl7-v2_4-RRI_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`RRI_I12_PATIENT_VISIT <hl7-v2_4-RRI_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE

.. _hl7-v2_4-RSP_K11:

RSP_K11: query by parameter/segment pattern response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K11.RSP_K11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_K13:

RSP_K13: query by parameter/tabular response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K13.RSP_K13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RSP_K13_ROW_DEFINITION <hl7-v2_4-RSP_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_K15:

RSP_K15: query by parameter/display response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K15.RSP_K15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_K21:

RSP_K21: RSP - Get person demographics response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K21.RSP_K21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - :ref:`RSP_K21_QUERY_RESPONSE <hl7-v2_4-RSP_K21_QUERY_RESPONSE>`
     - O
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_K22:

RSP_K22: RSP - Find candidates response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K22.RSP_K22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_K22_QUERY_RESPONSE <hl7-v2_4-RSP_K22_QUERY_RESPONSE>`]
     - O
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_K23:

RSP_K23: RSP - Get corresponding identifiers response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K23.RSP_K23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - O
     - PID
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_K24:

RSP_K24: RSP - Allocate identifiers response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K24.RSP_K24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - O
     - PID
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_K25:

RSP_K25: RSP - Personnel Information by Segment Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_K25.RSP_K25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``STAFF``
     - list[:ref:`RSP_K25_STAFF <hl7-v2_4-RSP_K25_STAFF>`]
     - R
     - STAFF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_Z82:

RSP_Z82: Dispense History (response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_Z82.RSP_Z82
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z82_QUERY_RESPONSE <hl7-v2_4-RSP_Z82_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_Z86:

RSP_Z86: Pharmacy Information Comprehensive (response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_Z86.RSP_Z86
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z86_QUERY_RESPONSE <hl7-v2_4-RSP_Z86_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RSP_Z88:

RSP_Z88: Dispense Information (response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_Z88.RSP_Z88
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z88_QUERY_RESPONSE <hl7-v2_4-RSP_Z88_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - R
     - DSC

.. _hl7-v2_4-RSP_Z90:

RSP_Z90: Lab Results History (response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.messages.RSP_Z90.RSP_Z90
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_4-RCP>`
     - R
     - RCP
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z90_QUERY_RESPONSE <hl7-v2_4-RSP_Z90_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - R
     - DSC

.. _hl7-v2_4-RTB_K13:

RTB_K13: query by parameter/tabular response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.RTB_K13.RTB_K13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_K13_ROW_DEFINITION <hl7-v2_4-RTB_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RTB_Knn:

RTB_Knn: HL7 v2 RTB_Knn message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.messages.RTB_Knn.RTB_Knn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RTB_Q13:

RTB_Q13: quey by parameter/tabluar response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.RTB_Q13.RTB_Q13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_Q13_ROW_DEFINITION <hl7-v2_4-RTB_Q13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-RTB_Z74:

RTB_Z74: Information about Phone Calls (response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.RTB_Z74.RTB_Z74
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_4-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_Z74_ROW_DEFINITION <hl7-v2_4-RTB_Z74_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-SIU_S12:

SIU_S12: Notification of new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S12.SIU_S12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S13:

SIU_S13: Notification of appointment rescheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.7.2

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S13.SIU_S13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S14:

SIU_S14: Notification of appointment modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.3

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S14.SIU_S14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S15:

SIU_S15: Notification of appointment cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.4

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S15.SIU_S15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S16:

SIU_S16: Notification of appointment discontinuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.5

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S16.SIU_S16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S17:

SIU_S17: Notification of appointment deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.6

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S17.SIU_S17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S18:

SIU_S18: Notification of addition of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.7

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S18.SIU_S18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S19:

SIU_S19: Notification of modification of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.8

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S19.SIU_S19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S20:

SIU_S20: Notification of cancellation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.9

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S20.SIU_S20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S21:

SIU_S21: Notification of discontinuation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.10

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S21.SIU_S21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S22:

SIU_S22: Notification of deletion of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.11

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S22.SIU_S22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S23:

SIU_S23: Notification of blocked schedule time slot(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.12

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S23.SIU_S23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S24:

SIU_S24: Notification of opened ("unblocked"") schedule time slot(s)"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.13

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S24.SIU_S24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SIU_S26:

SIU_S26: Notification that patient did not show up for schedule appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4.14

.. py:class:: hl7types.hl7.v2_4.messages.SIU_S26.SIU_S26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_4-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_4-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SPQ_Q08:

SPQ_Q08: SPQ - Stored procedure request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.SPQ_Q08.SPQ_Q08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``SPR``
     - :ref:`SPR <hl7-v2_4-SPR>`
     - R
     - SPR
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-SQM_S25:

SQM_S25: Schedule query message and response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10

.. py:class:: hl7types.hl7.v2_4.messages.SQM_S25.SQM_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``REQUEST``
     - :ref:`SQM_S25_REQUEST <hl7-v2_4-SQM_S25_REQUEST>`
     - O
     - REQUEST
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-SQR_S25:

SQR_S25: Schedule query message and response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10

.. py:class:: hl7types.hl7.v2_4.messages.SQR_S25.SQR_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``SCHEDULE``
     - list[:ref:`SQR_S25_SCHEDULE <hl7-v2_4-SQR_S25_SCHEDULE>`]
     - O
     - SCHEDULE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-SRM_S01:

SRM_S01: Request new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S01.SRM_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S02:

SRM_S02: Request appointment rescheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.2

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S02.SRM_S02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S03:

SRM_S03: Request appointment modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.3

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S03.SRM_S03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S04:

SRM_S04: Request appointment cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.4

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S04.SRM_S04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S05:

SRM_S05: Request appointment discontinuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.5

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S05.SRM_S05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S06:

SRM_S06: Request appointment deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.6

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S06.SRM_S06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S07:

SRM_S07: Request addition of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.7

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S07.SRM_S07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S08:

SRM_S08: Request modification of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.8

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S08.SRM_S08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S09:

SRM_S09: Request cancellation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.9

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S09.SRM_S09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S10:

SRM_S10: Request discontinuation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.10

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S10.SRM_S10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRM_S11:

SRM_S11: Request deletion of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.11

.. py:class:: hl7types.hl7.v2_4.messages.SRM_S11.SRM_S11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_4-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_4-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_4-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_4-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_4-SRR_S01:

SRR_S01: Request new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10

.. py:class:: hl7types.hl7.v2_4.messages.SRR_S01.SRR_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``SCHEDULE``
     - :ref:`SRR_S01_SCHEDULE <hl7-v2_4-SRR_S01_SCHEDULE>`
     - O
     - SCHEDULE

.. _hl7-v2_4-SSR_U04:

SSR_U04: specimen status request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.SSR_U04.SSR_U04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``SAC``
     - list[:ref:`SAC <hl7-v2_4-SAC>`]
     - R
     - SAC
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-SSU_U03:

SSU_U03: Specimen status update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.SSU_U03.SSU_U03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``SPECIMEN_CONTAINER``
     - list[:ref:`SSU_U03_SPECIMEN_CONTAINER <hl7-v2_4-SSU_U03_SPECIMEN_CONTAINER>`]
     - R
     - SPECIMEN_CONTAINER
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-SUR_P09:

SUR_P09: SUR - Summary product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7

.. py:class:: hl7types.hl7.v2_4.messages.SUR_P09.SUR_P09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``FACILITY``
     - list[:ref:`SUR_P09_FACILITY <hl7-v2_4-SUR_P09_FACILITY>`]
     - R
     - FACILITY

.. _hl7-v2_4-TBR_R08:

TBR_R08: Tabular Data Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.TBR_R08.TBR_R08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_4-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_4-QAK>`
     - R
     - QAK
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - R
     - RDF
   * - ``RDT``
     - list[:ref:`RDT <hl7-v2_4-RDT>`]
     - R
     - RDT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-TCU_U10:

TCU_U10: Automated equipment test code settings update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13

.. py:class:: hl7types.hl7.v2_4.messages.TCU_U10.TCU_U10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``TCC``
     - list[:ref:`TCC <hl7-v2_4-TCC>`]
     - R
     - TCC
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-TCU_U11:

TCU_U11: Automated equipment test code settings request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.11

.. py:class:: hl7types.hl7.v2_4.messages.TCU_U11.TCU_U11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``EQU``
     - :ref:`EQU <hl7-v2_4-EQU>`
     - R
     - EQU
   * - ``TCC``
     - list[:ref:`TCC <hl7-v2_4-TCC>`]
     - R
     - TCC
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - O
     - ROL

.. _hl7-v2_4-UDM_Q05:

UDM_Q05: Unsolicited display update message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``URD``
     - :ref:`URD <hl7-v2_4-URD>`
     - R
     - URD
   * - ``URS``
     - :ref:`URS <hl7-v2_4-URS>`
     - O
     - URS
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_4-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-VQQ_Q07:

VQQ_Q07: VQQ - Virtual table query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5

.. py:class:: hl7types.hl7.v2_4.messages.VQQ_Q07.VQQ_Q07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``VTQ``
     - :ref:`VTQ <hl7-v2_4-VTQ>`
     - R
     - VTQ
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - O
     - RDF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_4-DSC>`
     - O
     - DSC

.. _hl7-v2_4-VXQ_V01:

VXQ_V01: VXQ - Query for vaccination record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.VXQ_V01.VXQ_V01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF

.. _hl7-v2_4-VXR_V03:

VXR_V03: VXR - Vaccination record response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.VXR_V03.VXR_V03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PATIENT_VISIT``
     - :ref:`VXR_V03_PATIENT_VISIT <hl7-v2_4-VXR_V03_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`VXR_V03_INSURANCE <hl7-v2_4-VXR_V03_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ORDER``
     - list[:ref:`VXR_V03_ORDER <hl7-v2_4-VXR_V03_ORDER>`]
     - O
     - ORDER

.. _hl7-v2_4-VXU_V04:

VXU_V04: VXU - Unsolicited vaccination record update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.VXU_V04.VXU_V04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_4-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_4-NK1>`]
     - O
     - NK1
   * - ``PATIENT``
     - :ref:`VXU_V04_PATIENT <hl7-v2_4-VXU_V04_PATIENT>`
     - O
     - PATIENT
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_4-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`VXU_V04_INSURANCE <hl7-v2_4-VXU_V04_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ORDER``
     - list[:ref:`VXU_V04_ORDER <hl7-v2_4-VXU_V04_ORDER>`]
     - O
     - ORDER

.. _hl7-v2_4-VXX_V02:

VXX_V02: VXX - Response to vaccination query returning multiple PID matches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.messages.VXX_V02.VXX_V02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_4-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_4-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_4-QRF>`
     - O
     - QRF
   * - ``PATIENT``
     - list[:ref:`VXX_V02_PATIENT <hl7-v2_4-VXX_V02_PATIENT>`]
     - R
     - PATIENT
