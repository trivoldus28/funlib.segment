from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

setup(
        name='funlib.segment',
        version='0.1',
        description='Tools to segment graphs and volumes.',
        url='https://github.com/funkelab/funlib.segment',
        author='Jan Funke',
        author_email='funkej@janelia.hhmi.org',
        license='MIT',
        packages=[
            'funlib.segment',
            'funlib.segment.graphs',
            'funlib.segment.graphs.impl',
            'funlib.segment.arrays',
            'funlib.segment.arrays.impl'
        ],
        ext_modules=cythonize([
            Extension(
                'funlib.segment.arrays.impl.replace_values_inplace',
                sources=[
                    'funlib/segment/arrays/impl/replace_values_inplace.pyx'
                ],
                extra_compile_args=['-O3'],
                language='c++'),
            Extension(
                'funlib.segment.graphs.impl.connected_components',
                sources=[
                    'funlib/segment/graphs/impl/connected_components.pyx',
                    'funlib/segment/graphs/impl/connected_components_impl.cpp'
                ],
                extra_compile_args=['-O3', '-std=c++11'],
                language='c++')
        ])
)