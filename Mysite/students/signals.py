import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student


@receiver(post_save, sender=Student)
def lod_student_update_addded_event(sender, **kwargs):

    logger = logging.getLogger('students.signal')

    student = kwargs['instance']
    if kwargs['created']:
        logger.info("Student added :" + student.first_name + " " +
                    student.last_name + " ID " + str(student.id))
    else:
        logger.info("Student updated: " + student.first_name + " " +
                    student.last_name + " ID " + str(student.id))
