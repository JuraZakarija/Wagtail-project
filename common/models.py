from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField
from modelcluster.fields import ParentalKey

from .blocks import TitleAndTextBlock, RichTextBlock, SimpleRichTextBlock


class FlexPage(Page):
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    content = StreamField(
        [
            ('title_and_text', TitleAndTextBlock()),
            ('fult_text', RichTextBlock()),
            ("simple_richtext", SimpleRichTextBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        StreamFieldPanel('content')
    ]

    api_fields = [
        APIField('subtitle'),
        APIField('content'),
    ]

    

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('carousel_images', label="Homepage Carousel", min_num=1, max_num=5),
    ]

    max_count = 1

    api_fields = [
        APIField('body'),
        APIField('carousel_images'),
    ]


class HomePageCarousel(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='carousel_images')
    title = models.CharField(max_length=250)
    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('carousel_image'),
    ]

    api_fields = [
        APIField('carousel_image'),
    ]



class BlogListPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class BlogDetailPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('image')
    ]
