from setuptools import setup

setup(
    name='httpie-oauth-dm',
    description='Dailymotion OAuth plugin for HTTPie.',
    version='1.0',
    author='Fabrice Aneche',
    author_email='akh@nobugware.com',
    license='BSD',
    url='https://github.com/akhenakh/httpie-oauth-dm',
    download_url='https://github.com/akhenakh/httpie-oauth-dm',
    py_modules=['httpie_oauth_dm'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_oauth2dm = httpie_oauth_dm:OAuth2DMPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'requests-oauthlib>=0.3.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
