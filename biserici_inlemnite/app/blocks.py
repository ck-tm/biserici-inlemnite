from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    ListBlock,
)
from wagtail.contrib.table_block.blocks import TableBlock


class CarouselBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = "fa-camera-retro"
        # template = "blocks/carousel.html"


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class ImageTextBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    title = CharBlock(required=False)
    caption = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_text_block.html"


class SectionHeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to set a heading
    """

    heading_text = CharBlock(classname="title", required=True)

    class Meta:
        icon = "title"
        template = "blocks/section_heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"


class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    # heading_block = SectionHeadingBlock()
    paragraph_block = RichTextBlock(icon="fa-paragraph", features=["h1", "h2", "h3", "bold", "ol", "ul"])
    # image_block = ImageBlock()
    # image_text_block = ImageTextBlock()
    # carousel = ListBlock(
    # CarouselBlock(label="Poza"),
    # template="blocks/carousel.html")
    # block_quote = BlockQuote()

    class Meta:
        icon = "fa-quote-left"
        # template = "blocks/blockquote.html"
