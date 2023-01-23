##############
Code Structure
##############

The intent of this page is to describe the structure of robot software.

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


Directories
***********

lib
===

Contains libraries used throughout the code.

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``CoordSysUtil``
     - A collection of methods to calculate poses, angles, and distances depending on alliance
     - Not implemented yet

   * - ``Counter``
     - A counter with initial, min, and max values, which can wrap-around values
     -

   * - ``ElevArmKinematics``
     - Kinematics to model an elevator arm
     - Not implemented yet

   * - ``FailSource``
     - An enum representing different types of faults
     - 

   * - ``LatchedBoolean``
     - A boolean which only returns true once (when it changes from false to true)
     - 

   * - ``LinearInterpolationTable``
     - Implements linear interpolation based on a table of values
     - 

   * - ``LoopingQueue``
     - Implementation of a queue which wraps around to the beginning after iterating through the whole queue.
     -

   * - ``NetworkStatus``
     - An enum representing the status of the network (disconnected, connected to DS only, or connected to FMS)
     -

   * - ``PIDConstants``
     - Configures phoenix pro constants
     - 

   * - ``ThreadedRunnable``
     - Schedules a runnable as a thread
     - 

   * - ``Utility``
     - Various methods to work with strings, numbers, arrays, system functionality (threads, etc.)
     - 


audio
-----

Libraries related to producing audio with motors.

Uses the WPILib ``Filesystem`` object to get files from the deploy directory.

.. tip::
    Use the ``Filesystem.getDeployDirectory`` wpilib function to get a proper 
    path relative to the deploy directory.

dashboard
---------

Libraries related to sending information to the dashboard (SmartDashboard/ShuffleBoard)

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``Alert``
     - Sends persistent alerts to the driver station
     - We should use this for critical errors to help with debugging

   * - ``SendableTriggerButton``
     - Allows elements on the driver station to function like a button
     - With a touchscreen, perhaps this would be useful for game piece scoring

   * - ``SendableTriggerSwitch``
     - Similar to ``SendableTriggerButton``, but for continuing actions (but can also trigger actions on rising/falling edges)
     - 

   * - ``TelemetryFromSupplier``
     - Allows sending data to the dashboard from any class which implments a ``.get()`` method (``Supplier`` interface)
     - 

   * - ``TelemetryObject``
     - Allows sending data to the dashboard and a datalog function (any class which implements a ``.accept(Object)`` method - ie. a ``Consumer`` interface)
     - 

   * - ``WidgetConfig``
     - Configures a Shuffleboard widget based on location and type (including custom widgets)
     - 

   * - ``WidgetObject``
     - Represents a Shuffleboard widget configured with a ``WidgetConfig``
     - 

   * - ``WidgetSendable``
     - Does the same, but for ``Sendable`` datatypes.
     - 

   * - ``WidgetVideoStream``
     - Does the same, but for a video stream
     - 

input
-----

Libraries related to getting information from drivers, including controllers, as well 
as providing limited driver feedback through controller rumble. Also contains implementation 
of driver profiles

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``Controller``
     - Stores the state of sticks (axes) and buttons being sent from the DriverStation and does rising/falling edge detection.
     - Seems like a **RE-IMPLEMENTATION** of ``XBoxController``

   * - ``ControllerDriveInputs``
     - Performs drive-specific adjustments to controller inputs. Includes functionality such as cubing inputs for preceision control, max velocity, deadzone, etc.
     - This is a great idea for advanced control!

   * - ``ControllerRumbleTypes``
     - Defines enums for controller rumble
     - Great operator feedback

   * - ``DriverProfile``
     - Allows for customization of controls based on driver preferences
     - This is great, not only from a practical sense (ie. if the team has multiple drivers), but also from a code organization/abstraction sense. This means that there is one place where all preferences (as opposed to functionality/logic) is defined.

   * - ``DriverProfile.Triggers``
     - Defines different triggers/"actions" the driver would want to perform.
     - It is great that these are defined explicitly 

   * - ``HybridGenericHID``
     - Defines different types of HID to use for control. 
     - Appears to be unused. The types appear to be defined in **WPILib**, but implemented here as an enum

   * - ``OperatorProfile``
     - Similar to ``DriverProfile`` but for operator actions
     - 

leds
----

Libraries related to interacting with LEDs (ie. providing driver/human player feedback)

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``CANdleAnimation``
     - Defines an interface for CANdle animations to implement
     - 

   * - ``CANdleColor``
     - Defines colors as RGB combinations 
     - 

   * - ``ColorAnimationBuilder``
     - Simplifies building animations involving one color using the phoenix libraries
     - 

   * - ``ColorAnimationTypes``
     - Defines enum of supported animation types
     - 

   * - ``LEDGroup``
     - Defines an LED group (start, end, layer)
     -

   * - ``RainbowAnimationBuilder``
     - Simplifies building a rainbow animation using phoenix libraries
     - 


motors
------

Libraries related to interacting with motor controllers. Specifically, implements "Lazy" 
motor controllers which only update their state when commanded value changes. These are 
instantiated with "factory" classes. 

.. admonition:: Question
   :class: hint

    What is the benefit of this? Is it to save on CAN bandwidth or other performance metric?


.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``LazyCANSparkMax``
     - Extends ``CANSparkMax``, overrides ``.set(double speed)`` method to reduce CAN usage by only sending new values.
     - 

   * - ``LazyTalonFX``
     - Extends ``TalonFX``, overrides ``.set(double speed)`` method to reduce CAN usage by only sending new values.
     -

   * - ``LazyTalonSRX``
     - Extends ``TalonSRX``, overrides ``.set(double speed)`` method to reduce CAN usage by only sending new values.
     -

   * - ``LazyVictorSPX``
     - Extends ``VictorSPX``, overrides ``.set(double speed)`` method to reduce CAN usage by only sending new values.
     -

   * - ``SparkMaxFactory``
     - Provides static methods which return a ``LazyCANSparkMax`` (aka "Factory" methods), configured with good default values
     - Is there any reason to move some of this config into a config file? Or does this class serve as the config file, and additional configurations will be handled within this file? In general I like this because it makes motor controller definition a single line of code that is clear rather than doing all of the configuration in-line (too confusing, too verbose)

   * - ``SparkUtil``
     - Provides methods of retreiving, parsing, and storing faults. The default way of doing this requries many calls. This class greatly simplifies capturing all faults.
     - 

   * - ``TalonFXFactory``
     - Provides static methods which return a ``LazyTalonFX`` (aka "Factory" methods), configured with good default values
     -

   * - ``TalonFXProFactory``
     - Provides static methods which return a ``TalonFX`` (aka "Factory" methods), configured with good default values for Phoenix Pro.
     -

   * - ``TalonUtil``
     - Provides methods or retreiving, parsing, and storing faults. Also provides methods for retreiving faults from Phoenix pro itself.
     - 
     
power
-----

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``BatteryState``
     - Represents the state of the battery (voltage, estimated SoC), power draw (current, wattage), and implications (ie. brownout)
     - 

   * - ``EnergyBlock``
     - An interface to represent a group of energy consuming devices that can have their power reduced and restored synchronously
     - 


Libraries related to monitoring the power system of the robot. This includes voltage and 
current monitoring, brownout detection, and more. 
 

selftest
--------

Provides monitoring of the system and reporting of faults. 

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``DeviceStatus``
     - Enum representing state of a device in the diagnostics framework
     - 

   * - ``StatusReporter``
     - An interface (implemented mostly in Diagnostics subsystem) defining what a device has to do to report status
     - 

   * - ``StatusReporterBase``
     - An abstract base class which implements the methods defined by ``StatusReporter`` 
     - 

   * - ``SystemDiagnostics``
     - Defines system diagnostics for motor controllers, etc. 
     - 

sensors
-------

Libraries related to sensor interfacing (CAN Coder)

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``CANCoderProFactory``
     - Provides static methods which return a ``CANcoder`` (aka "Factory" methods), configured with good default values
     - 

subsystem
---------

Libraries related to thread and task executor subsystems. 
Uses classes from ``java.util.concurrency`` 

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``OldAbstractSubsystem``
     - Deprecated abstract subsystem
     - 

   * - ``ThreadSubsystem``
     - An abstract class which defines how a threaded subsystem works. The only abstract methods (which must be implemented by a child class) are ``.fastUpdate()`` and ``.slowUpdate()``. This abstract class wraps those methods to ensure the thread stays running (watchdog), and schedules the ``slowUpdate`` to run at a rate that is a multiple of the ``fastUpdate`` rate. 
     -

   * - ``TaskExecutorSubsystem``
     - An abstract class which extends ``ThreadSubsystem`` and defines a subsystem which executes a task at the ``fastUpdate`` rate. 
     - 

   * - ``TaskExecutorSubsystem``
     - An abstract class which defines a subsystem which executes a task at the ``fastUpdate`` rate. 
     - 

   * - ``ThreadWatchdog``
     - A class which implements methods to monitor a ``ThreadSubsystem``
     - 

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

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``AprilTagMetadata``
     - Simple class to represent an AprilTag and its position
     - 

   * - ``VisionPoseEstimate``
     - A class to represent the pose estimate retrieved from vision and when it was retrieved
     -


robot
=====

Files related to the base robot object (ie. definitions, constants, 
configuration).

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``BuildConstants``
     - Metadata associated with the build, such as source branch, build parameters, etc. 
     - 

   * - ``Constants``
     - Defines many constants about the robot (ie. configuration, rather than logic). Contains things such as: CAN configuration, Driver/Operator profiles, drivetrain configuration (motor controllers, gear ratios, PID constants, geometry/wheelbase), pneumatics, LEDs/human feedback, vision, etc. 
     - 

   * - ``FieldConstants``
     - Defines constants about the field (eg. AprilTag locations)
     - 

   * - ``Main``
     - Starts up the ``RobotBase`` code
     - 

   * - ``OI``
     - "Operator Interface" - Defines everything the operator needs to interface with (drive and tracking subsystems, tasks which get run when buttons are pressed, etc.)
     - 

   * - ``Robot``
     - Defines background interactions with the robot (ie. base functionality provided by WPILib scheduling). Sets up subsystems that run in the background, adds widgets to Shuffleboard (including some that configure how the robot will work - ie. ``Sendable``). ``robotInit`` method 
     - 

   * - ``SwerveLibrary``
     - Contains definitions for each chassis. Defines which motors, encoders, and module config (ie. PID constants, wheel diameter, and gear ratios) applies to the chassis. This is set in ``Drive.java`` in *subsystems* folder
     -

.. admonition:: Question
   :class: hint

    Is there a special way to schedule auton code that is not in ``autonomousPeriodic``?


subsystems
==========

Defines subsystems, which are entities (usually to be controlled or monitored) consisting of hardware and actions to perform on that hardware.

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``Claw``
     - 
     - 

   * - ``Diagnostics``
     - 
     - 

   * - ``Drive``
     - 
     - 

   * - ``EnergyManagement``
     - 
     - 

   * - ``InputManager``
     - 
     - 

   * - ``LEDController``
     - 
     - 

   * - ``Manipulator``
     - 
     - 

   * - ``Pneumatics``
     - 
     - 

   * - ``RobotTracker``
     - 
     - 

   * - ``Telemetry``
     - 
     - 


tasks
=====

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1

   * - Class/File
     - Description
     - Comments

   * - ``InstantRamsete``
     - 
     - 

   * - ``NoPushMode``
     - 
     - 

   * - ``TeleopDrive``
     - 
     - 