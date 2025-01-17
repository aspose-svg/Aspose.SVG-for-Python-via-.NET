from aspose.svg import *
from aspose.svg.saving import *
from aspose.svg.converters import *
from aspose.svg.rendering.image import *
from aspose.svg.rendering import *
from aspose.svg.drawing import *
from aspose.svg.imagevectorization import *


def vectorize_image(file, colors_limit=25, severity=-1, threshold_error=-1, max_iterations=-1, line_width=1):
    path_builder = BezierPathBuilder()
    path_builder.trace_smoother = ImageTraceSmoother(severity) if severity != -1 else None
    path_builder.error_threshold = float(threshold_error) if threshold_error != -1 else 30.0
    path_builder.max_iterations = int(max_iterations) if max_iterations != -1 else 30

    vectorizer = ImageVectorizer()
    vectorizer.configuration.path_builder = path_builder
    vectorizer.configuration.colors_limit = colors_limit
    vectorizer.configuration.line_width = float(line_width)
    vectorize(vectorizer, file)

def vectorize(vectorizer: ImageVectorizer, file: str):
    with vectorizer.vectorize(file) as document:
        output_file = file + ".svg"
        document.save(output_file)

def main():
    vectorize_image('data/fish.png', 25, -1, 10, 20, 1.2)
    vectorize_image('data/flower.png', 2, 1, 5)

if __name__ == '__main__':
    main()