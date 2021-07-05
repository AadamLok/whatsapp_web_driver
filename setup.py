from setuptools import find_packages, setup

setup(
    name='whatsapp_web_driver',
    packages=find_packages(include=['whatsapp_web_driver']),
    version='0.0.0',
    description='Enables the user to easily create their own whatsapp bot.',
    author='Aadam Lokhandwala, Murtaza Cyclewala',
    license='Apache 2.0',
    install_requires=['selenium','pywin32','pyautogui'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    url="https://github.com/AadamLok/whatsapp_web_driver",
    keywords=["Web Whatsapp Automation", "Whatsapp Bot", "Whatsapp"],
)