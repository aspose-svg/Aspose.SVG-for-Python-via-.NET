import aspose
import aspose.svg as svg
import aspose.svg.rendering as rendering
import aspose.svg.rendering.image as image_rendering
import aspose.svg.rendering.pdf as pdf_rendering
from aspose.svg.rendering import SizingType
from aspose.svg.drawing import Resolution

def convert_svg_to_png(svg_path, output_path):
    document = svg.SVGDocument(svg_path)
    options = image_rendering.ImageRenderingOptions()
    options.background_color = aspose.pydrawing.Color.transparent
    options.page_setup.sizing = SizingType.FIT_CONTENT
    with open(output_path, 'wb') as output_stream:
        device = image_rendering.ImageDevice(options, output_stream)
        renderer = rendering.SvgRenderer()
        renderer.render(device, document)

def convert_svg_to_pdf(svg_path, output_path):
    document = svg.SVGDocument(svg_path)
    options = pdf_rendering.PdfRenderingOptions()
    options.page_setup.sizing = SizingType.FIT_CONTENT
    options.horizontal_resolution = Resolution.from_dots_per_inch(96.0)
    options.vertical_resolution = Resolution.from_dots_per_inch(96.0)
    with open(output_path, 'wb') as output_stream:
        device = pdf_rendering.PdfDevice(options, output_stream)
        renderer = rendering.SvgRenderer()
        renderer.render(device, document)

def main():
    svg_file = 'data/paths.svg'  # Example SVG file path
    convert_svg_to_png(svg_file, 'output.png')
    convert_svg_to_pdf(svg_file, 'output.pdf')


if __name__ == '__main__':
    main()