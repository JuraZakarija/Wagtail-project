from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add title')
    text = blocks.TextBlock(required=True, help_text='Add text')

    class Meta:
        template = "blocks/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class RichTextBlock(blocks.RichTextBlock):
    
    class Meta:
        template = "blocks/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):
    
    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:
        template = "blocks/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"
