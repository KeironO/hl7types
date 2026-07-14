v2.3 Groups
===========

.. _hl7-v2_3-ADT_A01_INSURANCE:

ADT_A01_INSURANCE HL7 v2 ADT_A01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A01_INSURANCE.ADT_A01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-ADT_A01_PROCEDURE:

ADT_A01_PROCEDURE HL7 v2 ADT_A01.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A01_PROCEDURE.ADT_A01_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_3-ROL>`]]
     - optional
     - Role

.. _hl7-v2_3-ADT_A03_PROCEDURE:

ADT_A03_PROCEDURE HL7 v2 ADT_A03.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A03_PROCEDURE.ADT_A03_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_3-ROL>`]]
     - optional
     - Role

.. _hl7-v2_3-ADT_A06_INSURANCE:

ADT_A06_INSURANCE HL7 v2 ADT_A06.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A06_INSURANCE.ADT_A06_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-ADT_A06_PROCEDURE:

ADT_A06_PROCEDURE HL7 v2 ADT_A06.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A06_PROCEDURE.ADT_A06_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_3-ROL>`]]
     - optional
     - Role

.. _hl7-v2_3-ADT_A39_PATIENT:

ADT_A39_PATIENT HL7 v2 ADT_A39.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A39_PATIENT.ADT_A39_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit

.. _hl7-v2_3-ADT_A43_PATIENT:

ADT_A43_PATIENT HL7 v2 ADT_A43.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A43_PATIENT.ADT_A43_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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

.. _hl7-v2_3-ADT_A45_MERGE_INFO:

ADT_A45_MERGE_INFO HL7 v2 ADT_A45.MERGE_INFO group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ADT_A45_MERGE_INFO.ADT_A45_MERGE_INFO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MRG``
     - :ref:`MRG <hl7-v2_3-MRG>`
     - required
     - Merge patient information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit

.. _hl7-v2_3-ARD_A19_INSURANCE:

ARD_A19_INSURANCE HL7 v2 ARD_A19.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ARD_A19_INSURANCE.ARD_A19_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-ARD_A19_PROCEDURE:

ARD_A19_PROCEDURE HL7 v2 ARD_A19.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ARD_A19_PROCEDURE.ARD_A19_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_3-ROL>`]]
     - optional
     - Role

.. _hl7-v2_3-ARD_A19_QUERY_RESPONSE:

ARD_A19_QUERY_RESPONSE HL7 v2 ARD_A19.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ARD_A19_QUERY_RESPONSE.ARD_A19_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``EVN``
     - Optional[:ref:`EVN <hl7-v2_3-EVN>`]
     - optional
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
     - Optional[List[:ref:`ARD_A19_PROCEDURE <hl7-v2_3-ARD_A19_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ARD_A19_INSURANCE <hl7-v2_3-ARD_A19_INSURANCE>`]]
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

.. _hl7-v2_3-BAR_P01_INSURANCE:

BAR_P01_INSURANCE HL7 v2 BAR_P01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.BAR_P01_INSURANCE.BAR_P01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-BAR_P01_PROCEDURE:

BAR_P01_PROCEDURE HL7 v2 BAR_P01.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.BAR_P01_PROCEDURE.BAR_P01_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_3-ROL>`]]
     - optional
     - Role

.. _hl7-v2_3-BAR_P01_VISIT:

BAR_P01_VISIT HL7 v2 BAR_P01.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.BAR_P01_VISIT.BAR_P01_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
     - Optional[List[:ref:`BAR_P01_PROCEDURE <hl7-v2_3-BAR_P01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
   * - ``INSURANCE``
     - Optional[List[:ref:`BAR_P01_INSURANCE <hl7-v2_3-BAR_P01_INSURANCE>`]]
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

.. _hl7-v2_3-BAR_P02_PATIENT:

BAR_P02_PATIENT HL7 v2 BAR_P02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.BAR_P02_PATIENT.BAR_P02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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

.. _hl7-v2_3-BAR_P06_PATIENT:

BAR_P06_PATIENT HL7 v2 BAR_P06.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.BAR_P06_PATIENT.BAR_P06_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit

.. _hl7-v2_3-CRM_C01_PATIENT:

CRM_C01_PATIENT HL7 v2 CRM_C01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CRM_C01_PATIENT.CRM_C01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``CSR``
     - :ref:`CSR <hl7-v2_3-CSR>`
     - required
     - Clinical Study Registration
   * - ``CSP``
     - Optional[List[:ref:`CSP <hl7-v2_3-CSP>`]]
     - optional
     - Clinical Study Phase

.. _hl7-v2_3-CSU_C09_PATIENT:

CSU_C09_PATIENT HL7 v2 CSU_C09.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CSU_C09_PATIENT.CSU_C09_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
     - Optional[:ref:`CSU_C09_VISIT <hl7-v2_3-CSU_C09_VISIT>`]
     - optional
     - VISIT
   * - ``CSR``
     - :ref:`CSR <hl7-v2_3-CSR>`
     - required
     - Clinical Study Registration
   * - ``STUDY_PHASE``
     - List[:ref:`CSU_C09_STUDY_PHASE <hl7-v2_3-CSU_C09_STUDY_PHASE>`]
     - required
     - STUDY_PHASE

.. _hl7-v2_3-CSU_C09_RX_ADMIN:

CSU_C09_RX_ADMIN HL7 v2 CSU_C09.RX_ADMIN group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CSU_C09_RX_ADMIN.CSU_C09_RX_ADMIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_3-RXA>`
     - required
     - Pharmacy administration segment
   * - ``RXR``
     - :ref:`RXR <hl7-v2_3-RXR>`
     - required
     - Pharmacy route segment

.. _hl7-v2_3-CSU_C09_STUDY_OBSERVATION:

CSU_C09_STUDY_OBSERVATION HL7 v2 CSU_C09.STUDY_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CSU_C09_STUDY_OBSERVATION.CSU_C09_STUDY_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_3-ORC>`]
     - optional
     - Common order segment
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``OBX``
     - List[:ref:`OBX <hl7-v2_3-OBX>`]
     - required
     - Observation segment

.. _hl7-v2_3-CSU_C09_STUDY_PHARM:

CSU_C09_STUDY_PHARM HL7 v2 CSU_C09.STUDY_PHARM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CSU_C09_STUDY_PHARM.CSU_C09_STUDY_PHARM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_3-ORC>`]
     - optional
     - Common order segment
   * - ``RX_ADMIN``
     - List[:ref:`CSU_C09_RX_ADMIN <hl7-v2_3-CSU_C09_RX_ADMIN>`]
     - required
     - RX_ADMIN

.. _hl7-v2_3-CSU_C09_STUDY_PHASE:

CSU_C09_STUDY_PHASE HL7 v2 CSU_C09.STUDY_PHASE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CSU_C09_STUDY_PHASE.CSU_C09_STUDY_PHASE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CSP``
     - Optional[:ref:`CSP <hl7-v2_3-CSP>`]
     - optional
     - Clinical Study Phase
   * - ``STUDY_SCHEDULE``
     - List[:ref:`CSU_C09_STUDY_SCHEDULE <hl7-v2_3-CSU_C09_STUDY_SCHEDULE>`]
     - required
     - STUDY_SCHEDULE

.. _hl7-v2_3-CSU_C09_STUDY_SCHEDULE:

CSU_C09_STUDY_SCHEDULE HL7 v2 CSU_C09.STUDY_SCHEDULE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CSU_C09_STUDY_SCHEDULE.CSU_C09_STUDY_SCHEDULE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CSS``
     - Optional[:ref:`CSS <hl7-v2_3-CSS>`]
     - optional
     - Clinical Study Data Schedule
   * - ``STUDY_OBSERVATION``
     - Optional[List[:ref:`CSU_C09_STUDY_OBSERVATION <hl7-v2_3-CSU_C09_STUDY_OBSERVATION>`]]
     - optional
     - STUDY_OBSERVATION
   * - ``STUDY_PHARM``
     - List[:ref:`CSU_C09_STUDY_PHARM <hl7-v2_3-CSU_C09_STUDY_PHARM>`]
     - required
     - STUDY_PHARM

.. _hl7-v2_3-CSU_C09_VISIT:

CSU_C09_VISIT HL7 v2 CSU_C09.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.CSU_C09_VISIT.CSU_C09_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-DFT_P03_FINANCIAL:

DFT_P03_FINANCIAL HL7 v2 DFT_P03.FINANCIAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.DFT_P03_FINANCIAL.DFT_P03_FINANCIAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``FT1``
     - :ref:`FT1 <hl7-v2_3-FT1>`
     - required
     - Financial transaction
   * - ``FINANCIAL_PROCEDURE``
     - Optional[List[:ref:`DFT_P03_FINANCIAL_PROCEDURE <hl7-v2_3-DFT_P03_FINANCIAL_PROCEDURE>`]]
     - optional
     - FINANCIAL_PROCEDURE

.. _hl7-v2_3-DFT_P03_FINANCIAL_PROCEDURE:

DFT_P03_FINANCIAL_PROCEDURE HL7 v2 DFT_P03.FINANCIAL_PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.DFT_P03_FINANCIAL_PROCEDURE.DFT_P03_FINANCIAL_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_3-ROL>`]]
     - optional
     - Role

.. _hl7-v2_3-DFT_P03_INSURANCE:

DFT_P03_INSURANCE HL7 v2 DFT_P03.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.DFT_P03_INSURANCE.DFT_P03_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-DOC_T12_RESULT:

DOC_T12_RESULT HL7 v2 DOC_T12.RESULT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.DOC_T12_RESULT.DOC_T12_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``EVN``
     - Optional[:ref:`EVN <hl7-v2_3-EVN>`]
     - optional
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
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-MFN_M01_MF:

MFN_M01_MF HL7 v2 MFN_M01.MF group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M01_MF.MFN_M01_MF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment

.. _hl7-v2_3-MFN_M02_MF_STAFF:

MFN_M02_MF_STAFF HL7 v2 MFN_M02.MF_STAFF group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M02_MF_STAFF.MFN_M02_MF_STAFF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``STF``
     - :ref:`STF <hl7-v2_3-STF>`
     - required
     - Staff identification segment
   * - ``PRA``
     - Optional[:ref:`PRA <hl7-v2_3-PRA>`]
     - optional
     - Practitioner detail segment

.. _hl7-v2_3-MFN_M03_MF_TEST:

MFN_M03_MF_TEST HL7 v2 MFN_M03.MF_TEST group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M03_MF_TEST.MFN_M03_MF_TEST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_3-OM1>`
     - required
     - General - fields that apply to most observations

.. _hl7-v2_3-MFN_M05_MF_LOCATION:

MFN_M05_MF_LOCATION HL7 v2 MFN_M05.MF_LOCATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M05_MF_LOCATION.MFN_M05_MF_LOCATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``LOC``
     - :ref:`LOC <hl7-v2_3-LOC>`
     - required
     - Location Identification
   * - ``LCH``
     - Optional[List[:ref:`LCH <hl7-v2_3-LCH>`]]
     - optional
     - Location Characteristic
   * - ``LRL``
     - Optional[List[:ref:`LRL <hl7-v2_3-LRL>`]]
     - optional
     - Location Relationship
   * - ``MF_LOC_DEPT``
     - List[:ref:`MFN_M05_MF_LOC_DEPT <hl7-v2_3-MFN_M05_MF_LOC_DEPT>`]
     - required
     - MF_LOC_DEPT

.. _hl7-v2_3-MFN_M05_MF_LOC_DEPT:

MFN_M05_MF_LOC_DEPT HL7 v2 MFN_M05.MF_LOC_DEPT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M05_MF_LOC_DEPT.MFN_M05_MF_LOC_DEPT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``LDP``
     - :ref:`LDP <hl7-v2_3-LDP>`
     - required
     - Location Department
   * - ``LCH``
     - Optional[List[:ref:`LCH <hl7-v2_3-LCH>`]]
     - optional
     - Location Characteristic
   * - ``LCC``
     - Optional[List[:ref:`LCC <hl7-v2_3-LCC>`]]
     - optional
     - Location Charge Code

.. _hl7-v2_3-MFN_M06_MF_CDM:

MFN_M06_MF_CDM HL7 v2 MFN_M06.MF_CDM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M06_MF_CDM.MFN_M06_MF_CDM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``CDM``
     - :ref:`CDM <hl7-v2_3-CDM>`
     - required
     - Charge Description Master
   * - ``PRC``
     - Optional[List[:ref:`PRC <hl7-v2_3-PRC>`]]
     - optional
     - Pricing

.. _hl7-v2_3-MFN_M07_MF_CLIN_STUDY:

MFN_M07_MF_CLIN_STUDY HL7 v2 MFN_M07.MF_CLIN_STUDY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M07_MF_CLIN_STUDY.MFN_M07_MF_CLIN_STUDY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``CM0``
     - :ref:`CM0 <hl7-v2_3-CM0>`
     - required
     - Clinical Study Master
   * - ``MF_PHASE_SCHED_DETAIL``
     - Optional[List[:ref:`MFN_M07_MF_PHASE_SCHED_DETAIL <hl7-v2_3-MFN_M07_MF_PHASE_SCHED_DETAIL>`]]
     - optional
     - MF_PHASE_SCHED_DETAIL

.. _hl7-v2_3-MFN_M07_MF_PHASE_SCHED_DETAIL:

MFN_M07_MF_PHASE_SCHED_DETAIL HL7 v2 MFN_M07.MF_PHASE_SCHED_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M07_MF_PHASE_SCHED_DETAIL.MFN_M07_MF_PHASE_SCHED_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CM1``
     - :ref:`CM1 <hl7-v2_3-CM1>`
     - required
     - Clinical Study Phase Master
   * - ``CM2``
     - Optional[List[:ref:`CM2 <hl7-v2_3-CM2>`]]
     - optional
     - Clinical Study Schedule Master

.. _hl7-v2_3-MFN_M08_MF_NUMERIC_OBSERVATION:

MFN_M08_MF_NUMERIC_OBSERVATION HL7 v2 MFN_M08.MF_NUMERIC_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M08_MF_NUMERIC_OBSERVATION.MFN_M08_MF_NUMERIC_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OM2``
     - Optional[:ref:`OM2 <hl7-v2_3-OM2>`]
     - optional
     - Numeric observation
   * - ``OM3``
     - Optional[:ref:`OM3 <hl7-v2_3-OM3>`]
     - optional
     - Categorical test/observation
   * - ``OM4``
     - Optional[:ref:`OM4 <hl7-v2_3-OM4>`]
     - optional
     - Observations that require specimens

.. _hl7-v2_3-MFN_M08_MF_TEST_NUMERIC:

MFN_M08_MF_TEST_NUMERIC HL7 v2 MFN_M08.MF_TEST_NUMERIC group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M08_MF_TEST_NUMERIC.MFN_M08_MF_TEST_NUMERIC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_3-OM1>`
     - required
     - General - fields that apply to most observations
   * - ``MF_NUMERIC_OBSERVATION``
     - Optional[:ref:`MFN_M08_MF_NUMERIC_OBSERVATION <hl7-v2_3-MFN_M08_MF_NUMERIC_OBSERVATION>`]
     - optional
     - MF_NUMERIC_OBSERVATION

.. _hl7-v2_3-MFN_M09_MF_TEST_CATEGORICAL:

MFN_M09_MF_TEST_CATEGORICAL HL7 v2 MFN_M09.MF_TEST_CATEGORICAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M09_MF_TEST_CATEGORICAL.MFN_M09_MF_TEST_CATEGORICAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``MF_TEST_CAT_DETAIL``
     - Optional[:ref:`MFN_M09_MF_TEST_CAT_DETAIL <hl7-v2_3-MFN_M09_MF_TEST_CAT_DETAIL>`]
     - optional
     - MF_TEST_CAT_DETAIL

.. _hl7-v2_3-MFN_M09_MF_TEST_CAT_DETAIL:

MFN_M09_MF_TEST_CAT_DETAIL HL7 v2 MFN_M09.MF_TEST_CAT_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M09_MF_TEST_CAT_DETAIL.MFN_M09_MF_TEST_CAT_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OM3``
     - :ref:`OM3 <hl7-v2_3-OM3>`
     - required
     - Categorical test/observation
   * - ``OM4``
     - Optional[List[:ref:`OM4 <hl7-v2_3-OM4>`]]
     - optional
     - Observations that require specimens

.. _hl7-v2_3-MFN_M10_MF_TEST_BATTERIES:

MFN_M10_MF_TEST_BATTERIES HL7 v2 MFN_M10.MF_TEST_BATTERIES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M10_MF_TEST_BATTERIES.MFN_M10_MF_TEST_BATTERIES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MF_TEST_BATT_DETAIL``
     - Optional[:ref:`MFN_M10_MF_TEST_BATT_DETAIL <hl7-v2_3-MFN_M10_MF_TEST_BATT_DETAIL>`]
     - optional
     - MF_TEST_BATT_DETAIL

.. _hl7-v2_3-MFN_M10_MF_TEST_BATT_DETAIL:

MFN_M10_MF_TEST_BATT_DETAIL HL7 v2 MFN_M10.MF_TEST_BATT_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M10_MF_TEST_BATT_DETAIL.MFN_M10_MF_TEST_BATT_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OM5``
     - :ref:`OM5 <hl7-v2_3-OM5>`
     - required
     - Observation batteries
   * - ``OM4``
     - Optional[List[:ref:`OM4 <hl7-v2_3-OM4>`]]
     - optional
     - Observations that require specimens

.. _hl7-v2_3-MFN_M11_MF_TEST_CALCULATED:

MFN_M11_MF_TEST_CALCULATED HL7 v2 MFN_M11.MF_TEST_CALCULATED group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M11_MF_TEST_CALCULATED.MFN_M11_MF_TEST_CALCULATED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_3-MFE>`
     - required
     - Master file entry segment
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_3-OM1>`
     - required
     - General - fields that apply to most observations
   * - ``MF_TEST_CALC_DETAIL``
     - Optional[:ref:`MFN_M11_MF_TEST_CALC_DETAIL <hl7-v2_3-MFN_M11_MF_TEST_CALC_DETAIL>`]
     - optional
     - MF_TEST_CALC_DETAIL

.. _hl7-v2_3-MFN_M11_MF_TEST_CALC_DETAIL:

MFN_M11_MF_TEST_CALC_DETAIL HL7 v2 MFN_M11.MF_TEST_CALC_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.MFN_M11_MF_TEST_CALC_DETAIL.MFN_M11_MF_TEST_CALC_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OM6``
     - :ref:`OM6 <hl7-v2_3-OM6>`
     - required
     - Observations that are calculated from other observations
   * - ``OM2``
     - :ref:`OM2 <hl7-v2_3-OM2>`
     - required
     - Numeric observation

.. _hl7-v2_3-OMD_O01_DIET:

OMD_O01_DIET HL7 v2 OMD_O01.DIET group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMD_O01_DIET.OMD_O01_DIET
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ODS``
     - List[:ref:`ODS <hl7-v2_3-ODS>`]
     - required
     - Dietary orders, supplements, and preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``OBSERVATION``
     - List[:ref:`OMD_O01_OBSERVATION <hl7-v2_3-OMD_O01_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_3-OMD_O01_INSURANCE:

OMD_O01_INSURANCE HL7 v2 OMD_O01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMD_O01_INSURANCE.OMD_O01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-OMD_O01_OBSERVATION:

OMD_O01_OBSERVATION HL7 v2 OMD_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMD_O01_OBSERVATION.OMD_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-OMD_O01_ORDER_DIET:

OMD_O01_ORDER_DIET HL7 v2 OMD_O01.ORDER_DIET group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMD_O01_ORDER_DIET.OMD_O01_ORDER_DIET
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``DIET``
     - Optional[:ref:`OMD_O01_DIET <hl7-v2_3-OMD_O01_DIET>`]
     - optional
     - DIET

.. _hl7-v2_3-OMD_O01_ORDER_TRAY:

OMD_O01_ORDER_TRAY HL7 v2 OMD_O01.ORDER_TRAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMD_O01_ORDER_TRAY.OMD_O01_ORDER_TRAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ODT``
     - List[:ref:`ODT <hl7-v2_3-ODT>`]
     - required
     - Diet tray instructions segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-OMD_O01_PATIENT:

OMD_O01_PATIENT HL7 v2 OMD_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMD_O01_PATIENT.OMD_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMD_O01_PATIENT_VISIT <hl7-v2_3-OMD_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMD_O01_INSURANCE <hl7-v2_3-OMD_O01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_3-OMD_O01_PATIENT_VISIT:

OMD_O01_PATIENT_VISIT HL7 v2 OMD_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMD_O01_PATIENT_VISIT.OMD_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-OMN_O01_INSURANCE:

OMN_O01_INSURANCE HL7 v2 OMN_O01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMN_O01_INSURANCE.OMN_O01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-OMN_O01_OBSERVATION:

OMN_O01_OBSERVATION HL7 v2 OMN_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMN_O01_OBSERVATION.OMN_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-OMN_O01_ORDER:

OMN_O01_ORDER HL7 v2 OMN_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMN_O01_ORDER.OMN_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`OMN_O01_ORDER_DETAIL <hl7-v2_3-OMN_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_3-BLG>`]
     - optional
     - Billing Segment

.. _hl7-v2_3-OMN_O01_ORDER_DETAIL:

OMN_O01_ORDER_DETAIL HL7 v2 OMN_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMN_O01_ORDER_DETAIL.OMN_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RQD``
     - :ref:`RQD <hl7-v2_3-RQD>`
     - required
     - Requisition detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_3-RQ1>`]
     - optional
     - Requisition detail-1 segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`OMN_O01_OBSERVATION <hl7-v2_3-OMN_O01_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-OMN_O01_PATIENT:

OMN_O01_PATIENT HL7 v2 OMN_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMN_O01_PATIENT.OMN_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMN_O01_PATIENT_VISIT <hl7-v2_3-OMN_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMN_O01_INSURANCE <hl7-v2_3-OMN_O01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_3-OMN_O01_PATIENT_VISIT:

OMN_O01_PATIENT_VISIT HL7 v2 OMN_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMN_O01_PATIENT_VISIT.OMN_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-OMS_O01_INSURANCE:

OMS_O01_INSURANCE HL7 v2 OMS_O01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMS_O01_INSURANCE.OMS_O01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-OMS_O01_OBSERVATION:

OMS_O01_OBSERVATION HL7 v2 OMS_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMS_O01_OBSERVATION.OMS_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-OMS_O01_ORDER:

OMS_O01_ORDER HL7 v2 OMS_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMS_O01_ORDER.OMS_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`OMS_O01_ORDER_DETAIL <hl7-v2_3-OMS_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_3-BLG>`]
     - optional
     - Billing Segment

.. _hl7-v2_3-OMS_O01_ORDER_DETAIL:

OMS_O01_ORDER_DETAIL HL7 v2 OMS_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMS_O01_ORDER_DETAIL.OMS_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RQD``
     - :ref:`RQD <hl7-v2_3-RQD>`
     - required
     - Requisition detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`OMS_O01_OBSERVATION <hl7-v2_3-OMS_O01_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-OMS_O01_PATIENT:

OMS_O01_PATIENT HL7 v2 OMS_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMS_O01_PATIENT.OMS_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMS_O01_PATIENT_VISIT <hl7-v2_3-OMS_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMS_O01_INSURANCE <hl7-v2_3-OMS_O01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_3-OMS_O01_PATIENT_VISIT:

OMS_O01_PATIENT_VISIT HL7 v2 OMS_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OMS_O01_PATIENT_VISIT.OMS_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-ORD_O02_ORDER_DIET:

ORD_O02_ORDER_DIET HL7 v2 ORD_O02.ORDER_DIET group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORD_O02_ORDER_DIET.ORD_O02_ORDER_DIET
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ODS``
     - Optional[List[:ref:`ODS <hl7-v2_3-ODS>`]]
     - optional
     - Dietary orders, supplements, and preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORD_O02_ORDER_TRAY:

ORD_O02_ORDER_TRAY HL7 v2 ORD_O02.ORDER_TRAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORD_O02_ORDER_TRAY.ORD_O02_ORDER_TRAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ODT``
     - Optional[List[:ref:`ODT <hl7-v2_3-ODT>`]]
     - optional
     - Diet tray instructions segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORD_O02_PATIENT:

ORD_O02_PATIENT HL7 v2 ORD_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORD_O02_PATIENT.ORD_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORD_O02_RESPONSE:

ORD_O02_RESPONSE HL7 v2 ORD_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORD_O02_RESPONSE.ORD_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORD_O02_PATIENT <hl7-v2_3-ORD_O02_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_DIET``
     - List[:ref:`ORD_O02_ORDER_DIET <hl7-v2_3-ORD_O02_ORDER_DIET>`]
     - required
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - Optional[List[:ref:`ORD_O02_ORDER_TRAY <hl7-v2_3-ORD_O02_ORDER_TRAY>`]]
     - optional
     - ORDER_TRAY

.. _hl7-v2_3-ORF_R04_OBSERVATION:

ORF_R04_OBSERVATION HL7 v2 ORF_R04.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORF_R04_OBSERVATION.ORF_R04_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_3-OBX>`]
     - optional
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORF_R04_ORDER:

ORF_R04_ORDER HL7 v2 ORF_R04.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORF_R04_ORDER.ORF_R04_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_3-ORC>`]
     - optional
     - Common order segment
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``OBSERVATION``
     - List[:ref:`ORF_R04_OBSERVATION <hl7-v2_3-ORF_R04_OBSERVATION>`]
     - required
     - OBSERVATION
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_3-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_3-ORF_R04_PATIENT:

ORF_R04_PATIENT HL7 v2 ORF_R04.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORF_R04_PATIENT.ORF_R04_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORF_R04_QUERY_RESPONSE:

ORF_R04_QUERY_RESPONSE HL7 v2 ORF_R04.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORF_R04_QUERY_RESPONSE.ORF_R04_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORF_R04_PATIENT <hl7-v2_3-ORF_R04_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORF_R04_ORDER <hl7-v2_3-ORF_R04_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-ORM_O01_CHOICE:

ORM_O01_CHOICE HL7 v2 ORM_O01.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORM_O01_CHOICE.ORM_O01_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_3-OBR>`]
     - optional
     - Observation request segment
   * - ``RQD``
     - Optional[:ref:`RQD <hl7-v2_3-RQD>`]
     - optional
     - Requisition detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_3-RQ1>`]
     - optional
     - Requisition detail-1 segment
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_3-RXO>`]
     - optional
     - Pharmacy prescription order segment
   * - ``ODS``
     - Optional[:ref:`ODS <hl7-v2_3-ODS>`]
     - optional
     - Dietary orders, supplements, and preferences
   * - ``ODT``
     - Optional[:ref:`ODT <hl7-v2_3-ODT>`]
     - optional
     - Diet tray instructions segment

.. _hl7-v2_3-ORM_O01_INSURANCE:

ORM_O01_INSURANCE HL7 v2 ORM_O01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORM_O01_INSURANCE.ORM_O01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-ORM_O01_OBSERVATION:

ORM_O01_OBSERVATION HL7 v2 ORM_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORM_O01_OBSERVATION.ORM_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORM_O01_ORDER:

ORM_O01_ORDER HL7 v2 ORM_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORM_O01_ORDER.ORM_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`ORM_O01_ORDER_DETAIL <hl7-v2_3-ORM_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``CTI``
     - Optional[:ref:`CTI <hl7-v2_3-CTI>`]
     - optional
     - Clinical Trial Identification
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_3-BLG>`]
     - optional
     - Billing Segment

.. _hl7-v2_3-ORM_O01_ORDER_DETAIL:

ORM_O01_ORDER_DETAIL HL7 v2 ORM_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`ORM_O01_CHOICE <hl7-v2_3-ORM_O01_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis
   * - ``OBSERVATION``
     - Optional[List[:ref:`ORM_O01_OBSERVATION <hl7-v2_3-ORM_O01_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-ORM_O01_PATIENT:

ORM_O01_PATIENT HL7 v2 ORM_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORM_O01_PATIENT.ORM_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``PATIENT_VISIT``
     - Optional[:ref:`ORM_O01_PATIENT_VISIT <hl7-v2_3-ORM_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`ORM_O01_INSURANCE <hl7-v2_3-ORM_O01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_3-ORM_O01_PATIENT_VISIT:

ORM_O01_PATIENT_VISIT HL7 v2 ORM_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORM_O01_PATIENT_VISIT.ORM_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-ORN_O02_ORDER:

ORN_O02_ORDER HL7 v2 ORN_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORN_O02_ORDER.ORN_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``RQD``
     - :ref:`RQD <hl7-v2_3-RQD>`
     - required
     - Requisition detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_3-RQ1>`]
     - optional
     - Requisition detail-1 segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORN_O02_PATIENT:

ORN_O02_PATIENT HL7 v2 ORN_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORN_O02_PATIENT.ORN_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORN_O02_RESPONSE:

ORN_O02_RESPONSE HL7 v2 ORN_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORN_O02_RESPONSE.ORN_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORN_O02_PATIENT <hl7-v2_3-ORN_O02_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORN_O02_ORDER <hl7-v2_3-ORN_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-ORR_O02_CHOICE:

ORR_O02_CHOICE HL7 v2 ORR_O02.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORR_O02_CHOICE.ORR_O02_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_3-OBR>`]
     - optional
     - Observation request segment
   * - ``RQD``
     - Optional[:ref:`RQD <hl7-v2_3-RQD>`]
     - optional
     - Requisition detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_3-RQ1>`]
     - optional
     - Requisition detail-1 segment
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_3-RXO>`]
     - optional
     - Pharmacy prescription order segment
   * - ``ODS``
     - Optional[:ref:`ODS <hl7-v2_3-ODS>`]
     - optional
     - Dietary orders, supplements, and preferences
   * - ``ODT``
     - Optional[:ref:`ODT <hl7-v2_3-ODT>`]
     - optional
     - Diet tray instructions segment

.. _hl7-v2_3-ORR_O02_ORDER:

ORR_O02_ORDER HL7 v2 ORR_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORR_O02_ORDER.ORR_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``CHOICE``
     - :ref:`ORR_O02_CHOICE <hl7-v2_3-ORR_O02_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_3-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_3-ORR_O02_PATIENT:

ORR_O02_PATIENT HL7 v2 ORR_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORR_O02_PATIENT.ORR_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORR_O02_RESPONSE:

ORR_O02_RESPONSE HL7 v2 ORR_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORR_O02_RESPONSE.ORR_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORR_O02_PATIENT <hl7-v2_3-ORR_O02_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORR_O02_ORDER <hl7-v2_3-ORR_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-ORU_R01_OBSERVATION:

ORU_R01_OBSERVATION HL7 v2 ORU_R01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORU_R01_OBSERVATION.ORU_R01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_3-OBX>`]
     - optional
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-ORU_R01_ORDER_OBSERVATION:

ORU_R01_ORDER_OBSERVATION HL7 v2 ORU_R01.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORU_R01_ORDER_OBSERVATION.ORU_R01_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_3-ORC>`]
     - optional
     - Common order segment
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``OBSERVATION``
     - List[:ref:`ORU_R01_OBSERVATION <hl7-v2_3-ORU_R01_OBSERVATION>`]
     - required
     - OBSERVATION
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_3-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_3-ORU_R01_PATIENT:

ORU_R01_PATIENT HL7 v2 ORU_R01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORU_R01_PATIENT.ORU_R01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
     - Optional[:ref:`ORU_R01_VISIT <hl7-v2_3-ORU_R01_VISIT>`]
     - optional
     - VISIT

.. _hl7-v2_3-ORU_R01_RESPONSE:

ORU_R01_RESPONSE HL7 v2 ORU_R01.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORU_R01_RESPONSE.ORU_R01_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORU_R01_PATIENT <hl7-v2_3-ORU_R01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_OBSERVATION``
     - List[:ref:`ORU_R01_ORDER_OBSERVATION <hl7-v2_3-ORU_R01_ORDER_OBSERVATION>`]
     - required
     - ORDER_OBSERVATION

.. _hl7-v2_3-ORU_R01_VISIT:

ORU_R01_VISIT HL7 v2 ORU_R01.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ORU_R01_VISIT.ORU_R01_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-OSR_Q06_ORDER:

OSR_Q06_ORDER HL7 v2 OSR_Q06.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OSR_Q06_ORDER.OSR_Q06_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_3-OBR>`]
     - optional
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_3-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_3-OSR_Q06_PATIENT:

OSR_Q06_PATIENT HL7 v2 OSR_Q06.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OSR_Q06_PATIENT.OSR_Q06_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-OSR_Q06_RESPONSE:

OSR_Q06_RESPONSE HL7 v2 OSR_Q06.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.OSR_Q06_RESPONSE.OSR_Q06_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`OSR_Q06_PATIENT <hl7-v2_3-OSR_Q06_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OSR_Q06_ORDER <hl7-v2_3-OSR_Q06_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-PEX_P07_ASSOCIATED_PERSON:

PEX_P07_ASSOCIATED_PERSON HL7 v2 PEX_P07.ASSOCIATED_PERSON group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_ASSOCIATED_PERSON.PEX_P07_ASSOCIATED_PERSON
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NK1``
     - :ref:`NK1 <hl7-v2_3-NK1>`
     - required
     - Next of kin
   * - ``ASSOCIATED_RX_ORDER``
     - Optional[:ref:`PEX_P07_ASSOCIATED_RX_ORDER <hl7-v2_3-PEX_P07_ASSOCIATED_RX_ORDER>`]
     - optional
     - ASSOCIATED_RX_ORDER
   * - ``ASSOCIATED_RX_ADMIN``
     - Optional[List[:ref:`PEX_P07_ASSOCIATED_RX_ADMIN <hl7-v2_3-PEX_P07_ASSOCIATED_RX_ADMIN>`]]
     - optional
     - ASSOCIATED_RX_ADMIN
   * - ``PRB``
     - Optional[List[:ref:`PRB <hl7-v2_3-PRB>`]]
     - optional
     - Problem Detail
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment

.. _hl7-v2_3-PEX_P07_ASSOCIATED_RX_ADMIN:

PEX_P07_ASSOCIATED_RX_ADMIN HL7 v2 PEX_P07.ASSOCIATED_RX_ADMIN group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_ASSOCIATED_RX_ADMIN.PEX_P07_ASSOCIATED_RX_ADMIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_3-RXA>`
     - required
     - Pharmacy administration segment
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_3-RXR>`]
     - optional
     - Pharmacy route segment

.. _hl7-v2_3-PEX_P07_ASSOCIATED_RX_ORDER:

PEX_P07_ASSOCIATED_RX_ORDER HL7 v2 PEX_P07.ASSOCIATED_RX_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_ASSOCIATED_RX_ORDER.PEX_P07_ASSOCIATED_RX_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - Optional[List[:ref:`RXR <hl7-v2_3-RXR>`]]
     - optional
     - Pharmacy route segment

.. _hl7-v2_3-PEX_P07_EXPERIENCE:

PEX_P07_EXPERIENCE HL7 v2 PEX_P07.EXPERIENCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_EXPERIENCE.PEX_P07_EXPERIENCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PES``
     - :ref:`PES <hl7-v2_3-PES>`
     - required
     - Product Experience Sender
   * - ``PEX_OBSERVATION``
     - List[:ref:`PEX_P07_PEX_OBSERVATION <hl7-v2_3-PEX_P07_PEX_OBSERVATION>`]
     - required
     - PEX_OBSERVATION

.. _hl7-v2_3-PEX_P07_PEX_CAUSE:

PEX_P07_PEX_CAUSE HL7 v2 PEX_P07.PEX_CAUSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_PEX_CAUSE.PEX_P07_PEX_CAUSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PCR``
     - :ref:`PCR <hl7-v2_3-PCR>`
     - required
     - Possible Causal Relationship
   * - ``RX_ORDER``
     - Optional[:ref:`PEX_P07_RX_ORDER <hl7-v2_3-PEX_P07_RX_ORDER>`]
     - optional
     - RX_ORDER
   * - ``RX_ADMINISTRATION``
     - Optional[List[:ref:`PEX_P07_RX_ADMINISTRATION <hl7-v2_3-PEX_P07_RX_ADMINISTRATION>`]]
     - optional
     - RX_ADMINISTRATION
   * - ``PRB``
     - Optional[List[:ref:`PRB <hl7-v2_3-PRB>`]]
     - optional
     - Problem Detail
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``ASSOCIATED_PERSON``
     - Optional[:ref:`PEX_P07_ASSOCIATED_PERSON <hl7-v2_3-PEX_P07_ASSOCIATED_PERSON>`]
     - optional
     - ASSOCIATED_PERSON
   * - ``STUDY``
     - Optional[List[:ref:`PEX_P07_STUDY <hl7-v2_3-PEX_P07_STUDY>`]]
     - optional
     - STUDY

.. _hl7-v2_3-PEX_P07_PEX_OBSERVATION:

PEX_P07_PEX_OBSERVATION HL7 v2 PEX_P07.PEX_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_PEX_OBSERVATION.PEX_P07_PEX_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PEO``
     - :ref:`PEO <hl7-v2_3-PEO>`
     - required
     - Product Experience Observation
   * - ``PEX_CAUSE``
     - List[:ref:`PEX_P07_PEX_CAUSE <hl7-v2_3-PEX_P07_PEX_CAUSE>`]
     - required
     - PEX_CAUSE

.. _hl7-v2_3-PEX_P07_RX_ADMINISTRATION:

PEX_P07_RX_ADMINISTRATION HL7 v2 PEX_P07.RX_ADMINISTRATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_RX_ADMINISTRATION.PEX_P07_RX_ADMINISTRATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_3-RXA>`
     - required
     - Pharmacy administration segment
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_3-RXR>`]
     - optional
     - Pharmacy route segment

.. _hl7-v2_3-PEX_P07_RX_ORDER:

PEX_P07_RX_ORDER HL7 v2 PEX_P07.RX_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_RX_ORDER.PEX_P07_RX_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - Optional[List[:ref:`RXR <hl7-v2_3-RXR>`]]
     - optional
     - Pharmacy route segment

.. _hl7-v2_3-PEX_P07_STUDY:

PEX_P07_STUDY HL7 v2 PEX_P07.STUDY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_STUDY.PEX_P07_STUDY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CSR``
     - :ref:`CSR <hl7-v2_3-CSR>`
     - required
     - Clinical Study Registration
   * - ``CSP``
     - Optional[List[:ref:`CSP <hl7-v2_3-CSP>`]]
     - optional
     - Clinical Study Phase

.. _hl7-v2_3-PEX_P07_VISIT:

PEX_P07_VISIT HL7 v2 PEX_P07.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PEX_P07_VISIT.PEX_P07_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PGL_PC6_GOAL:

PGL_PC6_GOAL HL7 v2 PGL_PC6.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_GOAL.PGL_PC6_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PGL_PC6_GOAL_ROLE <hl7-v2_3-PGL_PC6_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``PATHWAY``
     - Optional[List[:ref:`PGL_PC6_PATHWAY <hl7-v2_3-PGL_PC6_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``OBSERVATION``
     - Optional[List[:ref:`PGL_PC6_OBSERVATION <hl7-v2_3-PGL_PC6_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PGL_PC6_PROBLEM <hl7-v2_3-PGL_PC6_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PGL_PC6_ORDER <hl7-v2_3-PGL_PC6_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PGL_PC6_GOAL_ROLE:

PGL_PC6_GOAL_ROLE HL7 v2 PGL_PC6.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_GOAL_ROLE.PGL_PC6_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PGL_PC6_OBSERVATION:

PGL_PC6_OBSERVATION HL7 v2 PGL_PC6.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_OBSERVATION.PGL_PC6_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PGL_PC6_ORDER:

PGL_PC6_ORDER HL7 v2 PGL_PC6.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_ORDER.PGL_PC6_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PGL_PC6_ORDER_DETAIL <hl7-v2_3-PGL_PC6_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PGL_PC6_ORDER_DETAIL:

PGL_PC6_ORDER_DETAIL HL7 v2 PGL_PC6.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_ORDER_DETAIL.PGL_PC6_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PGL_PC6_ORDER_OBSERVATION <hl7-v2_3-PGL_PC6_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PGL_PC6_ORDER_OBSERVATION:

PGL_PC6_ORDER_OBSERVATION HL7 v2 PGL_PC6.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_ORDER_OBSERVATION.PGL_PC6_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PGL_PC6_PATHWAY:

PGL_PC6_PATHWAY HL7 v2 PGL_PC6.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_PATHWAY.PGL_PC6_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PGL_PC6_PATIENT_VISIT:

PGL_PC6_PATIENT_VISIT HL7 v2 PGL_PC6.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_PATIENT_VISIT.PGL_PC6_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PGL_PC6_PROBLEM:

PGL_PC6_PROBLEM HL7 v2 PGL_PC6.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_PROBLEM.PGL_PC6_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PGL_PC6_PROBLEM_ROLE <hl7-v2_3-PGL_PC6_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PGL_PC6_PROBLEM_OBSERVATION <hl7-v2_3-PGL_PC6_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_3-PGL_PC6_PROBLEM_OBSERVATION:

PGL_PC6_PROBLEM_OBSERVATION HL7 v2 PGL_PC6.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_PROBLEM_OBSERVATION.PGL_PC6_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PGL_PC6_PROBLEM_ROLE:

PGL_PC6_PROBLEM_ROLE HL7 v2 PGL_PC6.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PGL_PC6_PROBLEM_ROLE.PGL_PC6_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PIN_I07_GUARANTOR_INSURANCE:

PIN_I07_GUARANTOR_INSURANCE HL7 v2 PIN_I07.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PIN_I07_GUARANTOR_INSURANCE.PIN_I07_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`PIN_I07_INSURANCE <hl7-v2_3-PIN_I07_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_3-PIN_I07_INSURANCE:

PIN_I07_INSURANCE HL7 v2 PIN_I07.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PIN_I07_INSURANCE.PIN_I07_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-PIN_I07_PROVIDER:

PIN_I07_PROVIDER HL7 v2 PIN_I07.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PIN_I07_PROVIDER.PIN_I07_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-PPG_PCG_GOAL:

PPG_PCG_GOAL HL7 v2 PPG_PCG.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_GOAL.PPG_PCG_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPG_PCG_GOAL_ROLE <hl7-v2_3-PPG_PCG_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPG_PCG_GOAL_OBSERVATION <hl7-v2_3-PPG_PCG_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PPG_PCG_PROBLEM <hl7-v2_3-PPG_PCG_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PPG_PCG_ORDER <hl7-v2_3-PPG_PCG_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PPG_PCG_GOAL_OBSERVATION:

PPG_PCG_GOAL_OBSERVATION HL7 v2 PPG_PCG.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_GOAL_OBSERVATION.PPG_PCG_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPG_PCG_GOAL_ROLE:

PPG_PCG_GOAL_ROLE HL7 v2 PPG_PCG.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_GOAL_ROLE.PPG_PCG_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPG_PCG_ORDER:

PPG_PCG_ORDER HL7 v2 PPG_PCG.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_ORDER.PPG_PCG_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPG_PCG_ORDER_DETAIL <hl7-v2_3-PPG_PCG_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PPG_PCG_ORDER_DETAIL:

PPG_PCG_ORDER_DETAIL HL7 v2 PPG_PCG.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_ORDER_DETAIL.PPG_PCG_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPG_PCG_ORDER_OBSERVATION <hl7-v2_3-PPG_PCG_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PPG_PCG_ORDER_OBSERVATION:

PPG_PCG_ORDER_OBSERVATION HL7 v2 PPG_PCG.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_ORDER_OBSERVATION.PPG_PCG_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPG_PCG_PATHWAY:

PPG_PCG_PATHWAY HL7 v2 PPG_PCG.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_PATHWAY.PPG_PCG_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PPG_PCG_PATHWAY_ROLE <hl7-v2_3-PPG_PCG_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``GOAL``
     - Optional[List[:ref:`PPG_PCG_GOAL <hl7-v2_3-PPG_PCG_GOAL>`]]
     - optional
     - GOAL

.. _hl7-v2_3-PPG_PCG_PATHWAY_ROLE:

PPG_PCG_PATHWAY_ROLE HL7 v2 PPG_PCG.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_PATHWAY_ROLE.PPG_PCG_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPG_PCG_PATIENT_VISIT:

PPG_PCG_PATIENT_VISIT HL7 v2 PPG_PCG.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_PATIENT_VISIT.PPG_PCG_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PPG_PCG_PROBLEM:

PPG_PCG_PROBLEM HL7 v2 PPG_PCG.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_PROBLEM.PPG_PCG_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPG_PCG_PROBLEM_ROLE <hl7-v2_3-PPG_PCG_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPG_PCG_PROBLEM_OBSERVATION <hl7-v2_3-PPG_PCG_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_3-PPG_PCG_PROBLEM_OBSERVATION:

PPG_PCG_PROBLEM_OBSERVATION HL7 v2 PPG_PCG.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_PROBLEM_OBSERVATION.PPG_PCG_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPG_PCG_PROBLEM_ROLE:

PPG_PCG_PROBLEM_ROLE HL7 v2 PPG_PCG.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPG_PCG_PROBLEM_ROLE.PPG_PCG_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPP_PCB_GOAL:

PPP_PCB_GOAL HL7 v2 PPP_PCB.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_GOAL.PPP_PCB_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPP_PCB_GOAL_ROLE <hl7-v2_3-PPP_PCB_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPP_PCB_GOAL_OBSERVATION <hl7-v2_3-PPP_PCB_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_3-PPP_PCB_GOAL_OBSERVATION:

PPP_PCB_GOAL_OBSERVATION HL7 v2 PPP_PCB.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_GOAL_OBSERVATION.PPP_PCB_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPP_PCB_GOAL_ROLE:

PPP_PCB_GOAL_ROLE HL7 v2 PPP_PCB.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_GOAL_ROLE.PPP_PCB_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPP_PCB_ORDER:

PPP_PCB_ORDER HL7 v2 PPP_PCB.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_ORDER.PPP_PCB_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPP_PCB_ORDER_DETAIL <hl7-v2_3-PPP_PCB_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PPP_PCB_ORDER_DETAIL:

PPP_PCB_ORDER_DETAIL HL7 v2 PPP_PCB.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_ORDER_DETAIL.PPP_PCB_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPP_PCB_ORDER_OBSERVATION <hl7-v2_3-PPP_PCB_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PPP_PCB_ORDER_OBSERVATION:

PPP_PCB_ORDER_OBSERVATION HL7 v2 PPP_PCB.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_ORDER_OBSERVATION.PPP_PCB_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPP_PCB_PATHWAY:

PPP_PCB_PATHWAY HL7 v2 PPP_PCB.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_PATHWAY.PPP_PCB_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PPP_PCB_PATHWAY_ROLE <hl7-v2_3-PPP_PCB_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``PROBLEM``
     - Optional[List[:ref:`PPP_PCB_PROBLEM <hl7-v2_3-PPP_PCB_PROBLEM>`]]
     - optional
     - PROBLEM

.. _hl7-v2_3-PPP_PCB_PATHWAY_ROLE:

PPP_PCB_PATHWAY_ROLE HL7 v2 PPP_PCB.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_PATHWAY_ROLE.PPP_PCB_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPP_PCB_PATIENT_VISIT:

PPP_PCB_PATIENT_VISIT HL7 v2 PPP_PCB.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_PATIENT_VISIT.PPP_PCB_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PPP_PCB_PROBLEM:

PPP_PCB_PROBLEM HL7 v2 PPP_PCB.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_PROBLEM.PPP_PCB_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPP_PCB_PROBLEM_ROLE <hl7-v2_3-PPP_PCB_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPP_PCB_PROBLEM_OBSERVATION <hl7-v2_3-PPP_PCB_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PPP_PCB_GOAL <hl7-v2_3-PPP_PCB_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PPP_PCB_ORDER <hl7-v2_3-PPP_PCB_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PPP_PCB_PROBLEM_OBSERVATION:

PPP_PCB_PROBLEM_OBSERVATION HL7 v2 PPP_PCB.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_PROBLEM_OBSERVATION.PPP_PCB_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPP_PCB_PROBLEM_ROLE:

PPP_PCB_PROBLEM_ROLE HL7 v2 PPP_PCB.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPP_PCB_PROBLEM_ROLE.PPP_PCB_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPR_PC1_GOAL:

PPR_PC1_GOAL HL7 v2 PPR_PC1.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_GOAL.PPR_PC1_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPR_PC1_GOAL_ROLE <hl7-v2_3-PPR_PC1_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPR_PC1_GOAL_OBSERVATION <hl7-v2_3-PPR_PC1_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_3-PPR_PC1_GOAL_OBSERVATION:

PPR_PC1_GOAL_OBSERVATION HL7 v2 PPR_PC1.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_GOAL_OBSERVATION.PPR_PC1_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPR_PC1_GOAL_ROLE:

PPR_PC1_GOAL_ROLE HL7 v2 PPR_PC1.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_GOAL_ROLE.PPR_PC1_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPR_PC1_ORDER:

PPR_PC1_ORDER HL7 v2 PPR_PC1.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_ORDER.PPR_PC1_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPR_PC1_ORDER_DETAIL <hl7-v2_3-PPR_PC1_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PPR_PC1_ORDER_DETAIL:

PPR_PC1_ORDER_DETAIL HL7 v2 PPR_PC1.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_ORDER_DETAIL.PPR_PC1_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPR_PC1_ORDER_OBSERVATION <hl7-v2_3-PPR_PC1_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PPR_PC1_ORDER_OBSERVATION:

PPR_PC1_ORDER_OBSERVATION HL7 v2 PPR_PC1.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_ORDER_OBSERVATION.PPR_PC1_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPR_PC1_PATHWAY:

PPR_PC1_PATHWAY HL7 v2 PPR_PC1.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_PATHWAY.PPR_PC1_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPR_PC1_PATIENT_VISIT:

PPR_PC1_PATIENT_VISIT HL7 v2 PPR_PC1.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_PATIENT_VISIT.PPR_PC1_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PPR_PC1_PROBLEM:

PPR_PC1_PROBLEM HL7 v2 PPR_PC1.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_PROBLEM.PPR_PC1_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPR_PC1_PROBLEM_ROLE <hl7-v2_3-PPR_PC1_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PATHWAY``
     - Optional[List[:ref:`PPR_PC1_PATHWAY <hl7-v2_3-PPR_PC1_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPR_PC1_PROBLEM_OBSERVATION <hl7-v2_3-PPR_PC1_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PPR_PC1_GOAL <hl7-v2_3-PPR_PC1_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PPR_PC1_ORDER <hl7-v2_3-PPR_PC1_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PPR_PC1_PROBLEM_OBSERVATION:

PPR_PC1_PROBLEM_OBSERVATION HL7 v2 PPR_PC1.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_PROBLEM_OBSERVATION.PPR_PC1_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPR_PC1_PROBLEM_ROLE:

PPR_PC1_PROBLEM_ROLE HL7 v2 PPR_PC1.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPR_PC1_PROBLEM_ROLE.PPR_PC1_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPT_PCL_GOAL:

PPT_PCL_GOAL HL7 v2 PPT_PCL.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_GOAL.PPT_PCL_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPT_PCL_GOAL_ROLE <hl7-v2_3-PPT_PCL_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPT_PCL_GOAL_OBSERVATION <hl7-v2_3-PPT_PCL_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PPT_PCL_PROBLEM <hl7-v2_3-PPT_PCL_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PPT_PCL_ORDER <hl7-v2_3-PPT_PCL_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PPT_PCL_GOAL_OBSERVATION:

PPT_PCL_GOAL_OBSERVATION HL7 v2 PPT_PCL.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_GOAL_OBSERVATION.PPT_PCL_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPT_PCL_GOAL_ROLE:

PPT_PCL_GOAL_ROLE HL7 v2 PPT_PCL.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_GOAL_ROLE.PPT_PCL_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPT_PCL_ORDER:

PPT_PCL_ORDER HL7 v2 PPT_PCL.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_ORDER.PPT_PCL_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPT_PCL_ORDER_DETAIL <hl7-v2_3-PPT_PCL_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PPT_PCL_ORDER_DETAIL:

PPT_PCL_ORDER_DETAIL HL7 v2 PPT_PCL.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_ORDER_DETAIL.PPT_PCL_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPT_PCL_ORDER_OBSERVATION <hl7-v2_3-PPT_PCL_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PPT_PCL_ORDER_OBSERVATION:

PPT_PCL_ORDER_OBSERVATION HL7 v2 PPT_PCL.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_ORDER_OBSERVATION.PPT_PCL_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPT_PCL_PATHWAY:

PPT_PCL_PATHWAY HL7 v2 PPT_PCL.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_PATHWAY.PPT_PCL_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PPT_PCL_PATHWAY_ROLE <hl7-v2_3-PPT_PCL_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``GOAL``
     - Optional[List[:ref:`PPT_PCL_GOAL <hl7-v2_3-PPT_PCL_GOAL>`]]
     - optional
     - GOAL

.. _hl7-v2_3-PPT_PCL_PATHWAY_ROLE:

PPT_PCL_PATHWAY_ROLE HL7 v2 PPT_PCL.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_PATHWAY_ROLE.PPT_PCL_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPT_PCL_PATIENT:

PPT_PCL_PATIENT HL7 v2 PPT_PCL.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_PATIENT.PPT_PCL_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPT_PCL_PATIENT_VISIT <hl7-v2_3-PPT_PCL_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPT_PCL_PATHWAY <hl7-v2_3-PPT_PCL_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PPT_PCL_PATIENT_VISIT:

PPT_PCL_PATIENT_VISIT HL7 v2 PPT_PCL.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_PATIENT_VISIT.PPT_PCL_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PPT_PCL_PROBLEM:

PPT_PCL_PROBLEM HL7 v2 PPT_PCL.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_PROBLEM.PPT_PCL_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPT_PCL_PROBLEM_ROLE <hl7-v2_3-PPT_PCL_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPT_PCL_PROBLEM_OBSERVATION <hl7-v2_3-PPT_PCL_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_3-PPT_PCL_PROBLEM_OBSERVATION:

PPT_PCL_PROBLEM_OBSERVATION HL7 v2 PPT_PCL.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_PROBLEM_OBSERVATION.PPT_PCL_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPT_PCL_PROBLEM_ROLE:

PPT_PCL_PROBLEM_ROLE HL7 v2 PPT_PCL.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPT_PCL_PROBLEM_ROLE.PPT_PCL_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPV_PCA_GOAL:

PPV_PCA_GOAL HL7 v2 PPV_PCA.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_GOAL.PPV_PCA_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPV_PCA_GOAL_ROLE <hl7-v2_3-PPV_PCA_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_PATHWAY``
     - Optional[List[:ref:`PPV_PCA_GOAL_PATHWAY <hl7-v2_3-PPV_PCA_GOAL_PATHWAY>`]]
     - optional
     - GOAL_PATHWAY
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPV_PCA_GOAL_OBSERVATION <hl7-v2_3-PPV_PCA_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PPV_PCA_PROBLEM <hl7-v2_3-PPV_PCA_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PPV_PCA_ORDER <hl7-v2_3-PPV_PCA_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PPV_PCA_GOAL_OBSERVATION:

PPV_PCA_GOAL_OBSERVATION HL7 v2 PPV_PCA.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_GOAL_OBSERVATION.PPV_PCA_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPV_PCA_GOAL_PATHWAY:

PPV_PCA_GOAL_PATHWAY HL7 v2 PPV_PCA.GOAL_PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_GOAL_PATHWAY.PPV_PCA_GOAL_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPV_PCA_GOAL_ROLE:

PPV_PCA_GOAL_ROLE HL7 v2 PPV_PCA.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_GOAL_ROLE.PPV_PCA_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPV_PCA_ORDER:

PPV_PCA_ORDER HL7 v2 PPV_PCA.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_ORDER.PPV_PCA_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPV_PCA_ORDER_DETAIL <hl7-v2_3-PPV_PCA_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PPV_PCA_ORDER_DETAIL:

PPV_PCA_ORDER_DETAIL HL7 v2 PPV_PCA.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_ORDER_DETAIL.PPV_PCA_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPV_PCA_ORDER_OBSERVATION <hl7-v2_3-PPV_PCA_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PPV_PCA_ORDER_OBSERVATION:

PPV_PCA_ORDER_OBSERVATION HL7 v2 PPV_PCA.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_ORDER_OBSERVATION.PPV_PCA_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PPV_PCA_PATIENT:

PPV_PCA_PATIENT HL7 v2 PPV_PCA.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_PATIENT.PPV_PCA_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPV_PCA_PATIENT_VISIT <hl7-v2_3-PPV_PCA_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PPV_PCA_GOAL <hl7-v2_3-PPV_PCA_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_3-PPV_PCA_PATIENT_VISIT:

PPV_PCA_PATIENT_VISIT HL7 v2 PPV_PCA.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_PATIENT_VISIT.PPV_PCA_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PPV_PCA_PROBLEM:

PPV_PCA_PROBLEM HL7 v2 PPV_PCA.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_PROBLEM.PPV_PCA_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPV_PCA_PROBLEM_ROLE <hl7-v2_3-PPV_PCA_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPV_PCA_PROBLEM_OBSERVATION <hl7-v2_3-PPV_PCA_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_3-PPV_PCA_PROBLEM_OBSERVATION:

PPV_PCA_PROBLEM_OBSERVATION HL7 v2 PPV_PCA.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_PROBLEM_OBSERVATION.PPV_PCA_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PPV_PCA_PROBLEM_ROLE:

PPV_PCA_PROBLEM_ROLE HL7 v2 PPV_PCA.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PPV_PCA_PROBLEM_ROLE.PPV_PCA_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PRR_PC5_GOAL:

PRR_PC5_GOAL HL7 v2 PRR_PC5.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_GOAL.PRR_PC5_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PRR_PC5_GOAL_ROLE <hl7-v2_3-PRR_PC5_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PRR_PC5_GOAL_OBSERVATION <hl7-v2_3-PRR_PC5_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_3-PRR_PC5_GOAL_OBSERVATION:

PRR_PC5_GOAL_OBSERVATION HL7 v2 PRR_PC5.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_GOAL_OBSERVATION.PRR_PC5_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PRR_PC5_GOAL_ROLE:

PRR_PC5_GOAL_ROLE HL7 v2 PRR_PC5.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_GOAL_ROLE.PRR_PC5_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PRR_PC5_ORDER:

PRR_PC5_ORDER HL7 v2 PRR_PC5.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_ORDER.PRR_PC5_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PRR_PC5_ORDER_DETAIL <hl7-v2_3-PRR_PC5_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PRR_PC5_ORDER_DETAIL:

PRR_PC5_ORDER_DETAIL HL7 v2 PRR_PC5.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_ORDER_DETAIL.PRR_PC5_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PRR_PC5_ORDER_OBSERVATION <hl7-v2_3-PRR_PC5_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PRR_PC5_ORDER_OBSERVATION:

PRR_PC5_ORDER_OBSERVATION HL7 v2 PRR_PC5.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_ORDER_OBSERVATION.PRR_PC5_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PRR_PC5_PATIENT:

PRR_PC5_PATIENT HL7 v2 PRR_PC5.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_PATIENT.PRR_PC5_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PRR_PC5_PATIENT_VISIT <hl7-v2_3-PRR_PC5_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PRR_PC5_PROBLEM <hl7-v2_3-PRR_PC5_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_3-PRR_PC5_PATIENT_VISIT:

PRR_PC5_PATIENT_VISIT HL7 v2 PRR_PC5.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_PATIENT_VISIT.PRR_PC5_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PRR_PC5_PROBLEM:

PRR_PC5_PROBLEM HL7 v2 PRR_PC5.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_PROBLEM.PRR_PC5_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PRR_PC5_PROBLEM_ROLE <hl7-v2_3-PRR_PC5_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_PATHWAY``
     - Optional[List[:ref:`PRR_PC5_PROBLEM_PATHWAY <hl7-v2_3-PRR_PC5_PROBLEM_PATHWAY>`]]
     - optional
     - PROBLEM_PATHWAY
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PRR_PC5_PROBLEM_OBSERVATION <hl7-v2_3-PRR_PC5_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PRR_PC5_GOAL <hl7-v2_3-PRR_PC5_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PRR_PC5_ORDER <hl7-v2_3-PRR_PC5_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PRR_PC5_PROBLEM_OBSERVATION:

PRR_PC5_PROBLEM_OBSERVATION HL7 v2 PRR_PC5.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_PROBLEM_OBSERVATION.PRR_PC5_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PRR_PC5_PROBLEM_PATHWAY:

PRR_PC5_PROBLEM_PATHWAY HL7 v2 PRR_PC5.PROBLEM_PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_PROBLEM_PATHWAY.PRR_PC5_PROBLEM_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PRR_PC5_PROBLEM_ROLE:

PRR_PC5_PROBLEM_ROLE HL7 v2 PRR_PC5.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PRR_PC5_PROBLEM_ROLE.PRR_PC5_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PTR_PCF_GOAL:

PTR_PCF_GOAL HL7 v2 PTR_PCF.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_GOAL.PTR_PCF_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_3-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PTR_PCF_GOAL_ROLE <hl7-v2_3-PTR_PCF_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PTR_PCF_GOAL_OBSERVATION <hl7-v2_3-PTR_PCF_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_3-PTR_PCF_GOAL_OBSERVATION:

PTR_PCF_GOAL_OBSERVATION HL7 v2 PTR_PCF.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_GOAL_OBSERVATION.PTR_PCF_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PTR_PCF_GOAL_ROLE:

PTR_PCF_GOAL_ROLE HL7 v2 PTR_PCF.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_GOAL_ROLE.PTR_PCF_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PTR_PCF_ORDER:

PTR_PCF_ORDER HL7 v2 PTR_PCF.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_ORDER.PTR_PCF_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PTR_PCF_ORDER_DETAIL <hl7-v2_3-PTR_PCF_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-PTR_PCF_ORDER_DETAIL:

PTR_PCF_ORDER_DETAIL HL7 v2 PTR_PCF.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_ORDER_DETAIL.PTR_PCF_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PTR_PCF_ORDER_OBSERVATION <hl7-v2_3-PTR_PCF_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_3-PTR_PCF_ORDER_OBSERVATION:

PTR_PCF_ORDER_OBSERVATION HL7 v2 PTR_PCF.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_ORDER_OBSERVATION.PTR_PCF_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PTR_PCF_PATHWAY:

PTR_PCF_PATHWAY HL7 v2 PTR_PCF.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_PATHWAY.PTR_PCF_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_3-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PTR_PCF_PATHWAY_ROLE <hl7-v2_3-PTR_PCF_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``PROBLEM``
     - Optional[List[:ref:`PTR_PCF_PROBLEM <hl7-v2_3-PTR_PCF_PROBLEM>`]]
     - optional
     - PROBLEM

.. _hl7-v2_3-PTR_PCF_PATHWAY_ROLE:

PTR_PCF_PATHWAY_ROLE HL7 v2 PTR_PCF.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_PATHWAY_ROLE.PTR_PCF_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-PTR_PCF_PATIENT:

PTR_PCF_PATIENT HL7 v2 PTR_PCF.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_PATIENT.PTR_PCF_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PTR_PCF_PATIENT_VISIT <hl7-v2_3-PTR_PCF_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PTR_PCF_PATHWAY <hl7-v2_3-PTR_PCF_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_3-PTR_PCF_PATIENT_VISIT:

PTR_PCF_PATIENT_VISIT HL7 v2 PTR_PCF.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_PATIENT_VISIT.PTR_PCF_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-PTR_PCF_PROBLEM:

PTR_PCF_PROBLEM HL7 v2 PTR_PCF.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_PROBLEM.PTR_PCF_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_3-PRB>`
     - required
     - Problem Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PTR_PCF_PROBLEM_ROLE <hl7-v2_3-PTR_PCF_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PTR_PCF_PROBLEM_OBSERVATION <hl7-v2_3-PTR_PCF_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PTR_PCF_GOAL <hl7-v2_3-PTR_PCF_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PTR_PCF_ORDER <hl7-v2_3-PTR_PCF_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_3-PTR_PCF_PROBLEM_OBSERVATION:

PTR_PCF_PROBLEM_OBSERVATION HL7 v2 PTR_PCF.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_PROBLEM_OBSERVATION.PTR_PCF_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-PTR_PCF_PROBLEM_ROLE:

PTR_PCF_PROBLEM_ROLE HL7 v2 PTR_PCF.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.PTR_PCF_PROBLEM_ROLE.PTR_PCF_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_3-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_3-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_3-RAR_RAR_DEFINITION:

RAR_RAR_DEFINITION HL7 v2 RAR_RAR.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAR_RAR_DEFINITION.RAR_RAR_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PATIENT``
     - Optional[:ref:`RAR_RAR_PATIENT <hl7-v2_3-RAR_RAR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RAR_RAR_ORDER <hl7-v2_3-RAR_RAR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RAR_RAR_ENCODING:

RAR_RAR_ENCODING HL7 v2 RAR_RAR.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAR_RAR_ENCODING.RAR_RAR_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RAR_RAR_ORDER:

RAR_RAR_ORDER HL7 v2 RAR_RAR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAR_RAR_ORDER.RAR_RAR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ENCODING``
     - Optional[:ref:`RAR_RAR_ENCODING <hl7-v2_3-RAR_RAR_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXA``
     - List[:ref:`RXA <hl7-v2_3-RXA>`]
     - required
     - Pharmacy administration segment

.. _hl7-v2_3-RAR_RAR_PATIENT:

RAR_RAR_PATIENT HL7 v2 RAR_RAR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAR_RAR_PATIENT.RAR_RAR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RAS_O01_COMPONENTS:

RAS_O01_COMPONENTS HL7 v2 RAS_O01.COMPONENTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_COMPONENTS.RAS_O01_COMPONENTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_3-RXC>`]
     - required
     - Pharmacy component order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RAS_O01_ENCODING:

RAS_O01_ENCODING HL7 v2 RAS_O01.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_ENCODING.RAS_O01_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RAS_O01_OBSERVATION:

RAS_O01_OBSERVATION HL7 v2 RAS_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_OBSERVATION.RAS_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RAS_O01_ORDER:

RAS_O01_ORDER HL7 v2 RAS_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_ORDER.RAS_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RAS_O01_ORDER_DETAIL <hl7-v2_3-RAS_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODING``
     - Optional[:ref:`RAS_O01_ENCODING <hl7-v2_3-RAS_O01_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXA``
     - List[:ref:`RXA <hl7-v2_3-RXA>`]
     - required
     - Pharmacy administration segment
   * - ``RXR``
     - :ref:`RXR <hl7-v2_3-RXR>`
     - required
     - Pharmacy route segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`RAS_O01_OBSERVATION <hl7-v2_3-RAS_O01_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_3-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_3-RAS_O01_ORDER_DETAIL:

RAS_O01_ORDER_DETAIL HL7 v2 RAS_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_ORDER_DETAIL.RAS_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_3-RXO>`
     - required
     - Pharmacy prescription order segment
   * - ``ORDER_DETAIL_SUPPLEMENT``
     - Optional[:ref:`RAS_O01_ORDER_DETAIL_SUPPLEMENT <hl7-v2_3-RAS_O01_ORDER_DETAIL_SUPPLEMENT>`]
     - optional
     - ORDER_DETAIL_SUPPLEMENT

.. _hl7-v2_3-RAS_O01_ORDER_DETAIL_SUPPLEMENT:

RAS_O01_ORDER_DETAIL_SUPPLEMENT HL7 v2 RAS_O01.ORDER_DETAIL_SUPPLEMENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_ORDER_DETAIL_SUPPLEMENT.RAS_O01_ORDER_DETAIL_SUPPLEMENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NTE``
     - List[:ref:`NTE <hl7-v2_3-NTE>`]
     - required
     - Notes and comments segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``COMPONENTS``
     - Optional[:ref:`RAS_O01_COMPONENTS <hl7-v2_3-RAS_O01_COMPONENTS>`]
     - optional
     - COMPONENTS

.. _hl7-v2_3-RAS_O01_PATIENT:

RAS_O01_PATIENT HL7 v2 RAS_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_PATIENT.RAS_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RAS_O01_PATIENT_VISIT <hl7-v2_3-RAS_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT

.. _hl7-v2_3-RAS_O01_PATIENT_VISIT:

RAS_O01_PATIENT_VISIT HL7 v2 RAS_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RAS_O01_PATIENT_VISIT.RAS_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-RCI_I05_OBSERVATION:

RCI_I05_OBSERVATION HL7 v2 RCI_I05.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RCI_I05_OBSERVATION.RCI_I05_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESULTS``
     - Optional[List[:ref:`RCI_I05_RESULTS <hl7-v2_3-RCI_I05_RESULTS>`]]
     - optional
     - RESULTS

.. _hl7-v2_3-RCI_I05_PROVIDER:

RCI_I05_PROVIDER HL7 v2 RCI_I05.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RCI_I05_PROVIDER.RCI_I05_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RCI_I05_RESULTS:

RCI_I05_RESULTS HL7 v2 RCI_I05.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RCI_I05_RESULTS.RCI_I05_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RCL_I06_PROVIDER:

RCL_I06_PROVIDER HL7 v2 RCL_I06.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RCL_I06_PROVIDER.RCL_I06_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RDE_O01_COMPONENT:

RDE_O01_COMPONENT HL7 v2 RDE_O01.COMPONENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDE_O01_COMPONENT.RDE_O01_COMPONENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_3-RXC>`]
     - required
     - Pharmacy component order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RDE_O01_INSURANCE:

RDE_O01_INSURANCE HL7 v2 RDE_O01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDE_O01_INSURANCE.RDE_O01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-RDE_O01_OBSERVATION:

RDE_O01_OBSERVATION HL7 v2 RDE_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDE_O01_OBSERVATION.RDE_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_3-OBX>`]
     - optional
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RDE_O01_ORDER:

RDE_O01_ORDER HL7 v2 RDE_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDE_O01_ORDER.RDE_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RDE_O01_ORDER_DETAIL <hl7-v2_3-RDE_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment
   * - ``OBSERVATION``
     - List[:ref:`RDE_O01_OBSERVATION <hl7-v2_3-RDE_O01_OBSERVATION>`]
     - required
     - OBSERVATION
   * - ``CTI``
     - Optional[:ref:`CTI <hl7-v2_3-CTI>`]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_3-RDE_O01_ORDER_DETAIL:

RDE_O01_ORDER_DETAIL HL7 v2 RDE_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDE_O01_ORDER_DETAIL.RDE_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_3-RXO>`
     - required
     - Pharmacy prescription order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``COMPONENT``
     - Optional[:ref:`RDE_O01_COMPONENT <hl7-v2_3-RDE_O01_COMPONENT>`]
     - optional
     - COMPONENT

.. _hl7-v2_3-RDE_O01_PATIENT:

RDE_O01_PATIENT HL7 v2 RDE_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDE_O01_PATIENT.RDE_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RDE_O01_PATIENT_VISIT <hl7-v2_3-RDE_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`RDE_O01_INSURANCE <hl7-v2_3-RDE_O01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_3-RDE_O01_PATIENT_VISIT:

RDE_O01_PATIENT_VISIT HL7 v2 RDE_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDE_O01_PATIENT_VISIT.RDE_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-RDO_O01_COMPONENT:

RDO_O01_COMPONENT HL7 v2 RDO_O01.COMPONENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDO_O01_COMPONENT.RDO_O01_COMPONENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_3-RXC>`]
     - required
     - Pharmacy component order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RDO_O01_INSURANCE:

RDO_O01_INSURANCE HL7 v2 RDO_O01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDO_O01_INSURANCE.RDO_O01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-RDO_O01_OBSERVATION:

RDO_O01_OBSERVATION HL7 v2 RDO_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDO_O01_OBSERVATION.RDO_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RDO_O01_ORDER:

RDO_O01_ORDER HL7 v2 RDO_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDO_O01_ORDER.RDO_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RDO_O01_ORDER_DETAIL <hl7-v2_3-RDO_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_3-BLG>`]
     - optional
     - Billing Segment

.. _hl7-v2_3-RDO_O01_ORDER_DETAIL:

RDO_O01_ORDER_DETAIL HL7 v2 RDO_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDO_O01_ORDER_DETAIL.RDO_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_3-RXO>`
     - required
     - Pharmacy prescription order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``COMPONENT``
     - Optional[:ref:`RDO_O01_COMPONENT <hl7-v2_3-RDO_O01_COMPONENT>`]
     - optional
     - COMPONENT
   * - ``OBSERVATION``
     - Optional[List[:ref:`RDO_O01_OBSERVATION <hl7-v2_3-RDO_O01_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-RDO_O01_PATIENT:

RDO_O01_PATIENT HL7 v2 RDO_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDO_O01_PATIENT.RDO_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RDO_O01_PATIENT_VISIT <hl7-v2_3-RDO_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`RDO_O01_INSURANCE <hl7-v2_3-RDO_O01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_3-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_3-RDO_O01_PATIENT_VISIT:

RDO_O01_PATIENT_VISIT HL7 v2 RDO_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDO_O01_PATIENT_VISIT.RDO_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-RDR_RDR_DEFINITION:

RDR_RDR_DEFINITION HL7 v2 RDR_RDR.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDR_RDR_DEFINITION.RDR_RDR_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PATIENT``
     - Optional[:ref:`RDR_RDR_PATIENT <hl7-v2_3-RDR_RDR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDR_RDR_ORDER <hl7-v2_3-RDR_RDR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RDR_RDR_DISPENSE:

RDR_RDR_DISPENSE HL7 v2 RDR_RDR.DISPENSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDR_RDR_DISPENSE.RDR_RDR_DISPENSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXD``
     - :ref:`RXD <hl7-v2_3-RXD>`
     - required
     - Pharmacy dispense segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RDR_RDR_ENCODING:

RDR_RDR_ENCODING HL7 v2 RDR_RDR.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDR_RDR_ENCODING.RDR_RDR_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - :ref:`RXR <hl7-v2_3-RXR>`
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RDR_RDR_ORDER:

RDR_RDR_ORDER HL7 v2 RDR_RDR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDR_RDR_ORDER.RDR_RDR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ENCODING``
     - Optional[:ref:`RDR_RDR_ENCODING <hl7-v2_3-RDR_RDR_ENCODING>`]
     - optional
     - ENCODING
   * - ``DISPENSE``
     - List[:ref:`RDR_RDR_DISPENSE <hl7-v2_3-RDR_RDR_DISPENSE>`]
     - required
     - DISPENSE

.. _hl7-v2_3-RDR_RDR_PATIENT:

RDR_RDR_PATIENT HL7 v2 RDR_RDR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDR_RDR_PATIENT.RDR_RDR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RDS_O01_COMPONENT:

RDS_O01_COMPONENT HL7 v2 RDS_O01.COMPONENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_COMPONENT.RDS_O01_COMPONENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_3-RXC>`]
     - required
     - Pharmacy component order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RDS_O01_ENCODING:

RDS_O01_ENCODING HL7 v2 RDS_O01.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_ENCODING.RDS_O01_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RDS_O01_OBSERVATION:

RDS_O01_OBSERVATION HL7 v2 RDS_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_OBSERVATION.RDS_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RDS_O01_ORDER:

RDS_O01_ORDER HL7 v2 RDS_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_ORDER.RDS_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RDS_O01_ORDER_DETAIL <hl7-v2_3-RDS_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODING``
     - Optional[:ref:`RDS_O01_ENCODING <hl7-v2_3-RDS_O01_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXD``
     - :ref:`RXD <hl7-v2_3-RXD>`
     - required
     - Pharmacy dispense segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment
   * - ``OBSERVATION``
     - List[:ref:`RDS_O01_OBSERVATION <hl7-v2_3-RDS_O01_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_3-RDS_O01_ORDER_DETAIL:

RDS_O01_ORDER_DETAIL HL7 v2 RDS_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_ORDER_DETAIL.RDS_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_3-RXO>`
     - required
     - Pharmacy prescription order segment
   * - ``ORDER_DETAIL_SUPPLEMENT``
     - Optional[:ref:`RDS_O01_ORDER_DETAIL_SUPPLEMENT <hl7-v2_3-RDS_O01_ORDER_DETAIL_SUPPLEMENT>`]
     - optional
     - ORDER_DETAIL_SUPPLEMENT

.. _hl7-v2_3-RDS_O01_ORDER_DETAIL_SUPPLEMENT:

RDS_O01_ORDER_DETAIL_SUPPLEMENT HL7 v2 RDS_O01.ORDER_DETAIL_SUPPLEMENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_ORDER_DETAIL_SUPPLEMENT.RDS_O01_ORDER_DETAIL_SUPPLEMENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NTE``
     - List[:ref:`NTE <hl7-v2_3-NTE>`]
     - required
     - Notes and comments segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``COMPONENT``
     - Optional[:ref:`RDS_O01_COMPONENT <hl7-v2_3-RDS_O01_COMPONENT>`]
     - optional
     - COMPONENT

.. _hl7-v2_3-RDS_O01_PATIENT:

RDS_O01_PATIENT HL7 v2 RDS_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_PATIENT.RDS_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
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
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RDS_O01_PATIENT_VISIT <hl7-v2_3-RDS_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT

.. _hl7-v2_3-RDS_O01_PATIENT_VISIT:

RDS_O01_PATIENT_VISIT HL7 v2 RDS_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RDS_O01_PATIENT_VISIT.RDS_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-REF_I12_AUTCTD_SUPPGRP2:

REF_I12_AUTCTD_SUPPGRP2 HL7 v2 REF_I12.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_AUTCTD_SUPPGRP2.REF_I12_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-REF_I12_AUTHORIZATION:

REF_I12_AUTHORIZATION HL7 v2 REF_I12.AUTHORIZATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_AUTHORIZATION.REF_I12_AUTHORIZATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-REF_I12_INSURANCE:

REF_I12_INSURANCE HL7 v2 REF_I12.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_INSURANCE.REF_I12_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-REF_I12_OBSERVATION:

REF_I12_OBSERVATION HL7 v2 REF_I12.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_OBSERVATION.REF_I12_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-REF_I12_PROCEDURE:

REF_I12_PROCEDURE HL7 v2 REF_I12.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_PROCEDURE.REF_I12_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`REF_I12_AUTCTD_SUPPGRP2 <hl7-v2_3-REF_I12_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_3-REF_I12_PROVIDER:

REF_I12_PROVIDER HL7 v2 REF_I12.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_PROVIDER.REF_I12_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-REF_I12_RESULTS:

REF_I12_RESULTS HL7 v2 REF_I12.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_RESULTS.REF_I12_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_3-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-REF_I12_VISIT:

REF_I12_VISIT HL7 v2 REF_I12.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.REF_I12_VISIT.REF_I12_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-RER_RER_DEFINITION:

RER_RER_DEFINITION HL7 v2 RER_RER.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RER_RER_DEFINITION.RER_RER_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PATIENT``
     - Optional[:ref:`RER_RER_PATIENT <hl7-v2_3-RER_RER_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RER_RER_ORDER <hl7-v2_3-RER_RER_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RER_RER_ORDER:

RER_RER_ORDER HL7 v2 RER_RER.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RER_RER_ORDER.RER_RER_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RER_RER_PATIENT:

RER_RER_PATIENT HL7 v2 RER_RER.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RER_RER_PATIENT.RER_RER_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RGR_RGR_DEFINITION:

RGR_RGR_DEFINITION HL7 v2 RGR_RGR.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGR_RGR_DEFINITION.RGR_RGR_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PATIENT``
     - Optional[:ref:`RGR_RGR_PATIENT <hl7-v2_3-RGR_RGR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RGR_RGR_ORDER <hl7-v2_3-RGR_RGR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RGR_RGR_ENCODING:

RGR_RGR_ENCODING HL7 v2 RGR_RGR.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGR_RGR_ENCODING.RGR_RGR_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RGR_RGR_ORDER:

RGR_RGR_ORDER HL7 v2 RGR_RGR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGR_RGR_ORDER.RGR_RGR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ENCODING``
     - Optional[:ref:`RGR_RGR_ENCODING <hl7-v2_3-RGR_RGR_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXG``
     - List[:ref:`RXG <hl7-v2_3-RXG>`]
     - required
     - Pharmacy give segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RGR_RGR_PATIENT:

RGR_RGR_PATIENT HL7 v2 RGR_RGR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGR_RGR_PATIENT.RGR_RGR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RGV_O01_COMPONENTS:

RGV_O01_COMPONENTS HL7 v2 RGV_O01.COMPONENTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_COMPONENTS.RGV_O01_COMPONENTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_3-RXC>`]
     - required
     - Pharmacy component order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RGV_O01_ENCODING:

RGV_O01_ENCODING HL7 v2 RGV_O01.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_ENCODING.RGV_O01_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_3-RXE>`
     - required
     - Pharmacy encoded order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RGV_O01_GIVE:

RGV_O01_GIVE HL7 v2 RGV_O01.GIVE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_GIVE.RGV_O01_GIVE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXG``
     - :ref:`RXG <hl7-v2_3-RXG>`
     - required
     - Pharmacy give segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`RGV_O01_OBSERVATION <hl7-v2_3-RGV_O01_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-RGV_O01_OBSERVATION:

RGV_O01_OBSERVATION HL7 v2 RGV_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_OBSERVATION.RGV_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RGV_O01_ORDER:

RGV_O01_ORDER HL7 v2 RGV_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_ORDER.RGV_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RGV_O01_ORDER_DETAIL <hl7-v2_3-RGV_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODING``
     - Optional[:ref:`RGV_O01_ENCODING <hl7-v2_3-RGV_O01_ENCODING>`]
     - optional
     - ENCODING
   * - ``GIVE``
     - List[:ref:`RGV_O01_GIVE <hl7-v2_3-RGV_O01_GIVE>`]
     - required
     - GIVE

.. _hl7-v2_3-RGV_O01_ORDER_DETAIL:

RGV_O01_ORDER_DETAIL HL7 v2 RGV_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_ORDER_DETAIL.RGV_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_3-RXO>`
     - required
     - Pharmacy prescription order segment
   * - ``ORDER_DETAIL_SUPPLEMENT``
     - Optional[:ref:`RGV_O01_ORDER_DETAIL_SUPPLEMENT <hl7-v2_3-RGV_O01_ORDER_DETAIL_SUPPLEMENT>`]
     - optional
     - ORDER_DETAIL_SUPPLEMENT

.. _hl7-v2_3-RGV_O01_ORDER_DETAIL_SUPPLEMENT:

RGV_O01_ORDER_DETAIL_SUPPLEMENT HL7 v2 RGV_O01.ORDER_DETAIL_SUPPLEMENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_ORDER_DETAIL_SUPPLEMENT.RGV_O01_ORDER_DETAIL_SUPPLEMENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NTE``
     - List[:ref:`NTE <hl7-v2_3-NTE>`]
     - required
     - Notes and comments segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``COMPONENTS``
     - Optional[:ref:`RGV_O01_COMPONENTS <hl7-v2_3-RGV_O01_COMPONENTS>`]
     - optional
     - COMPONENTS

.. _hl7-v2_3-RGV_O01_PATIENT:

RGV_O01_PATIENT HL7 v2 RGV_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_PATIENT.RGV_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_3-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RGV_O01_PATIENT_VISIT <hl7-v2_3-RGV_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT

.. _hl7-v2_3-RGV_O01_PATIENT_VISIT:

RGV_O01_PATIENT_VISIT HL7 v2 RGV_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RGV_O01_PATIENT_VISIT.RGV_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-ROR_ROR_DEFINITION:

ROR_ROR_DEFINITION HL7 v2 ROR_ROR.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ROR_ROR_DEFINITION.ROR_ROR_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_3-QRD>`
     - required
     - Query definition segment
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_3-QRF>`]
     - optional
     - Query filter segment
   * - ``PATIENT``
     - Optional[:ref:`ROR_ROR_PATIENT <hl7-v2_3-ROR_ROR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ROR_ROR_ORDER <hl7-v2_3-ROR_ROR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-ROR_ROR_ORDER:

ROR_ROR_ORDER HL7 v2 ROR_ROR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ROR_ROR_ORDER.ROR_ROR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``RXO``
     - :ref:`RXO <hl7-v2_3-RXO>`
     - required
     - Pharmacy prescription order segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-ROR_ROR_PATIENT:

ROR_ROR_PATIENT HL7 v2 ROR_ROR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.ROR_ROR_PATIENT.ROR_ROR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RPA_I08_AUTCTD_SUPPGRP2:

RPA_I08_AUTCTD_SUPPGRP2 HL7 v2 RPA_I08.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_AUTCTD_SUPPGRP2.RPA_I08_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-RPA_I08_AUTHORIZATION:

RPA_I08_AUTHORIZATION HL7 v2 RPA_I08.AUTHORIZATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_AUTHORIZATION.RPA_I08_AUTHORIZATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-RPA_I08_INSURANCE:

RPA_I08_INSURANCE HL7 v2 RPA_I08.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_INSURANCE.RPA_I08_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-RPA_I08_OBSERVATION:

RPA_I08_OBSERVATION HL7 v2 RPA_I08.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_OBSERVATION.RPA_I08_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESULTS``
     - Optional[List[:ref:`RPA_I08_RESULTS <hl7-v2_3-RPA_I08_RESULTS>`]]
     - optional
     - RESULTS

.. _hl7-v2_3-RPA_I08_PROCEDURE:

RPA_I08_PROCEDURE HL7 v2 RPA_I08.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_PROCEDURE.RPA_I08_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`RPA_I08_AUTCTD_SUPPGRP2 <hl7-v2_3-RPA_I08_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_3-RPA_I08_PROVIDER:

RPA_I08_PROVIDER HL7 v2 RPA_I08.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_PROVIDER.RPA_I08_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RPA_I08_RESULTS:

RPA_I08_RESULTS HL7 v2 RPA_I08.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_RESULTS.RPA_I08_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RPA_I08_VISIT:

RPA_I08_VISIT HL7 v2 RPA_I08.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPA_I08_VISIT.RPA_I08_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RPI_I01_GUARANTOR_INSURANCE:

RPI_I01_GUARANTOR_INSURANCE HL7 v2 RPI_I01.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPI_I01_GUARANTOR_INSURANCE.RPI_I01_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`RPI_I01_INSURANCE <hl7-v2_3-RPI_I01_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_3-RPI_I01_INSURANCE:

RPI_I01_INSURANCE HL7 v2 RPI_I01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPI_I01_INSURANCE.RPI_I01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-RPI_I01_PROVIDER:

RPI_I01_PROVIDER HL7 v2 RPI_I01.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPI_I01_PROVIDER.RPI_I01_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RPL_I02_PROVIDER:

RPL_I02_PROVIDER HL7 v2 RPL_I02.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RPL_I02_PROVIDER.RPL_I02_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RQA_I08_AUTCTD_SUPPGRP2:

RQA_I08_AUTCTD_SUPPGRP2 HL7 v2 RQA_I08.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_AUTCTD_SUPPGRP2.RQA_I08_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-RQA_I08_AUTHORIZATION:

RQA_I08_AUTHORIZATION HL7 v2 RQA_I08.AUTHORIZATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_AUTHORIZATION.RQA_I08_AUTHORIZATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-RQA_I08_GUARANTOR_INSURANCE:

RQA_I08_GUARANTOR_INSURANCE HL7 v2 RQA_I08.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_GUARANTOR_INSURANCE.RQA_I08_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`RQA_I08_INSURANCE <hl7-v2_3-RQA_I08_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_3-RQA_I08_INSURANCE:

RQA_I08_INSURANCE HL7 v2 RQA_I08.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_INSURANCE.RQA_I08_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-RQA_I08_OBSERVATION:

RQA_I08_OBSERVATION HL7 v2 RQA_I08.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_OBSERVATION.RQA_I08_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RESULTS``
     - Optional[List[:ref:`RQA_I08_RESULTS <hl7-v2_3-RQA_I08_RESULTS>`]]
     - optional
     - RESULTS

.. _hl7-v2_3-RQA_I08_PROCEDURE:

RQA_I08_PROCEDURE HL7 v2 RQA_I08.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_PROCEDURE.RQA_I08_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`RQA_I08_AUTCTD_SUPPGRP2 <hl7-v2_3-RQA_I08_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_3-RQA_I08_PROVIDER:

RQA_I08_PROVIDER HL7 v2 RQA_I08.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_PROVIDER.RQA_I08_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RQA_I08_RESULTS:

RQA_I08_RESULTS HL7 v2 RQA_I08.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_RESULTS.RQA_I08_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RQA_I08_VISIT:

RQA_I08_VISIT HL7 v2 RQA_I08.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQA_I08_VISIT.RQA_I08_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-RQC_I05_PROVIDER:

RQC_I05_PROVIDER HL7 v2 RQC_I05.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQC_I05_PROVIDER.RQC_I05_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RQC_I06_PROVIDER:

RQC_I06_PROVIDER HL7 v2 RQC_I06.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQC_I06_PROVIDER.RQC_I06_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RQI_I01_GUARANTOR_INSURANCE:

RQI_I01_GUARANTOR_INSURANCE HL7 v2 RQI_I01.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQI_I01_GUARANTOR_INSURANCE.RQI_I01_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_3-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`RQI_I01_INSURANCE <hl7-v2_3-RQI_I01_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_3-RQI_I01_INSURANCE:

RQI_I01_INSURANCE HL7 v2 RQI_I01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQI_I01_INSURANCE.RQI_I01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-RQI_I01_PROVIDER:

RQI_I01_PROVIDER HL7 v2 RQI_I01.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQI_I01_PROVIDER.RQI_I01_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RQP_I04_PROVIDER:

RQP_I04_PROVIDER HL7 v2 RQP_I04.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RQP_I04_PROVIDER.RQP_I04_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RRA_O02_ADMINISTRATION:

RRA_O02_ADMINISTRATION HL7 v2 RRA_O02.ADMINISTRATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRA_O02_ADMINISTRATION.RRA_O02_ADMINISTRATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_3-RXA>`
     - required
     - Pharmacy administration segment
   * - ``RXR``
     - :ref:`RXR <hl7-v2_3-RXR>`
     - required
     - Pharmacy route segment

.. _hl7-v2_3-RRA_O02_ORDER:

RRA_O02_ORDER HL7 v2 RRA_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRA_O02_ORDER.RRA_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ADMINISTRATION``
     - Optional[List[:ref:`RRA_O02_ADMINISTRATION <hl7-v2_3-RRA_O02_ADMINISTRATION>`]]
     - optional
     - ADMINISTRATION

.. _hl7-v2_3-RRA_O02_PATIENT:

RRA_O02_PATIENT HL7 v2 RRA_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRA_O02_PATIENT.RRA_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RRA_O02_RESPONSE:

RRA_O02_RESPONSE HL7 v2 RRA_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRA_O02_RESPONSE.RRA_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RRA_O02_PATIENT <hl7-v2_3-RRA_O02_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RRA_O02_ORDER <hl7-v2_3-RRA_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RRD_O02_DISPENSE:

RRD_O02_DISPENSE HL7 v2 RRD_O02.DISPENSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRD_O02_DISPENSE.RRD_O02_DISPENSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXD``
     - :ref:`RXD <hl7-v2_3-RXD>`
     - required
     - Pharmacy dispense segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RRD_O02_ORDER:

RRD_O02_ORDER HL7 v2 RRD_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRD_O02_ORDER.RRD_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``DISPENSE``
     - Optional[:ref:`RRD_O02_DISPENSE <hl7-v2_3-RRD_O02_DISPENSE>`]
     - optional
     - DISPENSE

.. _hl7-v2_3-RRD_O02_PATIENT:

RRD_O02_PATIENT HL7 v2 RRD_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRD_O02_PATIENT.RRD_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RESPONSE``
     - Optional[:ref:`RRD_O02_RESPONSE <hl7-v2_3-RRD_O02_RESPONSE>`]
     - optional
     - RESPONSE
   * - ``ORDER``
     - List[:ref:`RRD_O02_ORDER <hl7-v2_3-RRD_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RRD_O02_RESPONSE:

RRD_O02_RESPONSE HL7 v2 RRD_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRD_O02_RESPONSE.RRD_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RRG_O02_GIVE:

RRG_O02_GIVE HL7 v2 RRG_O02.GIVE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRG_O02_GIVE.RRG_O02_GIVE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXG``
     - :ref:`RXG <hl7-v2_3-RXG>`
     - required
     - Pharmacy give segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RRG_O02_ORDER:

RRG_O02_ORDER HL7 v2 RRG_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRG_O02_ORDER.RRG_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``GIVE``
     - Optional[:ref:`RRG_O02_GIVE <hl7-v2_3-RRG_O02_GIVE>`]
     - optional
     - GIVE

.. _hl7-v2_3-RRG_O02_PATIENT:

RRG_O02_PATIENT HL7 v2 RRG_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRG_O02_PATIENT.RRG_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RRG_O02_RESPONSE:

RRG_O02_RESPONSE HL7 v2 RRG_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRG_O02_RESPONSE.RRG_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RRG_O02_PATIENT <hl7-v2_3-RRG_O02_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RRG_O02_ORDER <hl7-v2_3-RRG_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-RRI_I12_AUTCTD_SUPPGRP2:

RRI_I12_AUTCTD_SUPPGRP2 HL7 v2 RRI_I12.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRI_I12_AUTCTD_SUPPGRP2.RRI_I12_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-RRI_I12_AUTHORIZATION:

RRI_I12_AUTHORIZATION HL7 v2 RRI_I12.AUTHORIZATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRI_I12_AUTHORIZATION.RRI_I12_AUTHORIZATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_3-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_3-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_3-RRI_I12_OBSERVATION:

RRI_I12_OBSERVATION HL7 v2 RRI_I12.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRI_I12_OBSERVATION.RRI_I12_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RRI_I12_PROCEDURE:

RRI_I12_PROCEDURE HL7 v2 RRI_I12.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRI_I12_PROCEDURE.RRI_I12_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_3-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`RRI_I12_AUTCTD_SUPPGRP2 <hl7-v2_3-RRI_I12_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_3-RRI_I12_PROVIDER:

RRI_I12_PROVIDER HL7 v2 RRI_I12.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRI_I12_PROVIDER.RRI_I12_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_3-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_3-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_3-RRI_I12_RESULTS:

RRI_I12_RESULTS HL7 v2 RRI_I12.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRI_I12_RESULTS.RRI_I12_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_3-OBR>`
     - required
     - Observation request segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`RRI_I12_OBSERVATION <hl7-v2_3-RRI_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-RRI_I12_VISIT:

RRI_I12_VISIT HL7 v2 RRI_I12.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRI_I12_VISIT.RRI_I12_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-RRO_O02_ORDER:

RRO_O02_ORDER HL7 v2 RRO_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRO_O02_ORDER.RRO_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_3-ORC>`
     - required
     - Common order segment
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RRO_O02_ORDER_DETAIL <hl7-v2_3-RRO_O02_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_3-RRO_O02_ORDER_DETAIL:

RRO_O02_ORDER_DETAIL HL7 v2 RRO_O02.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRO_O02_ORDER_DETAIL.RRO_O02_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_3-RXO>`
     - required
     - Pharmacy prescription order segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_3-RXR>`]
     - required
     - Pharmacy route segment
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_3-RXC>`]]
     - optional
     - Pharmacy component order segment

.. _hl7-v2_3-RRO_O02_PATIENT:

RRO_O02_PATIENT HL7 v2 RRO_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRO_O02_PATIENT.RRO_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-RRO_O02_RESPONSE:

RRO_O02_RESPONSE HL7 v2 RRO_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.RRO_O02_RESPONSE.RRO_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RRO_O02_PATIENT <hl7-v2_3-RRO_O02_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RRO_O02_ORDER <hl7-v2_3-RRO_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_3-SIU_S12_GENERAL_RESOURCE:

SIU_S12_GENERAL_RESOURCE HL7 v2 SIU_S12.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SIU_S12_GENERAL_RESOURCE.SIU_S12_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_3-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SIU_S12_LOCATION_RESOURCE:

SIU_S12_LOCATION_RESOURCE HL7 v2 SIU_S12.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SIU_S12_LOCATION_RESOURCE.SIU_S12_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_3-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SIU_S12_PATIENT:

SIU_S12_PATIENT HL7 v2 SIU_S12.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SIU_S12_PATIENT.SIU_S12_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_3-SIU_S12_PERSONNEL_RESOURCE:

SIU_S12_PERSONNEL_RESOURCE HL7 v2 SIU_S12.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SIU_S12_PERSONNEL_RESOURCE.SIU_S12_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_3-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SIU_S12_RESOURCES:

SIU_S12_RESOURCES HL7 v2 SIU_S12.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SIU_S12_RESOURCES.SIU_S12_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_3-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SIU_S12_SERVICE <hl7-v2_3-SIU_S12_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SIU_S12_GENERAL_RESOURCE <hl7-v2_3-SIU_S12_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SIU_S12_LOCATION_RESOURCE <hl7-v2_3-SIU_S12_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SIU_S12_PERSONNEL_RESOURCE <hl7-v2_3-SIU_S12_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE

.. _hl7-v2_3-SIU_S12_SERVICE:

SIU_S12_SERVICE HL7 v2 SIU_S12.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SIU_S12_SERVICE.SIU_S12_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_3-AIS>`
     - required
     - Appointment Information - Service
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SQM_S25_GENERAL_RESOURCE:

SQM_S25_GENERAL_RESOURCE HL7 v2 SQM_S25.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQM_S25_GENERAL_RESOURCE.SQM_S25_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_3-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_3-SQM_S25_LOCATION_RESOURCE:

SQM_S25_LOCATION_RESOURCE HL7 v2 SQM_S25.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQM_S25_LOCATION_RESOURCE.SQM_S25_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_3-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_3-SQM_S25_PERSONNEL_RESOURCE:

SQM_S25_PERSONNEL_RESOURCE HL7 v2 SQM_S25.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQM_S25_PERSONNEL_RESOURCE.SQM_S25_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_3-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_3-SQM_S25_REQUEST:

SQM_S25_REQUEST HL7 v2 SQM_S25.REQUEST group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQM_S25_REQUEST.SQM_S25_REQUEST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_3-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``PID``
     - Optional[:ref:`PID <hl7-v2_3-PID>`]
     - optional
     - Patient Identification
   * - ``RESOURCES``
     - List[:ref:`SQM_S25_RESOURCES <hl7-v2_3-SQM_S25_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SQM_S25_RESOURCES:

SQM_S25_RESOURCES HL7 v2 SQM_S25.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQM_S25_RESOURCES.SQM_S25_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_3-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SQM_S25_SERVICE <hl7-v2_3-SQM_S25_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SQM_S25_GENERAL_RESOURCE <hl7-v2_3-SQM_S25_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SQM_S25_PERSONNEL_RESOURCE <hl7-v2_3-SQM_S25_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SQM_S25_LOCATION_RESOURCE <hl7-v2_3-SQM_S25_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE

.. _hl7-v2_3-SQM_S25_SERVICE:

SQM_S25_SERVICE HL7 v2 SQM_S25.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQM_S25_SERVICE.SQM_S25_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_3-AIS>`
     - required
     - Appointment Information - Service
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_3-SQR_S25_GENERAL_RESOURCE:

SQR_S25_GENERAL_RESOURCE HL7 v2 SQR_S25.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQR_S25_GENERAL_RESOURCE.SQR_S25_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_3-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SQR_S25_LOCATION_RESOURCE:

SQR_S25_LOCATION_RESOURCE HL7 v2 SQR_S25.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQR_S25_LOCATION_RESOURCE.SQR_S25_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_3-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SQR_S25_PATIENT:

SQR_S25_PATIENT HL7 v2 SQR_S25.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQR_S25_PATIENT.SQR_S25_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_3-DG1>`]
     - optional
     - Diagnosis

.. _hl7-v2_3-SQR_S25_PERSONNEL_RESOURCE:

SQR_S25_PERSONNEL_RESOURCE HL7 v2 SQR_S25.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQR_S25_PERSONNEL_RESOURCE.SQR_S25_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_3-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SQR_S25_RESOURCES:

SQR_S25_RESOURCES HL7 v2 SQR_S25.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQR_S25_RESOURCES.SQR_S25_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_3-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SQR_S25_SERVICE <hl7-v2_3-SQR_S25_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SQR_S25_GENERAL_RESOURCE <hl7-v2_3-SQR_S25_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SQR_S25_PERSONNEL_RESOURCE <hl7-v2_3-SQR_S25_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SQR_S25_LOCATION_RESOURCE <hl7-v2_3-SQR_S25_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE

.. _hl7-v2_3-SQR_S25_SCHEDULE:

SQR_S25_SCHEDULE HL7 v2 SQR_S25.SCHEDULE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQR_S25_SCHEDULE.SQR_S25_SCHEDULE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[:ref:`SQR_S25_PATIENT <hl7-v2_3-SQR_S25_PATIENT>`]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SQR_S25_RESOURCES <hl7-v2_3-SQR_S25_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SQR_S25_SERVICE:

SQR_S25_SERVICE HL7 v2 SQR_S25.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SQR_S25_SERVICE.SQR_S25_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_3-AIS>`
     - required
     - Appointment Information - Service
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRM_S01_GENERAL_RESOURCE:

SRM_S01_GENERAL_RESOURCE HL7 v2 SRM_S01.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRM_S01_GENERAL_RESOURCE.SRM_S01_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_3-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRM_S01_LOCATION_RESOURCE:

SRM_S01_LOCATION_RESOURCE HL7 v2 SRM_S01.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRM_S01_LOCATION_RESOURCE.SRM_S01_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_3-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRM_S01_PATIENT:

SRM_S01_PATIENT HL7 v2 SRM_S01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRM_S01_PATIENT.SRM_S01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_3-OBX>`]]
     - optional
     - Observation segment
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_3-SRM_S01_PERSONNEL_RESOURCE:

SRM_S01_PERSONNEL_RESOURCE HL7 v2 SRM_S01.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRM_S01_PERSONNEL_RESOURCE.SRM_S01_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_3-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRM_S01_RESOURCES:

SRM_S01_RESOURCES HL7 v2 SRM_S01.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRM_S01_RESOURCES.SRM_S01_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_3-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SRM_S01_SERVICE <hl7-v2_3-SRM_S01_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SRM_S01_GENERAL_RESOURCE <hl7-v2_3-SRM_S01_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SRM_S01_LOCATION_RESOURCE <hl7-v2_3-SRM_S01_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SRM_S01_PERSONNEL_RESOURCE <hl7-v2_3-SRM_S01_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE

.. _hl7-v2_3-SRM_S01_SERVICE:

SRM_S01_SERVICE HL7 v2 SRM_S01.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRM_S01_SERVICE.SRM_S01_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_3-AIS>`
     - required
     - Appointment Information - Service
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_3-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRR_S01_GENERAL_RESOURCE:

SRR_S01_GENERAL_RESOURCE HL7 v2 SRR_S01.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRR_S01_GENERAL_RESOURCE.SRR_S01_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_3-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRR_S01_LOCATION_RESOURCE:

SRR_S01_LOCATION_RESOURCE HL7 v2 SRR_S01.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRR_S01_LOCATION_RESOURCE.SRR_S01_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_3-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRR_S01_PATIENT:

SRR_S01_PATIENT HL7 v2 SRR_S01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRR_S01_PATIENT.SRR_S01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_3-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_3-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_3-SRR_S01_PERSONNEL_RESOURCE:

SRR_S01_PERSONNEL_RESOURCE HL7 v2 SRR_S01.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRR_S01_PERSONNEL_RESOURCE.SRR_S01_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_3-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SRR_S01_RESOURCES:

SRR_S01_RESOURCES HL7 v2 SRR_S01.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRR_S01_RESOURCES.SRR_S01_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_3-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SRR_S01_SERVICE <hl7-v2_3-SRR_S01_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SRR_S01_GENERAL_RESOURCE <hl7-v2_3-SRR_S01_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SRR_S01_LOCATION_RESOURCE <hl7-v2_3-SRR_S01_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SRR_S01_PERSONNEL_RESOURCE <hl7-v2_3-SRR_S01_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE

.. _hl7-v2_3-SRR_S01_SCHEDULE:

SRR_S01_SCHEDULE HL7 v2 SRR_S01.SCHEDULE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRR_S01_SCHEDULE.SRR_S01_SCHEDULE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SCH``
     - :ref:`SCH <hl7-v2_3-SCH>`
     - required
     - Schedule Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment
   * - ``PATIENT``
     - Optional[List[:ref:`SRR_S01_PATIENT <hl7-v2_3-SRR_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRR_S01_RESOURCES <hl7-v2_3-SRR_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_3-SRR_S01_SERVICE:

SRR_S01_SERVICE HL7 v2 SRR_S01.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SRR_S01_SERVICE.SRR_S01_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_3-AIS>`
     - required
     - Appointment Information - Service
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-SUR_P09_FACILITY:

SUR_P09_FACILITY HL7 v2 SUR_P09.FACILITY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SUR_P09_FACILITY.SUR_P09_FACILITY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``FAC``
     - :ref:`FAC <hl7-v2_3-FAC>`
     - required
     - Facility
   * - ``PRODUCT``
     - List[:ref:`SUR_P09_PRODUCT <hl7-v2_3-SUR_P09_PRODUCT>`]
     - required
     - PRODUCT
   * - ``PSH``
     - :ref:`PSH <hl7-v2_3-PSH>`
     - required
     - Product Summary Header
   * - ``FACILITY_DETAIL``
     - List[:ref:`SUR_P09_FACILITY_DETAIL <hl7-v2_3-SUR_P09_FACILITY_DETAIL>`]
     - required
     - FACILITY_DETAIL

.. _hl7-v2_3-SUR_P09_FACILITY_DETAIL:

SUR_P09_FACILITY_DETAIL HL7 v2 SUR_P09.FACILITY_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SUR_P09_FACILITY_DETAIL.SUR_P09_FACILITY_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``FAC``
     - :ref:`FAC <hl7-v2_3-FAC>`
     - required
     - Facility
   * - ``PDC``
     - :ref:`PDC <hl7-v2_3-PDC>`
     - required
     - Product Detail Country
   * - ``NTE``
     - :ref:`NTE <hl7-v2_3-NTE>`
     - required
     - Notes and comments segment

.. _hl7-v2_3-SUR_P09_PRODUCT:

SUR_P09_PRODUCT HL7 v2 SUR_P09.PRODUCT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.SUR_P09_PRODUCT.SUR_P09_PRODUCT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PSH``
     - :ref:`PSH <hl7-v2_3-PSH>`
     - required
     - Product Summary Header
   * - ``PDC``
     - :ref:`PDC <hl7-v2_3-PDC>`
     - required
     - Product Detail Country

.. _hl7-v2_3-VXR_V03_INSURANCE:

VXR_V03_INSURANCE HL7 v2 VXR_V03.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXR_V03_INSURANCE.VXR_V03_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-VXR_V03_OBSERVATION:

VXR_V03_OBSERVATION HL7 v2 VXR_V03.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXR_V03_OBSERVATION.VXR_V03_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-VXR_V03_ORDER:

VXR_V03_ORDER HL7 v2 VXR_V03.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXR_V03_ORDER.VXR_V03_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_3-ORC>`]
     - optional
     - Common order segment
   * - ``RXA``
     - :ref:`RXA <hl7-v2_3-RXA>`
     - required
     - Pharmacy administration segment
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_3-RXR>`]
     - optional
     - Pharmacy route segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`VXR_V03_OBSERVATION <hl7-v2_3-VXR_V03_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-VXR_V03_PATIENT_VISIT:

VXR_V03_PATIENT_VISIT HL7 v2 VXR_V03.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXR_V03_PATIENT_VISIT.VXR_V03_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-VXU_V04_INSURANCE:

VXU_V04_INSURANCE HL7 v2 VXU_V04.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXU_V04_INSURANCE.VXU_V04_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_3-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_3-IN2>`]
     - optional
     - Insurance additional info
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_3-IN3>`]
     - optional
     - Insurance additional info - certification

.. _hl7-v2_3-VXU_V04_OBSERVATION:

VXU_V04_OBSERVATION HL7 v2 VXU_V04.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXU_V04_OBSERVATION.VXU_V04_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_3-OBX>`
     - required
     - Observation segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_3-NTE>`]]
     - optional
     - Notes and comments segment

.. _hl7-v2_3-VXU_V04_ORDER:

VXU_V04_ORDER HL7 v2 VXU_V04.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXU_V04_ORDER.VXU_V04_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_3-ORC>`]
     - optional
     - Common order segment
   * - ``RXA``
     - :ref:`RXA <hl7-v2_3-RXA>`
     - required
     - Pharmacy administration segment
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_3-RXR>`]
     - optional
     - Pharmacy route segment
   * - ``OBSERVATION``
     - Optional[List[:ref:`VXU_V04_OBSERVATION <hl7-v2_3-VXU_V04_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_3-VXU_V04_PATIENT:

VXU_V04_PATIENT HL7 v2 VXU_V04.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXU_V04_PATIENT.VXU_V04_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_3-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_3-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_3-VXX_V02_PATIENT:

VXX_V02_PATIENT HL7 v2 VXX_V02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_3.groups.VXX_V02_PATIENT.VXX_V02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_3-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_3-NK1>`]]
     - optional
     - Next of kin
