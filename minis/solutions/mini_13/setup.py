
from setuptools import Extension, setup

setup(
	name="matrixpow",
	version="1.0.0",
	description="pow matrix module",
	author="Trinity",
	author_email="n.sharapov.nsk@gmail.com",
	ext_modules=[
		Extension(
			name="matrixpow",
			sources=["matrixpow.c"],
		),
	]
)