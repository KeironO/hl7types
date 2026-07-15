v2.8 Messages
=============

.. _hl7-v2_8-ACK:

ACK: General acknowledgment message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR

.. _hl7-v2_8-ADT_A01:

ADT_A01: Admit/visit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_8-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_8-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_8-PDA>`
     - O
     - PDA

.. _hl7-v2_8-ADT_A02:

ADT_A02: Transfer a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``PDA``
     - :ref:`PDA <hl7-v2_8-PDA>`
     - O
     - PDA

.. _hl7-v2_8-ADT_A03:

ADT_A03:  Discharge/end visit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A03_PROCEDURE <hl7-v2_8-ADT_A03_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A03_INSURANCE <hl7-v2_8-ADT_A03_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``PDA``
     - :ref:`PDA <hl7-v2_8-PDA>`
     - O
     - PDA

.. _hl7-v2_8-ADT_A04:

ADT_A04:  Register a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.4

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_8-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_8-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_8-PDA>`
     - O
     - PDA

.. _hl7-v2_8-ADT_A05:

ADT_A05:  Pre-admit a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_8-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_8-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2

.. _hl7-v2_8-ADT_A06:

ADT_A06:  Change an outpatient to an inpatient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``MRG``
     - :ref:`MRG <hl7-v2_8-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A06_PROCEDURE <hl7-v2_8-ADT_A06_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A06_INSURANCE <hl7-v2_8-ADT_A06_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2

.. _hl7-v2_8-ADT_A07:

ADT_A07:  Change an inpatient to an outpatient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.7

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``MRG``
     - :ref:`MRG <hl7-v2_8-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A06_PROCEDURE <hl7-v2_8-ADT_A06_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A06_INSURANCE <hl7-v2_8-ADT_A06_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2

.. _hl7-v2_8-ADT_A08:

ADT_A08:  Update patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.8

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_8-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_8-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_8-PDA>`
     - O
     - PDA

.. _hl7-v2_8-ADT_A09:

ADT_A09:  Patient departing - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1

.. _hl7-v2_8-ADT_A10:

ADT_A10:  Patient arriving - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.10

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1

.. _hl7-v2_8-ADT_A11:

ADT_A11:  Cancel admit/visit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.11

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1

.. _hl7-v2_8-ADT_A12:

ADT_A12:  Cancel transfer
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - :ref:`DG1 <hl7-v2_8-DG1>`
     - O
     - DG1

.. _hl7-v2_8-ADT_A13:

ADT_A13:  Cancel discharge/end visit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.13

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_8-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_8-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2
   * - ``PDA``
     - :ref:`PDA <hl7-v2_8-PDA>`
     - O
     - PDA

.. _hl7-v2_8-ADT_A14:

ADT_A14:  Pending admit
~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.14

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_8-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_8-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2

.. _hl7-v2_8-ADT_A15:

ADT_A15:  Pending transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A16:

ADT_A16:  Pending discharge
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A16_PROCEDURE <hl7-v2_8-ADT_A16_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A16_INSURANCE <hl7-v2_8-ADT_A16_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC

.. _hl7-v2_8-ADT_A17:

ADT_A17:  Swap patients
~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A20:

ADT_A20:  Bed status update
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``NPU``
     - :ref:`NPU <hl7-v2_8-NPU>`
     - R
     - NPU

.. _hl7-v2_8-ADT_A21:

ADT_A21:  Patient goes on a "leave of absence"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A22:

ADT_A22:  Patient returns from a "leave of absence"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.22

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A22.ADT_A22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A23:

ADT_A23:  Delete a patient record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.23

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A23.ADT_A23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A24:

ADT_A24:  Link patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - O
     - PV1
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1

.. _hl7-v2_8-ADT_A25:

ADT_A25:  Cancel pending discharge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.25

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A25.ADT_A25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A26:

ADT_A26:  Cancel pending transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.26

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A26.ADT_A26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A27:

ADT_A27:  Cancel pending admit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.27

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A27.ADT_A27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A28:

ADT_A28:  Add person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.28

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_8-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_8-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2

.. _hl7-v2_8-ADT_A29:

ADT_A29:  Delete person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.29

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A29.ADT_A29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A31:

ADT_A31:  Update person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.31

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A05_PROCEDURE <hl7-v2_8-ADT_A05_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_8-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_8-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_8-UB2>`
     - O
     - UB2

.. _hl7-v2_8-ADT_A32:

ADT_A32:  Cancel patient arriving - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.32

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A32.ADT_A32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A33:

ADT_A33:  Cancel patient departing - tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.33

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A33.ADT_A33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX

.. _hl7-v2_8-ADT_A37:

ADT_A37:  Unlink patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - O
     - PV1
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1

.. _hl7-v2_8-ADT_A38:

ADT_A38: Cancel pre-admit
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A38.ADT_A38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_8-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG

.. _hl7-v2_8-ADT_A39:

ADT_A39: HL7 v2 ADT_A39 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A39.ADT_A39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_8-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-ADT_A43:

ADT_A43: Move patient information - patient identifier list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A43.ADT_A43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A43_PATIENT <hl7-v2_8-ADT_A43_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-ADT_A44:

ADT_A44: Move account information - patient account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A44.ADT_A44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A44_PATIENT <hl7-v2_8-ADT_A44_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-ADT_A45:

ADT_A45: Move visit information - visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A45.ADT_A45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``MERGE_INFO``
     - list[:ref:`ADT_A45_MERGE_INFO <hl7-v2_8-ADT_A45_MERGE_INFO>`]
     - R
     - MERGE_INFO

.. _hl7-v2_8-ADT_A47:

ADT_A47: Change patient identifier list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.47

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A47.ADT_A47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A44_PATIENT <hl7-v2_8-ADT_A44_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-ADT_A49:

ADT_A49: Change patient account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.49

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A49.ADT_A49
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A43_PATIENT <hl7-v2_8-ADT_A43_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-ADT_A50:

ADT_A50: Change visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A50.ADT_A50
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_8-MRG>`
     - R
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1

.. _hl7-v2_8-ADT_A51:

ADT_A51: Change alternate visit ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.51

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A51.ADT_A51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_8-MRG>`
     - R
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1

.. _hl7-v2_8-ADT_A52:

ADT_A52: Cancel leave of absence for a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A52.ADT_A52
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2

.. _hl7-v2_8-ADT_A53:

ADT_A53: Cancel patient returns from a leave of absence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.53

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A53.ADT_A53
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2

.. _hl7-v2_8-ADT_A54:

ADT_A54: Change attending doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A54.ADT_A54
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2

.. _hl7-v2_8-ADT_A55:

ADT_A55: Cancel change attending doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.55

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A55.ADT_A55
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2

.. _hl7-v2_8-ADT_A60:

ADT_A60: Update allergy information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A60.ADT_A60
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``VISIT``
     - :ref:`ADT_A60_VISIT <hl7-v2_8-ADT_A60_VISIT>`
     - O
     - VISIT
   * - ``ADVERSE_REACTION_GROUP``
     - list[:ref:`ADT_A60_ADVERSE_REACTION_GROUP <hl7-v2_8-ADT_A60_ADVERSE_REACTION_GROUP>`]
     - O
     - ADVERSE_REACTION_GROUP

.. _hl7-v2_8-ADT_A61:

ADT_A61: Change consulting doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A61.ADT_A61
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2

.. _hl7-v2_8-ADT_A62:

ADT_A62: Cancel change consulting doctor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.62

.. py:class:: hl7types.hl7.v2_8.messages.ADT_A62.ADT_A62
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2

.. _hl7-v2_8-BAR_P01:

BAR_P01: Add patient accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_8.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``VISIT``
     - list[:ref:`BAR_P01_VISIT <hl7-v2_8-BAR_P01_VISIT>`]
     - R
     - VISIT

.. _hl7-v2_8-BAR_P02:

BAR_P02: Purge patient accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_8.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`BAR_P02_PATIENT <hl7-v2_8-BAR_P02_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-BAR_P05:

BAR_P05: Update account
~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_8.messages.BAR_P05.BAR_P05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``VISIT``
     - list[:ref:`BAR_P05_VISIT <hl7-v2_8-BAR_P05_VISIT>`]
     - R
     - VISIT

.. _hl7-v2_8-BAR_P06:

BAR_P06: End account
~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_8.messages.BAR_P06.BAR_P06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`BAR_P06_PATIENT <hl7-v2_8-BAR_P06_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-BAR_P10:

BAR_P10: BAR/ACK -Transmit Ambulatory Payment  Classification(APC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_8.messages.BAR_P10.BAR_P10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``GP1``
     - :ref:`GP1 <hl7-v2_8-GP1>`
     - R
     - GP1
   * - ``PROCEDURE``
     - list[:ref:`BAR_P10_PROCEDURE <hl7-v2_8-BAR_P10_PROCEDURE>`]
     - O
     - PROCEDURE

.. _hl7-v2_8-BAR_P12:

BAR_P12: Update Diagnosis/Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.1

.. py:class:: hl7types.hl7.v2_8.messages.BAR_P12.BAR_P12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`BAR_P12_PROCEDURE <hl7-v2_8-BAR_P12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBX``
     - :ref:`OBX <hl7-v2_8-OBX>`
     - O
     - OBX

.. _hl7-v2_8-BPS_O29:

BPS_O29: BPS - Blood product dispense status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.3

.. py:class:: hl7types.hl7.v2_8.messages.BPS_O29.BPS_O29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`BPS_O29_PATIENT <hl7-v2_8-BPS_O29_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`BPS_O29_ORDER <hl7-v2_8-BPS_O29_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-BRP_O30:

BRP_O30: BRP - Blood product dispense status acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.4

.. py:class:: hl7types.hl7.v2_8.messages.BRP_O30.BRP_O30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`BRP_O30_RESPONSE <hl7-v2_8-BRP_O30_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-BRT_O32:

BRT_O32: BRT - Blood product transfusion/disposition acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.6

.. py:class:: hl7types.hl7.v2_8.messages.BRT_O32.BRT_O32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`BRT_O32_RESPONSE <hl7-v2_8-BRT_O32_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-BTS_O31:

BTS_O31: BTS - Blood product transfusion/disposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.5

.. py:class:: hl7types.hl7.v2_8.messages.BTS_O31.BTS_O31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`BTS_O31_PATIENT <hl7-v2_8-BTS_O31_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`BTS_O31_ORDER <hl7-v2_8-BTS_O31_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-CCF_I22:

CCF_I22: Collaborative Care Fetch / Collaborative Care Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.7.2

.. py:class:: hl7types.hl7.v2_8.messages.CCF_I22.CCF_I22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID

.. _hl7-v2_8-CCI_I22:

CCI_I22: Collaborative Care Fetch / Collaborative Care Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.7.2

.. py:class:: hl7types.hl7.v2_8.messages.CCI_I22.CCI_I22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``INSURANCE``
     - list[:ref:`CCI_I22_INSURANCE <hl7-v2_8-CCI_I22_INSURANCE>`]
     - O
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - list[:ref:`CCI_I22_APPOINTMENT_HISTORY <hl7-v2_8-CCI_I22_APPOINTMENT_HISTORY>`]
     - O
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - list[:ref:`CCI_I22_CLINICAL_HISTORY <hl7-v2_8-CCI_I22_CLINICAL_HISTORY>`]
     - O
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - list[:ref:`CCI_I22_PATIENT_VISITS <hl7-v2_8-CCI_I22_PATIENT_VISITS>`]
     - R
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - list[:ref:`CCI_I22_MEDICATION_HISTORY <hl7-v2_8-CCI_I22_MEDICATION_HISTORY>`]
     - O
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - list[:ref:`CCI_I22_PROBLEM <hl7-v2_8-CCI_I22_PROBLEM>`]
     - O
     - PROBLEM
   * - ``GOAL``
     - list[:ref:`CCI_I22_GOAL <hl7-v2_8-CCI_I22_GOAL>`]
     - O
     - GOAL
   * - ``PATHWAY``
     - list[:ref:`CCI_I22_PATHWAY <hl7-v2_8-CCI_I22_PATHWAY>`]
     - O
     - PATHWAY
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CCM_I21:

CCM_I21: Collaborative Care Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.6.1

.. py:class:: hl7types.hl7.v2_8.messages.CCM_I21.CCM_I21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``INSURANCE``
     - list[:ref:`CCM_I21_INSURANCE <hl7-v2_8-CCM_I21_INSURANCE>`]
     - O
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - list[:ref:`CCM_I21_APPOINTMENT_HISTORY <hl7-v2_8-CCM_I21_APPOINTMENT_HISTORY>`]
     - O
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - list[:ref:`CCM_I21_CLINICAL_HISTORY <hl7-v2_8-CCM_I21_CLINICAL_HISTORY>`]
     - O
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - list[:ref:`CCM_I21_PATIENT_VISITS <hl7-v2_8-CCM_I21_PATIENT_VISITS>`]
     - R
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - list[:ref:`CCM_I21_MEDICATION_HISTORY <hl7-v2_8-CCM_I21_MEDICATION_HISTORY>`]
     - O
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - list[:ref:`CCM_I21_PROBLEM <hl7-v2_8-CCM_I21_PROBLEM>`]
     - O
     - PROBLEM
   * - ``GOAL``
     - list[:ref:`CCM_I21_GOAL <hl7-v2_8-CCM_I21_GOAL>`]
     - O
     - GOAL
   * - ``PATHWAY``
     - list[:ref:`CCM_I21_PATHWAY <hl7-v2_8-CCM_I21_PATHWAY>`]
     - O
     - PATHWAY
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CCQ_I19:

CCQ_I19: Collaborative Care Query/Collaborative Care Query Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CCQ_I19.CCQ_I19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - R
     - RF1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`CCQ_I19_PROVIDER_CONTACT <hl7-v2_8-CCQ_I19_PROVIDER_CONTACT>`]
     - O
     - PROVIDER_CONTACT
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CCR_I16:

CCR_I16: Collaborative Care Referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.6.2

.. py:class:: hl7types.hl7.v2_8.messages.CCR_I16.CCR_I16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - list[:ref:`RF1 <hl7-v2_8-RF1>`]
     - R
     - RF1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`CCR_I16_PROVIDER_CONTACT <hl7-v2_8-CCR_I16_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``CLINICAL_ORDER``
     - list[:ref:`CCR_I16_CLINICAL_ORDER <hl7-v2_8-CCR_I16_CLINICAL_ORDER>`]
     - O
     - CLINICAL_ORDER
   * - ``PATIENT``
     - list[:ref:`CCR_I16_PATIENT <hl7-v2_8-CCR_I16_PATIENT>`]
     - R
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``INSURANCE``
     - list[:ref:`CCR_I16_INSURANCE <hl7-v2_8-CCR_I16_INSURANCE>`]
     - O
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - list[:ref:`CCR_I16_APPOINTMENT_HISTORY <hl7-v2_8-CCR_I16_APPOINTMENT_HISTORY>`]
     - O
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - list[:ref:`CCR_I16_CLINICAL_HISTORY <hl7-v2_8-CCR_I16_CLINICAL_HISTORY>`]
     - O
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - list[:ref:`CCR_I16_PATIENT_VISITS <hl7-v2_8-CCR_I16_PATIENT_VISITS>`]
     - R
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - list[:ref:`CCR_I16_MEDICATION_HISTORY <hl7-v2_8-CCR_I16_MEDICATION_HISTORY>`]
     - O
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - list[:ref:`CCR_I16_PROBLEM <hl7-v2_8-CCR_I16_PROBLEM>`]
     - O
     - PROBLEM
   * - ``GOAL``
     - list[:ref:`CCR_I16_GOAL <hl7-v2_8-CCR_I16_GOAL>`]
     - O
     - GOAL
   * - ``PATHWAY``
     - list[:ref:`CCR_I16_PATHWAY <hl7-v2_8-CCR_I16_PATHWAY>`]
     - O
     - PATHWAY
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CCR_I17:

CCR_I17: Modify Collaborative Care Referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.6.2

.. py:class:: hl7types.hl7.v2_8.messages.CCR_I17.CCR_I17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - list[:ref:`RF1 <hl7-v2_8-RF1>`]
     - R
     - RF1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`CCR_I16_PROVIDER_CONTACT <hl7-v2_8-CCR_I16_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``CLINICAL_ORDER``
     - list[:ref:`CCR_I16_CLINICAL_ORDER <hl7-v2_8-CCR_I16_CLINICAL_ORDER>`]
     - O
     - CLINICAL_ORDER
   * - ``PATIENT``
     - list[:ref:`CCR_I16_PATIENT <hl7-v2_8-CCR_I16_PATIENT>`]
     - R
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``INSURANCE``
     - list[:ref:`CCR_I16_INSURANCE <hl7-v2_8-CCR_I16_INSURANCE>`]
     - O
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - list[:ref:`CCR_I16_APPOINTMENT_HISTORY <hl7-v2_8-CCR_I16_APPOINTMENT_HISTORY>`]
     - O
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - list[:ref:`CCR_I16_CLINICAL_HISTORY <hl7-v2_8-CCR_I16_CLINICAL_HISTORY>`]
     - O
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - list[:ref:`CCR_I16_PATIENT_VISITS <hl7-v2_8-CCR_I16_PATIENT_VISITS>`]
     - R
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - list[:ref:`CCR_I16_MEDICATION_HISTORY <hl7-v2_8-CCR_I16_MEDICATION_HISTORY>`]
     - O
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - list[:ref:`CCR_I16_PROBLEM <hl7-v2_8-CCR_I16_PROBLEM>`]
     - O
     - PROBLEM
   * - ``GOAL``
     - list[:ref:`CCR_I16_GOAL <hl7-v2_8-CCR_I16_GOAL>`]
     - O
     - GOAL
   * - ``PATHWAY``
     - list[:ref:`CCR_I16_PATHWAY <hl7-v2_8-CCR_I16_PATHWAY>`]
     - O
     - PATHWAY
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CCR_I18:

CCR_I18: Cancel Collaborative Care Referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.6.2

.. py:class:: hl7types.hl7.v2_8.messages.CCR_I18.CCR_I18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - list[:ref:`RF1 <hl7-v2_8-RF1>`]
     - R
     - RF1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`CCR_I16_PROVIDER_CONTACT <hl7-v2_8-CCR_I16_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``CLINICAL_ORDER``
     - list[:ref:`CCR_I16_CLINICAL_ORDER <hl7-v2_8-CCR_I16_CLINICAL_ORDER>`]
     - O
     - CLINICAL_ORDER
   * - ``PATIENT``
     - list[:ref:`CCR_I16_PATIENT <hl7-v2_8-CCR_I16_PATIENT>`]
     - R
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``INSURANCE``
     - list[:ref:`CCR_I16_INSURANCE <hl7-v2_8-CCR_I16_INSURANCE>`]
     - O
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - list[:ref:`CCR_I16_APPOINTMENT_HISTORY <hl7-v2_8-CCR_I16_APPOINTMENT_HISTORY>`]
     - O
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - list[:ref:`CCR_I16_CLINICAL_HISTORY <hl7-v2_8-CCR_I16_CLINICAL_HISTORY>`]
     - O
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - list[:ref:`CCR_I16_PATIENT_VISITS <hl7-v2_8-CCR_I16_PATIENT_VISITS>`]
     - R
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - list[:ref:`CCR_I16_MEDICATION_HISTORY <hl7-v2_8-CCR_I16_MEDICATION_HISTORY>`]
     - O
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - list[:ref:`CCR_I16_PROBLEM <hl7-v2_8-CCR_I16_PROBLEM>`]
     - O
     - PROBLEM
   * - ``GOAL``
     - list[:ref:`CCR_I16_GOAL <hl7-v2_8-CCR_I16_GOAL>`]
     - O
     - GOAL
   * - ``PATHWAY``
     - list[:ref:`CCR_I16_PATHWAY <hl7-v2_8-CCR_I16_PATHWAY>`]
     - O
     - PATHWAY
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CCU_I20:

CCU_I20: Asynchronous Collaborative Care Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.6.6

.. py:class:: hl7types.hl7.v2_8.messages.CCU_I20.CCU_I20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - R
     - RF1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`CCU_I20_PROVIDER_CONTACT <hl7-v2_8-CCU_I20_PROVIDER_CONTACT>`]
     - O
     - PROVIDER_CONTACT
   * - ``PATIENT``
     - list[:ref:`CCU_I20_PATIENT <hl7-v2_8-CCU_I20_PATIENT>`]
     - O
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``INSURANCE``
     - list[:ref:`CCU_I20_INSURANCE <hl7-v2_8-CCU_I20_INSURANCE>`]
     - O
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - list[:ref:`CCU_I20_APPOINTMENT_HISTORY <hl7-v2_8-CCU_I20_APPOINTMENT_HISTORY>`]
     - O
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - list[:ref:`CCU_I20_CLINICAL_HISTORY <hl7-v2_8-CCU_I20_CLINICAL_HISTORY>`]
     - O
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - list[:ref:`CCU_I20_PATIENT_VISITS <hl7-v2_8-CCU_I20_PATIENT_VISITS>`]
     - R
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - list[:ref:`CCU_I20_MEDICATION_HISTORY <hl7-v2_8-CCU_I20_MEDICATION_HISTORY>`]
     - O
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - list[:ref:`CCU_I20_PROBLEM <hl7-v2_8-CCU_I20_PROBLEM>`]
     - O
     - PROBLEM
   * - ``GOAL``
     - list[:ref:`CCU_I20_GOAL <hl7-v2_8-CCU_I20_GOAL>`]
     - O
     - GOAL
   * - ``PATHWAY``
     - list[:ref:`CCU_I20_PATHWAY <hl7-v2_8-CCU_I20_PATHWAY>`]
     - O
     - PATHWAY
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CQU_I19:

CQU_I19: Collaborative Care Query/Collaborative Care Query Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CQU_I19.CQU_I19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - R
     - RF1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`CQU_I19_PROVIDER_CONTACT <hl7-v2_8-CQU_I19_PROVIDER_CONTACT>`]
     - O
     - PROVIDER_CONTACT
   * - ``PATIENT``
     - list[:ref:`CQU_I19_PATIENT <hl7-v2_8-CQU_I19_PATIENT>`]
     - O
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``INSURANCE``
     - list[:ref:`CQU_I19_INSURANCE <hl7-v2_8-CQU_I19_INSURANCE>`]
     - O
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - list[:ref:`CQU_I19_APPOINTMENT_HISTORY <hl7-v2_8-CQU_I19_APPOINTMENT_HISTORY>`]
     - O
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - list[:ref:`CQU_I19_CLINICAL_HISTORY <hl7-v2_8-CQU_I19_CLINICAL_HISTORY>`]
     - O
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - list[:ref:`CQU_I19_PATIENT_VISITS <hl7-v2_8-CQU_I19_PATIENT_VISITS>`]
     - R
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - list[:ref:`CQU_I19_MEDICATION_HISTORY <hl7-v2_8-CQU_I19_MEDICATION_HISTORY>`]
     - O
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - list[:ref:`CQU_I19_PROBLEM <hl7-v2_8-CQU_I19_PROBLEM>`]
     - O
     - PROBLEM
   * - ``GOAL``
     - list[:ref:`CQU_I19_GOAL <hl7-v2_8-CQU_I19_GOAL>`]
     - O
     - GOAL
   * - ``PATHWAY``
     - list[:ref:`CQU_I19_PATHWAY <hl7-v2_8-CQU_I19_PATHWAY>`]
     - O
     - PATHWAY
   * - ``REL``
     - list[:ref:`REL <hl7-v2_8-REL>`]
     - O
     - REL

.. _hl7-v2_8-CRM_C01:

CRM_C01: CRM - Register a patient on a clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C01.CRM_C01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CRM_C02:

CRM_C02: CRM - Cancel a patient registration on clinical trial (for clerical mistakes onl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C02.CRM_C02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CRM_C03:

CRM_C03: CRM - Correct/update registration information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C03.CRM_C03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CRM_C04:

CRM_C04: CRM - Patient has gone off a clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C04.CRM_C04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CRM_C05:

CRM_C05: CRM - Patient enters phase of clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C05.CRM_C05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CRM_C06:

CRM_C06: CRM - Cancel patient entering a phase (clerical mistake)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C06.CRM_C06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CRM_C07:

CRM_C07: CRM - Correct/update phase information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C07.CRM_C07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CRM_C08:

CRM_C08: CRM - Patient has gone off phase of clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.1

.. py:class:: hl7types.hl7.v2_8.messages.CRM_C08.CRM_C08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_8-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CSU_C09:

CSU_C09: CSU - Automated time intervals for reporting, like monthly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_8.messages.CSU_C09.CSU_C09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_8-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CSU_C10:

CSU_C10: CSU - Patient completes the clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_8.messages.CSU_C10.CSU_C10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_8-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CSU_C11:

CSU_C11: CSU - Patient completes a phase of the clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_8.messages.CSU_C11.CSU_C11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_8-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-CSU_C12:

CSU_C12: CSU - Update/correction of patient order/result information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.7.2

.. py:class:: hl7types.hl7.v2_8.messages.CSU_C12.CSU_C12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_8-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_8-DBC_O41:

DBC_O41: DBC - Create Donor Record Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.4

.. py:class:: hl7types.hl7.v2_8.messages.DBC_O41.DBC_O41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DBC_O41_DONOR <hl7-v2_8-DBC_O41_DONOR>`
     - O
     - DONOR

.. _hl7-v2_8-DBC_O42:

DBC_O42: DBU - Update Donor Record Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.4

.. py:class:: hl7types.hl7.v2_8.messages.DBC_O42.DBC_O42
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DBC_O42_DONOR <hl7-v2_8-DBC_O42_DONOR>`
     - O
     - DONOR

.. _hl7-v2_8-DEL_O46:

DEL_O46: Donor Eligiblity Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.13

.. py:class:: hl7types.hl7.v2_8.messages.DEL_O46.DEL_O46
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DEL_O46_DONOR <hl7-v2_8-DEL_O46_DONOR>`
     - O
     - DONOR
   * - ``DON``
     - :ref:`DON <hl7-v2_8-DON>`
     - R
     - DON
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-DEO_O45:

DEO_O45: Donor Eligibility Observations Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.12

.. py:class:: hl7types.hl7.v2_8.messages.DEO_O45.DEO_O45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DEO_O45_DONOR <hl7-v2_8-DEO_O45_DONOR>`
     - O
     - DONOR
   * - ``DONOR_ORDER``
     - list[:ref:`DEO_O45_DONOR_ORDER <hl7-v2_8-DEO_O45_DONOR_ORDER>`]
     - R
     - DONOR_ORDER

.. _hl7-v2_8-DER_O44:

DER_O44: Donor Registration - Minimal Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.11

.. py:class:: hl7types.hl7.v2_8.messages.DER_O44.DER_O44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DER_O44_DONOR <hl7-v2_8-DER_O44_DONOR>`
     - O
     - DONOR
   * - ``DONOR_ORDER``
     - list[:ref:`DER_O44_DONOR_ORDER <hl7-v2_8-DER_O44_DONOR_ORDER>`]
     - R
     - DONOR_ORDER

.. _hl7-v2_8-DFT_P03:

DFT_P03: Post detail financial transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.3

.. py:class:: hl7types.hl7.v2_8.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``VISIT``
     - :ref:`DFT_P03_VISIT <hl7-v2_8-DFT_P03_VISIT>`
     - O
     - VISIT
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``COMMON_ORDER``
     - list[:ref:`DFT_P03_COMMON_ORDER <hl7-v2_8-DFT_P03_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``FINANCIAL``
     - list[:ref:`DFT_P03_FINANCIAL <hl7-v2_8-DFT_P03_FINANCIAL>`]
     - R
     - FINANCIAL
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`DFT_P03_INSURANCE <hl7-v2_8-DFT_P03_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC

.. _hl7-v2_8-DFT_P11:

DFT_P11: Post Detail Financial Transactions - New
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.3

.. py:class:: hl7types.hl7.v2_8.messages.DFT_P11.DFT_P11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL
   * - ``VISIT``
     - :ref:`DFT_P11_VISIT <hl7-v2_8-DFT_P11_VISIT>`
     - O
     - VISIT
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_8-DB1>`]
     - O
     - DB1
   * - ``COMMON_ORDER``
     - list[:ref:`DFT_P11_COMMON_ORDER <hl7-v2_8-DFT_P11_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_8-DRG>`
     - O
     - DRG
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`DFT_P11_INSURANCE <hl7-v2_8-DFT_P11_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``FINANCIAL``
     - list[:ref:`DFT_P11_FINANCIAL <hl7-v2_8-DFT_P11_FINANCIAL>`]
     - R
     - FINANCIAL

.. _hl7-v2_8-DPR_O48:

DPR_O48: Donation Procedure Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.15

.. py:class:: hl7types.hl7.v2_8.messages.DPR_O48.DPR_O48
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DPR_O48_DONOR <hl7-v2_8-DPR_O48_DONOR>`
     - O
     - DONOR
   * - ``DONATION_ORDER``
     - list[:ref:`DPR_O48_DONATION_ORDER <hl7-v2_8-DPR_O48_DONATION_ORDER>`]
     - R
     - DONATION_ORDER
   * - ``DONATION``
     - :ref:`DPR_O48_DONATION <hl7-v2_8-DPR_O48_DONATION>`
     - O
     - DONATION

.. _hl7-v2_8-DRC_O47:

DRC_O47: Donor Request to Collect Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.14

.. py:class:: hl7types.hl7.v2_8.messages.DRC_O47.DRC_O47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DRC_O47_DONOR <hl7-v2_8-DRC_O47_DONOR>`
     - O
     - DONOR
   * - ``DONATION_ORDER``
     - list[:ref:`DRC_O47_DONATION_ORDER <hl7-v2_8-DRC_O47_DONATION_ORDER>`]
     - R
     - DONATION_ORDER

.. _hl7-v2_8-DRG_O43:

DRG_O43: General Order Message with Document Payload Acknowledgement Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.10

.. py:class:: hl7types.hl7.v2_8.messages.DRG_O43.DRG_O43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DONOR``
     - :ref:`DRG_O43_DONOR <hl7-v2_8-DRG_O43_DONOR>`
     - O
     - DONOR

.. _hl7-v2_8-EAC_U07:

EAC_U07: Automated equipment command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.7

.. py:class:: hl7types.hl7.v2_8.messages.EAC_U07.EAC_U07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``COMMAND``
     - list[:ref:`EAC_U07_COMMAND <hl7-v2_8-EAC_U07_COMMAND>`]
     - R
     - COMMAND

.. _hl7-v2_8-EAN_U09:

EAN_U09: Automated equipment notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.9

.. py:class:: hl7types.hl7.v2_8.messages.EAN_U09.EAN_U09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``NOTIFICATION``
     - list[:ref:`EAN_U09_NOTIFICATION <hl7-v2_8-EAN_U09_NOTIFICATION>`]
     - R
     - NOTIFICATION

.. _hl7-v2_8-EAR_U08:

EAR_U08: Automated equipment response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.8

.. py:class:: hl7types.hl7.v2_8.messages.EAR_U08.EAR_U08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``COMMAND_RESPONSE``
     - list[:ref:`EAR_U08_COMMAND_RESPONSE <hl7-v2_8-EAR_U08_COMMAND_RESPONSE>`]
     - R
     - COMMAND_RESPONSE

.. _hl7-v2_8-EHC_E01:

EHC_E01: Submit HealthCare Services Invoice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E01.EHC_E01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``INVOICE_INFORMATION_SUBMIT``
     - :ref:`EHC_E01_INVOICE_INFORMATION_SUBMIT <hl7-v2_8-EHC_E01_INVOICE_INFORMATION_SUBMIT>`
     - R
     - INVOICE_INFORMATION_SUBMIT

.. _hl7-v2_8-EHC_E02:

EHC_E02: Cancel HealthCare Services Invoice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E02.EHC_E02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``INVOICE_INFORMATION_CANCEL``
     - :ref:`EHC_E02_INVOICE_INFORMATION_CANCEL <hl7-v2_8-EHC_E02_INVOICE_INFORMATION_CANCEL>`
     - R
     - INVOICE_INFORMATION_CANCEL

.. _hl7-v2_8-EHC_E04:

EHC_E04: Re-Assess HealthCare Services Invoice Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E04.EHC_E04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``REASSESSMENT_REQUEST_INFO``
     - :ref:`EHC_E04_REASSESSMENT_REQUEST_INFO <hl7-v2_8-EHC_E04_REASSESSMENT_REQUEST_INFO>`
     - R
     - REASSESSMENT_REQUEST_INFO

.. _hl7-v2_8-EHC_E10:

EHC_E10: Edit/Adjudication Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E10.EHC_E10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``INVOICE_PROCESSING_RESULTS_INFO``
     - list[:ref:`EHC_E10_INVOICE_PROCESSING_RESULTS_INFO <hl7-v2_8-EHC_E10_INVOICE_PROCESSING_RESULTS_INFO>`]
     - R
     - INVOICE_PROCESSING_RESULTS_INFO

.. _hl7-v2_8-EHC_E12:

EHC_E12: Request Additional Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E12.EHC_E12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``RFI``
     - :ref:`RFI <hl7-v2_8-RFI>`
     - R
     - RFI
   * - ``CTD``
     - list[:ref:`CTD <hl7-v2_8-CTD>`]
     - O
     - CTD
   * - ``IVC``
     - :ref:`IVC <hl7-v2_8-IVC>`
     - R
     - IVC
   * - ``PSS``
     - :ref:`PSS <hl7-v2_8-PSS>`
     - R
     - PSS
   * - ``PSG``
     - :ref:`PSG <hl7-v2_8-PSG>`
     - R
     - PSG
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - O
     - PID
   * - ``PSL``
     - list[:ref:`PSL <hl7-v2_8-PSL>`]
     - O
     - PSL
   * - ``REQUEST``
     - list[:ref:`EHC_E12_REQUEST <hl7-v2_8-EHC_E12_REQUEST>`]
     - R
     - REQUEST

.. _hl7-v2_8-EHC_E13:

EHC_E13: Additional Information Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E13.EHC_E13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``RFI``
     - :ref:`RFI <hl7-v2_8-RFI>`
     - R
     - RFI
   * - ``CTD``
     - list[:ref:`CTD <hl7-v2_8-CTD>`]
     - O
     - CTD
   * - ``IVC``
     - :ref:`IVC <hl7-v2_8-IVC>`
     - R
     - IVC
   * - ``PSS``
     - :ref:`PSS <hl7-v2_8-PSS>`
     - R
     - PSS
   * - ``PSG``
     - :ref:`PSG <hl7-v2_8-PSG>`
     - R
     - PSG
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - O
     - PID
   * - ``PSL``
     - :ref:`PSL <hl7-v2_8-PSL>`
     - O
     - PSL
   * - ``REQUEST``
     - list[:ref:`EHC_E13_REQUEST <hl7-v2_8-EHC_E13_REQUEST>`]
     - R
     - REQUEST

.. _hl7-v2_8-EHC_E15:

EHC_E15: Payment/Remittance Advice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E15.EHC_E15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``PAYMENT_REMITTANCE_HEADER_INFO``
     - :ref:`EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO <hl7-v2_8-EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO>`
     - R
     - PAYMENT_REMITTANCE_HEADER_INFO
   * - ``PAYMENT_REMITTANCE_DETAIL_INFO``
     - list[:ref:`EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO <hl7-v2_8-EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO>`]
     - O
     - PAYMENT_REMITTANCE_DETAIL_INFO
   * - ``ADJUSTMENT_PAYEE``
     - list[:ref:`EHC_E15_ADJUSTMENT_PAYEE <hl7-v2_8-EHC_E15_ADJUSTMENT_PAYEE>`]
     - O
     - ADJUSTMENT_PAYEE

.. _hl7-v2_8-EHC_E20:

EHC_E20: Submit Authorization Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E20.EHC_E20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``AUTHORIZATION_REQUEST``
     - :ref:`EHC_E20_AUTHORIZATION_REQUEST <hl7-v2_8-EHC_E20_AUTHORIZATION_REQUEST>`
     - R
     - AUTHORIZATION_REQUEST

.. _hl7-v2_8-EHC_E21:

EHC_E21: Cancel Authorization Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E21.EHC_E21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``AUTHORIZATION_REQUEST``
     - :ref:`EHC_E21_AUTHORIZATION_REQUEST <hl7-v2_8-EHC_E21_AUTHORIZATION_REQUEST>`
     - R
     - AUTHORIZATION_REQUEST

.. _hl7-v2_8-EHC_E24:

EHC_E24: Authorization Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 16.3.1

.. py:class:: hl7types.hl7.v2_8.messages.EHC_E24.EHC_E24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``AUTHORIZATION_RESPONSE_INFO``
     - :ref:`EHC_E24_AUTHORIZATION_RESPONSE_INFO <hl7-v2_8-EHC_E24_AUTHORIZATION_RESPONSE_INFO>`
     - R
     - AUTHORIZATION_RESPONSE_INFO

.. _hl7-v2_8-ESR_U02:

ESR_U02: Automated equipment status request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.2

.. py:class:: hl7types.hl7.v2_8.messages.ESR_U02.ESR_U02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU

.. _hl7-v2_8-ESU_U01:

ESU_U01: Automated equipment status update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ESU_U01.ESU_U01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``ISD``
     - list[:ref:`ISD <hl7-v2_8-ISD>`]
     - O
     - ISD

.. _hl7-v2_8-INR_U06:

INR_U06: Automated equipment inventory request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.6

.. py:class:: hl7types.hl7.v2_8.messages.INR_U06.INR_U06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``INV``
     - list[:ref:`INV <hl7-v2_8-INV>`]
     - R
     - INV

.. _hl7-v2_8-INU_U05:

INU_U05: INU/ACK  - Automated equipment inventory update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.5

.. py:class:: hl7types.hl7.v2_8.messages.INU_U05.INU_U05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``INV``
     - list[:ref:`INV <hl7-v2_8-INV>`]
     - R
     - INV

.. _hl7-v2_8-LSU_U12:

LSU_U12: Automated equipment log/service update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.12

.. py:class:: hl7types.hl7.v2_8.messages.LSU_U12.LSU_U12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``EQP``
     - list[:ref:`EQP <hl7-v2_8-EQP>`]
     - R
     - EQP

.. _hl7-v2_8-LSU_U13:

LSU_U13: Automated equipment log/service request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.13

.. py:class:: hl7types.hl7.v2_8.messages.LSU_U13.LSU_U13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``EQP``
     - list[:ref:`EQP <hl7-v2_8-EQP>`]
     - R
     - EQP

.. _hl7-v2_8-MDM_T01:

MDM_T01: Original document notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.1

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T01.MDM_T01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8-MDM_T01_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON

.. _hl7-v2_8-MDM_T02:

MDM_T02: Original document notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.1

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T02.MDM_T02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8-MDM_T02_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON
   * - ``OBSERVATION``
     - list[:ref:`MDM_T02_OBSERVATION <hl7-v2_8-MDM_T02_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-MDM_T03:

MDM_T03: Document status change notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.3

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T03.MDM_T03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8-MDM_T01_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON

.. _hl7-v2_8-MDM_T04:

MDM_T04: Document status change notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.4

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T04.MDM_T04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8-MDM_T02_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON
   * - ``OBSERVATION``
     - list[:ref:`MDM_T02_OBSERVATION <hl7-v2_8-MDM_T02_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-MDM_T05:

MDM_T05: Document addendum notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.5

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T05.MDM_T05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8-MDM_T01_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON

.. _hl7-v2_8-MDM_T06:

MDM_T06: Document addendum notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.6

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T06.MDM_T06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8-MDM_T02_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON
   * - ``OBSERVATION``
     - list[:ref:`MDM_T02_OBSERVATION <hl7-v2_8-MDM_T02_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-MDM_T07:

MDM_T07: Document edit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.7

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T07.MDM_T07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8-MDM_T01_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON

.. _hl7-v2_8-MDM_T08:

MDM_T08: Document edit notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.8

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T08.MDM_T08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8-MDM_T02_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON
   * - ``OBSERVATION``
     - list[:ref:`MDM_T02_OBSERVATION <hl7-v2_8-MDM_T02_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-MDM_T09:

MDM_T09: Document replacement notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.9

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T09.MDM_T09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8-MDM_T01_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON

.. _hl7-v2_8-MDM_T10:

MDM_T10: Document replacement notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.10

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T10.MDM_T10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8-MDM_T02_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON
   * - ``OBSERVATION``
     - list[:ref:`MDM_T02_OBSERVATION <hl7-v2_8-MDM_T02_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-MDM_T11:

MDM_T11: Document cancel notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.6.11

.. py:class:: hl7types.hl7.v2_8.messages.MDM_T11.MDM_T11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``COMMON_ORDER``
     - list[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8-MDM_T01_COMMON_ORDER>`]
     - O
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8-TXA>`
     - R
     - TXA
   * - ``CON``
     - list[:ref:`CON <hl7-v2_8-CON>`]
     - O
     - CON

.. _hl7-v2_8-MFK_M01:

MFK_M01: HL7 v2 MFK_M01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_8-MFA>`]
     - O
     - MFA

.. _hl7-v2_8-MFN_M02:

MFN_M02: Master file - staff practitioner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_STAFF``
     - list[:ref:`MFN_M02_MF_STAFF <hl7-v2_8-MFN_M02_MF_STAFF>`]
     - R
     - MF_STAFF

.. _hl7-v2_8-MFN_M04:

MFN_M04: Master files charge description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M04.MFN_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_CDM``
     - list[:ref:`MFN_M04_MF_CDM <hl7-v2_8-MFN_M04_MF_CDM>`]
     - R
     - MF_CDM

.. _hl7-v2_8-MFN_M05:

MFN_M05: Patient location master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M05.MFN_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_LOCATION``
     - list[:ref:`MFN_M05_MF_LOCATION <hl7-v2_8-MFN_M05_MF_LOCATION>`]
     - R
     - MF_LOCATION

.. _hl7-v2_8-MFN_M06:

MFN_M06: Clinical study with phases and schedules master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M06.MFN_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_CLIN_STUDY``
     - list[:ref:`MFN_M06_MF_CLIN_STUDY <hl7-v2_8-MFN_M06_MF_CLIN_STUDY>`]
     - R
     - MF_CLIN_STUDY

.. _hl7-v2_8-MFN_M07:

MFN_M07: Clinical study without phases but with schedules master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M07.MFN_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_CLIN_STUDY_SCHED``
     - list[:ref:`MFN_M07_MF_CLIN_STUDY_SCHED <hl7-v2_8-MFN_M07_MF_CLIN_STUDY_SCHED>`]
     - R
     - MF_CLIN_STUDY_SCHED

.. _hl7-v2_8-MFN_M08:

MFN_M08: Test/observation (numeric) master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M08.MFN_M08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_TEST_NUMERIC``
     - list[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_8-MFN_M08_MF_TEST_NUMERIC>`]
     - R
     - MF_TEST_NUMERIC

.. _hl7-v2_8-MFN_M09:

MFN_M09: Test/observation (categorical) master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M09.MFN_M09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_TEST_CATEGORICAL``
     - list[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_8-MFN_M09_MF_TEST_CATEGORICAL>`]
     - R
     - MF_TEST_CATEGORICAL

.. _hl7-v2_8-MFN_M10:

MFN_M10: Test /observation batteries master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M10.MFN_M10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_TEST_BATTERIES``
     - list[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_8-MFN_M10_MF_TEST_BATTERIES>`]
     - R
     - MF_TEST_BATTERIES

.. _hl7-v2_8-MFN_M11:

MFN_M11: Test/calculated observations master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M11.MFN_M11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_TEST_CALCULATED``
     - list[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_8-MFN_M11_MF_TEST_CALCULATED>`]
     - R
     - MF_TEST_CALCULATED

.. _hl7-v2_8-MFN_M12:

MFN_M12: Master file notification message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M12.MFN_M12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_OBS_ATTRIBUTES``
     - list[:ref:`MFN_M12_MF_OBS_ATTRIBUTES <hl7-v2_8-MFN_M12_MF_OBS_ATTRIBUTES>`]
     - R
     - MF_OBS_ATTRIBUTES

.. _hl7-v2_8-MFN_M13:

MFN_M13: Master file notification - general
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M13.MFN_M13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MFE``
     - list[:ref:`MFE <hl7-v2_8-MFE>`]
     - R
     - MFE

.. _hl7-v2_8-MFN_M14:

MFN_M14: Master file notification - site defined
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.4.3

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M14.MFN_M14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_SITE_DEFINED``
     - list[MFN_ZnnMF_SITE_DEFINED]
     - R
     - MF_SITE_DEFINED

.. _hl7-v2_8-MFN_M15:

MFN_M15: Inventory item master file notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M15.MFN_M15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_INV_ITEM``
     - list[:ref:`MFN_M15_MF_INV_ITEM <hl7-v2_8-MFN_M15_MF_INV_ITEM>`]
     - R
     - MF_INV_ITEM

.. _hl7-v2_8-MFN_M16:

MFN_M16: Master File Notification Inventory Item Enhanced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M16.MFN_M16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MATERIAL_ITEM_RECORD``
     - list[:ref:`MFN_M16_MATERIAL_ITEM_RECORD <hl7-v2_8-MFN_M16_MATERIAL_ITEM_RECORD>`]
     - R
     - MATERIAL_ITEM_RECORD

.. _hl7-v2_8-MFN_M17:

MFN_M17: DRG Master File Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_M17.MFN_M17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_DRG``
     - list[:ref:`MFN_M17_MF_DRG <hl7-v2_8-MFN_M17_MF_DRG>`]
     - R
     - MF_DRG

.. _hl7-v2_8-MFN_Znn:

MFN_Znn: Master files notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.10.1

.. py:class:: hl7types.hl7.v2_8.messages.MFN_Znn.MFN_Znn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8-MFI>`
     - R
     - MFI
   * - ``MF_SITE_DEFINED``
     - list[MFN_ZnnMF_SITE_DEFINED]
     - R
     - MF_SITE_DEFINED

.. _hl7-v2_8-NMD_N02:

NMD_N02: Application management data message (unsolicited)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14.3.2

.. py:class:: hl7types.hl7.v2_8.messages.NMD_N02.NMD_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     - list[:ref:`NMD_N02_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_8-NMD_N02_CLOCK_AND_STATS_WITH_NOTES>`]
     - R
     - CLOCK_AND_STATS_WITH_NOTES

.. _hl7-v2_8-OMB_O27:

OMB_O27: OMB - Blood product order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.1

.. py:class:: hl7types.hl7.v2_8.messages.OMB_O27.OMB_O27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMB_O27_PATIENT <hl7-v2_8-OMB_O27_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMB_O27_ORDER <hl7-v2_8-OMB_O27_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OMD_O03:

OMD_O03: OMD - Diet order
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.7.1

.. py:class:: hl7types.hl7.v2_8.messages.OMD_O03.OMD_O03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMD_O03_PATIENT <hl7-v2_8-OMD_O03_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER_DIET``
     - list[:ref:`OMD_O03_ORDER_DIET <hl7-v2_8-OMD_O03_ORDER_DIET>`]
     - R
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - list[:ref:`OMD_O03_ORDER_TRAY <hl7-v2_8-OMD_O03_ORDER_TRAY>`]
     - O
     - ORDER_TRAY

.. _hl7-v2_8-OMG_O19:

OMG_O19: OMG - General clinical order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.4

.. py:class:: hl7types.hl7.v2_8.messages.OMG_O19.OMG_O19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMG_O19_PATIENT <hl7-v2_8-OMG_O19_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMG_O19_ORDER <hl7-v2_8-OMG_O19_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OMI_O23:

OMI_O23: OMI - Imaging order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.14

.. py:class:: hl7types.hl7.v2_8.messages.OMI_O23.OMI_O23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMI_O23_PATIENT <hl7-v2_8-OMI_O23_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMI_O23_ORDER <hl7-v2_8-OMI_O23_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OML_O21:

OML_O21: OML - Laboratory order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.10

.. py:class:: hl7types.hl7.v2_8.messages.OML_O21.OML_O21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OML_O21_PATIENT <hl7-v2_8-OML_O21_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OML_O21_ORDER <hl7-v2_8-OML_O21_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OML_O33:

OML_O33: OML - Laboratory order for multiple orders related to a single specimen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.10

.. py:class:: hl7types.hl7.v2_8.messages.OML_O33.OML_O33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OML_O33_PATIENT <hl7-v2_8-OML_O33_PATIENT>`
     - O
     - PATIENT
   * - ``SPECIMEN``
     - list[:ref:`OML_O33_SPECIMEN <hl7-v2_8-OML_O33_SPECIMEN>`]
     - R
     - SPECIMEN

.. _hl7-v2_8-OML_O35:

OML_O35: OML - Laboratory order for multiple orders related to a single container of a sp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.10

.. py:class:: hl7types.hl7.v2_8.messages.OML_O35.OML_O35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OML_O35_PATIENT <hl7-v2_8-OML_O35_PATIENT>`
     - O
     - PATIENT
   * - ``SPECIMEN``
     - list[:ref:`OML_O35_SPECIMEN <hl7-v2_8-OML_O35_SPECIMEN>`]
     - R
     - SPECIMEN

.. _hl7-v2_8-OML_O39:

OML_O39: Specimen shipment centric laboratory order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.10

.. py:class:: hl7types.hl7.v2_8.messages.OML_O39.OML_O39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OML_O39_PATIENT <hl7-v2_8-OML_O39_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OML_O39_ORDER <hl7-v2_8-OML_O39_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OMN_O07:

OMN_O07: OMN - Non-stock requisition order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.10.3

.. py:class:: hl7types.hl7.v2_8.messages.OMN_O07.OMN_O07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMN_O07_PATIENT <hl7-v2_8-OMN_O07_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMN_O07_ORDER <hl7-v2_8-OMN_O07_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OMP_O09:

OMP_O09: OMP - Pharmacy/treatment order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.3

.. py:class:: hl7types.hl7.v2_8.messages.OMP_O09.OMP_O09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMP_O09_PATIENT <hl7-v2_8-OMP_O09_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMP_O09_ORDER <hl7-v2_8-OMP_O09_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OMQ_O57:

OMQ_O57: HL7 v2 OMQ_O57 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.OMQ_O57.OMQ_O57
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMQ_O57_PATIENT <hl7-v2_8-OMQ_O57_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMQ_O57_ORDER <hl7-v2_8-OMQ_O57_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OMS_O05:

OMS_O05: OMS - Stock requisition order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.10.1

.. py:class:: hl7types.hl7.v2_8.messages.OMS_O05.OMS_O05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMS_O05_PATIENT <hl7-v2_8-OMS_O05_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMS_O05_ORDER <hl7-v2_8-OMS_O05_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OPL_O37:

OPL_O37: OPL - Population/Location-Based Laboratory Order Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.16

.. py:class:: hl7types.hl7.v2_8.messages.OPL_O37.OPL_O37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - R
     - PRT
   * - ``GUARANTOR``
     - :ref:`OPL_O37_GUARANTOR <hl7-v2_8-OPL_O37_GUARANTOR>`
     - O
     - GUARANTOR
   * - ``ORDER``
     - list[:ref:`OPL_O37_ORDER <hl7-v2_8-OPL_O37_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-OPR_O38:

OPR_O38: OPR - Population/Location-Based Laboratory Order Acknowledgment Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.17

.. py:class:: hl7types.hl7.v2_8.messages.OPR_O38.OPR_O38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`OPR_O38_RESPONSE <hl7-v2_8-OPR_O38_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-OPU_R25:

OPU_R25: OPU - Unsolicited Population/Location-Based Laboratory Observation Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.11

.. py:class:: hl7types.hl7.v2_8.messages.OPU_R25.OPU_R25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - :ref:`NTE <hl7-v2_8-NTE>`
     - O
     - NTE
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_8-PV2>`
     - O
     - PV2
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``PATIENT_VISIT_OBSERVATION``
     - list[:ref:`OPU_R25_PATIENT_VISIT_OBSERVATION <hl7-v2_8-OPU_R25_PATIENT_VISIT_OBSERVATION>`]
     - O
     - PATIENT_VISIT_OBSERVATION
   * - ``ACCESSION_DETAIL``
     - list[:ref:`OPU_R25_ACCESSION_DETAIL <hl7-v2_8-OPU_R25_ACCESSION_DETAIL>`]
     - R
     - ACCESSION_DETAIL

.. _hl7-v2_8-ORA_R33:

ORA_R33: ORA - Observation Report Acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.13

.. py:class:: hl7types.hl7.v2_8.messages.ORA_R33.ORA_R33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``ORC``
     - :ref:`ORC <hl7-v2_8-ORC>`
     - O
     - ORC

.. _hl7-v2_8-ORA_R41:

ORA_R41: Observation Report Alert Acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.13

.. py:class:: hl7types.hl7.v2_8.messages.ORA_R41.ORA_R41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT

.. _hl7-v2_8-ORB_O28:

ORB_O28: ORB - Blood product order acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.13.2

.. py:class:: hl7types.hl7.v2_8.messages.ORB_O28.ORB_O28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORB_O28_RESPONSE <hl7-v2_8-ORB_O28_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORD_O04:

ORD_O04: ORD - Diet order acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.7.2

.. py:class:: hl7types.hl7.v2_8.messages.ORD_O04.ORD_O04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORD_O04_RESPONSE <hl7-v2_8-ORD_O04_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORG_O20:

ORG_O20: General clinical order response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.5

.. py:class:: hl7types.hl7.v2_8.messages.ORG_O20.ORG_O20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORG_O20_RESPONSE <hl7-v2_8-ORG_O20_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORI_O24:

ORI_O24: ORI - Imaging order response message to any OMI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.15

.. py:class:: hl7types.hl7.v2_8.messages.ORI_O24.ORI_O24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORI_O24_RESPONSE <hl7-v2_8-ORI_O24_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORL_O22:

ORL_O22: ORL - General laboratory order response message to any OML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.11

.. py:class:: hl7types.hl7.v2_8.messages.ORL_O22.ORL_O22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORL_O22_RESPONSE <hl7-v2_8-ORL_O22_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORL_O34:

ORL_O34: ORL - Laboratory order response message to a multiple order related to single sp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.11

.. py:class:: hl7types.hl7.v2_8.messages.ORL_O34.ORL_O34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORL_O34_RESPONSE <hl7-v2_8-ORL_O34_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORL_O36:

ORL_O36: ORL - Laboratory order response message to a single container of a specimen OML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.11

.. py:class:: hl7types.hl7.v2_8.messages.ORL_O36.ORL_O36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORL_O36_RESPONSE <hl7-v2_8-ORL_O36_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORL_O40:

ORL_O40: Specimen Shipment Centric Laboratory Order Acknowledgment Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.4.11

.. py:class:: hl7types.hl7.v2_8.messages.ORL_O40.ORL_O40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORL_O40_RESPONSE <hl7-v2_8-ORL_O40_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORN_O08:

ORN_O08: ORN - Non-stock requisition acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.10.4

.. py:class:: hl7types.hl7.v2_8.messages.ORN_O08.ORN_O08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORN_O08_RESPONSE <hl7-v2_8-ORN_O08_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORP_O10:

ORP_O10: ORP - Pharmacy/treatment order acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.4

.. py:class:: hl7types.hl7.v2_8.messages.ORP_O10.ORP_O10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORP_O10_RESPONSE <hl7-v2_8-ORP_O10_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORS_O06:

ORS_O06: ORS - Stock requisition acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.10.2

.. py:class:: hl7types.hl7.v2_8.messages.ORS_O06.ORS_O06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORS_O06_RESPONSE <hl7-v2_8-ORS_O06_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-ORU_R01:

ORU_R01: Unsolicited transmission of an observation message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT_RESULT``
     - list[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_8-ORU_R01_PATIENT_RESULT>`]
     - R
     - PATIENT_RESULT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-ORU_R30:

ORU_R30: ORU - Unsolicited Point-Of-Care Observation Message Without Existing Order - Pla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.1

.. py:class:: hl7types.hl7.v2_8.messages.ORU_R30.ORU_R30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``PATIENT_OBSERVATION``
     - list[:ref:`ORU_R30_PATIENT_OBSERVATION <hl7-v2_8-ORU_R30_PATIENT_OBSERVATION>`]
     - O
     - PATIENT_OBSERVATION
   * - ``VISIT``
     - :ref:`ORU_R30_VISIT <hl7-v2_8-ORU_R30_VISIT>`
     - O
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_8-ORC>`
     - R
     - ORC
   * - ``OBR``
     - :ref:`OBR <hl7-v2_8-OBR>`
     - R
     - OBR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``TIMING_QTY``
     - list[:ref:`ORU_R30_TIMING_QTY <hl7-v2_8-ORU_R30_TIMING_QTY>`]
     - O
     - TIMING_QTY
   * - ``OBSERVATION``
     - list[:ref:`ORU_R30_OBSERVATION <hl7-v2_8-ORU_R30_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-ORU_R31:

ORU_R31: ORU - Unsolicited New Point-Of-Care Observation Message - Search For An Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.5

.. py:class:: hl7types.hl7.v2_8.messages.ORU_R31.ORU_R31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``PATIENT_OBSERVATION``
     - list[:ref:`ORU_R30_PATIENT_OBSERVATION <hl7-v2_8-ORU_R30_PATIENT_OBSERVATION>`]
     - O
     - PATIENT_OBSERVATION
   * - ``VISIT``
     - :ref:`ORU_R30_VISIT <hl7-v2_8-ORU_R30_VISIT>`
     - O
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_8-ORC>`
     - R
     - ORC
   * - ``OBR``
     - :ref:`OBR <hl7-v2_8-OBR>`
     - R
     - OBR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``TIMING_QTY``
     - list[:ref:`ORU_R30_TIMING_QTY <hl7-v2_8-ORU_R30_TIMING_QTY>`]
     - O
     - TIMING_QTY
   * - ``OBSERVATION``
     - list[:ref:`ORU_R30_OBSERVATION <hl7-v2_8-ORU_R30_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-ORU_R32:

ORU_R32: ORU - Unsolicited Pre-Ordered Point-Of-Care Observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.6

.. py:class:: hl7types.hl7.v2_8.messages.ORU_R32.ORU_R32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``PATIENT_OBSERVATION``
     - list[:ref:`ORU_R30_PATIENT_OBSERVATION <hl7-v2_8-ORU_R30_PATIENT_OBSERVATION>`]
     - O
     - PATIENT_OBSERVATION
   * - ``VISIT``
     - :ref:`ORU_R30_VISIT <hl7-v2_8-ORU_R30_VISIT>`
     - O
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_8-ORC>`
     - R
     - ORC
   * - ``OBR``
     - :ref:`OBR <hl7-v2_8-OBR>`
     - R
     - OBR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``TIMING_QTY``
     - list[:ref:`ORU_R30_TIMING_QTY <hl7-v2_8-ORU_R30_TIMING_QTY>`]
     - O
     - TIMING_QTY
   * - ``OBSERVATION``
     - list[:ref:`ORU_R30_OBSERVATION <hl7-v2_8-ORU_R30_OBSERVATION>`]
     - R
     - OBSERVATION

.. _hl7-v2_8-ORU_R40:

ORU_R40: ORU - Unsolicited Report Alarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.12

.. py:class:: hl7types.hl7.v2_8.messages.ORU_R40.ORU_R40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PATIENT_RESULT``
     - list[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_8-ORU_R01_PATIENT_RESULT>`]
     - R
     - PATIENT_RESULT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-ORX_O58:

ORX_O58: HL7 v2 ORX_O58 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.ORX_O58.ORX_O58
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORX_O58_RESPONSE <hl7-v2_8-ORX_O58_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-OSM_R26:

OSM_R26: OSM - Unsolicited Specimen Shipment Manifest Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.18.1

.. py:class:: hl7types.hl7.v2_8.messages.OSM_R26.OSM_R26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``SHIPMENT``
     - list[:ref:`OSM_R26_SHIPMENT <hl7-v2_8-OSM_R26_SHIPMENT>`]
     - R
     - SHIPMENT

.. _hl7-v2_8-OSU_O51:

OSU_O51: HL7 v2 OSU_O51 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.OSU_O51.OSU_O51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - O
     - PID
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``ORDER_STATUS``
     - list[:ref:`OSU_O51_ORDER_STATUS <hl7-v2_8-OSU_O51_ORDER_STATUS>`]
     - R
     - ORDER_STATUS

.. _hl7-v2_8-OUL_R22:

OUL_R22: OUL - Unsolicited Specimen Oriented Observation Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.10

.. py:class:: hl7types.hl7.v2_8.messages.OUL_R22.OUL_R22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - :ref:`NTE <hl7-v2_8-NTE>`
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OUL_R22_PATIENT <hl7-v2_8-OUL_R22_PATIENT>`
     - O
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``SPECIMEN``
     - list[:ref:`OUL_R22_SPECIMEN <hl7-v2_8-OUL_R22_SPECIMEN>`]
     - R
     - SPECIMEN
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-OUL_R23:

OUL_R23: OUL - Unsolicited Specimen Container Oriented Observation Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.10

.. py:class:: hl7types.hl7.v2_8.messages.OUL_R23.OUL_R23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - :ref:`NTE <hl7-v2_8-NTE>`
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OUL_R23_PATIENT <hl7-v2_8-OUL_R23_PATIENT>`
     - O
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``SPECIMEN``
     - list[:ref:`OUL_R23_SPECIMEN <hl7-v2_8-OUL_R23_SPECIMEN>`]
     - R
     - SPECIMEN
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-OUL_R24:

OUL_R24: OUL - Unsolicited Order Oriented Observation Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.3.10

.. py:class:: hl7types.hl7.v2_8.messages.OUL_R24.OUL_R24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - :ref:`NTE <hl7-v2_8-NTE>`
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OUL_R24_PATIENT <hl7-v2_8-OUL_R24_PATIENT>`
     - O
     - PATIENT
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``ORDER``
     - list[:ref:`OUL_R24_ORDER <hl7-v2_8-OUL_R24_ORDER>`]
     - R
     - ORDER
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-PEX_P07:

PEX_P07: PEX - Unsolicited initial individual product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.1

.. py:class:: hl7types.hl7.v2_8.messages.PEX_P07.PEX_P07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``VISIT``
     - :ref:`PEX_P07_VISIT <hl7-v2_8-PEX_P07_VISIT>`
     - O
     - VISIT
   * - ``EXPERIENCE``
     - list[:ref:`PEX_P07_EXPERIENCE <hl7-v2_8-PEX_P07_EXPERIENCE>`]
     - R
     - EXPERIENCE

.. _hl7-v2_8-PEX_P08:

PEX_P08: PEX - Unsolicited update individual product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.11.1

.. py:class:: hl7types.hl7.v2_8.messages.PEX_P08.PEX_P08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``VISIT``
     - :ref:`PEX_P07_VISIT <hl7-v2_8-PEX_P07_VISIT>`
     - O
     - VISIT
   * - ``EXPERIENCE``
     - list[:ref:`PEX_P07_EXPERIENCE <hl7-v2_8-PEX_P07_EXPERIENCE>`]
     - R
     - EXPERIENCE

.. _hl7-v2_8-PGL_PC6:

PGL_PC6: PGL - PC/ goal add
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PGL_PC6.PGL_PC6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_8-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_8-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_8-PGL_PC7:

PGL_PC7: PGL - PC/ goal update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PGL_PC7.PGL_PC7
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_8-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_8-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_8-PGL_PC8:

PGL_PC8: PGL - PC/ goal delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PGL_PC8.PGL_PC8
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_8-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_8-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_8-PMU_B01:

PMU_B01: Add personnel record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B01.PMU_B01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_8-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - list[:ref:`ORG <hl7-v2_8-ORG>`]
     - O
     - ORG
   * - ``AFF``
     - list[:ref:`AFF <hl7-v2_8-AFF>`]
     - O
     - AFF
   * - ``LAN``
     - list[:ref:`LAN <hl7-v2_8-LAN>`]
     - O
     - LAN
   * - ``EDU``
     - list[:ref:`EDU <hl7-v2_8-EDU>`]
     - O
     - EDU
   * - ``CER``
     - list[:ref:`CER <hl7-v2_8-CER>`]
     - O
     - CER
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL

.. _hl7-v2_8-PMU_B02:

PMU_B02: Update personnel record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.2

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B02.PMU_B02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_8-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - list[:ref:`ORG <hl7-v2_8-ORG>`]
     - O
     - ORG
   * - ``AFF``
     - list[:ref:`AFF <hl7-v2_8-AFF>`]
     - O
     - AFF
   * - ``LAN``
     - list[:ref:`LAN <hl7-v2_8-LAN>`]
     - O
     - LAN
   * - ``EDU``
     - list[:ref:`EDU <hl7-v2_8-EDU>`]
     - O
     - EDU
   * - ``CER``
     - list[:ref:`CER <hl7-v2_8-CER>`]
     - O
     - CER
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``PRT``
     - list[:ref:`PRT <hl7-v2_8-PRT>`]
     - O
     - PRT
   * - ``ROL``
     - list[:ref:`ROL <hl7-v2_8-ROL>`]
     - O
     - ROL

.. _hl7-v2_8-PMU_B03:

PMU_B03: Delete personnel re cord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B03.PMU_B03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF

.. _hl7-v2_8-PMU_B04:

PMU_B04: Active practicing person
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B04.PMU_B04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_8-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - list[:ref:`ORG <hl7-v2_8-ORG>`]
     - O
     - ORG

.. _hl7-v2_8-PMU_B05:

PMU_B05: Deactivate practicing person
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.5

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B05.PMU_B05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_8-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - list[:ref:`ORG <hl7-v2_8-ORG>`]
     - O
     - ORG

.. _hl7-v2_8-PMU_B06:

PMU_B06: Terminate practicing person
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.6

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B06.PMU_B06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF
   * - ``PRA``
     - list[:ref:`PRA <hl7-v2_8-PRA>`]
     - O
     - PRA
   * - ``ORG``
     - list[:ref:`ORG <hl7-v2_8-ORG>`]
     - O
     - ORG

.. _hl7-v2_8-PMU_B07:

PMU_B07: Grant Certificate/Permission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B07.PMU_B07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF
   * - ``PRA``
     - :ref:`PRA <hl7-v2_8-PRA>`
     - O
     - PRA
   * - ``CERTIFICATE``
     - list[:ref:`PMU_B07_CERTIFICATE <hl7-v2_8-PMU_B07_CERTIFICATE>`]
     - O
     - CERTIFICATE

.. _hl7-v2_8-PMU_B08:

PMU_B08: Revoke Certificate/Permission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.1

.. py:class:: hl7types.hl7.v2_8.messages.PMU_B08.PMU_B08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8-EVN>`
     - R
     - EVN
   * - ``STF``
     - :ref:`STF <hl7-v2_8-STF>`
     - R
     - STF
   * - ``PRA``
     - :ref:`PRA <hl7-v2_8-PRA>`
     - O
     - PRA
   * - ``CER``
     - list[:ref:`CER <hl7-v2_8-CER>`]
     - O
     - CER

.. _hl7-v2_8-PPG_PCG:

PPG_PCG: PPG - PC/ pathway (goal-oriented) add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.4

.. py:class:: hl7types.hl7.v2_8.messages.PPG_PCG.PPG_PCG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_8-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_8-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_8-PPG_PCH:

PPG_PCH: PPG - PC/ pathway (goal-oriented) update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.4

.. py:class:: hl7types.hl7.v2_8.messages.PPG_PCH.PPG_PCH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_8-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_8-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_8-PPG_PCJ:

PPG_PCJ: PPG - PC/ pathway (goal-oriented) delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.4

.. py:class:: hl7types.hl7.v2_8.messages.PPG_PCJ.PPG_PCJ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_8-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_8-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_8-PPP_PCB:

PPP_PCB: PPP - PC/ pathway (problem-oriented) add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.3

.. py:class:: hl7types.hl7.v2_8.messages.PPP_PCB.PPP_PCB
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_8-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_8-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_8-PPP_PCC:

PPP_PCC: PPP - PC/ pathway (problem-oriented) update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.3

.. py:class:: hl7types.hl7.v2_8.messages.PPP_PCC.PPP_PCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_8-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_8-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_8-PPP_PCD:

PPP_PCD: PPP - PC/ pathway (problem-oriented) delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.3

.. py:class:: hl7types.hl7.v2_8.messages.PPP_PCD.PPP_PCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_8-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_8-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_8-PPR_PC1:

PPR_PC1: PPR - PC/ problem add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.2

.. py:class:: hl7types.hl7.v2_8.messages.PPR_PC1.PPR_PC1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_8-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_8-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_8-PPR_PC2:

PPR_PC2: PPR - PC/ problem update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.2

.. py:class:: hl7types.hl7.v2_8.messages.PPR_PC2.PPR_PC2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_8-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_8-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_8-PPR_PC3:

PPR_PC3: PPR - PC/ problem delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.3.2

.. py:class:: hl7types.hl7.v2_8.messages.PPR_PC3.PPR_PC3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_8-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_8-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_8-QBP_E03:

QBP_E03: HealthCare Services Invoice Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_E03.QBP_E03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``QUERY_INFORMATION``
     - :ref:`QBP_E03_QUERY_INFORMATION <hl7-v2_8-QBP_E03_QUERY_INFORMATION>`
     - R
     - QUERY_INFORMATION

.. _hl7-v2_8-QBP_E22:

QBP_E22: Authorization Request Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_E22.QBP_E22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``QUERY``
     - :ref:`QBP_E22_QUERY <hl7-v2_8-QBP_E22_QUERY>`
     - R
     - QUERY

.. _hl7-v2_8-QBP_O33:

QBP_O33: OML - Laboratory order for multiple orders related to a single specimen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_O33.QBP_O33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP

.. _hl7-v2_8-QBP_O34:

QBP_O34: ORL - Laboratory order response message to a multiple order related to single sp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_O34.QBP_O34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP

.. _hl7-v2_8-QBP_Q11:

QBP_Q11: QBP - Query by parameter requesting an RSP segment pattern response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q11.QBP_Q11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q11_QBP <hl7-v2_8-QBP_Q11_QBP>`
     - O
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q13:

QBP_Q13: HL7 v2 QBP_Q13 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q13.QBP_Q13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - O
     - PID
   * - ``RDF``
     - :ref:`RDF <hl7-v2_8-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q15:

QBP_Q15: QBP - Query by parameter requesting an RDY display response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q15.QBP_Q15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q21:

QBP_Q21: QBP - Get person demographics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q21.QBP_Q21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q22:

QBP_Q22: QBP - Find candidates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.57

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q22.QBP_Q22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q23:

QBP_Q23: QBP - Get corresponding identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.58

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q23.QBP_Q23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q24:

QBP_Q24: QBP - Allocate identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.59

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q24.QBP_Q24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q25:

QBP_Q25: QBP - Personnel Information by Segment Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q25.QBP_Q25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q31:

QBP_Q31: QBP Query Dispense history
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.20

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q31.QBP_Q31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q11_QBP <hl7-v2_8-QBP_Q11_QBP>`
     - O
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q32:

QBP_Q32: Find Candidates including Visit Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.63

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q32.QBP_Q32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Q33:

QBP_Q33: Get Donor Record Candidates Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.6

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q33.QBP_Q33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP

.. _hl7-v2_8-QBP_Q34:

QBP_Q34: Get Donor Record Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.8

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Q34.QBP_Q34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP

.. _hl7-v2_8-QBP_Qnn:

QBP_Qnn: HL7 v2 QBP_Qnn message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Qnn.QBP_Qnn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RDF``
     - :ref:`RDF <hl7-v2_8-RDF>`
     - O
     - RDF
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Z73:

QBP_Z73: Information about Phone Calls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Z73.QBP_Z73
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP

.. _hl7-v2_8-QBP_Z87:

QBP_Z87: Dispense Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.2.1.1

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Z87.QBP_Z87
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q11_QBP <hl7-v2_8-QBP_Q11_QBP>`
     - O
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QBP_Z89:

QBP_Z89: Lab Results History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.2.4

.. py:class:: hl7types.hl7.v2_8.messages.QBP_Z89.QBP_Z89
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QBP_Q11_QBP <hl7-v2_8-QBP_Q11_QBP>`
     - O
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QCN_J01:

QCN_J01: Cancel query/acknowledge message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.4.6

.. py:class:: hl7types.hl7.v2_8.messages.QCN_J01.QCN_J01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QID``
     - :ref:`QID <hl7-v2_8-QID>`
     - R
     - QID

.. _hl7-v2_8-QCN_J02:

QCN_J02: Cancel subscription/acknowledge message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.4.7

.. py:class:: hl7types.hl7.v2_8.messages.QCN_J02.QCN_J02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QID``
     - :ref:`QID <hl7-v2_8-QID>`
     - R
     - QID

.. _hl7-v2_8-QSB_Q16:

QSB_Q16: QSB - Create subscription
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.4.4

.. py:class:: hl7types.hl7.v2_8.messages.QSB_Q16.QSB_Q16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QSB_Z83:

QSB_Z83: ORU Subscription
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.7.3.1

.. py:class:: hl7types.hl7.v2_8.messages.QSB_Z83.QSB_Z83
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-QVR_Q17:

QVR_Q17: QVR - Query for previous events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.4.5

.. py:class:: hl7types.hl7.v2_8.messages.QVR_Q17.QVR_Q17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QBP``
     - :ref:`QVR_Q17_QBP <hl7-v2_8-QVR_Q17_QBP>`
     - O
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RAS_O17:

RAS_O17: RAS - Pharmacy/treatment administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.11

.. py:class:: hl7types.hl7.v2_8.messages.RAS_O17.RAS_O17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RAS_O17_PATIENT <hl7-v2_8-RAS_O17_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RAS_O17_ORDER <hl7-v2_8-RAS_O17_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-RDE_O11:

RDE_O11: RDE - Pharmacy/treatment encoded order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.13

.. py:class:: hl7types.hl7.v2_8.messages.RDE_O11.RDE_O11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDE_O11_PATIENT <hl7-v2_8-RDE_O11_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDE_O11_ORDER <hl7-v2_8-RDE_O11_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-RDE_O25:

RDE_O25: RDE - Pharmacy/treatment refill authorization request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.13

.. py:class:: hl7types.hl7.v2_8.messages.RDE_O25.RDE_O25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDE_O11_PATIENT <hl7-v2_8-RDE_O11_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDE_O11_ORDER <hl7-v2_8-RDE_O11_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-RDR_RDR:

RDR_RDR: Pharmacy/treatment Dispense Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.1.1

.. py:class:: hl7types.hl7.v2_8.messages.RDR_RDR.RDR_RDR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - :ref:`SFT <hl7-v2_8-SFT>`
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``DEFINITION``
     - list[:ref:`RDR_RDR_DEFINITION <hl7-v2_8-RDR_RDR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RDS_O13:

RDS_O13: RDS - Pharmacy/treatment dispense
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.7

.. py:class:: hl7types.hl7.v2_8.messages.RDS_O13.RDS_O13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDS_O13_PATIENT <hl7-v2_8-RDS_O13_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDS_O13_ORDER <hl7-v2_8-RDS_O13_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-RDY_K15:

RDY_K15: RDY - Display response in response to QBP^Q15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.3.2.5

.. py:class:: hl7types.hl7.v2_8.messages.RDY_K15.RDY_K15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_8-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RDY_Z80:

RDY_Z80: Dispense Information (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.3.2.5

.. py:class:: hl7types.hl7.v2_8.messages.RDY_Z80.RDY_Z80
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_8-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RDY_Z98:

RDY_Z98: Dispense History (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.5.1

.. py:class:: hl7types.hl7.v2_8.messages.RDY_Z98.RDY_Z98
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_8-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-REF_I12:

REF_I12: Patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.1

.. py:class:: hl7types.hl7.v2_8.messages.REF_I12.REF_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT1``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT1 <hl7-v2_8-REF_I12_AUTHORIZATION_CONTACT1>`
     - O
     - AUTHORIZATION_CONTACT1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_8-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_8-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_8-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_8-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-REF_I13:

REF_I13: Modify patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.1

.. py:class:: hl7types.hl7.v2_8.messages.REF_I13.REF_I13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT1``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT1 <hl7-v2_8-REF_I12_AUTHORIZATION_CONTACT1>`
     - O
     - AUTHORIZATION_CONTACT1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_8-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_8-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_8-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_8-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-REF_I14:

REF_I14: Cancel patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.1

.. py:class:: hl7types.hl7.v2_8.messages.REF_I14.REF_I14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT1``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT1 <hl7-v2_8-REF_I12_AUTHORIZATION_CONTACT1>`
     - O
     - AUTHORIZATION_CONTACT1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_8-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_8-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_8-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_8-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-REF_I15:

REF_I15: Request patient referral status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.1

.. py:class:: hl7types.hl7.v2_8.messages.REF_I15.REF_I15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT1``
     - :ref:`REF_I12_AUTHORIZATION_CONTACT1 <hl7-v2_8-REF_I12_AUTHORIZATION_CONTACT1>`
     - O
     - AUTHORIZATION_CONTACT1
   * - ``PROVIDER_CONTACT``
     - list[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8-REF_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_8-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_8-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`REF_I12_OBSERVATION <hl7-v2_8-REF_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`REF_I12_PATIENT_VISIT <hl7-v2_8-REF_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RGV_O15:

RGV_O15: RGV - Pharmacy/treatment give
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.9

.. py:class:: hl7types.hl7.v2_8.messages.RGV_O15.RGV_O15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RGV_O15_PATIENT <hl7-v2_8-RGV_O15_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RGV_O15_ORDER <hl7-v2_8-RGV_O15_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_8-RPA_I08:

RPA_I08: Request for treatment authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.1

.. py:class:: hl7types.hl7.v2_8.messages.RPA_I08.RPA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RPA_I08_AUTHORIZATION <hl7-v2_8-RPA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RPA_I08_PROVIDER <hl7-v2_8-RPA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`RPA_I08_INSURANCE <hl7-v2_8-RPA_I08_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RPA_I08_PROCEDURE <hl7-v2_8-RPA_I08_PROCEDURE>`]
     - R
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RPA_I08_OBSERVATION <hl7-v2_8-RPA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RPA_I08_VISIT <hl7-v2_8-RPA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RPI_I01:

RPI_I01: Request for insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.1

.. py:class:: hl7types.hl7.v2_8.messages.RPI_I01.RPI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPI_I01_PROVIDER <hl7-v2_8-RPI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_8-RPI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RPI_I04:

RPI_I04: Request for patient demographic data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.1

.. py:class:: hl7types.hl7.v2_8.messages.RPI_I04.RPI_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPI_I04_PROVIDER <hl7-v2_8-RPI_I04_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RPI_I04_GUARANTOR_INSURANCE <hl7-v2_8-RPI_I04_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RPL_I02:

RPL_I02: Request/receipt of patient selection display list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.2

.. py:class:: hl7types.hl7.v2_8.messages.RPL_I02.RPL_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPL_I02_PROVIDER <hl7-v2_8-RPL_I02_PROVIDER>`]
     - R
     - PROVIDER
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_8-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RPR_I03:

RPR_I03: Request/receipt of patient selection list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.3

.. py:class:: hl7types.hl7.v2_8.messages.RPR_I03.RPR_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPR_I03_PROVIDER <hl7-v2_8-RPR_I03_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - list[:ref:`PID <hl7-v2_8-PID>`]
     - O
     - PID
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQA_I08:

RQA_I08: Request for treatment authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.1

.. py:class:: hl7types.hl7.v2_8.messages.RQA_I08.RQA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_8-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_8-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_8-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_8-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_8-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQA_I09:

RQA_I09: Request for modification to an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.1

.. py:class:: hl7types.hl7.v2_8.messages.RQA_I09.RQA_I09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_8-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_8-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_8-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_8-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_8-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQA_I10:

RQA_I10: Request for resubmission of an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.1

.. py:class:: hl7types.hl7.v2_8.messages.RQA_I10.RQA_I10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_8-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_8-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_8-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_8-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_8-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQA_I11:

RQA_I11: Request for cancellation of an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.1

.. py:class:: hl7types.hl7.v2_8.messages.RQA_I11.RQA_I11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_8-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_8-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_8-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_8-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_8-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQI_I01:

RQI_I01: Request for insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.1

.. py:class:: hl7types.hl7.v2_8.messages.RQI_I01.RQI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_8-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQI_I02:

RQI_I02: Request/receipt of patient selection display list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.2

.. py:class:: hl7types.hl7.v2_8.messages.RQI_I02.RQI_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_8-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQI_I03:

RQI_I03: Request/receipt of patient selection list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.3

.. py:class:: hl7types.hl7.v2_8.messages.RQI_I03.RQI_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_8-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQI_I07:

RQI_I07: Unsolicited insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RQI_I07.RQI_I07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_8-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RQP_I04:

RQP_I04: Request for patient demographic data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.4

.. py:class:: hl7types.hl7.v2_8.messages.RQP_I04.RQP_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PROVIDER``
     - list[:ref:`RQP_I04_PROVIDER <hl7-v2_8-RQP_I04_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RRA_O18:

RRA_O18: RRA - Pharmacy/treatment administration acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.12

.. py:class:: hl7types.hl7.v2_8.messages.RRA_O18.RRA_O18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRA_O18_RESPONSE <hl7-v2_8-RRA_O18_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-RRD_O14:

RRD_O14: RRD - Pharmacy/treatment dispense acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.8

.. py:class:: hl7types.hl7.v2_8.messages.RRD_O14.RRD_O14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRD_O14_RESPONSE <hl7-v2_8-RRD_O14_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-RRE_O12:

RRE_O12: RRE - Pharmacy/treatment encoded order acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.14

.. py:class:: hl7types.hl7.v2_8.messages.RRE_O12.RRE_O12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRE_O12_RESPONSE <hl7-v2_8-RRE_O12_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-RRE_O26:

RRE_O26: RRE - Pharmacy/Treatment Refill Authorization Acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.14

.. py:class:: hl7types.hl7.v2_8.messages.RRE_O26.RRE_O26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRE_O12_RESPONSE <hl7-v2_8-RRE_O12_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-RRG_O16:

RRG_O16: RRG - Pharmacy/treatment give acknowledgment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.10

.. py:class:: hl7types.hl7.v2_8.messages.RRG_O16.RRG_O16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRG_O16_RESPONSE <hl7-v2_8-RRG_O16_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_8-RRI_I12:

RRI_I12: Patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.5.1

.. py:class:: hl7types.hl7.v2_8.messages.RRI_I12.RRI_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - O
     - MSA
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION_CONTACT2``
     - :ref:`RRI_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8-RRI_I12_AUTHORIZATION_CONTACT2>`
     - O
     - AUTHORIZATION_CONTACT2
   * - ``PROVIDER_CONTACT``
     - list[:ref:`RRI_I12_PROVIDER_CONTACT <hl7-v2_8-RRI_I12_PROVIDER_CONTACT>`]
     - R
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``ACC``
     - :ref:`ACC <hl7-v2_8-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_8-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_8-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_8-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RRI_I12_PROCEDURE <hl7-v2_8-RRI_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RRI_I12_OBSERVATION <hl7-v2_8-RRI_I12_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - :ref:`RRI_I12_PATIENT_VISIT <hl7-v2_8-RRI_I12_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE

.. _hl7-v2_8-RSP_E03:

RSP_E03: HealthCare Services Invoice Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_E03.RSP_E03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``QUERY_ACK_IPR``
     - :ref:`RSP_E03_QUERY_ACK_IPR <hl7-v2_8-RSP_E03_QUERY_ACK_IPR>`
     - R
     - QUERY_ACK_IPR

.. _hl7-v2_8-RSP_E22:

RSP_E22: Authorization Request Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_E22.RSP_E22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - list[:ref:`UAC <hl7-v2_8-UAC>`]
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``QUERY_ACK``
     - :ref:`RSP_E22_QUERY_ACK <hl7-v2_8-RSP_E22_QUERY_ACK>`
     - R
     - QUERY_ACK

.. _hl7-v2_8-RSP_K11:

RSP_K11: RSP - Segment pattern response in response to QBP^Q11
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K11.RSP_K11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``SEGMENT_PATTERN``
     - :ref:`RSP_K11_SEGMENT_PATTERN <hl7-v2_8-RSP_K11_SEGMENT_PATTERN>`
     - O
     - SEGMENT_PATTERN
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K21:

RSP_K21: RSP - Get person demographics response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K21.RSP_K21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - :ref:`RSP_K21_QUERY_RESPONSE <hl7-v2_8-RSP_K21_QUERY_RESPONSE>`
     - O
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K22:

RSP_K22: RSP - Find candidates response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K22.RSP_K22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_K22_QUERY_RESPONSE <hl7-v2_8-RSP_K22_QUERY_RESPONSE>`]
     - O
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K23:

RSP_K23: RSP - Get corresponding identifiers response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K23.RSP_K23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - :ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_8-RSP_K23_QUERY_RESPONSE>`
     - O
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K24:

RSP_K24: RSP - Allocate identifiers response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.3.59

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K24.RSP_K24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - :ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_8-RSP_K23_QUERY_RESPONSE>`
     - O
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K25:

RSP_K25: RSP - Personnel Information by Segment Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K25.RSP_K25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``STAFF``
     - list[:ref:`RSP_K25_STAFF <hl7-v2_8-RSP_K25_STAFF>`]
     - R
     - STAFF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K31:

RSP_K31: RSP -Dispense History Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K31.RSP_K31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``RESPONSE``
     - list[:ref:`RSP_K31_RESPONSE <hl7-v2_8-RSP_K31_RESPONSE>`]
     - R
     - RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K32:

RSP_K32: Find Candidates including Visit Information Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K32.RSP_K32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_K32_QUERY_RESPONSE <hl7-v2_8-RSP_K32_QUERY_RESPONSE>`]
     - O
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_K33:

RSP_K33: Get Donor Record Candidates Response Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K33.RSP_K33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DONOR``
     - :ref:`RSP_O33_DONOR <hl7-v2_8-RSP_O33_DONOR>`
     - O
     - DONOR

.. _hl7-v2_8-RSP_K34:

RSP_K34: Segment Pattern Response Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.16.9

.. py:class:: hl7types.hl7.v2_8.messages.RSP_K34.RSP_K34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DONOR``
     - :ref:`RSP_O34_DONOR <hl7-v2_8-RSP_O34_DONOR>`
     - O
     - DONOR
   * - ``DONATION``
     - :ref:`RSP_O34_DONATION <hl7-v2_8-RSP_O34_DONATION>`
     - O
     - DONATION

.. _hl7-v2_8-RSP_O33:

RSP_O33: OML - Laboratory order for multiple orders related to a single specimen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_O33.RSP_O33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DONOR``
     - :ref:`RSP_O33_DONOR <hl7-v2_8-RSP_O33_DONOR>`
     - O
     - DONOR

.. _hl7-v2_8-RSP_O34:

RSP_O34: ORL - Laboratory order response message to a multiple order related to single sp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_O34.RSP_O34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DONOR``
     - :ref:`RSP_O34_DONOR <hl7-v2_8-RSP_O34_DONOR>`
     - O
     - DONOR
   * - ``DONATION``
     - :ref:`RSP_O34_DONATION <hl7-v2_8-RSP_O34_DONATION>`
     - O
     - DONATION

.. _hl7-v2_8-RSP_Z82:

RSP_Z82: Dispense History (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_Z82.RSP_Z82
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z82_QUERY_RESPONSE <hl7-v2_8-RSP_Z82_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_Z84:

RSP_Z84: Who Am I (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_Z84.RSP_Z84
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RSP_Z84_ROW_DEFINITION <hl7-v2_8-RSP_Z84_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_Z86:

RSP_Z86: Pharmacy Information Comprehensive (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_Z86.RSP_Z86
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z86_QUERY_RESPONSE <hl7-v2_8-RSP_Z86_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RSP_Z88:

RSP_Z88: Dispense Information (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_Z88.RSP_Z88
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z88_QUERY_RESPONSE <hl7-v2_8-RSP_Z88_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - R
     - DSC

.. _hl7-v2_8-RSP_Z90:

RSP_Z90: Lab Results History (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_Z90.RSP_Z90
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8-RCP>`
     - R
     - RCP
   * - ``QUERY_RESPONSE``
     - list[:ref:`RSP_Z90_QUERY_RESPONSE <hl7-v2_8-RSP_Z90_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - R
     - DSC

.. _hl7-v2_8-RSP_Znn:

RSP_Znn: Segment pattern response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15.3.7

.. py:class:: hl7types.hl7.v2_8.messages.RSP_Znn.RSP_Znn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_K13:

RTB_K13: RTB - Tabular response in response to QBP^Q13
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.6.2

.. py:class:: hl7types.hl7.v2_8.messages.RTB_K13.RTB_K13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8-RTB_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_Knn:

RTB_Knn: HL7 v2 RTB_Knn message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8.messages.RTB_Knn.RTB_Knn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_Z74:

RTB_Z74: Information about Phone Calls (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.6.2

.. py:class:: hl7types.hl7.v2_8.messages.RTB_Z74.RTB_Z74
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_Z74_ROW_DEFINITION <hl7-v2_8-RTB_Z74_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_Z76:

RTB_Z76: Tabular Patient List (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.7.2

.. py:class:: hl7types.hl7.v2_8.messages.RTB_Z76.RTB_Z76
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8-RTB_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_Z78:

RTB_Z78: Tabular Patient List (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.7.1

.. py:class:: hl7types.hl7.v2_8.messages.RTB_Z78.RTB_Z78
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8-RTB_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_Z92:

RTB_Z92: Who Am I (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.3.1.1

.. py:class:: hl7types.hl7.v2_8.messages.RTB_Z92.RTB_Z92
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8-RTB_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_Z94:

RTB_Z94: Tabular Dispense History (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.3.2.1

.. py:class:: hl7types.hl7.v2_8.messages.RTB_Z94.RTB_Z94
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8-RTB_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-RTB_Z96:

RTB_Z96: Tabular Dispense History (Response)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.9.4.1.1

.. py:class:: hl7types.hl7.v2_8.messages.RTB_Z96.RTB_Z96
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_8-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8-QAK>`
     - R
     - QAK
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8-QPD>`
     - R
     - QPD
   * - ``ROW_DEFINITION``
     - :ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8-RTB_K13_ROW_DEFINITION>`
     - O
     - ROW_DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-SDR_S31:

SDR_S31: Request anti-microbial device data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.5.4

.. py:class:: hl7types.hl7.v2_8.messages.SDR_S31.SDR_S31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``ANTI_MICROBIAL_DEVICE_DATA``
     - :ref:`SDR_S31_ANTI_MICROBIAL_DEVICE_DATA <hl7-v2_8-SDR_S31_ANTI_MICROBIAL_DEVICE_DATA>`
     - R
     - ANTI_MICROBIAL_DEVICE_DATA

.. _hl7-v2_8-SDR_S32:

SDR_S32: Request anti-microbial device cycle data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.5.4

.. py:class:: hl7types.hl7.v2_8.messages.SDR_S32.SDR_S32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``ANTI_MICROBIAL_DEVICE_CYCLE_DATA``
     - :ref:`SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA <hl7-v2_8-SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA>`
     - R
     - ANTI_MICROBIAL_DEVICE_CYCLE_DATA

.. _hl7-v2_8-SDR_S36:

SDR_S36: Notification of anti-microbial device data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.6.4

.. py:class:: hl7types.hl7.v2_8.messages.SDR_S36.SDR_S36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``ANTI_MICROBIAL_DEVICE_DATA``
     - :ref:`SDR_S31_ANTI_MICROBIAL_DEVICE_DATA <hl7-v2_8-SDR_S31_ANTI_MICROBIAL_DEVICE_DATA>`
     - R
     - ANTI_MICROBIAL_DEVICE_DATA

.. _hl7-v2_8-SDR_S37:

SDR_S37: Notification of anti-microbial device cycle data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.6.5

.. py:class:: hl7types.hl7.v2_8.messages.SDR_S37.SDR_S37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``ANTI_MICROBIAL_DEVICE_CYCLE_DATA``
     - :ref:`SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA <hl7-v2_8-SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA>`
     - R
     - ANTI_MICROBIAL_DEVICE_CYCLE_DATA

.. _hl7-v2_8-SIU_S12:

SIU_S12: Notification of new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S12.SIU_S12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S13:

SIU_S13: Notification of appointment rescheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S13.SIU_S13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S14:

SIU_S14: Notification of appointment modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S14.SIU_S14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S15:

SIU_S15: Notification of appointment cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S15.SIU_S15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S16:

SIU_S16: Notification of appointment discontinuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S16.SIU_S16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S17:

SIU_S17: Notification of appointment deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S17.SIU_S17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S18:

SIU_S18: Notification of addition of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S18.SIU_S18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S19:

SIU_S19: Notification of modification of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S19.SIU_S19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S20:

SIU_S20: Notification of cancellation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S20.SIU_S20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S21:

SIU_S21: Notification of discontinuation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S21.SIU_S21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S22:

SIU_S22: Notification of deletion of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S22.SIU_S22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S23:

SIU_S23: Notification of blocked schedule time slot(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S23.SIU_S23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S24:

SIU_S24: Notification of opened ("unblocked"") schedule time slot(s)"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S24.SIU_S24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S26:

SIU_S26: SIU/ACK Notification that patient did not show up for schedule appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S26.SIU_S26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SIU_S27:

SIU_S27: Broadcast Notification of Scheduled Appointments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.4

.. py:class:: hl7types.hl7.v2_8.messages.SIU_S27.SIU_S27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8-SCH>`
     - R
     - SCH
   * - ``TQ1``
     - list[:ref:`TQ1 <hl7-v2_8-TQ1>`]
     - O
     - TQ1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_8-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_8-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SLR_S28:

SLR_S28: Request new sterilization lot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.5.1

.. py:class:: hl7types.hl7.v2_8.messages.SLR_S28.SLR_S28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``SLT``
     - list[:ref:`SLT <hl7-v2_8-SLT>`]
     - R
     - SLT

.. _hl7-v2_8-SLR_S29:

SLR_S29: Request Sterilization lot deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.5.2

.. py:class:: hl7types.hl7.v2_8.messages.SLR_S29.SLR_S29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``SLT``
     - list[:ref:`SLT <hl7-v2_8-SLT>`]
     - R
     - SLT

.. _hl7-v2_8-SLR_S30:

SLR_S30: Request item
~~~~~~~~~~~~~~~~~~~~~

Section 17.5.3

.. py:class:: hl7types.hl7.v2_8.messages.SLR_S30.SLR_S30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``SLT``
     - list[:ref:`SLT <hl7-v2_8-SLT>`]
     - R
     - SLT

.. _hl7-v2_8-SLR_S34:

SLR_S34: Notification of sterilization lot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.6.2

.. py:class:: hl7types.hl7.v2_8.messages.SLR_S34.SLR_S34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``SLT``
     - list[:ref:`SLT <hl7-v2_8-SLT>`]
     - R
     - SLT

.. _hl7-v2_8-SLR_S35:

SLR_S35: Notification of sterilization lot deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.6.3

.. py:class:: hl7types.hl7.v2_8.messages.SLR_S35.SLR_S35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``SLT``
     - list[:ref:`SLT <hl7-v2_8-SLT>`]
     - R
     - SLT

.. _hl7-v2_8-SRM_S01:

SRM_S01: Request new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S01.SRM_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S02:

SRM_S02: Request appointment rescheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S02.SRM_S02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S03:

SRM_S03: Request appointment modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S03.SRM_S03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S04:

SRM_S04: Request appointment cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S04.SRM_S04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S05:

SRM_S05: Request appointment discontinuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S05.SRM_S05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S06:

SRM_S06: Request appointment deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S06.SRM_S06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S07:

SRM_S07: Request addition of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S07.SRM_S07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S08:

SRM_S08: Request modification of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S08.SRM_S08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S09:

SRM_S09: Request cancellation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S09.SRM_S09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S10:

SRM_S10: Request discontinuation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S10.SRM_S10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRM_S11:

SRM_S11: Request deletion of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRM_S11.SRM_S11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_8-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_8-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_8-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_8-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_8-SRR_S01:

SRR_S01: Request new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3

.. py:class:: hl7types.hl7.v2_8.messages.SRR_S01.SRR_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8-MSA>`
     - R
     - MSA
   * - ``ERR``
     - list[:ref:`ERR <hl7-v2_8-ERR>`]
     - O
     - ERR
   * - ``SCHEDULE``
     - :ref:`SRR_S01_SCHEDULE <hl7-v2_8-SRR_S01_SCHEDULE>`
     - O
     - SCHEDULE

.. _hl7-v2_8-SSR_U04:

SSR_U04: specimen status request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.4

.. py:class:: hl7types.hl7.v2_8.messages.SSR_U04.SSR_U04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``SPECIMEN_CONTAINER``
     - list[:ref:`SSR_U04_SPECIMEN_CONTAINER <hl7-v2_8-SSR_U04_SPECIMEN_CONTAINER>`]
     - R
     - SPECIMEN_CONTAINER

.. _hl7-v2_8-SSU_U03:

SSU_U03: Specimen status update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.3

.. py:class:: hl7types.hl7.v2_8.messages.SSU_U03.SSU_U03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``SPECIMEN_CONTAINER``
     - list[:ref:`SSU_U03_SPECIMEN_CONTAINER <hl7-v2_8-SSU_U03_SPECIMEN_CONTAINER>`]
     - R
     - SPECIMEN_CONTAINER

.. _hl7-v2_8-STC_S33:

STC_S33: Notification of sterilization configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 17.6.1

.. py:class:: hl7types.hl7.v2_8.messages.STC_S33.STC_S33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``SCP``
     - list[:ref:`SCP <hl7-v2_8-SCP>`]
     - R
     - SCP

.. _hl7-v2_8-TCU_U10:

TCU_U10: Automated equipment test code settings update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.10

.. py:class:: hl7types.hl7.v2_8.messages.TCU_U10.TCU_U10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``TEST_CONFIGURATION``
     - list[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_8-TCU_U10_TEST_CONFIGURATION>`]
     - R
     - TEST_CONFIGURATION

.. _hl7-v2_8-TCU_U11:

TCU_U11: Automated equipment test code settings request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 13.3.11

.. py:class:: hl7types.hl7.v2_8.messages.TCU_U11.TCU_U11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8-EQU>`
     - R
     - EQU
   * - ``TEST_CONFIGURATION``
     - list[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_8-TCU_U10_TEST_CONFIGURATION>`]
     - R
     - TEST_CONFIGURATION

.. _hl7-v2_8-UDM_Q05:

UDM_Q05: Unsolicited display update message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.10.1.1

.. py:class:: hl7types.hl7.v2_8.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``URD``
     - :ref:`URD <hl7-v2_8-URD>`
     - R
     - URD
   * - ``URS``
     - :ref:`URS <hl7-v2_8-URS>`
     - O
     - URS
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_8-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8-DSC>`
     - O
     - DSC

.. _hl7-v2_8-VXU_V04:

VXU_V04: VXU - Unsolicited vaccination record update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 4.A.6

.. py:class:: hl7types.hl7.v2_8.messages.VXU_V04.VXU_V04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8-MSH>`
     - R
     - MSH
   * - ``SFT``
     - list[:ref:`SFT <hl7-v2_8-SFT>`]
     - O
     - SFT
   * - ``UAC``
     - :ref:`UAC <hl7-v2_8-UAC>`
     - O
     - UAC
   * - ``PID``
     - :ref:`PID <hl7-v2_8-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_8-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_8-NK1>`]
     - O
     - NK1
   * - ``ARV``
     - list[:ref:`ARV <hl7-v2_8-ARV>`]
     - O
     - ARV
   * - ``PATIENT_VISIT``
     - :ref:`VXU_V04_PATIENT_VISIT <hl7-v2_8-VXU_V04_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_8-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`VXU_V04_INSURANCE <hl7-v2_8-VXU_V04_INSURANCE>`]
     - O
     - INSURANCE
   * - ``PERSON_OBSERVATION``
     - list[:ref:`VXU_V04_PERSON_OBSERVATION <hl7-v2_8-VXU_V04_PERSON_OBSERVATION>`]
     - O
     - PERSON_OBSERVATION
   * - ``ORDER``
     - list[:ref:`VXU_V04_ORDER <hl7-v2_8-VXU_V04_ORDER>`]
     - O
     - ORDER
