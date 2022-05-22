const placeFormset = document.querySelector("#placeformset");
const add_button = document.querySelector(".placeformset_add_button");
const del_button = document.querySelector(".placeformset_del_button");
const add_place_button = document.querySelector(".placeformset_add_place_button");
const inputTotalForm = document.querySelector("#id_places-TOTAL_FORMS");
let placeFormsetNumber = 1;

function makeFormsetP(number){
    const p = document.createElement("p");
    // label 생성
    const label = document.createElement("label");
    label.for = `places-${number}-name`
    label.innerText="Name: "
    // input 생성
    const input = document.createElement("input");
    input.type = "text";
    input.name = `places-${number}-name`;
    input.id=`id_places-${number}-name`
    // input type="hidden" 생성
    const inputHidden = document.createElement("input");
    inputHidden.type = "hidden";
    inputHidden.name=`places-${number}-id`;
    inputHidden.id = `id_places-${number}-id`;
    // 삭제 button 생성
    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", formsetDel);
    p.appendChild(label);
    p.appendChild(input);
    p.appendChild(inputHidden);
    p.appendChild(button);
    return p;
}

// + 버튼 클릭시 폼 생성
function formsetAdd(){
    const p = makeFormsetP(placeFormsetNumber);
    placeFormsetNumber ++ ;
    inputTotalForm.value = placeFormsetNumber;
    placeFormset.appendChild(p);
}

// x 버튼 클릭시 폼 삭제
function formsetDel(event){
    const p = event.target.parentElement;
    p.remove();
}

function formsetAddPlace(){
    const p = makeFormsetP(placeFormsetNumber);
    placeFormsetNumber ++ ;
    inputTotalForm.value = placeFormsetNumber;
    placeFormset.appendChild(p);
}

add_button.addEventListener("click", formsetAdd);
del_button.addEventListener("click", formsetDel);
add_place_button.addEventListener("click", formsetAddPlace);

