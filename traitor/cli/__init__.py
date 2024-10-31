from cloup import group, version_option, help_option

from .. import __version__


@group(
    "traitor",
    help="A tool to extract morphological traits from images",
    no_args_is_help=True,
)
@help_option("-h", "--help")
@version_option(__version__, "-v", "--version")
def cli():
    pass


from . import extract, align, measure, extract_ordered, shape

cli.add_command(extract.extract)
cli.add_command(align.align)
cli.add_command(measure.measure)
cli.add_command(extract_ordered.extract_ordered)
cli.add_command(shape.shape)
