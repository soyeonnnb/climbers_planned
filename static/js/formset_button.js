const placeFormset = document.querySelector("#placeformset");
const add_button = document.querySelector(".placeformset_add_button");
const del_button = document.querySelector(".placeformset_del_button");
const add_place_button = document.querySelector(".placeformset_add_place_button");
const inputTotalForm = document.querySelector("#id_places-TOTAL_FORMS");
let placeFormsetNumber = 1;

function makeFormsetP(number, name, address, latLng){
    const p = document.createElement("p");
    // label 생성
    const label_name = document.createElement("label");
    label_name.for = `places-${number}-name`
    label_name.innerText="Name: "
    // input - name 생성
    const input_name = document.createElement("input");
    input_name.type = "text";
    input_name.name = `places-${number}-name`;
    input_name.id=`id_places-${number}-name`
    input_name.value=name;
    // input - latitude 생성
    const input_lat = document.createElement("input");
    input_lat.type = "hidden";
    input_lat.name = `places-${number}-latitude`;
    input_lat.step = "any";
    input_lat.id = `id_places-${number}-latitude`;
    input_lat.value = latLng[0];

    // input - longitude 생성
    const input_lng = document.createElement("input");
    input_lng.type = "hidden";
    input_lng.name = `places-${number}-longitude`;
    input_lng.step = "any";
    input_lng.id = `id_places-${number}-longitude`;
    input_lng.value = latLng[1];

    // input type="hidden" 생성
    const inputHidden = document.createElement("input");
    inputHidden.type = "hidden";
    inputHidden.name=`places-${number}-id`;
    inputHidden.id = `id_places-${number}-id`;
    // 삭제 button 생성
    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", formsetDel);
    p.appendChild(label_name);
    p.appendChild(input_name);
    p.appendChild(input_lat);
    p.appendChild(input_lng);
    p.appendChild(inputHidden);
    p.appendChild(button);
    return p;
}

// + 버튼 클릭시 폼 생성
function formsetAdd(){
    var formAddName = document.getElementById("click-result__name").innerText;
    var formAddAddress = document.getElementById("click-result__address").innerText;
    var latLng = document.getElementById("addplace_latlng").innerText;
    if (!latLng || latLng === ""){
        alert("지도에서 여행지를 선택해주세요");
        return false;
    }
    latLng = latLng.replace("(", "");
    latLng = latLng.replace(")", "");
    latLng = latLng.replace(" ", "");
    latLng = latLng.split(",");
    const p = makeFormsetP(placeFormsetNumber, formAddName, formAddAddress, latLng);
    placeFormsetNumber ++ ;
    inputTotalForm.value = placeFormsetNumber;
    placeFormset.appendChild(p);
    formAddName.innerText = "";
    formAddAddress.innerText = "";
    latLng = "";
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
// add_place_button.addEventListener("click", formsetAddPlace);