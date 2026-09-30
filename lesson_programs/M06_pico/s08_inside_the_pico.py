# Facts about the Pico, asked from MicroPython
import machine
import gc       # gc = "garbage collector": manages the memory
import os       # os = files on the flash memory

print("Board:", os.uname().machine)
print("MicroPython version:", os.uname().release)
print("Processor speed:", machine.freq() // 1000000, "MHz")
print("Free working memory:", gc.mem_free() // 1024, "KB")

s = os.statvfs("/")                    # information about the flash
print("Free flash memory:", s[0] * s[3] // 1024, "KB")
print("Files on the Pico:", os.listdir())
