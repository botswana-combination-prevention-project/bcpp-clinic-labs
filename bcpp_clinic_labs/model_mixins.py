from django.db import models

from edc_lab.model_mixins.requisition import RequisitionIdentifierMixin
from edc_lab.model_mixins.requisition import RequisitionModelMixin, RequisitionStatusMixin
from edc_map.site_mappers import site_mappers
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_offstudy.model_mixins import OffstudyMixin
from edc_search.model_mixins import SearchSlugManager
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as VisitTrackingCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin


class Manager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass


class SubjectRequisitionModelMixin(
        RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin,
        VisitTrackingCrfModelMixin, OffstudyMixin,
        PreviousVisitModelMixin,
        UpdatesRequisitionMetadataModelMixin, models.Model):

    objects = Manager()

    def save(self, *args, **kwargs):
        self.study_site = site_mappers.current_map_code
        self.study_site_name = site_mappers.current_map_area
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        fields = [
            'requisition_identifier',
            'human_readable_identifier',
            'panel_name',
            'panel_object.abbreviation',
            'identifier_prefix']
        return fields

    class Meta:
        abstract = True
