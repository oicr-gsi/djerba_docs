=============================
djerba: case_overview: v1.0.0
=============================


        * :ref:`djerba.case_overview_summary`
        * :ref:`djerba.case_overview_generic_params`
        * :ref:`djerba.case_overview_specific_params`
        * :ref:`djerba.case_overview_description`
        


For explanation of each section, see the main :ref:`plugin-reference` page.

.. _djerba.case_overview_summary:

***********************************
Summary
***********************************

Plugin to generate the Case Overview report section

Assay can be specified by:
- Short name, which looks up in a table of known assays
- Full name -- if this parameter is set manually, the short name is ignored
Typically the short name will be used, but the full name is supported as an INI parameter
in case assay names are introduced/changed at short notice


.. _djerba.case_overview_specific_params:

***********************************
Specific Parameters
***********************************

==================== ======= =====
Parameter            Default Notes
==================== ======= =====
assay                N/A          
assay_description    N/A          
donor                N/A          
normal_id            N/A          
patient_study_id     N/A          
primary_cancer       N/A          
report_id            N/A          
requisition_approved N/A          
site_of_biopsy       N/A          
study                N/A          
tumour_id            N/A          
==================== ======= =====

.. _djerba.case_overview_generic_params:

***********************************
Generic Parameters
***********************************

================== ======== =====
Parameter          Default  Notes
================== ======== =====
attributes         clinical      
configure_priority 200           
depends_configure  (empty)       
depends_extract    (empty)       
extract_priority   200           
render_priority    40            
================== ======== =====

.. _djerba.case_overview_description:

***********************************
Description
***********************************

No description provided.

