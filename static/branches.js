var branches = document.getElementById("branches_list");

// generate dropdown from the list here
branches_list.forEach(function(branch){
    var opt = document.createElement("option");
    if (branches_list.indexOf(branch) == 0) {
        opt.selected = true;
    }
    opt.setAttribute("value", branch["name"]);
    opt.textContent = branch["name"];

    branches.appendChild(opt);
})

// watch for change here
branches.addEventListener("change", function(){
    current_branches = branches.value;
    branches_list.forEach(function(branch){
        if (branch["name"] === current_branches) {
            current_url = branch["url"];
        }
    })
});