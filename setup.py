from setuptools import find_packages, setup

package_name = 'optitrack_pose'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gianluca',
    maintainer_email='gianluca.nordio01@outlook.it',
    description='convert the optitrack /poses topic to a ROS2 pose',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node = optitrack_pose.node:main',
        ],
    },
)
