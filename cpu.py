from pyembedded.raspberry_pi_tools.raspberrypi import PI

pi = PI()

info=""
with open('/sys/class/thermal/thermal_zone0/temp', 'r') as ftemp:
    current_temp = int(ftemp.read()) / 1000
    info=info+str(current_temp)+","+pi.get_ram_info()[0]+","+pi.get_ram_info()[1]+","+pi.get_ram_info()[2]+","+pi.get_disk_space()[0]+","+pi.get_disk_space()[1]+","+pi.get_disk_space()[2]+","+pi.get_disk_space()[3]+","+pi.get_cpu_usage()+" "
    print(info)
