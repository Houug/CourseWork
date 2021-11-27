async function create_new_table(name) {
    return await eel.create_new_table(name)();
}

async function add_new_person(surname, name, departament, start_vac, end_vac, salary, non18child) {
    return await eel.add_new_person(surname, name, departament, start_vac, end_vac, salary, non18child)();
}

async function del_from_db(id) {
    return await eel.del_from_db(id)();
}

async function load_db() {
    return await eel.load_db()();
}