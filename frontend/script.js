let rawIncidents = [];
let sortKey = "";
let sortAsc = true;

// Active filters
let activeFilters = {
    device: "",
    severity: "",
    cause: ""
};

document.addEventListener("DOMContentLoaded", () => {
    fetchAlertData();
    setInterval(fetchAlertData, 5000);

    // Global Search
    document.getElementById("search-input").addEventListener("input", renderTable);

    // Dropdown Filters
    document.getElementById("filter-device").addEventListener("change", (e) => {
        activeFilters.device = e.target.value;
        renderTable();
    });
    document.getElementById("filter-severity").addEventListener("change", (e) => {
        activeFilters.severity = e.target.value;
        renderTable();
    });
    document.getElementById("filter-cause").addEventListener("change", (e) => {
        activeFilters.cause = e.target.value;
        renderTable();
    });

    // Sorting functionality.
    document.querySelectorAll("th[data-sort]").forEach(th => {
        th.addEventListener("click", () => {
            const key = th.getAttribute("data-sort");
            if (sortKey === key) {
                sortAsc = !sortAsc;
            } else {
                sortKey = key;
                sortAsc = true;
            }
            renderTable();
        });
    });
});

function fetchAlertData() {
    fetch('http://127.0.0.1:5000/process-alerts')
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            updateDashboardMetrics(data);
            rawIncidents = data.incidents;
            populateDropdowns();
            renderTable();
        })
        .catch(error => {
            console.error("Error fetching data: ", error);
        });
}

function updateDashboardMetrics(data) {
    document.getElementById("total-alerts").innerText = data.total_alerts;
    document.getElementById("total-incidents").innerText = data.total_incidents;
    document.getElementById("noise-reduction").innerText = data.reduction;
    
    const now = new Date();
    document.getElementById("last-updated").innerText = now.toLocaleTimeString();
}

function populateDropdowns() {
    // Only populate if not currently focused so we don't interrupt the user
    if (document.activeElement.tagName === "SELECT") return;

    const deviceSelect = document.getElementById("filter-device");
    const causeSelect = document.getElementById("filter-cause");

    // Extract unique sorted lists
    const uniqueDevices = [...new Set(rawIncidents.map(i => i.device))].sort();
    const uniqueCauses = [...new Set(rawIncidents.map(i => i.root_cause))].sort();

    // Preserve current selection
    const currentDevice = deviceSelect.value;
    const currentCause = causeSelect.value;

    // Reset options
    deviceSelect.innerHTML = '<option value="">All Devices</option>';
    causeSelect.innerHTML = '<option value="">All Causes</option>';

    uniqueDevices.forEach(device => {
        const opt = document.createElement("option");
        opt.value = device;
        opt.innerText = device;
        if (device === currentDevice) opt.selected = true;
        deviceSelect.appendChild(opt);
    });

    uniqueCauses.forEach(cause => {
        const opt = document.createElement("option");
        opt.value = cause;
        opt.innerText = cause;
        if (cause === currentCause) opt.selected = true;
        causeSelect.appendChild(opt);
    });
}

function renderTable() {
    const tbody = document.getElementById("table-body");
    const filterQuery = document.getElementById("search-input").value.toLowerCase();
    
    // Filtering Logic
    let displayIncidents = rawIncidents.filter(inc => {
        // Global text search
        const matchesSearch = (
            inc.device.toLowerCase().includes(filterQuery) ||
            inc.root_cause.toLowerCase().includes(filterQuery) ||
            inc.severity.toLowerCase().includes(filterQuery) ||
            inc.incident_id.toLowerCase().includes(filterQuery)
        );

        if (!matchesSearch) return false;

        // Dropdown specific filters
        if (activeFilters.device && inc.device !== activeFilters.device) return false;
        if (activeFilters.severity && inc.severity !== activeFilters.severity) return false;
        if (activeFilters.cause && inc.root_cause !== activeFilters.cause) return false;

        return true;
    });

    // Sorting Logic
    if (sortKey) {
        displayIncidents.sort((a, b) => {
            let valA = a[sortKey];
            let valB = b[sortKey];
            
            if (sortKey === "alerts_count") {
                valA = Number(valA);
                valB = Number(valB);
            } 
            else if (sortKey === "duration") {
                valA = parseInt(valA) || 0;
                valB = parseInt(valB) || 0;
            }
            else {
                valA = String(valA).toLowerCase();
                valB = String(valB).toLowerCase();
            }

            if (valA < valB) return sortAsc ? -1 : 1;
            if (valA > valB) return sortAsc ? 1 : -1;
            return 0;
        });
    }

    // Render HTML
    tbody.innerHTML = "";
    displayIncidents.forEach(inc => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td class="code-style">${inc.incident_id}</td>
            <td style="color: #fff; font-weight: 500;">${inc.device}</td>
            <td>${inc.start_time.substring(11)}</td>
            <td>${inc.alerts_count} alerts</td>
            <td><span class="sev-tag severity-${inc.severity}">${inc.severity}</span></td>
            <td>${inc.root_cause}</td>
            <td>${inc.duration}</td>
        `;
        tbody.appendChild(row);
    });
}
