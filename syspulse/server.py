from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import psutil
import os
from pathlib import Path
import platform
import datetime
import socket
import requests

app = FastAPI(title="SysPulse", description="System Monitoring Tool")

# Get the package directory
PACKAGE_DIR = Path(__file__).parent

# Mount static files
app.mount("/static", StaticFiles(directory=PACKAGE_DIR / "static"), name="static")

# Setup templates
templates = Jinja2Templates(directory=str(PACKAGE_DIR / "templates"))

def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/health")
def read_health():
    return {"status": "OK", "message": "SysPulse is live!"}

@app.get("/api/metrics/cpu")
def get_cpu_metrics():
    # Call once to initialize, then again for real value
    psutil.cpu_percent(interval=0.1)
    cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
    return {"cpu_percent": cpu_percent}

@app.get("/api/metrics/memory")
def get_memory_metrics():
    mem = psutil.virtual_memory()
    return {
        "total_gb": bytes_to_gb(mem.total),
        "used_gb": bytes_to_gb(mem.used),
        "free_gb": bytes_to_gb(mem.available),
        "percent": mem.percent,
    }

@app.get("/api/metrics/disk")
def get_disk_metrics():
    if platform.system() == "Windows":
        partition = "C:\\"
    else:
        partition = "/"
    usage = psutil.disk_usage(partition)
    return {
        "total_gb": bytes_to_gb(usage.total),
        "used_gb": bytes_to_gb(usage.used),
        "free_gb": bytes_to_gb(usage.free),
        "percent": usage.percent,
    }

@app.get("/api/specs")
def get_specs():
    uname = platform.uname()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    return {
        "hostname": socket.gethostname(),
        "os": f"{uname.system} {uname.release}",
        "os_version": uname.version,
        "cpu": uname.processor or platform.processor(),
        "cpu_cores": psutil.cpu_count(logical=False),
        "cpu_threads": psutil.cpu_count(logical=True),
        "total_ram_gb": bytes_to_gb(psutil.virtual_memory().total),
        "total_disk_gb": bytes_to_gb(psutil.disk_usage('/') .total),
        "uptime": str(uptime).split('.')[0],
    }

@app.get("/api/network")
def get_network_info():
    # Private IP
    private_ip = socket.gethostbyname(socket.gethostname())
    # Public IP
    try:
        public_ip = requests.get('https://api.ipify.org').text
    except Exception:
        public_ip = None
    # Network stats
    net_io = psutil.net_io_counters()
    # Active connections
    active_conns = len(psutil.net_connections())
    return {
        "private_ip": private_ip,
        "public_ip": public_ip,
        "bytes_sent": net_io.bytes_sent,
        "bytes_recv": net_io.bytes_recv,
        "packets_sent": net_io.packets_sent,
        "packets_recv": net_io.packets_recv,
        "active_connections": active_conns
    }

@app.get("/api/processes")
def get_top_processes():
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'create_time']):
        try:
            procs.append(p.info)
        except Exception:
            continue
    # Top 5 by CPU
    top_cpu = sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    # Top 5 by memory
    top_mem = sorted(procs, key=lambda x: x['memory_percent'], reverse=True)[:5]
    # Most resource-intensive process uptime
    if top_cpu:
        now = datetime.datetime.now()
        uptime = now - datetime.datetime.fromtimestamp(top_cpu[0]['create_time'])
        uptime_str = str(uptime).split('.')[0]
    else:
        uptime_str = None
    return {
        "top_cpu": top_cpu,
        "top_mem": top_mem,
        "total_processes": len(procs),
        "top_process_uptime": uptime_str
    }

@app.get("/api/warnings")
def get_warnings():
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\" if platform.system() == "Windows" else "/")
    warnings = []
    if mem.percent > 90:
        warnings.append(f"High memory usage: {mem.percent}%")
    if disk.percent > 90:
        warnings.append(f"High disk usage: {disk.percent}%")
    # Uptime warning (e.g., > 30 days)
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = (datetime.datetime.now() - boot_time).days
    if uptime > 30:
        warnings.append(f"System uptime is {uptime} days. Consider a reboot.")
    return {"warnings": warnings} 