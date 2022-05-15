const placeFormset = document.querySelector("#placeformset");
const add_button = document.querySelector(".placeformset_add_button");
const del_button = document.querySelector(".placeformset_del_button");
const inputTotalForm = document.querySelector("#id_places-TOTAL_FORMS");
let placeFormsetNumber = 1;

function makeFormsetP(number){
    const p = document.createElement("p");
    const label = document.createElement("label");
    label.for = `places-${number}-name`
    label.innerText="Name: "
    const input = document.createElement("input");
    input.type = "text";
    input.name = `places-${number}-name`;
    input.id=`id_places-${number}-name`
    const inputHidden = document.createElement("input");
    inputHidden.type = "hidden";
    inputHidden.name=`places-${number}-id`;
    inputHidden.id = `id_places-${number}-id`;
    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", formsetDel);
    p.appendChild(label);
    p.appendChild(input);
    p.appendChild(inputHidden);
    p.appendChild(button);
    return p;
}

function formsetAdd(){
    const p = makeFormsetP(placeFormsetNumber);
    placeFormsetNumber ++ ;
    inputTotalForm.value = placeFormsetNumber;
    placeFormset.appendChild(p);
}
function formsetDel(event){
    const p = event.target.parentElement;
    p.style.display = "none";

    p.remove();
}

add_button.addEventListener("click", formsetAdd);
del_button.addEventListener("click", formsetDel);


