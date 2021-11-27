async function load() {
    let array = Array.from(await load_db());

    let old_table = document.getElementsByClassName("table").item(0);
    let old_content = document.querySelector("div.content");
    let new_content = document.createElement("div").;

    for (let arrayKey in array) {
        let new_row = document.createElement("tr");
        for (let val in array[arrayKey]) {

            let new_id = document.createElement("td");
            let new_id_text;
            if (typeof array[arrayKey][val] == "string") {
                new_id_text = document.createTextNode(array[arrayKey][val].replace("\u0000", ""));
            } else {
                new_id_text = document.createTextNode(array[arrayKey][val]);
            }

            new_id.appendChild(new_id_text);
            new_row.appendChild(new_id);
        }
        new_content.appendChild(new_row);
    }
    old_content.replaceWith(new_content);
}

document.addEventListener("DOMContentLoaded", async function () {
    await create_new_table("Main_Table");
    await load()
});
document.getElementsByClassName("reload")[0].addEventListener("click", load);