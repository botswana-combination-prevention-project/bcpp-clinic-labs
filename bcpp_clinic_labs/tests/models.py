from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin

from ..model_mixins import SubjectRequisitionModelMixin


class SubjectVisit(NonUniqueSubjectIdentifierFieldMixin, BaseUuidModel):

    pass


class SubjectRequisition(SubjectRequisitionModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)
