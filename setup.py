from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A collection of custom NER tools that make tagging, labeling with custom labels, training a custom NER (NERC) model, evaluating it, and visualizing the results a lot easier by automating much of the process. Annotation to BIO/CoNLL-2003 file format, SpaCy, and SimpleTransformers dataframe is provided. Any library can be used for training from then on, but Flair, Spacy, SimpleTransformers are provided as optioing (AllenNLPalong with basic visualization.',
    author='Dainis Boumber',
    license='MIT',
)
