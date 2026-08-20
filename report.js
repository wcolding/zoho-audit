// Hides all report content
function hideReports() {
    reports = document.getElementsByClassName("report_content");
    Array.from(reports).forEach((section) => {
        section.style.display = "none";
    });
}

// Shows specfied report content
function showReport(event, report) {
    hideReports();
    content = document.getElementById(report);
    content.style.display = "grid";
}