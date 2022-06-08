const placeFormset = document.querySelector("#placeformset");
const place_button = document.querySelector(".placeformset_place_button");
const del_button = document.querySelector(".placeformset_del_button");
const inputTotalForm = document.querySelector("#id_places-TOTAL_FORMS");
const lodging_button = document.querySelector("#lodging_button");
let placeFormsetNumber = 1;


function makeFormsetP(number, name, address, lat, lng){
    const p = document.createElement("p");
    // label 생성
    const formSpan = document.createElement("span");
    formSpan.innerText = name;
    formSpan.className="textbar input";
    // input - name 생성
    const input_name = document.createElement("input");
    input_name.type = "hidden";
    input_name.name = `places-${number}-name`;
    input_name.id=`id_places-${number}-name`
    input_name.value=name;
    // input - latitude 생성
    const input_lat = document.createElement("input");
    input_lat.type = "hidden";
    input_lat.name = `places-${number}-latitude`;
    input_lat.step = "any";
    input_lat.id = `id_places-${number}-latitude`;
    input_lat.value = lat;

    // input - longitude 생성
    const input_lng = document.createElement("input");
    input_lng.type = "hidden";
    input_lng.name = `places-${number}-longitude`;
    input_lng.step = "any";
    input_lng.id = `id_places-${number}-longitude`;
    input_lng.value = lng;

    // input type="hidden" 생성
    const inputHidden = document.createElement("input");
    inputHidden.type = "hidden";
    inputHidden.name=`places-${number}-id`;
    inputHidden.id = `id_places-${number}-id`;
    // 삭제 button 생성
    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", formsetDel);
    p.appendChild(formSpan);
    p.appendChild(input_name);
    p.appendChild(input_lat);
    p.appendChild(input_lng);
    p.appendChild(inputHidden);
    p.appendChild(button);
    return p;
}

function cleanResult(){
    document.getElementById("click-result__name").innerText = "";
    document.getElementById("click-result__address").innerText = "";
    document.getElementById("click-result__lat").innerText = "";
    document.getElementById("click-result__lng").innerText ="";
}

// 여행지 추가 버튼 클릭시 폼 생성
function formsetAdd(){
    var formAddName = document.getElementById("click-result__name").innerText;
    var formAddAddress = document.getElementById("click-result__address").innerText;
    var formAddLat = document.getElementById("click-result__lat").innerText;
    var formAddLng = document.getElementById("click-result__lng").innerText;
    if (!formAddLat || formAddLat === ""){
        alert("지도에서 여행지를 선택해주세요");
        return false;
    }
    const p = makeFormsetP(placeFormsetNumber, formAddName, formAddAddress, formAddLat, formAddLng);
    placeFormsetNumber ++ ;
    inputTotalForm.value = placeFormsetNumber;
    placeFormset.appendChild(p);
    cleanResult();
}

// x 버튼 클릭시 폼 삭제
function formsetDel(event){
    const p = event.target.parentElement;
    p.remove();
}

function makeLodgingP(name, lat, lng){
    const p = document.createElement("p");
    // label 생성
    const formSpan = document.createElement("span");
    formSpan.innerText = name;
    formSpan.className="textbar input";
    // input - name 생성
    const input_name = document.createElement("input");
    input_name.type = "hidden";
    input_name.name = "lodging-name";
    input_name.id="id_lodging-name";
    input_name.value=name;
    // input - latitude 생성
    const input_lat = document.createElement("input");
    input_lat.type = "hidden";
    input_lat.name = "lodging-latitude";
    input_lat.step = "any";
    input_lat.id = "id_lodging-latitude";
    input_lat.value = lat;

    // input - longitude 생성
    const input_lng = document.createElement("input");
    input_lng.type = "hidden";
    input_lng.name = "lodging-longitude";
    input_lng.step = "any";
    input_lng.id = "id_lodging-longitude";
    input_lng.value = lng;

    p.appendChild(formSpan);
    p.appendChild(input_name);
    p.appendChild(input_lat);
    p.appendChild(input_lng);
    
    return p;

}

function lodgingAdd(){
    var formAddName = document.getElementById("click-result__name").innerText;
    var formAddAddress = document.getElementById("click-result__address").innerText;
    var formAddLat = document.getElementById("click-result__lat").innerText;
    var formAddLng = document.getElementById("click-result__lng").innerText;
    var lodging_form = document.querySelector("#lodging_form");
    if (!formAddLat || formAddLat === ""){
        alert("지도에서 숙소를 선택해주세요");
        return false;
    }
    if (lodging_form.firstChild.nodeName !== "#text"){
        var ans = confirm("이미 숙소를 선택하였습니다. 숙소를 변경하시겠습니까?");
        if (!ans) {
            return false;
        }
    }
    p = makeLodgingP(formAddName,formAddLat,formAddLng);
    lodging_form.innerHTML = "";
    lodging_form.appendChild(p);
    cleanResult();
}

place_button.addEventListener("click", formsetAdd);
lodging_button.addEventListener("click", lodgingAdd);