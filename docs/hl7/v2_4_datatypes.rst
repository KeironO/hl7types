v2.4 Data Types
===============

.. _hl7-v2_4-AD:

AD: Address
~~~~~~~~~~~

Section 2.9.1

.. py:class:: hl7types.hl7.v2_4.datatypes.AD.AD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ad_1``
     - AD.1
     - str
     - O
     - street address (ST)
   * - ``ad_2``
     - AD.2
     - str
     - O
     - other designation
   * - ``ad_3``
     - AD.3
     - str
     - O
     - city
   * - ``ad_4``
     - AD.4
     - str
     - O
     - state or province
   * - ``ad_5``
     - AD.5
     - str
     - O
     - zip or postal code
   * - ``ad_6``
     - AD.6
     - str
     - O
     - country
   * - ``ad_7``
     - AD.7
     - str
     - O
     - address type
   * - ``ad_8``
     - AD.8
     - str
     - O
     - other geographic designation

.. _hl7-v2_4-AUI:

AUI: Authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.AUI.AUI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``aui_1``
     - AUI.1
     - str
     - O
     - authorization number
   * - ``aui_2``
     - AUI.2
     - str
     - O
     - date
   * - ``aui_3``
     - AUI.3
     - str
     - O
     - source

.. _hl7-v2_4-CCD:

CCD: Charge time
~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CCD.CCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ccd_1``
     - CCD.1
     - str
     - O
     - when to charge code
   * - ``ccd_2``
     - CCD.2
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - date/time

.. _hl7-v2_4-CCP:

CCP: Channel calibration parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.13.1.3

.. py:class:: hl7types.hl7.v2_4.datatypes.CCP.CCP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ccp_1``
     - CCP.1
     - str
     - O
     - channel calibration sensitivity correction factor
   * - ``ccp_2``
     - CCP.2
     - str
     - O
     - channel calibration baseline
   * - ``ccp_3``
     - CCP.3
     - str
     - O
     - channel calibration time skew

.. _hl7-v2_4-CD:

CD: Channel definition
~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.2

.. py:class:: hl7types.hl7.v2_4.datatypes.CD.CD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cd_1``
     - CD.1
     - :ref:`WVI <hl7-v2_4-WVI>`
     - O
     - channel identifier
   * - ``cd_2``
     - CD.2
     - :ref:`WVS <hl7-v2_4-WVS>`
     - O
     - waveform source
   * - ``cd_3``
     - CD.3
     - :ref:`CSU <hl7-v2_4-CSU>`
     - O
     - channel sensitivity/units
   * - ``cd_4``
     - CD.4
     - :ref:`CCP <hl7-v2_4-CCP>`
     - O
     - channel calibration parameters
   * - ``cd_5``
     - CD.5
     - str
     - O
     - channel sampling frequency
   * - ``cd_6``
     - CD.6
     - :ref:`NR <hl7-v2_4-NR>`
     - O
     - minimum/maximum data values

.. _hl7-v2_4-CE:

CE: Coded element
~~~~~~~~~~~~~~~~~

Section 2.9.3

.. py:class:: hl7types.hl7.v2_4.datatypes.CE.CE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ce_1``
     - CE.1
     - str
     - O
     - identifier (ST)
   * - ``ce_2``
     - CE.2
     - str
     - O
     - text
   * - ``ce_3``
     - CE.3
     - str
     - O
     - name of coding system
   * - ``ce_4``
     - CE.4
     - str
     - O
     - alternate identifier (ST)
   * - ``ce_5``
     - CE.5
     - str
     - O
     - alternate text
   * - ``ce_6``
     - CE.6
     - str
     - O
     - name of alternate coding system

.. _hl7-v2_4-CF:

CF: Coded element with formatted values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.4

.. py:class:: hl7types.hl7.v2_4.datatypes.CF.CF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cf_1``
     - CF.1
     - str
     - O
     - identifier (ID)
   * - ``cf_2``
     - CF.2
     - str
     - O
     - formatted text
   * - ``cf_3``
     - CF.3
     - str
     - O
     - name of coding system
   * - ``cf_4``
     - CF.4
     - str
     - O
     - alternate identifier (ID)
   * - ``cf_5``
     - CF.5
     - str
     - O
     - alternate formatted text
   * - ``cf_6``
     - CF.6
     - str
     - O
     - name of alternate coding system

.. _hl7-v2_4-CK:

CK: Composite id with check digit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.5

.. py:class:: hl7types.hl7.v2_4.datatypes.CK.CK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ck_1``
     - CK.1
     - str
     - O
     - ID number (NM)
   * - ``ck_2``
     - CK.2
     - str
     - O
     - check digit (NM)
   * - ``ck_3``
     - CK.3
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``ck_4``
     - CK.4
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning authority

.. _hl7-v2_4-CN:

CN: Composite id number and name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.7

.. py:class:: hl7types.hl7.v2_4.datatypes.CN.CN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cn_1``
     - CN.1
     - str
     - O
     - ID number (ST)
   * - ``cn_2``
     - CN.2
     - :ref:`FN <hl7-v2_4-FN>`
     - O
     - family name
   * - ``cn_3``
     - CN.3
     - str
     - O
     - given name
   * - ``cn_4``
     - CN.4
     - str
     - O
     - second and further given names or initials thereof
   * - ``cn_5``
     - CN.5
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``cn_6``
     - CN.6
     - str
     - O
     - prefix (e.g., DR)
   * - ``cn_7``
     - CN.7
     - str
     - O
     - degree (e.g., MD)
   * - ``cn_8``
     - CN.8
     - str
     - O
     - source table
   * - ``cn_9``
     - CN.9
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning authority

.. _hl7-v2_4-CNE:

CNE: Coded with no exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.8

.. py:class:: hl7types.hl7.v2_4.datatypes.CNE.CNE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cne_1``
     - CNE.1
     - str
     - O
     - identifier (ST)
   * - ``cne_2``
     - CNE.2
     - str
     - O
     - text
   * - ``cne_3``
     - CNE.3
     - str
     - O
     - name of coding system
   * - ``cne_4``
     - CNE.4
     - str
     - O
     - alternate identifier (ST)
   * - ``cne_5``
     - CNE.5
     - str
     - O
     - alternate text
   * - ``cne_6``
     - CNE.6
     - str
     - O
     - name of alternate coding system
   * - ``cne_7``
     - CNE.7
     - str
     - O
     - coding system version ID
   * - ``cne_8``
     - CNE.8
     - str
     - O
     - alternate coding system version ID
   * - ``cne_9``
     - CNE.9
     - str
     - O
     - original text

.. _hl7-v2_4-CNN:

CNN: Composite id number and name (special dt for ndl)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.CNN.CNN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cnn_1``
     - CNN.1
     - str
     - O
     - ID number (ST)
   * - ``cnn_2``
     - CNN.2
     - str
     - O
     - family name
   * - ``cnn_3``
     - CNN.3
     - str
     - O
     - given name
   * - ``cnn_4``
     - CNN.4
     - str
     - O
     - second and further given names or initials thereof
   * - ``cnn_5``
     - CNN.5
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``cnn_6``
     - CNN.6
     - str
     - O
     - prefix (e.g., DR)
   * - ``cnn_7``
     - CNN.7
     - str
     - O
     - degree (e.g., MD)
   * - ``cnn_8``
     - CNN.8
     - str
     - O
     - source table
   * - ``cnn_9``
     - CNN.9
     - str
     - O
     - assigning authority namespace ID
   * - ``cnn_10``
     - CNN.10
     - str
     - O
     - assigning authority universal ID
   * - ``cnn_11``
     - CNN.11
     - str
     - O
     - assigning authority universal ID type

.. _hl7-v2_4-CP:

CP: Composite price
~~~~~~~~~~~~~~~~~~~

Section 2.9.9

.. py:class:: hl7types.hl7.v2_4.datatypes.CP.CP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cp_1``
     - CP.1
     - :ref:`MO <hl7-v2_4-MO>`
     - O
     - price
   * - ``cp_2``
     - CP.2
     - str
     - O
     - price type
   * - ``cp_3``
     - CP.3
     - str
     - O
     - from value
   * - ``cp_4``
     - CP.4
     - str
     - O
     - to value
   * - ``cp_5``
     - CP.5
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - range units
   * - ``cp_6``
     - CP.6
     - str
     - O
     - range type

.. _hl7-v2_4-CQ:

CQ: Composite quantity with units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.10

.. py:class:: hl7types.hl7.v2_4.datatypes.CQ.CQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cq_1``
     - CQ.1
     - str
     - O
     - quantity
   * - ``cq_2``
     - CQ.2
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - units

.. _hl7-v2_4-CSU:

CSU: Channel sensitivity/units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 7.13.1.3

.. py:class:: hl7types.hl7.v2_4.datatypes.CSU.CSU
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``csu_1``
     - CSU.1
     - str
     - O
     - channel sensitivity
   * - ``csu_2``
     - CSU.2
     - str
     - O
     - unit of measure identifier
   * - ``csu_3``
     - CSU.3
     - str
     - O
     - unit of measure description
   * - ``csu_4``
     - CSU.4
     - str
     - O
     - unit of measure coding system
   * - ``csu_5``
     - CSU.5
     - str
     - O
     - alternate unit of measure identifier
   * - ``csu_6``
     - CSU.6
     - str
     - O
     - alternate unit of measure description
   * - ``csu_7``
     - CSU.7
     - str
     - O
     - alternate unit of measure coding system

.. _hl7-v2_4-CWE:

CWE: Coded with exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.11

.. py:class:: hl7types.hl7.v2_4.datatypes.CWE.CWE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cwe_1``
     - CWE.1
     - str
     - O
     - identifier (ST)
   * - ``cwe_2``
     - CWE.2
     - str
     - O
     - text
   * - ``cwe_3``
     - CWE.3
     - str
     - O
     - name of coding system
   * - ``cwe_4``
     - CWE.4
     - str
     - O
     - alternate identifier (ST)
   * - ``cwe_5``
     - CWE.5
     - str
     - O
     - alternate text
   * - ``cwe_6``
     - CWE.6
     - str
     - O
     - name of alternate coding system
   * - ``cwe_7``
     - CWE.7
     - str
     - O
     - coding system version ID
   * - ``cwe_8``
     - CWE.8
     - str
     - O
     - alternate coding system version ID
   * - ``cwe_9``
     - CWE.9
     - str
     - O
     - original text

.. _hl7-v2_4-CX:

CX: Extended composite id with check digit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.12

.. py:class:: hl7types.hl7.v2_4.datatypes.CX.CX
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cx_1``
     - CX.1
     - str
     - O
     - ID
   * - ``cx_2``
     - CX.2
     - str
     - O
     - check digit (ST)
   * - ``cx_3``
     - CX.3
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``cx_4``
     - CX.4
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning authority
   * - ``cx_5``
     - CX.5
     - str
     - O
     - identifier type code (ID)
   * - ``cx_6``
     - CX.6
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning facility
   * - ``cx_7``
     - CX.7
     - str
     - O
     - effective date (DT)
   * - ``cx_8``
     - CX.8
     - str
     - O
     - expiration date

.. _hl7-v2_4-DDI:

DDI: Daily deductible
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DDI.DDI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ddi_1``
     - DDI.1
     - str
     - O
     - delay days
   * - ``ddi_2``
     - DDI.2
     - str
     - O
     - amount
   * - ``ddi_3``
     - DDI.3
     - str
     - O
     - number of days

.. _hl7-v2_4-DIN:

DIN: Activation date
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DIN.DIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``din_1``
     - DIN.1
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - date
   * - ``din_2``
     - DIN.2
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - institution name

.. _hl7-v2_4-DLD:

DLD: Discharge location
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DLD.DLD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dld_1``
     - DLD.1
     - str
     - O
     - discharge location
   * - ``dld_2``
     - DLD.2
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - effective date

.. _hl7-v2_4-DLN:

DLN: Driver's license number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.13

.. py:class:: hl7types.hl7.v2_4.datatypes.DLN.DLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dln_1``
     - DLN.1
     - str
     - O
     - Driver´s License Number
   * - ``dln_2``
     - DLN.2
     - str
     - O
     - Issuing State, province, country
   * - ``dln_3``
     - DLN.3
     - str
     - O
     - expiration date

.. _hl7-v2_4-DLT:

DLT: Delta check
~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.DLT.DLT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dlt_1``
     - DLT.1
     - :ref:`NR <hl7-v2_4-NR>`
     - O
     - Range
   * - ``dlt_2``
     - DLT.2
     - str
     - O
     - numeric threshold
   * - ``dlt_3``
     - DLT.3
     - str
     - O
     - change computation
   * - ``dlt_4``
     - DLT.4
     - str
     - O
     - length of time-days

.. _hl7-v2_4-DR:

DR: Date/time range
~~~~~~~~~~~~~~~~~~~

Section 2.9.14

.. py:class:: hl7types.hl7.v2_4.datatypes.DR.DR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dr_1``
     - DR.1
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - range start date/time
   * - ``dr_2``
     - DR.2
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - range end date/time

.. _hl7-v2_4-DTN:

DTN: Day type and number
~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.5.8.11

.. py:class:: hl7types.hl7.v2_4.datatypes.DTN.DTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dtn_1``
     - DTN.1
     - str
     - O
     - day type
   * - ``dtn_2``
     - DTN.2
     - str
     - O
     - number of days

.. _hl7-v2_4-ED:

ED: Encapsulated data
~~~~~~~~~~~~~~~~~~~~~

Section 2.9.16

.. py:class:: hl7types.hl7.v2_4.datatypes.ED.ED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ed_1``
     - ED.1
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - source application
   * - ``ed_2``
     - ED.2
     - str
     - O
     - type of data
   * - ``ed_3``
     - ED.3
     - str
     - O
     - data
   * - ``ed_4``
     - ED.4
     - str
     - O
     - encoding
   * - ``ed_5``
     - ED.5
     - str
     - O
     - data

.. _hl7-v2_4-EI:

EI: Entity identifier
~~~~~~~~~~~~~~~~~~~~~

Section 2.9.17

.. py:class:: hl7types.hl7.v2_4.datatypes.EI.EI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ei_1``
     - EI.1
     - str
     - O
     - entity identifier
   * - ``ei_2``
     - EI.2
     - str
     - O
     - namespace ID
   * - ``ei_3``
     - EI.3
     - str
     - O
     - universal ID
   * - ``ei_4``
     - EI.4
     - str
     - O
     - universal ID type

.. _hl7-v2_4-EIP:

EIP: Parent order
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.EIP.EIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``eip_1``
     - EIP.1
     - :ref:`EI <hl7-v2_4-EI>`
     - O
     - parent´s placer order number
   * - ``eip_2``
     - EIP.2
     - :ref:`EI <hl7-v2_4-EI>`
     - O
     - parent´s filler order number

.. _hl7-v2_4-ELD:

ELD: Error
~~~~~~~~~~

Section 2

.. py:class:: hl7types.hl7.v2_4.datatypes.ELD.ELD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``eld_1``
     - ELD.1
     - str
     - O
     - segment ID
   * - ``eld_2``
     - ELD.2
     - str
     - O
     - sequence
   * - ``eld_3``
     - ELD.3
     - str
     - O
     - field position
   * - ``eld_4``
     - ELD.4
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - code identifying error

.. _hl7-v2_4-FC:

FC: Financial class
~~~~~~~~~~~~~~~~~~~

Section 2.9.18

.. py:class:: hl7types.hl7.v2_4.datatypes.FC.FC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``fc_1``
     - FC.1
     - str
     - O
     - Financial Class
   * - ``fc_2``
     - FC.2
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - Effective Date (TS)

.. _hl7-v2_4-FN:

FN: Familiy name
~~~~~~~~~~~~~~~~

Section 2.9.19

.. py:class:: hl7types.hl7.v2_4.datatypes.FN.FN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``fn_1``
     - FN.1
     - str
     - O
     - surname
   * - ``fn_2``
     - FN.2
     - str
     - O
     - own surname prefix
   * - ``fn_3``
     - FN.3
     - str
     - O
     - own surname
   * - ``fn_4``
     - FN.4
     - str
     - O
     - surname prefix from partner/spouse
   * - ``fn_5``
     - FN.5
     - str
     - O
     - surname from partner/spouse

.. _hl7-v2_4-HD:

HD: Hierarchic designator
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.21

.. py:class:: hl7types.hl7.v2_4.datatypes.HD.HD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``hd_1``
     - HD.1
     - str
     - O
     - namespace ID
   * - ``hd_2``
     - HD.2
     - str
     - O
     - universal ID
   * - ``hd_3``
     - HD.3
     - str
     - O
     - universal ID type

.. _hl7-v2_4-JCC:

JCC: Job code/class
~~~~~~~~~~~~~~~~~~~

Section 2.9.24

.. py:class:: hl7types.hl7.v2_4.datatypes.JCC.JCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``jcc_1``
     - JCC.1
     - str
     - O
     - job code
   * - ``jcc_2``
     - JCC.2
     - str
     - O
     - job class

.. _hl7-v2_4-LA1:

LA1: Location with address information (variant 1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.LA1.LA1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``la1_1``
     - LA1.1
     - str
     - O
     - point of care (IS)
   * - ``la1_2``
     - LA1.2
     - str
     - O
     - room
   * - ``la1_3``
     - LA1.3
     - str
     - O
     - bed
   * - ``la1_4``
     - LA1.4
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - facility (HD)
   * - ``la1_5``
     - LA1.5
     - str
     - O
     - location status
   * - ``la1_6``
     - LA1.6
     - str
     - O
     - person location type
   * - ``la1_7``
     - LA1.7
     - str
     - O
     - building
   * - ``la1_8``
     - LA1.8
     - str
     - O
     - floor
   * - ``la1_9``
     - LA1.9
     - :ref:`AD <hl7-v2_4-AD>`
     - O
     - address

.. _hl7-v2_4-LA2:

LA2: Location with address information (variant 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.LA2.LA2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``la2_1``
     - LA2.1
     - str
     - O
     - point of care (IS)
   * - ``la2_2``
     - LA2.2
     - str
     - O
     - room
   * - ``la2_3``
     - LA2.3
     - str
     - O
     - bed
   * - ``la2_4``
     - LA2.4
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - facility (HD)
   * - ``la2_5``
     - LA2.5
     - str
     - O
     - location status
   * - ``la2_6``
     - LA2.6
     - str
     - O
     - person location type
   * - ``la2_7``
     - LA2.7
     - str
     - O
     - building
   * - ``la2_8``
     - LA2.8
     - str
     - O
     - floor
   * - ``la2_9``
     - LA2.9
     - str
     - O
     - street address (ST)
   * - ``la2_10``
     - LA2.10
     - str
     - O
     - other designation
   * - ``la2_11``
     - LA2.11
     - str
     - O
     - city
   * - ``la2_12``
     - LA2.12
     - str
     - O
     - state or province
   * - ``la2_13``
     - LA2.13
     - str
     - O
     - zip or postal code
   * - ``la2_14``
     - LA2.14
     - str
     - O
     - country
   * - ``la2_15``
     - LA2.15
     - str
     - O
     - address type
   * - ``la2_16``
     - LA2.16
     - str
     - O
     - other geographic designation

.. _hl7-v2_4-MA:

MA: Multiplexed array
~~~~~~~~~~~~~~~~~~~~~

Section 2.9.25

.. py:class:: hl7types.hl7.v2_4.datatypes.MA.MA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ma_1``
     - MA.1
     - str
     - O
     - sample 1 from channel 1
   * - ``ma_2``
     - MA.2
     - str
     - O
     - sample 1 from channel 2
   * - ``ma_3``
     - MA.3
     - str
     - O
     - sample 1 from channel 3
   * - ``ma_4``
     - MA.4
     - str
     - O
     - sample 1 from channel 4
   * - ``ma_5``
     - MA.5
     - str
     - O
     - sample 1 from channel 5
   * - ``ma_6``
     - MA.6
     - str
     - O
     - sample 1 from channel 6

.. _hl7-v2_4-MO:

MO: Money
~~~~~~~~~

Section 2.9.26

.. py:class:: hl7types.hl7.v2_4.datatypes.MO.MO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``mo_1``
     - MO.1
     - str
     - O
     - quantity
   * - ``mo_2``
     - MO.2
     - str
     - O
     - denomination

.. _hl7-v2_4-MOC:

MOC: Charge to practise
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.MOC.MOC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``moc_1``
     - MOC.1
     - :ref:`MO <hl7-v2_4-MO>`
     - O
     - dollar amount
   * - ``moc_2``
     - MOC.2
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - charge code

.. _hl7-v2_4-MOP:

MOP: Money or percentage
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.MOP.MOP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``mop_1``
     - MOP.1
     - str
     - O
     - money or percentage indicator
   * - ``mop_2``
     - MOP.2
     - str
     - O
     - money or percentage quantity

.. _hl7-v2_4-MSG:

MSG: Message type
~~~~~~~~~~~~~~~~~

Section 2.24.1.9

.. py:class:: hl7types.hl7.v2_4.datatypes.MSG.MSG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``msg_1``
     - MSG.1
     - str
     - O
     - message type
   * - ``msg_2``
     - MSG.2
     - str
     - O
     - trigger event
   * - ``msg_3``
     - MSG.3
     - str
     - O
     - message structure

.. _hl7-v2_4-NA:

NA: Numeric array
~~~~~~~~~~~~~~~~~

Section 2.9.27

.. py:class:: hl7types.hl7.v2_4.datatypes.NA.NA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``na_1``
     - NA.1
     - str
     - O
     - value1
   * - ``na_2``
     - NA.2
     - str
     - O
     - value2
   * - ``na_3``
     - NA.3
     - str
     - O
     - value3
   * - ``na_4``
     - NA.4
     - str
     - O
     - value4

.. _hl7-v2_4-NDL:

NDL: Observing practitioner
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.NDL.NDL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ndl_1``
     - NDL.1
     - :ref:`CNN <hl7-v2_4-CNN>`
     - O
     - name
   * - ``ndl_2``
     - NDL.2
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - start date/time
   * - ``ndl_3``
     - NDL.3
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - end date/time
   * - ``ndl_4``
     - NDL.4
     - str
     - O
     - point of care (IS)
   * - ``ndl_5``
     - NDL.5
     - str
     - O
     - room
   * - ``ndl_6``
     - NDL.6
     - str
     - O
     - bed
   * - ``ndl_7``
     - NDL.7
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - facility (HD)
   * - ``ndl_8``
     - NDL.8
     - str
     - O
     - location status
   * - ``ndl_9``
     - NDL.9
     - str
     - O
     - person location type
   * - ``ndl_10``
     - NDL.10
     - str
     - O
     - building
   * - ``ndl_11``
     - NDL.11
     - str
     - O
     - floor

.. _hl7-v2_4-NR:

NR: Numeric range
~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.NR.NR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``nr_1``
     - NR.1
     - str
     - O
     - Low Value
   * - ``nr_2``
     - NR.2
     - str
     - O
     - High Value

.. _hl7-v2_4-OCD:

OCD: Occurence
~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.OCD.OCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ocd_1``
     - OCD.1
     - str
     - O
     - occurrence code
   * - ``ocd_2``
     - OCD.2
     - str
     - O
     - occurrence date

.. _hl7-v2_4-OSD:

OSD: Order sequence
~~~~~~~~~~~~~~~~~~~

Section 4

.. py:class:: hl7types.hl7.v2_4.datatypes.OSD.OSD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``osd_1``
     - OSD.1
     - str
     - O
     - sequence/results flag
   * - ``osd_2``
     - OSD.2
     - str
     - O
     - placer order number: entity identifier
   * - ``osd_3``
     - OSD.3
     - str
     - O
     - placer order number: namespace ID
   * - ``osd_4``
     - OSD.4
     - str
     - O
     - filler order number: entity identifier
   * - ``osd_5``
     - OSD.5
     - str
     - O
     - filler order number: namespace ID
   * - ``osd_6``
     - OSD.6
     - str
     - O
     - sequence condition value
   * - ``osd_7``
     - OSD.7
     - str
     - O
     - maximum number of repeats
   * - ``osd_8``
     - OSD.8
     - str
     - O
     - placer order number: universal ID
   * - ``osd_9``
     - OSD.9
     - str
     - O
     - placer order number; universal ID type
   * - ``osd_10``
     - OSD.10
     - str
     - O
     - filler order number: universal ID
   * - ``osd_11``
     - OSD.11
     - str
     - O
     - filler order number: universal ID type

.. _hl7-v2_4-OSP:

OSP: Occurence span
~~~~~~~~~~~~~~~~~~~

Section 6.5.11.8

.. py:class:: hl7types.hl7.v2_4.datatypes.OSP.OSP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``osp_1``
     - OSP.1
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - occurrence span code
   * - ``osp_2``
     - OSP.2
     - str
     - O
     - occurrence span start date
   * - ``osp_3``
     - OSP.3
     - str
     - O
     - occurrence span stop date

.. _hl7-v2_4-PCF:

PCF: Pre-certification required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 6.4.8.20

.. py:class:: hl7types.hl7.v2_4.datatypes.PCF.PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pcf_1``
     - PCF.1
     - str
     - O
     - pre-certification patient type
   * - ``pcf_2``
     - PCF.2
     - str
     - O
     - pre-certification required
   * - ``pcf_3``
     - PCF.3
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - pre-certification window

.. _hl7-v2_4-PI:

PI: Person identifier
~~~~~~~~~~~~~~~~~~~~~

Section 11

.. py:class:: hl7types.hl7.v2_4.datatypes.PI.PI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pi_1``
     - PI.1
     - str
     - O
     - ID number (ST)
   * - ``pi_2``
     - PI.2
     - str
     - O
     - type of ID number (IS)
   * - ``pi_3``
     - PI.3
     - str
     - O
     - other qualifying info

.. _hl7-v2_4-PIP:

PIP: Privileges
~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.datatypes.PIP.PIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pip_1``
     - PIP.1
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - privilege
   * - ``pip_2``
     - PIP.2
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - privilege class
   * - ``pip_3``
     - PIP.3
     - str
     - O
     - expiration date
   * - ``pip_4``
     - PIP.4
     - str
     - O
     - activation date
   * - ``pip_5``
     - PIP.5
     - :ref:`EI <hl7-v2_4-EI>`
     - O
     - facility (EI)

.. _hl7-v2_4-PL:

PL: Person location
~~~~~~~~~~~~~~~~~~~

Section 2.9.29

.. py:class:: hl7types.hl7.v2_4.datatypes.PL.PL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pl_1``
     - PL.1
     - str
     - O
     - point of care
   * - ``pl_2``
     - PL.2
     - str
     - O
     - room
   * - ``pl_3``
     - PL.3
     - str
     - O
     - bed
   * - ``pl_4``
     - PL.4
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - facility (HD)
   * - ``pl_5``
     - PL.5
     - str
     - O
     - location status
   * - ``pl_6``
     - PL.6
     - str
     - O
     - person location type
   * - ``pl_7``
     - PL.7
     - str
     - O
     - building
   * - ``pl_8``
     - PL.8
     - str
     - O
     - floor
   * - ``pl_9``
     - PL.9
     - str
     - O
     - Location description

.. _hl7-v2_4-PLN:

PLN: Practitioner id numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 15

.. py:class:: hl7types.hl7.v2_4.datatypes.PLN.PLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pln_1``
     - PLN.1
     - str
     - O
     - ID number (ST)
   * - ``pln_2``
     - PLN.2
     - str
     - O
     - type of ID number (IS)
   * - ``pln_3``
     - PLN.3
     - str
     - O
     - state/other qualifying info
   * - ``pln_4``
     - PLN.4
     - str
     - O
     - expiration date

.. _hl7-v2_4-PN:

PN: Person name
~~~~~~~~~~~~~~~

Section 2.9.30

.. py:class:: hl7types.hl7.v2_4.datatypes.PN.PN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pn_1``
     - PN.1
     - :ref:`FN <hl7-v2_4-FN>`
     - O
     - family name
   * - ``pn_2``
     - PN.2
     - str
     - O
     - given name
   * - ``pn_3``
     - PN.3
     - str
     - O
     - second and further given names or initials thereof
   * - ``pn_4``
     - PN.4
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``pn_5``
     - PN.5
     - str
     - O
     - prefix (e.g., DR)
   * - ``pn_6``
     - PN.6
     - str
     - O
     - degree (e.g., MD)

.. _hl7-v2_4-PPN:

PPN: Performing person time stamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.31

.. py:class:: hl7types.hl7.v2_4.datatypes.PPN.PPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ppn_1``
     - PPN.1
     - str
     - O
     - ID number (ST)
   * - ``ppn_2``
     - PPN.2
     - :ref:`FN <hl7-v2_4-FN>`
     - O
     - family name
   * - ``ppn_3``
     - PPN.3
     - str
     - O
     - given name
   * - ``ppn_4``
     - PPN.4
     - str
     - O
     - second and further given names or initials thereof
   * - ``ppn_5``
     - PPN.5
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``ppn_6``
     - PPN.6
     - str
     - O
     - prefix (e.g., DR)
   * - ``ppn_7``
     - PPN.7
     - str
     - O
     - degree (e.g., MD)
   * - ``ppn_8``
     - PPN.8
     - str
     - O
     - source table
   * - ``ppn_9``
     - PPN.9
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning authority
   * - ``ppn_10``
     - PPN.10
     - str
     - O
     - name type code
   * - ``ppn_11``
     - PPN.11
     - str
     - O
     - identifier check digit
   * - ``ppn_12``
     - PPN.12
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``ppn_13``
     - PPN.13
     - str
     - O
     - identifier type code (IS)
   * - ``ppn_14``
     - PPN.14
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning facility
   * - ``ppn_15``
     - PPN.15
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - Date/Time Action Performed
   * - ``ppn_16``
     - PPN.16
     - str
     - O
     - Name Representation code
   * - ``ppn_17``
     - PPN.17
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - name context
   * - ``ppn_18``
     - PPN.18
     - :ref:`DR <hl7-v2_4-DR>`
     - O
     - name validity range
   * - ``ppn_19``
     - PPN.19
     - str
     - O
     - name assembly order

.. _hl7-v2_4-PRL:

PRL: Parent result link
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.PRL.PRL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``prl_1``
     - PRL.1
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - OBX-3 observation identifier of parent result
   * - ``prl_2``
     - PRL.2
     - str
     - O
     - OBX-4 sub-ID of parent result
   * - ``prl_3``
     - PRL.3
     - str
     - O
     - part of OBX-5 observation result from parent

.. _hl7-v2_4-PT:

PT: Processing type
~~~~~~~~~~~~~~~~~~~

Section 2.9.32

.. py:class:: hl7types.hl7.v2_4.datatypes.PT.PT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pt_1``
     - PT.1
     - str
     - O
     - processing ID
   * - ``pt_2``
     - PT.2
     - str
     - O
     - processing mode

.. _hl7-v2_4-PTA:

PTA: Policy type
~~~~~~~~~~~~~~~~

Section 6.4.7.29

.. py:class:: hl7types.hl7.v2_4.datatypes.PTA.PTA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pta_1``
     - PTA.1
     - str
     - O
     - policy type
   * - ``pta_2``
     - PTA.2
     - str
     - O
     - amount class
   * - ``pta_3``
     - PTA.3
     - str
     - O
     - amount

.. _hl7-v2_4-QIP:

QIP: Query input parameter list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.33

.. py:class:: hl7types.hl7.v2_4.datatypes.QIP.QIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``qip_1``
     - QIP.1
     - str
     - O
     - segment field name
   * - ``qip_2``
     - QIP.2
     - str
     - O
     - value1&value2&value3

.. _hl7-v2_4-QSC:

QSC: Query selection criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.34

.. py:class:: hl7types.hl7.v2_4.datatypes.QSC.QSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``qsc_1``
     - QSC.1
     - str
     - O
     - segment field name
   * - ``qsc_2``
     - QSC.2
     - str
     - O
     - relational operator
   * - ``qsc_3``
     - QSC.3
     - str
     - O
     - Value
   * - ``qsc_4``
     - QSC.4
     - str
     - O
     - relational conjunction

.. _hl7-v2_4-RCD:

RCD: Row column definition
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.35

.. py:class:: hl7types.hl7.v2_4.datatypes.RCD.RCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rcd_1``
     - RCD.1
     - str
     - O
     - segment field name
   * - ``rcd_2``
     - RCD.2
     - str
     - O
     - HL7 date type
   * - ``rcd_3``
     - RCD.3
     - str
     - O
     - maximum column width

.. _hl7-v2_4-RFR:

RFR: Reference range
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.RFR.RFR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rfr_1``
     - RFR.1
     - :ref:`NR <hl7-v2_4-NR>`
     - O
     - numeric range
   * - ``rfr_2``
     - RFR.2
     - str
     - O
     - administrative sex
   * - ``rfr_3``
     - RFR.3
     - :ref:`NR <hl7-v2_4-NR>`
     - O
     - age range
   * - ``rfr_4``
     - RFR.4
     - :ref:`NR <hl7-v2_4-NR>`
     - O
     - gestational range
   * - ``rfr_5``
     - RFR.5
     - str
     - O
     - species
   * - ``rfr_6``
     - RFR.6
     - str
     - O
     - race/subspecies
   * - ``rfr_7``
     - RFR.7
     - str
     - O
     - conditions

.. _hl7-v2_4-RI:

RI: Repeat interval
~~~~~~~~~~~~~~~~~~~

Section 2.9.36

.. py:class:: hl7types.hl7.v2_4.datatypes.RI.RI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ri_1``
     - RI.1
     - str
     - O
     - repeat pattern
   * - ``ri_2``
     - RI.2
     - str
     - O
     - explicit time interval

.. _hl7-v2_4-RMC:

RMC: Room coverage
~~~~~~~~~~~~~~~~~~

Section 6.4.7.28

.. py:class:: hl7types.hl7.v2_4.datatypes.RMC.RMC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rmc_1``
     - RMC.1
     - str
     - O
     - room type
   * - ``rmc_2``
     - RMC.2
     - str
     - O
     - amount type
   * - ``rmc_3``
     - RMC.3
     - str
     - O
     - coverage amount

.. _hl7-v2_4-RP:

RP: Reference pointer
~~~~~~~~~~~~~~~~~~~~~

Section 2.9.37

.. py:class:: hl7types.hl7.v2_4.datatypes.RP.RP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rp_1``
     - RP.1
     - str
     - O
     - pointer
   * - ``rp_2``
     - RP.2
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - application ID
   * - ``rp_3``
     - RP.3
     - str
     - O
     - type of data
   * - ``rp_4``
     - RP.4
     - str
     - O
     - subtype

.. _hl7-v2_4-SAD:

SAD: Street address
~~~~~~~~~~~~~~~~~~~

Section 2.9.38

.. py:class:: hl7types.hl7.v2_4.datatypes.SAD.SAD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``sad_1``
     - SAD.1
     - str
     - O
     - street or mailing address
   * - ``sad_2``
     - SAD.2
     - str
     - O
     - street name
   * - ``sad_3``
     - SAD.3
     - str
     - O
     - dwelling number

.. _hl7-v2_4-SCV:

SCV: Scheduling class value pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.39

.. py:class:: hl7types.hl7.v2_4.datatypes.SCV.SCV
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``scv_1``
     - SCV.1
     - str
     - O
     - parameter class
   * - ``scv_2``
     - SCV.2
     - str
     - O
     - parameter value

.. _hl7-v2_4-SN:

SN: Structured numeric
~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.41

.. py:class:: hl7types.hl7.v2_4.datatypes.SN.SN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``sn_1``
     - SN.1
     - str
     - O
     - comparator
   * - ``sn_2``
     - SN.2
     - str
     - O
     - num1
   * - ``sn_3``
     - SN.3
     - str
     - O
     - separator/suffix
   * - ``sn_4``
     - SN.4
     - str
     - O
     - num2

.. _hl7-v2_4-SPD:

SPD: Specialty
~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SPD.SPD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``spd_1``
     - SPD.1
     - str
     - O
     - specialty name
   * - ``spd_2``
     - SPD.2
     - str
     - O
     - governing board
   * - ``spd_3``
     - SPD.3
     - str
     - O
     - eligible or certified
   * - ``spd_4``
     - SPD.4
     - str
     - O
     - date of certification

.. _hl7-v2_4-SPS:

SPS: Specimen source
~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.SPS.SPS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``sps_1``
     - SPS.1
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - specimen source name or code
   * - ``sps_2``
     - SPS.2
     - str
     - O
     - additives
   * - ``sps_3``
     - SPS.3
     - str
     - O
     - freetext
   * - ``sps_4``
     - SPS.4
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - body site
   * - ``sps_5``
     - SPS.5
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - site modifier
   * - ``sps_6``
     - SPS.6
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - collection modifier method code
   * - ``sps_7``
     - SPS.7
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - specimen role

.. _hl7-v2_4-SRT:

SRT: Sort order
~~~~~~~~~~~~~~~

Section 2.9.42

.. py:class:: hl7types.hl7.v2_4.datatypes.SRT.SRT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``srt_1``
     - SRT.1
     - str
     - O
     - sort-by field
   * - ``srt_2``
     - SRT.2
     - str
     - O
     - sequencing

.. _hl7-v2_4-TQ:

TQ: Timing quantity
~~~~~~~~~~~~~~~~~~~

Section 2.9.46

.. py:class:: hl7types.hl7.v2_4.datatypes.TQ.TQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``tq_1``
     - TQ.1
     - :ref:`CQ <hl7-v2_4-CQ>`
     - O
     - quantity
   * - ``tq_2``
     - TQ.2
     - :ref:`RI <hl7-v2_4-RI>`
     - O
     - interval
   * - ``tq_3``
     - TQ.3
     - str
     - O
     - duration
   * - ``tq_4``
     - TQ.4
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - start date/time
   * - ``tq_5``
     - TQ.5
     - :ref:`TS <hl7-v2_4-TS>`
     - O
     - end date/time
   * - ``tq_6``
     - TQ.6
     - str
     - O
     - priority
   * - ``tq_7``
     - TQ.7
     - str
     - O
     - condition
   * - ``tq_8``
     - TQ.8
     - str
     - O
     - text (TX)
   * - ``tq_9``
     - TQ.9
     - str
     - O
     - conjunction component
   * - ``tq_10``
     - TQ.10
     - :ref:`OSD <hl7-v2_4-OSD>`
     - O
     - order sequencing
   * - ``tq_11``
     - TQ.11
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - occurrence duration
   * - ``tq_12``
     - TQ.12
     - str
     - O
     - total occurences

.. _hl7-v2_4-TS:

TS: Time stamp
~~~~~~~~~~~~~~

Section 2.9.47

.. py:class:: hl7types.hl7.v2_4.datatypes.TS.TS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ts_1``
     - TS.1
     - str
     - O
     - time of an event
   * - ``ts_2``
     - TS.2
     - str
     - O
     - degree of precision

.. _hl7-v2_4-TX_CHALLENGE:

TX_CHALLENGE: Challenge information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 8.7.3.44

.. py:class:: hl7types.hl7.v2_4.datatypes.TX_CHALLENGE.TX_CHALLENGE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``tx_challenge_1``
     - TX_CHALLENGE.1
     - str
     - O
     - ???????????
   * - ``tx_challenge_2``
     - TX_CHALLENGE.2
     - str
     - O
     - ???????????

.. _hl7-v2_4-UVC:

UVC: Value code and amount
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.UVC.UVC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``uvc_1``
     - UVC.1
     - str
     - O
     - value code
   * - ``uvc_2``
     - UVC.2
     - str
     - O
     - value amount

.. _hl7-v2_4-VH:

VH: Visiting hours
~~~~~~~~~~~~~~~~~~

Section 2.9.49

.. py:class:: hl7types.hl7.v2_4.datatypes.VH.VH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``vh_1``
     - VH.1
     - str
     - O
     - start day range
   * - ``vh_2``
     - VH.2
     - str
     - O
     - end day range
   * - ``vh_3``
     - VH.3
     - str
     - O
     - start hour range
   * - ``vh_4``
     - VH.4
     - str
     - O
     - end hour range

.. _hl7-v2_4-VID:

VID: Version identifier
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.50

.. py:class:: hl7types.hl7.v2_4.datatypes.VID.VID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``vid_1``
     - VID.1
     - str
     - O
     - version ID
   * - ``vid_2``
     - VID.2
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - internationalization code
   * - ``vid_3``
     - VID.3
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - international version ID

.. _hl7-v2_4-VR:

VR: Value qualifier
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_4.datatypes.VR.VR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``vr_1``
     - VR.1
     - str
     - O
     - first data code value
   * - ``vr_2``
     - VR.2
     - str
     - O
     - Last data code calue

.. _hl7-v2_4-WVI:

WVI: Channel identifier
~~~~~~~~~~~~~~~~~~~~~~~

Section 7.13.1.3

.. py:class:: hl7types.hl7.v2_4.datatypes.WVI.WVI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``wvi_1``
     - WVI.1
     - str
     - O
     - Channel Number
   * - ``wvi_2``
     - WVI.2
     - str
     - O
     - Channel Name

.. _hl7-v2_4-WVS:

WVS: Waveform source
~~~~~~~~~~~~~~~~~~~~

Section 7.13.1.3

.. py:class:: hl7types.hl7.v2_4.datatypes.WVS.WVS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``wvs_1``
     - WVS.1
     - str
     - O
     - source name 1
   * - ``wvs_2``
     - WVS.2
     - str
     - O
     - source name 2

.. _hl7-v2_4-XAD:

XAD: Extended address
~~~~~~~~~~~~~~~~~~~~~

Section 2.9.51

.. py:class:: hl7types.hl7.v2_4.datatypes.XAD.XAD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xad_1``
     - XAD.1
     - :ref:`SAD <hl7-v2_4-SAD>`
     - O
     - street address (SAD)
   * - ``xad_2``
     - XAD.2
     - str
     - O
     - other designation
   * - ``xad_3``
     - XAD.3
     - str
     - O
     - city
   * - ``xad_4``
     - XAD.4
     - str
     - O
     - state or province
   * - ``xad_5``
     - XAD.5
     - str
     - O
     - zip or postal code
   * - ``xad_6``
     - XAD.6
     - str
     - O
     - country
   * - ``xad_7``
     - XAD.7
     - str
     - O
     - address type
   * - ``xad_8``
     - XAD.8
     - str
     - O
     - other geographic designation
   * - ``xad_9``
     - XAD.9
     - str
     - O
     - county/parish code
   * - ``xad_10``
     - XAD.10
     - str
     - O
     - census tract
   * - ``xad_11``
     - XAD.11
     - str
     - O
     - address representation code
   * - ``xad_12``
     - XAD.12
     - :ref:`DR <hl7-v2_4-DR>`
     - O
     - address validity range

.. _hl7-v2_4-XCN:

XCN: Extended composite id number and name for persons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.52

.. py:class:: hl7types.hl7.v2_4.datatypes.XCN.XCN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xcn_1``
     - XCN.1
     - str
     - O
     - ID number (ST)
   * - ``xcn_2``
     - XCN.2
     - :ref:`FN <hl7-v2_4-FN>`
     - O
     - family name
   * - ``xcn_3``
     - XCN.3
     - str
     - O
     - given name
   * - ``xcn_4``
     - XCN.4
     - str
     - O
     - second and further given names or initials thereof
   * - ``xcn_5``
     - XCN.5
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``xcn_6``
     - XCN.6
     - str
     - O
     - prefix (e.g., DR)
   * - ``xcn_7``
     - XCN.7
     - str
     - O
     - degree (e.g., MD)
   * - ``xcn_8``
     - XCN.8
     - str
     - O
     - source table
   * - ``xcn_9``
     - XCN.9
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning authority
   * - ``xcn_10``
     - XCN.10
     - str
     - O
     - name type code
   * - ``xcn_11``
     - XCN.11
     - str
     - O
     - identifier check digit
   * - ``xcn_12``
     - XCN.12
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``xcn_13``
     - XCN.13
     - str
     - O
     - identifier type code (IS)
   * - ``xcn_14``
     - XCN.14
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning facility
   * - ``xcn_15``
     - XCN.15
     - str
     - O
     - Name Representation code
   * - ``xcn_16``
     - XCN.16
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - name context
   * - ``xcn_17``
     - XCN.17
     - :ref:`DR <hl7-v2_4-DR>`
     - O
     - name validity range
   * - ``xcn_18``
     - XCN.18
     - str
     - O
     - name assembly order

.. _hl7-v2_4-XON:

XON: Extended composite name and identification number for organizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.53

.. py:class:: hl7types.hl7.v2_4.datatypes.XON.XON
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xon_1``
     - XON.1
     - str
     - O
     - organization name
   * - ``xon_2``
     - XON.2
     - str
     - O
     - organization name type code
   * - ``xon_3``
     - XON.3
     - str
     - O
     - ID number (NM)
   * - ``xon_4``
     - XON.4
     - str
     - O
     - check digit (NM)
   * - ``xon_5``
     - XON.5
     - str
     - O
     - code identifying the check digit scheme employed
   * - ``xon_6``
     - XON.6
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning authority
   * - ``xon_7``
     - XON.7
     - str
     - O
     - identifier type code (IS)
   * - ``xon_8``
     - XON.8
     - :ref:`HD <hl7-v2_4-HD>`
     - O
     - assigning facility ID
   * - ``xon_9``
     - XON.9
     - str
     - O
     - Name Representation code

.. _hl7-v2_4-XPN:

XPN: Extended person name
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.54

.. py:class:: hl7types.hl7.v2_4.datatypes.XPN.XPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xpn_1``
     - XPN.1
     - :ref:`FN <hl7-v2_4-FN>`
     - O
     - family name
   * - ``xpn_2``
     - XPN.2
     - str
     - O
     - given name
   * - ``xpn_3``
     - XPN.3
     - str
     - O
     - second and further given names or initials thereof
   * - ``xpn_4``
     - XPN.4
     - str
     - O
     - suffix (e.g., JR or III)
   * - ``xpn_5``
     - XPN.5
     - str
     - O
     - prefix (e.g., DR)
   * - ``xpn_6``
     - XPN.6
     - str
     - O
     - degree (e.g., MD)
   * - ``xpn_7``
     - XPN.7
     - str
     - O
     - name type code
   * - ``xpn_8``
     - XPN.8
     - str
     - O
     - Name Representation code
   * - ``xpn_9``
     - XPN.9
     - :ref:`CE <hl7-v2_4-CE>`
     - O
     - name context
   * - ``xpn_10``
     - XPN.10
     - :ref:`DR <hl7-v2_4-DR>`
     - O
     - name validity range
   * - ``xpn_11``
     - XPN.11
     - str
     - O
     - name assembly order

.. _hl7-v2_4-XTN:

XTN: Extended telecommunication number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.9.55

.. py:class:: hl7types.hl7.v2_4.datatypes.XTN.XTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xtn_1``
     - XTN.1
     - str
     - O
     - [(999)] 999-9999 [X99999][C any text]
   * - ``xtn_2``
     - XTN.2
     - str
     - O
     - telecommunication use code
   * - ``xtn_3``
     - XTN.3
     - str
     - O
     - telecommunication equipment type (ID)
   * - ``xtn_4``
     - XTN.4
     - str
     - O
     - Email address
   * - ``xtn_5``
     - XTN.5
     - str
     - O
     - Country Code
   * - ``xtn_6``
     - XTN.6
     - str
     - O
     - Area/city code
   * - ``xtn_7``
     - XTN.7
     - str
     - O
     - Phone number
   * - ``xtn_8``
     - XTN.8
     - str
     - O
     - Extension
   * - ``xtn_9``
     - XTN.9
     - str
     - O
     - any text
