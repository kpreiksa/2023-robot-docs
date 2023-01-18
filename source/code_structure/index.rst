##############
Code Structure
##############

The intent of this page is to describe the structure of robot software.

Directories
***********

lib
===

Contains libraries used throughout the code.

audio
-----

Libraries related to producing audio with motors.

dashboard
---------

Libraries related to sending information to the dashboard (SmartDashboard/ShuffleBoard)

input
-----

Libraries related to getting information from drivers, including controllers, as well 
as providing limited driver feedback through controller rumble. Also contains implementation 
of driver profiles

leds
----

Libraries related to interacting with LEDs (ie. providing driver/human player feedback)

motors
------

Libraries related to interacting with motor controllers. Specifically, implements "Lazy" 
motor controllers which only update their state when commanded value changes. These are 
instantiated with "factory" classes. 

.. hint::

    What is the benefit of this? Is it to save on CAN bandwidth or other performance metric?

power
-----

Libraries related to monitoring the power system of the robot. This includes voltage and 
current monitoring, brownout detection, and more. 

``EnergyBlock`` is an interface allowing devices to be disabled if desired. 

selftest
--------

Provides monitoring of the system and reporting of faults. 

sensors
-------

Libraries related to sensor interfacing (CAN Coder)

subsystem
---------

Libraries related to thread and task executor subsystems. 
Uses classes from ``java.util.concurrency`` 

swerve
------

Libraries related to controlling a Swerve drivetrain.

drive
^^^^^

Different implementation of swerve drive motors

encoder
^^^^^^^

Different implementation of encoders for swerve drive 
wheel rotation (twist)

twist
^^^^^

Different implementation of swerve twist motors

SwerveDrive
^^^^^^^^^^^

Interface which implements a swerve drive motor

SwerveEncoder
^^^^^^^^^^^^^

Interface which implements a swerve twist encoder

SwerveSteering
^^^^^^^^^^^^^^

Interface which implments a swerve twist motor

SwerveModule
^^^^^^^^^^^^

Interface which implements an individual swerve module 
(state and control). 

SwerveModuleBase
^^^^^^^^^^^^^^^^

An implementation of SwerveModule

SwerveModuleGroup
^^^^^^^^^^^^^^^^^

A group of individual ``SwerveModule`` s (ie. a chassis)

SwerveModuleTelemetry
^^^^^^^^^^^^^^^^^^^^^

Diagnostics and monitoring of swerve modules and components


tasks
-----

Libraries to implement "tasks"

.. hint::

    Unsure of the use-cases for this. 

vision
------

Libraries related to vision processing 

AprilTagMetadata
^^^^^^^^^^^^^^^^

Simple class to represent an AprilTag and its position

robot
=====

Files related to the base robot object (ie. definitions, constants, 
configuration).

BuildConstants
--------------

Metadata associated with the build, such as source branch, build parameters, 
etc. 

Constants
---------

Configuration that changes based on robot build, motors, tuning, 
user preferences, etc. 

FieldConstants
--------------

Information about the field, which should not change between 
matches, robots, etc. 

OI (Operator Interface)
-----------------------

Initializes code to interface with the operator/driver


SwerveLibrary
-------------

Various implementaiton of swerve drive, defined for different robots, etc. 

