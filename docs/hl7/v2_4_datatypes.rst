v2.4 Data Types
===============

.. _hl7-v2_4-AD:

AD Address (S2.9.1).
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.AD.AD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ad_1``
     - AD.1
     - Optional[str]
     - optional
     - street address (ST)
   * - ``ad_2``
     - AD.2
     - Optional[str]
     - optional
     - other designation
   * - ``ad_3``
     - AD.3
     - Optional[str]
     - optional
     - city
   * - ``ad_4``
     - AD.4
     - Optional[str]
     - optional
     - state or province
   * - ``ad_5``
     - AD.5
     - Optional[str]
     - optional
     - zip or postal code
   * - ``ad_6``
     - AD.6
     - Optional[str]
     - optional
     - country
   * - ``ad_7``
     - AD.7
     - Optional[str]
     - optional
     - address type
   * - ``ad_8``
     - AD.8
     - Optional[str]
     - optional
     - other geographic designation

.. _hl7-v2_4-AUI:

AUI Authorization information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.AUI.AUI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``aui_1``
     - AUI.1
     - Optional[str]
     - optional
     - authorization number
   * - ``aui_2``
     - AUI.2
     - Optional[str]
     - optional
     - date
   * - ``aui_3``
     - AUI.3
     - Optional[str]
     - optional
     - source

.. _hl7-v2_4-CCD:

CCD Charge time.
~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CCD.CCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ccd_1``
     - CCD.1
     - Optional[str]
     - optional
     - when to charge code
   * - ``ccd_2``
     - CCD.2
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - date/time

.. _hl7-v2_4-CCP:

CCP Channel calibration parameters (S7.13.1.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CCP.CCP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ccp_1``
     - CCP.1
     - Optional[str]
     - optional
     - channel calibration sensitivity correction factor
   * - ``ccp_2``
     - CCP.2
     - Optional[str]
     - optional
     - channel calibration baseline
   * - ``ccp_3``
     - CCP.3
     - Optional[str]
     - optional
     - channel calibration time skew

.. _hl7-v2_4-CD:

CD Channel definition (S2.9.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CD.CD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cd_1``
     - CD.1
     - Optional[:ref:`WVI <hl7-v2_4-WVI>`]
     - optional
     - channel identifier
   * - ``cd_2``
     - CD.2
     - Optional[:ref:`WVS <hl7-v2_4-WVS>`]
     - optional
     - waveform source
   * - ``cd_3``
     - CD.3
     - Optional[:ref:`CSU <hl7-v2_4-CSU>`]
     - optional
     - channel sensitivity/units
   * - ``cd_4``
     - CD.4
     - Optional[:ref:`CCP <hl7-v2_4-CCP>`]
     - optional
     - channel calibration parameters
   * - ``cd_5``
     - CD.5
     - Optional[str]
     - optional
     - channel sampling frequency
   * - ``cd_6``
     - CD.6
     - Optional[:ref:`NR <hl7-v2_4-NR>`]
     - optional
     - minimum/maximum data values

.. _hl7-v2_4-CE:

CE Coded element (S2.9.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CE.CE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ce_1``
     - CE.1
     - Optional[str]
     - optional
     - identifier (ST)
   * - ``ce_2``
     - CE.2
     - Optional[str]
     - optional
     - text
   * - ``ce_3``
     - CE.3
     - Optional[str]
     - optional
     - name of coding system
   * - ``ce_4``
     - CE.4
     - Optional[str]
     - optional
     - alternate identifier (ST)
   * - ``ce_5``
     - CE.5
     - Optional[str]
     - optional
     - alternate text
   * - ``ce_6``
     - CE.6
     - Optional[str]
     - optional
     - name of alternate coding system

.. _hl7-v2_4-CF:

CF Coded element with formatted values (S2.9.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CF.CF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cf_1``
     - CF.1
     - Optional[str]
     - optional
     - identifier (ID)
   * - ``cf_2``
     - CF.2
     - Optional[str]
     - optional
     - formatted text
   * - ``cf_3``
     - CF.3
     - Optional[str]
     - optional
     - name of coding system
   * - ``cf_4``
     - CF.4
     - Optional[str]
     - optional
     - alternate identifier (ID)
   * - ``cf_5``
     - CF.5
     - Optional[str]
     - optional
     - alternate formatted text
   * - ``cf_6``
     - CF.6
     - Optional[str]
     - optional
     - name of alternate coding system

.. _hl7-v2_4-CK:

CK Composite id with check digit (S2.9.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CK.CK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ck_1``
     - CK.1
     - Optional[str]
     - optional
     - ID number (NM)
   * - ``ck_2``
     - CK.2
     - Optional[str]
     - optional
     - check digit (NM)
   * - ``ck_3``
     - CK.3
     - Optional[str]
     - optional
     - code identifying the check digit scheme employed
   * - ``ck_4``
     - CK.4
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning authority

.. _hl7-v2_4-CN:

CN Composite id number and name (S2.9.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CN.CN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cn_1``
     - CN.1
     - Optional[str]
     - optional
     - ID number (ST)
   * - ``cn_2``
     - CN.2
     - Optional[:ref:`FN <hl7-v2_4-FN>`]
     - optional
     - family name
   * - ``cn_3``
     - CN.3
     - Optional[str]
     - optional
     - given name
   * - ``cn_4``
     - CN.4
     - Optional[str]
     - optional
     - second and further given names or initials thereof
   * - ``cn_5``
     - CN.5
     - Optional[str]
     - optional
     - suffix (e.g., JR or III)
   * - ``cn_6``
     - CN.6
     - Optional[str]
     - optional
     - prefix (e.g., DR)
   * - ``cn_7``
     - CN.7
     - Optional[str]
     - optional
     - degree (e.g., MD)
   * - ``cn_8``
     - CN.8
     - Optional[str]
     - optional
     - source table
   * - ``cn_9``
     - CN.9
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning authority

.. _hl7-v2_4-CNE:

CNE Coded with no exceptions (S2.9.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CNE.CNE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cne_1``
     - CNE.1
     - Optional[str]
     - optional
     - identifier (ST)
   * - ``cne_2``
     - CNE.2
     - Optional[str]
     - optional
     - text
   * - ``cne_3``
     - CNE.3
     - Optional[str]
     - optional
     - name of coding system
   * - ``cne_4``
     - CNE.4
     - Optional[str]
     - optional
     - alternate identifier (ST)
   * - ``cne_5``
     - CNE.5
     - Optional[str]
     - optional
     - alternate text
   * - ``cne_6``
     - CNE.6
     - Optional[str]
     - optional
     - name of alternate coding system
   * - ``cne_7``
     - CNE.7
     - Optional[str]
     - optional
     - coding system version ID
   * - ``cne_8``
     - CNE.8
     - Optional[str]
     - optional
     - alternate coding system version ID
   * - ``cne_9``
     - CNE.9
     - Optional[str]
     - optional
     - original text

.. _hl7-v2_4-CNN:

CNN Composite id number and name (special dt for ndl).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CNN.CNN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cnn_1``
     - CNN.1
     - Optional[str]
     - optional
     - ID number (ST)
   * - ``cnn_2``
     - CNN.2
     - Optional[str]
     - optional
     - family name
   * - ``cnn_3``
     - CNN.3
     - Optional[str]
     - optional
     - given name
   * - ``cnn_4``
     - CNN.4
     - Optional[str]
     - optional
     - second and further given names or initials thereof
   * - ``cnn_5``
     - CNN.5
     - Optional[str]
     - optional
     - suffix (e.g., JR or III)
   * - ``cnn_6``
     - CNN.6
     - Optional[str]
     - optional
     - prefix (e.g., DR)
   * - ``cnn_7``
     - CNN.7
     - Optional[str]
     - optional
     - degree (e.g., MD)
   * - ``cnn_8``
     - CNN.8
     - Optional[str]
     - optional
     - source table
   * - ``cnn_9``
     - CNN.9
     - Optional[str]
     - optional
     - assigning authority namespace ID
   * - ``cnn_10``
     - CNN.10
     - Optional[str]
     - optional
     - assigning authority universal ID
   * - ``cnn_11``
     - CNN.11
     - Optional[str]
     - optional
     - assigning authority universal ID type

.. _hl7-v2_4-CP:

CP Composite price (S2.9.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CP.CP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cp_1``
     - CP.1
     - Optional[:ref:`MO <hl7-v2_4-MO>`]
     - optional
     - price
   * - ``cp_2``
     - CP.2
     - Optional[str]
     - optional
     - price type
   * - ``cp_3``
     - CP.3
     - Optional[str]
     - optional
     - from value
   * - ``cp_4``
     - CP.4
     - Optional[str]
     - optional
     - to value
   * - ``cp_5``
     - CP.5
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - range units
   * - ``cp_6``
     - CP.6
     - Optional[str]
     - optional
     - range type

.. _hl7-v2_4-CQ:

CQ Composite quantity with units (S2.9.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CQ.CQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cq_1``
     - CQ.1
     - Optional[str]
     - optional
     - quantity
   * - ``cq_2``
     - CQ.2
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - units

.. _hl7-v2_4-CSU:

CSU Channel sensitivity/units (S7.13.1.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CSU.CSU
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``csu_1``
     - CSU.1
     - Optional[str]
     - optional
     - channel sensitivity
   * - ``csu_2``
     - CSU.2
     - Optional[str]
     - optional
     - unit of measure identifier
   * - ``csu_3``
     - CSU.3
     - Optional[str]
     - optional
     - unit of measure description
   * - ``csu_4``
     - CSU.4
     - Optional[str]
     - optional
     - unit of measure coding system
   * - ``csu_5``
     - CSU.5
     - Optional[str]
     - optional
     - alternate unit of measure identifier
   * - ``csu_6``
     - CSU.6
     - Optional[str]
     - optional
     - alternate unit of measure description
   * - ``csu_7``
     - CSU.7
     - Optional[str]
     - optional
     - alternate unit of measure coding system

.. _hl7-v2_4-CWE:

CWE Coded with exceptions (S2.9.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CWE.CWE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cwe_1``
     - CWE.1
     - Optional[str]
     - optional
     - identifier (ST)
   * - ``cwe_2``
     - CWE.2
     - Optional[str]
     - optional
     - text
   * - ``cwe_3``
     - CWE.3
     - Optional[str]
     - optional
     - name of coding system
   * - ``cwe_4``
     - CWE.4
     - Optional[str]
     - optional
     - alternate identifier (ST)
   * - ``cwe_5``
     - CWE.5
     - Optional[str]
     - optional
     - alternate text
   * - ``cwe_6``
     - CWE.6
     - Optional[str]
     - optional
     - name of alternate coding system
   * - ``cwe_7``
     - CWE.7
     - Optional[str]
     - optional
     - coding system version ID
   * - ``cwe_8``
     - CWE.8
     - Optional[str]
     - optional
     - alternate coding system version ID
   * - ``cwe_9``
     - CWE.9
     - Optional[str]
     - optional
     - original text

.. _hl7-v2_4-CX:

CX Extended composite id with check digit (S2.9.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CX.CX
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``cx_1``
     - CX.1
     - Optional[str]
     - optional
     - ID
   * - ``cx_2``
     - CX.2
     - Optional[str]
     - optional
     - check digit (ST)
   * - ``cx_3``
     - CX.3
     - Optional[str]
     - optional
     - code identifying the check digit scheme employed
   * - ``cx_4``
     - CX.4
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning authority
   * - ``cx_5``
     - CX.5
     - Optional[str]
     - optional
     - identifier type code (ID)
   * - ``cx_6``
     - CX.6
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning facility
   * - ``cx_7``
     - CX.7
     - Optional[str]
     - optional
     - effective date (DT)
   * - ``cx_8``
     - CX.8
     - Optional[str]
     - optional
     - expiration date

.. _hl7-v2_4-DDI:

DDI Daily deductible.
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DDI.DDI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ddi_1``
     - DDI.1
     - Optional[str]
     - optional
     - delay days
   * - ``ddi_2``
     - DDI.2
     - Optional[str]
     - optional
     - amount
   * - ``ddi_3``
     - DDI.3
     - Optional[str]
     - optional
     - number of days

.. _hl7-v2_4-DIN:

DIN Activation date.
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DIN.DIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``din_1``
     - DIN.1
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - date
   * - ``din_2``
     - DIN.2
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - institution name

.. _hl7-v2_4-DLD:

DLD Discharge location.
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DLD.DLD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dld_1``
     - DLD.1
     - Optional[str]
     - optional
     - discharge location
   * - ``dld_2``
     - DLD.2
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - effective date

.. _hl7-v2_4-DLN:

DLN Driver's license number (S2.9.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DLN.DLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dln_1``
     - DLN.1
     - Optional[str]
     - optional
     - Driver´s License Number
   * - ``dln_2``
     - DLN.2
     - Optional[str]
     - optional
     - Issuing State, province, country
   * - ``dln_3``
     - DLN.3
     - Optional[str]
     - optional
     - expiration date

.. _hl7-v2_4-DLT:

DLT Delta check.
~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DLT.DLT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dlt_1``
     - DLT.1
     - Optional[:ref:`NR <hl7-v2_4-NR>`]
     - optional
     - Range
   * - ``dlt_2``
     - DLT.2
     - Optional[str]
     - optional
     - numeric threshold
   * - ``dlt_3``
     - DLT.3
     - Optional[str]
     - optional
     - change computation
   * - ``dlt_4``
     - DLT.4
     - Optional[str]
     - optional
     - length of time-days

.. _hl7-v2_4-DR:

DR Date/time range (S2.9.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DR.DR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dr_1``
     - DR.1
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - range start date/time
   * - ``dr_2``
     - DR.2
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - range end date/time

.. _hl7-v2_4-DTN:

DTN Day type and number (S6.5.8.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DTN.DTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``dtn_1``
     - DTN.1
     - Optional[str]
     - optional
     - day type
   * - ``dtn_2``
     - DTN.2
     - Optional[str]
     - optional
     - number of days

.. _hl7-v2_4-ED:

ED Encapsulated data (S2.9.16).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.ED.ED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ed_1``
     - ED.1
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - source application
   * - ``ed_2``
     - ED.2
     - Optional[str]
     - optional
     - type of data
   * - ``ed_3``
     - ED.3
     - Optional[str]
     - optional
     - data
   * - ``ed_4``
     - ED.4
     - Optional[str]
     - optional
     - encoding
   * - ``ed_5``
     - ED.5
     - Optional[str]
     - optional
     - data

.. _hl7-v2_4-EI:

EI Entity identifier (S2.9.17).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.EI.EI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ei_1``
     - EI.1
     - Optional[str]
     - optional
     - entity identifier
   * - ``ei_2``
     - EI.2
     - Optional[str]
     - optional
     - namespace ID
   * - ``ei_3``
     - EI.3
     - Optional[str]
     - optional
     - universal ID
   * - ``ei_4``
     - EI.4
     - Optional[str]
     - optional
     - universal ID type

.. _hl7-v2_4-EIP:

EIP Parent order.
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.EIP.EIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``eip_1``
     - EIP.1
     - Optional[:ref:`EI <hl7-v2_4-EI>`]
     - optional
     - parent´s placer order number
   * - ``eip_2``
     - EIP.2
     - Optional[:ref:`EI <hl7-v2_4-EI>`]
     - optional
     - parent´s filler order number

.. _hl7-v2_4-ELD:

ELD Error (S2).
~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.ELD.ELD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``eld_1``
     - ELD.1
     - Optional[str]
     - optional
     - segment ID
   * - ``eld_2``
     - ELD.2
     - Optional[str]
     - optional
     - sequence
   * - ``eld_3``
     - ELD.3
     - Optional[str]
     - optional
     - field position
   * - ``eld_4``
     - ELD.4
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - code identifying error

.. _hl7-v2_4-FC:

FC Financial class (S2.9.18).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.FC.FC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``fc_1``
     - FC.1
     - Optional[str]
     - optional
     - Financial Class
   * - ``fc_2``
     - FC.2
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - Effective Date (TS)

.. _hl7-v2_4-FN:

FN Familiy name (S2.9.19).
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.FN.FN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``fn_1``
     - FN.1
     - Optional[str]
     - optional
     - surname
   * - ``fn_2``
     - FN.2
     - Optional[str]
     - optional
     - own surname prefix
   * - ``fn_3``
     - FN.3
     - Optional[str]
     - optional
     - own surname
   * - ``fn_4``
     - FN.4
     - Optional[str]
     - optional
     - surname prefix from partner/spouse
   * - ``fn_5``
     - FN.5
     - Optional[str]
     - optional
     - surname from partner/spouse

.. _hl7-v2_4-HD:

HD Hierarchic designator (S2.9.21).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.HD.HD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``hd_1``
     - HD.1
     - Optional[str]
     - optional
     - namespace ID
   * - ``hd_2``
     - HD.2
     - Optional[str]
     - optional
     - universal ID
   * - ``hd_3``
     - HD.3
     - Optional[str]
     - optional
     - universal ID type

.. _hl7-v2_4-JCC:

JCC Job code/class (S2.9.24).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.JCC.JCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``jcc_1``
     - JCC.1
     - Optional[str]
     - optional
     - job code
   * - ``jcc_2``
     - JCC.2
     - Optional[str]
     - optional
     - job class

.. _hl7-v2_4-LA1:

LA1 Location with address information (variant 1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.LA1.LA1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``la1_1``
     - LA1.1
     - Optional[str]
     - optional
     - point of care (IS)
   * - ``la1_2``
     - LA1.2
     - Optional[str]
     - optional
     - room
   * - ``la1_3``
     - LA1.3
     - Optional[str]
     - optional
     - bed
   * - ``la1_4``
     - LA1.4
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - facility (HD)
   * - ``la1_5``
     - LA1.5
     - Optional[str]
     - optional
     - location status
   * - ``la1_6``
     - LA1.6
     - Optional[str]
     - optional
     - person location type
   * - ``la1_7``
     - LA1.7
     - Optional[str]
     - optional
     - building
   * - ``la1_8``
     - LA1.8
     - Optional[str]
     - optional
     - floor
   * - ``la1_9``
     - LA1.9
     - Optional[:ref:`AD <hl7-v2_4-AD>`]
     - optional
     - address

.. _hl7-v2_4-LA2:

LA2 Location with address information (variant 2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.LA2.LA2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``la2_1``
     - LA2.1
     - Optional[str]
     - optional
     - point of care (IS)
   * - ``la2_2``
     - LA2.2
     - Optional[str]
     - optional
     - room
   * - ``la2_3``
     - LA2.3
     - Optional[str]
     - optional
     - bed
   * - ``la2_4``
     - LA2.4
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - facility (HD)
   * - ``la2_5``
     - LA2.5
     - Optional[str]
     - optional
     - location status
   * - ``la2_6``
     - LA2.6
     - Optional[str]
     - optional
     - person location type
   * - ``la2_7``
     - LA2.7
     - Optional[str]
     - optional
     - building
   * - ``la2_8``
     - LA2.8
     - Optional[str]
     - optional
     - floor
   * - ``la2_9``
     - LA2.9
     - Optional[str]
     - optional
     - street address (ST)
   * - ``la2_10``
     - LA2.10
     - Optional[str]
     - optional
     - other designation
   * - ``la2_11``
     - LA2.11
     - Optional[str]
     - optional
     - city
   * - ``la2_12``
     - LA2.12
     - Optional[str]
     - optional
     - state or province
   * - ``la2_13``
     - LA2.13
     - Optional[str]
     - optional
     - zip or postal code
   * - ``la2_14``
     - LA2.14
     - Optional[str]
     - optional
     - country
   * - ``la2_15``
     - LA2.15
     - Optional[str]
     - optional
     - address type
   * - ``la2_16``
     - LA2.16
     - Optional[str]
     - optional
     - other geographic designation

.. _hl7-v2_4-MA:

MA Multiplexed array (S2.9.25).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.MA.MA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ma_1``
     - MA.1
     - Optional[str]
     - optional
     - sample 1 from channel 1
   * - ``ma_2``
     - MA.2
     - Optional[str]
     - optional
     - sample 1 from channel 2
   * - ``ma_3``
     - MA.3
     - Optional[str]
     - optional
     - sample 1 from channel 3
   * - ``ma_4``
     - MA.4
     - Optional[str]
     - optional
     - sample 1 from channel 4
   * - ``ma_5``
     - MA.5
     - Optional[str]
     - optional
     - sample 1 from channel 5
   * - ``ma_6``
     - MA.6
     - Optional[str]
     - optional
     - sample 1 from channel 6

.. _hl7-v2_4-MO:

MO Money (S2.9.26).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.MO.MO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``mo_1``
     - MO.1
     - Optional[str]
     - optional
     - quantity
   * - ``mo_2``
     - MO.2
     - Optional[str]
     - optional
     - denomination

.. _hl7-v2_4-MOC:

MOC Charge to practise.
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.MOC.MOC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``moc_1``
     - MOC.1
     - Optional[:ref:`MO <hl7-v2_4-MO>`]
     - optional
     - dollar amount
   * - ``moc_2``
     - MOC.2
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - charge code

.. _hl7-v2_4-MOP:

MOP Money or percentage.
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.MOP.MOP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``mop_1``
     - MOP.1
     - Optional[str]
     - optional
     - money or percentage indicator
   * - ``mop_2``
     - MOP.2
     - Optional[str]
     - optional
     - money or percentage quantity

.. _hl7-v2_4-MSG:

MSG Message type (S2.24.1.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.MSG.MSG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``msg_1``
     - MSG.1
     - Optional[str]
     - optional
     - message type
   * - ``msg_2``
     - MSG.2
     - Optional[str]
     - optional
     - trigger event
   * - ``msg_3``
     - MSG.3
     - Optional[str]
     - optional
     - message structure

.. _hl7-v2_4-NA:

NA Numeric array (S2.9.27).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.NA.NA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``na_1``
     - NA.1
     - Optional[str]
     - optional
     - value1
   * - ``na_2``
     - NA.2
     - Optional[str]
     - optional
     - value2
   * - ``na_3``
     - NA.3
     - Optional[str]
     - optional
     - value3
   * - ``na_4``
     - NA.4
     - Optional[str]
     - optional
     - value4

.. _hl7-v2_4-NDL:

NDL Observing practitioner.
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.NDL.NDL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ndl_1``
     - NDL.1
     - Optional[:ref:`CNN <hl7-v2_4-CNN>`]
     - optional
     - name
   * - ``ndl_2``
     - NDL.2
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - start date/time
   * - ``ndl_3``
     - NDL.3
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - end date/time
   * - ``ndl_4``
     - NDL.4
     - Optional[str]
     - optional
     - point of care (IS)
   * - ``ndl_5``
     - NDL.5
     - Optional[str]
     - optional
     - room
   * - ``ndl_6``
     - NDL.6
     - Optional[str]
     - optional
     - bed
   * - ``ndl_7``
     - NDL.7
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - facility (HD)
   * - ``ndl_8``
     - NDL.8
     - Optional[str]
     - optional
     - location status
   * - ``ndl_9``
     - NDL.9
     - Optional[str]
     - optional
     - person location type
   * - ``ndl_10``
     - NDL.10
     - Optional[str]
     - optional
     - building
   * - ``ndl_11``
     - NDL.11
     - Optional[str]
     - optional
     - floor

.. _hl7-v2_4-NR:

NR Numeric range.
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.NR.NR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``nr_1``
     - NR.1
     - Optional[str]
     - optional
     - Low Value
   * - ``nr_2``
     - NR.2
     - Optional[str]
     - optional
     - High Value

.. _hl7-v2_4-OCD:

OCD Occurence.
~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.OCD.OCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ocd_1``
     - OCD.1
     - Optional[str]
     - optional
     - occurrence code
   * - ``ocd_2``
     - OCD.2
     - Optional[str]
     - optional
     - occurrence date

.. _hl7-v2_4-OSD:

OSD Order sequence (S4).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.OSD.OSD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``osd_1``
     - OSD.1
     - Optional[str]
     - optional
     - sequence/results flag
   * - ``osd_2``
     - OSD.2
     - Optional[str]
     - optional
     - placer order number: entity identifier
   * - ``osd_3``
     - OSD.3
     - Optional[str]
     - optional
     - placer order number: namespace ID
   * - ``osd_4``
     - OSD.4
     - Optional[str]
     - optional
     - filler order number: entity identifier
   * - ``osd_5``
     - OSD.5
     - Optional[str]
     - optional
     - filler order number: namespace ID
   * - ``osd_6``
     - OSD.6
     - Optional[str]
     - optional
     - sequence condition value
   * - ``osd_7``
     - OSD.7
     - Optional[str]
     - optional
     - maximum number of repeats
   * - ``osd_8``
     - OSD.8
     - Optional[str]
     - optional
     - placer order number: universal ID
   * - ``osd_9``
     - OSD.9
     - Optional[str]
     - optional
     - placer order number; universal ID type
   * - ``osd_10``
     - OSD.10
     - Optional[str]
     - optional
     - filler order number: universal ID
   * - ``osd_11``
     - OSD.11
     - Optional[str]
     - optional
     - filler order number: universal ID type

.. _hl7-v2_4-OSP:

OSP Occurence span (S6.5.11.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.OSP.OSP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``osp_1``
     - OSP.1
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - occurrence span code
   * - ``osp_2``
     - OSP.2
     - Optional[str]
     - optional
     - occurrence span start date
   * - ``osp_3``
     - OSP.3
     - Optional[str]
     - optional
     - occurrence span stop date

.. _hl7-v2_4-PCF:

PCF Pre-certification required (S6.4.8.20).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PCF.PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pcf_1``
     - PCF.1
     - Optional[str]
     - optional
     - pre-certification patient type
   * - ``pcf_2``
     - PCF.2
     - Optional[str]
     - optional
     - pre-certification required
   * - ``pcf_3``
     - PCF.3
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - pre-certification window

.. _hl7-v2_4-PI:

PI Person identifier (S11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PI.PI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pi_1``
     - PI.1
     - Optional[str]
     - optional
     - ID number (ST)
   * - ``pi_2``
     - PI.2
     - Optional[str]
     - optional
     - type of ID number (IS)
   * - ``pi_3``
     - PI.3
     - Optional[str]
     - optional
     - other qualifying info

.. _hl7-v2_4-PIP:

PIP Privileges (S15).
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PIP.PIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pip_1``
     - PIP.1
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - privilege
   * - ``pip_2``
     - PIP.2
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - privilege class
   * - ``pip_3``
     - PIP.3
     - Optional[str]
     - optional
     - expiration date
   * - ``pip_4``
     - PIP.4
     - Optional[str]
     - optional
     - activation date
   * - ``pip_5``
     - PIP.5
     - Optional[:ref:`EI <hl7-v2_4-EI>`]
     - optional
     - facility (EI)

.. _hl7-v2_4-PL:

PL Person location (S2.9.29).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PL.PL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pl_1``
     - PL.1
     - Optional[str]
     - optional
     - point of care
   * - ``pl_2``
     - PL.2
     - Optional[str]
     - optional
     - room
   * - ``pl_3``
     - PL.3
     - Optional[str]
     - optional
     - bed
   * - ``pl_4``
     - PL.4
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - facility (HD)
   * - ``pl_5``
     - PL.5
     - Optional[str]
     - optional
     - location status
   * - ``pl_6``
     - PL.6
     - Optional[str]
     - optional
     - person location type
   * - ``pl_7``
     - PL.7
     - Optional[str]
     - optional
     - building
   * - ``pl_8``
     - PL.8
     - Optional[str]
     - optional
     - floor
   * - ``pl_9``
     - PL.9
     - Optional[str]
     - optional
     - Location description

.. _hl7-v2_4-PLN:

PLN Practitioner id numbers (S15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PLN.PLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pln_1``
     - PLN.1
     - Optional[str]
     - optional
     - ID number (ST)
   * - ``pln_2``
     - PLN.2
     - Optional[str]
     - optional
     - type of ID number (IS)
   * - ``pln_3``
     - PLN.3
     - Optional[str]
     - optional
     - state/other qualifying info
   * - ``pln_4``
     - PLN.4
     - Optional[str]
     - optional
     - expiration date

.. _hl7-v2_4-PN:

PN Person name (S2.9.30).
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PN.PN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pn_1``
     - PN.1
     - Optional[:ref:`FN <hl7-v2_4-FN>`]
     - optional
     - family name
   * - ``pn_2``
     - PN.2
     - Optional[str]
     - optional
     - given name
   * - ``pn_3``
     - PN.3
     - Optional[str]
     - optional
     - second and further given names or initials thereof
   * - ``pn_4``
     - PN.4
     - Optional[str]
     - optional
     - suffix (e.g., JR or III)
   * - ``pn_5``
     - PN.5
     - Optional[str]
     - optional
     - prefix (e.g., DR)
   * - ``pn_6``
     - PN.6
     - Optional[str]
     - optional
     - degree (e.g., MD)

.. _hl7-v2_4-PPN:

PPN Performing person time stamp (S2.9.31).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PPN.PPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ppn_1``
     - PPN.1
     - Optional[str]
     - optional
     - ID number (ST)
   * - ``ppn_2``
     - PPN.2
     - Optional[:ref:`FN <hl7-v2_4-FN>`]
     - optional
     - family name
   * - ``ppn_3``
     - PPN.3
     - Optional[str]
     - optional
     - given name
   * - ``ppn_4``
     - PPN.4
     - Optional[str]
     - optional
     - second and further given names or initials thereof
   * - ``ppn_5``
     - PPN.5
     - Optional[str]
     - optional
     - suffix (e.g., JR or III)
   * - ``ppn_6``
     - PPN.6
     - Optional[str]
     - optional
     - prefix (e.g., DR)
   * - ``ppn_7``
     - PPN.7
     - Optional[str]
     - optional
     - degree (e.g., MD)
   * - ``ppn_8``
     - PPN.8
     - Optional[str]
     - optional
     - source table
   * - ``ppn_9``
     - PPN.9
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning authority
   * - ``ppn_10``
     - PPN.10
     - Optional[str]
     - optional
     - name type code
   * - ``ppn_11``
     - PPN.11
     - Optional[str]
     - optional
     - identifier check digit
   * - ``ppn_12``
     - PPN.12
     - Optional[str]
     - optional
     - code identifying the check digit scheme employed
   * - ``ppn_13``
     - PPN.13
     - Optional[str]
     - optional
     - identifier type code (IS)
   * - ``ppn_14``
     - PPN.14
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning facility
   * - ``ppn_15``
     - PPN.15
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - Date/Time Action Performed
   * - ``ppn_16``
     - PPN.16
     - Optional[str]
     - optional
     - Name Representation code
   * - ``ppn_17``
     - PPN.17
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - name context
   * - ``ppn_18``
     - PPN.18
     - Optional[:ref:`DR <hl7-v2_4-DR>`]
     - optional
     - name validity range
   * - ``ppn_19``
     - PPN.19
     - Optional[str]
     - optional
     - name assembly order

.. _hl7-v2_4-PRL:

PRL Parent result link.
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PRL.PRL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``prl_1``
     - PRL.1
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - OBX-3 observation identifier of parent result
   * - ``prl_2``
     - PRL.2
     - Optional[str]
     - optional
     - OBX-4 sub-ID of parent result
   * - ``prl_3``
     - PRL.3
     - Optional[str]
     - optional
     - part of OBX-5 observation result from parent

.. _hl7-v2_4-PT:

PT Processing type (S2.9.32).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PT.PT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pt_1``
     - PT.1
     - Optional[str]
     - optional
     - processing ID
   * - ``pt_2``
     - PT.2
     - Optional[str]
     - optional
     - processing mode

.. _hl7-v2_4-PTA:

PTA Policy type (S6.4.7.29).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PTA.PTA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``pta_1``
     - PTA.1
     - Optional[str]
     - optional
     - policy type
   * - ``pta_2``
     - PTA.2
     - Optional[str]
     - optional
     - amount class
   * - ``pta_3``
     - PTA.3
     - Optional[str]
     - optional
     - amount

.. _hl7-v2_4-QIP:

QIP Query input parameter list (S2.9.33).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.QIP.QIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``qip_1``
     - QIP.1
     - Optional[str]
     - optional
     - segment field name
   * - ``qip_2``
     - QIP.2
     - Optional[str]
     - optional
     - value1&value2&value3

.. _hl7-v2_4-QSC:

QSC Query selection criteria (S2.9.34).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.QSC.QSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``qsc_1``
     - QSC.1
     - Optional[str]
     - optional
     - segment field name
   * - ``qsc_2``
     - QSC.2
     - Optional[str]
     - optional
     - relational operator
   * - ``qsc_3``
     - QSC.3
     - Optional[str]
     - optional
     - Value
   * - ``qsc_4``
     - QSC.4
     - Optional[str]
     - optional
     - relational conjunction

.. _hl7-v2_4-RCD:

RCD Row column definition (S2.9.35).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.RCD.RCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rcd_1``
     - RCD.1
     - Optional[str]
     - optional
     - segment field name
   * - ``rcd_2``
     - RCD.2
     - Optional[str]
     - optional
     - HL7 date type
   * - ``rcd_3``
     - RCD.3
     - Optional[str]
     - optional
     - maximum column width

.. _hl7-v2_4-RFR:

RFR Reference range.
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.RFR.RFR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rfr_1``
     - RFR.1
     - Optional[:ref:`NR <hl7-v2_4-NR>`]
     - optional
     - numeric range
   * - ``rfr_2``
     - RFR.2
     - Optional[str]
     - optional
     - administrative sex
   * - ``rfr_3``
     - RFR.3
     - Optional[:ref:`NR <hl7-v2_4-NR>`]
     - optional
     - age range
   * - ``rfr_4``
     - RFR.4
     - Optional[:ref:`NR <hl7-v2_4-NR>`]
     - optional
     - gestational range
   * - ``rfr_5``
     - RFR.5
     - Optional[str]
     - optional
     - species
   * - ``rfr_6``
     - RFR.6
     - Optional[str]
     - optional
     - race/subspecies
   * - ``rfr_7``
     - RFR.7
     - Optional[str]
     - optional
     - conditions

.. _hl7-v2_4-RI:

RI Repeat interval (S2.9.36).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.RI.RI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ri_1``
     - RI.1
     - Optional[str]
     - optional
     - repeat pattern
   * - ``ri_2``
     - RI.2
     - Optional[str]
     - optional
     - explicit time interval

.. _hl7-v2_4-RMC:

RMC Room coverage (S6.4.7.28).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.RMC.RMC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rmc_1``
     - RMC.1
     - Optional[str]
     - optional
     - room type
   * - ``rmc_2``
     - RMC.2
     - Optional[str]
     - optional
     - amount type
   * - ``rmc_3``
     - RMC.3
     - Optional[str]
     - optional
     - coverage amount

.. _hl7-v2_4-RP:

RP Reference pointer (S2.9.37).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.RP.RP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``rp_1``
     - RP.1
     - Optional[str]
     - optional
     - pointer
   * - ``rp_2``
     - RP.2
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - application ID
   * - ``rp_3``
     - RP.3
     - Optional[str]
     - optional
     - type of data
   * - ``rp_4``
     - RP.4
     - Optional[str]
     - optional
     - subtype

.. _hl7-v2_4-SAD:

SAD Street address (S2.9.38).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SAD.SAD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sad_1``
     - SAD.1
     - Optional[str]
     - optional
     - street or mailing address
   * - ``sad_2``
     - SAD.2
     - Optional[str]
     - optional
     - street name
   * - ``sad_3``
     - SAD.3
     - Optional[str]
     - optional
     - dwelling number

.. _hl7-v2_4-SCV:

SCV Scheduling class value pair (S2.9.39).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SCV.SCV
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``scv_1``
     - SCV.1
     - Optional[str]
     - optional
     - parameter class
   * - ``scv_2``
     - SCV.2
     - Optional[str]
     - optional
     - parameter value

.. _hl7-v2_4-SN:

SN Structured numeric (S2.9.41).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SN.SN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sn_1``
     - SN.1
     - Optional[str]
     - optional
     - comparator
   * - ``sn_2``
     - SN.2
     - Optional[str]
     - optional
     - num1
   * - ``sn_3``
     - SN.3
     - Optional[str]
     - optional
     - separator/suffix
   * - ``sn_4``
     - SN.4
     - Optional[str]
     - optional
     - num2

.. _hl7-v2_4-SPD:

SPD Specialty.
~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SPD.SPD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``spd_1``
     - SPD.1
     - Optional[str]
     - optional
     - specialty name
   * - ``spd_2``
     - SPD.2
     - Optional[str]
     - optional
     - governing board
   * - ``spd_3``
     - SPD.3
     - Optional[str]
     - optional
     - eligible or certified
   * - ``spd_4``
     - SPD.4
     - Optional[str]
     - optional
     - date of certification

.. _hl7-v2_4-SPS:

SPS Specimen source.
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SPS.SPS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``sps_1``
     - SPS.1
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - specimen source name or code
   * - ``sps_2``
     - SPS.2
     - Optional[str]
     - optional
     - additives
   * - ``sps_3``
     - SPS.3
     - Optional[str]
     - optional
     - freetext
   * - ``sps_4``
     - SPS.4
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - body site
   * - ``sps_5``
     - SPS.5
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - site modifier
   * - ``sps_6``
     - SPS.6
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - collection modifier method code
   * - ``sps_7``
     - SPS.7
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - specimen role

.. _hl7-v2_4-SRT:

SRT Sort order (S2.9.42).
~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SRT.SRT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``srt_1``
     - SRT.1
     - Optional[str]
     - optional
     - sort-by field
   * - ``srt_2``
     - SRT.2
     - Optional[str]
     - optional
     - sequencing

.. _hl7-v2_4-TQ:

TQ Timing quantity (S2.9.46).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.TQ.TQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``tq_1``
     - TQ.1
     - Optional[:ref:`CQ <hl7-v2_4-CQ>`]
     - optional
     - quantity
   * - ``tq_2``
     - TQ.2
     - Optional[:ref:`RI <hl7-v2_4-RI>`]
     - optional
     - interval
   * - ``tq_3``
     - TQ.3
     - Optional[str]
     - optional
     - duration
   * - ``tq_4``
     - TQ.4
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - start date/time
   * - ``tq_5``
     - TQ.5
     - Optional[:ref:`TS <hl7-v2_4-TS>`]
     - optional
     - end date/time
   * - ``tq_6``
     - TQ.6
     - Optional[str]
     - optional
     - priority
   * - ``tq_7``
     - TQ.7
     - Optional[str]
     - optional
     - condition
   * - ``tq_8``
     - TQ.8
     - Optional[str]
     - optional
     - text (TX)
   * - ``tq_9``
     - TQ.9
     - Optional[str]
     - optional
     - conjunction component
   * - ``tq_10``
     - TQ.10
     - Optional[:ref:`OSD <hl7-v2_4-OSD>`]
     - optional
     - order sequencing
   * - ``tq_11``
     - TQ.11
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - occurrence duration
   * - ``tq_12``
     - TQ.12
     - Optional[str]
     - optional
     - total occurences

.. _hl7-v2_4-TS:

TS Time stamp (S2.9.47).
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.TS.TS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``ts_1``
     - TS.1
     - Optional[str]
     - optional
     - time of an event
   * - ``ts_2``
     - TS.2
     - Optional[str]
     - optional
     - degree of precision

.. _hl7-v2_4-TX_CHALLENGE:

TX_CHALLENGE Challenge information (S8.7.3.44).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.TX_CHALLENGE.TX_CHALLENGE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``tx_challenge_1``
     - TX_CHALLENGE.1
     - Optional[str]
     - optional
     - ???????????
   * - ``tx_challenge_2``
     - TX_CHALLENGE.2
     - Optional[str]
     - optional
     - ???????????

.. _hl7-v2_4-UVC:

UVC Value code and amount.
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.UVC.UVC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``uvc_1``
     - UVC.1
     - Optional[str]
     - optional
     - value code
   * - ``uvc_2``
     - UVC.2
     - Optional[str]
     - optional
     - value amount

.. _hl7-v2_4-VH:

VH Visiting hours (S2.9.49).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.VH.VH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``vh_1``
     - VH.1
     - Optional[str]
     - optional
     - start day range
   * - ``vh_2``
     - VH.2
     - Optional[str]
     - optional
     - end day range
   * - ``vh_3``
     - VH.3
     - Optional[str]
     - optional
     - start hour range
   * - ``vh_4``
     - VH.4
     - Optional[str]
     - optional
     - end hour range

.. _hl7-v2_4-VID:

VID Version identifier (S2.9.50).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.VID.VID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``vid_1``
     - VID.1
     - Optional[str]
     - optional
     - version ID
   * - ``vid_2``
     - VID.2
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - internationalization code
   * - ``vid_3``
     - VID.3
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - international version ID

.. _hl7-v2_4-VR:

VR Value qualifier.
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.VR.VR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``vr_1``
     - VR.1
     - Optional[str]
     - optional
     - first data code value
   * - ``vr_2``
     - VR.2
     - Optional[str]
     - optional
     - Last data code calue

.. _hl7-v2_4-WVI:

WVI Channel identifier (S7.13.1.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.WVI.WVI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``wvi_1``
     - WVI.1
     - Optional[str]
     - optional
     - Channel Number
   * - ``wvi_2``
     - WVI.2
     - Optional[str]
     - optional
     - Channel Name

.. _hl7-v2_4-WVS:

WVS Waveform source (S7.13.1.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.WVS.WVS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``wvs_1``
     - WVS.1
     - Optional[str]
     - optional
     - source name 1
   * - ``wvs_2``
     - WVS.2
     - Optional[str]
     - optional
     - source name 2

.. _hl7-v2_4-XAD:

XAD Extended address (S2.9.51).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.XAD.XAD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``xad_1``
     - XAD.1
     - Optional[:ref:`SAD <hl7-v2_4-SAD>`]
     - optional
     - street address (SAD)
   * - ``xad_2``
     - XAD.2
     - Optional[str]
     - optional
     - other designation
   * - ``xad_3``
     - XAD.3
     - Optional[str]
     - optional
     - city
   * - ``xad_4``
     - XAD.4
     - Optional[str]
     - optional
     - state or province
   * - ``xad_5``
     - XAD.5
     - Optional[str]
     - optional
     - zip or postal code
   * - ``xad_6``
     - XAD.6
     - Optional[str]
     - optional
     - country
   * - ``xad_7``
     - XAD.7
     - Optional[str]
     - optional
     - address type
   * - ``xad_8``
     - XAD.8
     - Optional[str]
     - optional
     - other geographic designation
   * - ``xad_9``
     - XAD.9
     - Optional[str]
     - optional
     - county/parish code
   * - ``xad_10``
     - XAD.10
     - Optional[str]
     - optional
     - census tract
   * - ``xad_11``
     - XAD.11
     - Optional[str]
     - optional
     - address representation code
   * - ``xad_12``
     - XAD.12
     - Optional[:ref:`DR <hl7-v2_4-DR>`]
     - optional
     - address validity range

.. _hl7-v2_4-XCN:

XCN Extended composite id number and name for persons (S2.9.52).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.XCN.XCN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``xcn_1``
     - XCN.1
     - Optional[str]
     - optional
     - ID number (ST)
   * - ``xcn_2``
     - XCN.2
     - Optional[:ref:`FN <hl7-v2_4-FN>`]
     - optional
     - family name
   * - ``xcn_3``
     - XCN.3
     - Optional[str]
     - optional
     - given name
   * - ``xcn_4``
     - XCN.4
     - Optional[str]
     - optional
     - second and further given names or initials thereof
   * - ``xcn_5``
     - XCN.5
     - Optional[str]
     - optional
     - suffix (e.g., JR or III)
   * - ``xcn_6``
     - XCN.6
     - Optional[str]
     - optional
     - prefix (e.g., DR)
   * - ``xcn_7``
     - XCN.7
     - Optional[str]
     - optional
     - degree (e.g., MD)
   * - ``xcn_8``
     - XCN.8
     - Optional[str]
     - optional
     - source table
   * - ``xcn_9``
     - XCN.9
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning authority
   * - ``xcn_10``
     - XCN.10
     - Optional[str]
     - optional
     - name type code
   * - ``xcn_11``
     - XCN.11
     - Optional[str]
     - optional
     - identifier check digit
   * - ``xcn_12``
     - XCN.12
     - Optional[str]
     - optional
     - code identifying the check digit scheme employed
   * - ``xcn_13``
     - XCN.13
     - Optional[str]
     - optional
     - identifier type code (IS)
   * - ``xcn_14``
     - XCN.14
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning facility
   * - ``xcn_15``
     - XCN.15
     - Optional[str]
     - optional
     - Name Representation code
   * - ``xcn_16``
     - XCN.16
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - name context
   * - ``xcn_17``
     - XCN.17
     - Optional[:ref:`DR <hl7-v2_4-DR>`]
     - optional
     - name validity range
   * - ``xcn_18``
     - XCN.18
     - Optional[str]
     - optional
     - name assembly order

.. _hl7-v2_4-XON:

XON Extended composite name and identification number for organizations (S2.9.53).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.XON.XON
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``xon_1``
     - XON.1
     - Optional[str]
     - optional
     - organization name
   * - ``xon_2``
     - XON.2
     - Optional[str]
     - optional
     - organization name type code
   * - ``xon_3``
     - XON.3
     - Optional[str]
     - optional
     - ID number (NM)
   * - ``xon_4``
     - XON.4
     - Optional[str]
     - optional
     - check digit (NM)
   * - ``xon_5``
     - XON.5
     - Optional[str]
     - optional
     - code identifying the check digit scheme employed
   * - ``xon_6``
     - XON.6
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning authority
   * - ``xon_7``
     - XON.7
     - Optional[str]
     - optional
     - identifier type code (IS)
   * - ``xon_8``
     - XON.8
     - Optional[:ref:`HD <hl7-v2_4-HD>`]
     - optional
     - assigning facility ID
   * - ``xon_9``
     - XON.9
     - Optional[str]
     - optional
     - Name Representation code

.. _hl7-v2_4-XPN:

XPN Extended person name (S2.9.54).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.XPN.XPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``xpn_1``
     - XPN.1
     - Optional[:ref:`FN <hl7-v2_4-FN>`]
     - optional
     - family name
   * - ``xpn_2``
     - XPN.2
     - Optional[str]
     - optional
     - given name
   * - ``xpn_3``
     - XPN.3
     - Optional[str]
     - optional
     - second and further given names or initials thereof
   * - ``xpn_4``
     - XPN.4
     - Optional[str]
     - optional
     - suffix (e.g., JR or III)
   * - ``xpn_5``
     - XPN.5
     - Optional[str]
     - optional
     - prefix (e.g., DR)
   * - ``xpn_6``
     - XPN.6
     - Optional[str]
     - optional
     - degree (e.g., MD)
   * - ``xpn_7``
     - XPN.7
     - Optional[str]
     - optional
     - name type code
   * - ``xpn_8``
     - XPN.8
     - Optional[str]
     - optional
     - Name Representation code
   * - ``xpn_9``
     - XPN.9
     - Optional[:ref:`CE <hl7-v2_4-CE>`]
     - optional
     - name context
   * - ``xpn_10``
     - XPN.10
     - Optional[:ref:`DR <hl7-v2_4-DR>`]
     - optional
     - name validity range
   * - ``xpn_11``
     - XPN.11
     - Optional[str]
     - optional
     - name assembly order

.. _hl7-v2_4-XTN:

XTN Extended telecommunication number (S2.9.55).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.XTN.XTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``xtn_1``
     - XTN.1
     - Optional[str]
     - optional
     - [(999)] 999-9999 [X99999][C any text]
   * - ``xtn_2``
     - XTN.2
     - Optional[str]
     - optional
     - telecommunication use code
   * - ``xtn_3``
     - XTN.3
     - Optional[str]
     - optional
     - telecommunication equipment type (ID)
   * - ``xtn_4``
     - XTN.4
     - Optional[str]
     - optional
     - Email address
   * - ``xtn_5``
     - XTN.5
     - Optional[str]
     - optional
     - Country Code
   * - ``xtn_6``
     - XTN.6
     - Optional[str]
     - optional
     - Area/city code
   * - ``xtn_7``
     - XTN.7
     - Optional[str]
     - optional
     - Phone number
   * - ``xtn_8``
     - XTN.8
     - Optional[str]
     - optional
     - Extension
   * - ``xtn_9``
     - XTN.9
     - Optional[str]
     - optional
     - any text
