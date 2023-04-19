const spec_tag = [
    "platform",
    "processor",
    "total_ram",
    "platform_release",
    "platform_version",
    "architecture",
    "hostname",
    "ip_address",
    "mac_address",
]

const temp_tag = [
    "cpu_temp",
    "gpu_temp",
    "disk_temp",
]

function update_specs() {
    let request = new XMLHttpRequest();
    request.open("GET", current_url + "/specs");
    request.send();
    
    request.onload = function() {
        var data = JSON.parse(this.response)
        if (request.status >= 200 && request.status < 400) {
            spec_tag.forEach(
                (tag) => {
                    var html_id_tag = "spec_" + tag;
                    document.getElementById(html_id_tag).innerHTML = data[tag]
                }
            )
        }
    }
}

function update_temp() {
    let request = new XMLHttpRequest();
    request.open("GET", current_url + "/sensors");
    request.send();
    
    request.onload = function() {
        var data = JSON.parse(this.response)
        if (request.status >= 200 && request.status < 400) {
            temp_tag.forEach(
                (tag) => {
                    var html_id_tag = tag;
                    document.getElementById(html_id_tag).innerHTML = data[tag]
                }
            )
        }
    }
}

update_specs();
update_temp();
setInterval(update_specs, 60*1000);
setInterval(update_temp, interval*1000);