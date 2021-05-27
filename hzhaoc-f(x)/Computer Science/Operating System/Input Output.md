# Basic I/O Features
![[basic_io_features.png]]
# CPU - Device Interconnect: PCI
Peripheral component interconnect
- Memory-mapped
- Path: interrupt, poll
- PIO (programmed I/O)
- DMA (direct memory access)
# Device Driver
-  Per each device type
-  Responsible for device access, management and control
-  Provided by device manufacturers, per OS version
-  designed within an interface framework provided by OS version
# Type of Device
- Block: disk
	- Read / write blocks of data
	- Direct access to arbitrary block
- Character: keyboard
	- Get/put char
- Network device
- Virtual device
	- /dev/null
	- /dev/random

# Typical Device Access
![[device_access.png]]
# OS Bypass
![[device_bypass_OS.png]]
# Block Device Stack
Generic block layer: to provide a standard for an OS to all block devices
![[gejneric_block_layer.png]]
# Virtual File System
![[virtual_file_system.png]]
-  File == elements on which the VFS operates
-  File descriptor == OS representation of file
-  Inode == index of file blocks
-  Dentry == directory entry
-  Superblocks == filesystem specific information regarding the FS layout