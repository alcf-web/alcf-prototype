# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 05:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_homepage_page_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='image_carousel',
            field=wagtail.wagtailcore.fields.StreamField([('carousel', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock()), (b'text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock())]))]),
        ),
    ]
