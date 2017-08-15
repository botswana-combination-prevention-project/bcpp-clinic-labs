from edc_lab import AliquotType, LabProfile, ProcessingProfile, RequisitionPanel
from edc_lab.lab.processing_profile import Process
from edc_lab.site_labs import site_labs

from .constants import VIRAL_LOAD, RESEARCH_BLOOD_DRAW

lab_profile = LabProfile(name='bcpp_clinic_subject')

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')
bc = AliquotType(name='Buffy Coat', alpha_code='BC', numeric_code='16')
pl = AliquotType(name='Plasma', alpha_code='PL', numeric_code='32')

wb.add_derivatives(pl, bc)


processing_profile = ProcessingProfile(name='viral_load', aliquot_type=wb)
process_vl_bc = Process(aliquot_type=bc, aliquot_count=2)
process_vl_pl = Process(aliquot_type=pl, aliquot_count=3)
processing_profile.add_processes(process_vl_bc, process_vl_pl)

processing_profile = ProcessingProfile(name='rbd', aliquot_type=wb)
process_rbd_bc = Process(aliquot_type=bc, aliquot_count=2)
process_rbd_pl = Process(aliquot_type=pl, aliquot_count=4)
processing_profile.add_processes(process_rbd_bc, process_rbd_pl)


panel_vl = RequisitionPanel(
    name=VIRAL_LOAD,
    aliquot_type=wb,
    processing_profile=processing_profile)

panel_rbd = RequisitionPanel(
    name=RESEARCH_BLOOD_DRAW,
    aliquot_type=wb,
    abbreviation='RBD',
    processing_profile=processing_profile)

lab_profile.add_panel(panel_vl)
lab_profile.add_panel(panel_rbd)

site_labs.register(
    lab_profile, requisition_model='bcpp_clinic_subject.subjectrequisition')
