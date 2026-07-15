v2.3 Messages
=============

.. _hl7-v2_3-ACK:

ACK: General acknowledgment message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR

.. _hl7-v2_3-ADT_A01:

ADT_A01: Admit/visit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A02:

ADT_A02:  Transfer a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A03:

ADT_A03:  Discharge a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A03_PROCEDURE <hl7-v2_3-ADT_A03_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A04:

ADT_A04:  Register a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.4

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A05:

ADT_A05:  Preadmit a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.5

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A06:

ADT_A06:  Transfer an outpatient to inpatient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``PROCEDURE``
     - list[:ref:`ADT_A06_PROCEDURE <hl7-v2_3-ADT_A06_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A06_INSURANCE <hl7-v2_3-ADT_A06_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A07:

ADT_A07:  Transfer an inpatient to outpatient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.7

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``PROCEDURE``
     - list[:ref:`ADT_A06_PROCEDURE <hl7-v2_3-ADT_A06_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A06_INSURANCE <hl7-v2_3-ADT_A06_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A08:

ADT_A08:  Update patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.8

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A09:

ADT_A09:  Patient departing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1

.. _hl7-v2_3-ADT_A10:

ADT_A10:  Patient arriving
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.10

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1

.. _hl7-v2_3-ADT_A11:

ADT_A11:  Cancel admit
~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.11

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1

.. _hl7-v2_3-ADT_A12:

ADT_A12:  Cancel transfer
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - :ref:`DG1 <hl7-v2_3-DG1>`
     - O
     - DG1

.. _hl7-v2_3-ADT_A13:

ADT_A13:  Cancel discharge
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.13

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A14:

ADT_A14:  Pending admit
~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.14

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A15:

ADT_A15:  Pending transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.15

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1

.. _hl7-v2_3-ADT_A16:

ADT_A16:  Pending discharge
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - :ref:`DG1 <hl7-v2_3-DG1>`
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG

.. _hl7-v2_3-ADT_A17:

ADT_A17:  Swap patients
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A18:

ADT_A18:  Merge patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A18.ADT_A18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - O
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1

.. _hl7-v2_3-ADT_A20:

ADT_A20:  Nursing/Census application updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``NPU``
     - :ref:`NPU <hl7-v2_3-NPU>`
     - R
     - NPU

.. _hl7-v2_3-ADT_A21:

ADT_A21:  Leave of absence - out (leaving)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.21

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A22:

ADT_A22:  Leave of absence - in (returning)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.22

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A22.ADT_A22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A23:

ADT_A23:  Delete a patient record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.23

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A23.ADT_A23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A24:

ADT_A24:  Link patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - O
     - PV1
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1

.. _hl7-v2_3-ADT_A25:

ADT_A25:  Cancel pending discharge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.25

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A25.ADT_A25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A26:

ADT_A26:  Cancel pending transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.26

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A26.ADT_A26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A27:

ADT_A27:  Cancel pending admit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.27

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A27.ADT_A27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A28:

ADT_A28:  Add person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.28

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A29:

ADT_A29:  Delete person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.29

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A29.ADT_A29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A30:

ADT_A30:  Merge person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A30.ADT_A30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A31:

ADT_A31:  Update person information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.31

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``PROCEDURE``
     - list[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_3-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_3-UB2>`
     - O
     - UB2

.. _hl7-v2_3-ADT_A32:

ADT_A32:  Cancel patient arriving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.32

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A32.ADT_A32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A33:

ADT_A33:  Cancel patient departing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.33

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A33.ADT_A33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX

.. _hl7-v2_3-ADT_A34:

ADT_A34:  Merge patient information - patient ID only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.34

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A34.ADT_A34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A35:

ADT_A35:  Merge patient information - account number only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.35

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A35.ADT_A35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A36:

ADT_A36:  Merge patient information - patient ID and account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.36

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A36.ADT_A36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A37:

ADT_A37:  Unlink patient information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.37

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - O
     - PV1
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1

.. _hl7-v2_3-ADT_A38:

ADT_A38: Cancel pre-admit
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A38.ADT_A38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG

.. _hl7-v2_3-ADT_A39:

ADT_A39: Merge person - external ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A39.ADT_A39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-ADT_A40:

ADT_A40: Merge patient - internal ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.40

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A40.ADT_A40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-ADT_A41:

ADT_A41: Merge account - patient account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.41

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A41.ADT_A41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-ADT_A42:

ADT_A42: Merge visit - visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.42

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A42.ADT_A42
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-ADT_A43:

ADT_A43: Move patient information - internal ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A43.ADT_A43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A43_PATIENT <hl7-v2_3-ADT_A43_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-ADT_A44:

ADT_A44: Move account information - internal ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.44

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A44.ADT_A44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`ADT_A43_PATIENT <hl7-v2_3-ADT_A43_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-ADT_A45:

ADT_A45: Move visit information - visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A45.ADT_A45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MERGE_INFO``
     - list[:ref:`ADT_A45_MERGE_INFO <hl7-v2_3-ADT_A45_MERGE_INFO>`]
     - R
     - MERGE_INFO

.. _hl7-v2_3-ADT_A46:

ADT_A46: Change external ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.46

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A46.ADT_A46
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A47:

ADT_A47: Change internal ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.47

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A47.ADT_A47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A48:

ADT_A48: Change alternate patient ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.48

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A48.ADT_A48
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A49:

ADT_A49: Change patient account number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.49

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A49.ADT_A49
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG

.. _hl7-v2_3-ADT_A50:

ADT_A50: Change visit number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A50.ADT_A50
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1

.. _hl7-v2_3-ADT_A51:

ADT_A51: Change alternate visit ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 3.2.51

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A51.ADT_A51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - R
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1

.. _hl7-v2_3-ARD_A19:

ARD_A19: HL7 v2 ARD_A19 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ARD_A19.ARD_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``QUERY_RESPONSE``
     - list[:ref:`ARD_A19_QUERY_RESPONSE <hl7-v2_3-ARD_A19_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-BAR_P01:

BAR_P01: Add patient account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``VISIT``
     - list[:ref:`BAR_P01_VISIT <hl7-v2_3-BAR_P01_VISIT>`]
     - R
     - VISIT

.. _hl7-v2_3-BAR_P02:

BAR_P02: Purge patient account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`BAR_P02_PATIENT <hl7-v2_3-BAR_P02_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-BAR_P05:

BAR_P05: Update account
~~~~~~~~~~~~~~~~~~~~~~~

Section 6.3.5

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P05.BAR_P05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``VISIT``
     - list[:ref:`BAR_P01_VISIT <hl7-v2_3-BAR_P01_VISIT>`]
     - R
     - VISIT

.. _hl7-v2_3-BAR_P06:

BAR_P06: End account
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P06.BAR_P06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`BAR_P06_PATIENT <hl7-v2_3-BAR_P06_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C01:

CRM_C01: SRM - Register a patient on a clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C01.CRM_C01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C02:

CRM_C02: SRM - Cancel a patient registration on clin.trial (for clerical mistakes only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.1

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C02.CRM_C02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C03:

CRM_C03: SRM - Correct/update registration information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.1

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C03.CRM_C03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C04:

CRM_C04: SRM - Patient has gone off a clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.1

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C04.CRM_C04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C05:

CRM_C05: SRM - Patient enters phase of clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.1

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C05.CRM_C05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C06:

CRM_C06: SRM - Cancel patient entering a phase (clerical mistake)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.1

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C06.CRM_C06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C07:

CRM_C07: SRM - Correct/update phase information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.1

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C07.CRM_C07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CRM_C08:

CRM_C08: SRM - Patient has gone off phase of clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.1

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C08.CRM_C08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CSU_C09:

CSU_C09: CSU - Automated time intervals for reporting, like monthly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C09.CSU_C09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CSU_C10:

CSU_C10: CSU - Patient completes the clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.2

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C10.CSU_C10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CSU_C11:

CSU_C11: CSU - Patient completes a phase of the clinical trial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.2

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C11.CSU_C11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-CSU_C12:

CSU_C12: CSU - Update/correction of patient order/result information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.6.2

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C12.CSU_C12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PATIENT``
     - list[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-DFT_P03:

DFT_P03: Post detail financial transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - O
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_3-PV2>`
     - O
     - PV2
   * - ``DB1``
     - list[:ref:`DB1 <hl7-v2_3-DB1>`]
     - O
     - DB1
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - O
     - OBX
   * - ``FINANCIAL``
     - list[:ref:`DFT_P03_FINANCIAL <hl7-v2_3-DFT_P03_FINANCIAL>`]
     - R
     - FINANCIAL
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - :ref:`DRG <hl7-v2_3-DRG>`
     - O
     - DRG
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`DFT_P03_INSURANCE <hl7-v2_3-DFT_P03_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC

.. _hl7-v2_3-DOC_T12:

DOC_T12: Document query
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DOC_T12.DOC_T12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``RESULT``
     - list[:ref:`DOC_T12_RESULT <hl7-v2_3-DOC_T12_RESULT>`]
     - R
     - RESULT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-DSR_Q01:

DSR_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DSR_Q01.DSR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_3-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-DSR_Q03:

DSR_Q03: Deferred response to a query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DSR_Q03.DSR_Q03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - O
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - O
     - QAK
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_3-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-EDR_Q01:

EDR_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.EDR_Q01.EDR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - R
     - QAK
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_3-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-EQQ_Q01:

EQQ_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.EQQ_Q01.EQQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EQL``
     - :ref:`EQL <hl7-v2_3-EQL>`
     - R
     - EQL
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-ERP_Q01:

ERP_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ERP_Q01.ERP_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - R
     - QAK
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_3-ERQ>`
     - R
     - ERQ
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-MDM_T01:

MDM_T01: Original document notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T01.MDM_T01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA

.. _hl7-v2_3-MDM_T02:

MDM_T02: Original document notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T02.MDM_T02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - R
     - OBX

.. _hl7-v2_3-MDM_T03:

MDM_T03: Document status change notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.3

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T03.MDM_T03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA

.. _hl7-v2_3-MDM_T04:

MDM_T04: Document status change notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.4

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T04.MDM_T04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - R
     - OBX

.. _hl7-v2_3-MDM_T05:

MDM_T05: Document addendum notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.5

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T05.MDM_T05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA

.. _hl7-v2_3-MDM_T06:

MDM_T06: Document addendum notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.6

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T06.MDM_T06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - R
     - OBX

.. _hl7-v2_3-MDM_T07:

MDM_T07: Document edit notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.7

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T07.MDM_T07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA

.. _hl7-v2_3-MDM_T08:

MDM_T08: Document edit notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.8

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T08.MDM_T08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - R
     - OBX

.. _hl7-v2_3-MDM_T09:

MDM_T09: Document replace notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.9

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T09.MDM_T09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA

.. _hl7-v2_3-MDM_T10:

MDM_T10: Document replacement notification and content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.10

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T10.MDM_T10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_3-OBX>`]
     - R
     - OBX

.. _hl7-v2_3-MDM_T11:

MDM_T11: Document cancel notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 9.4.11

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T11.MDM_T11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - R
     - PV1
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - R
     - TXA

.. _hl7-v2_3-MFK_M01:

MFK_M01: Master file not otherwise specified (for backward comp.only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_3-MFA>`]
     - O
     - MFA

.. _hl7-v2_3-MFK_M02:

MFK_M02: HL7 v2 MFK_M02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFK_M02.MFK_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_3-MFA>`]
     - O
     - MFA

.. _hl7-v2_3-MFN_M01:

MFN_M01: Master file not otherwise specified (for backward comp.only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M01.MFN_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF``
     - list[:ref:`MFN_M01_MF <hl7-v2_3-MFN_M01_MF>`]
     - R
     - MF

.. _hl7-v2_3-MFN_M02:

MFN_M02: Master file - Staff Practioner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_STAFF``
     - list[:ref:`MFN_M02_MF_STAFF <hl7-v2_3-MFN_M02_MF_STAFF>`]
     - R
     - MF_STAFF

.. _hl7-v2_3-MFN_M03:

MFN_M03: Master file - Test/Observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M03.MFN_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_TEST``
     - list[:ref:`MFN_M03_MF_TEST <hl7-v2_3-MFN_M03_MF_TEST>`]
     - R
     - MF_TEST

.. _hl7-v2_3-MFN_M04:

MFN_M04: Charge description master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.9.1

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M04.MFN_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_CDM``
     - list[:ref:`MFN_M06_MF_CDM <hl7-v2_3-MFN_M06_MF_CDM>`]
     - R
     - MF_CDM

.. _hl7-v2_3-MFN_M05:

MFN_M05: Patient location master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M05.MFN_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_LOCATION``
     - list[:ref:`MFN_M05_MF_LOCATION <hl7-v2_3-MFN_M05_MF_LOCATION>`]
     - R
     - MF_LOCATION

.. _hl7-v2_3-MFN_M06:

MFN_M06: Clinical study master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M06.MFN_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_CDM``
     - list[:ref:`MFN_M06_MF_CDM <hl7-v2_3-MFN_M06_MF_CDM>`]
     - R
     - MF_CDM

.. _hl7-v2_3-MFN_M07:

MFN_M07: Clinical study without phases but with schedules master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M07.MFN_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_CLIN_STUDY``
     - list[:ref:`MFN_M07_MF_CLIN_STUDY <hl7-v2_3-MFN_M07_MF_CLIN_STUDY>`]
     - R
     - MF_CLIN_STUDY

.. _hl7-v2_3-MFN_M08:

MFN_M08: Test/Observation (Numeric) master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M08.MFN_M08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_TEST_NUMERIC``
     - list[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_3-MFN_M08_MF_TEST_NUMERIC>`]
     - R
     - MF_TEST_NUMERIC

.. _hl7-v2_3-MFN_M09:

MFN_M09: Test/Observation (Categorical) master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M09.MFN_M09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_TEST_CATEGORICAL``
     - list[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_3-MFN_M09_MF_TEST_CATEGORICAL>`]
     - R
     - MF_TEST_CATEGORICAL

.. _hl7-v2_3-MFN_M10:

MFN_M10: Test/Observation batteries master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M10.MFN_M10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_TEST_BATTERIES``
     - list[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_3-MFN_M10_MF_TEST_BATTERIES>`]
     - R
     - MF_TEST_BATTERIES

.. _hl7-v2_3-MFN_M11:

MFN_M11: Test/calculated observation master file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M11.MFN_M11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - R
     - MFI
   * - ``MF_TEST_CALCULATED``
     - list[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_3-MFN_M11_MF_TEST_CALCULATED>`]
     - R
     - MF_TEST_CALCULATED

.. _hl7-v2_3-OMD_O01:

OMD_O01: HL7 v2 OMD_O01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OMD_O01.OMD_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMD_O01_PATIENT <hl7-v2_3-OMD_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER_DIET``
     - list[:ref:`OMD_O01_ORDER_DIET <hl7-v2_3-OMD_O01_ORDER_DIET>`]
     - R
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - list[:ref:`OMD_O01_ORDER_TRAY <hl7-v2_3-OMD_O01_ORDER_TRAY>`]
     - O
     - ORDER_TRAY

.. _hl7-v2_3-OMN_O01:

OMN_O01: HL7 v2 OMN_O01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OMN_O01.OMN_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMN_O01_PATIENT <hl7-v2_3-OMN_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMN_O01_ORDER <hl7-v2_3-OMN_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-OMS_O01:

OMS_O01: HL7 v2 OMS_O01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OMS_O01.OMS_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`OMS_O01_PATIENT <hl7-v2_3-OMS_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`OMS_O01_ORDER <hl7-v2_3-OMS_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-ORD_O02:

ORD_O02: HL7 v2 ORD_O02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORD_O02.ORD_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORD_O02_RESPONSE <hl7-v2_3-ORD_O02_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_3-ORF_R04:

ORF_R04: ORF - Response to query; transmission of requested observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORF_R04.ORF_R04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``QUERY_RESPONSE``
     - list[:ref:`ORF_R04_QUERY_RESPONSE <hl7-v2_3-ORF_R04_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-ORM_O01:

ORM_O01: ORM - Order message (also RDE, RDS, RGV, RAS,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORM_O01.ORM_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`ORM_O01_PATIENT <hl7-v2_3-ORM_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`ORM_O01_ORDER <hl7-v2_3-ORM_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-ORN_O02:

ORN_O02: HL7 v2 ORN_O02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORN_O02.ORN_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORN_O02_RESPONSE <hl7-v2_3-ORN_O02_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_3-ORR_O02:

ORR_O02: ORR - Order response (also RRE, RRD, RRG, RRA,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORR_O02.ORR_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`ORR_O02_RESPONSE <hl7-v2_3-ORR_O02_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_3-ORU_R01:

ORU_R01: Unsolicited transmission of an observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RESPONSE``
     - list[:ref:`ORU_R01_RESPONSE <hl7-v2_3-ORU_R01_RESPONSE>`]
     - R
     - RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-OSQ_Q06:

OSQ_Q06: Query for order status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OSQ_Q06.OSQ_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-OSR_Q06:

OSR_Q06: Query for order status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OSR_Q06.OSR_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``RESPONSE``
     - :ref:`OSR_Q06_RESPONSE <hl7-v2_3-OSR_Q06_RESPONSE>`
     - O
     - RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-PEX_P07:

PEX_P07: PEX - Unsolicited initial individual product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PEX_P07.PEX_P07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``VISIT``
     - :ref:`PEX_P07_VISIT <hl7-v2_3-PEX_P07_VISIT>`
     - O
     - VISIT
   * - ``EXPERIENCE``
     - list[:ref:`PEX_P07_EXPERIENCE <hl7-v2_3-PEX_P07_EXPERIENCE>`]
     - R
     - EXPERIENCE

.. _hl7-v2_3-PEX_P08:

PEX_P08: PEX - Unsolicited update individual product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.10.1

.. py:class:: hl7types.hl7.v2_3.messages.PEX_P08.PEX_P08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``VISIT``
     - :ref:`PEX_P07_VISIT <hl7-v2_3-PEX_P07_VISIT>`
     - O
     - VISIT
   * - ``EXPERIENCE``
     - list[:ref:`PEX_P07_EXPERIENCE <hl7-v2_3-PEX_P07_EXPERIENCE>`]
     - R
     - EXPERIENCE

.. _hl7-v2_3-PGL_PC6:

PGL_PC6: PGL - PC/Goal Add
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PGL_PC6.PGL_PC6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_3-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_3-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_3-PGL_PC7:

PGL_PC7: PGL - PC/Goal Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.1

.. py:class:: hl7types.hl7.v2_3.messages.PGL_PC7.PGL_PC7
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_3-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_3-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_3-PGL_PC8:

PGL_PC8: PGL - PC/Goal Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.1

.. py:class:: hl7types.hl7.v2_3.messages.PGL_PC8.PGL_PC8
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_3-PGL_PC6_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``GOAL``
     - list[:ref:`PGL_PC6_GOAL <hl7-v2_3-PGL_PC6_GOAL>`]
     - R
     - GOAL

.. _hl7-v2_3-PIN_I07:

PIN_I07: Unsolicited insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PIN_I07.PIN_I07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`PIN_I07_PROVIDER <hl7-v2_3-PIN_I07_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`PIN_I07_GUARANTOR_INSURANCE <hl7-v2_3-PIN_I07_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-PPG_PCG:

PPG_PCG: PPP - PC/Pathway (Goal Oriented) Add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPG_PCG.PPG_PCG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_3-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_3-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_3-PPG_PCH:

PPG_PCH: PPP - PC/Pathway (Goal Oriented) Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.4

.. py:class:: hl7types.hl7.v2_3.messages.PPG_PCH.PPG_PCH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_3-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_3-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_3-PPG_PCJ:

PPG_PCJ: PPP - PC/Pathway (Goal Oriented) Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.4

.. py:class:: hl7types.hl7.v2_3.messages.PPG_PCJ.PPG_PCJ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_3-PPG_PCG_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPG_PCG_PATHWAY <hl7-v2_3-PPG_PCG_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_3-PPP_PCB:

PPP_PCB: PPP - PC/Pathway (Problem Oriented) Add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPP_PCB.PPP_PCB
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_3-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_3-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_3-PPP_PCC:

PPP_PCC: PPP - PC/Pathway (Problem Oriented) Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.3

.. py:class:: hl7types.hl7.v2_3.messages.PPP_PCC.PPP_PCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_3-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_3-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_3-PPP_PCD:

PPP_PCD: PPP - PC/Pathway (Problem Oriented) Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.3

.. py:class:: hl7types.hl7.v2_3.messages.PPP_PCD.PPP_PCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_3-PPP_PCB_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PATHWAY``
     - list[:ref:`PPP_PCB_PATHWAY <hl7-v2_3-PPP_PCB_PATHWAY>`]
     - R
     - PATHWAY

.. _hl7-v2_3-PPR_PC1:

PPR_PC1: PPR - PC/Problem Add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPR_PC1.PPR_PC1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_3-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_3-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_3-PPR_PC2:

PPR_PC2: PPR - PC/Problem Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.2

.. py:class:: hl7types.hl7.v2_3.messages.PPR_PC2.PPR_PC2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_3-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_3-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_3-PPR_PC3:

PPR_PC3: PPR - PC/Problem Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.2

.. py:class:: hl7types.hl7.v2_3.messages.PPR_PC3.PPR_PC3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PATIENT_VISIT``
     - :ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_3-PPR_PC1_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``PROBLEM``
     - list[:ref:`PPR_PC1_PROBLEM <hl7-v2_3-PPR_PC1_PROBLEM>`]
     - R
     - PROBLEM

.. _hl7-v2_3-PPT_PCL:

PPT_PCL: PPP - PC/Pathway (Goal Oriented) Query Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPT_PCL.PPT_PCL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PPT_PCL_PATIENT <hl7-v2_3-PPT_PCL_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-PPV_PCA:

PPV_PCA: PGL - PC/Goal Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPV_PCA.PPV_PCA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PPV_PCA_PATIENT <hl7-v2_3-PPV_PCA_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-PRR_PC5:

PRR_PC5: PPR - PC/Problem Reponse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PRR_PC5.PRR_PC5
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PRR_PC5_PATIENT <hl7-v2_3-PRR_PC5_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-PTR_PCF:

PTR_PCF: PPP - PC/Pathway (Problem Oriented) Query Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PTR_PCF.PTR_PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``PATIENT``
     - list[:ref:`PTR_PCF_PATIENT <hl7-v2_3-PTR_PCF_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_3-QCK_Q02:

QCK_Q02: Query sent for deferred response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QCK_Q02.QCK_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - O
     - QAK

.. _hl7-v2_3-QRY_A19:

QRY_A19:  Patient query
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_A19.QRY_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF

.. _hl7-v2_3-QRY_PC4:

QRY_PC4: PPR - PC/Problem Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PC4.QRY_PC4
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF

.. _hl7-v2_3-QRY_PC9:

QRY_PC9: PGL - PC/Goal Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.7

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PC9.QRY_PC9
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF

.. _hl7-v2_3-QRY_PCE:

QRY_PCE: PPP - PC/Pathway (Problem Oriented) Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.9

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PCE.QRY_PCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF

.. _hl7-v2_3-QRY_PCK:

QRY_PCK: PPP - PC/Pathway (Goal Oriented) Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 12.2.11

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PCK.QRY_PCK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF

.. _hl7-v2_3-QRY_Q01:

QRY_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_Q01.QRY_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-QRY_Q02:

QRY_Q02: Query sent for deferred response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_Q02.QRY_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-QRY_R02:

QRY_R02: QRY - Query for results of observation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_R02.QRY_R02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - R
     - QRF

.. _hl7-v2_3-QRY_T12:

QRY_T12: Document query
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_T12.QRY_T12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF

.. _hl7-v2_3-RAR_RAR:

RAR_RAR: RAR - Pharmacy administration information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RAR_RAR.RAR_RAR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`RAR_RAR_DEFINITION <hl7-v2_3-RAR_RAR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RAS_O01:

RAS_O01: ORM - Order message (also RDE, RDS, RGV, RAS,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RAS_O01.RAS_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RAS_O01_PATIENT <hl7-v2_3-RAS_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RAS_O01_ORDER <hl7-v2_3-RAS_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-RCI_I05:

RCI_I05: Request for patient clinical information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RCI_I05.RCI_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RCI_I05_PROVIDER <hl7-v2_3-RCI_I05_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``OBSERVATION``
     - list[:ref:`RCI_I05_OBSERVATION <hl7-v2_3-RCI_I05_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RCL_I06:

RCL_I06: Request/receipt of clinical data listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RCL_I06.RCL_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RCL_I06_PROVIDER <hl7-v2_3-RCL_I06_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_3-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RDE_O01:

RDE_O01: ORM - Order message (also RDE, RDS, RGV, RAS,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDE_O01.RDE_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDE_O01_PATIENT <hl7-v2_3-RDE_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDE_O01_ORDER <hl7-v2_3-RDE_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-RDO_O01:

RDO_O01: HL7 v2 RDO_O01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDO_O01.RDO_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDO_O01_PATIENT <hl7-v2_3-RDO_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDO_O01_ORDER <hl7-v2_3-RDO_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-RDR_RDR:

RDR_RDR: RDR - Pharmacy dispense information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDR_RDR.RDR_RDR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`RDR_RDR_DEFINITION <hl7-v2_3-RDR_RDR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RDS_O01:

RDS_O01: ORM - Order message (also RDE, RDS, RGV, RAS,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDS_O01.RDS_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RDS_O01_PATIENT <hl7-v2_3-RDS_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RDS_O01_ORDER <hl7-v2_3-RDS_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-REF_I12:

REF_I12:  Patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.REF_I12.REF_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``RESULTS``
     - list[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]
     - O
     - RESULTS
   * - ``VISIT``
     - :ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-REF_I13:

REF_I13: Modify patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.3

.. py:class:: hl7types.hl7.v2_3.messages.REF_I13.REF_I13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``RESULTS``
     - list[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]
     - O
     - RESULTS
   * - ``VISIT``
     - :ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-REF_I14:

REF_I14: Cancel patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.4

.. py:class:: hl7types.hl7.v2_3.messages.REF_I14.REF_I14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``RESULTS``
     - list[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]
     - O
     - RESULTS
   * - ``VISIT``
     - :ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-REF_I15:

REF_I15: Request patient referral status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4.5

.. py:class:: hl7types.hl7.v2_3.messages.REF_I15.REF_I15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``RESULTS``
     - list[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]
     - O
     - RESULTS
   * - ``VISIT``
     - :ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RER_RER:

RER_RER: RER - Pharmacy encoded order information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RER_RER.RER_RER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`RER_RER_DEFINITION <hl7-v2_3-RER_RER_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RGR_RGR:

RGR_RGR: RGR - Pharmacy dose information query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RGR_RGR.RGR_RGR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`RGR_RGR_DEFINITION <hl7-v2_3-RGR_RGR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RGV_O01:

RGV_O01: ORM - Order message (also RDE, RDS, RGV, RAS,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RGV_O01.RGV_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RGV_O01_PATIENT <hl7-v2_3-RGV_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`RGV_O01_ORDER <hl7-v2_3-RGV_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_3-ROR_ROR:

ROR_ROR: ROR - Pharmacy prescription order query response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ROR_ROR.ROR_ROR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``DEFINITION``
     - list[:ref:`ROR_ROR_DEFINITION <hl7-v2_3-ROR_ROR_DEFINITION>`]
     - R
     - DEFINITION
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RPA_I08:

RPA_I08: Request for treatment authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RPA_I08.RPA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RPA_I08_AUTHORIZATION <hl7-v2_3-RPA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RPA_I08_PROVIDER <hl7-v2_3-RPA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`RPA_I08_INSURANCE <hl7-v2_3-RPA_I08_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RPA_I08_PROCEDURE <hl7-v2_3-RPA_I08_PROCEDURE>`]
     - R
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RPA_I08_OBSERVATION <hl7-v2_3-RPA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RPA_I08_VISIT <hl7-v2_3-RPA_I08_VISIT>`
     - O
     - VISIT

.. _hl7-v2_3-RPI_I01:

RPI_I01: Request for insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RPI_I01.RPI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPI_I01_PROVIDER <hl7-v2_3-RPI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RPI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RPL_I02:

RPL_I02: Request/receipt of patient selection display list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RPL_I02.RPL_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``PROVIDER``
     - list[:ref:`RPL_I02_PROVIDER <hl7-v2_3-RPL_I02_PROVIDER>`]
     - R
     - PROVIDER
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_3-DSP>`]
     - O
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RQA_I08:

RQA_I08: Request for treatment authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I08.RQA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQA_I09:

RQA_I09: Request for modification to an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.3

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I09.RQA_I09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQA_I10:

RQA_I10: Request for resubmission of an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.3.4

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I10.RQA_I10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQA_I11:

RQA_I11: Request for cancellation of an authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.4

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I11.RQA_I11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``OBSERVATION``
     - list[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]
     - O
     - OBSERVATION
   * - ``VISIT``
     - :ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQC_I05:

RQC_I05: Request for patient clinical information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQC_I05.RQC_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RQC_I05_PROVIDER <hl7-v2_3-RQC_I05_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQC_I06:

RQC_I06: Request/receipt of clinical data listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQC_I06.RQC_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``PROVIDER``
     - list[:ref:`RQC_I06_PROVIDER <hl7-v2_3-RQC_I06_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - :ref:`GT1 <hl7-v2_3-GT1>`
     - O
     - GT1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQI_I01:

RQI_I01: Request for insurance information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQI_I01.RQI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_3-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQI_I02:

RQI_I02: Request/receipt of patient selection display list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.2.2

.. py:class:: hl7types.hl7.v2_3.messages.RQI_I02.RQI_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_3-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQI_I03:

RQI_I03: Request/receipt of patient selection list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 11.2.3

.. py:class:: hl7types.hl7.v2_3.messages.RQI_I03.RQI_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQI_I01_PROVIDER <hl7-v2_3-RQI_I01_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GUARANTOR_INSURANCE``
     - :ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE>`
     - O
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQP_I04:

RQP_I04: Request for patient demographic data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQP_I04.RQP_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PROVIDER``
     - list[:ref:`RQP_I04_PROVIDER <hl7-v2_3-RQP_I04_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_3-GT1>`]
     - O
     - GT1
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RQQ_Q01:

RQQ_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQQ_Q01.RQQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_3-ERQ>`
     - R
     - ERQ
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-RRA_O02:

RRA_O02: ORR - Order response (also RRE, RRD, RRG, RRA,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRA_O02.RRA_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRA_O02_RESPONSE <hl7-v2_3-RRA_O02_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_3-RRD_O02:

RRD_O02: ORR - Order response (also RRE, RRD, RRG, RRA,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRD_O02.RRD_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`RRD_O02_PATIENT <hl7-v2_3-RRD_O02_PATIENT>`
     - O
     - PATIENT

.. _hl7-v2_3-RRG_O02:

RRG_O02: ORR - Order response (also RRE, RRD, RRG, RRA,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRG_O02.RRG_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRG_O02_RESPONSE <hl7-v2_3-RRG_O02_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_3-RRI_I12:

RRI_I12:  Patient referral
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRI_I12.RRI_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - O
     - MSA
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_3-RF1>`
     - O
     - RF1
   * - ``AUTHORIZATION``
     - :ref:`RRI_I12_AUTHORIZATION <hl7-v2_3-RRI_I12_AUTHORIZATION>`
     - O
     - AUTHORIZATION
   * - ``PROVIDER``
     - list[:ref:`RRI_I12_PROVIDER <hl7-v2_3-RRI_I12_PROVIDER>`]
     - R
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``ACC``
     - :ref:`ACC <hl7-v2_3-ACC>`
     - O
     - ACC
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_3-DG1>`]
     - O
     - DG1
   * - ``DRG``
     - list[:ref:`DRG <hl7-v2_3-DRG>`]
     - O
     - DRG
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_3-AL1>`]
     - O
     - AL1
   * - ``PROCEDURE``
     - list[:ref:`RRI_I12_PROCEDURE <hl7-v2_3-RRI_I12_PROCEDURE>`]
     - O
     - PROCEDURE
   * - ``RESULTS``
     - list[:ref:`RRI_I12_RESULTS <hl7-v2_3-RRI_I12_RESULTS>`]
     - O
     - RESULTS
   * - ``VISIT``
     - :ref:`RRI_I12_VISIT <hl7-v2_3-RRI_I12_VISIT>`
     - O
     - VISIT
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE

.. _hl7-v2_3-RRO_O02:

RRO_O02: HL7 v2 RRO_O02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRO_O02.RRO_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``RESPONSE``
     - :ref:`RRO_O02_RESPONSE <hl7-v2_3-RRO_O02_RESPONSE>`
     - O
     - RESPONSE

.. _hl7-v2_3-SIU_S12:

SIU_S12: Notification of new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S12.SIU_S12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S13:

SIU_S13: Notification of appointment rescheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.6.2

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S13.SIU_S13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S14:

SIU_S14: Notification of appointment modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.3

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S14.SIU_S14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S15:

SIU_S15: Notification of appointment cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.4

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S15.SIU_S15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S16:

SIU_S16: Notification of appointment discontinuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.5

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S16.SIU_S16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S17:

SIU_S17: Notification of appointment deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.6

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S17.SIU_S17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S18:

SIU_S18: Notification of addition of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.7

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S18.SIU_S18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S19:

SIU_S19: Notification of modification of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.8

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S19.SIU_S19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S20:

SIU_S20: Notification of cancellation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.9

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S20.SIU_S20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S21:

SIU_S21: Notification of discontinuation of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.10

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S21.SIU_S21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S22:

SIU_S22: Notification of deletion of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.11

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S22.SIU_S22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S23:

SIU_S23: Notification of blocked schedule time slot(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.12

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S23.SIU_S23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S24:

SIU_S24: Notification of open ("unblocked"") schedule time slot(s)"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.13

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S24.SIU_S24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SIU_S26:

SIU_S26: notification that patient did not show up for schedule appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.3.14

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S26.SIU_S26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - R
     - SCH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SPQ_Q01:

SPQ_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SPQ_Q01.SPQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``SPR``
     - :ref:`SPR <hl7-v2_3-SPR>`
     - R
     - SPR
   * - ``RDF``
     - :ref:`RDF <hl7-v2_3-RDF>`
     - O
     - RDF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-SQM_S25:

SQM_S25: Query schedule information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SQM_S25.SQM_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``REQUEST``
     - :ref:`SQM_S25_REQUEST <hl7-v2_3-SQM_S25_REQUEST>`
     - O
     - REQUEST
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-SQR_S25:

SQR_S25: Query schedule information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SQR_S25.SQR_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - R
     - QAK
   * - ``SCHEDULE``
     - list[:ref:`SQR_S25_SCHEDULE <hl7-v2_3-SQR_S25_SCHEDULE>`]
     - O
     - SCHEDULE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-SRM_S01:

SRM_S01: Request new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S01.SRM_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S02:

SRM_S02: Request appointment rescheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.2

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S02.SRM_S02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S03:

SRM_S03: Request appointment modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.3

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S03.SRM_S03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S04:

SRM_S04: Request appointment cancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.4

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S04.SRM_S04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S05:

SRM_S05: Request appointment discontinuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.5

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S05.SRM_S05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S06:

SRM_S06: Request appointment deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.6

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S06.SRM_S06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S07:

SRM_S07: Request addition of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.7

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S07.SRM_S07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S08:

SRM_S08: Request modification of service/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.8

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S08.SRM_S08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S09:

SRM_S09: Request cancellation of servic/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.9

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S09.SRM_S09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S10:

SRM_S10: Request discontinuation of servic/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.10

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S10.SRM_S10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRM_S11:

SRM_S11: Request deletion of servic/resource on appointment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 10.2.11

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S11.SRM_S11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - R
     - ARQ
   * - ``APR``
     - :ref:`APR <hl7-v2_3-APR>`
     - O
     - APR
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_3-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - list[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]
     - O
     - PATIENT
   * - ``RESOURCES``
     - list[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - R
     - RESOURCES

.. _hl7-v2_3-SRR_S01:

SRR_S01: Request new appointment booking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRR_S01.SRR_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``SCHEDULE``
     - :ref:`SRR_S01_SCHEDULE <hl7-v2_3-SRR_S01_SCHEDULE>`
     - O
     - SCHEDULE

.. _hl7-v2_3-SUR_P09:

SUR_P09: SUR - Summary product experience report
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SUR_P09.SUR_P09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``FACILITY``
     - list[:ref:`SUR_P09_FACILITY <hl7-v2_3-SUR_P09_FACILITY>`]
     - R
     - FACILITY

.. _hl7-v2_3-TBR_Q01:

TBR_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.TBR_Q01.TBR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_3-ERR>`
     - O
     - ERR
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - R
     - QAK
   * - ``RDF``
     - :ref:`RDF <hl7-v2_3-RDF>`
     - R
     - RDF
   * - ``RDT``
     - list[:ref:`RDT <hl7-v2_3-RDT>`]
     - R
     - RDT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-UDM_Q05:

UDM_Q05: Unsolicited display update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``URD``
     - :ref:`URD <hl7-v2_3-URD>`
     - R
     - URD
   * - ``URS``
     - :ref:`URS <hl7-v2_3-URS>`
     - O
     - URS
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_3-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-VQQ_Q01:

VQQ_Q01: Query sent for immediate response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VQQ_Q01.VQQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``VTQ``
     - :ref:`VTQ <hl7-v2_3-VTQ>`
     - R
     - VTQ
   * - ``RDF``
     - :ref:`RDF <hl7-v2_3-RDF>`
     - O
     - RDF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_3-DSC>`
     - O
     - DSC

.. _hl7-v2_3-VXQ_V01:

VXQ_V01: VXQ - Query for vaccination record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXQ_V01.VXQ_V01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF

.. _hl7-v2_3-VXR_V03:

VXR_V03: VXR - Vaccination record response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXR_V03.VXR_V03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PATIENT_VISIT``
     - :ref:`VXR_V03_PATIENT_VISIT <hl7-v2_3-VXR_V03_PATIENT_VISIT>`
     - O
     - PATIENT_VISIT
   * - ``INSURANCE``
     - list[:ref:`VXR_V03_INSURANCE <hl7-v2_3-VXR_V03_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ORDER``
     - list[:ref:`VXR_V03_ORDER <hl7-v2_3-VXR_V03_ORDER>`]
     - O
     - ORDER

.. _hl7-v2_3-VXU_V04:

VXU_V04: VXU - Unsolicited vaccination record update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXU_V04.VXU_V04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - R
     - PID
   * - ``PD1``
     - :ref:`PD1 <hl7-v2_3-PD1>`
     - O
     - PD1
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_3-NK1>`]
     - O
     - NK1
   * - ``PATIENT``
     - :ref:`VXU_V04_PATIENT <hl7-v2_3-VXU_V04_PATIENT>`
     - O
     - PATIENT
   * - ``INSURANCE``
     - list[:ref:`VXU_V04_INSURANCE <hl7-v2_3-VXU_V04_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ORDER``
     - list[:ref:`VXU_V04_ORDER <hl7-v2_3-VXU_V04_ORDER>`]
     - O
     - ORDER

.. _hl7-v2_3-VXX_V02:

VXX_V02: VXX - Response to vaccination query returning multiple PID matches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXX_V02.VXX_V02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - R
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - O
     - QRF
   * - ``PATIENT``
     - list[:ref:`VXX_V02_PATIENT <hl7-v2_3-VXX_V02_PATIENT>`]
     - R
     - PATIENT
