// Function to format numbers to 2 decimal places
function formatNumber(num) {
    return Number(num).toFixed(2);
}

// Function to update the timestamp
function updateTimestamp() {
    const now = new Date();
    document.getElementById('last-update').textContent = now.toLocaleString();
}

// Function to fetch and update metrics
async function fetchMetrics() {
    try {
        // Fetch CPU metrics
        const cpuResponse = await fetch('/api/metrics/cpu');
        if (!cpuResponse.ok) throw new Error(`CPU metrics failed: ${cpuResponse.statusText}`);
        const cpuData = await cpuResponse.json();
        
        // Fetch Memory metrics
        const memoryResponse = await fetch('/api/metrics/memory');
        if (!memoryResponse.ok) throw new Error(`Memory metrics failed: ${memoryResponse.statusText}`);
        const memoryData = await memoryResponse.json();
        
        // Fetch Disk metrics
        const diskResponse = await fetch('/api/metrics/disk');
        if (!diskResponse.ok) throw new Error(`Disk metrics failed: ${diskResponse.statusText}`);
        const diskData = await diskResponse.json();
        
        // Update CPU metrics
        document.getElementById('cpu-percent').textContent = formatNumber(cpuData.cpu_percent);
        
        // Update Memory metrics
        document.getElementById('memory-percent').textContent = formatNumber(memoryData.percent);
        document.getElementById('memory-total').textContent = formatNumber(memoryData.total_gb);
        document.getElementById('memory-used').textContent = formatNumber(memoryData.used_gb);
        document.getElementById('memory-free').textContent = formatNumber(memoryData.free_gb);
        
        // Update Disk metrics
        document.getElementById('disk-percent').textContent = formatNumber(diskData.percent);
        document.getElementById('disk-total').textContent = formatNumber(diskData.total_gb);
        document.getElementById('disk-used').textContent = formatNumber(diskData.used_gb);
        document.getElementById('disk-free').textContent = formatNumber(diskData.free_gb);
        
        // Update timestamp
        updateTimestamp();
        
        // Reset error styling
        document.querySelectorAll('.metric-card span').forEach(span => {
            span.style.color = '';
        });
    } catch (error) {
        console.error('Error fetching metrics:', error);
        // Show error state in UI
        document.querySelectorAll('.metric-card span').forEach(span => {
            span.textContent = 'Error';
            span.style.color = '#e74c3c';
        });
    }
}

// Function to fetch and update system specs
async function fetchSpecs() {
    try {
        const res = await fetch('/api/specs');
        if (!res.ok) throw new Error(`Specs fetch failed: ${res.statusText}`);
        const specs = await res.json();
        document.getElementById('spec-hostname').textContent = specs.hostname;
        document.getElementById('spec-os').textContent = specs.os;
        document.getElementById('spec-os-version').textContent = specs.os_version;
        document.getElementById('spec-cpu').textContent = specs.cpu;
        document.getElementById('spec-cores').textContent = specs.cpu_cores;
        document.getElementById('spec-threads').textContent = specs.cpu_threads;
        document.getElementById('spec-ram').textContent = formatNumber(specs.total_ram_gb);
        document.getElementById('spec-disk').textContent = formatNumber(specs.total_disk_gb);
        document.getElementById('spec-uptime').textContent = specs.uptime;
    } catch (error) {
        console.error('Error fetching specs:', error);
        document.querySelectorAll('.specs-card span[id^="spec-"]').forEach(span => {
            span.textContent = 'Error';
        });
    }
}

// Function to fetch and display warnings
async function fetchWarnings() {
    try {
        const res = await fetch('/api/warnings');
        const data = await res.json();
        const banner = document.getElementById('warning-banner');
        if (data.warnings && data.warnings.length > 0) {
            banner.style.display = '';
            banner.innerHTML = data.warnings.map(w => `<span>⚠️ ${w}</span>`).join('<br>');
        } else {
            banner.style.display = 'none';
            banner.innerHTML = '';
        }
    } catch (e) {
        // Hide banner on error
        document.getElementById('warning-banner').style.display = 'none';
    }
}

// Function to fetch and display network info
async function fetchNetwork() {
    try {
        const res = await fetch('/api/network');
        const net = await res.json();
        document.getElementById('net-private-ip').textContent = net.private_ip || 'N/A';
        document.getElementById('net-public-ip').textContent = net.public_ip || 'N/A';
        document.getElementById('net-bytes-sent').textContent = net.bytes_sent;
        document.getElementById('net-bytes-recv').textContent = net.bytes_recv;
        document.getElementById('net-packets-sent').textContent = net.packets_sent;
        document.getElementById('net-packets-recv').textContent = net.packets_recv;
        document.getElementById('net-active-conns').textContent = net.active_connections;
    } catch (e) {
        document.querySelectorAll('.network-card span[id^="net-"]').forEach(span => span.textContent = 'Error');
    }
}

// Function to fetch and display top processes
async function fetchProcesses() {
    try {
        const res = await fetch('/api/processes');
        const data = await res.json();
        document.getElementById('proc-total').textContent = data.total_processes;
        document.getElementById('proc-uptime').textContent = data.top_process_uptime || 'N/A';
        // Top CPU
        const cpuTable = document.getElementById('proc-cpu-table');
        cpuTable.innerHTML = '';
        data.top_cpu.forEach(proc => {
            cpuTable.innerHTML += `<tr><td>${proc.name}</td><td>${proc.pid}</td><td>${proc.cpu_percent}</td></tr>`;
        });
        // Top Mem
        const memTable = document.getElementById('proc-mem-table');
        memTable.innerHTML = '';
        data.top_mem.forEach(proc => {
            memTable.innerHTML += `<tr><td>${proc.name}</td><td>${proc.pid}</td><td>${proc.memory_percent.toFixed(2)}</td></tr>`;
        });
    } catch (e) {
        document.getElementById('proc-total').textContent = 'Error';
        document.getElementById('proc-uptime').textContent = 'Error';
        document.getElementById('proc-cpu-table').innerHTML = '<tr><td colspan="3">Error</td></tr>';
        document.getElementById('proc-mem-table').innerHTML = '<tr><td colspan="3">Error</td></tr>';
    }
}

// Function to refresh metrics (called by button click)
function refreshMetrics() {
    const button = document.querySelector('.refresh-button');
    button.textContent = 'Refreshing...';
    button.disabled = true;
    
    fetchMetrics().finally(() => {
        button.textContent = 'Refresh Metrics';
        button.disabled = false;
    });
}

// Initial load
fetchWarnings();
fetchMetrics();
fetchSpecs();
fetchNetwork();
fetchProcesses();

// Auto-refresh every 30 seconds
setInterval(fetchWarnings, 30000);
setInterval(fetchMetrics, 30000);
setInterval(fetchSpecs, 30000);
setInterval(fetchNetwork, 30000);
setInterval(fetchProcesses, 30000); 