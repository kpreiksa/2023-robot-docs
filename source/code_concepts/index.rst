.. _code-concepts:

#############
Code Concepts
#############

The intent of this page is to describe concepts employed in writing the robot code

Java Concepts
*************

.. list-table:: 
   :widths: 25 75
   :header-rows: 1

   * - Term
     - Description

   * - ``interface``
     - Defines what methods a class must implement. That is, it defines a way to interact with an object of that type (ie. to "interface" with it), but does not define what these interactions are. 

   * - ``abstract class``
     - A class which defines some "base" functionality of a class, but which can be extended (with the ``extend`` keyword) by child classes.

   * - ``final``
     - This type modifier means that a reference (ie. variable) cannot be reassigned to another object. That is, you cannot make the pointer point to another spot in memory. However, if the object itself can make changes to itself (through methods or properties), those can be changed.

   * - Singleton
     - A pattern in which there is exactly one instance of a class in the entire program. This is (almost) always implemented as a ``static`` reference inside the class itself.


Control Concepts
****************

Kinematics and Odometry
=======================

Kinematics describes the movement of the robot (both forwards-backwards, left-to-right, and rotaton)

Odometry is the process of estimating the position of the robot on the field. 

Kinematics will primarily work with ``ChassisSpeeds`` objects, and odometry will primarily work with ``Pose2d`` objects.

Kinematics can also transform speeds between robot-relative and field-relative

PID
===

Holonomic Drive
===============

Ramsete
=======

Geometric Concepts
******************

Pose
====

WPI References
**************

.. list-table:: 
   :widths: 25 75
   :header-rows: 1

   * - WPI Link
     - Description

   * - `Controls Glossary <https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controls-glossary.html>`_ 
     - An overview of Controls terms

   * - `Ramsete Controller <https://docs.wpilib.org/en/stable/docs/software/advanced-controls/trajectories/ramsete.html>`_ 
     - Describes how a Ramsete controller works

   * - `Path Planning <https://docs.wpilib.org/en/stable/docs/software/pathplanning/index.html>`_ 
     - Describes path planning as a concept and how to implement it on an FRC robot

   * - `Intro to Kinematics <https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/intro-and-chassis-speeds.html>`_ 
     - Describes the concepts of Kinematics and Odometry, and the ``ChassisSpeeds`` object used in Java to work with Kinematics.

   * - `Swerve Drive Kinematics <https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/swerve-drive-kinematics.html>`_ 
     - Kinematics for Swerve Drive robots!

   * - `Swerve Drive Odometry <https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/swerve-drive-odometry.html>`_ 
     - Odometry for Swerve Drive robots!