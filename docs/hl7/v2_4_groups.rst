v2.4 Groups
===========

.. _hl7-v2_4-ADR_A19_INSURANCE:

ADR_A19_INSURANCE HL7 v2 ADR_A19.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADR_A19_INSURANCE.ADR_A19_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADR_A19_PROCEDURE:

ADR_A19_PROCEDURE HL7 v2 ADR_A19.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADR_A19_PROCEDURE.ADR_A19_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADR_A19_QUERY_RESPONSE:

ADR_A19_QUERY_RESPONSE HL7 v2 ADR_A19.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADR_A19_QUERY_RESPONSE.ADR_A19_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``EVN``
     - Optional[:ref:`EVN <hl7-v2_4-EVN>`]
     - optional
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_4-NK1>`]]
     - optional
     - Next of kin / associated parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_4-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_4-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADR_A19_PROCEDURE <hl7-v2_4-ADR_A19_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADR_A19_INSURANCE <hl7-v2_4-ADR_A19_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_4-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_4-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_4-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_4-ADT_A01_INSURANCE:

ADT_A01_INSURANCE HL7 v2 ADT_A01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A01_INSURANCE.ADT_A01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADT_A01_PROCEDURE:

ADT_A01_PROCEDURE HL7 v2 ADT_A01.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A01_PROCEDURE.ADT_A01_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADT_A03_PROCEDURE:

ADT_A03_PROCEDURE HL7 v2 ADT_A03.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A03_PROCEDURE.ADT_A03_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADT_A05_INSURANCE:

ADT_A05_INSURANCE HL7 v2 ADT_A05.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A05_INSURANCE.ADT_A05_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADT_A05_PROCEDURE:

ADT_A05_PROCEDURE HL7 v2 ADT_A05.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A05_PROCEDURE.ADT_A05_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADT_A06_INSURANCE:

ADT_A06_INSURANCE HL7 v2 ADT_A06.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A06_INSURANCE.ADT_A06_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADT_A06_PROCEDURE:

ADT_A06_PROCEDURE HL7 v2 ADT_A06.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A06_PROCEDURE.ADT_A06_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-ADT_A39_PATIENT:

ADT_A39_PATIENT HL7 v2 ADT_A39.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A39_PATIENT.ADT_A39_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - required
     - Merge patient information
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit

.. _hl7-v2_4-ADT_A43_PATIENT:

ADT_A43_PATIENT HL7 v2 ADT_A43.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A43_PATIENT.ADT_A43_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - required
     - Merge patient information

.. _hl7-v2_4-ADT_A45_MERGE_INFO:

ADT_A45_MERGE_INFO HL7 v2 ADT_A45.MERGE_INFO group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ADT_A45_MERGE_INFO.ADT_A45_MERGE_INFO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MRG``
     - :ref:`MRG <hl7-v2_4-MRG>`
     - required
     - Merge patient information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit

.. _hl7-v2_4-BAR_P01_INSURANCE:

BAR_P01_INSURANCE HL7 v2 BAR_P01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P01_INSURANCE.BAR_P01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-BAR_P01_PROCEDURE:

BAR_P01_PROCEDURE HL7 v2 BAR_P01.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P01_PROCEDURE.BAR_P01_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-BAR_P01_VISIT:

BAR_P01_VISIT HL7 v2 BAR_P01.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P01_VISIT.BAR_P01_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_4-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_4-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`BAR_P01_PROCEDURE <hl7-v2_4-BAR_P01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_4-NK1>`]]
     - optional
     - Next of kin / associated parties
   * - ``INSURANCE``
     - Optional[List[:ref:`BAR_P01_INSURANCE <hl7-v2_4-BAR_P01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_4-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_4-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_4-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_4-BAR_P02_PATIENT:

BAR_P02_PATIENT HL7 v2 BAR_P02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P02_PATIENT.BAR_P02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_4-DB1>`]]
     - optional
     - Disability

.. _hl7-v2_4-BAR_P05_INSURANCE:

BAR_P05_INSURANCE HL7 v2 BAR_P05.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P05_INSURANCE.BAR_P05_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-BAR_P05_PROCEDURE:

BAR_P05_PROCEDURE HL7 v2 BAR_P05.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P05_PROCEDURE.BAR_P05_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-BAR_P05_VISIT:

BAR_P05_VISIT HL7 v2 BAR_P05.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P05_VISIT.BAR_P05_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_4-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_4-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`BAR_P05_PROCEDURE <hl7-v2_4-BAR_P05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_4-NK1>`]]
     - optional
     - Next of kin / associated parties
   * - ``INSURANCE``
     - Optional[List[:ref:`BAR_P05_INSURANCE <hl7-v2_4-BAR_P05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_4-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_4-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_4-UB2>`]
     - optional
     - UB92 Data
   * - ``ABS``
     - Optional[:ref:`ABS <hl7-v2_4-ABS>`]
     - optional
     - Abstract
   * - ``BLC``
     - Optional[List[:ref:`BLC <hl7-v2_4-BLC>`]]
     - optional
     - Blood Code
   * - ``RMI``
     - Optional[:ref:`RMI <hl7-v2_4-RMI>`]
     - optional
     - Risk Management Incident

.. _hl7-v2_4-BAR_P06_PATIENT:

BAR_P06_PATIENT HL7 v2 BAR_P06.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P06_PATIENT.BAR_P06_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit

.. _hl7-v2_4-BAR_P10_PROCEDURE:

BAR_P10_PROCEDURE HL7 v2 BAR_P10.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.BAR_P10_PROCEDURE.BAR_P10_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``GP2``
     - Optional[:ref:`GP2 <hl7-v2_4-GP2>`]
     - optional
     - Grouping/Reimbursement - Procedure Line Item

.. _hl7-v2_4-CRM_C01_PATIENT:

CRM_C01_PATIENT HL7 v2 CRM_C01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CRM_C01_PATIENT.CRM_C01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``CSR``
     - :ref:`CSR <hl7-v2_4-CSR>`
     - required
     - Clinical Study Registration
   * - ``CSP``
     - Optional[List[:ref:`CSP <hl7-v2_4-CSP>`]]
     - optional
     - Clinical Study Phase

.. _hl7-v2_4-CSU_C09_PATIENT:

CSU_C09_PATIENT HL7 v2 CSU_C09.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CSU_C09_PATIENT.CSU_C09_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`CSU_C09_VISIT <hl7-v2_4-CSU_C09_VISIT>`]
     - optional
     - VISIT
   * - ``CSR``
     - :ref:`CSR <hl7-v2_4-CSR>`
     - required
     - Clinical Study Registration
   * - ``STUDY_PHASE``
     - List[:ref:`CSU_C09_STUDY_PHASE <hl7-v2_4-CSU_C09_STUDY_PHASE>`]
     - required
     - STUDY_PHASE

.. _hl7-v2_4-CSU_C09_RX_ADMIN:

CSU_C09_RX_ADMIN HL7 v2 CSU_C09.RX_ADMIN group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CSU_C09_RX_ADMIN.CSU_C09_RX_ADMIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_4-RXA>`
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - :ref:`RXR <hl7-v2_4-RXR>`
     - required
     - Pharmacy/Treatment Route

.. _hl7-v2_4-CSU_C09_STUDY_OBSERVATION:

CSU_C09_STUDY_OBSERVATION HL7 v2 CSU_C09.STUDY_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CSU_C09_STUDY_OBSERVATION.CSU_C09_STUDY_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``OBX``
     - List[:ref:`OBX <hl7-v2_4-OBX>`]
     - required
     - Observation/Result

.. _hl7-v2_4-CSU_C09_STUDY_PHARM:

CSU_C09_STUDY_PHARM HL7 v2 CSU_C09.STUDY_PHARM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CSU_C09_STUDY_PHARM.CSU_C09_STUDY_PHARM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``RX_ADMIN``
     - List[:ref:`CSU_C09_RX_ADMIN <hl7-v2_4-CSU_C09_RX_ADMIN>`]
     - required
     - RX_ADMIN

.. _hl7-v2_4-CSU_C09_STUDY_PHASE:

CSU_C09_STUDY_PHASE HL7 v2 CSU_C09.STUDY_PHASE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CSU_C09_STUDY_PHASE.CSU_C09_STUDY_PHASE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CSP``
     - Optional[List[:ref:`CSP <hl7-v2_4-CSP>`]]
     - optional
     - Clinical Study Phase
   * - ``STUDY_SCHEDULE``
     - List[:ref:`CSU_C09_STUDY_SCHEDULE <hl7-v2_4-CSU_C09_STUDY_SCHEDULE>`]
     - required
     - STUDY_SCHEDULE

.. _hl7-v2_4-CSU_C09_STUDY_SCHEDULE:

CSU_C09_STUDY_SCHEDULE HL7 v2 CSU_C09.STUDY_SCHEDULE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CSU_C09_STUDY_SCHEDULE.CSU_C09_STUDY_SCHEDULE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CSS``
     - Optional[:ref:`CSS <hl7-v2_4-CSS>`]
     - optional
     - Clinical Study Data Schedule Segment
   * - ``STUDY_OBSERVATION``
     - List[:ref:`CSU_C09_STUDY_OBSERVATION <hl7-v2_4-CSU_C09_STUDY_OBSERVATION>`]
     - required
     - STUDY_OBSERVATION
   * - ``STUDY_PHARM``
     - List[:ref:`CSU_C09_STUDY_PHARM <hl7-v2_4-CSU_C09_STUDY_PHARM>`]
     - required
     - STUDY_PHARM

.. _hl7-v2_4-CSU_C09_VISIT:

CSU_C09_VISIT HL7 v2 CSU_C09.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.CSU_C09_VISIT.CSU_C09_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-DFT_P03_COMMON_ORDER:

DFT_P03_COMMON_ORDER HL7 v2 DFT_P03.COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_COMMON_ORDER.DFT_P03_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``ORDER``
     - Optional[:ref:`DFT_P03_ORDER <hl7-v2_4-DFT_P03_ORDER>`]
     - optional
     - ORDER
   * - ``OBSERVATION``
     - Optional[List[:ref:`DFT_P03_OBSERVATION <hl7-v2_4-DFT_P03_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_4-DFT_P03_FINANCIAL:

DFT_P03_FINANCIAL HL7 v2 DFT_P03.FINANCIAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_FINANCIAL.DFT_P03_FINANCIAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``FT1``
     - :ref:`FT1 <hl7-v2_4-FT1>`
     - required
     - Financial Transaction
   * - ``FINANCIAL_PROCEDURE``
     - Optional[List[:ref:`DFT_P03_FINANCIAL_PROCEDURE <hl7-v2_4-DFT_P03_FINANCIAL_PROCEDURE>`]]
     - optional
     - FINANCIAL_PROCEDURE
   * - ``FINANCIAL_COMMON_ORDER``
     - Optional[List[:ref:`DFT_P03_FINANCIAL_COMMON_ORDER <hl7-v2_4-DFT_P03_FINANCIAL_COMMON_ORDER>`]]
     - optional
     - FINANCIAL_COMMON_ORDER

.. _hl7-v2_4-DFT_P03_FINANCIAL_COMMON_ORDER:

DFT_P03_FINANCIAL_COMMON_ORDER HL7 v2 DFT_P03.FINANCIAL_COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_FINANCIAL_COMMON_ORDER.DFT_P03_FINANCIAL_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``FINANCIAL_ORDER``
     - Optional[:ref:`DFT_P03_FINANCIAL_ORDER <hl7-v2_4-DFT_P03_FINANCIAL_ORDER>`]
     - optional
     - FINANCIAL_ORDER
   * - ``FINANCIAL_OBSERVATION``
     - Optional[List[:ref:`DFT_P03_FINANCIAL_OBSERVATION <hl7-v2_4-DFT_P03_FINANCIAL_OBSERVATION>`]]
     - optional
     - FINANCIAL_OBSERVATION

.. _hl7-v2_4-DFT_P03_FINANCIAL_OBSERVATION:

DFT_P03_FINANCIAL_OBSERVATION HL7 v2 DFT_P03.FINANCIAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_FINANCIAL_OBSERVATION.DFT_P03_FINANCIAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DFT_P03_FINANCIAL_ORDER:

DFT_P03_FINANCIAL_ORDER HL7 v2 DFT_P03.FINANCIAL_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_FINANCIAL_ORDER.DFT_P03_FINANCIAL_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DFT_P03_FINANCIAL_PROCEDURE:

DFT_P03_FINANCIAL_PROCEDURE HL7 v2 DFT_P03.FINANCIAL_PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_FINANCIAL_PROCEDURE.DFT_P03_FINANCIAL_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-DFT_P03_INSURANCE:

DFT_P03_INSURANCE HL7 v2 DFT_P03.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_INSURANCE.DFT_P03_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-DFT_P03_OBSERVATION:

DFT_P03_OBSERVATION HL7 v2 DFT_P03.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_OBSERVATION.DFT_P03_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DFT_P03_ORDER:

DFT_P03_ORDER HL7 v2 DFT_P03.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P03_ORDER.DFT_P03_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DFT_P11_COMMON_ORDER:

DFT_P11_COMMON_ORDER HL7 v2 DFT_P11.COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_COMMON_ORDER.DFT_P11_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``ORDER``
     - Optional[:ref:`DFT_P11_ORDER <hl7-v2_4-DFT_P11_ORDER>`]
     - optional
     - ORDER
   * - ``OBSERVATION``
     - Optional[List[:ref:`DFT_P11_OBSERVATION <hl7-v2_4-DFT_P11_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_4-DFT_P11_FINANCIAL:

DFT_P11_FINANCIAL HL7 v2 DFT_P11.FINANCIAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_FINANCIAL.DFT_P11_FINANCIAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``FT1``
     - :ref:`FT1 <hl7-v2_4-FT1>`
     - required
     - Financial Transaction
   * - ``FINANCIAL_PROCEDURE``
     - Optional[List[:ref:`DFT_P11_FINANCIAL_PROCEDURE <hl7-v2_4-DFT_P11_FINANCIAL_PROCEDURE>`]]
     - optional
     - FINANCIAL_PROCEDURE
   * - ``FINANCIAL_COMMON_ORDER``
     - Optional[List[:ref:`DFT_P11_FINANCIAL_COMMON_ORDER <hl7-v2_4-DFT_P11_FINANCIAL_COMMON_ORDER>`]]
     - optional
     - FINANCIAL_COMMON_ORDER
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_4-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``FINANCIAL_INSURANCE``
     - Optional[List[:ref:`DFT_P11_FINANCIAL_INSURANCE <hl7-v2_4-DFT_P11_FINANCIAL_INSURANCE>`]]
     - optional
     - FINANCIAL_INSURANCE

.. _hl7-v2_4-DFT_P11_FINANCIAL_COMMON_ORDER:

DFT_P11_FINANCIAL_COMMON_ORDER HL7 v2 DFT_P11.FINANCIAL_COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_FINANCIAL_COMMON_ORDER.DFT_P11_FINANCIAL_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``FINANCIAL_ORDER``
     - Optional[:ref:`DFT_P11_FINANCIAL_ORDER <hl7-v2_4-DFT_P11_FINANCIAL_ORDER>`]
     - optional
     - FINANCIAL_ORDER
   * - ``FINANCIAL_OBSERVATION``
     - Optional[List[:ref:`DFT_P11_FINANCIAL_OBSERVATION <hl7-v2_4-DFT_P11_FINANCIAL_OBSERVATION>`]]
     - optional
     - FINANCIAL_OBSERVATION

.. _hl7-v2_4-DFT_P11_FINANCIAL_INSURANCE:

DFT_P11_FINANCIAL_INSURANCE HL7 v2 DFT_P11.FINANCIAL_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_FINANCIAL_INSURANCE.DFT_P11_FINANCIAL_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-DFT_P11_FINANCIAL_OBSERVATION:

DFT_P11_FINANCIAL_OBSERVATION HL7 v2 DFT_P11.FINANCIAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_FINANCIAL_OBSERVATION.DFT_P11_FINANCIAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DFT_P11_FINANCIAL_ORDER:

DFT_P11_FINANCIAL_ORDER HL7 v2 DFT_P11.FINANCIAL_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_FINANCIAL_ORDER.DFT_P11_FINANCIAL_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DFT_P11_FINANCIAL_PROCEDURE:

DFT_P11_FINANCIAL_PROCEDURE HL7 v2 DFT_P11.FINANCIAL_PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_FINANCIAL_PROCEDURE.DFT_P11_FINANCIAL_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-DFT_P11_INSURANCE:

DFT_P11_INSURANCE HL7 v2 DFT_P11.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_INSURANCE.DFT_P11_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[List[:ref:`IN3 <hl7-v2_4-IN3>`]]
     - optional
     - Insurance Additional Information, Certification
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_4-ROL>`]]
     - optional
     - Role

.. _hl7-v2_4-DFT_P11_OBSERVATION:

DFT_P11_OBSERVATION HL7 v2 DFT_P11.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_OBSERVATION.DFT_P11_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DFT_P11_ORDER:

DFT_P11_ORDER HL7 v2 DFT_P11.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DFT_P11_ORDER.DFT_P11_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-DOC_T12_RESULT:

DOC_T12_RESULT HL7 v2 DOC_T12.RESULT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.DOC_T12_RESULT.DOC_T12_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``EVN``
     - Optional[:ref:`EVN <hl7-v2_4-EVN>`]
     - optional
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``TXA``
     - :ref:`TXA <hl7-v2_4-TXA>`
     - required
     - Transcription Document Header
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_4-EAN_U09_NOTIFICATION:

EAN_U09_NOTIFICATION HL7 v2 EAN_U09.NOTIFICATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.EAN_U09_NOTIFICATION.EAN_U09_NOTIFICATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NDS``
     - :ref:`NDS <hl7-v2_4-NDS>`
     - required
     - Notification Detail
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_4-NTE>`]
     - optional
     - Notes and Comments

.. _hl7-v2_4-EAR_U08_COMMAND_RESPONSE:

EAR_U08_COMMAND_RESPONSE HL7 v2 EAR_U08.COMMAND_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.EAR_U08_COMMAND_RESPONSE.EAR_U08_COMMAND_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ECD``
     - :ref:`ECD <hl7-v2_4-ECD>`
     - required
     - Equipment Command
   * - ``SAC``
     - Optional[:ref:`SAC <hl7-v2_4-SAC>`]
     - optional
     - Specimen and container detail
   * - ``ECR``
     - :ref:`ECR <hl7-v2_4-ECR>`
     - required
     - Equipment Command Response

.. _hl7-v2_4-MFN_M01_MF:

MFN_M01_MF HL7 v2 MFN_M01.MF group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M01_MF.MFN_M01_MF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry

.. _hl7-v2_4-MFN_M02_MF_STAFF:

MFN_M02_MF_STAFF HL7 v2 MFN_M02.MF_STAFF group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M02_MF_STAFF.MFN_M02_MF_STAFF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[:ref:`PRA <hl7-v2_4-PRA>`]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[:ref:`ORG <hl7-v2_4-ORG>`]
     - optional
     - Practitioner Organization Unit

.. _hl7-v2_4-MFN_M03_MF_TEST:

MFN_M03_MF_TEST HL7 v2 MFN_M03.MF_TEST group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M03_MF_TEST.MFN_M03_MF_TEST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_4-OM1>`
     - required
     - General Segment

.. _hl7-v2_4-MFN_M04_MF_CDM:

MFN_M04_MF_CDM HL7 v2 MFN_M04.MF_CDM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M04_MF_CDM.MFN_M04_MF_CDM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``CDM``
     - :ref:`CDM <hl7-v2_4-CDM>`
     - required
     - Charge Description Master
   * - ``PRC``
     - Optional[List[:ref:`PRC <hl7-v2_4-PRC>`]]
     - optional
     - Pricing

.. _hl7-v2_4-MFN_M05_MF_LOCATION:

MFN_M05_MF_LOCATION HL7 v2 MFN_M05.MF_LOCATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M05_MF_LOCATION.MFN_M05_MF_LOCATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``LOC``
     - :ref:`LOC <hl7-v2_4-LOC>`
     - required
     - Location Identification
   * - ``LCH``
     - Optional[List[:ref:`LCH <hl7-v2_4-LCH>`]]
     - optional
     - Location Characteristic
   * - ``LRL``
     - Optional[List[:ref:`LRL <hl7-v2_4-LRL>`]]
     - optional
     - Location Relationship
   * - ``MF_LOC_DEPT``
     - List[:ref:`MFN_M05_MF_LOC_DEPT <hl7-v2_4-MFN_M05_MF_LOC_DEPT>`]
     - required
     - MF_LOC_DEPT

.. _hl7-v2_4-MFN_M05_MF_LOC_DEPT:

MFN_M05_MF_LOC_DEPT HL7 v2 MFN_M05.MF_LOC_DEPT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M05_MF_LOC_DEPT.MFN_M05_MF_LOC_DEPT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``LDP``
     - :ref:`LDP <hl7-v2_4-LDP>`
     - required
     - Location Department
   * - ``LCH``
     - Optional[List[:ref:`LCH <hl7-v2_4-LCH>`]]
     - optional
     - Location Characteristic
   * - ``LCC``
     - Optional[List[:ref:`LCC <hl7-v2_4-LCC>`]]
     - optional
     - Location Charge Code

.. _hl7-v2_4-MFN_M06_MF_CLIN_STUDY:

MFN_M06_MF_CLIN_STUDY HL7 v2 MFN_M06.MF_CLIN_STUDY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M06_MF_CLIN_STUDY.MFN_M06_MF_CLIN_STUDY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``CM0``
     - :ref:`CM0 <hl7-v2_4-CM0>`
     - required
     - Clinical Study Master
   * - ``MF_PHASE_SCHED_DETAIL``
     - Optional[List[:ref:`MFN_M06_MF_PHASE_SCHED_DETAIL <hl7-v2_4-MFN_M06_MF_PHASE_SCHED_DETAIL>`]]
     - optional
     - MF_PHASE_SCHED_DETAIL

.. _hl7-v2_4-MFN_M06_MF_PHASE_SCHED_DETAIL:

MFN_M06_MF_PHASE_SCHED_DETAIL HL7 v2 MFN_M06.MF_PHASE_SCHED_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M06_MF_PHASE_SCHED_DETAIL.MFN_M06_MF_PHASE_SCHED_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CM1``
     - :ref:`CM1 <hl7-v2_4-CM1>`
     - required
     - Clinical Study Phase Master
   * - ``CM2``
     - Optional[List[:ref:`CM2 <hl7-v2_4-CM2>`]]
     - optional
     - Clinical Study Schedule Master

.. _hl7-v2_4-MFN_M07_MF_CLIN_STUDY_SCHED:

MFN_M07_MF_CLIN_STUDY_SCHED HL7 v2 MFN_M07.MF_CLIN_STUDY_SCHED group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M07_MF_CLIN_STUDY_SCHED.MFN_M07_MF_CLIN_STUDY_SCHED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``CM0``
     - :ref:`CM0 <hl7-v2_4-CM0>`
     - required
     - Clinical Study Master
   * - ``CM2``
     - Optional[List[:ref:`CM2 <hl7-v2_4-CM2>`]]
     - optional
     - Clinical Study Schedule Master

.. _hl7-v2_4-MFN_M08_MF_TEST_NUMERIC:

MFN_M08_MF_TEST_NUMERIC HL7 v2 MFN_M08.MF_TEST_NUMERIC group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M08_MF_TEST_NUMERIC.MFN_M08_MF_TEST_NUMERIC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_4-OM1>`
     - required
     - General Segment
   * - ``OM2``
     - Optional[:ref:`OM2 <hl7-v2_4-OM2>`]
     - optional
     - Numeric Observation
   * - ``OM3``
     - Optional[:ref:`OM3 <hl7-v2_4-OM3>`]
     - optional
     - Categorical Service/Test/Observation
   * - ``OM4``
     - Optional[:ref:`OM4 <hl7-v2_4-OM4>`]
     - optional
     - Observations that Require Specimens

.. _hl7-v2_4-MFN_M09_MF_TEST_CATEGORICAL:

MFN_M09_MF_TEST_CATEGORICAL HL7 v2 MFN_M09.MF_TEST_CATEGORICAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M09_MF_TEST_CATEGORICAL.MFN_M09_MF_TEST_CATEGORICAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_4-OM1>`
     - required
     - General Segment
   * - ``MF_TEST_CAT_DETAIL``
     - Optional[:ref:`MFN_M09_MF_TEST_CAT_DETAIL <hl7-v2_4-MFN_M09_MF_TEST_CAT_DETAIL>`]
     - optional
     - MF_TEST_CAT_DETAIL

.. _hl7-v2_4-MFN_M09_MF_TEST_CAT_DETAIL:

MFN_M09_MF_TEST_CAT_DETAIL HL7 v2 MFN_M09.MF_TEST_CAT_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M09_MF_TEST_CAT_DETAIL.MFN_M09_MF_TEST_CAT_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OM3``
     - :ref:`OM3 <hl7-v2_4-OM3>`
     - required
     - Categorical Service/Test/Observation
   * - ``OM4``
     - Optional[List[:ref:`OM4 <hl7-v2_4-OM4>`]]
     - optional
     - Observations that Require Specimens

.. _hl7-v2_4-MFN_M10_MF_TEST_BATTERIES:

MFN_M10_MF_TEST_BATTERIES HL7 v2 MFN_M10.MF_TEST_BATTERIES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M10_MF_TEST_BATTERIES.MFN_M10_MF_TEST_BATTERIES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_4-OM1>`
     - required
     - General Segment
   * - ``MF_TEST_BATT_DETAIL``
     - Optional[:ref:`MFN_M10_MF_TEST_BATT_DETAIL <hl7-v2_4-MFN_M10_MF_TEST_BATT_DETAIL>`]
     - optional
     - MF_TEST_BATT_DETAIL

.. _hl7-v2_4-MFN_M10_MF_TEST_BATT_DETAIL:

MFN_M10_MF_TEST_BATT_DETAIL HL7 v2 MFN_M10.MF_TEST_BATT_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M10_MF_TEST_BATT_DETAIL.MFN_M10_MF_TEST_BATT_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OM5``
     - :ref:`OM5 <hl7-v2_4-OM5>`
     - required
     - Observation Batteries (Sets)
   * - ``OM4``
     - Optional[List[:ref:`OM4 <hl7-v2_4-OM4>`]]
     - optional
     - Observations that Require Specimens

.. _hl7-v2_4-MFN_M11_MF_TEST_CALCULATED:

MFN_M11_MF_TEST_CALCULATED HL7 v2 MFN_M11.MF_TEST_CALCULATED group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M11_MF_TEST_CALCULATED.MFN_M11_MF_TEST_CALCULATED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_4-OM1>`
     - required
     - General Segment
   * - ``MF_TEST_CALC_DETAIL``
     - Optional[:ref:`MFN_M11_MF_TEST_CALC_DETAIL <hl7-v2_4-MFN_M11_MF_TEST_CALC_DETAIL>`]
     - optional
     - MF_TEST_CALC_DETAIL

.. _hl7-v2_4-MFN_M11_MF_TEST_CALC_DETAIL:

MFN_M11_MF_TEST_CALC_DETAIL HL7 v2 MFN_M11.MF_TEST_CALC_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M11_MF_TEST_CALC_DETAIL.MFN_M11_MF_TEST_CALC_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OM6``
     - :ref:`OM6 <hl7-v2_4-OM6>`
     - required
     - Observations that are Calculated from Other Observ
   * - ``OM2``
     - :ref:`OM2 <hl7-v2_4-OM2>`
     - required
     - Numeric Observation

.. _hl7-v2_4-MFN_M12_MF_OBS_ATTRIBUTES:

MFN_M12_MF_OBS_ATTRIBUTES HL7 v2 MFN_M12.MF_OBS_ATTRIBUTES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFN_M12_MF_OBS_ATTRIBUTES.MFN_M12_MF_OBS_ATTRIBUTES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry
   * - ``OM1``
     - :ref:`OM1 <hl7-v2_4-OM1>`
     - required
     - General Segment
   * - ``OM7``
     - Optional[:ref:`OM7 <hl7-v2_4-OM7>`]
     - optional
     - Additional Basic Attributes

.. _hl7-v2_4-MFR_M01_MF_QUERY:

MFR_M01_MF_QUERY HL7 v2 MFR_M01.MF_QUERY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.MFR_M01_MF_QUERY.MFR_M01_MF_QUERY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MFE``
     - :ref:`MFE <hl7-v2_4-MFE>`
     - required
     - Master File Entry

.. _hl7-v2_4-NMD_N02_APP_STATS:

NMD_N02_APP_STATS HL7 v2 NMD_N02.APP_STATS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.NMD_N02_APP_STATS.NMD_N02_APP_STATS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NST``
     - :ref:`NST <hl7-v2_4-NST>`
     - required
     - Application control level statistics
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-NMD_N02_APP_STATUS:

NMD_N02_APP_STATUS HL7 v2 NMD_N02.APP_STATUS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.NMD_N02_APP_STATUS.NMD_N02_APP_STATUS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NSC``
     - :ref:`NSC <hl7-v2_4-NSC>`
     - required
     - Application status change
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-NMD_N02_CLOCK:

NMD_N02_CLOCK HL7 v2 NMD_N02.CLOCK group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.NMD_N02_CLOCK.NMD_N02_CLOCK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NCK``
     - :ref:`NCK <hl7-v2_4-NCK>`
     - required
     - System clock
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-NMD_N02_CLOCK_AND_STATS_WITH_NOTES:

NMD_N02_CLOCK_AND_STATS_WITH_NOTES HL7 v2 NMD_N02.CLOCK_AND_STATS_WITH_NOTES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES.NMD_N02_CLOCK_AND_STATS_WITH_NOTES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CLOCK``
     - Optional[:ref:`NMD_N02_CLOCK <hl7-v2_4-NMD_N02_CLOCK>`]
     - optional
     - CLOCK
   * - ``APP_STATS``
     - Optional[:ref:`NMD_N02_APP_STATS <hl7-v2_4-NMD_N02_APP_STATS>`]
     - optional
     - APP_STATS
   * - ``APP_STATUS``
     - Optional[:ref:`NMD_N02_APP_STATUS <hl7-v2_4-NMD_N02_APP_STATUS>`]
     - optional
     - APP_STATUS

.. _hl7-v2_4-NMQ_N01_CLOCK_AND_STATISTICS:

NMQ_N01_CLOCK_AND_STATISTICS HL7 v2 NMQ_N01.CLOCK_AND_STATISTICS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.NMQ_N01_CLOCK_AND_STATISTICS.NMQ_N01_CLOCK_AND_STATISTICS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NCK``
     - Optional[:ref:`NCK <hl7-v2_4-NCK>`]
     - optional
     - System clock
   * - ``NST``
     - Optional[:ref:`NST <hl7-v2_4-NST>`]
     - optional
     - Application control level statistics
   * - ``NSC``
     - Optional[:ref:`NSC <hl7-v2_4-NSC>`]
     - optional
     - Application status change

.. _hl7-v2_4-NMQ_N01_QRY_WITH_DETAIL:

NMQ_N01_QRY_WITH_DETAIL HL7 v2 NMQ_N01.QRY_WITH_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.NMQ_N01_QRY_WITH_DETAIL.NMQ_N01_QRY_WITH_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_4-QRF>`]
     - optional
     - Original Style Query Filter

.. _hl7-v2_4-NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT:

NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT HL7 v2 NMR_N01.CLOCK_AND_STATS_WITH_NOTES_ALT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT.NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NCK``
     - Optional[:ref:`NCK <hl7-v2_4-NCK>`]
     - optional
     - System clock
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``NST``
     - Optional[:ref:`NST <hl7-v2_4-NST>`]
     - optional
     - Application control level statistics
   * - ``NSC``
     - Optional[:ref:`NSC <hl7-v2_4-NSC>`]
     - optional
     - Application status change

.. _hl7-v2_4-OMD_O03_DIET:

OMD_O03_DIET HL7 v2 OMD_O03.DIET group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMD_O03_DIET.OMD_O03_DIET
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ODS``
     - List[:ref:`ODS <hl7-v2_4-ODS>`]
     - required
     - Dietary Orders, Supplements, and Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``OBSERVATION``
     - Optional[List[:ref:`OMD_O03_OBSERVATION <hl7-v2_4-OMD_O03_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_4-OMD_O03_INSURANCE:

OMD_O03_INSURANCE HL7 v2 OMD_O03.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMD_O03_INSURANCE.OMD_O03_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-OMD_O03_OBSERVATION:

OMD_O03_OBSERVATION HL7 v2 OMD_O03.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMD_O03_OBSERVATION.OMD_O03_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMD_O03_ORDER_DIET:

OMD_O03_ORDER_DIET HL7 v2 OMD_O03.ORDER_DIET group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMD_O03_ORDER_DIET.OMD_O03_ORDER_DIET
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``DIET``
     - Optional[:ref:`OMD_O03_DIET <hl7-v2_4-OMD_O03_DIET>`]
     - optional
     - DIET

.. _hl7-v2_4-OMD_O03_ORDER_TRAY:

OMD_O03_ORDER_TRAY HL7 v2 OMD_O03.ORDER_TRAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMD_O03_ORDER_TRAY.OMD_O03_ORDER_TRAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ODT``
     - List[:ref:`ODT <hl7-v2_4-ODT>`]
     - required
     - Diet Tray Instructions
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMD_O03_PATIENT:

OMD_O03_PATIENT HL7 v2 OMD_O03.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMD_O03_PATIENT.OMD_O03_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMD_O03_PATIENT_VISIT <hl7-v2_4-OMD_O03_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMD_O03_INSURANCE <hl7-v2_4-OMD_O03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-OMD_O03_PATIENT_VISIT:

OMD_O03_PATIENT_VISIT HL7 v2 OMD_O03.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMD_O03_PATIENT_VISIT.OMD_O03_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OMG_O19_INSURANCE:

OMG_O19_INSURANCE HL7 v2 OMG_O19.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_INSURANCE.OMG_O19_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-OMG_O19_OBSERVATION:

OMG_O19_OBSERVATION HL7 v2 OMG_O19.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_OBSERVATION.OMG_O19_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMG_O19_OBSERVATION_PRIOR:

OMG_O19_OBSERVATION_PRIOR HL7 v2 OMG_O19.OBSERVATION_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_OBSERVATION_PRIOR.OMG_O19_OBSERVATION_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMG_O19_ORDER:

OMG_O19_ORDER HL7 v2 OMG_O19.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_ORDER.OMG_O19_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis
   * - ``OBSERVATION``
     - Optional[List[:ref:`OMG_O19_OBSERVATION <hl7-v2_4-OMG_O19_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PRIOR_RESULT``
     - Optional[List[:ref:`OMG_O19_PRIOR_RESULT <hl7-v2_4-OMG_O19_PRIOR_RESULT>`]]
     - optional
     - PRIOR_RESULT
   * - ``FT1``
     - Optional[List[:ref:`FT1 <hl7-v2_4-FT1>`]]
     - optional
     - Financial Transaction
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_4-BLG>`]
     - optional
     - Billing

.. _hl7-v2_4-OMG_O19_ORDER_PRIOR:

OMG_O19_ORDER_PRIOR HL7 v2 OMG_O19.ORDER_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_ORDER_PRIOR.OMG_O19_ORDER_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data
   * - ``OBSERVATION_PRIOR``
     - List[:ref:`OMG_O19_OBSERVATION_PRIOR <hl7-v2_4-OMG_O19_OBSERVATION_PRIOR>`]
     - required
     - OBSERVATION_PRIOR

.. _hl7-v2_4-OMG_O19_PATIENT:

OMG_O19_PATIENT HL7 v2 OMG_O19.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_PATIENT.OMG_O19_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMG_O19_PATIENT_VISIT <hl7-v2_4-OMG_O19_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMG_O19_INSURANCE <hl7-v2_4-OMG_O19_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-OMG_O19_PATIENT_PRIOR:

OMG_O19_PATIENT_PRIOR HL7 v2 OMG_O19.PATIENT_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_PATIENT_PRIOR.OMG_O19_PATIENT_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic

.. _hl7-v2_4-OMG_O19_PATIENT_VISIT:

OMG_O19_PATIENT_VISIT HL7 v2 OMG_O19.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_PATIENT_VISIT.OMG_O19_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OMG_O19_PATIENT_VISIT_PRIOR:

OMG_O19_PATIENT_VISIT_PRIOR HL7 v2 OMG_O19.PATIENT_VISIT_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_PATIENT_VISIT_PRIOR.OMG_O19_PATIENT_VISIT_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OMG_O19_PRIOR_RESULT:

OMG_O19_PRIOR_RESULT HL7 v2 OMG_O19.PRIOR_RESULT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMG_O19_PRIOR_RESULT.OMG_O19_PRIOR_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT_PRIOR``
     - Optional[:ref:`OMG_O19_PATIENT_PRIOR <hl7-v2_4-OMG_O19_PATIENT_PRIOR>`]
     - optional
     - PATIENT_PRIOR
   * - ``PATIENT_VISIT_PRIOR``
     - Optional[:ref:`OMG_O19_PATIENT_VISIT_PRIOR <hl7-v2_4-OMG_O19_PATIENT_VISIT_PRIOR>`]
     - optional
     - PATIENT_VISIT_PRIOR
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``ORDER_PRIOR``
     - List[:ref:`OMG_O19_ORDER_PRIOR <hl7-v2_4-OMG_O19_ORDER_PRIOR>`]
     - required
     - ORDER_PRIOR

.. _hl7-v2_4-OML_O21_CONTAINER_1:

OML_O21_CONTAINER_1 HL7 v2 OML_O21.CONTAINER_1 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_CONTAINER_1.OML_O21_CONTAINER_1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SAC``
     - :ref:`SAC <hl7-v2_4-SAC>`
     - required
     - Specimen and container detail
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_4-OML_O21_CONTAINER_2:

OML_O21_CONTAINER_2 HL7 v2 OML_O21.CONTAINER_2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_CONTAINER_2.OML_O21_CONTAINER_2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SAC``
     - :ref:`SAC <hl7-v2_4-SAC>`
     - required
     - Specimen and container detail
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_4-OML_O21_INSURANCE:

OML_O21_INSURANCE HL7 v2 OML_O21.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_INSURANCE.OML_O21_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-OML_O21_OBSERVATION:

OML_O21_OBSERVATION HL7 v2 OML_O21.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_OBSERVATION.OML_O21_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``TCD``
     - Optional[:ref:`TCD <hl7-v2_4-TCD>`]
     - optional
     - Test Code Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OML_O21_OBSERVATION_PRIOR:

OML_O21_OBSERVATION_PRIOR HL7 v2 OML_O21.OBSERVATION_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_OBSERVATION_PRIOR.OML_O21_OBSERVATION_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OML_O21_OBSERVATION_REQUEST:

OML_O21_OBSERVATION_REQUEST HL7 v2 OML_O21.OBSERVATION_REQUEST group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_OBSERVATION_REQUEST.OML_O21_OBSERVATION_REQUEST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``CONTAINER_2``
     - Optional[List[:ref:`OML_O21_CONTAINER_2 <hl7-v2_4-OML_O21_CONTAINER_2>`]]
     - optional
     - CONTAINER_2
   * - ``TCD``
     - Optional[:ref:`TCD <hl7-v2_4-TCD>`]
     - optional
     - Test Code Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis
   * - ``OBSERVATION``
     - Optional[List[:ref:`OML_O21_OBSERVATION <hl7-v2_4-OML_O21_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PRIOR_RESULT``
     - Optional[List[:ref:`OML_O21_PRIOR_RESULT <hl7-v2_4-OML_O21_PRIOR_RESULT>`]]
     - optional
     - PRIOR_RESULT

.. _hl7-v2_4-OML_O21_ORDER:

OML_O21_ORDER HL7 v2 OML_O21.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_ORDER.OML_O21_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``OBSERVATION_REQUEST``
     - Optional[:ref:`OML_O21_OBSERVATION_REQUEST <hl7-v2_4-OML_O21_OBSERVATION_REQUEST>`]
     - optional
     - OBSERVATION_REQUEST
   * - ``FT1``
     - Optional[List[:ref:`FT1 <hl7-v2_4-FT1>`]]
     - optional
     - Financial Transaction
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_4-BLG>`]
     - optional
     - Billing

.. _hl7-v2_4-OML_O21_ORDER_GENERAL:

OML_O21_ORDER_GENERAL HL7 v2 OML_O21.ORDER_GENERAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_ORDER_GENERAL.OML_O21_ORDER_GENERAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CONTAINER_1``
     - Optional[:ref:`OML_O21_CONTAINER_1 <hl7-v2_4-OML_O21_CONTAINER_1>`]
     - optional
     - CONTAINER_1
   * - ``ORDER``
     - List[:ref:`OML_O21_ORDER <hl7-v2_4-OML_O21_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-OML_O21_ORDER_PRIOR:

OML_O21_ORDER_PRIOR HL7 v2 OML_O21.ORDER_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_ORDER_PRIOR.OML_O21_ORDER_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``OBSERVATION_PRIOR``
     - List[:ref:`OML_O21_OBSERVATION_PRIOR <hl7-v2_4-OML_O21_OBSERVATION_PRIOR>`]
     - required
     - OBSERVATION_PRIOR

.. _hl7-v2_4-OML_O21_PATIENT:

OML_O21_PATIENT HL7 v2 OML_O21.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_PATIENT.OML_O21_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OML_O21_PATIENT_VISIT <hl7-v2_4-OML_O21_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OML_O21_INSURANCE <hl7-v2_4-OML_O21_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-OML_O21_PATIENT_PRIOR:

OML_O21_PATIENT_PRIOR HL7 v2 OML_O21.PATIENT_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_PATIENT_PRIOR.OML_O21_PATIENT_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic

.. _hl7-v2_4-OML_O21_PATIENT_VISIT:

OML_O21_PATIENT_VISIT HL7 v2 OML_O21.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_PATIENT_VISIT.OML_O21_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OML_O21_PATIENT_VISIT_PRIOR:

OML_O21_PATIENT_VISIT_PRIOR HL7 v2 OML_O21.PATIENT_VISIT_PRIOR group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_PATIENT_VISIT_PRIOR.OML_O21_PATIENT_VISIT_PRIOR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OML_O21_PRIOR_RESULT:

OML_O21_PRIOR_RESULT HL7 v2 OML_O21.PRIOR_RESULT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OML_O21_PRIOR_RESULT.OML_O21_PRIOR_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT_PRIOR``
     - Optional[:ref:`OML_O21_PATIENT_PRIOR <hl7-v2_4-OML_O21_PATIENT_PRIOR>`]
     - optional
     - PATIENT_PRIOR
   * - ``PATIENT_VISIT_PRIOR``
     - Optional[:ref:`OML_O21_PATIENT_VISIT_PRIOR <hl7-v2_4-OML_O21_PATIENT_VISIT_PRIOR>`]
     - optional
     - PATIENT_VISIT_PRIOR
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``ORDER_PRIOR``
     - List[:ref:`OML_O21_ORDER_PRIOR <hl7-v2_4-OML_O21_ORDER_PRIOR>`]
     - required
     - ORDER_PRIOR

.. _hl7-v2_4-OMN_O07_INSURANCE:

OMN_O07_INSURANCE HL7 v2 OMN_O07.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMN_O07_INSURANCE.OMN_O07_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-OMN_O07_OBSERVATION:

OMN_O07_OBSERVATION HL7 v2 OMN_O07.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMN_O07_OBSERVATION.OMN_O07_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMN_O07_ORDER:

OMN_O07_ORDER HL7 v2 OMN_O07.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMN_O07_ORDER.OMN_O07_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``RQD``
     - :ref:`RQD <hl7-v2_4-RQD>`
     - required
     - Requisition Detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_4-RQ1>`]
     - optional
     - Requisition Detail-1
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``OBSERVATION``
     - Optional[List[:ref:`OMN_O07_OBSERVATION <hl7-v2_4-OMN_O07_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_4-BLG>`]
     - optional
     - Billing

.. _hl7-v2_4-OMN_O07_PATIENT:

OMN_O07_PATIENT HL7 v2 OMN_O07.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMN_O07_PATIENT.OMN_O07_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMN_O07_PATIENT_VISIT <hl7-v2_4-OMN_O07_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMN_O07_INSURANCE <hl7-v2_4-OMN_O07_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-OMN_O07_PATIENT_VISIT:

OMN_O07_PATIENT_VISIT HL7 v2 OMN_O07.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMN_O07_PATIENT_VISIT.OMN_O07_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OMP_O09_COMPONENT:

OMP_O09_COMPONENT HL7 v2 OMP_O09.COMPONENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMP_O09_COMPONENT.OMP_O09_COMPONENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_4-RXC>`]
     - required
     - Pharmacy/Treatment Component Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMP_O09_INSURANCE:

OMP_O09_INSURANCE HL7 v2 OMP_O09.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMP_O09_INSURANCE.OMP_O09_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-OMP_O09_OBSERVATION:

OMP_O09_OBSERVATION HL7 v2 OMP_O09.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMP_O09_OBSERVATION.OMP_O09_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMP_O09_ORDER:

OMP_O09_ORDER HL7 v2 OMP_O09.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMP_O09_ORDER.OMP_O09_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``COMPONENT``
     - Optional[:ref:`OMP_O09_COMPONENT <hl7-v2_4-OMP_O09_COMPONENT>`]
     - optional
     - COMPONENT
   * - ``OBSERVATION``
     - Optional[List[:ref:`OMP_O09_OBSERVATION <hl7-v2_4-OMP_O09_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``FT1``
     - Optional[List[:ref:`FT1 <hl7-v2_4-FT1>`]]
     - optional
     - Financial Transaction
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_4-BLG>`]
     - optional
     - Billing

.. _hl7-v2_4-OMP_O09_PATIENT:

OMP_O09_PATIENT HL7 v2 OMP_O09.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMP_O09_PATIENT.OMP_O09_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMP_O09_PATIENT_VISIT <hl7-v2_4-OMP_O09_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMP_O09_INSURANCE <hl7-v2_4-OMP_O09_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-OMP_O09_PATIENT_VISIT:

OMP_O09_PATIENT_VISIT HL7 v2 OMP_O09.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMP_O09_PATIENT_VISIT.OMP_O09_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OMS_O05_INSURANCE:

OMS_O05_INSURANCE HL7 v2 OMS_O05.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMS_O05_INSURANCE.OMS_O05_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-OMS_O05_OBSERVATION:

OMS_O05_OBSERVATION HL7 v2 OMS_O05.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMS_O05_OBSERVATION.OMS_O05_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OMS_O05_ORDER:

OMS_O05_ORDER HL7 v2 OMS_O05.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMS_O05_ORDER.OMS_O05_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``RQD``
     - :ref:`RQD <hl7-v2_4-RQD>`
     - required
     - Requisition Detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_4-RQ1>`]
     - optional
     - Requisition Detail-1
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``OBSERVATION``
     - Optional[List[:ref:`OMS_O05_OBSERVATION <hl7-v2_4-OMS_O05_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_4-BLG>`]
     - optional
     - Billing

.. _hl7-v2_4-OMS_O05_PATIENT:

OMS_O05_PATIENT HL7 v2 OMS_O05.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMS_O05_PATIENT.OMS_O05_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`OMS_O05_PATIENT_VISIT <hl7-v2_4-OMS_O05_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`OMS_O05_INSURANCE <hl7-v2_4-OMS_O05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-OMS_O05_PATIENT_VISIT:

OMS_O05_PATIENT_VISIT HL7 v2 OMS_O05.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OMS_O05_PATIENT_VISIT.OMS_O05_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-ORD_O04_ORDER_DIET:

ORD_O04_ORDER_DIET HL7 v2 ORD_O04.ORDER_DIET group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORD_O04_ORDER_DIET.ORD_O04_ORDER_DIET
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ODS``
     - Optional[List[:ref:`ODS <hl7-v2_4-ODS>`]]
     - optional
     - Dietary Orders, Supplements, and Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORD_O04_ORDER_TRAY:

ORD_O04_ORDER_TRAY HL7 v2 ORD_O04.ORDER_TRAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORD_O04_ORDER_TRAY.ORD_O04_ORDER_TRAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ODT``
     - Optional[List[:ref:`ODT <hl7-v2_4-ODT>`]]
     - optional
     - Diet Tray Instructions
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORD_O04_PATIENT:

ORD_O04_PATIENT HL7 v2 ORD_O04.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORD_O04_PATIENT.ORD_O04_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORD_O04_RESPONSE:

ORD_O04_RESPONSE HL7 v2 ORD_O04.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORD_O04_RESPONSE.ORD_O04_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORD_O04_PATIENT <hl7-v2_4-ORD_O04_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_DIET``
     - List[:ref:`ORD_O04_ORDER_DIET <hl7-v2_4-ORD_O04_ORDER_DIET>`]
     - required
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - Optional[List[:ref:`ORD_O04_ORDER_TRAY <hl7-v2_4-ORD_O04_ORDER_TRAY>`]]
     - optional
     - ORDER_TRAY

.. _hl7-v2_4-ORF_R04_OBSERVATION:

ORF_R04_OBSERVATION HL7 v2 ORF_R04.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORF_R04_OBSERVATION.ORF_R04_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORF_R04_ORDER:

ORF_R04_ORDER HL7 v2 ORF_R04.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORF_R04_ORDER.ORF_R04_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data
   * - ``OBSERVATION``
     - List[:ref:`ORF_R04_OBSERVATION <hl7-v2_4-ORF_R04_OBSERVATION>`]
     - required
     - OBSERVATION
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-ORF_R04_PATIENT:

ORF_R04_PATIENT HL7 v2 ORF_R04.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORF_R04_PATIENT.ORF_R04_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORF_R04_RESPONSE:

ORF_R04_RESPONSE HL7 v2 ORF_R04.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORF_R04_RESPONSE.ORF_R04_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORF_R04_PATIENT <hl7-v2_4-ORF_R04_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORF_R04_ORDER <hl7-v2_4-ORF_R04_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-ORG_O20_ORDER:

ORG_O20_ORDER HL7 v2 ORG_O20.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORG_O20_ORDER.ORG_O20_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-ORG_O20_PATIENT:

ORG_O20_PATIENT HL7 v2 ORG_O20.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORG_O20_PATIENT.ORG_O20_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORG_O20_RESPONSE:

ORG_O20_RESPONSE HL7 v2 ORG_O20.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORG_O20_RESPONSE.ORG_O20_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORG_O20_PATIENT <hl7-v2_4-ORG_O20_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORG_O20_ORDER <hl7-v2_4-ORG_O20_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-ORL_O22_CONTAINER:

ORL_O22_CONTAINER HL7 v2 ORL_O22.CONTAINER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORL_O22_CONTAINER.ORL_O22_CONTAINER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SAC``
     - :ref:`SAC <hl7-v2_4-SAC>`
     - required
     - Specimen and container detail
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_4-ORL_O22_GENERAL_ORDER:

ORL_O22_GENERAL_ORDER HL7 v2 ORL_O22.GENERAL_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORL_O22_GENERAL_ORDER.ORL_O22_GENERAL_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CONTAINER``
     - Optional[:ref:`ORL_O22_CONTAINER <hl7-v2_4-ORL_O22_CONTAINER>`]
     - optional
     - CONTAINER
   * - ``ORDER``
     - Optional[List[:ref:`ORL_O22_ORDER <hl7-v2_4-ORL_O22_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-ORL_O22_OBSERVATION_REQUEST:

ORL_O22_OBSERVATION_REQUEST HL7 v2 ORL_O22.OBSERVATION_REQUEST group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORL_O22_OBSERVATION_REQUEST.ORL_O22_OBSERVATION_REQUEST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``SAC``
     - Optional[List[:ref:`SAC <hl7-v2_4-SAC>`]]
     - optional
     - Specimen and container detail

.. _hl7-v2_4-ORL_O22_ORDER:

ORL_O22_ORDER HL7 v2 ORL_O22.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORL_O22_ORDER.ORL_O22_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``OBSERVATION_REQUEST``
     - Optional[:ref:`ORL_O22_OBSERVATION_REQUEST <hl7-v2_4-ORL_O22_OBSERVATION_REQUEST>`]
     - optional
     - OBSERVATION_REQUEST

.. _hl7-v2_4-ORL_O22_PATIENT:

ORL_O22_PATIENT HL7 v2 ORL_O22.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORL_O22_PATIENT.ORL_O22_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``GENERAL_ORDER``
     - List[:ref:`ORL_O22_GENERAL_ORDER <hl7-v2_4-ORL_O22_GENERAL_ORDER>`]
     - required
     - GENERAL_ORDER

.. _hl7-v2_4-ORL_O22_RESPONSE:

ORL_O22_RESPONSE HL7 v2 ORL_O22.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORL_O22_RESPONSE.ORL_O22_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORL_O22_PATIENT <hl7-v2_4-ORL_O22_PATIENT>`]
     - optional
     - PATIENT

.. _hl7-v2_4-ORM_O01_CHOICE:

ORM_O01_CHOICE HL7 v2 ORM_O01.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORM_O01_CHOICE.ORM_O01_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RQD``
     - Optional[:ref:`RQD <hl7-v2_4-RQD>`]
     - optional
     - Requisition Detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_4-RQ1>`]
     - optional
     - Requisition Detail-1
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order
   * - ``ODS``
     - Optional[:ref:`ODS <hl7-v2_4-ODS>`]
     - optional
     - Dietary Orders, Supplements, and Preferences
   * - ``ODT``
     - Optional[:ref:`ODT <hl7-v2_4-ODT>`]
     - optional
     - Diet Tray Instructions

.. _hl7-v2_4-ORM_O01_INSURANCE:

ORM_O01_INSURANCE HL7 v2 ORM_O01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORM_O01_INSURANCE.ORM_O01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-ORM_O01_OBSERVATION:

ORM_O01_OBSERVATION HL7 v2 ORM_O01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORM_O01_OBSERVATION.ORM_O01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORM_O01_ORDER:

ORM_O01_ORDER HL7 v2 ORM_O01.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORM_O01_ORDER.ORM_O01_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`ORM_O01_ORDER_DETAIL <hl7-v2_4-ORM_O01_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``FT1``
     - Optional[List[:ref:`FT1 <hl7-v2_4-FT1>`]]
     - optional
     - Financial Transaction
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification
   * - ``BLG``
     - Optional[:ref:`BLG <hl7-v2_4-BLG>`]
     - optional
     - Billing

.. _hl7-v2_4-ORM_O01_ORDER_DETAIL:

ORM_O01_ORDER_DETAIL HL7 v2 ORM_O01.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`ORM_O01_CHOICE <hl7-v2_4-ORM_O01_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis
   * - ``OBSERVATION``
     - Optional[List[:ref:`ORM_O01_OBSERVATION <hl7-v2_4-ORM_O01_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_4-ORM_O01_PATIENT:

ORM_O01_PATIENT HL7 v2 ORM_O01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORM_O01_PATIENT.ORM_O01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`ORM_O01_PATIENT_VISIT <hl7-v2_4-ORM_O01_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`ORM_O01_INSURANCE <hl7-v2_4-ORM_O01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-ORM_O01_PATIENT_VISIT:

ORM_O01_PATIENT_VISIT HL7 v2 ORM_O01.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORM_O01_PATIENT_VISIT.ORM_O01_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-ORN_O08_ORDER:

ORN_O08_ORDER HL7 v2 ORN_O08.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORN_O08_ORDER.ORN_O08_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``RQD``
     - :ref:`RQD <hl7-v2_4-RQD>`
     - required
     - Requisition Detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_4-RQ1>`]
     - optional
     - Requisition Detail-1
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORN_O08_PATIENT:

ORN_O08_PATIENT HL7 v2 ORN_O08.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORN_O08_PATIENT.ORN_O08_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORN_O08_RESPONSE:

ORN_O08_RESPONSE HL7 v2 ORN_O08.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORN_O08_RESPONSE.ORN_O08_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORN_O08_PATIENT <hl7-v2_4-ORN_O08_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORN_O08_ORDER <hl7-v2_4-ORN_O08_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-ORP_O10_ORDER:

ORP_O10_ORDER HL7 v2 ORP_O10.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORP_O10_ORDER.ORP_O10_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`ORP_O10_ORDER_DETAIL <hl7-v2_4-ORP_O10_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-ORP_O10_ORDER_DETAIL:

ORP_O10_ORDER_DETAIL HL7 v2 ORP_O10.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORP_O10_ORDER_DETAIL.ORP_O10_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-ORP_O10_PATIENT:

ORP_O10_PATIENT HL7 v2 ORP_O10.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORP_O10_PATIENT.ORP_O10_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORP_O10_RESPONSE:

ORP_O10_RESPONSE HL7 v2 ORP_O10.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORP_O10_RESPONSE.ORP_O10_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORP_O10_PATIENT <hl7-v2_4-ORP_O10_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORP_O10_ORDER <hl7-v2_4-ORP_O10_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-ORR_O02_ORDER:

ORR_O02_ORDER HL7 v2 ORR_O02.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORR_O02_ORDER.ORR_O02_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - :ref:`ORR_O02_ORDER_DETAIL <hl7-v2_4-ORR_O02_ORDER_DETAIL>`
     - required
     - ORDER_DETAIL
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-ORR_O02_ORDER_DETAIL:

ORR_O02_ORDER_DETAIL HL7 v2 ORR_O02.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORR_O02_ORDER_DETAIL.ORR_O02_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RQD``
     - Optional[:ref:`RQD <hl7-v2_4-RQD>`]
     - optional
     - Requisition Detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_4-RQ1>`]
     - optional
     - Requisition Detail-1
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order
   * - ``ODS``
     - Optional[:ref:`ODS <hl7-v2_4-ODS>`]
     - optional
     - Dietary Orders, Supplements, and Preferences
   * - ``ODT``
     - Optional[:ref:`ODT <hl7-v2_4-ODT>`]
     - optional
     - Diet Tray Instructions

.. _hl7-v2_4-ORR_O02_PATIENT:

ORR_O02_PATIENT HL7 v2 ORR_O02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORR_O02_PATIENT.ORR_O02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORR_O02_RESPONSE:

ORR_O02_RESPONSE HL7 v2 ORR_O02.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORR_O02_RESPONSE.ORR_O02_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORR_O02_PATIENT <hl7-v2_4-ORR_O02_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORR_O02_ORDER <hl7-v2_4-ORR_O02_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-ORS_O06_ORDER:

ORS_O06_ORDER HL7 v2 ORS_O06.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORS_O06_ORDER.ORS_O06_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``RQD``
     - :ref:`RQD <hl7-v2_4-RQD>`
     - required
     - Requisition Detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_4-RQ1>`]
     - optional
     - Requisition Detail-1
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORS_O06_PATIENT:

ORS_O06_PATIENT HL7 v2 ORS_O06.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORS_O06_PATIENT.ORS_O06_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORS_O06_RSPONSE:

ORS_O06_RSPONSE HL7 v2 ORS_O06.RSPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORS_O06_RSPONSE.ORS_O06_RSPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORS_O06_PATIENT <hl7-v2_4-ORS_O06_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORS_O06_ORDER <hl7-v2_4-ORS_O06_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-ORU_R01_OBSERVATION:

ORU_R01_OBSERVATION HL7 v2 ORU_R01.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORU_R01_OBSERVATION.ORU_R01_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-ORU_R01_ORDER_OBSERVATION:

ORU_R01_ORDER_OBSERVATION HL7 v2 ORU_R01.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORU_R01_ORDER_OBSERVATION.ORU_R01_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data
   * - ``OBSERVATION``
     - List[:ref:`ORU_R01_OBSERVATION <hl7-v2_4-ORU_R01_OBSERVATION>`]
     - required
     - OBSERVATION
   * - ``FT1``
     - Optional[List[:ref:`FT1 <hl7-v2_4-FT1>`]]
     - optional
     - Financial Transaction
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-ORU_R01_PATIENT:

ORU_R01_PATIENT HL7 v2 ORU_R01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORU_R01_PATIENT.ORU_R01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_4-NK1>`]]
     - optional
     - Next of kin / associated parties
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`ORU_R01_VISIT <hl7-v2_4-ORU_R01_VISIT>`]
     - optional
     - VISIT

.. _hl7-v2_4-ORU_R01_PATIENT_RESULT:

ORU_R01_PATIENT_RESULT HL7 v2 ORU_R01.PATIENT_RESULT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT_RESULT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`ORU_R01_PATIENT <hl7-v2_4-ORU_R01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_OBSERVATION``
     - List[:ref:`ORU_R01_ORDER_OBSERVATION <hl7-v2_4-ORU_R01_ORDER_OBSERVATION>`]
     - required
     - ORDER_OBSERVATION

.. _hl7-v2_4-ORU_R01_VISIT:

ORU_R01_VISIT HL7 v2 ORU_R01.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ORU_R01_VISIT.ORU_R01_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-OSR_Q06_CHOICE:

OSR_Q06_CHOICE HL7 v2 OSR_Q06.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OSR_Q06_CHOICE.OSR_Q06_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RQD``
     - Optional[:ref:`RQD <hl7-v2_4-RQD>`]
     - optional
     - Requisition Detail
   * - ``RQ1``
     - Optional[:ref:`RQ1 <hl7-v2_4-RQ1>`]
     - optional
     - Requisition Detail-1
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order
   * - ``ODS``
     - Optional[:ref:`ODS <hl7-v2_4-ODS>`]
     - optional
     - Dietary Orders, Supplements, and Preferences
   * - ``ODT``
     - Optional[:ref:`ODT <hl7-v2_4-ODT>`]
     - optional
     - Diet Tray Instructions

.. _hl7-v2_4-OSR_Q06_ORDER:

OSR_Q06_ORDER HL7 v2 OSR_Q06.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OSR_Q06_ORDER.OSR_Q06_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``CHOICE``
     - :ref:`OSR_Q06_CHOICE <hl7-v2_4-OSR_Q06_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-OSR_Q06_PATIENT:

OSR_Q06_PATIENT HL7 v2 OSR_Q06.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OSR_Q06_PATIENT.OSR_Q06_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OSR_Q06_RESPONSE:

OSR_Q06_RESPONSE HL7 v2 OSR_Q06.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OSR_Q06_RESPONSE.OSR_Q06_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`OSR_Q06_PATIENT <hl7-v2_4-OSR_Q06_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OSR_Q06_ORDER <hl7-v2_4-OSR_Q06_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-OUL_R21_CONTAINER:

OUL_R21_CONTAINER HL7 v2 OUL_R21.CONTAINER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OUL_R21_CONTAINER.OUL_R21_CONTAINER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SAC``
     - :ref:`SAC <hl7-v2_4-SAC>`
     - required
     - Specimen and container detail
   * - ``SID``
     - Optional[:ref:`SID <hl7-v2_4-SID>`]
     - optional
     - Substance Identifier
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_4-OUL_R21_OBSERVATION:

OUL_R21_OBSERVATION HL7 v2 OUL_R21.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OUL_R21_OBSERVATION.OUL_R21_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``TCD``
     - Optional[:ref:`TCD <hl7-v2_4-TCD>`]
     - optional
     - Test Code Detail
   * - ``SID``
     - Optional[List[:ref:`SID <hl7-v2_4-SID>`]]
     - optional
     - Substance Identifier
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OUL_R21_ORDER_OBSERVATION:

OUL_R21_ORDER_OBSERVATION HL7 v2 OUL_R21.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OUL_R21_ORDER_OBSERVATION.OUL_R21_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CONTAINER``
     - Optional[:ref:`OUL_R21_CONTAINER <hl7-v2_4-OUL_R21_CONTAINER>`]
     - optional
     - CONTAINER
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``OBSERVATION``
     - List[:ref:`OUL_R21_OBSERVATION <hl7-v2_4-OUL_R21_OBSERVATION>`]
     - required
     - OBSERVATION
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-OUL_R21_PATIENT:

OUL_R21_PATIENT HL7 v2 OUL_R21.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OUL_R21_PATIENT.OUL_R21_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-OUL_R21_VISIT:

OUL_R21_VISIT HL7 v2 OUL_R21.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.OUL_R21_VISIT.OUL_R21_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PEX_P07_ASSOCIATED_PERSON:

PEX_P07_ASSOCIATED_PERSON HL7 v2 PEX_P07.ASSOCIATED_PERSON group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_ASSOCIATED_PERSON.PEX_P07_ASSOCIATED_PERSON
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NK1``
     - :ref:`NK1 <hl7-v2_4-NK1>`
     - required
     - Next of kin / associated parties
   * - ``ASSOCIATED_RX_ORDER``
     - Optional[:ref:`PEX_P07_ASSOCIATED_RX_ORDER <hl7-v2_4-PEX_P07_ASSOCIATED_RX_ORDER>`]
     - optional
     - ASSOCIATED_RX_ORDER
   * - ``ASSOCIATED_RX_ADMIN``
     - Optional[List[:ref:`PEX_P07_ASSOCIATED_RX_ADMIN <hl7-v2_4-PEX_P07_ASSOCIATED_RX_ADMIN>`]]
     - optional
     - ASSOCIATED_RX_ADMIN
   * - ``PRB``
     - Optional[List[:ref:`PRB <hl7-v2_4-PRB>`]]
     - optional
     - Problem Details
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_4-PEX_P07_ASSOCIATED_RX_ADMIN:

PEX_P07_ASSOCIATED_RX_ADMIN HL7 v2 PEX_P07.ASSOCIATED_RX_ADMIN group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_ASSOCIATED_RX_ADMIN.PEX_P07_ASSOCIATED_RX_ADMIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_4-RXA>`
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_4-RXR>`]
     - optional
     - Pharmacy/Treatment Route

.. _hl7-v2_4-PEX_P07_ASSOCIATED_RX_ORDER:

PEX_P07_ASSOCIATED_RX_ORDER HL7 v2 PEX_P07.ASSOCIATED_RX_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_ASSOCIATED_RX_ORDER.PEX_P07_ASSOCIATED_RX_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - Optional[List[:ref:`RXR <hl7-v2_4-RXR>`]]
     - optional
     - Pharmacy/Treatment Route

.. _hl7-v2_4-PEX_P07_EXPERIENCE:

PEX_P07_EXPERIENCE HL7 v2 PEX_P07.EXPERIENCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_EXPERIENCE.PEX_P07_EXPERIENCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PES``
     - :ref:`PES <hl7-v2_4-PES>`
     - required
     - Product Experience Sender
   * - ``PEX_OBSERVATION``
     - List[:ref:`PEX_P07_PEX_OBSERVATION <hl7-v2_4-PEX_P07_PEX_OBSERVATION>`]
     - required
     - PEX_OBSERVATION

.. _hl7-v2_4-PEX_P07_PEX_CAUSE:

PEX_P07_PEX_CAUSE HL7 v2 PEX_P07.PEX_CAUSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_PEX_CAUSE.PEX_P07_PEX_CAUSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PCR``
     - :ref:`PCR <hl7-v2_4-PCR>`
     - required
     - Possible Causal Relationship
   * - ``RX_ORDER``
     - Optional[:ref:`PEX_P07_RX_ORDER <hl7-v2_4-PEX_P07_RX_ORDER>`]
     - optional
     - RX_ORDER
   * - ``RX_ADMINISTRATION``
     - Optional[List[:ref:`PEX_P07_RX_ADMINISTRATION <hl7-v2_4-PEX_P07_RX_ADMINISTRATION>`]]
     - optional
     - RX_ADMINISTRATION
   * - ``PRB``
     - Optional[List[:ref:`PRB <hl7-v2_4-PRB>`]]
     - optional
     - Problem Details
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``ASSOCIATED_PERSON``
     - Optional[:ref:`PEX_P07_ASSOCIATED_PERSON <hl7-v2_4-PEX_P07_ASSOCIATED_PERSON>`]
     - optional
     - ASSOCIATED_PERSON
   * - ``STUDY``
     - Optional[List[:ref:`PEX_P07_STUDY <hl7-v2_4-PEX_P07_STUDY>`]]
     - optional
     - STUDY

.. _hl7-v2_4-PEX_P07_PEX_OBSERVATION:

PEX_P07_PEX_OBSERVATION HL7 v2 PEX_P07.PEX_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_PEX_OBSERVATION.PEX_P07_PEX_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PEO``
     - :ref:`PEO <hl7-v2_4-PEO>`
     - required
     - Product Experience Observation
   * - ``PEX_CAUSE``
     - List[:ref:`PEX_P07_PEX_CAUSE <hl7-v2_4-PEX_P07_PEX_CAUSE>`]
     - required
     - PEX_CAUSE

.. _hl7-v2_4-PEX_P07_RX_ADMINISTRATION:

PEX_P07_RX_ADMINISTRATION HL7 v2 PEX_P07.RX_ADMINISTRATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_RX_ADMINISTRATION.PEX_P07_RX_ADMINISTRATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_4-RXA>`
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_4-RXR>`]
     - optional
     - Pharmacy/Treatment Route

.. _hl7-v2_4-PEX_P07_RX_ORDER:

PEX_P07_RX_ORDER HL7 v2 PEX_P07.RX_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_RX_ORDER.PEX_P07_RX_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - Optional[List[:ref:`RXR <hl7-v2_4-RXR>`]]
     - optional
     - Pharmacy/Treatment Route

.. _hl7-v2_4-PEX_P07_STUDY:

PEX_P07_STUDY HL7 v2 PEX_P07.STUDY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_STUDY.PEX_P07_STUDY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CSR``
     - :ref:`CSR <hl7-v2_4-CSR>`
     - required
     - Clinical Study Registration
   * - ``CSP``
     - Optional[List[:ref:`CSP <hl7-v2_4-CSP>`]]
     - optional
     - Clinical Study Phase

.. _hl7-v2_4-PEX_P07_VISIT:

PEX_P07_VISIT HL7 v2 PEX_P07.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PEX_P07_VISIT.PEX_P07_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PGL_PC6_GOAL:

PGL_PC6_GOAL HL7 v2 PGL_PC6.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_GOAL.PGL_PC6_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PGL_PC6_GOAL_ROLE <hl7-v2_4-PGL_PC6_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``PATHWAY``
     - Optional[List[:ref:`PGL_PC6_PATHWAY <hl7-v2_4-PGL_PC6_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``OBSERVATION``
     - Optional[List[:ref:`PGL_PC6_OBSERVATION <hl7-v2_4-PGL_PC6_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PGL_PC6_PROBLEM <hl7-v2_4-PGL_PC6_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PGL_PC6_ORDER <hl7-v2_4-PGL_PC6_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PGL_PC6_GOAL_ROLE:

PGL_PC6_GOAL_ROLE HL7 v2 PGL_PC6.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_GOAL_ROLE.PGL_PC6_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PGL_PC6_OBRRXO_SUPPGRP:

PGL_PC6_OBRRXO_SUPPGRP HL7 v2 PGL_PC6.OBRRXO_SUPPGRP group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_OBRRXO_SUPPGRP.PGL_PC6_OBRRXO_SUPPGRP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PGL_PC6_OBSERVATION:

PGL_PC6_OBSERVATION HL7 v2 PGL_PC6.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_OBSERVATION.PGL_PC6_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PGL_PC6_ORDER:

PGL_PC6_ORDER HL7 v2 PGL_PC6.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_ORDER.PGL_PC6_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PGL_PC6_ORDER_DETAIL <hl7-v2_4-PGL_PC6_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PGL_PC6_ORDER_DETAIL:

PGL_PC6_ORDER_DETAIL HL7 v2 PGL_PC6.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_ORDER_DETAIL.PGL_PC6_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBRRXO_SUPPGRP``
     - :ref:`PGL_PC6_OBRRXO_SUPPGRP <hl7-v2_4-PGL_PC6_OBRRXO_SUPPGRP>`
     - required
     - OBRRXO_SUPPGRP
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PGL_PC6_ORDER_OBSERVATION <hl7-v2_4-PGL_PC6_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PGL_PC6_ORDER_OBSERVATION:

PGL_PC6_ORDER_OBSERVATION HL7 v2 PGL_PC6.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_ORDER_OBSERVATION.PGL_PC6_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PGL_PC6_PATHWAY:

PGL_PC6_PATHWAY HL7 v2 PGL_PC6.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_PATHWAY.PGL_PC6_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PGL_PC6_PATIENT_VISIT:

PGL_PC6_PATIENT_VISIT HL7 v2 PGL_PC6.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_PATIENT_VISIT.PGL_PC6_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PGL_PC6_PROBLEM:

PGL_PC6_PROBLEM HL7 v2 PGL_PC6.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_PROBLEM.PGL_PC6_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PGL_PC6_PROBLEM_ROLE <hl7-v2_4-PGL_PC6_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PGL_PC6_PROBLEM_OBSERVATION <hl7-v2_4-PGL_PC6_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_4-PGL_PC6_PROBLEM_OBSERVATION:

PGL_PC6_PROBLEM_OBSERVATION HL7 v2 PGL_PC6.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_PROBLEM_OBSERVATION.PGL_PC6_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PGL_PC6_PROBLEM_ROLE:

PGL_PC6_PROBLEM_ROLE HL7 v2 PGL_PC6.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PGL_PC6_PROBLEM_ROLE.PGL_PC6_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPG_PCG_GOAL:

PPG_PCG_GOAL HL7 v2 PPG_PCG.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_GOAL.PPG_PCG_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPG_PCG_GOAL_ROLE <hl7-v2_4-PPG_PCG_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPG_PCG_GOAL_OBSERVATION <hl7-v2_4-PPG_PCG_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PPG_PCG_PROBLEM <hl7-v2_4-PPG_PCG_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PPG_PCG_ORDER <hl7-v2_4-PPG_PCG_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PPG_PCG_GOAL_OBSERVATION:

PPG_PCG_GOAL_OBSERVATION HL7 v2 PPG_PCG.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_GOAL_OBSERVATION.PPG_PCG_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPG_PCG_GOAL_ROLE:

PPG_PCG_GOAL_ROLE HL7 v2 PPG_PCG.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_GOAL_ROLE.PPG_PCG_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPG_PCG_OBRRXO_SUPPGRP:

PPG_PCG_OBRRXO_SUPPGRP HL7 v2 PPG_PCG.OBRRXO_SUPPGRP group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_OBRRXO_SUPPGRP.PPG_PCG_OBRRXO_SUPPGRP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PPG_PCG_ORDER:

PPG_PCG_ORDER HL7 v2 PPG_PCG.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_ORDER.PPG_PCG_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPG_PCG_ORDER_DETAIL <hl7-v2_4-PPG_PCG_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PPG_PCG_ORDER_DETAIL:

PPG_PCG_ORDER_DETAIL HL7 v2 PPG_PCG.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_ORDER_DETAIL.PPG_PCG_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBRRXO_SUPPGRP``
     - :ref:`PPG_PCG_OBRRXO_SUPPGRP <hl7-v2_4-PPG_PCG_OBRRXO_SUPPGRP>`
     - required
     - OBRRXO_SUPPGRP
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPG_PCG_ORDER_OBSERVATION <hl7-v2_4-PPG_PCG_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PPG_PCG_ORDER_OBSERVATION:

PPG_PCG_ORDER_OBSERVATION HL7 v2 PPG_PCG.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_ORDER_OBSERVATION.PPG_PCG_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPG_PCG_PATHWAY:

PPG_PCG_PATHWAY HL7 v2 PPG_PCG.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_PATHWAY.PPG_PCG_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PPG_PCG_PATHWAY_ROLE <hl7-v2_4-PPG_PCG_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``GOAL``
     - Optional[List[:ref:`PPG_PCG_GOAL <hl7-v2_4-PPG_PCG_GOAL>`]]
     - optional
     - GOAL

.. _hl7-v2_4-PPG_PCG_PATHWAY_ROLE:

PPG_PCG_PATHWAY_ROLE HL7 v2 PPG_PCG.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_PATHWAY_ROLE.PPG_PCG_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPG_PCG_PATIENT_VISIT:

PPG_PCG_PATIENT_VISIT HL7 v2 PPG_PCG.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_PATIENT_VISIT.PPG_PCG_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PPG_PCG_PROBLEM:

PPG_PCG_PROBLEM HL7 v2 PPG_PCG.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_PROBLEM.PPG_PCG_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPG_PCG_PROBLEM_ROLE <hl7-v2_4-PPG_PCG_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPG_PCG_PROBLEM_OBSERVATION <hl7-v2_4-PPG_PCG_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_4-PPG_PCG_PROBLEM_OBSERVATION:

PPG_PCG_PROBLEM_OBSERVATION HL7 v2 PPG_PCG.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_PROBLEM_OBSERVATION.PPG_PCG_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPG_PCG_PROBLEM_ROLE:

PPG_PCG_PROBLEM_ROLE HL7 v2 PPG_PCG.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPG_PCG_PROBLEM_ROLE.PPG_PCG_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPP_PCB_CHOICE:

PPP_PCB_CHOICE HL7 v2 PPP_PCB.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_CHOICE.PPP_PCB_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PPP_PCB_GOAL:

PPP_PCB_GOAL HL7 v2 PPP_PCB.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_GOAL.PPP_PCB_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPP_PCB_GOAL_ROLE <hl7-v2_4-PPP_PCB_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPP_PCB_GOAL_OBSERVATION <hl7-v2_4-PPP_PCB_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_4-PPP_PCB_GOAL_OBSERVATION:

PPP_PCB_GOAL_OBSERVATION HL7 v2 PPP_PCB.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_GOAL_OBSERVATION.PPP_PCB_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPP_PCB_GOAL_ROLE:

PPP_PCB_GOAL_ROLE HL7 v2 PPP_PCB.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_GOAL_ROLE.PPP_PCB_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPP_PCB_ORDER:

PPP_PCB_ORDER HL7 v2 PPP_PCB.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_ORDER.PPP_PCB_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPP_PCB_ORDER_DETAIL <hl7-v2_4-PPP_PCB_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PPP_PCB_ORDER_DETAIL:

PPP_PCB_ORDER_DETAIL HL7 v2 PPP_PCB.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_ORDER_DETAIL.PPP_PCB_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`PPP_PCB_CHOICE <hl7-v2_4-PPP_PCB_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPP_PCB_ORDER_OBSERVATION <hl7-v2_4-PPP_PCB_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PPP_PCB_ORDER_OBSERVATION:

PPP_PCB_ORDER_OBSERVATION HL7 v2 PPP_PCB.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_ORDER_OBSERVATION.PPP_PCB_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPP_PCB_PATHWAY:

PPP_PCB_PATHWAY HL7 v2 PPP_PCB.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_PATHWAY.PPP_PCB_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PPP_PCB_PATHWAY_ROLE <hl7-v2_4-PPP_PCB_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``PROBLEM``
     - Optional[List[:ref:`PPP_PCB_PROBLEM <hl7-v2_4-PPP_PCB_PROBLEM>`]]
     - optional
     - PROBLEM

.. _hl7-v2_4-PPP_PCB_PATHWAY_ROLE:

PPP_PCB_PATHWAY_ROLE HL7 v2 PPP_PCB.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_PATHWAY_ROLE.PPP_PCB_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPP_PCB_PATIENT_VISIT:

PPP_PCB_PATIENT_VISIT HL7 v2 PPP_PCB.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_PATIENT_VISIT.PPP_PCB_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PPP_PCB_PROBLEM:

PPP_PCB_PROBLEM HL7 v2 PPP_PCB.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_PROBLEM.PPP_PCB_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPP_PCB_PROBLEM_ROLE <hl7-v2_4-PPP_PCB_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPP_PCB_PROBLEM_OBSERVATION <hl7-v2_4-PPP_PCB_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PPP_PCB_GOAL <hl7-v2_4-PPP_PCB_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PPP_PCB_ORDER <hl7-v2_4-PPP_PCB_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PPP_PCB_PROBLEM_OBSERVATION:

PPP_PCB_PROBLEM_OBSERVATION HL7 v2 PPP_PCB.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_PROBLEM_OBSERVATION.PPP_PCB_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPP_PCB_PROBLEM_ROLE:

PPP_PCB_PROBLEM_ROLE HL7 v2 PPP_PCB.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPP_PCB_PROBLEM_ROLE.PPP_PCB_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPR_PC1_CHOICE:

PPR_PC1_CHOICE HL7 v2 PPR_PC1.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_CHOICE.PPR_PC1_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PPR_PC1_GOAL:

PPR_PC1_GOAL HL7 v2 PPR_PC1.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_GOAL.PPR_PC1_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPR_PC1_GOAL_ROLE <hl7-v2_4-PPR_PC1_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPR_PC1_GOAL_OBSERVATION <hl7-v2_4-PPR_PC1_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_4-PPR_PC1_GOAL_OBSERVATION:

PPR_PC1_GOAL_OBSERVATION HL7 v2 PPR_PC1.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_GOAL_OBSERVATION.PPR_PC1_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPR_PC1_GOAL_ROLE:

PPR_PC1_GOAL_ROLE HL7 v2 PPR_PC1.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_GOAL_ROLE.PPR_PC1_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPR_PC1_ORDER:

PPR_PC1_ORDER HL7 v2 PPR_PC1.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_ORDER.PPR_PC1_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPR_PC1_ORDER_DETAIL <hl7-v2_4-PPR_PC1_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PPR_PC1_ORDER_DETAIL:

PPR_PC1_ORDER_DETAIL HL7 v2 PPR_PC1.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_ORDER_DETAIL.PPR_PC1_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`PPR_PC1_CHOICE <hl7-v2_4-PPR_PC1_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPR_PC1_ORDER_OBSERVATION <hl7-v2_4-PPR_PC1_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PPR_PC1_ORDER_OBSERVATION:

PPR_PC1_ORDER_OBSERVATION HL7 v2 PPR_PC1.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_ORDER_OBSERVATION.PPR_PC1_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPR_PC1_PATHWAY:

PPR_PC1_PATHWAY HL7 v2 PPR_PC1.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_PATHWAY.PPR_PC1_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPR_PC1_PATIENT_VISIT:

PPR_PC1_PATIENT_VISIT HL7 v2 PPR_PC1.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_PATIENT_VISIT.PPR_PC1_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PPR_PC1_PROBLEM:

PPR_PC1_PROBLEM HL7 v2 PPR_PC1.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_PROBLEM.PPR_PC1_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPR_PC1_PROBLEM_ROLE <hl7-v2_4-PPR_PC1_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PATHWAY``
     - Optional[List[:ref:`PPR_PC1_PATHWAY <hl7-v2_4-PPR_PC1_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPR_PC1_PROBLEM_OBSERVATION <hl7-v2_4-PPR_PC1_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PPR_PC1_GOAL <hl7-v2_4-PPR_PC1_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PPR_PC1_ORDER <hl7-v2_4-PPR_PC1_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PPR_PC1_PROBLEM_OBSERVATION:

PPR_PC1_PROBLEM_OBSERVATION HL7 v2 PPR_PC1.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_PROBLEM_OBSERVATION.PPR_PC1_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPR_PC1_PROBLEM_ROLE:

PPR_PC1_PROBLEM_ROLE HL7 v2 PPR_PC1.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPR_PC1_PROBLEM_ROLE.PPR_PC1_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPT_PCL_CHOICE:

PPT_PCL_CHOICE HL7 v2 PPT_PCL.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_CHOICE.PPT_PCL_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PPT_PCL_GOAL:

PPT_PCL_GOAL HL7 v2 PPT_PCL.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_GOAL.PPT_PCL_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPT_PCL_GOAL_ROLE <hl7-v2_4-PPT_PCL_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPT_PCL_GOAL_OBSERVATION <hl7-v2_4-PPT_PCL_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PPT_PCL_PROBLEM <hl7-v2_4-PPT_PCL_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PPT_PCL_ORDER <hl7-v2_4-PPT_PCL_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PPT_PCL_GOAL_OBSERVATION:

PPT_PCL_GOAL_OBSERVATION HL7 v2 PPT_PCL.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_GOAL_OBSERVATION.PPT_PCL_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPT_PCL_GOAL_ROLE:

PPT_PCL_GOAL_ROLE HL7 v2 PPT_PCL.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_GOAL_ROLE.PPT_PCL_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPT_PCL_ORDER:

PPT_PCL_ORDER HL7 v2 PPT_PCL.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_ORDER.PPT_PCL_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPT_PCL_ORDER_DETAIL <hl7-v2_4-PPT_PCL_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PPT_PCL_ORDER_DETAIL:

PPT_PCL_ORDER_DETAIL HL7 v2 PPT_PCL.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_ORDER_DETAIL.PPT_PCL_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`PPT_PCL_CHOICE <hl7-v2_4-PPT_PCL_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPT_PCL_ORDER_OBSERVATION <hl7-v2_4-PPT_PCL_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PPT_PCL_ORDER_OBSERVATION:

PPT_PCL_ORDER_OBSERVATION HL7 v2 PPT_PCL.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_ORDER_OBSERVATION.PPT_PCL_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPT_PCL_PATHWAY:

PPT_PCL_PATHWAY HL7 v2 PPT_PCL.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_PATHWAY.PPT_PCL_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PPT_PCL_PATHWAY_ROLE <hl7-v2_4-PPT_PCL_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``GOAL``
     - Optional[List[:ref:`PPT_PCL_GOAL <hl7-v2_4-PPT_PCL_GOAL>`]]
     - optional
     - GOAL

.. _hl7-v2_4-PPT_PCL_PATHWAY_ROLE:

PPT_PCL_PATHWAY_ROLE HL7 v2 PPT_PCL.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_PATHWAY_ROLE.PPT_PCL_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPT_PCL_PATIENT:

PPT_PCL_PATIENT HL7 v2 PPT_PCL.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_PATIENT.PPT_PCL_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPT_PCL_PATIENT_VISIT <hl7-v2_4-PPT_PCL_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPT_PCL_PATHWAY <hl7-v2_4-PPT_PCL_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_4-PPT_PCL_PATIENT_VISIT:

PPT_PCL_PATIENT_VISIT HL7 v2 PPT_PCL.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_PATIENT_VISIT.PPT_PCL_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PPT_PCL_PROBLEM:

PPT_PCL_PROBLEM HL7 v2 PPT_PCL.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_PROBLEM.PPT_PCL_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPT_PCL_PROBLEM_ROLE <hl7-v2_4-PPT_PCL_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPT_PCL_PROBLEM_OBSERVATION <hl7-v2_4-PPT_PCL_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_4-PPT_PCL_PROBLEM_OBSERVATION:

PPT_PCL_PROBLEM_OBSERVATION HL7 v2 PPT_PCL.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_PROBLEM_OBSERVATION.PPT_PCL_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPT_PCL_PROBLEM_ROLE:

PPT_PCL_PROBLEM_ROLE HL7 v2 PPT_PCL.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPT_PCL_PROBLEM_ROLE.PPT_PCL_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPV_PCA_CHOICE:

PPV_PCA_CHOICE HL7 v2 PPV_PCA.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_CHOICE.PPV_PCA_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PPV_PCA_GOAL:

PPV_PCA_GOAL HL7 v2 PPV_PCA.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_GOAL.PPV_PCA_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PPV_PCA_GOAL_ROLE <hl7-v2_4-PPV_PCA_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_PATHWAY``
     - Optional[List[:ref:`PPV_PCA_GOAL_PATHWAY <hl7-v2_4-PPV_PCA_GOAL_PATHWAY>`]]
     - optional
     - GOAL_PATHWAY
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PPV_PCA_GOAL_OBSERVATION <hl7-v2_4-PPV_PCA_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION
   * - ``PROBLEM``
     - Optional[List[:ref:`PPV_PCA_PROBLEM <hl7-v2_4-PPV_PCA_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``ORDER``
     - Optional[List[:ref:`PPV_PCA_ORDER <hl7-v2_4-PPV_PCA_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PPV_PCA_GOAL_OBSERVATION:

PPV_PCA_GOAL_OBSERVATION HL7 v2 PPV_PCA.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_GOAL_OBSERVATION.PPV_PCA_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPV_PCA_GOAL_PATHWAY:

PPV_PCA_GOAL_PATHWAY HL7 v2 PPV_PCA.GOAL_PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_GOAL_PATHWAY.PPV_PCA_GOAL_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPV_PCA_GOAL_ROLE:

PPV_PCA_GOAL_ROLE HL7 v2 PPV_PCA.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_GOAL_ROLE.PPV_PCA_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPV_PCA_ORDER:

PPV_PCA_ORDER HL7 v2 PPV_PCA.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_ORDER.PPV_PCA_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PPV_PCA_ORDER_DETAIL <hl7-v2_4-PPV_PCA_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PPV_PCA_ORDER_DETAIL:

PPV_PCA_ORDER_DETAIL HL7 v2 PPV_PCA.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_ORDER_DETAIL.PPV_PCA_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`PPV_PCA_CHOICE <hl7-v2_4-PPV_PCA_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PPV_PCA_ORDER_OBSERVATION <hl7-v2_4-PPV_PCA_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PPV_PCA_ORDER_OBSERVATION:

PPV_PCA_ORDER_OBSERVATION HL7 v2 PPV_PCA.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_ORDER_OBSERVATION.PPV_PCA_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PPV_PCA_PATIENT:

PPV_PCA_PATIENT HL7 v2 PPV_PCA.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_PATIENT.PPV_PCA_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPV_PCA_PATIENT_VISIT <hl7-v2_4-PPV_PCA_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PPV_PCA_GOAL <hl7-v2_4-PPV_PCA_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_4-PPV_PCA_PATIENT_VISIT:

PPV_PCA_PATIENT_VISIT HL7 v2 PPV_PCA.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_PATIENT_VISIT.PPV_PCA_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PPV_PCA_PROBLEM:

PPV_PCA_PROBLEM HL7 v2 PPV_PCA.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_PROBLEM.PPV_PCA_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PPV_PCA_PROBLEM_ROLE <hl7-v2_4-PPV_PCA_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PPV_PCA_PROBLEM_OBSERVATION <hl7-v2_4-PPV_PCA_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION

.. _hl7-v2_4-PPV_PCA_PROBLEM_OBSERVATION:

PPV_PCA_PROBLEM_OBSERVATION HL7 v2 PPV_PCA.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_PROBLEM_OBSERVATION.PPV_PCA_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PPV_PCA_PROBLEM_ROLE:

PPV_PCA_PROBLEM_ROLE HL7 v2 PPV_PCA.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PPV_PCA_PROBLEM_ROLE.PPV_PCA_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PRR_PC5_CHOICE:

PRR_PC5_CHOICE HL7 v2 PRR_PC5.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_CHOICE.PRR_PC5_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PRR_PC5_GOAL:

PRR_PC5_GOAL HL7 v2 PRR_PC5.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_GOAL.PRR_PC5_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PRR_PC5_GOAL_ROLE <hl7-v2_4-PRR_PC5_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PRR_PC5_GOAL_OBSERVATION <hl7-v2_4-PRR_PC5_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_4-PRR_PC5_GOAL_OBSERVATION:

PRR_PC5_GOAL_OBSERVATION HL7 v2 PRR_PC5.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_GOAL_OBSERVATION.PRR_PC5_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PRR_PC5_GOAL_ROLE:

PRR_PC5_GOAL_ROLE HL7 v2 PRR_PC5.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_GOAL_ROLE.PRR_PC5_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PRR_PC5_ORDER:

PRR_PC5_ORDER HL7 v2 PRR_PC5.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_ORDER.PRR_PC5_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PRR_PC5_ORDER_DETAIL <hl7-v2_4-PRR_PC5_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PRR_PC5_ORDER_DETAIL:

PRR_PC5_ORDER_DETAIL HL7 v2 PRR_PC5.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_ORDER_DETAIL.PRR_PC5_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`PRR_PC5_CHOICE <hl7-v2_4-PRR_PC5_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PRR_PC5_ORDER_OBSERVATION <hl7-v2_4-PRR_PC5_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PRR_PC5_ORDER_OBSERVATION:

PRR_PC5_ORDER_OBSERVATION HL7 v2 PRR_PC5.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_ORDER_OBSERVATION.PRR_PC5_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PRR_PC5_PATIENT:

PRR_PC5_PATIENT HL7 v2 PRR_PC5.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_PATIENT.PRR_PC5_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PRR_PC5_PATIENT_VISIT <hl7-v2_4-PRR_PC5_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PRR_PC5_PROBLEM <hl7-v2_4-PRR_PC5_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_4-PRR_PC5_PATIENT_VISIT:

PRR_PC5_PATIENT_VISIT HL7 v2 PRR_PC5.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_PATIENT_VISIT.PRR_PC5_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PRR_PC5_PROBLEM:

PRR_PC5_PROBLEM HL7 v2 PRR_PC5.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_PROBLEM.PRR_PC5_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PRR_PC5_PROBLEM_ROLE <hl7-v2_4-PRR_PC5_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_PATHWAY``
     - Optional[List[:ref:`PRR_PC5_PROBLEM_PATHWAY <hl7-v2_4-PRR_PC5_PROBLEM_PATHWAY>`]]
     - optional
     - PROBLEM_PATHWAY
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PRR_PC5_PROBLEM_OBSERVATION <hl7-v2_4-PRR_PC5_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PRR_PC5_GOAL <hl7-v2_4-PRR_PC5_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PRR_PC5_ORDER <hl7-v2_4-PRR_PC5_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PRR_PC5_PROBLEM_OBSERVATION:

PRR_PC5_PROBLEM_OBSERVATION HL7 v2 PRR_PC5.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_PROBLEM_OBSERVATION.PRR_PC5_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PRR_PC5_PROBLEM_PATHWAY:

PRR_PC5_PROBLEM_PATHWAY HL7 v2 PRR_PC5.PROBLEM_PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_PROBLEM_PATHWAY.PRR_PC5_PROBLEM_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PRR_PC5_PROBLEM_ROLE:

PRR_PC5_PROBLEM_ROLE HL7 v2 PRR_PC5.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PRR_PC5_PROBLEM_ROLE.PRR_PC5_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PTR_PCF_CHOICE:

PTR_PCF_CHOICE HL7 v2 PTR_PCF.CHOICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_CHOICE.PTR_PCF_CHOICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - Optional[:ref:`OBR <hl7-v2_4-OBR>`]
     - optional
     - Observation Request
   * - ``RXO``
     - Optional[:ref:`RXO <hl7-v2_4-RXO>`]
     - optional
     - Pharmacy/Treatment Order

.. _hl7-v2_4-PTR_PCF_GOAL:

PTR_PCF_GOAL HL7 v2 PTR_PCF.GOAL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_GOAL.PTR_PCF_GOAL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GOL``
     - :ref:`GOL <hl7-v2_4-GOL>`
     - required
     - Goal Detail
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``GOAL_ROLE``
     - Optional[List[:ref:`PTR_PCF_GOAL_ROLE <hl7-v2_4-PTR_PCF_GOAL_ROLE>`]]
     - optional
     - GOAL_ROLE
   * - ``GOAL_OBSERVATION``
     - Optional[List[:ref:`PTR_PCF_GOAL_OBSERVATION <hl7-v2_4-PTR_PCF_GOAL_OBSERVATION>`]]
     - optional
     - GOAL_OBSERVATION

.. _hl7-v2_4-PTR_PCF_GOAL_OBSERVATION:

PTR_PCF_GOAL_OBSERVATION HL7 v2 PTR_PCF.GOAL_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_GOAL_OBSERVATION.PTR_PCF_GOAL_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PTR_PCF_GOAL_ROLE:

PTR_PCF_GOAL_ROLE HL7 v2 PTR_PCF.GOAL_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_GOAL_ROLE.PTR_PCF_GOAL_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PTR_PCF_ORDER:

PTR_PCF_ORDER HL7 v2 PTR_PCF.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_ORDER.PTR_PCF_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`PTR_PCF_ORDER_DETAIL <hl7-v2_4-PTR_PCF_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL

.. _hl7-v2_4-PTR_PCF_ORDER_DETAIL:

PTR_PCF_ORDER_DETAIL HL7 v2 PTR_PCF.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_ORDER_DETAIL.PTR_PCF_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``CHOICE``
     - :ref:`PTR_PCF_CHOICE <hl7-v2_4-PTR_PCF_CHOICE>`
     - required
     - CHOICE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``ORDER_OBSERVATION``
     - Optional[List[:ref:`PTR_PCF_ORDER_OBSERVATION <hl7-v2_4-PTR_PCF_ORDER_OBSERVATION>`]]
     - optional
     - ORDER_OBSERVATION

.. _hl7-v2_4-PTR_PCF_ORDER_OBSERVATION:

PTR_PCF_ORDER_OBSERVATION HL7 v2 PTR_PCF.ORDER_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_ORDER_OBSERVATION.PTR_PCF_ORDER_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PTR_PCF_PATHWAY:

PTR_PCF_PATHWAY HL7 v2 PTR_PCF.PATHWAY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_PATHWAY.PTR_PCF_PATHWAY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PTH``
     - :ref:`PTH <hl7-v2_4-PTH>`
     - required
     - Pathway
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PATHWAY_ROLE``
     - Optional[List[:ref:`PTR_PCF_PATHWAY_ROLE <hl7-v2_4-PTR_PCF_PATHWAY_ROLE>`]]
     - optional
     - PATHWAY_ROLE
   * - ``PROBLEM``
     - Optional[List[:ref:`PTR_PCF_PROBLEM <hl7-v2_4-PTR_PCF_PROBLEM>`]]
     - optional
     - PROBLEM

.. _hl7-v2_4-PTR_PCF_PATHWAY_ROLE:

PTR_PCF_PATHWAY_ROLE HL7 v2 PTR_PCF.PATHWAY_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_PATHWAY_ROLE.PTR_PCF_PATHWAY_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-PTR_PCF_PATIENT:

PTR_PCF_PATIENT HL7 v2 PTR_PCF.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_PATIENT.PTR_PCF_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PTR_PCF_PATIENT_VISIT <hl7-v2_4-PTR_PCF_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PTR_PCF_PATHWAY <hl7-v2_4-PTR_PCF_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_4-PTR_PCF_PATIENT_VISIT:

PTR_PCF_PATIENT_VISIT HL7 v2 PTR_PCF.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_PATIENT_VISIT.PTR_PCF_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-PTR_PCF_PROBLEM:

PTR_PCF_PROBLEM HL7 v2 PTR_PCF.PROBLEM group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_PROBLEM.PTR_PCF_PROBLEM
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRB``
     - :ref:`PRB <hl7-v2_4-PRB>`
     - required
     - Problem Details
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance
   * - ``PROBLEM_ROLE``
     - Optional[List[:ref:`PTR_PCF_PROBLEM_ROLE <hl7-v2_4-PTR_PCF_PROBLEM_ROLE>`]]
     - optional
     - PROBLEM_ROLE
   * - ``PROBLEM_OBSERVATION``
     - Optional[List[:ref:`PTR_PCF_PROBLEM_OBSERVATION <hl7-v2_4-PTR_PCF_PROBLEM_OBSERVATION>`]]
     - optional
     - PROBLEM_OBSERVATION
   * - ``GOAL``
     - Optional[List[:ref:`PTR_PCF_GOAL <hl7-v2_4-PTR_PCF_GOAL>`]]
     - optional
     - GOAL
   * - ``ORDER``
     - Optional[List[:ref:`PTR_PCF_ORDER <hl7-v2_4-PTR_PCF_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_4-PTR_PCF_PROBLEM_OBSERVATION:

PTR_PCF_PROBLEM_OBSERVATION HL7 v2 PTR_PCF.PROBLEM_OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_PROBLEM_OBSERVATION.PTR_PCF_PROBLEM_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-PTR_PCF_PROBLEM_ROLE:

PTR_PCF_PROBLEM_ROLE HL7 v2 PTR_PCF.PROBLEM_ROLE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.PTR_PCF_PROBLEM_ROLE.PTR_PCF_PROBLEM_ROLE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ROL``
     - :ref:`ROL <hl7-v2_4-ROL>`
     - required
     - Role
   * - ``VAR``
     - Optional[List[:ref:`VAR <hl7-v2_4-VAR>`]]
     - optional
     - Variance

.. _hl7-v2_4-QBP_K13_ROW_DEFINITION:

QBP_K13_ROW_DEFINITION HL7 v2 QBP_K13.ROW_DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.QBP_K13_ROW_DEFINITION.QBP_K13_ROW_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - required
     - Table Row Definition
   * - ``RDT``
     - Optional[List[:ref:`RDT <hl7-v2_4-RDT>`]]
     - optional
     - Table Row Data

.. _hl7-v2_4-RAR_RAR_DEFINITION:

RAR_RAR_DEFINITION HL7 v2 RAR_RAR.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAR_RAR_DEFINITION.RAR_RAR_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_4-QRF>`]
     - optional
     - Original Style Query Filter
   * - ``PATIENT``
     - Optional[:ref:`RAR_RAR_PATIENT <hl7-v2_4-RAR_RAR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RAR_RAR_ORDER <hl7-v2_4-RAR_RAR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RAR_RAR_ENCODING:

RAR_RAR_ENCODING HL7 v2 RAR_RAR.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAR_RAR_ENCODING.RAR_RAR_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RAR_RAR_ORDER:

RAR_RAR_ORDER HL7 v2 RAR_RAR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAR_RAR_ORDER.RAR_RAR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ENCODING``
     - Optional[:ref:`RAR_RAR_ENCODING <hl7-v2_4-RAR_RAR_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXA``
     - List[:ref:`RXA <hl7-v2_4-RXA>`]
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - :ref:`RXR <hl7-v2_4-RXR>`
     - required
     - Pharmacy/Treatment Route

.. _hl7-v2_4-RAR_RAR_PATIENT:

RAR_RAR_PATIENT HL7 v2 RAR_RAR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAR_RAR_PATIENT.RAR_RAR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RAS_O17_COMPONENTS:

RAS_O17_COMPONENTS HL7 v2 RAS_O17.COMPONENTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_COMPONENTS.RAS_O17_COMPONENTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_4-RXC>`]
     - required
     - Pharmacy/Treatment Component Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RAS_O17_ENCODING:

RAS_O17_ENCODING HL7 v2 RAS_O17.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_ENCODING.RAS_O17_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RAS_O17_OBSERVATION:

RAS_O17_OBSERVATION HL7 v2 RAS_O17.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_OBSERVATION.RAS_O17_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RAS_O17_ORDER:

RAS_O17_ORDER HL7 v2 RAS_O17.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_ORDER.RAS_O17_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RAS_O17_ORDER_DETAIL <hl7-v2_4-RAS_O17_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODING``
     - Optional[:ref:`RAS_O17_ENCODING <hl7-v2_4-RAS_O17_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXA``
     - List[:ref:`RXA <hl7-v2_4-RXA>`]
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - :ref:`RXR <hl7-v2_4-RXR>`
     - required
     - Pharmacy/Treatment Route
   * - ``OBSERVATION``
     - Optional[List[:ref:`RAS_O17_OBSERVATION <hl7-v2_4-RAS_O17_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-RAS_O17_ORDER_DETAIL:

RAS_O17_ORDER_DETAIL HL7 v2 RAS_O17.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_ORDER_DETAIL.RAS_O17_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``ORDER_DETAIL_SUPPLEMENT``
     - Optional[:ref:`RAS_O17_ORDER_DETAIL_SUPPLEMENT <hl7-v2_4-RAS_O17_ORDER_DETAIL_SUPPLEMENT>`]
     - optional
     - ORDER_DETAIL_SUPPLEMENT

.. _hl7-v2_4-RAS_O17_ORDER_DETAIL_SUPPLEMENT:

RAS_O17_ORDER_DETAIL_SUPPLEMENT HL7 v2 RAS_O17.ORDER_DETAIL_SUPPLEMENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_ORDER_DETAIL_SUPPLEMENT.RAS_O17_ORDER_DETAIL_SUPPLEMENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NTE``
     - List[:ref:`NTE <hl7-v2_4-NTE>`]
     - required
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``COMPONENTS``
     - Optional[:ref:`RAS_O17_COMPONENTS <hl7-v2_4-RAS_O17_COMPONENTS>`]
     - optional
     - COMPONENTS

.. _hl7-v2_4-RAS_O17_PATIENT:

RAS_O17_PATIENT HL7 v2 RAS_O17.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_PATIENT.RAS_O17_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RAS_O17_PATIENT_VISIT <hl7-v2_4-RAS_O17_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT

.. _hl7-v2_4-RAS_O17_PATIENT_VISIT:

RAS_O17_PATIENT_VISIT HL7 v2 RAS_O17.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RAS_O17_PATIENT_VISIT.RAS_O17_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RCI_I05_OBSERVATION:

RCI_I05_OBSERVATION HL7 v2 RCI_I05.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RCI_I05_OBSERVATION.RCI_I05_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESULTS``
     - Optional[List[:ref:`RCI_I05_RESULTS <hl7-v2_4-RCI_I05_RESULTS>`]]
     - optional
     - RESULTS

.. _hl7-v2_4-RCI_I05_PROVIDER:

RCI_I05_PROVIDER HL7 v2 RCI_I05.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RCI_I05_PROVIDER.RCI_I05_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RCI_I05_RESULTS:

RCI_I05_RESULTS HL7 v2 RCI_I05.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RCI_I05_RESULTS.RCI_I05_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RCL_I06_PROVIDER:

RCL_I06_PROVIDER HL7 v2 RCL_I06.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RCL_I06_PROVIDER.RCL_I06_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RDE_O11_COMPONENT:

RDE_O11_COMPONENT HL7 v2 RDE_O11.COMPONENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDE_O11_COMPONENT.RDE_O11_COMPONENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_4-RXC>`]
     - required
     - Pharmacy/Treatment Component Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RDE_O11_INSURANCE:

RDE_O11_INSURANCE HL7 v2 RDE_O11.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDE_O11_INSURANCE.RDE_O11_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-RDE_O11_OBSERVATION:

RDE_O11_OBSERVATION HL7 v2 RDE_O11.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDE_O11_OBSERVATION.RDE_O11_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RDE_O11_ORDER:

RDE_O11_ORDER HL7 v2 RDE_O11.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDE_O11_ORDER.RDE_O11_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RDE_O11_ORDER_DETAIL <hl7-v2_4-RDE_O11_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order
   * - ``OBSERVATION``
     - Optional[List[:ref:`RDE_O11_OBSERVATION <hl7-v2_4-RDE_O11_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``CTI``
     - Optional[List[:ref:`CTI <hl7-v2_4-CTI>`]]
     - optional
     - Clinical Trial Identification

.. _hl7-v2_4-RDE_O11_ORDER_DETAIL:

RDE_O11_ORDER_DETAIL HL7 v2 RDE_O11.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDE_O11_ORDER_DETAIL.RDE_O11_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``COMPONENT``
     - Optional[:ref:`RDE_O11_COMPONENT <hl7-v2_4-RDE_O11_COMPONENT>`]
     - optional
     - COMPONENT

.. _hl7-v2_4-RDE_O11_PATIENT:

RDE_O11_PATIENT HL7 v2 RDE_O11.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDE_O11_PATIENT.RDE_O11_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RDE_O11_PATIENT_VISIT <hl7-v2_4-RDE_O11_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``INSURANCE``
     - Optional[List[:ref:`RDE_O11_INSURANCE <hl7-v2_4-RDE_O11_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``GT1``
     - Optional[:ref:`GT1 <hl7-v2_4-GT1>`]
     - optional
     - Guarantor
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information

.. _hl7-v2_4-RDE_O11_PATIENT_VISIT:

RDE_O11_PATIENT_VISIT HL7 v2 RDE_O11.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDE_O11_PATIENT_VISIT.RDE_O11_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RDR_RDR_DEFINITION:

RDR_RDR_DEFINITION HL7 v2 RDR_RDR.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDR_RDR_DEFINITION.RDR_RDR_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_4-QRF>`]
     - optional
     - Original Style Query Filter
   * - ``PATIENT``
     - Optional[:ref:`RDR_RDR_PATIENT <hl7-v2_4-RDR_RDR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDR_RDR_ORDER <hl7-v2_4-RDR_RDR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RDR_RDR_DISPENSE:

RDR_RDR_DISPENSE HL7 v2 RDR_RDR.DISPENSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDR_RDR_DISPENSE.RDR_RDR_DISPENSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXD``
     - :ref:`RXD <hl7-v2_4-RXD>`
     - required
     - Pharmacy/Treatment Dispense
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RDR_RDR_ENCODING:

RDR_RDR_ENCODING HL7 v2 RDR_RDR.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDR_RDR_ENCODING.RDR_RDR_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RDR_RDR_ORDER:

RDR_RDR_ORDER HL7 v2 RDR_RDR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDR_RDR_ORDER.RDR_RDR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ENCODING``
     - Optional[:ref:`RDR_RDR_ENCODING <hl7-v2_4-RDR_RDR_ENCODING>`]
     - optional
     - ENCODING
   * - ``DISPENSE``
     - List[:ref:`RDR_RDR_DISPENSE <hl7-v2_4-RDR_RDR_DISPENSE>`]
     - required
     - DISPENSE

.. _hl7-v2_4-RDR_RDR_PATIENT:

RDR_RDR_PATIENT HL7 v2 RDR_RDR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDR_RDR_PATIENT.RDR_RDR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RDS_O13_COMPONENT:

RDS_O13_COMPONENT HL7 v2 RDS_O13.COMPONENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_COMPONENT.RDS_O13_COMPONENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_4-RXC>`]
     - required
     - Pharmacy/Treatment Component Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RDS_O13_ENCODING:

RDS_O13_ENCODING HL7 v2 RDS_O13.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_ENCODING.RDS_O13_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RDS_O13_OBSERVATION:

RDS_O13_OBSERVATION HL7 v2 RDS_O13.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_OBSERVATION.RDS_O13_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RDS_O13_ORDER:

RDS_O13_ORDER HL7 v2 RDS_O13.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_ORDER.RDS_O13_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RDS_O13_ORDER_DETAIL <hl7-v2_4-RDS_O13_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODING``
     - Optional[:ref:`RDS_O13_ENCODING <hl7-v2_4-RDS_O13_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXD``
     - :ref:`RXD <hl7-v2_4-RXD>`
     - required
     - Pharmacy/Treatment Dispense
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order
   * - ``OBSERVATION``
     - Optional[List[:ref:`RDS_O13_OBSERVATION <hl7-v2_4-RDS_O13_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``FT1``
     - Optional[List[:ref:`FT1 <hl7-v2_4-FT1>`]]
     - optional
     - Financial Transaction

.. _hl7-v2_4-RDS_O13_ORDER_DETAIL:

RDS_O13_ORDER_DETAIL HL7 v2 RDS_O13.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_ORDER_DETAIL.RDS_O13_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``ORDER_DETAIL_SUPPLEMENT``
     - Optional[:ref:`RDS_O13_ORDER_DETAIL_SUPPLEMENT <hl7-v2_4-RDS_O13_ORDER_DETAIL_SUPPLEMENT>`]
     - optional
     - ORDER_DETAIL_SUPPLEMENT

.. _hl7-v2_4-RDS_O13_ORDER_DETAIL_SUPPLEMENT:

RDS_O13_ORDER_DETAIL_SUPPLEMENT HL7 v2 RDS_O13.ORDER_DETAIL_SUPPLEMENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_ORDER_DETAIL_SUPPLEMENT.RDS_O13_ORDER_DETAIL_SUPPLEMENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NTE``
     - List[:ref:`NTE <hl7-v2_4-NTE>`]
     - required
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``COMPONENT``
     - Optional[:ref:`RDS_O13_COMPONENT <hl7-v2_4-RDS_O13_COMPONENT>`]
     - optional
     - COMPONENT

.. _hl7-v2_4-RDS_O13_PATIENT:

RDS_O13_PATIENT HL7 v2 RDS_O13.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_PATIENT.RDS_O13_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RDS_O13_PATIENT_VISIT <hl7-v2_4-RDS_O13_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT

.. _hl7-v2_4-RDS_O13_PATIENT_VISIT:

RDS_O13_PATIENT_VISIT HL7 v2 RDS_O13.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RDS_O13_PATIENT_VISIT.RDS_O13_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-REF_I12_AUTCTD_SUPPGRP2:

REF_I12_AUTCTD_SUPPGRP2 HL7 v2 REF_I12.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_AUTCTD_SUPPGRP2.REF_I12_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-REF_I12_AUTHORIZATION_CONTACT:

REF_I12_AUTHORIZATION_CONTACT HL7 v2 REF_I12.AUTHORIZATION_CONTACT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_AUTHORIZATION_CONTACT.REF_I12_AUTHORIZATION_CONTACT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-REF_I12_INSURANCE:

REF_I12_INSURANCE HL7 v2 REF_I12.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_INSURANCE.REF_I12_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-REF_I12_OBSERVATION:

REF_I12_OBSERVATION HL7 v2 REF_I12.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_OBSERVATION.REF_I12_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESULTS_NOTES``
     - Optional[List[:ref:`REF_I12_RESULTS_NOTES <hl7-v2_4-REF_I12_RESULTS_NOTES>`]]
     - optional
     - RESULTS_NOTES

.. _hl7-v2_4-REF_I12_PATIENT_VISIT:

REF_I12_PATIENT_VISIT HL7 v2 REF_I12.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_PATIENT_VISIT.REF_I12_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-REF_I12_PROCEDURE:

REF_I12_PROCEDURE HL7 v2 REF_I12.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_PROCEDURE.REF_I12_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`REF_I12_AUTCTD_SUPPGRP2 <hl7-v2_4-REF_I12_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_4-REF_I12_PROVIDER_CONTACT:

REF_I12_PROVIDER_CONTACT HL7 v2 REF_I12.PROVIDER_CONTACT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_PROVIDER_CONTACT.REF_I12_PROVIDER_CONTACT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-REF_I12_RESULTS_NOTES:

REF_I12_RESULTS_NOTES HL7 v2 REF_I12.RESULTS_NOTES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.REF_I12_RESULTS_NOTES.REF_I12_RESULTS_NOTES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RER_RER_DEFINITION:

RER_RER_DEFINITION HL7 v2 RER_RER.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RER_RER_DEFINITION.RER_RER_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_4-QRF>`]
     - optional
     - Original Style Query Filter
   * - ``PATIENT``
     - Optional[:ref:`RER_RER_PATIENT <hl7-v2_4-RER_RER_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RER_RER_ORDER <hl7-v2_4-RER_RER_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RER_RER_ORDER:

RER_RER_ORDER HL7 v2 RER_RER.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RER_RER_ORDER.RER_RER_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RER_RER_PATIENT:

RER_RER_PATIENT HL7 v2 RER_RER.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RER_RER_PATIENT.RER_RER_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RGR_RGR_DEFINTION:

RGR_RGR_DEFINTION HL7 v2 RGR_RGR.DEFINTION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGR_RGR_DEFINTION.RGR_RGR_DEFINTION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_4-QRF>`]
     - optional
     - Original Style Query Filter
   * - ``PATIENT``
     - Optional[:ref:`RGR_RGR_PATIENT <hl7-v2_4-RGR_RGR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RGR_RGR_ORDER <hl7-v2_4-RGR_RGR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RGR_RGR_ENCODING:

RGR_RGR_ENCODING HL7 v2 RGR_RGR.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGR_RGR_ENCODING.RGR_RGR_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RGR_RGR_ORDER:

RGR_RGR_ORDER HL7 v2 RGR_RGR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGR_RGR_ORDER.RGR_RGR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ENCODING``
     - Optional[:ref:`RGR_RGR_ENCODING <hl7-v2_4-RGR_RGR_ENCODING>`]
     - optional
     - ENCODING
   * - ``RXG``
     - List[:ref:`RXG <hl7-v2_4-RXG>`]
     - required
     - Pharmacy/Treatment Give
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RGR_RGR_PATIENT:

RGR_RGR_PATIENT HL7 v2 RGR_RGR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGR_RGR_PATIENT.RGR_RGR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RGV_O15_COMPONENTS:

RGV_O15_COMPONENTS HL7 v2 RGV_O15.COMPONENTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_COMPONENTS.RGV_O15_COMPONENTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_4-RXC>`]
     - required
     - Pharmacy/Treatment Component Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RGV_O15_ENCODING:

RGV_O15_ENCODING HL7 v2 RGV_O15.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_ENCODING.RGV_O15_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RGV_O15_GIVE:

RGV_O15_GIVE HL7 v2 RGV_O15.GIVE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_GIVE.RGV_O15_GIVE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXG``
     - :ref:`RXG <hl7-v2_4-RXG>`
     - required
     - Pharmacy/Treatment Give
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order
   * - ``OBSERVATION``
     - List[:ref:`RGV_O15_OBSERVATION <hl7-v2_4-RGV_O15_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_4-RGV_O15_OBSERVATION:

RGV_O15_OBSERVATION HL7 v2 RGV_O15.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_OBSERVATION.RGV_O15_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RGV_O15_ORDER:

RGV_O15_ORDER HL7 v2 RGV_O15.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_ORDER.RGV_O15_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RGV_O15_ORDER_DETAIL <hl7-v2_4-RGV_O15_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODING``
     - Optional[:ref:`RGV_O15_ENCODING <hl7-v2_4-RGV_O15_ENCODING>`]
     - optional
     - ENCODING
   * - ``GIVE``
     - List[:ref:`RGV_O15_GIVE <hl7-v2_4-RGV_O15_GIVE>`]
     - required
     - GIVE

.. _hl7-v2_4-RGV_O15_ORDER_DETAIL:

RGV_O15_ORDER_DETAIL HL7 v2 RGV_O15.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_ORDER_DETAIL.RGV_O15_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``ORDER_DETAIL_SUPPLEMENT``
     - Optional[:ref:`RGV_O15_ORDER_DETAIL_SUPPLEMENT <hl7-v2_4-RGV_O15_ORDER_DETAIL_SUPPLEMENT>`]
     - optional
     - ORDER_DETAIL_SUPPLEMENT

.. _hl7-v2_4-RGV_O15_ORDER_DETAIL_SUPPLEMENT:

RGV_O15_ORDER_DETAIL_SUPPLEMENT HL7 v2 RGV_O15.ORDER_DETAIL_SUPPLEMENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_ORDER_DETAIL_SUPPLEMENT.RGV_O15_ORDER_DETAIL_SUPPLEMENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``NTE``
     - List[:ref:`NTE <hl7-v2_4-NTE>`]
     - required
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``COMPONENTS``
     - Optional[:ref:`RGV_O15_COMPONENTS <hl7-v2_4-RGV_O15_COMPONENTS>`]
     - optional
     - COMPONENTS

.. _hl7-v2_4-RGV_O15_PATIENT:

RGV_O15_PATIENT HL7 v2 RGV_O15.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_PATIENT.RGV_O15_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RGV_O15_PATIENT_VISIT <hl7-v2_4-RGV_O15_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT

.. _hl7-v2_4-RGV_O15_PATIENT_VISIT:

RGV_O15_PATIENT_VISIT HL7 v2 RGV_O15.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RGV_O15_PATIENT_VISIT.RGV_O15_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-ROR_ROR_DEFINITION:

ROR_ROR_DEFINITION HL7 v2 ROR_ROR.DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ROR_ROR_DEFINITION.ROR_ROR_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``QRD``
     - :ref:`QRD <hl7-v2_4-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_4-QRF>`]
     - optional
     - Original Style Query Filter
   * - ``PATIENT``
     - Optional[:ref:`ROR_ROR_PATIENT <hl7-v2_4-ROR_ROR_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ROR_ROR_ORDER <hl7-v2_4-ROR_ROR_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-ROR_ROR_ORDER:

ROR_ROR_ORDER HL7 v2 ROR_ROR.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ROR_ROR_ORDER.ROR_ROR_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-ROR_ROR_PATIENT:

ROR_ROR_PATIENT HL7 v2 ROR_ROR.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.ROR_ROR_PATIENT.ROR_ROR_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RPA_I08_AUTCTD_SUPPGRP2:

RPA_I08_AUTCTD_SUPPGRP2 HL7 v2 RPA_I08.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_AUTCTD_SUPPGRP2.RPA_I08_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-RPA_I08_AUTHORIZATION:

RPA_I08_AUTHORIZATION HL7 v2 RPA_I08.AUTHORIZATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_AUTHORIZATION.RPA_I08_AUTHORIZATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-RPA_I08_INSURANCE:

RPA_I08_INSURANCE HL7 v2 RPA_I08.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_INSURANCE.RPA_I08_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-RPA_I08_OBSERVATION:

RPA_I08_OBSERVATION HL7 v2 RPA_I08.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_OBSERVATION.RPA_I08_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESULTS``
     - Optional[List[:ref:`RPA_I08_RESULTS <hl7-v2_4-RPA_I08_RESULTS>`]]
     - optional
     - RESULTS

.. _hl7-v2_4-RPA_I08_PROCEDURE:

RPA_I08_PROCEDURE HL7 v2 RPA_I08.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_PROCEDURE.RPA_I08_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`RPA_I08_AUTCTD_SUPPGRP2 <hl7-v2_4-RPA_I08_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_4-RPA_I08_PROVIDER:

RPA_I08_PROVIDER HL7 v2 RPA_I08.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_PROVIDER.RPA_I08_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RPA_I08_RESULTS:

RPA_I08_RESULTS HL7 v2 RPA_I08.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_RESULTS.RPA_I08_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RPA_I08_VISIT:

RPA_I08_VISIT HL7 v2 RPA_I08.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPA_I08_VISIT.RPA_I08_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RPI_I01_GUARANTOR_INSURANCE:

RPI_I01_GUARANTOR_INSURANCE HL7 v2 RPI_I01.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPI_I01_GUARANTOR_INSURANCE.RPI_I01_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`RPI_I01_INSURANCE <hl7-v2_4-RPI_I01_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_4-RPI_I01_INSURANCE:

RPI_I01_INSURANCE HL7 v2 RPI_I01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPI_I01_INSURANCE.RPI_I01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-RPI_I01_PROVIDER:

RPI_I01_PROVIDER HL7 v2 RPI_I01.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPI_I01_PROVIDER.RPI_I01_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RPI_I04_GUARANTOR_INSURANCE:

RPI_I04_GUARANTOR_INSURANCE HL7 v2 RPI_I04.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPI_I04_GUARANTOR_INSURANCE.RPI_I04_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`RPI_I04_INSURANCE <hl7-v2_4-RPI_I04_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_4-RPI_I04_INSURANCE:

RPI_I04_INSURANCE HL7 v2 RPI_I04.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPI_I04_INSURANCE.RPI_I04_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-RPI_I04_PROVIDER:

RPI_I04_PROVIDER HL7 v2 RPI_I04.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPI_I04_PROVIDER.RPI_I04_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RPL_I02_PROVIDER:

RPL_I02_PROVIDER HL7 v2 RPL_I02.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPL_I02_PROVIDER.RPL_I02_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RPR_I03_PROVIDER:

RPR_I03_PROVIDER HL7 v2 RPR_I03.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RPR_I03_PROVIDER.RPR_I03_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RQA_I08_AUTCTD_SUPPGRP2:

RQA_I08_AUTCTD_SUPPGRP2 HL7 v2 RQA_I08.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_AUTCTD_SUPPGRP2.RQA_I08_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-RQA_I08_AUTHORIZATION:

RQA_I08_AUTHORIZATION HL7 v2 RQA_I08.AUTHORIZATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_AUTHORIZATION.RQA_I08_AUTHORIZATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-RQA_I08_GUARANTOR_INSURANCE:

RQA_I08_GUARANTOR_INSURANCE HL7 v2 RQA_I08.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_GUARANTOR_INSURANCE.RQA_I08_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`RQA_I08_INSURANCE <hl7-v2_4-RQA_I08_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_4-RQA_I08_INSURANCE:

RQA_I08_INSURANCE HL7 v2 RQA_I08.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_INSURANCE.RQA_I08_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-RQA_I08_OBSERVATION:

RQA_I08_OBSERVATION HL7 v2 RQA_I08.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_OBSERVATION.RQA_I08_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESULTS``
     - Optional[List[:ref:`RQA_I08_RESULTS <hl7-v2_4-RQA_I08_RESULTS>`]]
     - optional
     - RESULTS

.. _hl7-v2_4-RQA_I08_PROCEDURE:

RQA_I08_PROCEDURE HL7 v2 RQA_I08.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_PROCEDURE.RQA_I08_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`RQA_I08_AUTCTD_SUPPGRP2 <hl7-v2_4-RQA_I08_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_4-RQA_I08_PROVIDER:

RQA_I08_PROVIDER HL7 v2 RQA_I08.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_PROVIDER.RQA_I08_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RQA_I08_RESULTS:

RQA_I08_RESULTS HL7 v2 RQA_I08.RESULTS group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_RESULTS.RQA_I08_RESULTS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RQA_I08_VISIT:

RQA_I08_VISIT HL7 v2 RQA_I08.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQA_I08_VISIT.RQA_I08_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RQC_I05_PROVIDER:

RQC_I05_PROVIDER HL7 v2 RQC_I05.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQC_I05_PROVIDER.RQC_I05_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RQI_I01_GUARANTOR_INSURANCE:

RQI_I01_GUARANTOR_INSURANCE HL7 v2 RQI_I01.GUARANTOR_INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQI_I01_GUARANTOR_INSURANCE.RQI_I01_GUARANTOR_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_4-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - List[:ref:`RQI_I01_INSURANCE <hl7-v2_4-RQI_I01_INSURANCE>`]
     - required
     - INSURANCE

.. _hl7-v2_4-RQI_I01_INSURANCE:

RQI_I01_INSURANCE HL7 v2 RQI_I01.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQI_I01_INSURANCE.RQI_I01_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-RQI_I01_PROVIDER:

RQI_I01_PROVIDER HL7 v2 RQI_I01.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQI_I01_PROVIDER.RQI_I01_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RQP_I04_PROVIDER:

RQP_I04_PROVIDER HL7 v2 RQP_I04.PROVIDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RQP_I04_PROVIDER.RQP_I04_PROVIDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RRA_O18_ADMINISTRATION:

RRA_O18_ADMINISTRATION HL7 v2 RRA_O18.ADMINISTRATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRA_O18_ADMINISTRATION.RRA_O18_ADMINISTRATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - List[:ref:`RXA <hl7-v2_4-RXA>`]
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - :ref:`RXR <hl7-v2_4-RXR>`
     - required
     - Pharmacy/Treatment Route

.. _hl7-v2_4-RRA_O18_ORDER:

RRA_O18_ORDER HL7 v2 RRA_O18.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRA_O18_ORDER.RRA_O18_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ADMINISTRATION``
     - Optional[:ref:`RRA_O18_ADMINISTRATION <hl7-v2_4-RRA_O18_ADMINISTRATION>`]
     - optional
     - ADMINISTRATION

.. _hl7-v2_4-RRA_O18_PATIENT:

RRA_O18_PATIENT HL7 v2 RRA_O18.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRA_O18_PATIENT.RRA_O18_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RRA_O18_RESPONSE:

RRA_O18_RESPONSE HL7 v2 RRA_O18.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRA_O18_RESPONSE.RRA_O18_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RRA_O18_PATIENT <hl7-v2_4-RRA_O18_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RRA_O18_ORDER <hl7-v2_4-RRA_O18_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RRD_O14_DISPENSE:

RRD_O14_DISPENSE HL7 v2 RRD_O14.DISPENSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRD_O14_DISPENSE.RRD_O14_DISPENSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXD``
     - :ref:`RXD <hl7-v2_4-RXD>`
     - required
     - Pharmacy/Treatment Dispense
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RRD_O14_ORDER:

RRD_O14_ORDER HL7 v2 RRD_O14.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRD_O14_ORDER.RRD_O14_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``DISPENSE``
     - Optional[:ref:`RRD_O14_DISPENSE <hl7-v2_4-RRD_O14_DISPENSE>`]
     - optional
     - DISPENSE

.. _hl7-v2_4-RRD_O14_PATIENT:

RRD_O14_PATIENT HL7 v2 RRD_O14.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRD_O14_PATIENT.RRD_O14_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RRD_O14_RESPONSE:

RRD_O14_RESPONSE HL7 v2 RRD_O14.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRD_O14_RESPONSE.RRD_O14_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RRD_O14_PATIENT <hl7-v2_4-RRD_O14_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RRD_O14_ORDER <hl7-v2_4-RRD_O14_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RRE_O12_ENCODING:

RRE_O12_ENCODING HL7 v2 RRE_O12.ENCODING group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRE_O12_ENCODING.RRE_O12_ENCODING
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RRE_O12_ORDER:

RRE_O12_ORDER HL7 v2 RRE_O12.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRE_O12_ORDER.RRE_O12_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ENCODING``
     - Optional[:ref:`RRE_O12_ENCODING <hl7-v2_4-RRE_O12_ENCODING>`]
     - optional
     - ENCODING

.. _hl7-v2_4-RRE_O12_PATIENT:

RRE_O12_PATIENT HL7 v2 RRE_O12.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRE_O12_PATIENT.RRE_O12_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RRE_O12_RESPONSE:

RRE_O12_RESPONSE HL7 v2 RRE_O12.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRE_O12_RESPONSE.RRE_O12_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RRE_O12_PATIENT <hl7-v2_4-RRE_O12_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RRE_O12_ORDER <hl7-v2_4-RRE_O12_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RRG_O16_GIVE:

RRG_O16_GIVE HL7 v2 RRG_O16.GIVE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRG_O16_GIVE.RRG_O16_GIVE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXG``
     - :ref:`RXG <hl7-v2_4-RXG>`
     - required
     - Pharmacy/Treatment Give
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RRG_O16_ORDER:

RRG_O16_ORDER HL7 v2 RRG_O16.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRG_O16_ORDER.RRG_O16_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``GIVE``
     - Optional[:ref:`RRG_O16_GIVE <hl7-v2_4-RRG_O16_GIVE>`]
     - optional
     - GIVE

.. _hl7-v2_4-RRG_O16_PATIENT:

RRG_O16_PATIENT HL7 v2 RRG_O16.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRG_O16_PATIENT.RRG_O16_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RRG_O16_RESPONSE:

RRG_O16_RESPONSE HL7 v2 RRG_O16.RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRG_O16_RESPONSE.RRG_O16_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RRG_O16_PATIENT <hl7-v2_4-RRG_O16_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RRG_O16_ORDER <hl7-v2_4-RRG_O16_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_4-RRI_I12_AUTCTD_SUPPGRP2:

RRI_I12_AUTCTD_SUPPGRP2 HL7 v2 RRI_I12.AUTCTD_SUPPGRP2 group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRI_I12_AUTCTD_SUPPGRP2.RRI_I12_AUTCTD_SUPPGRP2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-RRI_I12_AUTHORIZATION_CONTACT:

RRI_I12_AUTHORIZATION_CONTACT HL7 v2 RRI_I12.AUTHORIZATION_CONTACT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRI_I12_AUTHORIZATION_CONTACT.RRI_I12_AUTHORIZATION_CONTACT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AUT``
     - :ref:`AUT <hl7-v2_4-AUT>`
     - required
     - Authorization Information
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data

.. _hl7-v2_4-RRI_I12_OBSERVATION:

RRI_I12_OBSERVATION HL7 v2 RRI_I12.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRI_I12_OBSERVATION.RRI_I12_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESULTS_NOTES``
     - Optional[List[:ref:`RRI_I12_RESULTS_NOTES <hl7-v2_4-RRI_I12_RESULTS_NOTES>`]]
     - optional
     - RESULTS_NOTES

.. _hl7-v2_4-RRI_I12_PATIENT_VISIT:

RRI_I12_PATIENT_VISIT HL7 v2 RRI_I12.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRI_I12_PATIENT_VISIT.RRI_I12_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RRI_I12_PROCEDURE:

RRI_I12_PROCEDURE HL7 v2 RRI_I12.PROCEDURE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRI_I12_PROCEDURE.RRI_I12_PROCEDURE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PR1``
     - :ref:`PR1 <hl7-v2_4-PR1>`
     - required
     - Procedures
   * - ``AUTCTD_SUPPGRP2``
     - Optional[:ref:`RRI_I12_AUTCTD_SUPPGRP2 <hl7-v2_4-RRI_I12_AUTCTD_SUPPGRP2>`]
     - optional
     - AUTCTD_SUPPGRP2

.. _hl7-v2_4-RRI_I12_PROVIDER_CONTACT:

RRI_I12_PROVIDER_CONTACT HL7 v2 RRI_I12.PROVIDER_CONTACT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRI_I12_PROVIDER_CONTACT.RRI_I12_PROVIDER_CONTACT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PRD``
     - :ref:`PRD <hl7-v2_4-PRD>`
     - required
     - Provider Data
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_4-CTD>`]]
     - optional
     - Contact Data

.. _hl7-v2_4-RRI_I12_RESULTS_NOTES:

RRI_I12_RESULTS_NOTES HL7 v2 RRI_I12.RESULTS_NOTES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RRI_I12_RESULTS_NOTES.RRI_I12_RESULTS_NOTES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RSP_K13_ROW_DEFINITION:

RSP_K13_ROW_DEFINITION HL7 v2 RSP_K13.ROW_DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_K13_ROW_DEFINITION.RSP_K13_ROW_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - required
     - Table Row Definition
   * - ``RDT``
     - Optional[List[:ref:`RDT <hl7-v2_4-RDT>`]]
     - optional
     - Table Row Data

.. _hl7-v2_4-RSP_K21_QUERY_RESPONSE:

RSP_K21_QUERY_RESPONSE HL7 v2 RSP_K21.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_K21_QUERY_RESPONSE.RSP_K21_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic

.. _hl7-v2_4-RSP_K22_QUERY_RESPONSE:

RSP_K22_QUERY_RESPONSE HL7 v2 RSP_K22.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_K22_QUERY_RESPONSE.RSP_K22_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``QRI``
     - Optional[:ref:`QRI <hl7-v2_4-QRI>`]
     - optional
     - Query Response Instance

.. _hl7-v2_4-RSP_K25_STAFF:

RSP_K25_STAFF HL7 v2 RSP_K25.STAFF group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_K25_STAFF.RSP_K25_STAFF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``STF``
     - :ref:`STF <hl7-v2_4-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[:ref:`PRA <hl7-v2_4-PRA>`]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_4-ORG>`]]
     - optional
     - Practitioner Organization Unit
   * - ``AFF``
     - Optional[List[:ref:`AFF <hl7-v2_4-AFF>`]]
     - optional
     - Professional Affiliation
   * - ``LAN``
     - Optional[List[:ref:`LAN <hl7-v2_4-LAN>`]]
     - optional
     - Language Detail
   * - ``EDU``
     - Optional[List[:ref:`EDU <hl7-v2_4-EDU>`]]
     - optional
     - Educational Detail

.. _hl7-v2_4-RSP_Z82_COMMON_ORDER:

RSP_Z82_COMMON_ORDER HL7 v2 RSP_Z82.COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_COMMON_ORDER.RSP_Z82_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RSP_Z82_ORDER_DETAIL <hl7-v2_4-RSP_Z82_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODED_ORDER``
     - Optional[:ref:`RSP_Z82_ENCODED_ORDER <hl7-v2_4-RSP_Z82_ENCODED_ORDER>`]
     - optional
     - ENCODED_ORDER
   * - ``RXD``
     - :ref:`RXD <hl7-v2_4-RXD>`
     - required
     - Pharmacy/Treatment Dispense
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order
   * - ``OBSERVATION``
     - List[:ref:`RSP_Z82_OBSERVATION <hl7-v2_4-RSP_Z82_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_4-RSP_Z82_ENCODED_ORDER:

RSP_Z82_ENCODED_ORDER HL7 v2 RSP_Z82.ENCODED_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_ENCODED_ORDER.RSP_Z82_ENCODED_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RSP_Z82_OBSERVATION:

RSP_Z82_OBSERVATION HL7 v2 RSP_Z82.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_OBSERVATION.RSP_Z82_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RSP_Z82_ORDER_DETAIL:

RSP_Z82_ORDER_DETAIL HL7 v2 RSP_Z82.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_ORDER_DETAIL.RSP_Z82_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``TREATMENT``
     - Optional[:ref:`RSP_Z82_TREATMENT <hl7-v2_4-RSP_Z82_TREATMENT>`]
     - optional
     - TREATMENT

.. _hl7-v2_4-RSP_Z82_PATIENT:

RSP_Z82_PATIENT HL7 v2 RSP_Z82.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_PATIENT.RSP_Z82_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`RSP_Z82_VISIT <hl7-v2_4-RSP_Z82_VISIT>`]
     - optional
     - VISIT
   * - ``COMMON_ORDER``
     - List[:ref:`RSP_Z82_COMMON_ORDER <hl7-v2_4-RSP_Z82_COMMON_ORDER>`]
     - required
     - COMMON_ORDER

.. _hl7-v2_4-RSP_Z82_PATIENT_VISIT:

RSP_Z82_PATIENT_VISIT HL7 v2 RSP_Z82.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_PATIENT_VISIT.RSP_Z82_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RSP_Z82_QUERY_RESPONSE:

RSP_Z82_QUERY_RESPONSE HL7 v2 RSP_Z82.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_QUERY_RESPONSE.RSP_Z82_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RSP_Z82_PATIENT <hl7-v2_4-RSP_Z82_PATIENT>`]
     - optional
     - PATIENT

.. _hl7-v2_4-RSP_Z82_TREATMENT:

RSP_Z82_TREATMENT HL7 v2 RSP_Z82.TREATMENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_TREATMENT.RSP_Z82_TREATMENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_4-RXC>`]
     - required
     - Pharmacy/Treatment Component Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RSP_Z82_VISIT:

RSP_Z82_VISIT HL7 v2 RSP_Z82.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z82_VISIT.RSP_Z82_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AL1``
     - List[:ref:`AL1 <hl7-v2_4-AL1>`]
     - required
     - Patient allergy information
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RSP_Z82_PATIENT_VISIT <hl7-v2_4-RSP_Z82_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT

.. _hl7-v2_4-RSP_Z86_ADMINISTRATION:

RSP_Z86_ADMINISTRATION HL7 v2 RSP_Z86.ADMINISTRATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_ADMINISTRATION.RSP_Z86_ADMINISTRATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXA``
     - :ref:`RXA <hl7-v2_4-RXA>`
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RSP_Z86_COMMON_ORDER:

RSP_Z86_COMMON_ORDER HL7 v2 RSP_Z86.COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_COMMON_ORDER.RSP_Z86_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RSP_Z86_ORDER_DETAIL <hl7-v2_4-RSP_Z86_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ENCODED_ORDER``
     - Optional[:ref:`RSP_Z86_ENCODED_ORDER <hl7-v2_4-RSP_Z86_ENCODED_ORDER>`]
     - optional
     - ENCODED_ORDER
   * - ``DISPENSE``
     - Optional[:ref:`RSP_Z86_DISPENSE <hl7-v2_4-RSP_Z86_DISPENSE>`]
     - optional
     - DISPENSE
   * - ``GIVE``
     - Optional[:ref:`RSP_Z86_GIVE <hl7-v2_4-RSP_Z86_GIVE>`]
     - optional
     - GIVE
   * - ``ADMINISTRATION``
     - Optional[:ref:`RSP_Z86_ADMINISTRATION <hl7-v2_4-RSP_Z86_ADMINISTRATION>`]
     - optional
     - ADMINISTRATION
   * - ``OBSERVATION``
     - List[:ref:`RSP_Z86_OBSERVATION <hl7-v2_4-RSP_Z86_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_4-RSP_Z86_DISPENSE:

RSP_Z86_DISPENSE HL7 v2 RSP_Z86.DISPENSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_DISPENSE.RSP_Z86_DISPENSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXD``
     - :ref:`RXD <hl7-v2_4-RXD>`
     - required
     - Pharmacy/Treatment Dispense
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RSP_Z86_ENCODED_ORDER:

RSP_Z86_ENCODED_ORDER HL7 v2 RSP_Z86.ENCODED_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_ENCODED_ORDER.RSP_Z86_ENCODED_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RSP_Z86_GIVE:

RSP_Z86_GIVE HL7 v2 RSP_Z86.GIVE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_GIVE.RSP_Z86_GIVE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXG``
     - :ref:`RXG <hl7-v2_4-RXG>`
     - required
     - Pharmacy/Treatment Give
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RSP_Z86_OBSERVATION:

RSP_Z86_OBSERVATION HL7 v2 RSP_Z86.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_OBSERVATION.RSP_Z86_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RSP_Z86_ORDER_DETAIL:

RSP_Z86_ORDER_DETAIL HL7 v2 RSP_Z86.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_ORDER_DETAIL.RSP_Z86_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RSP_Z86_PATIENT:

RSP_Z86_PATIENT HL7 v2 RSP_Z86.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_PATIENT.RSP_Z86_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_4-AL1>`]]
     - optional
     - Patient allergy information
   * - ``COMMON_ORDER``
     - List[:ref:`RSP_Z86_COMMON_ORDER <hl7-v2_4-RSP_Z86_COMMON_ORDER>`]
     - required
     - COMMON_ORDER

.. _hl7-v2_4-RSP_Z86_QUERY_RESPONSE:

RSP_Z86_QUERY_RESPONSE HL7 v2 RSP_Z86.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z86_QUERY_RESPONSE.RSP_Z86_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RSP_Z86_PATIENT <hl7-v2_4-RSP_Z86_PATIENT>`]
     - optional
     - PATIENT

.. _hl7-v2_4-RSP_Z88_ALLERGY:

RSP_Z88_ALLERGY HL7 v2 RSP_Z88.ALLERGY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_ALLERGY.RSP_Z88_ALLERGY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AL1``
     - List[:ref:`AL1 <hl7-v2_4-AL1>`]
     - required
     - Patient allergy information
   * - ``VISIT``
     - Optional[:ref:`RSP_Z88_VISIT <hl7-v2_4-RSP_Z88_VISIT>`]
     - optional
     - VISIT

.. _hl7-v2_4-RSP_Z88_COMMON_ORDER:

RSP_Z88_COMMON_ORDER HL7 v2 RSP_Z88.COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_COMMON_ORDER.RSP_Z88_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``ORDER_DETAIL``
     - Optional[:ref:`RSP_Z88_ORDER_DETAIL <hl7-v2_4-RSP_Z88_ORDER_DETAIL>`]
     - optional
     - ORDER_DETAIL
   * - ``ORDER_ENCODED``
     - Optional[:ref:`RSP_Z88_ORDER_ENCODED <hl7-v2_4-RSP_Z88_ORDER_ENCODED>`]
     - optional
     - ORDER_ENCODED
   * - ``RXD``
     - :ref:`RXD <hl7-v2_4-RXD>`
     - required
     - Pharmacy/Treatment Dispense
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order
   * - ``OBSERVATION``
     - List[:ref:`RSP_Z88_OBSERVATION <hl7-v2_4-RSP_Z88_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_4-RSP_Z88_COMPONENT:

RSP_Z88_COMPONENT HL7 v2 RSP_Z88.COMPONENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_COMPONENT.RSP_Z88_COMPONENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXC``
     - List[:ref:`RXC <hl7-v2_4-RXC>`]
     - required
     - Pharmacy/Treatment Component Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RSP_Z88_OBSERVATION:

RSP_Z88_OBSERVATION HL7 v2 RSP_Z88.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_OBSERVATION.RSP_Z88_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RSP_Z88_ORDER_DETAIL:

RSP_Z88_ORDER_DETAIL HL7 v2 RSP_Z88.ORDER_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_ORDER_DETAIL.RSP_Z88_ORDER_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXO``
     - :ref:`RXO <hl7-v2_4-RXO>`
     - required
     - Pharmacy/Treatment Order
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``COMPONENT``
     - Optional[:ref:`RSP_Z88_COMPONENT <hl7-v2_4-RSP_Z88_COMPONENT>`]
     - optional
     - COMPONENT

.. _hl7-v2_4-RSP_Z88_ORDER_ENCODED:

RSP_Z88_ORDER_ENCODED HL7 v2 RSP_Z88.ORDER_ENCODED group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_ORDER_ENCODED.RSP_Z88_ORDER_ENCODED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RXE``
     - :ref:`RXE <hl7-v2_4-RXE>`
     - required
     - Pharmacy/Treatment Encoded Order
   * - ``RXR``
     - List[:ref:`RXR <hl7-v2_4-RXR>`]
     - required
     - Pharmacy/Treatment Route
   * - ``RXC``
     - Optional[List[:ref:`RXC <hl7-v2_4-RXC>`]]
     - optional
     - Pharmacy/Treatment Component Order

.. _hl7-v2_4-RSP_Z88_PATIENT:

RSP_Z88_PATIENT HL7 v2 RSP_Z88.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_PATIENT.RSP_Z88_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``ALLERGY``
     - Optional[:ref:`RSP_Z88_ALLERGY <hl7-v2_4-RSP_Z88_ALLERGY>`]
     - optional
     - ALLERGY
   * - ``COMMON_ORDER``
     - List[:ref:`RSP_Z88_COMMON_ORDER <hl7-v2_4-RSP_Z88_COMMON_ORDER>`]
     - required
     - COMMON_ORDER

.. _hl7-v2_4-RSP_Z88_QUERY_RESPONSE:

RSP_Z88_QUERY_RESPONSE HL7 v2 RSP_Z88.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_QUERY_RESPONSE.RSP_Z88_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RSP_Z88_PATIENT <hl7-v2_4-RSP_Z88_PATIENT>`]
     - optional
     - PATIENT

.. _hl7-v2_4-RSP_Z88_VISIT:

RSP_Z88_VISIT HL7 v2 RSP_Z88.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z88_VISIT.RSP_Z88_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RSP_Z90_COMMON_ORDER:

RSP_Z90_COMMON_ORDER HL7 v2 RSP_Z90.COMMON_ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z90_COMMON_ORDER.RSP_Z90_COMMON_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - :ref:`ORC <hl7-v2_4-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_4-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``CTD``
     - Optional[:ref:`CTD <hl7-v2_4-CTD>`]
     - optional
     - Contact Data
   * - ``OBSERVATION``
     - List[:ref:`RSP_Z90_OBSERVATION <hl7-v2_4-RSP_Z90_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_4-RSP_Z90_OBSERVATION:

RSP_Z90_OBSERVATION HL7 v2 RSP_Z90.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z90_OBSERVATION.RSP_Z90_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-RSP_Z90_PATIENT:

RSP_Z90_PATIENT HL7 v2 RSP_Z90.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z90_PATIENT.RSP_Z90_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_4-NK1>`]]
     - optional
     - Next of kin / associated parties
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`RSP_Z90_VISIT <hl7-v2_4-RSP_Z90_VISIT>`]
     - optional
     - VISIT

.. _hl7-v2_4-RSP_Z90_QUERY_RESPONSE:

RSP_Z90_QUERY_RESPONSE HL7 v2 RSP_Z90.QUERY_RESPONSE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z90_QUERY_RESPONSE.RSP_Z90_QUERY_RESPONSE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PATIENT``
     - Optional[:ref:`RSP_Z90_PATIENT <hl7-v2_4-RSP_Z90_PATIENT>`]
     - optional
     - PATIENT
   * - ``COMMON_ORDER``
     - List[:ref:`RSP_Z90_COMMON_ORDER <hl7-v2_4-RSP_Z90_COMMON_ORDER>`]
     - required
     - COMMON_ORDER

.. _hl7-v2_4-RSP_Z90_VISIT:

RSP_Z90_VISIT HL7 v2 RSP_Z90.VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RSP_Z90_VISIT.RSP_Z90_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-RTB_K13_ROW_DEFINITION:

RTB_K13_ROW_DEFINITION HL7 v2 RTB_K13.ROW_DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RTB_K13_ROW_DEFINITION.RTB_K13_ROW_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - required
     - Table Row Definition
   * - ``RDT``
     - Optional[List[:ref:`RDT <hl7-v2_4-RDT>`]]
     - optional
     - Table Row Data

.. _hl7-v2_4-RTB_Q13_ROW_DEFINITION:

RTB_Q13_ROW_DEFINITION HL7 v2 RTB_Q13.ROW_DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RTB_Q13_ROW_DEFINITION.RTB_Q13_ROW_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - required
     - Table Row Definition
   * - ``RDT``
     - Optional[List[:ref:`RDT <hl7-v2_4-RDT>`]]
     - optional
     - Table Row Data

.. _hl7-v2_4-RTB_Z74_ROW_DEFINITION:

RTB_Z74_ROW_DEFINITION HL7 v2 RTB_Z74.ROW_DEFINITION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.RTB_Z74_ROW_DEFINITION.RTB_Z74_ROW_DEFINITION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RDF``
     - :ref:`RDF <hl7-v2_4-RDF>`
     - required
     - Table Row Definition
   * - ``RDT``
     - Optional[List[:ref:`RDT <hl7-v2_4-RDT>`]]
     - optional
     - Table Row Data

.. _hl7-v2_4-SIU_S12_GENERAL_RESOURCE:

SIU_S12_GENERAL_RESOURCE HL7 v2 SIU_S12.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SIU_S12_GENERAL_RESOURCE.SIU_S12_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_4-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SIU_S12_LOCATION_RESOURCE:

SIU_S12_LOCATION_RESOURCE HL7 v2 SIU_S12.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SIU_S12_LOCATION_RESOURCE.SIU_S12_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_4-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SIU_S12_PATIENT:

SIU_S12_PATIENT HL7 v2 SIU_S12.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SIU_S12_PATIENT.SIU_S12_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_4-PD1>`]
     - optional
     - patient additional demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_4-SIU_S12_PERSONNEL_RESOURCE:

SIU_S12_PERSONNEL_RESOURCE HL7 v2 SIU_S12.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SIU_S12_PERSONNEL_RESOURCE.SIU_S12_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_4-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SIU_S12_RESOURCES:

SIU_S12_RESOURCES HL7 v2 SIU_S12.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SIU_S12_RESOURCES.SIU_S12_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_4-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SIU_S12_SERVICE <hl7-v2_4-SIU_S12_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SIU_S12_GENERAL_RESOURCE <hl7-v2_4-SIU_S12_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SIU_S12_LOCATION_RESOURCE <hl7-v2_4-SIU_S12_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SIU_S12_PERSONNEL_RESOURCE <hl7-v2_4-SIU_S12_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE

.. _hl7-v2_4-SIU_S12_SERVICE:

SIU_S12_SERVICE HL7 v2 SIU_S12.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SIU_S12_SERVICE.SIU_S12_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_4-AIS>`
     - required
     - Appointment Information - Service
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SQM_S25_GENERAL_RESOURCE:

SQM_S25_GENERAL_RESOURCE HL7 v2 SQM_S25.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQM_S25_GENERAL_RESOURCE.SQM_S25_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_4-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_4-SQM_S25_LOCATION_RESOURCE:

SQM_S25_LOCATION_RESOURCE HL7 v2 SQM_S25.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQM_S25_LOCATION_RESOURCE.SQM_S25_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_4-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_4-SQM_S25_PERSONNEL_RESOURCE:

SQM_S25_PERSONNEL_RESOURCE HL7 v2 SQM_S25.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQM_S25_PERSONNEL_RESOURCE.SQM_S25_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_4-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_4-SQM_S25_REQUEST:

SQM_S25_REQUEST HL7 v2 SQM_S25.REQUEST group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQM_S25_REQUEST.SQM_S25_REQUEST
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_4-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences
   * - ``PID``
     - Optional[:ref:`PID <hl7-v2_4-PID>`]
     - optional
     - Patient identification
   * - ``RESOURCES``
     - List[:ref:`SQM_S25_RESOURCES <hl7-v2_4-SQM_S25_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_4-SQM_S25_RESOURCES:

SQM_S25_RESOURCES HL7 v2 SQM_S25.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQM_S25_RESOURCES.SQM_S25_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_4-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SQM_S25_SERVICE <hl7-v2_4-SQM_S25_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SQM_S25_GENERAL_RESOURCE <hl7-v2_4-SQM_S25_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SQM_S25_PERSONNEL_RESOURCE <hl7-v2_4-SQM_S25_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SQM_S25_LOCATION_RESOURCE <hl7-v2_4-SQM_S25_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE

.. _hl7-v2_4-SQM_S25_SERVICE:

SQM_S25_SERVICE HL7 v2 SQM_S25.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQM_S25_SERVICE.SQM_S25_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_4-AIS>`
     - required
     - Appointment Information - Service
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences

.. _hl7-v2_4-SQR_S25_GENERAL_RESOURCE:

SQR_S25_GENERAL_RESOURCE HL7 v2 SQR_S25.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQR_S25_GENERAL_RESOURCE.SQR_S25_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_4-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SQR_S25_LOCATION_RESOURCE:

SQR_S25_LOCATION_RESOURCE HL7 v2 SQR_S25.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQR_S25_LOCATION_RESOURCE.SQR_S25_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_4-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SQR_S25_PATIENT:

SQR_S25_PATIENT HL7 v2 SQR_S25.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQR_S25_PATIENT.SQR_S25_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_4-DG1>`]
     - optional
     - Diagnosis

.. _hl7-v2_4-SQR_S25_PERSONNEL_RESOURCE:

SQR_S25_PERSONNEL_RESOURCE HL7 v2 SQR_S25.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQR_S25_PERSONNEL_RESOURCE.SQR_S25_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_4-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SQR_S25_RESOURCES:

SQR_S25_RESOURCES HL7 v2 SQR_S25.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQR_S25_RESOURCES.SQR_S25_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_4-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SQR_S25_SERVICE <hl7-v2_4-SQR_S25_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SQR_S25_GENERAL_RESOURCE <hl7-v2_4-SQR_S25_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SQR_S25_PERSONNEL_RESOURCE <hl7-v2_4-SQR_S25_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SQR_S25_LOCATION_RESOURCE <hl7-v2_4-SQR_S25_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE

.. _hl7-v2_4-SQR_S25_SCHEDULE:

SQR_S25_SCHEDULE HL7 v2 SQR_S25.SCHEDULE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQR_S25_SCHEDULE.SQR_S25_SCHEDULE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - required
     - Scheduling Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`SQR_S25_PATIENT <hl7-v2_4-SQR_S25_PATIENT>`]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SQR_S25_RESOURCES <hl7-v2_4-SQR_S25_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_4-SQR_S25_SERVICE:

SQR_S25_SERVICE HL7 v2 SQR_S25.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SQR_S25_SERVICE.SQR_S25_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_4-AIS>`
     - required
     - Appointment Information - Service
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRM_S01_GENERAL_RESOURCE:

SRM_S01_GENERAL_RESOURCE HL7 v2 SRM_S01.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRM_S01_GENERAL_RESOURCE.SRM_S01_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_4-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRM_S01_LOCATION_RESOURCE:

SRM_S01_LOCATION_RESOURCE HL7 v2 SRM_S01.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRM_S01_LOCATION_RESOURCE.SRM_S01_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_4-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRM_S01_PATIENT:

SRM_S01_PATIENT HL7 v2 SRM_S01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRM_S01_PATIENT.SRM_S01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_4-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_4-SRM_S01_PERSONNEL_RESOURCE:

SRM_S01_PERSONNEL_RESOURCE HL7 v2 SRM_S01.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRM_S01_PERSONNEL_RESOURCE.SRM_S01_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_4-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRM_S01_RESOURCES:

SRM_S01_RESOURCES HL7 v2 SRM_S01.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRM_S01_RESOURCES.SRM_S01_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_4-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SRM_S01_SERVICE <hl7-v2_4-SRM_S01_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SRM_S01_GENERAL_RESOURCE <hl7-v2_4-SRM_S01_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SRM_S01_LOCATION_RESOURCE <hl7-v2_4-SRM_S01_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SRM_S01_PERSONNEL_RESOURCE <hl7-v2_4-SRM_S01_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE

.. _hl7-v2_4-SRM_S01_SERVICE:

SRM_S01_SERVICE HL7 v2 SRM_S01.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRM_S01_SERVICE.SRM_S01_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_4-AIS>`
     - required
     - Appointment Information - Service
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_4-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRR_S01_GENERAL_RESOURCE:

SRR_S01_GENERAL_RESOURCE HL7 v2 SRR_S01.GENERAL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRR_S01_GENERAL_RESOURCE.SRR_S01_GENERAL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIG``
     - :ref:`AIG <hl7-v2_4-AIG>`
     - required
     - Appointment Information - General Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRR_S01_LOCATION_RESOURCE:

SRR_S01_LOCATION_RESOURCE HL7 v2 SRR_S01.LOCATION_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRR_S01_LOCATION_RESOURCE.SRR_S01_LOCATION_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIL``
     - :ref:`AIL <hl7-v2_4-AIL>`
     - required
     - Appointment Information - Location Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRR_S01_PATIENT:

SRR_S01_PATIENT HL7 v2 SRR_S01.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRR_S01_PATIENT.SRR_S01_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_4-PV1>`]
     - optional
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_4-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_4-SRR_S01_PERSONNEL_RESOURCE:

SRR_S01_PERSONNEL_RESOURCE HL7 v2 SRR_S01.PERSONNEL_RESOURCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRR_S01_PERSONNEL_RESOURCE.SRR_S01_PERSONNEL_RESOURCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIP``
     - :ref:`AIP <hl7-v2_4-AIP>`
     - required
     - Appointment Information - Personnel Resource
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SRR_S01_RESOURCES:

SRR_S01_RESOURCES HL7 v2 SRR_S01.RESOURCES group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRR_S01_RESOURCES.SRR_S01_RESOURCES
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``RGS``
     - :ref:`RGS <hl7-v2_4-RGS>`
     - required
     - Resource Group
   * - ``SERVICE``
     - Optional[List[:ref:`SRR_S01_SERVICE <hl7-v2_4-SRR_S01_SERVICE>`]]
     - optional
     - SERVICE
   * - ``GENERAL_RESOURCE``
     - Optional[List[:ref:`SRR_S01_GENERAL_RESOURCE <hl7-v2_4-SRR_S01_GENERAL_RESOURCE>`]]
     - optional
     - GENERAL_RESOURCE
   * - ``LOCATION_RESOURCE``
     - Optional[List[:ref:`SRR_S01_LOCATION_RESOURCE <hl7-v2_4-SRR_S01_LOCATION_RESOURCE>`]]
     - optional
     - LOCATION_RESOURCE
   * - ``PERSONNEL_RESOURCE``
     - Optional[List[:ref:`SRR_S01_PERSONNEL_RESOURCE <hl7-v2_4-SRR_S01_PERSONNEL_RESOURCE>`]]
     - optional
     - PERSONNEL_RESOURCE

.. _hl7-v2_4-SRR_S01_SCHEDULE:

SRR_S01_SCHEDULE HL7 v2 SRR_S01.SCHEDULE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRR_S01_SCHEDULE.SRR_S01_SCHEDULE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SCH``
     - :ref:`SCH <hl7-v2_4-SCH>`
     - required
     - Scheduling Activity Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRR_S01_PATIENT <hl7-v2_4-SRR_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRR_S01_RESOURCES <hl7-v2_4-SRR_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_4-SRR_S01_SERVICE:

SRR_S01_SERVICE HL7 v2 SRR_S01.SERVICE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SRR_S01_SERVICE.SRR_S01_SERVICE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``AIS``
     - :ref:`AIS <hl7-v2_4-AIS>`
     - required
     - Appointment Information - Service
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-SSU_U03_SPECIMEN_CONTAINER:

SSU_U03_SPECIMEN_CONTAINER HL7 v2 SSU_U03.SPECIMEN_CONTAINER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SSU_U03_SPECIMEN_CONTAINER.SSU_U03_SPECIMEN_CONTAINER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``SAC``
     - :ref:`SAC <hl7-v2_4-SAC>`
     - required
     - Specimen and container detail
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_4-OBX>`]
     - optional
     - Observation/Result

.. _hl7-v2_4-SUR_P09_FACILITY:

SUR_P09_FACILITY HL7 v2 SUR_P09.FACILITY group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SUR_P09_FACILITY.SUR_P09_FACILITY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``FAC``
     - :ref:`FAC <hl7-v2_4-FAC>`
     - required
     - Facility
   * - ``PRODUCT``
     - List[:ref:`SUR_P09_PRODUCT <hl7-v2_4-SUR_P09_PRODUCT>`]
     - required
     - PRODUCT
   * - ``PSH``
     - :ref:`PSH <hl7-v2_4-PSH>`
     - required
     - Product Summary Header
   * - ``FACILITY_DETAIL``
     - List[:ref:`SUR_P09_FACILITY_DETAIL <hl7-v2_4-SUR_P09_FACILITY_DETAIL>`]
     - required
     - FACILITY_DETAIL

.. _hl7-v2_4-SUR_P09_FACILITY_DETAIL:

SUR_P09_FACILITY_DETAIL HL7 v2 SUR_P09.FACILITY_DETAIL group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SUR_P09_FACILITY_DETAIL.SUR_P09_FACILITY_DETAIL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``FAC``
     - :ref:`FAC <hl7-v2_4-FAC>`
     - required
     - Facility
   * - ``PDC``
     - :ref:`PDC <hl7-v2_4-PDC>`
     - required
     - Product Detail Country
   * - ``NTE``
     - :ref:`NTE <hl7-v2_4-NTE>`
     - required
     - Notes and Comments

.. _hl7-v2_4-SUR_P09_PRODUCT:

SUR_P09_PRODUCT HL7 v2 SUR_P09.PRODUCT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.SUR_P09_PRODUCT.SUR_P09_PRODUCT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PSH``
     - :ref:`PSH <hl7-v2_4-PSH>`
     - required
     - Product Summary Header
   * - ``PDC``
     - :ref:`PDC <hl7-v2_4-PDC>`
     - required
     - Product Detail Country

.. _hl7-v2_4-VXR_V03_INSURANCE:

VXR_V03_INSURANCE HL7 v2 VXR_V03.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXR_V03_INSURANCE.VXR_V03_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-VXR_V03_OBSERVATION:

VXR_V03_OBSERVATION HL7 v2 VXR_V03.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXR_V03_OBSERVATION.VXR_V03_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-VXR_V03_ORDER:

VXR_V03_ORDER HL7 v2 VXR_V03.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXR_V03_ORDER.VXR_V03_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``RXA``
     - :ref:`RXA <hl7-v2_4-RXA>`
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_4-RXR>`]
     - optional
     - Pharmacy/Treatment Route
   * - ``OBSERVATION``
     - Optional[List[:ref:`VXR_V03_OBSERVATION <hl7-v2_4-VXR_V03_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_4-VXR_V03_PATIENT_VISIT:

VXR_V03_PATIENT_VISIT HL7 v2 VXR_V03.PATIENT_VISIT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXR_V03_PATIENT_VISIT.VXR_V03_PATIENT_VISIT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-VXU_V04_INSURANCE:

VXU_V04_INSURANCE HL7 v2 VXU_V04.INSURANCE group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXU_V04_INSURANCE.VXU_V04_INSURANCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``IN1``
     - :ref:`IN1 <hl7-v2_4-IN1>`
     - required
     - Insurance
   * - ``IN2``
     - Optional[:ref:`IN2 <hl7-v2_4-IN2>`]
     - optional
     - Insurance Additional Information
   * - ``IN3``
     - Optional[:ref:`IN3 <hl7-v2_4-IN3>`]
     - optional
     - Insurance Additional Information, Certification

.. _hl7-v2_4-VXU_V04_OBSERVATION:

VXU_V04_OBSERVATION HL7 v2 VXU_V04.OBSERVATION group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXU_V04_OBSERVATION.VXU_V04_OBSERVATION
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``OBX``
     - :ref:`OBX <hl7-v2_4-OBX>`
     - required
     - Observation/Result
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_4-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_4-VXU_V04_ORDER:

VXU_V04_ORDER HL7 v2 VXU_V04.ORDER group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXU_V04_ORDER.VXU_V04_ORDER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_4-ORC>`]
     - optional
     - Common Order
   * - ``RXA``
     - :ref:`RXA <hl7-v2_4-RXA>`
     - required
     - Pharmacy/Treatment Administration
   * - ``RXR``
     - Optional[:ref:`RXR <hl7-v2_4-RXR>`]
     - optional
     - Pharmacy/Treatment Route
   * - ``OBSERVATION``
     - Optional[List[:ref:`VXU_V04_OBSERVATION <hl7-v2_4-VXU_V04_OBSERVATION>`]]
     - optional
     - OBSERVATION

.. _hl7-v2_4-VXU_V04_PATIENT:

VXU_V04_PATIENT HL7 v2 VXU_V04.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXU_V04_PATIENT.VXU_V04_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_4-PV1>`
     - required
     - Patient visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_4-PV2>`]
     - optional
     - Patient visit - additional information

.. _hl7-v2_4-VXX_V02_PATIENT:

VXX_V02_PATIENT HL7 v2 VXX_V02.PATIENT group.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.groups.VXX_V02_PATIENT.VXX_V02_PATIENT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``PID``
     - :ref:`PID <hl7-v2_4-PID>`
     - required
     - Patient identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_4-NK1>`]]
     - optional
     - Next of kin / associated parties
