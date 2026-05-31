v2.2 Messages
=============

.. _hl7-v2_2-ACK:

.. py:class:: hl7types.hl7.v2_2.messages.ACK.ACK
   :noindex:

   HL7 v2 ACK message.

ACK
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional

.. _hl7-v2_2-ADR_A19:

.. py:class:: hl7types.hl7.v2_2.messages.ADR_A19.ADR_A19
   :noindex:

   HL7 v2 ADR_A19 message.

ADR_A19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_2-ADR_A19_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-ADT_A01:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A01.ADT_A01
   :noindex:

   HL7 v2 ADT_A01 message.

ADT_A01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_2-ADT_A01_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A02:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A02.ADT_A02
   :noindex:

   HL7 v2 ADT_A02 message.

ADT_A02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A03:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A03.ADT_A03
   :noindex:

   HL7 v2 ADT_A03 message.

ADT_A03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A04:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A04.ADT_A04
   :noindex:

   HL7 v2 ADT_A04 message.

ADT_A04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A04_INSURANCE <hl7-v2_2-ADT_A04_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A05:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A05.ADT_A05
   :noindex:

   HL7 v2 ADT_A05 message.

ADT_A05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_2-ADT_A05_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A06:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A06.ADT_A06
   :noindex:

   HL7 v2 ADT_A06 message.

ADT_A06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``MRG``
     -
     - Optional[:ref:`MRG <hl7-v2_2-MRG>`]
     - optional
     -
     - MRG: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_2-ADT_A06_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A07:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A07.ADT_A07
   :noindex:

   HL7 v2 ADT_A07 message.

ADT_A07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``MRG``
     -
     - Optional[:ref:`MRG <hl7-v2_2-MRG>`]
     - optional
     -
     - MRG: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A07_INSURANCE <hl7-v2_2-ADT_A07_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A08:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A08.ADT_A08
   :noindex:

   HL7 v2 ADT_A08 message.

ADT_A08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A08_INSURANCE <hl7-v2_2-ADT_A08_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A09:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A09.ADT_A09
   :noindex:

   HL7 v2 ADT_A09 message.

ADT_A09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_2-ADT_A10:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A10.ADT_A10
   :noindex:

   HL7 v2 ADT_A10 message.

ADT_A10
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_2-ADT_A11:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A11.ADT_A11
   :noindex:

   HL7 v2 ADT_A11 message.

ADT_A11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_2-ADT_A12:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A12.ADT_A12
   :noindex:

   HL7 v2 ADT_A12 message.

ADT_A12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_2-ADT_A13:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A13.ADT_A13
   :noindex:

   HL7 v2 ADT_A13 message.

ADT_A13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A13_INSURANCE <hl7-v2_2-ADT_A13_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A14:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A14.ADT_A14
   :noindex:

   HL7 v2 ADT_A14 message.

ADT_A14
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A14_INSURANCE <hl7-v2_2-ADT_A14_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A15:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A15.ADT_A15
   :noindex:

   HL7 v2 ADT_A15 message.

ADT_A15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_2-ADT_A16:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A16.ADT_A16
   :noindex:

   HL7 v2 ADT_A16 message.

ADT_A16
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_2-ADT_A17:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A17.ADT_A17
   :noindex:

   HL7 v2 ADT_A17 message.

ADT_A17
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A18:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A18.ADT_A18
   :noindex:

   HL7 v2 ADT_A18 message.

ADT_A18
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``MRG``
     -
     - Optional[:ref:`MRG <hl7-v2_2-MRG>`]
     - optional
     -
     - MRG: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required

.. _hl7-v2_2-ADT_A20:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A20.ADT_A20
   :noindex:

   HL7 v2 ADT_A20 message.

ADT_A20
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``NPU``
     -
     - :ref:`NPU <hl7-v2_2-NPU>`
     - required
     -
     - NPU: Required

.. _hl7-v2_2-ADT_A21:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A21.ADT_A21
   :noindex:

   HL7 v2 ADT_A21 message.

ADT_A21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A22:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A22.ADT_A22
   :noindex:

   HL7 v2 ADT_A22 message.

ADT_A22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A23:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A23.ADT_A23
   :noindex:

   HL7 v2 ADT_A23 message.

ADT_A23
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A24:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A24.ADT_A24
   :noindex:

   HL7 v2 ADT_A24 message.

ADT_A24
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_2-PV1>`]
     - optional
     -
     - PV1: Optional

.. _hl7-v2_2-ADT_A25:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A25.ADT_A25
   :noindex:

   HL7 v2 ADT_A25 message.

ADT_A25
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A26:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A26.ADT_A26
   :noindex:

   HL7 v2 ADT_A26 message.

ADT_A26
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A27:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A27.ADT_A27
   :noindex:

   HL7 v2 ADT_A27 message.

ADT_A27
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A28:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A28.ADT_A28
   :noindex:

   HL7 v2 ADT_A28 message.

ADT_A28
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A28_INSURANCE <hl7-v2_2-ADT_A28_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A29:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A29.ADT_A29
   :noindex:

   HL7 v2 ADT_A29 message.

ADT_A29
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A30:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A30.ADT_A30
   :noindex:

   HL7 v2 ADT_A30 message.

ADT_A30
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     -
     - MRG: Required

.. _hl7-v2_2-ADT_A31:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A31.ADT_A31
   :noindex:

   HL7 v2 ADT_A31 message.

ADT_A31
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_2-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_2-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_2-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PR1``
     -
     - Optional[List[:ref:`PR1 <hl7-v2_2-PR1>`]]
     - optional
     -
     - PR1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_2-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A31_INSURANCE <hl7-v2_2-ADT_A31_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_2-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_2-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_2-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_2-ADT_A32:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A32.ADT_A32
   :noindex:

   HL7 v2 ADT_A32 message.

ADT_A32
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A33:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A33.ADT_A33
   :noindex:

   HL7 v2 ADT_A33 message.

ADT_A33
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_2-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_2-ADT_A34:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A34.ADT_A34
   :noindex:

   HL7 v2 ADT_A34 message.

ADT_A34
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     -
     - MRG: Required

.. _hl7-v2_2-ADT_A35:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A35.ADT_A35
   :noindex:

   HL7 v2 ADT_A35 message.

ADT_A35
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     -
     - MRG: Required

.. _hl7-v2_2-ADT_A36:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A36.ADT_A36
   :noindex:

   HL7 v2 ADT_A36 message.

ADT_A36
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_2-MRG>`
     - required
     -
     - MRG: Required

.. _hl7-v2_2-ADT_A37:

.. py:class:: hl7types.hl7.v2_2.messages.ADT_A37.ADT_A37
   :noindex:

   HL7 v2 ADT_A37 message.

ADT_A37
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_2-PV1>`]
     - optional
     -
     - PV1: Optional

.. _hl7-v2_2-BAR_P01:

.. py:class:: hl7types.hl7.v2_2.messages.BAR_P01.BAR_P01
   :noindex:

   HL7 v2 BAR_P01 message.

BAR_P01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``VISIT``
     -
     - List[:ref:`BAR_P01_VISIT <hl7-v2_2-BAR_P01_VISIT>`]
     - required
     -
     - VISIT: Required, repeating

.. _hl7-v2_2-BAR_P02:

.. py:class:: hl7types.hl7.v2_2.messages.BAR_P02.BAR_P02
   :noindex:

   HL7 v2 BAR_P02 message.

BAR_P02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_2-BAR_P02_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_2-DFT_P03:

.. py:class:: hl7types.hl7.v2_2.messages.DFT_P03.DFT_P03
   :noindex:

   HL7 v2 DFT_P03 message.

DFT_P03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_2-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_2-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_2-PV1>`]
     - optional
     -
     - PV1: Optional
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_2-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_2-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``FT1``
     -
     - List[:ref:`FT1 <hl7-v2_2-FT1>`]
     - required
     -
     - FT1: Required, repeating

.. _hl7-v2_2-DSR_P04:

.. py:class:: hl7types.hl7.v2_2.messages.DSR_P04.DSR_P04
   :noindex:

   HL7 v2 DSR_P04 message.

DSR_P04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-DSR_Q01:

.. py:class:: hl7types.hl7.v2_2.messages.DSR_Q01.DSR_Q01
   :noindex:

   HL7 v2 DSR_Q01 message.

DSR_Q01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-DSR_Q03:

.. py:class:: hl7types.hl7.v2_2.messages.DSR_Q03.DSR_Q03
   :noindex:

   HL7 v2 DSR_Q03 message.

DSR_Q03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - Optional[:ref:`MSA <hl7-v2_2-MSA>`]
     - optional
     -
     - MSA: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-DSR_R03:

.. py:class:: hl7types.hl7.v2_2.messages.DSR_R03.DSR_R03
   :noindex:

   HL7 v2 DSR_R03 message.

DSR_R03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - Optional[:ref:`MSA <hl7-v2_2-MSA>`]
     - optional
     -
     - MSA: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-MFD_M01:

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M01.MFD_M01
   :noindex:

   HL7 v2 MFD_M01 message.

MFD_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_2-MFD_M02:

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M02.MFD_M02
   :noindex:

   HL7 v2 MFD_M02 message.

MFD_M02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_2-MFD_M03:

.. py:class:: hl7types.hl7.v2_2.messages.MFD_M03.MFD_M03
   :noindex:

   HL7 v2 MFD_M03 message.

MFD_M03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_2-MFK_M01:

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M01.MFK_M01
   :noindex:

   HL7 v2 MFK_M01 message.

MFK_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_2-MFK_M02:

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M02.MFK_M02
   :noindex:

   HL7 v2 MFK_M02 message.

MFK_M02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_2-MFK_M03:

.. py:class:: hl7types.hl7.v2_2.messages.MFK_M03.MFK_M03
   :noindex:

   HL7 v2 MFK_M03 message.

MFK_M03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_2-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_2-MFN_M01:

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M01.MFN_M01
   :noindex:

   HL7 v2 MFN_M01 message.

MFN_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF``
     -
     - List[:ref:`MFN_M01_MF <hl7-v2_2-MFN_M01_MF>`]
     - required
     -
     - MF: Required, repeating

.. _hl7-v2_2-MFN_M02:

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M02.MFN_M02
   :noindex:

   HL7 v2 MFN_M02 message.

MFN_M02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_STAFF``
     -
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_2-MFN_M02_MF_STAFF>`]
     - required
     -
     - MF_STAFF: Required, repeating

.. _hl7-v2_2-MFN_M03:

.. py:class:: hl7types.hl7.v2_2.messages.MFN_M03.MFN_M03
   :noindex:

   HL7 v2 MFN_M03 message.

MFN_M03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST``
     -
     - List[:ref:`MFN_M03_MF_TEST <hl7-v2_2-MFN_M03_MF_TEST>`]
     - required
     -
     - MF_TEST: Required, repeating

.. _hl7-v2_2-MFQ_M01:

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M01.MFQ_M01
   :noindex:

   HL7 v2 MFQ_M01 message.

MFQ_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-MFQ_M02:

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M02.MFQ_M02
   :noindex:

   HL7 v2 MFQ_M02 message.

MFQ_M02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-MFQ_M03:

.. py:class:: hl7types.hl7.v2_2.messages.MFQ_M03.MFQ_M03
   :noindex:

   HL7 v2 MFQ_M03 message.

MFQ_M03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-MFR_M01:

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M01.MFR_M01
   :noindex:

   HL7 v2 MFR_M01 message.

MFR_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF``
     -
     - List[:ref:`MFR_M01_MF <hl7-v2_2-MFR_M01_MF>`]
     - required
     -
     - MF: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-MFR_M02:

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M02.MFR_M02
   :noindex:

   HL7 v2 MFR_M02 message.

MFR_M02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_STAFF``
     -
     - List[:ref:`MFR_M02_MF_STAFF <hl7-v2_2-MFR_M02_MF_STAFF>`]
     - required
     -
     - MF_STAFF: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-MFR_M03:

.. py:class:: hl7types.hl7.v2_2.messages.MFR_M03.MFR_M03
   :noindex:

   HL7 v2 MFR_M03 message.

MFR_M03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_2-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST``
     -
     - List[:ref:`MFR_M03_MF_TEST <hl7-v2_2-MFR_M03_MF_TEST>`]
     - required
     -
     - MF_TEST: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-NMD_N01:

.. py:class:: hl7types.hl7.v2_2.messages.NMD_N01.NMD_N01
   :noindex:

   HL7 v2 NMD_N01 message.

NMD_N01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     -
     - List[:ref:`NMD_N01_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_2-NMD_N01_CLOCK_AND_STATS_WITH_NOTES>`]
     - required
     -
     - CLOCK_AND_STATS_WITH_NOTES: Required, repeating

.. _hl7-v2_2-NMQ_N02:

.. py:class:: hl7types.hl7.v2_2.messages.NMQ_N02.NMQ_N02
   :noindex:

   HL7 v2 NMQ_N02 message.

NMQ_N02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRY_WITH_DETAIL``
     -
     - Optional[:ref:`NMQ_N02_QRY_WITH_DETAIL <hl7-v2_2-NMQ_N02_QRY_WITH_DETAIL>`]
     - optional
     -
     - QRY_WITH_DETAIL: Optional
   * - ``CLOCK_AND_STATISTICS``
     -
     - List[:ref:`NMQ_N02_CLOCK_AND_STATISTICS <hl7-v2_2-NMQ_N02_CLOCK_AND_STATISTICS>`]
     - required
     -
     - CLOCK_AND_STATISTICS: Required, repeating

.. _hl7-v2_2-NMR_N02:

.. py:class:: hl7types.hl7.v2_2.messages.NMR_N02.NMR_N02
   :noindex:

   HL7 v2 NMR_N02 message.

NMR_N02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_2-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - Optional[:ref:`QRD <hl7-v2_2-QRD>`]
     - optional
     -
     - QRD: Optional
   * - ``CLOCK_AND_STATS_WITH_NOTES_ALT``
     -
     - List[:ref:`NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT <hl7-v2_2-NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT>`]
     - required
     -
     - CLOCK_AND_STATS_WITH_NOTES_ALT: Required, repeating

.. _hl7-v2_2-ORF_R04:

.. py:class:: hl7types.hl7.v2_2.messages.ORF_R04.ORF_R04
   :noindex:

   HL7 v2 ORF_R04 message.

ORF_R04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`ORF_R04_QUERY_RESPONSE <hl7-v2_2-ORF_R04_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``ORDER``
     -
     - List[:ref:`ORF_R04_ORDER <hl7-v2_2-ORF_R04_ORDER>`]
     - required
     -
     - ORDER: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-ORM_O01:

.. py:class:: hl7types.hl7.v2_2.messages.ORM_O01.ORM_O01
   :noindex:

   HL7 v2 ORM_O01 message.

ORM_O01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_2-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_2-ORM_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`ORM_O01_ORDER <hl7-v2_2-ORM_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_2-ORR_O02:

.. py:class:: hl7types.hl7.v2_2.messages.ORR_O02.ORR_O02
   :noindex:

   HL7 v2 ORR_O02 message.

ORR_O02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_2-MSA>`
     - required
     -
     - MSA: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_2-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`ORR_O02_PATIENT <hl7-v2_2-ORR_O02_PATIENT>`]
     - optional
     -
     - PATIENT: Optional

.. _hl7-v2_2-ORU_R01:

.. py:class:: hl7types.hl7.v2_2.messages.ORU_R01.ORU_R01
   :noindex:

   HL7 v2 ORU_R01 message.

ORU_R01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``PATIENT_RESULT``
     -
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_2-ORU_R01_PATIENT_RESULT>`]
     - required
     -
     - PATIENT_RESULT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-QRY_A19:

.. py:class:: hl7types.hl7.v2_2.messages.QRY_A19.QRY_A19
   :noindex:

   HL7 v2 QRY_A19 message.

QRY_A19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional

.. _hl7-v2_2-QRY_P04:

.. py:class:: hl7types.hl7.v2_2.messages.QRY_P04.QRY_P04
   :noindex:

   HL7 v2 QRY_P04 message.

QRY_P04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-QRY_Q01:

.. py:class:: hl7types.hl7.v2_2.messages.QRY_Q01.QRY_Q01
   :noindex:

   HL7 v2 QRY_Q01 message.

QRY_Q01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-QRY_Q02:

.. py:class:: hl7types.hl7.v2_2.messages.QRY_Q02.QRY_Q02
   :noindex:

   HL7 v2 QRY_Q02 message.

QRY_Q02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_2-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-QRY_R02:

.. py:class:: hl7types.hl7.v2_2.messages.QRY_R02.QRY_R02
   :noindex:

   HL7 v2 QRY_R02 message.

QRY_R02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_2-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - :ref:`QRF <hl7-v2_2-QRF>`
     - required
     -
     - QRF: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_2-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_2-UDM_Q05:

.. py:class:: hl7types.hl7.v2_2.messages.UDM_Q05.UDM_Q05
   :noindex:

   HL7 v2 UDM_Q05 message.

UDM_Q05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_2-MSH>`
     - required
     -
     - MSH: Required
   * - ``URD``
     -
     - :ref:`URD <hl7-v2_2-URD>`
     - required
     -
     - URD: Required
   * - ``URS``
     -
     - Optional[:ref:`URS <hl7-v2_2-URS>`]
     - optional
     -
     - URS: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_2-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_2-DSC>`
     - required
     -
     - DSC: Required
