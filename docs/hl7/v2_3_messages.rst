v2.3 Messages
=============

.. _hl7-v2_3-ACK:

ACK General acknowledgment message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment

.. _hl7-v2_3-ADT_A01:

ADT_A01 ADT/ACK - Admit/visit notification.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A02:

ADT_A02 ADT/ACK -  Transfer a patient.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A03:

ADT_A03 ADT/ACK -  Discharge a patient.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A03_PROCEDURE <hl7-v2_3-ADT_A03_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A04:

ADT_A04 ADT/ACK -  Register a patient (S3.2.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A05:

ADT_A05 ADT/ACK -  Preadmit a patient (S3.2.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A06:

ADT_A06 ADT/ACK -  Transfer an outpatient to inpatient.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_3-MRG>`]
     - optional
     - Merge patient information
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_3-ADT_A06_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_3-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A07:

ADT_A07 ADT/ACK -  Transfer an inpatient to outpatient (S3.2.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_3-MRG>`]
     - optional
     - Merge patient information
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_3-ADT_A06_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_3-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A08:

ADT_A08 ADT/ACK -  Update patient information (S3.2.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A09:

ADT_A09 ADT/ACK -  Patient departing.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_3-ADT_A10:

ADT_A10 ADT/ACK -  Patient arriving (S3.2.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_3-ADT_A11:

ADT_A11 ADT/ACK -  Cancel admit (S3.2.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_3-ADT_A12:

ADT_A12 ADT/ACK -  Cancel transfer.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_3-DG1>`]
     - optional
     - Diagnosis

.. _hl7-v2_3-ADT_A13:

ADT_A13 ADT/ACK -  Cancel discharge (S3.2.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A14:

ADT_A14 ADT/ACK -  Pending admit (S3.2.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A15:

ADT_A15 ADT/ACK -  Pending transfer (S3.2.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_3-ADT_A16:

ADT_A16 ADT/ACK -  Pending discharge.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_3-DG1>`]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group

.. _hl7-v2_3-ADT_A17:

ADT_A17 ADT/ACK -  Swap patients.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A18:

ADT_A18 ADT/ACK -  Merge patient information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A18.ADT_A18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_3-MRG>`]
     - optional
     - Merge patient information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit

.. _hl7-v2_3-ADT_A20:

ADT_A20 ADT/ACK -  Nursing/Census application updates.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``NPU``
     - :ref:`NPU <hl7-v2_3-NPU>`
     - required
     - Bed status update

.. _hl7-v2_3-ADT_A21:

ADT_A21 ADT/ACK -  Leave of absence - out (leaving) (S3.2.21).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A22:

ADT_A22 ADT/ACK -  Leave of absence - in (returning) (S3.2.22).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A22.ADT_A22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A23:

ADT_A23 ADT/ACK -  Delete a patient record (S3.2.23).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A23.ADT_A23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A24:

ADT_A24 ADT/ACK -  Link patient information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment

.. _hl7-v2_3-ADT_A25:

ADT_A25 ADT/ACK -  Cancel pending discharge (S3.2.25).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A25.ADT_A25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A26:

ADT_A26 ADT/ACK -  Cancel pending transfer (S3.2.26).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A26.ADT_A26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A27:

ADT_A27 ADT/ACK -  Cancel pending admit (S3.2.27).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A27.ADT_A27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A28:

ADT_A28 ADT/ACK -  Add person information (S3.2.28).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A29:

ADT_A29 ADT/ACK -  Delete person information (S3.2.29).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A29.ADT_A29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A30:

ADT_A30 ADT/ACK -  Merge person information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A30.ADT_A30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A31:

ADT_A31 ADT/ACK -  Update person information (S3.2.31).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_3-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_3-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_3-UB1>`]
     - optional
     - UB82  data
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_3-UB2>`]
     - optional
     - UB92 data

.. _hl7-v2_3-ADT_A32:

ADT_A32 ADT/ACK -  Cancel patient arriving (S3.2.32).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A32.ADT_A32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A33:

ADT_A33 ADT/ACK -  Cancel patient departing (S3.2.33).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A33.ADT_A33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-ADT_A34:

ADT_A34 ADT/ACK -  Merge patient information - patient ID only (S3.2.34).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A34.ADT_A34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A35:

ADT_A35 ADT/ACK -  Merge patient information - account number only (S3.2.35).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A35.ADT_A35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A36:

ADT_A36 ADT/ACK -  Merge patient information - patient ID and account number (S3.2.36).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A36.ADT_A36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A37:

ADT_A37 ADT/ACK -  Unlink patient information (S3.2.37).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment

.. _hl7-v2_3-ADT_A38:

ADT_A38 ADT/ACK - Cancel pre-admit.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A38.ADT_A38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group

.. _hl7-v2_3-ADT_A39:

ADT_A39 ADT/ACK - Merge person - external ID.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A39.ADT_A39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-ADT_A40:

ADT_A40 ADT/ACK - Merge patient - internal ID (S3.2.40).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A40.ADT_A40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-ADT_A41:

ADT_A41 ADT/ACK - Merge account - patient account number (S3.2.41).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A41.ADT_A41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-ADT_A42:

ADT_A42 ADT/ACK - Merge visit - visit number (S3.2.42).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A42.ADT_A42
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_3-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-ADT_A43:

ADT_A43 ADT/ACK - Move patient information - internal ID.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A43.ADT_A43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_3-ADT_A43_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-ADT_A44:

ADT_A44 ADT/ACK - Move account information - internal ID (S3.2.44).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A44.ADT_A44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_3-ADT_A43_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-ADT_A45:

ADT_A45 ADT/ACK - Move visit information - visit number.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A45.ADT_A45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MERGE_INFO``
     - List[:ref:`ADT_A45_MERGE_INFO <hl7-v2_3-ADT_A45_MERGE_INFO>`]
     - required
     - MERGE_INFO

.. _hl7-v2_3-ADT_A46:

ADT_A46 ADT/ACK - Change external ID (S3.2.46).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A46.ADT_A46
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A47:

ADT_A47 ADT/ACK - Change internal ID (S3.2.47).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A47.ADT_A47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A48:

ADT_A48 ADT/ACK - Change alternate patient ID (S3.2.48).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A48.ADT_A48
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A49:

ADT_A49 ADT/ACK - Change patient account number (S3.2.49).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A49.ADT_A49
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_3-ADT_A50:

ADT_A50 ADT/ACK - Change visit number.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A50.ADT_A50
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit

.. _hl7-v2_3-ADT_A51:

ADT_A51 ADT/ACK - Change alternate visit ID (S3.2.51).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ADT_A51.ADT_A51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit

.. _hl7-v2_3-ARD_A19:

ARD_A19 HL7 v2 ARD_A19 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ARD_A19.ARD_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``QUERY_RESPONSE``
     - List[:ref:`ARD_A19_QUERY_RESPONSE <hl7-v2_3-ARD_A19_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-BAR_P01:

BAR_P01 BAR/ACK - Add patient account.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``VISIT``
     - List[:ref:`BAR_P01_VISIT <hl7-v2_3-BAR_P01_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_3-BAR_P02:

BAR_P02 BAR/ACK - Purge patient account.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_3-BAR_P02_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-BAR_P05:

BAR_P05 BAR/ACK - Update account (S6.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P05.BAR_P05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``VISIT``
     - List[:ref:`BAR_P01_VISIT <hl7-v2_3-BAR_P01_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_3-BAR_P06:

BAR_P06 BAR/ACK - End account.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.BAR_P06.BAR_P06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PATIENT``
     - List[:ref:`BAR_P06_PATIENT <hl7-v2_3-BAR_P06_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C01:

CRM_C01 SRM - Register a patient on a clinical trial.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C01.CRM_C01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C02:

CRM_C02 SRM - Cancel a patient registration on clin.trial (for clerical mistakes only) (S7.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C02.CRM_C02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C03:

CRM_C03 SRM - Correct/update registration information (S7.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C03.CRM_C03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C04:

CRM_C04 SRM - Patient has gone off a clinical trial (S7.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C04.CRM_C04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C05:

CRM_C05 SRM - Patient enters phase of clinical trial (S7.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C05.CRM_C05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C06:

CRM_C06 SRM - Cancel patient entering a phase (clerical mistake) (S7.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C06.CRM_C06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C07:

CRM_C07 SRM - Correct/update phase information (S7.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C07.CRM_C07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CRM_C08:

CRM_C08 SRM - Patient has gone off phase of clinical trial (S7.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CRM_C08.CRM_C08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_3-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CSU_C09:

CSU_C09 CSU - Automated time intervals for reporting, like monthly.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C09.CSU_C09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CSU_C10:

CSU_C10 CSU - Patient completes the clinical trial (S7.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C10.CSU_C10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CSU_C11:

CSU_C11 CSU - Patient completes a phase of the clinical trial (S7.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C11.CSU_C11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-CSU_C12:

CSU_C12 CSU - Update/correction of patient order/result information (S7.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.CSU_C12.CSU_C12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_3-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-DFT_P03:

DFT_P03 DFT/ACK - Post detail financial transaction.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_3-DB1>`]]
     - optional
     - Disability Segment
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``FINANCIAL``
     - List[:ref:`DFT_P03_FINANCIAL <hl7-v2_3-DFT_P03_FINANCIAL>`]
     - required
     - FINANCIAL
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_3-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`DFT_P03_INSURANCE <hl7-v2_3-DFT_P03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident

.. _hl7-v2_3-DOC_T12:

DOC_T12 QRY/DOC - Document query.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DOC_T12.DOC_T12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``RESULT``
     - List[:ref:`DOC_T12_RESULT <hl7-v2_3-DOC_T12_RESULT>`]
     - required
     - RESULT
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-DSR_Q01:

DSR_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DSR_Q01.DSR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_3-QAK>`]
     - optional
     - Query Acknowledgement
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     - Display data segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-DSR_Q03:

DSR_Q03 DSR/ACK - Deferred response to a query.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.DSR_Q03.DSR_Q03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - Optional[:ref:`MSA <hl7-v2_3-MSA>`]
     - optional
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_3-QAK>`]
     - optional
     - Query Acknowledgement
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     - Display data segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-EDR_Q01:

EDR_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.EDR_Q01.EDR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     - Query Acknowledgement
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     - Display data segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-EQQ_Q01:

EQQ_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.EQQ_Q01.EQQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EQL``
     - :ref:`EQL <hl7-v2_3-EQL>`
     - required
     - Embedded Query Language
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-ERP_Q01:

ERP_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ERP_Q01.ERP_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     - Query Acknowledgement
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_3-ERQ>`
     - required
     - Event Replay Query Segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-MDM_T01:

MDM_T01 MDM/ACK - Original document notification.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T01.MDM_T01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment

.. _hl7-v2_3-MDM_T02:

MDM_T02 MDM/ACK - Original document notification and content.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T02.MDM_T02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment
   * - ``OBX``
     - List[:ref:`OBX <hl7-v2_3-OBX>`]
     - required
     - Observation segment

.. _hl7-v2_3-MDM_T03:

MDM_T03 MDM/ACK - Document status change notification (S9.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T03.MDM_T03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment

.. _hl7-v2_3-MDM_T04:

MDM_T04 MDM/ACK - Document status change notification and content (S9.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T04.MDM_T04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment
   * - ``OBX``
     - List[:ref:`OBX <hl7-v2_3-OBX>`]
     - required
     - Observation segment

.. _hl7-v2_3-MDM_T05:

MDM_T05 MDM/ACK - Document addendum notification (S9.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T05.MDM_T05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment

.. _hl7-v2_3-MDM_T06:

MDM_T06 MDM/ACK - Document addendum notification and content (S9.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T06.MDM_T06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment
   * - ``OBX``
     - List[:ref:`OBX <hl7-v2_3-OBX>`]
     - required
     - Observation segment

.. _hl7-v2_3-MDM_T07:

MDM_T07 MDM/ACK - Document edit notification (S9.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T07.MDM_T07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment

.. _hl7-v2_3-MDM_T08:

MDM_T08 MDM/ACK - Document edit notification and content (S9.4.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T08.MDM_T08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment
   * - ``OBX``
     - List[:ref:`OBX <hl7-v2_3-OBX>`]
     - required
     - Observation segment

.. _hl7-v2_3-MDM_T09:

MDM_T09 MDM/ACK - Document replace notification (S9.4.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T09.MDM_T09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment

.. _hl7-v2_3-MDM_T10:

MDM_T10 MDM/ACK - Document replacement notification and content (S9.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T10.MDM_T10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment
   * - ``OBX``
     - List[:ref:`OBX <hl7-v2_3-OBX>`]
     - required
     - Observation segment

.. _hl7-v2_3-MDM_T11:

MDM_T11 MDM/ACK - Document cancel notification (S9.4.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MDM_T11.MDM_T11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_3-TXA>`
     - required
     - Document notification segment

.. _hl7-v2_3-MFK_M01:

MFK_M01 MFN/MFK - Master file not otherwise specified (for backward comp.only).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_3-MFA>`]]
     - optional
     - Master file acknowledgement segment

.. _hl7-v2_3-MFK_M02:

MFK_M02 HL7 v2 MFK_M02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFK_M02.MFK_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_3-MFA>`]]
     - optional
     - Master file acknowledgement segment

.. _hl7-v2_3-MFN_M01:

MFN_M01 MFN/MFK - Master file not otherwise specified (for backward comp.only).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M01.MFN_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF``
     - List[:ref:`MFN_M01_MF <hl7-v2_3-MFN_M01_MF>`]
     - required
     - MF

.. _hl7-v2_3-MFN_M02:

MFN_M02 MFN/MFK - Master file - Staff Practioner.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_STAFF``
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_3-MFN_M02_MF_STAFF>`]
     - required
     - MF_STAFF

.. _hl7-v2_3-MFN_M03:

MFN_M03 MFN/MFK - Master file - Test/Observation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M03.MFN_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_TEST``
     - List[:ref:`MFN_M03_MF_TEST <hl7-v2_3-MFN_M03_MF_TEST>`]
     - required
     - MF_TEST

.. _hl7-v2_3-MFN_M04:

MFN_M04 MFN/MFK - Charge description master file (S8.9.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M04.MFN_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_CDM``
     - List[:ref:`MFN_M06_MF_CDM <hl7-v2_3-MFN_M06_MF_CDM>`]
     - required
     - MF_CDM

.. _hl7-v2_3-MFN_M05:

MFN_M05 MFN/MFK - Patient location master file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M05.MFN_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_LOCATION``
     - List[:ref:`MFN_M05_MF_LOCATION <hl7-v2_3-MFN_M05_MF_LOCATION>`]
     - required
     - MF_LOCATION

.. _hl7-v2_3-MFN_M06:

MFN_M06 MFN/MFK - Clinical study master file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M06.MFN_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_CDM``
     - List[:ref:`MFN_M06_MF_CDM <hl7-v2_3-MFN_M06_MF_CDM>`]
     - required
     - MF_CDM

.. _hl7-v2_3-MFN_M07:

MFN_M07 MFN/MFK - Clinical study without phases but with schedules master file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M07.MFN_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_CLIN_STUDY``
     - List[:ref:`MFN_M07_MF_CLIN_STUDY <hl7-v2_3-MFN_M07_MF_CLIN_STUDY>`]
     - required
     - MF_CLIN_STUDY

.. _hl7-v2_3-MFN_M08:

MFN_M08 MFN/MFK - Test/Observation (Numeric) master file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M08.MFN_M08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_TEST_NUMERIC``
     - List[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_3-MFN_M08_MF_TEST_NUMERIC>`]
     - required
     - MF_TEST_NUMERIC

.. _hl7-v2_3-MFN_M09:

MFN_M09 MFN/MFK - Test/Observation (Categorical) master file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M09.MFN_M09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_TEST_CATEGORICAL``
     - List[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_3-MFN_M09_MF_TEST_CATEGORICAL>`]
     - required
     - MF_TEST_CATEGORICAL

.. _hl7-v2_3-MFN_M10:

MFN_M10 MFN/MFK - Test/Observation batteries master file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M10.MFN_M10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_TEST_BATTERIES``
     - List[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_3-MFN_M10_MF_TEST_BATTERIES>`]
     - required
     - MF_TEST_BATTERIES

.. _hl7-v2_3-MFN_M11:

MFN_M11 MFN/MFK - Test/calculated observation master file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.MFN_M11.MFN_M11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_3-MFI>`
     - required
     - Master file identification segment
   * - ``MF_TEST_CALCULATED``
     - List[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_3-MFN_M11_MF_TEST_CALCULATED>`]
     - required
     - MF_TEST_CALCULATED

.. _hl7-v2_3-OMD_O01:

OMD_O01 HL7 v2 OMD_O01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OMD_O01.OMD_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`OMD_O01_PATIENT <hl7-v2_3-OMD_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_DIET``
     - List[:ref:`OMD_O01_ORDER_DIET <hl7-v2_3-OMD_O01_ORDER_DIET>`]
     - required
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - Optional[List[:ref:`OMD_O01_ORDER_TRAY <hl7-v2_3-OMD_O01_ORDER_TRAY>`]]
     - optional
     - ORDER_TRAY

.. _hl7-v2_3-OMN_O01:

OMN_O01 HL7 v2 OMN_O01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OMN_O01.OMN_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`OMN_O01_PATIENT <hl7-v2_3-OMN_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMN_O01_ORDER <hl7-v2_3-OMN_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-OMS_O01:

OMS_O01 HL7 v2 OMS_O01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OMS_O01.OMS_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`OMS_O01_PATIENT <hl7-v2_3-OMS_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMS_O01_ORDER <hl7-v2_3-OMS_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-ORD_O02:

ORD_O02 HL7 v2 ORD_O02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORD_O02.ORD_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESPONSE``
     - Optional[:ref:`ORD_O02_RESPONSE <hl7-v2_3-ORD_O02_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_3-ORF_R04:

ORF_R04 ORF - Response to query; transmission of requested observation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORF_R04.ORF_R04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``QUERY_RESPONSE``
     - List[:ref:`ORF_R04_QUERY_RESPONSE <hl7-v2_3-ORF_R04_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-ORM_O01:

ORM_O01 ORM - Order message (also RDE, RDS, RGV, RAS,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORM_O01.ORM_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_3-ORM_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORM_O01_ORDER <hl7-v2_3-ORM_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-ORN_O02:

ORN_O02 HL7 v2 ORN_O02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORN_O02.ORN_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESPONSE``
     - Optional[:ref:`ORN_O02_RESPONSE <hl7-v2_3-ORN_O02_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_3-ORR_O02:

ORR_O02 ORR - Order response (also RRE, RRD, RRG, RRA,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORR_O02.ORR_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESPONSE``
     - Optional[:ref:`ORR_O02_RESPONSE <hl7-v2_3-ORR_O02_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_3-ORU_R01:

ORU_R01 ORU/ACK - Unsolicited transmission of an observation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RESPONSE``
     - List[:ref:`ORU_R01_RESPONSE <hl7-v2_3-ORU_R01_RESPONSE>`]
     - required
     - RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-OSQ_Q06:

OSQ_Q06 OSQ/OSR - Query for order status.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OSQ_Q06.OSQ_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-OSR_Q06:

OSR_Q06 OSQ/OSR - Query for order status.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.OSR_Q06.OSR_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``RESPONSE``
     - Optional[:ref:`OSR_Q06_RESPONSE <hl7-v2_3-OSR_Q06_RESPONSE>`]
     - optional
     - RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-PEX_P07:

PEX_P07 PEX - Unsolicited initial individual product experience report.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PEX_P07.PEX_P07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VISIT``
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_3-PEX_P07_VISIT>`]
     - optional
     - VISIT
   * - ``EXPERIENCE``
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_3-PEX_P07_EXPERIENCE>`]
     - required
     - EXPERIENCE

.. _hl7-v2_3-PEX_P08:

PEX_P08 PEX - Unsolicited update individual product experience report (S7.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PEX_P08.PEX_P08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_3-EVN>`
     - required
     - Event type
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VISIT``
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_3-PEX_P07_VISIT>`]
     - optional
     - VISIT
   * - ``EXPERIENCE``
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_3-PEX_P07_EXPERIENCE>`]
     - required
     - EXPERIENCE

.. _hl7-v2_3-PGL_PC6:

PGL_PC6 PGL - PC/Goal Add.
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PGL_PC6.PGL_PC6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_3-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_3-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_3-PGL_PC7:

PGL_PC7 PGL - PC/Goal Update (S12.2.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PGL_PC7.PGL_PC7
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_3-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_3-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_3-PGL_PC8:

PGL_PC8 PGL - PC/Goal Delete (S12.2.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PGL_PC8.PGL_PC8
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_3-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_3-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_3-PIN_I07:

PIN_I07 PIN/ACK - Unsolicited insurance information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PIN_I07.PIN_I07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PROVIDER``
     - List[:ref:`PIN_I07_PROVIDER <hl7-v2_3-PIN_I07_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`PIN_I07_GUARANTOR_INSURANCE <hl7-v2_3-PIN_I07_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPG_PCG:

PPG_PCG PPP - PC/Pathway (Goal Oriented) Add.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPG_PCG.PPG_PCG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_3-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_3-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PPG_PCH:

PPG_PCH PPP - PC/Pathway (Goal Oriented) Update (S12.2.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPG_PCH.PPG_PCH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_3-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_3-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PPG_PCJ:

PPG_PCJ PPP - PC/Pathway (Goal Oriented) Delete (S12.2.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPG_PCJ.PPG_PCJ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_3-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_3-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PPP_PCB:

PPP_PCB PPP - PC/Pathway (Problem Oriented) Add.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPP_PCB.PPP_PCB
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_3-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_3-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PPP_PCC:

PPP_PCC PPP - PC/Pathway (Problem Oriented) Update (S12.2.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPP_PCC.PPP_PCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_3-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_3-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PPP_PCD:

PPP_PCD PPP - PC/Pathway (Problem Oriented) Delete (S12.2.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPP_PCD.PPP_PCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_3-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_3-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PPR_PC1:

PPR_PC1 PPR - PC/Problem Add.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPR_PC1.PPR_PC1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_3-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_3-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_3-PPR_PC2:

PPR_PC2 PPR - PC/Problem Update (S12.2.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPR_PC2.PPR_PC2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_3-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_3-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_3-PPR_PC3:

PPR_PC3 PPR - PC/Problem Delete (S12.2.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPR_PC3.PPR_PC3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_3-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_3-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_3-PPT_PCL:

PPT_PCL PPP - PC/Pathway (Goal Oriented) Query Response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPT_PCL.PPT_PCL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``PATIENT``
     - List[:ref:`PPT_PCL_PATIENT <hl7-v2_3-PPT_PCL_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-PPV_PCA:

PPV_PCA PGL - PC/Goal Response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PPV_PCA.PPV_PCA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``PATIENT``
     - List[:ref:`PPV_PCA_PATIENT <hl7-v2_3-PPV_PCA_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-PRR_PC5:

PRR_PC5 PPR - PC/Problem Reponse.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PRR_PC5.PRR_PC5
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``PATIENT``
     - List[:ref:`PRR_PC5_PATIENT <hl7-v2_3-PRR_PC5_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-PTR_PCF:

PTR_PCF PPP - PC/Pathway (Problem Oriented) Query Response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.PTR_PCF.PTR_PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``PATIENT``
     - List[:ref:`PTR_PCF_PATIENT <hl7-v2_3-PTR_PCF_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_3-QCK_Q02:

QCK_Q02 QRY/ACK - Query sent for deferred response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QCK_Q02.QCK_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_3-QAK>`]
     - optional
     - Query Acknowledgement

.. _hl7-v2_3-QRY_A19:

QRY_A19 QRY/ACK -  Patient query.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_A19.QRY_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment

.. _hl7-v2_3-QRY_PC4:

QRY_PC4 PPR - PC/Problem Query.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PC4.QRY_PC4
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment

.. _hl7-v2_3-QRY_PC9:

QRY_PC9 PGL - PC/Goal Query (S12.2.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PC9.QRY_PC9
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment

.. _hl7-v2_3-QRY_PCE:

QRY_PCE PPP - PC/Pathway (Problem Oriented) Query (S12.2.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PCE.QRY_PCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment

.. _hl7-v2_3-QRY_PCK:

QRY_PCK PPP - PC/Pathway (Goal Oriented) Query (S12.2.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_PCK.QRY_PCK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment

.. _hl7-v2_3-QRY_Q01:

QRY_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_Q01.QRY_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-QRY_Q02:

QRY_Q02 QRY/ACK - Query sent for deferred response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_Q02.QRY_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-QRY_R02:

QRY_R02 QRY - Query for results of observation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_R02.QRY_R02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - :ref:`QRF <hl7-v2_3-QRF>`
     - required
     - Query filter segment

.. _hl7-v2_3-QRY_T12:

QRY_T12 QRY/DOC - Document query.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.QRY_T12.QRY_T12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment

.. _hl7-v2_3-RAR_RAR:

RAR_RAR RAR - Pharmacy administration information query response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RAR_RAR.RAR_RAR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``DEFINITION``
     - List[:ref:`RAR_RAR_DEFINITION <hl7-v2_3-RAR_RAR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RAS_O01:

RAS_O01 ORM - Order message (also RDE, RDS, RGV, RAS,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RAS_O01.RAS_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`RAS_O01_PATIENT <hl7-v2_3-RAS_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RAS_O01_ORDER <hl7-v2_3-RAS_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RCI_I05:

RCI_I05 RQC/RCI - Request for patient clinical information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RCI_I05.RCI_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PROVIDER``
     - List[:ref:`RCI_I05_PROVIDER <hl7-v2_3-RCI_I05_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``OBSERVATION``
     - Optional[List[:ref:`RCI_I05_OBSERVATION <hl7-v2_3-RCI_I05_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RCL_I06:

RCL_I06 RQC/RCL - Request/receipt of clinical data listing.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RCL_I06.RCL_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PROVIDER``
     - List[:ref:`RCL_I06_PROVIDER <hl7-v2_3-RCL_I06_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_3-DSP>`]]
     - optional
     - Display data segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RDE_O01:

RDE_O01 ORM - Order message (also RDE, RDS, RGV, RAS,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDE_O01.RDE_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`RDE_O01_PATIENT <hl7-v2_3-RDE_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDE_O01_ORDER <hl7-v2_3-RDE_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RDO_O01:

RDO_O01 HL7 v2 RDO_O01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDO_O01.RDO_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`RDO_O01_PATIENT <hl7-v2_3-RDO_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDO_O01_ORDER <hl7-v2_3-RDO_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RDR_RDR:

RDR_RDR RDR - Pharmacy dispense information query response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDR_RDR.RDR_RDR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``DEFINITION``
     - List[:ref:`RDR_RDR_DEFINITION <hl7-v2_3-RDR_RDR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RDS_O01:

RDS_O01 ORM - Order message (also RDE, RDS, RGV, RAS,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RDS_O01.RDS_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`RDS_O01_PATIENT <hl7-v2_3-RDS_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDS_O01_ORDER <hl7-v2_3-RDS_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-REF_I12:

REF_I12 REF/RRI -  Patient referral.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.REF_I12.REF_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``RESULTS``
     - Optional[List[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]]
     - optional
     - RESULTS
   * - ``VISIT``
     - Optional[:ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-REF_I13:

REF_I13 REF/RRI - Modify patient referral (S11.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.REF_I13.REF_I13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``RESULTS``
     - Optional[List[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]]
     - optional
     - RESULTS
   * - ``VISIT``
     - Optional[:ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-REF_I14:

REF_I14 REF/RRI - Cancel patient referral (S11.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.REF_I14.REF_I14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``RESULTS``
     - Optional[List[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]]
     - optional
     - RESULTS
   * - ``VISIT``
     - Optional[:ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-REF_I15:

REF_I15 REF/RRI - Request patient referral status (S11.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.REF_I15.REF_I15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`REF_I12_AUTHORIZATION <hl7-v2_3-REF_I12_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`REF_I12_PROVIDER <hl7-v2_3-REF_I12_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_3-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_3-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``RESULTS``
     - Optional[List[:ref:`REF_I12_RESULTS <hl7-v2_3-REF_I12_RESULTS>`]]
     - optional
     - RESULTS
   * - ``VISIT``
     - Optional[:ref:`REF_I12_VISIT <hl7-v2_3-REF_I12_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RER_RER:

RER_RER RER - Pharmacy encoded order information query response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RER_RER.RER_RER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``DEFINITION``
     - List[:ref:`RER_RER_DEFINITION <hl7-v2_3-RER_RER_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RGR_RGR:

RGR_RGR RGR - Pharmacy dose information query response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RGR_RGR.RGR_RGR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``DEFINITION``
     - List[:ref:`RGR_RGR_DEFINITION <hl7-v2_3-RGR_RGR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RGV_O01:

RGV_O01 ORM - Order message (also RDE, RDS, RGV, RAS,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RGV_O01.RGV_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`RGV_O01_PATIENT <hl7-v2_3-RGV_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RGV_O01_ORDER <hl7-v2_3-RGV_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-ROR_ROR:

ROR_ROR ROR - Pharmacy prescription order query response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.ROR_ROR.ROR_ROR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``DEFINITION``
     - List[:ref:`ROR_ROR_DEFINITION <hl7-v2_3-ROR_ROR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RPA_I08:

RPA_I08 RQA/RPA - Request for treatment authorization information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RPA_I08.RPA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`RPA_I08_AUTHORIZATION <hl7-v2_3-RPA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RPA_I08_PROVIDER <hl7-v2_3-RPA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`RPA_I08_INSURANCE <hl7-v2_3-RPA_I08_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - List[:ref:`RPA_I08_PROCEDURE <hl7-v2_3-RPA_I08_PROCEDURE>`]
     - required
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RPA_I08_OBSERVATION <hl7-v2_3-RPA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RPA_I08_VISIT <hl7-v2_3-RPA_I08_VISIT>`]
     - optional
     - VISIT

.. _hl7-v2_3-RPI_I01:

RPI_I01 RQI/RPI - Request for insurance information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RPI_I01.RPI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``PROVIDER``
     - List[:ref:`RPI_I01_PROVIDER <hl7-v2_3-RPI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RPI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RPL_I02:

RPL_I02 RQI/RPL - Request/receipt of patient selection display list.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RPL_I02.RPL_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``PROVIDER``
     - List[:ref:`RPL_I02_PROVIDER <hl7-v2_3-RPL_I02_PROVIDER>`]
     - required
     - PROVIDER
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_3-DSP>`]]
     - optional
     - Display data segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RQA_I08:

RQA_I08 RQA/RPA - Request for treatment authorization information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I08.RQA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQA_I09:

RQA_I09 RQA/RPA - Request for modification to an authorization (S11.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I09.RQA_I09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQA_I10:

RQA_I10 RQA/RPA - Request for resubmission of an authorization (S11.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I10.RQA_I10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQA_I11:

RQA_I11 RQA/RPA - Request for cancellation of an authorization (S11.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQA_I11.RQA_I11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_3-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_3-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_3-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_3-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_3-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQC_I05:

RQC_I05 RQC/RCI - Request for patient clinical information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQC_I05.RQC_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PROVIDER``
     - List[:ref:`RQC_I05_PROVIDER <hl7-v2_3-RQC_I05_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQC_I06:

RQC_I06 RQC/RCL - Request/receipt of clinical data listing.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQC_I06.RQC_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PROVIDER``
     - List[:ref:`RQC_I06_PROVIDER <hl7-v2_3-RQC_I06_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     - Guarantor
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQI_I01:

RQI_I01 RQI/RPI - Request for insurance information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQI_I01.RQI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_3-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQI_I02:

RQI_I02 RQI/RPL - Request/receipt of patient selection display list (S11.2.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQI_I02.RQI_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_3-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQI_I03:

RQI_I03 RQI/RPR - Request/receipt of patient selection list (S11.2.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQI_I03.RQI_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_3-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQP_I04:

RQP_I04 RQP/RPI - Request for patient demographic data.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQP_I04.RQP_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PROVIDER``
     - List[:ref:`RQP_I04_PROVIDER <hl7-v2_3-RQP_I04_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQQ_Q01:

RQQ_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RQQ_Q01.RQQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_3-ERQ>`
     - required
     - Event Replay Query Segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-RRA_O02:

RRA_O02 ORR - Order response (also RRE, RRD, RRG, RRA,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRA_O02.RRA_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESPONSE``
     - Optional[:ref:`RRA_O02_RESPONSE <hl7-v2_3-RRA_O02_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_3-RRD_O02:

RRD_O02 ORR - Order response (also RRE, RRD, RRG, RRA,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRD_O02.RRD_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`RRD_O02_PATIENT <hl7-v2_3-RRD_O02_PATIENT>`]
     - optional
     - PATIENT

.. _hl7-v2_3-RRG_O02:

RRG_O02 ORR - Order response (also RRE, RRD, RRG, RRA,.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRG_O02.RRG_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESPONSE``
     - Optional[:ref:`RRG_O02_RESPONSE <hl7-v2_3-RRG_O02_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_3-RRI_I12:

RRI_I12 REF/RRI -  Patient referral.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRI_I12.RRI_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - Optional[:ref:`MSA <hl7-v2_3-MSA>`]
     - optional
     - Message acknowledgement segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_3-RF1>`]
     - optional
     - Referral Information Segment
   * - ``AUTHORIZATION``
     - Optional[:ref:`RRI_I12_AUTHORIZATION <hl7-v2_3-RRI_I12_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RRI_I12_PROVIDER <hl7-v2_3-RRI_I12_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_3-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_3-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RRI_I12_PROCEDURE <hl7-v2_3-RRI_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``RESULTS``
     - Optional[List[:ref:`RRI_I12_RESULTS <hl7-v2_3-RRI_I12_RESULTS>`]]
     - optional
     - RESULTS
   * - ``VISIT``
     - Optional[:ref:`RRI_I12_VISIT <hl7-v2_3-RRI_I12_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RRO_O02:

RRO_O02 HL7 v2 RRO_O02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.RRO_O02.RRO_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESPONSE``
     - Optional[:ref:`RRO_O02_RESPONSE <hl7-v2_3-RRO_O02_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_3-SIU_S12:

SIU_S12 SIU/ACK - Notification of new appointment booking.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S12.SIU_S12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S13:

SIU_S13 SIU/ACK - Notification of appointment rescheduling (S10.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S13.SIU_S13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S14:

SIU_S14 SIU/ACK - Notification of appointment modification (S10.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S14.SIU_S14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S15:

SIU_S15 SIU/ACK - Notification of appointment cancellation (S10.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S15.SIU_S15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S16:

SIU_S16 SIU/ACK - Notification of appointment discontinuation (S10.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S16.SIU_S16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S17:

SIU_S17 SIU/ACK - Notification of appointment deletion (S10.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S17.SIU_S17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S18:

SIU_S18 SIU/ACK - Notification of addition of service/resource on appointment (S10.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S18.SIU_S18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S19:

SIU_S19 SIU/ACK - Notification of modification of service/resource on appointment (S10.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S19.SIU_S19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S20:

SIU_S20 SIU/ACK - Notification of cancellation of service/resource on appointment (S10.3.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S20.SIU_S20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S21:

SIU_S21 SIU/ACK - Notification of discontinuation of service/resource on appointment (S10.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S21.SIU_S21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S22:

SIU_S22 SIU/ACK - Notification of deletion of service/resource on appointment (S10.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S22.SIU_S22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S23:

SIU_S23 SIU/ACK - Notification of blocked schedule time slot(s) (S10.3.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S23.SIU_S23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S24:

SIU_S24 SIU/ACK - Notification of open ("unblocked"") schedule time slot(s)" (S10.3.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S24.SIU_S24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SIU_S26:

SIU_S26 notification that patient did not show up for schedule appointment (S10.3.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SIU_S26.SIU_S26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_3-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_3-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SPQ_Q01:

SPQ_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SPQ_Q01.SPQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``SPR``
     - :ref:`SPR <hl7-v2_3-SPR>`
     - required
     - Stored Procedure Request Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_3-RDF>`]
     - optional
     - Table Row Definition
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-SQM_S25:

SQM_S25 SQM/SQR - Query schedule information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SQM_S25.SQM_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``REQUEST``
     - Optional[:ref:`SQM_S25_REQUEST <hl7-v2_3-SQM_S25_REQUEST>`]
     - optional
     - REQUEST
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-SQR_S25:

SQR_S25 SQM/SQR - Query schedule information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SQR_S25.SQR_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     - Query Acknowledgement
   * - ``SCHEDULE``
     - Optional[List[:ref:`SQR_S25_SCHEDULE <hl7-v2_3-SQR_S25_SCHEDULE>`]]
     - optional
     - SCHEDULE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-SRM_S01:

SRM_S01 SRM/SRR - Request new appointment booking.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S01.SRM_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S02:

SRM_S02 SRM/SRR - Request appointment rescheduling (S10.2.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S02.SRM_S02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S03:

SRM_S03 SRM/SRR - Request appointment modification (S10.2.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S03.SRM_S03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S04:

SRM_S04 SRM/SRR - Request appointment cancellation (S10.2.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S04.SRM_S04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S05:

SRM_S05 SRM/SRR - Request appointment discontinuation (S10.2.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S05.SRM_S05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S06:

SRM_S06 SRM/SRR - Request appointment deletion (S10.2.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S06.SRM_S06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S07:

SRM_S07 SRM/SRR - Request addition of service/resource on appointment (S10.2.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S07.SRM_S07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S08:

SRM_S08 SRM/SRR - Request modification of service/resource on appointment (S10.2.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S08.SRM_S08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S09:

SRM_S09 SRM/SRR - Request cancellation of servic/resource on appointment (S10.2.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S09.SRM_S09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S10:

SRM_S10 SRM/SRR - Request discontinuation of servic/resource on appointment (S10.2.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S10.SRM_S10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRM_S11:

SRM_S11 SRM/SRR - Request deletion of servic/resource on appointment (S10.2.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRM_S11.SRM_S11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_3-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_3-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRR_S01:

SRR_S01 SRM/SRR - Request new appointment booking.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SRR_S01.SRR_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``SCHEDULE``
     - Optional[:ref:`SRR_S01_SCHEDULE <hl7-v2_3-SRR_S01_SCHEDULE>`]
     - optional
     - SCHEDULE

.. _hl7-v2_3-SUR_P09:

SUR_P09 SUR - Summary product experience report.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.SUR_P09.SUR_P09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``FACILITY``
     - List[:ref:`SUR_P09_FACILITY <hl7-v2_3-SUR_P09_FACILITY>`]
     - required
     - FACILITY

.. _hl7-v2_3-TBR_Q01:

TBR_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.TBR_Q01.TBR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_3-ERR>`]
     - optional
     - Error segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_3-QAK>`
     - required
     - Query Acknowledgement
   * - ``RDF``
     - :ref:`RDF <hl7-v2_3-RDF>`
     - required
     - Table Row Definition
   * - ``RDT``
     - List[:ref:`RDT <hl7-v2_3-RDT>`]
     - required
     - Table Row Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-UDM_Q05:

UDM_Q05 UDM/ACK - Unsolicited display update.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``URD``
     - :ref:`URD <hl7-v2_3-URD>`
     - required
     - Results/update definition segment
   * - ``URS``
     - Optional[:ref:`URS <hl7-v2_3-URS>`]
     - optional
     - Unsolicited selection segment
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_3-DSP>`]
     - required
     - Display data segment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-VQQ_Q01:

VQQ_Q01 QRY/DSR - Query sent for immediate response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VQQ_Q01.VQQ_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``VTQ``
     - :ref:`VTQ <hl7-v2_3-VTQ>`
     - required
     - Virtual Table Query Request
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_3-RDF>`]
     - optional
     - Table Row Definition
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_3-DSC>`]
     - optional
     - Continuation pointer segment

.. _hl7-v2_3-VXQ_V01:

VXQ_V01 VXQ - Query for vaccination record.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXQ_V01.VXQ_V01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment

.. _hl7-v2_3-VXR_V03:

VXR_V03 VXR - Vaccination record response.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXR_V03.VXR_V03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PATIENT_VISIT``
     - Optional[:ref:`VXR_V03_PATIENT_VISIT <hl7-v2_3-VXR_V03_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`VXR_V03_INSURANCE <hl7-v2_3-VXR_V03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ORDER``
     - Optional[List[:ref:`VXR_V03_ORDER <hl7-v2_3-VXR_V03_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-VXU_V04:

VXU_V04 VXU - Unsolicited vaccination record update.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXU_V04.VXU_V04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_3-PD1>`]
     - optional
     - Patient Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``PATIENT``
     - Optional[:ref:`VXU_V04_PATIENT <hl7-v2_3-VXU_V04_PATIENT>`]
     - optional
     - PATIENT
   * - ``INSURANCE``
     - Optional[List[:ref:`VXU_V04_INSURANCE <hl7-v2_3-VXU_V04_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ORDER``
     - Optional[List[:ref:`VXU_V04_ORDER <hl7-v2_3-VXU_V04_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-VXX_V02:

VXX_V02 VXX - Response to vaccination query returning multiple PID matches.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.messages.VXX_V02.VXX_V02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_3-MSH>`
     - required
     - Message header segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_3-MSA>`
     - required
     - Message acknowledgement segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PATIENT``
     - List[:ref:`VXX_V02_PATIENT <hl7-v2_3-VXX_V02_PATIENT>`]
     - required
     - PATIENT
