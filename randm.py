import psutil

def number_rand(s):
        switch = psutil.cpu_stats().ctx_switches+s
        ineterppupts = psutil.cpu_stats().interrupts+s
        sysalls = psutil.cpu_stats().syscalls+s
        total = psutil.swap_memory().total+s
        used = psutil.swap_memory().used+s
        free = psutil.swap_memory().free+s
        bytes_recv = psutil.net_io_counters().bytes_recv+s
        packets_recv = psutil.net_io_counters().packets_recv+s
        i = switch + ineterppupts + sysalls + total + used + free + bytes_recv + packets_recv
        return i


a = number_rand(905)
print(a)