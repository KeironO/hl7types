v2.3 Messages
=============

.. _hl7-v2_3-ACK:

.. py:class:: hl7types.hl7.v2_3.messages.ACK.ACK
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional

.. _hl7-v2_3-ADT_A01:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A01.ADT_A01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_3-ADT_A02:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A02.ADT_A02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_3-ADT_A03:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A03.ADT_A03
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A03_PROCEDURE <hl7-v2_3-ADT_A03_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_3-ADT_A06:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A06.ADT_A06
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``MRG``
     -
     - Optional[:ref:`MRG <hl7-v2_3-MRG>`]
     - optional
     -
     - MRG: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_3-ADT_A06_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_3-ADT_A06_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_3-ADT_A09:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A09.ADT_A09
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_3-ADT_A12:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A12.ADT_A12
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_3-DG1>`]
     - optional
     -
     - DG1: Optional

.. _hl7-v2_3-ADT_A16:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A16.ADT_A16
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_3-DG1>`]
     - optional
     -
     - DG1: Optional
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     -
     - DRG: Optional

.. _hl7-v2_3-ADT_A17:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A17.ADT_A17
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_3-ADT_A18:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A18.ADT_A18
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``MRG``
     -
     - Optional[:ref:`MRG <hl7-v2_3-MRG>`]
     - optional
     -
     - MRG: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required

.. _hl7-v2_3-ADT_A20:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A20.ADT_A20
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``NPU``
     -
     - :ref:`NPU <hl7-v2_3-NPU>`
     - required
     -
     - NPU: Required

.. _hl7-v2_3-ADT_A24:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A24.ADT_A24
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     -
     - PV1: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating

.. _hl7-v2_3-ADT_A30:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A30.ADT_A30
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     -
     - MRG: Required

.. _hl7-v2_3-ADT_A38:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A38.ADT_A38
   :noindex:

   HL7 v2 ADT_A38 message.

ADT_A38
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     -
     - DRG: Optional

.. _hl7-v2_3-ADT_A39:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A39.ADT_A39
   :noindex:

   HL7 v2 ADT_A39 message.

ADT_A39
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-ADT_A43:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A43.ADT_A43
   :noindex:

   HL7 v2 ADT_A43 message.

ADT_A43
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_3-ADT_A43_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-ADT_A45:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A45.ADT_A45
   :noindex:

   HL7 v2 ADT_A45 message.

ADT_A45
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``MERGE_INFO``
     -
     - List[:ref:`ADT_A45_MERGE_INFO <hl7-v2_3-ADT_A45_MERGE_INFO>`]
     - required
     -
     - MERGE_INFO: Required, repeating

.. _hl7-v2_3-ADT_A50:

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A50.ADT_A50
   :noindex:

   HL7 v2 ADT_A50 message.

ADT_A50
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     -
     - MRG: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required

.. _hl7-v2_3-ARD_A19:

.. py:class:: hl7types.hl7.v2_3.messages.ARD_A19.ARD_A19
   :noindex:

   HL7 v2 ARD_A19 message.

ARD_A19
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`ARD_A19_QUERY_RESPONSE <hl7-v2_3-ARD_A19_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-BAR_P01:

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P01.BAR_P01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``VISIT``
     -
     - List[:ref:`BAR_P01_VISIT <hl7-v2_3-BAR_P01_VISIT>`]
     - required
     -
     - VISIT: Required, repeating

.. _hl7-v2_3-BAR_P02:

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P02.BAR_P02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_3-BAR_P02_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-BAR_P06:

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P06.BAR_P06
   :noindex:

   HL7 v2 BAR_P06 message.

BAR_P06
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P06_PATIENT <hl7-v2_3-BAR_P06_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-CRM_C01:

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C01.CRM_C01
   :noindex:

   HL7 v2 CRM_C01 message.

CRM_C01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PATIENT``
     -
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-CSU_C09:

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C09.CSU_C09
   :noindex:

   HL7 v2 CSU_C09 message.

CSU_C09
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PATIENT``
     -
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-DFT_P03:

.. py:class:: hl7types.hl7.v2_3.messages.DFT_P03.DFT_P03
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     -
     - PV1: Optional
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``FINANCIAL``
     -
     - List[:ref:`DFT_P03_FINANCIAL <hl7-v2_3-DFT_P03_FINANCIAL>`]
     - required
     -
     - FINANCIAL: Required, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`DFT_P03_INSURANCE <hl7-v2_3-DFT_P03_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     -
     - ACC: Optional

.. _hl7-v2_3-DOC_T12:

.. py:class:: hl7types.hl7.v2_3.messages.DOC_T12.DOC_T12
   :noindex:

   HL7 v2 DOC_T12 message.

DOC_T12
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``RESULT``
     -
     - List[:ref:`DOC_T12_RESULT <hl7-v2_3-DOC_T12_RESULT>`]
     - required
     -
     - RESULT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-DSR_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.DSR_Q01.DSR_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_3-QAK>`]
     - optional
     -
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-DSR_Q03:

.. py:class:: hl7types.hl7.v2_3.messages.DSR_Q03.DSR_Q03
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - Optional[:ref:`MSA <hl7-v2_3-MSA>`]
     - optional
     -
     - MSA: Optional
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_3-QAK>`]
     - optional
     -
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-EDR_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.EDR_Q01.EDR_Q01
   :noindex:

   HL7 v2 EDR_Q01 message.

EDR_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     -
     - QAK: Required
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-EQQ_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.EQQ_Q01.EQQ_Q01
   :noindex:

   HL7 v2 EQQ_Q01 message.

EQQ_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EQL``
     -
     - :ref:`EQL <hl7-v2_3-EQL>`
     - required
     -
     - EQL: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-ERP_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.ERP_Q01.ERP_Q01
   :noindex:

   HL7 v2 ERP_Q01 message.

ERP_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     -
     - QAK: Required
   * - ``ERQ``
     -
     - :ref:`ERQ <hl7-v2_3-ERQ>`
     - required
     -
     - ERQ: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-MDM_T01:

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T01.MDM_T01
   :noindex:

   HL7 v2 MDM_T01 message.

MDM_T01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``TXA``
     -
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     -
     - TXA: Required

.. _hl7-v2_3-MDM_T02:

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T02.MDM_T02
   :noindex:

   HL7 v2 MDM_T02 message.

MDM_T02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     -
     - PV1: Required
   * - ``TXA``
     -
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     -
     - TXA: Required
   * - ``OBX``
     -
     - List[:ref:`OBX <hl7-v2_3-OBX>`]
     - required
     -
     - OBX: Required, repeating

.. _hl7-v2_3-MFK_M01:

.. py:class:: hl7types.hl7.v2_3.messages.MFK_M01.MFK_M01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_3-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_3-MFK_M02:

.. py:class:: hl7types.hl7.v2_3.messages.MFK_M02.MFK_M02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_3-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_3-MFN_M01:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M01.MFN_M01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF``
     -
     - List[:ref:`MFN_M01_MF <hl7-v2_3-MFN_M01_MF>`]
     - required
     -
     - MF: Required, repeating

.. _hl7-v2_3-MFN_M02:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M02.MFN_M02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_STAFF``
     -
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_3-MFN_M02_MF_STAFF>`]
     - required
     -
     - MF_STAFF: Required, repeating

.. _hl7-v2_3-MFN_M03:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M03.MFN_M03
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST``
     -
     - List[:ref:`MFN_M03_MF_TEST <hl7-v2_3-MFN_M03_MF_TEST>`]
     - required
     -
     - MF_TEST: Required, repeating

.. _hl7-v2_3-MFN_M05:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M05.MFN_M05
   :noindex:

   HL7 v2 MFN_M05 message.

MFN_M05
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_LOCATION``
     -
     - List[:ref:`MFN_M05_MF_LOCATION <hl7-v2_3-MFN_M05_MF_LOCATION>`]
     - required
     -
     - MF_LOCATION: Required, repeating

.. _hl7-v2_3-MFN_M06:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M06.MFN_M06
   :noindex:

   HL7 v2 MFN_M06 message.

MFN_M06
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_CDM``
     -
     - List[:ref:`MFN_M06_MF_CDM <hl7-v2_3-MFN_M06_MF_CDM>`]
     - required
     -
     - MF_CDM: Required, repeating

.. _hl7-v2_3-MFN_M07:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M07.MFN_M07
   :noindex:

   HL7 v2 MFN_M07 message.

MFN_M07
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_CLIN_STUDY``
     -
     - List[:ref:`MFN_M07_MF_CLIN_STUDY <hl7-v2_3-MFN_M07_MF_CLIN_STUDY>`]
     - required
     -
     - MF_CLIN_STUDY: Required, repeating

.. _hl7-v2_3-MFN_M08:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M08.MFN_M08
   :noindex:

   HL7 v2 MFN_M08 message.

MFN_M08
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_NUMERIC``
     -
     - List[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_3-MFN_M08_MF_TEST_NUMERIC>`]
     - required
     -
     - MF_TEST_NUMERIC: Required, repeating

.. _hl7-v2_3-MFN_M09:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M09.MFN_M09
   :noindex:

   HL7 v2 MFN_M09 message.

MFN_M09
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_CATEGORICAL``
     -
     - List[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_3-MFN_M09_MF_TEST_CATEGORICAL>`]
     - required
     -
     - MF_TEST_CATEGORICAL: Required, repeating

.. _hl7-v2_3-MFN_M10:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M10.MFN_M10
   :noindex:

   HL7 v2 MFN_M10 message.

MFN_M10
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_BATTERIES``
     -
     - List[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_3-MFN_M10_MF_TEST_BATTERIES>`]
     - required
     -
     - MF_TEST_BATTERIES: Required, repeating

.. _hl7-v2_3-MFN_M11:

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M11.MFN_M11
   :noindex:

   HL7 v2 MFN_M11 message.

MFN_M11
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_CALCULATED``
     -
     - List[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_3-MFN_M11_MF_TEST_CALCULATED>`]
     - required
     -
     - MF_TEST_CALCULATED: Required, repeating

.. _hl7-v2_3-OMD_O01:

.. py:class:: hl7types.hl7.v2_3.messages.OMD_O01.OMD_O01
   :noindex:

   HL7 v2 OMD_O01 message.

OMD_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMD_O01_PATIENT <hl7-v2_3-OMD_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER_DIET``
     -
     - List[:ref:`OMD_O01_ORDER_DIET <hl7-v2_3-OMD_O01_ORDER_DIET>`]
     - required
     -
     - ORDER_DIET: Required, repeating
   * - ``ORDER_TRAY``
     -
     - Optional[List[:ref:`OMD_O01_ORDER_TRAY <hl7-v2_3-OMD_O01_ORDER_TRAY>`]]
     - optional
     -
     - ORDER_TRAY: Optional, repeating

.. _hl7-v2_3-OMN_O01:

.. py:class:: hl7types.hl7.v2_3.messages.OMN_O01.OMN_O01
   :noindex:

   HL7 v2 OMN_O01 message.

OMN_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMN_O01_PATIENT <hl7-v2_3-OMN_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMN_O01_ORDER <hl7-v2_3-OMN_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-OMS_O01:

.. py:class:: hl7types.hl7.v2_3.messages.OMS_O01.OMS_O01
   :noindex:

   HL7 v2 OMS_O01 message.

OMS_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMS_O01_PATIENT <hl7-v2_3-OMS_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMS_O01_ORDER <hl7-v2_3-OMS_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-ORD_O02:

.. py:class:: hl7types.hl7.v2_3.messages.ORD_O02.ORD_O02
   :noindex:

   HL7 v2 ORD_O02 message.

ORD_O02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORD_O02_RESPONSE <hl7-v2_3-ORD_O02_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_3-ORF_R04:

.. py:class:: hl7types.hl7.v2_3.messages.ORF_R04.ORF_R04
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`ORF_R04_QUERY_RESPONSE <hl7-v2_3-ORF_R04_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-ORM_O01:

.. py:class:: hl7types.hl7.v2_3.messages.ORM_O01.ORM_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_3-ORM_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`ORM_O01_ORDER <hl7-v2_3-ORM_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-ORN_O02:

.. py:class:: hl7types.hl7.v2_3.messages.ORN_O02.ORN_O02
   :noindex:

   HL7 v2 ORN_O02 message.

ORN_O02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORN_O02_RESPONSE <hl7-v2_3-ORN_O02_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_3-ORR_O02:

.. py:class:: hl7types.hl7.v2_3.messages.ORR_O02.ORR_O02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORR_O02_RESPONSE <hl7-v2_3-ORR_O02_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_3-ORU_R01:

.. py:class:: hl7types.hl7.v2_3.messages.ORU_R01.ORU_R01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``RESPONSE``
     -
     - List[:ref:`ORU_R01_RESPONSE <hl7-v2_3-ORU_R01_RESPONSE>`]
     - required
     -
     - RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-OSQ_Q06:

.. py:class:: hl7types.hl7.v2_3.messages.OSQ_Q06.OSQ_Q06
   :noindex:

   HL7 v2 OSQ_Q06 message.

OSQ_Q06
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-OSR_Q06:

.. py:class:: hl7types.hl7.v2_3.messages.OSR_Q06.OSR_Q06
   :noindex:

   HL7 v2 OSR_Q06 message.

OSR_Q06
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``RESPONSE``
     -
     - Optional[:ref:`OSR_Q06_RESPONSE <hl7-v2_3-OSR_Q06_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-PEX_P07:

.. py:class:: hl7types.hl7.v2_3.messages.PEX_P07.PEX_P07
   :noindex:

   HL7 v2 PEX_P07 message.

PEX_P07
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_3-PEX_P07_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``EXPERIENCE``
     -
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_3-PEX_P07_EXPERIENCE>`]
     - required
     -
     - EXPERIENCE: Required, repeating

.. _hl7-v2_3-PGL_PC6:

.. py:class:: hl7types.hl7.v2_3.messages.PGL_PC6.PGL_PC6
   :noindex:

   HL7 v2 PGL_PC6 message.

PGL_PC6
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_3-PGL_PC6_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``GOAL``
     -
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_3-PGL_PC6_GOAL>`]
     - required
     -
     - GOAL: Required, repeating

.. _hl7-v2_3-PIN_I07:

.. py:class:: hl7types.hl7.v2_3.messages.PIN_I07.PIN_I07
   :noindex:

   HL7 v2 PIN_I07 message.

PIN_I07
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PROVIDER``
     -
     - List[:ref:`PIN_I07_PROVIDER <hl7-v2_3-PIN_I07_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`PIN_I07_GUARANTOR_INSURANCE <hl7-v2_3-PIN_I07_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-PPG_PCG:

.. py:class:: hl7types.hl7.v2_3.messages.PPG_PCG.PPG_PCG
   :noindex:

   HL7 v2 PPG_PCG message.

PPG_PCG
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_3-PPG_PCG_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``PATHWAY``
     -
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_3-PPG_PCG_PATHWAY>`]
     - required
     -
     - PATHWAY: Required, repeating

.. _hl7-v2_3-PPP_PCB:

.. py:class:: hl7types.hl7.v2_3.messages.PPP_PCB.PPP_PCB
   :noindex:

   HL7 v2 PPP_PCB message.

PPP_PCB
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_3-PPP_PCB_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``PATHWAY``
     -
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_3-PPP_PCB_PATHWAY>`]
     - required
     -
     - PATHWAY: Required, repeating

.. _hl7-v2_3-PPR_PC1:

.. py:class:: hl7types.hl7.v2_3.messages.PPR_PC1.PPR_PC1
   :noindex:

   HL7 v2 PPR_PC1 message.

PPR_PC1
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_3-PPR_PC1_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``PROBLEM``
     -
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_3-PPR_PC1_PROBLEM>`]
     - required
     -
     - PROBLEM: Required, repeating

.. _hl7-v2_3-PPT_PCL:

.. py:class:: hl7types.hl7.v2_3.messages.PPT_PCL.PPT_PCL
   :noindex:

   HL7 v2 PPT_PCL message.

PPT_PCL
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PPT_PCL_PATIENT <hl7-v2_3-PPT_PCL_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-PPV_PCA:

.. py:class:: hl7types.hl7.v2_3.messages.PPV_PCA.PPV_PCA
   :noindex:

   HL7 v2 PPV_PCA message.

PPV_PCA
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PPV_PCA_PATIENT <hl7-v2_3-PPV_PCA_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-PRR_PC5:

.. py:class:: hl7types.hl7.v2_3.messages.PRR_PC5.PRR_PC5
   :noindex:

   HL7 v2 PRR_PC5 message.

PRR_PC5
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PRR_PC5_PATIENT <hl7-v2_3-PRR_PC5_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-PTR_PCF:

.. py:class:: hl7types.hl7.v2_3.messages.PTR_PCF.PTR_PCF
   :noindex:

   HL7 v2 PTR_PCF message.

PTR_PCF
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PTR_PCF_PATIENT <hl7-v2_3-PTR_PCF_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_3-QCK_Q02:

.. py:class:: hl7types.hl7.v2_3.messages.QCK_Q02.QCK_Q02
   :noindex:

   HL7 v2 QCK_Q02 message.

QCK_Q02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_3-QAK>`]
     - optional
     -
     - QAK: Optional

.. _hl7-v2_3-QRY_A19:

.. py:class:: hl7types.hl7.v2_3.messages.QRY_A19.QRY_A19
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional

.. _hl7-v2_3-QRY_PC4:

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PC4.QRY_PC4
   :noindex:

   HL7 v2 QRY_PC4 message.

QRY_PC4
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional

.. _hl7-v2_3-QRY_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.QRY_Q01.QRY_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-QRY_Q02:

.. py:class:: hl7types.hl7.v2_3.messages.QRY_Q02.QRY_Q02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-QRY_R02:

.. py:class:: hl7types.hl7.v2_3.messages.QRY_R02.QRY_R02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - :ref:`QRF <hl7-v2_3-QRF>`
     - required
     -
     - QRF: Required

.. _hl7-v2_3-QRY_T12:

.. py:class:: hl7types.hl7.v2_3.messages.QRY_T12.QRY_T12
   :noindex:

   HL7 v2 QRY_T12 message.

QRY_T12
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional

.. _hl7-v2_3-RAR_RAR:

.. py:class:: hl7types.hl7.v2_3.messages.RAR_RAR.RAR_RAR
   :noindex:

   HL7 v2 RAR_RAR message.

RAR_RAR
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``DEFINITION``
     -
     - List[:ref:`RAR_RAR_DEFINITION <hl7-v2_3-RAR_RAR_DEFINITION>`]
     - required
     -
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RAS_O01:

.. py:class:: hl7types.hl7.v2_3.messages.RAS_O01.RAS_O01
   :noindex:

   HL7 v2 RAS_O01 message.

RAS_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RAS_O01_PATIENT <hl7-v2_3-RAS_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RAS_O01_ORDER <hl7-v2_3-RAS_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-RCI_I05:

.. py:class:: hl7types.hl7.v2_3.messages.RCI_I05.RCI_I05
   :noindex:

   HL7 v2 RCI_I05 message.

RCI_I05
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RCI_I05_PROVIDER <hl7-v2_3-RCI_I05_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RCI_I05_OBSERVATION <hl7-v2_3-RCI_I05_OBSERVATION>`]]
     - optional
     -
     - OBSERVATION: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RCL_I06:

.. py:class:: hl7types.hl7.v2_3.messages.RCL_I06.RCL_I06
   :noindex:

   HL7 v2 RCL_I06 message.

RCL_I06
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RCL_I06_PROVIDER <hl7-v2_3-RCL_I06_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_3-DSP>`]]
     - optional
     -
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RDE_O01:

.. py:class:: hl7types.hl7.v2_3.messages.RDE_O01.RDE_O01
   :noindex:

   HL7 v2 RDE_O01 message.

RDE_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RDE_O01_PATIENT <hl7-v2_3-RDE_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RDE_O01_ORDER <hl7-v2_3-RDE_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-RDO_O01:

.. py:class:: hl7types.hl7.v2_3.messages.RDO_O01.RDO_O01
   :noindex:

   HL7 v2 RDO_O01 message.

RDO_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RDO_O01_PATIENT <hl7-v2_3-RDO_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RDO_O01_ORDER <hl7-v2_3-RDO_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-RDR_RDR:

.. py:class:: hl7types.hl7.v2_3.messages.RDR_RDR.RDR_RDR
   :noindex:

   HL7 v2 RDR_RDR message.

RDR_RDR
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``DEFINITION``
     -
     - List[:ref:`RDR_RDR_DEFINITION <hl7-v2_3-RDR_RDR_DEFINITION>`]
     - required
     -
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RDS_O01:

.. py:class:: hl7types.hl7.v2_3.messages.RDS_O01.RDS_O01
   :noindex:

   HL7 v2 RDS_O01 message.

RDS_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RDS_O01_PATIENT <hl7-v2_3-RDS_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RDS_O01_ORDER <hl7-v2_3-RDS_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-REF_I12:

.. py:class:: hl7types.hl7.v2_3.messages.REF_I12.REF_I12
   :noindex:

   HL7 v2 REF_I12 message.

REF_I12
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION``
     -
     - Optional[:ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`]
     - optional
     -
     - AUTHORIZATION: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``RESULTS``
     -
     - Optional[List[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]]
     - optional
     -
     - RESULTS: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RER_RER:

.. py:class:: hl7types.hl7.v2_3.messages.RER_RER.RER_RER
   :noindex:

   HL7 v2 RER_RER message.

RER_RER
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``DEFINITION``
     -
     - List[:ref:`RER_RER_DEFINITION <hl7-v2_3-RER_RER_DEFINITION>`]
     - required
     -
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RGR_RGR:

.. py:class:: hl7types.hl7.v2_3.messages.RGR_RGR.RGR_RGR
   :noindex:

   HL7 v2 RGR_RGR message.

RGR_RGR
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``DEFINITION``
     -
     - List[:ref:`RGR_RGR_DEFINITION <hl7-v2_3-RGR_RGR_DEFINITION>`]
     - required
     -
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RGV_O01:

.. py:class:: hl7types.hl7.v2_3.messages.RGV_O01.RGV_O01
   :noindex:

   HL7 v2 RGV_O01 message.

RGV_O01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RGV_O01_PATIENT <hl7-v2_3-RGV_O01_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RGV_O01_ORDER <hl7-v2_3-RGV_O01_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_3-ROR_ROR:

.. py:class:: hl7types.hl7.v2_3.messages.ROR_ROR.ROR_ROR
   :noindex:

   HL7 v2 ROR_ROR message.

ROR_ROR
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``DEFINITION``
     -
     - List[:ref:`ROR_ROR_DEFINITION <hl7-v2_3-ROR_ROR_DEFINITION>`]
     - required
     -
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RPA_I08:

.. py:class:: hl7types.hl7.v2_3.messages.RPA_I08.RPA_I08
   :noindex:

   HL7 v2 RPA_I08 message.

RPA_I08
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION``
     -
     - Optional[:ref:`RPA_I08_AUTHORIZATION <hl7-v2_3-RPA_I08_AUTHORIZATION>`]
     - optional
     -
     - AUTHORIZATION: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RPA_I08_PROVIDER <hl7-v2_3-RPA_I08_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`RPA_I08_INSURANCE <hl7-v2_3-RPA_I08_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - List[:ref:`RPA_I08_PROCEDURE <hl7-v2_3-RPA_I08_PROCEDURE>`]
     - required
     -
     - PROCEDURE: Required, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RPA_I08_OBSERVATION <hl7-v2_3-RPA_I08_OBSERVATION>`]]
     - optional
     -
     - OBSERVATION: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`RPA_I08_VISIT <hl7-v2_3-RPA_I08_VISIT>`]
     - optional
     -
     - VISIT: Optional

.. _hl7-v2_3-RPI_I01:

.. py:class:: hl7types.hl7.v2_3.messages.RPI_I01.RPI_I01
   :noindex:

   HL7 v2 RPI_I01 message.

RPI_I01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPI_I01_PROVIDER <hl7-v2_3-RPI_I01_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RPI_I01_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RPL_I02:

.. py:class:: hl7types.hl7.v2_3.messages.RPL_I02.RPL_I02
   :noindex:

   HL7 v2 RPL_I02 message.

RPL_I02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPL_I02_PROVIDER <hl7-v2_3-RPL_I02_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_3-DSP>`]]
     - optional
     -
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RQA_I08:

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I08.RQA_I08
   :noindex:

   HL7 v2 RQA_I08 message.

RQA_I08
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION``
     -
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`]
     - optional
     -
     - AUTHORIZATION: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]]
     - optional
     -
     - OBSERVATION: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RQC_I05:

.. py:class:: hl7types.hl7.v2_3.messages.RQC_I05.RQC_I05
   :noindex:

   HL7 v2 RQC_I05 message.

RQC_I05
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQC_I05_PROVIDER <hl7-v2_3-RQC_I05_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RQC_I06:

.. py:class:: hl7types.hl7.v2_3.messages.RQC_I06.RQC_I06
   :noindex:

   HL7 v2 RQC_I06 message.

RQC_I06
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQC_I06_PROVIDER <hl7-v2_3-RQC_I06_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     -
     - GT1: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RQI_I01:

.. py:class:: hl7types.hl7.v2_3.messages.RQI_I01.RQI_I01
   :noindex:

   HL7 v2 RQI_I01 message.

RQI_I01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_3-RQI_I01_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RQP_I04:

.. py:class:: hl7types.hl7.v2_3.messages.RQP_I04.RQP_I04
   :noindex:

   HL7 v2 RQP_I04 message.

RQP_I04
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RQP_I04_PROVIDER <hl7-v2_3-RQP_I04_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RQQ_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.RQQ_Q01.RQQ_Q01
   :noindex:

   HL7 v2 RQQ_Q01 message.

RQQ_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``ERQ``
     -
     - :ref:`ERQ <hl7-v2_3-ERQ>`
     - required
     -
     - ERQ: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-RRA_O02:

.. py:class:: hl7types.hl7.v2_3.messages.RRA_O02.RRA_O02
   :noindex:

   HL7 v2 RRA_O02 message.

RRA_O02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRA_O02_RESPONSE <hl7-v2_3-RRA_O02_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_3-RRD_O02:

.. py:class:: hl7types.hl7.v2_3.messages.RRD_O02.RRD_O02
   :noindex:

   HL7 v2 RRD_O02 message.

RRD_O02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RRD_O02_PATIENT <hl7-v2_3-RRD_O02_PATIENT>`]
     - optional
     -
     - PATIENT: Optional

.. _hl7-v2_3-RRG_O02:

.. py:class:: hl7types.hl7.v2_3.messages.RRG_O02.RRG_O02
   :noindex:

   HL7 v2 RRG_O02 message.

RRG_O02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRG_O02_RESPONSE <hl7-v2_3-RRG_O02_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_3-RRI_I12:

.. py:class:: hl7types.hl7.v2_3.messages.RRI_I12.RRI_I12
   :noindex:

   HL7 v2 RRI_I12 message.

RRI_I12
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - Optional[:ref:`MSA <hl7-v2_3-MSA>`]
     - optional
     -
     - MSA: Optional
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION``
     -
     - Optional[:ref:`RRI_I12_AUTHORIZATION <hl7-v2_3-RRI_I12_AUTHORIZATION>`]
     - optional
     -
     - AUTHORIZATION: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RRI_I12_PROVIDER <hl7-v2_3-RRI_I12_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`RRI_I12_PROCEDURE <hl7-v2_3-RRI_I12_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``RESULTS``
     -
     - Optional[List[:ref:`RRI_I12_RESULTS <hl7-v2_3-RRI_I12_RESULTS>`]]
     - optional
     -
     - RESULTS: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`RRI_I12_VISIT <hl7-v2_3-RRI_I12_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_3-RRO_O02:

.. py:class:: hl7types.hl7.v2_3.messages.RRO_O02.RRO_O02
   :noindex:

   HL7 v2 RRO_O02 message.

RRO_O02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRO_O02_RESPONSE <hl7-v2_3-RRO_O02_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_3-SIU_S12:

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S12.SIU_S12
   :noindex:

   HL7 v2 SIU_S12 message.

SIU_S12
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``SCH``
     -
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     -
     - SCH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     -
     - PATIENT: Optional, repeating
   * - ``RESOURCES``
     -
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     -
     - RESOURCES: Required, repeating

.. _hl7-v2_3-SPQ_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.SPQ_Q01.SPQ_Q01
   :noindex:

   HL7 v2 SPQ_Q01 message.

SPQ_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``SPR``
     -
     - :ref:`SPR <hl7-v2_3-SPR>`
     - required
     -
     - SPR: Required
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_3-RDF>`]
     - optional
     -
     - RDF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-SQM_S25:

.. py:class:: hl7types.hl7.v2_3.messages.SQM_S25.SQM_S25
   :noindex:

   HL7 v2 SQM_S25 message.

SQM_S25
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``REQUEST``
     -
     - Optional[:ref:`SQM_S25_REQUEST <hl7-v2_3-SQM_S25_REQUEST>`]
     - optional
     -
     - REQUEST: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-SQR_S25:

.. py:class:: hl7types.hl7.v2_3.messages.SQR_S25.SQR_S25
   :noindex:

   HL7 v2 SQR_S25 message.

SQR_S25
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     -
     - QAK: Required
   * - ``SCHEDULE``
     -
     - Optional[List[:ref:`SQR_S25_SCHEDULE <hl7-v2_3-SQR_S25_SCHEDULE>`]]
     - optional
     -
     - SCHEDULE: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-SRM_S01:

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S01.SRM_S01
   :noindex:

   HL7 v2 SRM_S01 message.

SRM_S01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``ARQ``
     -
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     -
     - ARQ: Required
   * - ``APR``
     -
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     -
     - APR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     -
     - PATIENT: Optional, repeating
   * - ``RESOURCES``
     -
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     -
     - RESOURCES: Required, repeating

.. _hl7-v2_3-SRR_S01:

.. py:class:: hl7types.hl7.v2_3.messages.SRR_S01.SRR_S01
   :noindex:

   HL7 v2 SRR_S01 message.

SRR_S01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``SCHEDULE``
     -
     - Optional[:ref:`SRR_S01_SCHEDULE <hl7-v2_3-SRR_S01_SCHEDULE>`]
     - optional
     -
     - SCHEDULE: Optional

.. _hl7-v2_3-SUR_P09:

.. py:class:: hl7types.hl7.v2_3.messages.SUR_P09.SUR_P09
   :noindex:

   HL7 v2 SUR_P09 message.

SUR_P09
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``FACILITY``
     -
     - List[:ref:`SUR_P09_FACILITY <hl7-v2_3-SUR_P09_FACILITY>`]
     - required
     -
     - FACILITY: Required, repeating

.. _hl7-v2_3-TBR_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.TBR_Q01.TBR_Q01
   :noindex:

   HL7 v2 TBR_Q01 message.

TBR_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     -
     - QAK: Required
   * - ``RDF``
     -
     - :ref:`RDF <hl7-v2_3-RDF>`
     - required
     -
     - RDF: Required
   * - ``RDT``
     -
     - List[:ref:`RDT <hl7-v2_3-RDT>`]
     - required
     -
     - RDT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-UDM_Q05:

.. py:class:: hl7types.hl7.v2_3.messages.UDM_Q05.UDM_Q05
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``URD``
     -
     - :ref:`URD <hl7-v2_3-URD>`
     - required
     -
     - URD: Required
   * - ``URS``
     -
     - Optional[:ref:`URS <hl7-v2_3-URS>`]
     - optional
     -
     - URS: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-VQQ_Q01:

.. py:class:: hl7types.hl7.v2_3.messages.VQQ_Q01.VQQ_Q01
   :noindex:

   HL7 v2 VQQ_Q01 message.

VQQ_Q01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``VTQ``
     -
     - :ref:`VTQ <hl7-v2_3-VTQ>`
     - required
     -
     - VTQ: Required
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_3-RDF>`]
     - optional
     -
     - RDF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_3-VXQ_V01:

.. py:class:: hl7types.hl7.v2_3.messages.VXQ_V01.VXQ_V01
   :noindex:

   HL7 v2 VXQ_V01 message.

VXQ_V01
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional

.. _hl7-v2_3-VXR_V03:

.. py:class:: hl7types.hl7.v2_3.messages.VXR_V03.VXR_V03
   :noindex:

   HL7 v2 VXR_V03 message.

VXR_V03
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`VXR_V03_PATIENT_VISIT <hl7-v2_3-VXR_V03_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`VXR_V03_INSURANCE <hl7-v2_3-VXR_V03_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ORDER``
     -
     - Optional[List[:ref:`VXR_V03_ORDER <hl7-v2_3-VXR_V03_ORDER>`]]
     - optional
     -
     - ORDER: Optional, repeating

.. _hl7-v2_3-VXU_V04:

.. py:class:: hl7types.hl7.v2_3.messages.VXU_V04.VXU_V04
   :noindex:

   HL7 v2 VXU_V04 message.

VXU_V04
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`VXU_V04_PATIENT <hl7-v2_3-VXU_V04_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`VXU_V04_INSURANCE <hl7-v2_3-VXU_V04_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ORDER``
     -
     - Optional[List[:ref:`VXU_V04_ORDER <hl7-v2_3-VXU_V04_ORDER>`]]
     - optional
     -
     - ORDER: Optional, repeating

.. _hl7-v2_3-VXX_V02:

.. py:class:: hl7types.hl7.v2_3.messages.VXX_V02.VXX_V02
   :noindex:

   HL7 v2 VXX_V02 message.

VXX_V02
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
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     -
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     -
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     -
     - QRF: Optional
   * - ``PATIENT``
     -
     - List[:ref:`VXX_V02_PATIENT <hl7-v2_3-VXX_V02_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating
