##############
Code Structure
##############

The intent of this page is to describe the structure of 3707's robot software.

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

