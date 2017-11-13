# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Student(models.Model):
    class Meta(object):
        verbose_name = _(u"Student")
        verbose_name_plural = _(u"Students")

    first_name = models.CharField(max_length=256,
                                  blank=False,
                                  verbose_name=_(u"First Name"))

    last_name = models.CharField(max_length=256,
                                 blank=False,
                                 verbose_name=_(u"Last Name"))

    middle_name = models.CharField(max_length=256,
                                   blank=True,
                                   verbose_name=(u"Surname"),
                                   default='')

    student_group = models.ForeignKey('Group',
                                      verbose_name=_(u"Group"),
                                      blank=False,
                                      null=True,
                                      on_delete=models.PROTECT)

    birthday = models.DateField(blank=False,
                                verbose_name=_(u"Birthday"),
                                null=True)

    photo = models.ImageField(blank=True,
                              verbose_name=_(u"Photo"),
                              null=True)

    ticket = models.CharField(max_length=256,
                              blank=False,
                              verbose_name=_(u"Ticket"))

    notes = models.TextField(blank=True,
                             verbose_name=_(u"Additional notes"))

    def __str__(self):
        return self.first_name + " " + self.last_name


class Group(models.Model):

    class Meta(object):
        verbose_name = _(u"Group")
        verbose_name_plural = _(u"Groups")

    title = models.CharField(max_length=256,
                             blank=False,
                             verbose_name=_(u"Name"))

    leader = models.OneToOneField('Student',
                                  verbose_name=_(u"Leader"),
                                  blank=True,
                                  null=True,
                                  on_delete=models.SET_NULL)

    notes = models.TextField(blank=True,
                             verbose_name=_(u"Additional notes"))

    def __str__(self):
        if self.leader:
            return self.title + ' ' + self.leader.first_name + ' ' + self.leader.last_name
        else:
            return self.title


class Exam(models.Model):

    class Meta(object):
        verbose_name = _(u"Exam")
        verbose_name_plural = _(u"Exams")

    title = models.CharField(max_length=256,
                             blank=False,
                             verbose_name=_(u"Subject"))

    data = models.DateTimeField( blank=True,
                                verbose_name=_(u"Data"),
                                null=True)

    ticher_name = models.CharField(max_length=256,
                                   blank=False,
                                   verbose_name=_(u"Teacher"))

    exam_group = models.ForeignKey('Group',
                                        verbose_name=_(u"Group"),
                                        blank=False)

    def __str__(self):
        return self.title


class Journal(models.Model):

    class Meta(object):
        verbose_name = _(u"Monthly Magazine")
        verbose_name_plural = _(u"Monthlys Magazine")

    student = models.ForeignKey('Student',
                                verbose_name=_(u'Student'),
                                blank=False,
                                unique_for_month='date'
                                )

    data = models.DateField(blank=False,
                            verbose_name=_(u"Data"),
                            )

    present_day1 = models.BooleanField(default=False)
    present_day2 = models.BooleanField(default=False)
    present_day3 = models.BooleanField(default=False)
    present_day4 = models.BooleanField(default=False)
    present_day5 = models.BooleanField(default=False)
    present_day6 = models.BooleanField(default=False)
    present_day7 = models.BooleanField(default=False)
    present_day8 = models.BooleanField(default=False)
    present_day9 = models.BooleanField(default=False)
    present_day10 = models.BooleanField(default=False)
    present_day11 = models.BooleanField(default=False)
    present_day12 = models.BooleanField(default=False)
    present_day13 = models.BooleanField(default=False)
    present_day14 = models.BooleanField(default=False)
    present_day15 = models.BooleanField(default=False)
    present_day16 = models.BooleanField(default=False)
    present_day17 = models.BooleanField(default=False)
    present_day18 = models.BooleanField(default=False)
    present_day19 = models.BooleanField(default=False)
    present_day20 = models.BooleanField(default=False)
    present_day21 = models.BooleanField(default=False)
    present_day22 = models.BooleanField(default=False)
    present_day23 = models.BooleanField(default=False)
    present_day24 = models.BooleanField(default=False)
    present_day25 = models.BooleanField(default=False)
    present_day26 = models.BooleanField(default=False)
    present_day27 = models.BooleanField(default=False)
    present_day28 = models.BooleanField(default=False)
    present_day29 = models.BooleanField(default=False)
    present_day30 = models.BooleanField(default=False)
    present_day31 = models.BooleanField(default=False)

    def __str__(self):
        return self.student.last_name


