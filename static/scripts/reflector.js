const choose_date = document.getElementById("choose_date")

function revealer() {
    if (choose_date.style.display == "none"){
        choose_date.style.display = "block"
    } else if (choose_date.style.display == "block"){
        choose_date.style.display = "none"
    }
  }