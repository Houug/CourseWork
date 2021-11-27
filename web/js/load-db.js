document.getElementsByClassName("reload")[0].addEventListener("click", async function () {
    let array = Array.from(await load_db());
    console.log(array);

    let table = document.getElementsByClassName("table").item(0);
    for (let arrayKey in array) {
        console.log(arrayKey);
        let new_row = document.createElement("tr");
        for (let arrayKeyKey in arrayKey) {

            let new_id = document.createElement("td");
            let new_id_text = document.createTextNode(arrayKeyKey);
            new_id.appendChild(new_id_text);
            new_row.appendChild(new_id);
        }

/*
        let new_surname = document.createElement("td");
        let new_surname_text = document.createTextNode(arrayKey['Фамилия'].toString());
        new_surname.appendChild(new_surname_text);
        new_row.appendChild(new_surname);

        let new_name = document.createElement("td");
        let new_name_text = document.createTextNode(arrayKey['Имя'].toString());
        new_name.appendChild(new_name_text);
        new_row.appendChild(new_name);

        let new_depart = document.createElement("td");
        let new_depart_text = document.createTextNode(arrayKey['Отдел'].toString());
        new_depart.appendChild(new_depart_text);
        new_row.appendChild(new_depart);

        let new_start_vac = document.createElement("td");
        let new_start_vac_text = document.createTextNode(arrayKey['Начало отпуска'].toString());
        new_start_vac.appendChild(new_start_vac_text);
        new_row.appendChild(new_start_vac);

        let new_end_vac = document.createElement("td");
        let new_end_vac_text = document.createTextNode(arrayKey['Конец отпуска'].toString());
        new_end_vac.appendChild(new_end_vac_text);
        new_row.appendChild(new_end_vac);
*/
        table.appendChild(new_row);
    }

})
$(window).resize(function () {
    let table = document.getElementsByClassName("table").item(0);
    let new_row = document.createElement("tr");
    let new_elem = document.createElement("td");
    let new_text = document.createTextNode("4");
    new_elem.appendChild(new_text);
    new_row.appendChild(new_elem);
    new_row.appendChild(new_elem.appendChild(document.createElement("td")));
    new_row.appendChild(new_elem.appendChild(document.createElement("td")));
    new_row.appendChild(new_elem.appendChild(document.createElement("td")));
    new_row.appendChild(new_elem.appendChild(document.createElement("td")));
    new_row.appendChild(new_elem.appendChild(document.createElement("td")));
    new_row.appendChild(new_elem.appendChild(document.createElement("td")));
    new_row.appendChild(new_elem.appendChild(document.createElement("td")));

    table.appendChild(new_row);
    table.getElementsByTagName("td").item(0);

    let arr = create_new_table("Main_Table");
    add_new_person("jjjjj", "dsd", "asd", "21-12-2001", "21-2-2002", 1000, false);
    //let a = load_db();
    console.log(a);

})