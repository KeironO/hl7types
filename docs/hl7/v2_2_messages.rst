v2.2 Messages
=============

.. _hl7-v2_2-ACK:

ACK: General acknowledgment message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR

.. _hl7-v2_2-ADR_A19:

ADR_A19: HL7 v2 ADR_A19 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADR_A19.ADR_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QUERY_RESPONSE``
     - list[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_2-ADR_A19_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-ADT_A01:

ADT_A01: HL7 v2 ADT_A01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A01_INSURANCE <hl7-v2_2-ADT_A01_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A02:

ADT_A02: HL7 v2 ADT_A02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A03:

ADT_A03: HL7 v2 ADT_A03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A04:

ADT_A04: HL7 v2 ADT_A04 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A04_INSURANCE <hl7-v2_2-ADT_A04_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A05:

ADT_A05: HL7 v2 ADT_A05 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A05_INSURANCE <hl7-v2_2-ADT_A05_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A06:

ADT_A06: HL7 v2 ADT_A06 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A06_INSURANCE <hl7-v2_2-ADT_A06_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A07:

ADT_A07: HL7 v2 ADT_A07 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - O
     - MRG
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A07_INSURANCE <hl7-v2_2-ADT_A07_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A08:

ADT_A08: HL7 v2 ADT_A08 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A08_INSURANCE <hl7-v2_2-ADT_A08_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A09:

ADT_A09: HL7 v2 ADT_A09 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1

.. _hl7-v2_2-ADT_A10:

ADT_A10: HL7 v2 ADT_A10 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1

.. _hl7-v2_2-ADT_A11:

ADT_A11: HL7 v2 ADT_A11 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1

.. _hl7-v2_2-ADT_A12:

ADT_A12: HL7 v2 ADT_A12 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1

.. _hl7-v2_2-ADT_A13:

ADT_A13: HL7 v2 ADT_A13 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A13_INSURANCE <hl7-v2_2-ADT_A13_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A14:

ADT_A14: HL7 v2 ADT_A14 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A14_INSURANCE <hl7-v2_2-ADT_A14_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A15:

ADT_A15: HL7 v2 ADT_A15 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1

.. _hl7-v2_2-ADT_A16:

ADT_A16: HL7 v2 ADT_A16 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1

.. _hl7-v2_2-ADT_A17:

ADT_A17: HL7 v2 ADT_A17 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A18:

ADT_A18: HL7 v2 ADT_A18 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A18.ADT_A18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - O
     - MRG
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1

.. _hl7-v2_2-ADT_A20:

ADT_A20: HL7 v2 ADT_A20 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``NPU``
     - :ref:`NPU <hl7-v2_2-NPU>`
     - R
     - NPU

.. _hl7-v2_2-ADT_A21:

ADT_A21: HL7 v2 ADT_A21 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A22:

ADT_A22: HL7 v2 ADT_A22 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A22.ADT_A22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A23:

ADT_A23: HL7 v2 ADT_A23 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A23.ADT_A23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A24:

ADT_A24: HL7 v2 ADT_A24 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - O
     - PV1

.. _hl7-v2_2-ADT_A25:

ADT_A25: HL7 v2 ADT_A25 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A25.ADT_A25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A26:

ADT_A26: HL7 v2 ADT_A26 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A26.ADT_A26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A27:

ADT_A27: HL7 v2 ADT_A27 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A27.ADT_A27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A28:

ADT_A28: HL7 v2 ADT_A28 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A28_INSURANCE <hl7-v2_2-ADT_A28_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A29:

ADT_A29: HL7 v2 ADT_A29 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A29.ADT_A29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A30:

ADT_A30: HL7 v2 ADT_A30 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A30.ADT_A30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - R
     - MRG

.. _hl7-v2_2-ADT_A31:

ADT_A31: HL7 v2 ADT_A31 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``NK1``
     - list[:ref:`NK1 <hl7-v2_2-NK1>`]
     - O
     - NK1
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``AL1``
     - list[:ref:`AL1 <hl7-v2_2-AL1>`]
     - O
     - AL1
   * - ``DG1``
     - list[:ref:`DG1 <hl7-v2_2-DG1>`]
     - O
     - DG1
   * - ``PR1``
     - list[:ref:`PR1 <hl7-v2_2-PR1>`]
     - O
     - PR1
   * - ``GT1``
     - list[:ref:`GT1 <hl7-v2_2-GT1>`]
     - O
     - GT1
   * - ``INSURANCE``
     - list[:ref:`ADT_A31_INSURANCE <hl7-v2_2-ADT_A31_INSURANCE>`]
     - O
     - INSURANCE
   * - ``ACC``
     - :ref:`ACC <hl7-v2_2-ACC>`
     - O
     - ACC
   * - ``UB1``
     - :ref:`UB1 <hl7-v2_2-UB1>`
     - O
     - UB1
   * - ``UB2``
     - :ref:`UB2 <hl7-v2_2-UB2>`
     - O
     - UB2

.. _hl7-v2_2-ADT_A32:

ADT_A32: HL7 v2 ADT_A32 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A32.ADT_A32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A33:

ADT_A33: HL7 v2 ADT_A33 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A33.ADT_A33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - R
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX

.. _hl7-v2_2-ADT_A34:

ADT_A34: HL7 v2 ADT_A34 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A34.ADT_A34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - R
     - MRG

.. _hl7-v2_2-ADT_A35:

ADT_A35: HL7 v2 ADT_A35 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A35.ADT_A35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - R
     - MRG

.. _hl7-v2_2-ADT_A36:

ADT_A36: HL7 v2 ADT_A36 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A36.ADT_A36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``MRG``
     - :ref:`MRG <hl7-v2_2-MRG>`
     - R
     - MRG

.. _hl7-v2_2-ADT_A37:

ADT_A37: HL7 v2 ADT_A37 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - O
     - PV1

.. _hl7-v2_2-BAR_P01:

BAR_P01: HL7 v2 BAR_P01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``VISIT``
     - list[:ref:`BAR_P01_VISIT <hl7-v2_2-BAR_P01_VISIT>`]
     - R
     - VISIT

.. _hl7-v2_2-BAR_P02:

BAR_P02: HL7 v2 BAR_P02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PATIENT``
     - list[:ref:`BAR_P02_PATIENT <hl7-v2_2-BAR_P02_PATIENT>`]
     - R
     - PATIENT

.. _hl7-v2_2-DFT_P03:

DFT_P03: HL7 v2 DFT_P03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``EVN``
     - :ref:`EVN <hl7-v2_2-EVN>`
     - R
     - EVN
   * - ``PID``
     - :ref:`PID <hl7-v2_2-PID>`
     - R
     - PID
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - O
     - PV1
   * - ``PV2``
     - :ref:`PV2 <hl7-v2_2-PV2>`
     - O
     - PV2
   * - ``OBX``
     - list[:ref:`OBX <hl7-v2_2-OBX>`]
     - O
     - OBX
   * - ``FT1``
     - list[:ref:`FT1 <hl7-v2_2-FT1>`]
     - R
     - FT1

.. _hl7-v2_2-DSR_P04:

DSR_P04: HL7 v2 DSR_P04 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_P04.DSR_P04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_2-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-DSR_Q01:

DSR_Q01: HL7 v2 DSR_Q01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_Q01.DSR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_2-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-DSR_Q03:

DSR_Q03: HL7 v2 DSR_Q03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_Q03.DSR_Q03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - O
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_2-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-DSR_R03:

DSR_R03: HL7 v2 DSR_R03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.DSR_R03.DSR_R03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - O
     - MSA
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_2-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-MFD_M01:

MFD_M01: HL7 v2 MFD_M01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M01.MFD_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_2-MFA>`]
     - O
     - MFA

.. _hl7-v2_2-MFD_M02:

MFD_M02: HL7 v2 MFD_M02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M02.MFD_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_2-MFA>`]
     - O
     - MFA

.. _hl7-v2_2-MFD_M03:

MFD_M03: HL7 v2 MFD_M03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M03.MFD_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_2-MFA>`]
     - O
     - MFA

.. _hl7-v2_2-MFK_M01:

MFK_M01: HL7 v2 MFK_M01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_2-MFA>`]
     - O
     - MFA

.. _hl7-v2_2-MFK_M02:

MFK_M02: HL7 v2 MFK_M02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M02.MFK_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_2-MFA>`]
     - O
     - MFA

.. _hl7-v2_2-MFK_M03:

MFK_M03: HL7 v2 MFK_M03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M03.MFK_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MFA``
     - list[:ref:`MFA <hl7-v2_2-MFA>`]
     - O
     - MFA

.. _hl7-v2_2-MFN_M01:

MFN_M01: HL7 v2 MFN_M01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M01.MFN_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MF``
     - list[:ref:`MFN_M01_MF <hl7-v2_2-MFN_M01_MF>`]
     - R
     - MF

.. _hl7-v2_2-MFN_M02:

MFN_M02: HL7 v2 MFN_M02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MF_STAFF``
     - list[:ref:`MFN_M02_MF_STAFF <hl7-v2_2-MFN_M02_MF_STAFF>`]
     - R
     - MF_STAFF

.. _hl7-v2_2-MFN_M03:

MFN_M03: HL7 v2 MFN_M03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M03.MFN_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MF_TEST``
     - list[:ref:`MFN_M03_MF_TEST <hl7-v2_2-MFN_M03_MF_TEST>`]
     - R
     - MF_TEST

.. _hl7-v2_2-MFQ_M01:

MFQ_M01: HL7 v2 MFQ_M01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M01.MFQ_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-MFQ_M02:

MFQ_M02: HL7 v2 MFQ_M02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M02.MFQ_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-MFQ_M03:

MFQ_M03: HL7 v2 MFQ_M03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M03.MFQ_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-MFR_M01:

MFR_M01: HL7 v2 MFR_M01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M01.MFR_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MF``
     - list[:ref:`MFR_M01_MF <hl7-v2_2-MFR_M01_MF>`]
     - R
     - MF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-MFR_M02:

MFR_M02: HL7 v2 MFR_M02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M02.MFR_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MF_STAFF``
     - list[:ref:`MFR_M02_MF_STAFF <hl7-v2_2-MFR_M02_MF_STAFF>`]
     - R
     - MF_STAFF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-MFR_M03:

MFR_M03: HL7 v2 MFR_M03 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M03.MFR_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``MFI``
     - :ref:`MFI <hl7-v2_2-MFI>`
     - R
     - MFI
   * - ``MF_TEST``
     - list[:ref:`MFR_M03_MF_TEST <hl7-v2_2-MFR_M03_MF_TEST>`]
     - R
     - MF_TEST
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-NMD_N01:

NMD_N01: HL7 v2 NMD_N01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.NMD_N01.NMD_N01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     - list[:ref:`NMD_N01_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_2-NMD_N01_CLOCK_AND_STATS_WITH_NOTES>`]
     - R
     - CLOCK_AND_STATS_WITH_NOTES

.. _hl7-v2_2-NMQ_N02:

NMQ_N02: HL7 v2 NMQ_N02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.NMQ_N02.NMQ_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRY_WITH_DETAIL``
     - :ref:`NMQ_N02_QRY_WITH_DETAIL <hl7-v2_2-NMQ_N02_QRY_WITH_DETAIL>`
     - O
     - QRY_WITH_DETAIL
   * - ``CLOCK_AND_STATISTICS``
     - list[:ref:`NMQ_N02_CLOCK_AND_STATISTICS <hl7-v2_2-NMQ_N02_CLOCK_AND_STATISTICS>`]
     - R
     - CLOCK_AND_STATISTICS

.. _hl7-v2_2-NMR_N02:

NMR_N02: HL7 v2 NMR_N02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.NMR_N02.NMR_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``ERR``
     - :ref:`ERR <hl7-v2_2-ERR>`
     - O
     - ERR
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - O
     - QRD
   * - ``CLOCK_AND_STATS_WITH_NOTES_ALT``
     - list[:ref:`NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT <hl7-v2_2-NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT>`]
     - R
     - CLOCK_AND_STATS_WITH_NOTES_ALT

.. _hl7-v2_2-ORF_R04:

ORF_R04: HL7 v2 ORF_R04 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORF_R04.ORF_R04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``QUERY_RESPONSE``
     - list[:ref:`ORF_R04_QUERY_RESPONSE <hl7-v2_2-ORF_R04_QUERY_RESPONSE>`]
     - R
     - QUERY_RESPONSE
   * - ``ORDER``
     - list[:ref:`ORF_R04_ORDER <hl7-v2_2-ORF_R04_ORDER>`]
     - R
     - ORDER
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-ORM_O01:

ORM_O01: HL7 v2 ORM_O01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORM_O01.ORM_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_2-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`ORM_O01_PATIENT <hl7-v2_2-ORM_O01_PATIENT>`
     - O
     - PATIENT
   * - ``ORDER``
     - list[:ref:`ORM_O01_ORDER <hl7-v2_2-ORM_O01_ORDER>`]
     - R
     - ORDER

.. _hl7-v2_2-ORR_O02:

ORR_O02: HL7 v2 ORR_O02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORR_O02.ORR_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``MSA``
     - :ref:`MSA <hl7-v2_2-MSA>`
     - R
     - MSA
   * - ``NTE``
     - list[:ref:`NTE <hl7-v2_2-NTE>`]
     - O
     - NTE
   * - ``PATIENT``
     - :ref:`ORR_O02_PATIENT <hl7-v2_2-ORR_O02_PATIENT>`
     - O
     - PATIENT

.. _hl7-v2_2-ORU_R01:

ORU_R01: HL7 v2 ORU_R01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``PATIENT_RESULT``
     - list[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_2-ORU_R01_PATIENT_RESULT>`]
     - R
     - PATIENT_RESULT
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-QRY_A19:

QRY_A19: HL7 v2 QRY_A19 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_A19.QRY_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF

.. _hl7-v2_2-QRY_P04:

QRY_P04: HL7 v2 QRY_P04 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_P04.QRY_P04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-QRY_Q01:

QRY_Q01: HL7 v2 QRY_Q01 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_Q01.QRY_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-QRY_Q02:

QRY_Q02: HL7 v2 QRY_Q02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_Q02.QRY_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - O
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-QRY_R02:

QRY_R02: HL7 v2 QRY_R02 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.QRY_R02.QRY_R02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``QRD``
     - :ref:`QRD <hl7-v2_2-QRD>`
     - R
     - QRD
   * - ``QRF``
     - :ref:`QRF <hl7-v2_2-QRF>`
     - R
     - QRF
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - O
     - DSC

.. _hl7-v2_2-UDM_Q05:

UDM_Q05: HL7 v2 UDM_Q05 message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_2.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - OPT
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_2-MSH>`
     - R
     - MSH
   * - ``URD``
     - :ref:`URD <hl7-v2_2-URD>`
     - R
     - URD
   * - ``URS``
     - :ref:`URS <hl7-v2_2-URS>`
     - O
     - URS
   * - ``DSP``
     - list[:ref:`DSP <hl7-v2_2-DSP>`]
     - R
     - DSP
   * - ``DSC``
     - :ref:`DSC <hl7-v2_2-DSC>`
     - R
     - DSC
