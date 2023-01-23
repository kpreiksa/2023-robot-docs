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

PID
===

Holonomic Drive
===============

Ramsete
=======

Geometric Concepts
******************


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


     
