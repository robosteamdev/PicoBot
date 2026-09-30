# Lesson programs

All complete programs of the PicoBot Teachers' Toolkit lessons, tested, one folder per module. The file names are the
ones used in the lessons: `s15_…` belongs to session 15, `quiz_…` to the module quiz. The lesson explains each program.

| Folder | Module |
|---|---|
| `M04_cpp_to_python/` | M04 From C++ to Python |
| `M05_python/` | M05 Introduction to Python |
| `M06_pico/` | M06 The Raspberry Pi Pico 2 W |
| `M07_programming_pico/` | M07 Programming the Pico |
| `M08_sensors_electricity/` | M08 Sensors and electricity |
| `M09_driving/` | M09 Programming the mecanum base |
| `M10_arm/` | M10 Programming the arm |
| `M11_line_following/` | M11 Line following and marker detection |
| `M12_capstone_competitions/` | M12 Capstone projects and competitions |

**Where they run:** the programs of M04 and M05 run on the computer, in Thonny with **Local Python 3** (except the two
Pico programs of M04, blink and SOS). From M06 on, the programs run on the Pico: open them in Thonny, connected to the
Pico, and click **Run**. Programs that drive the wheels or move the arm need the files of `../library/` in the Pico's
main folder. A few programs import a helper file of the same folder (for example `helpers.py`) — copy it too. The competition
programs of M12 also need `competition.py` and your own `credentials.py` from
<https://github.com/robosteamdev/picobot-competition-library>.

**Safety:** lift the robot before a program turns the wheels for the first time, and keep fingers away from the gripper.
